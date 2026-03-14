"""
Main FastAPI application
Family Law Assistant for Bangladeshi Women
"""

import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uuid
import structlog

from app.config import get_settings
from app.models import (
    ChatRequest,
    ChatResponse,
    NewSessionResponse,
    HealthResponse,
)
from app.services.data_loader import get_data_loader
from app.services.llm_service import get_llm_service
from app.services.supabase_service import get_supabase_service

# Initialize settings and logger
settings = get_settings()
logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown lifecycle."""
    logger.info("app_starting", app=settings.app_name, version=settings.app_version)

    # Pre-load data
    get_data_loader()
    logger.info("data_loaded")

    # Initialize LLM service
    try:
        llm_service = get_llm_service()
        logger.info("llm_service_ready", model=llm_service.model)
    except Exception as e:
        logger.warning("llm_service_init_warning", error=str(e))

    # Initialize Supabase
    supabase_service = get_supabase_service()
    if supabase_service.client:
        logger.info("supabase_connected")
    else:
        logger.warning("supabase_not_configured", message="Using in-memory storage")

    yield

    logger.info("app_shutting_down", app=settings.app_name)


# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered family law assistant chatbot for Bangladeshi women",
    docs_url="/docs" if settings.debug else None,
    redoc_url="/redoc" if settings.debug else None,
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        version=settings.app_version,
    )


@app.post("/chat/new", response_model=NewSessionResponse)
async def create_new_session():
    """
    Create a new chat session.
    Returns a unique session ID and greeting message.
    """
    session_id = str(uuid.uuid4())

    return NewSessionResponse(
        session_id=session_id,
        greeting="আসসালামু আলাইকুম। আমি আপনার পারিবারিক আইন সহায়ক। আপনি কি ধরনের আইনি সমস্যার মুখোমুখি?",
    )


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint.
    Processes user message and returns AI response.

    Flow:
    1. Fetch conversation history from Supabase (up to 50 messages)
    2. Call LLM with history + current message
    3. Store user message and assistant response
    """
    start_time = time.time()
    session_id = request.session_id

    try:
        supabase_service = get_supabase_service()
        llm_service = get_llm_service()

        # Get conversation history (up to 50 messages)
        history = supabase_service.get_conversation_history(
            profile_id=session_id,
            limit=50
        )

        # Call LLM with tools
        result = llm_service.chat(
            user_message=request.message,
            conversation_history=history
        )

        if not result["success"]:
            raise HTTPException(
                status_code=500,
                detail=result.get("error", "Failed to generate response")
            )

        # Store user message and assistant response
        supabase_service.store_message(
            profile_id=session_id,
            role="user",
            content=request.message
        )
        supabase_service.store_message(
            profile_id=session_id,
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
        response_time_ms = int((time.time() - start_time) * 1000)
        supabase_service.log_analytics(
            profile_id=session_id,
            user_query=request.message,
            intent_detected=intent_detected,
            tools_used=result["tools_used"],
            sections_retrieved=total_sections,
            tokens_used=result["tokens_used"],
            response_time_ms=response_time_ms,
            model=result["model"],
            success=True
        )

        return ChatResponse(
            session_id=session_id,
            response=result["response"],
            intent=intent_detected,
            tools_used=[tool["tool"] for tool in result["tools_used"]],
        )

    except HTTPException:
        raise
    except Exception as e:
        # Log failed analytics
        try:
            supabase_service.log_analytics(
                profile_id=session_id,
                user_query=request.message,
                success=False,
                error_message=str(e)
            )
        except Exception:
            pass

        raise HTTPException(
            status_code=500,
            detail="An internal error occurred. Please try again."
        )


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler."""
    logger.error("unhandled_exception", error=str(exc), error_type=type(exc).__name__)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "দুঃখিত, একটি সমস্যা হয়েছে। অনুগ্রহ করে আবার চেষ্টা করুন।",
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
