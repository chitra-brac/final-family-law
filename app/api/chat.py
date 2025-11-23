"""
Chat API Endpoint
Handles user chat interactions with the legal chatbot
"""

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
import time
import structlog
import uuid

from app.services.llm_service import get_llm_service
from app.services.supabase_service import get_supabase_service

logger = structlog.get_logger()

router = APIRouter()


class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    message: str = Field(..., min_length=1, max_length=2000, description="User's message")
    session_id: Optional[str] = Field(None, description="Session ID for conversation continuity")


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    response: str = Field(..., description="Chatbot's response")
    session_id: str = Field(..., description="Session ID")
    tools_used: List[Dict[str, Any]] = Field(default_factory=list, description="Tools that were called")
    tokens_used: int = Field(..., description="Total tokens consumed")
    model: str = Field(..., description="Model used")
    response_time_ms: int = Field(..., description="Response time in milliseconds")
    success: bool = Field(..., description="Whether the request was successful")


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat with the legal chatbot

    - **message**: User's query in Bengali or English
    - **session_id**: Optional session ID for multi-turn conversations

    Returns the chatbot's response with legal advice
    """
    start_time = time.time()

    # Generate session ID if not provided
    session_id = request.session_id or str(uuid.uuid4())

    logger.info(
        "chat_request_received",
        session_id=session_id,
        message_length=len(request.message)
    )

    try:
        # Get services
        llm_service = get_llm_service()
        supabase_service = get_supabase_service()

        # Store user message
        supabase_service.store_message(
            session_id=session_id,
            role="user",
            content=request.message
        )

        # Get conversation history
        conversation_history = supabase_service.get_conversation_history(
            session_id=session_id,
            limit=10  # Last 10 messages for context
        )

        # Call LLM with tools
        result = llm_service.chat(
            user_message=request.message,
            conversation_history=conversation_history[:-1]  # Exclude the message we just added
        )

        # Calculate response time
        response_time_ms = int((time.time() - start_time) * 1000)

        if not result["success"]:
            logger.error(
                "chat_llm_error",
                session_id=session_id,
                error=result.get("error")
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=result.get("error", "Failed to generate response")
            )

        # Store assistant response
        supabase_service.store_message(
            session_id=session_id,
            role="assistant",
            content=result["response"]
        )

        # Detect intent from tools used
        intent_detected = None
        if result["tools_used"]:
            for tool_use in result["tools_used"]:
                if tool_use["tool"] == "get_legal_knowledge":
                    intent_detected = tool_use["args"].get("intent")
                    break

        # Calculate total sections retrieved
        total_sections = sum(
            tool["sections_count"]
            for tool in result["tools_used"]
            if "sections_count" in tool
        )

        # Log analytics
        supabase_service.log_analytics(
            session_id=session_id,
            user_query=request.message,
            intent_detected=intent_detected,
            tools_used=result["tools_used"],
            sections_retrieved=total_sections,
            tokens_used=result["tokens_used"],
            response_time_ms=response_time_ms,
            model=result["model"],
            success=True
        )

        logger.info(
            "chat_response_sent",
            session_id=session_id,
            intent=intent_detected,
            tools_count=len(result["tools_used"]),
            tokens=result["tokens_used"],
            response_time_ms=response_time_ms
        )

        return ChatResponse(
            response=result["response"],
            session_id=session_id,
            tools_used=result["tools_used"],
            tokens_used=result["tokens_used"],
            model=result["model"],
            response_time_ms=response_time_ms,
            success=True
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(
            "chat_error",
            session_id=session_id,
            error=str(e),
            error_type=type(e).__name__
        )

        # Log failed analytics
        try:
            supabase_service.log_analytics(
                session_id=session_id,
                user_query=request.message,
                success=False,
                error_message=str(e)
            )
        except:
            pass

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "ain-bandhu-legal-chatbot",
        "version": "1.0.0"
    }


@router.get("/analytics/intents")
async def get_intent_analytics():
    """Get analytics grouped by intent"""
    try:
        supabase_service = get_supabase_service()
        analytics = supabase_service.get_intent_analytics()
        return {
            "success": True,
            "data": analytics
        }
    except Exception as e:
        logger.error("analytics_error", error=str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve analytics: {str(e)}"
        )
