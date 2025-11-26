"""
Main FastAPI application
Ain Bandhu - AI Legal Assistant for Bangladeshi Women
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uuid
from datetime import datetime
import structlog

from app.config import get_settings
from app.models import (
    ChatRequest,
    ChatResponse,
    NewSessionRequest,
    NewSessionResponse,
    HealthResponse,
)

# Initialize settings and logger
settings = get_settings()
logger = structlog.get_logger()

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered legal assistant chatbot for underprivileged Bangladeshi women",
    docs_url="/docs" if settings.debug else None,  # Disable docs in production
    redoc_url="/redoc" if settings.debug else None,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """
    Startup event - load data, initialize services
    """
    print(f"Starting {settings.app_name} v{settings.app_version}")

    # Initialize services (lazy loading on first use)
    from app.services.data_loader import get_data_loader
    from app.services.llm_service import get_llm_service
    from app.services.supabase_service import get_supabase_service

    # Pre-load data
    data_loader = get_data_loader()
    print("✓ Data loaded into memory")

    # Initialize LLM service
    try:
        llm_service = get_llm_service()
        print(f"✓ LLM service initialized ({llm_service.model})")
    except Exception as e:
        print(f"⚠ LLM service initialization warning: {e}")

    # Initialize Supabase
    supabase_service = get_supabase_service()
    if supabase_service.client:
        print("✓ Supabase connected")
    else:
        print("⚠ Supabase not configured (using in-memory storage)")


@app.on_event("shutdown")
async def shutdown_event():
    """
    Shutdown event - cleanup
    """
    print(f"Shutting down {settings.app_name}")


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint
    """
    return HealthResponse(
        status="healthy",
        version=settings.app_version,
    )


@app.post("/chat/new", response_model=NewSessionResponse)
async def create_new_session(request: NewSessionRequest):
    """
    Create a new chat session
    Returns a unique session ID and greeting message
    """
    session_id = str(uuid.uuid4())

    # TODO: Store session in Supabase

    return NewSessionResponse(
        session_id=session_id,
        greeting="আসসালামু আলাইকুম। আমি আইন বন্ধু, আপনার আইনি সহায়ক। আপনি কি ধরনের আইনি সমস্যার মুখোমুখি?",
    )


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint
    Processes user message and returns AI response

    Flow:
    1. Get conversation history from Supabase (up to 50 messages)
    2. Smart context windowing: if > 10 messages, summarize old ones
    3. Send message to OpenAI with tools
    4. Execute tools if called
    5. Store conversation in Supabase
    6. Return response
    """
    import time
    from app.services.llm_service import get_llm_service
    from app.services.supabase_service import get_supabase_service

    start_time = time.time()
    profile_id = request.session_id  # Using session_id as profile_id for now (frontend compatibility)

    try:
        llm_service = get_llm_service()
        supabase_service = get_supabase_service()

        # Store user message
        supabase_service.store_message(
            profile_id=profile_id,
            role="user",
            content=request.message
        )

        # Get conversation history (up to 50 messages)
        all_messages = supabase_service.get_conversation_history(
            profile_id=profile_id,
            limit=50
        )

        # Exclude the message we just added
        history = all_messages[:-1] if all_messages else []

        # Smart context windowing: summarize old messages if > 10
        if len(history) > 10:
            # Split into old (to summarize) and recent (keep verbatim)
            old_messages = history[:-10]
            recent_messages = history[-10:]

            # Generate summary of old messages
            summary = llm_service.summarize_conversation(old_messages)

            # Prepare context: summary as system message + recent messages
            conversation_history = [
                {"role": "system", "content": f"পূর্ববর্তী কথোপকথনের সংক্ষিপ্তসার:\n{summary}"}
            ] + recent_messages

            logger.info(
                "context_summarized",
                profile_id=profile_id,
                old_messages_count=len(old_messages),
                recent_messages_count=len(recent_messages),
                summary_length=len(summary)
            )
        else:
            # Short conversation, use all messages as-is
            conversation_history = history

        # Call LLM with tools
        result = llm_service.chat(
            user_message=request.message,
            conversation_history=conversation_history
        )

        if not result["success"]:
            raise HTTPException(
                status_code=500,
                detail=result.get("error", "Failed to generate response")
            )

        # Store assistant response
        supabase_service.store_message(
            profile_id=profile_id,
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
            profile_id=profile_id,
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
            session_id=profile_id,  # Return as session_id for frontend compatibility
            response=result["response"],
            intent=intent_detected,
            urgency=None,  # Can add urgency detection later
            tools_used=[tool["tool"] for tool in result["tools_used"]],
        )

    except HTTPException:
        raise
    except Exception as e:
        # Log failed analytics
        try:
            supabase_service.log_analytics(
                profile_id=profile_id,
                user_query=request.message,
                success=False,
                error_message=str(e)
            )
        except:
            pass

        raise HTTPException(
            status_code=500,
            detail=f"An error occurred: {str(e)}"
        )


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """
    Global exception handler
    """
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
