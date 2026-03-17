"""
Pydantic models for request/response schemas
"""

from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import datetime


class ChatRequest(BaseModel):
    """Request model for chat endpoint"""

    profile_id: str = Field(..., description="Persistent anonymous profile ID")
    session_id: str = Field(..., description="Unique session ID for conversation tracking")
    message: str = Field(..., min_length=1, max_length=1000, description="User message in Bengali or English")


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""

    profile_id: str
    session_id: str
    response: str = Field(..., description="AI assistant response in Bengali")
    intent: Optional[str] = Field(None, description="Classified intent if applicable")
    tools_used: Optional[list[str]] = Field(None, description="List of tools called")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class NewSessionRequest(BaseModel):
    """Request model for creating new session"""
    profile_id: Optional[str] = None


class NewSessionResponse(BaseModel):
    """Response model for new session"""

    profile_id: str
    session_id: str
    greeting: str = Field(default="আমি আপনার পারিবারিক আইন সহায়ক। আপনি কি ধরনের আইনি সমস্যার মুখোমুখি?")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class HealthResponse(BaseModel):
    """Response model for health check"""

    status: Literal["healthy", "unhealthy"]
    version: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
