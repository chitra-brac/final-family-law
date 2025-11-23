"""
Pydantic models for request/response schemas
"""

from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


class ChatRequest(BaseModel):
    """Request model for chat endpoint"""

    session_id: str = Field(..., description="Unique session ID for conversation tracking")
    message: str = Field(..., min_length=1, max_length=1000, description="User message in Bengali or English")


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""

    session_id: str
    response: str = Field(..., description="AI assistant response in Bengali")
    intent: Optional[str] = Field(None, description="Classified intent if applicable")
    urgency: Optional[Literal["critical", "high", "medium", "low"]] = Field(None, description="Urgency level")
    tools_used: Optional[list[str]] = Field(None, description="List of tools called")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class NewSessionRequest(BaseModel):
    """Request model for creating new session"""

    metadata: Optional[dict] = Field(None, description="Optional metadata about the session")


class NewSessionResponse(BaseModel):
    """Response model for new session"""

    session_id: str
    greeting: str = Field(default="আসসালামু আলাইকুম। আমি আইন বন্ধু, আপনার আইনি সহায়ক। আপনি কি ধরনের আইনি সমস্যার মুখোমুখি?")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class HealthResponse(BaseModel):
    """Response model for health check"""

    status: Literal["healthy", "unhealthy"]
    version: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
