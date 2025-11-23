"""
Main FastAPI application
Ain Bandhu - AI Legal Assistant for Bangladeshi Women
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uuid
from datetime import datetime

from app.config import get_settings
from app.models import (
    ChatRequest,
    ChatResponse,
    NewSessionRequest,
    NewSessionResponse,
    HealthResponse,
)

# Initialize settings
settings = get_settings()

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
    # TODO: Load JSON data into memory (data loader)
    # TODO: Initialize OpenAI client
    # TODO: Initialize Supabase client


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
    1. Validate session
    2. Send message to OpenAI with tools
    3. Execute tools if called
    4. Store conversation in Supabase
    5. Return response
    """
    # TODO: Validate session exists
    # TODO: Get conversation history from Supabase
    # TODO: Send to OpenAI with tools
    # TODO: Execute tools if needed
    # TODO: Store messages in Supabase
    # TODO: Return response

    # Placeholder response for now
    return ChatResponse(
        session_id=request.session_id,
        response="দুঃখিত, চ্যাটবট এখনও সম্পূর্ণভাবে কার্যকর নয়। আমরা শীঘ্রই চালু করবো।",
        intent=None,
        urgency=None,
        tools_used=None,
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
