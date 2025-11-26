"""
Supabase Service
Handles conversation storage and analytics logging with profile-based tracking
"""

import os
from typing import List, Dict, Any, Optional
from datetime import datetime
import json
from supabase import create_client, Client
import structlog

logger = structlog.get_logger()


class SupabaseService:
    """Service for interacting with Supabase"""

    def __init__(self):
        """Initialize Supabase client"""
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")

        if not supabase_url or not supabase_key:
            logger.warning("supabase_not_configured",
                         message="Supabase credentials not found. Using in-memory storage.")
            self.client: Optional[Client] = None
            self._in_memory_conversations: Dict[str, List[Dict]] = {}
        else:
            self.client = create_client(supabase_url, supabase_key)
            logger.info("supabase_initialized")

    def ensure_profile(self, profile_id: str) -> bool:
        """
        Ensure profile exists (creates if doesn't exist, updates last_active if exists)

        Args:
            profile_id: Unique profile identifier

        Returns:
            True if successful, False otherwise
        """
        if not self.client:
            return True  # In-memory mode

        try:
            # Call the get_or_create_profile function
            result = self.client.rpc('get_or_create_profile', {'p_profile_id': profile_id}).execute()
            logger.info("profile_ensured", profile_id=profile_id)
            return True
        except Exception as e:
            logger.error("profile_ensure_error", error=str(e), profile_id=profile_id)
            return False

    def store_message(
        self,
        profile_id: str,
        role: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Optional[str]:
        """
        Store a conversation message

        Args:
            profile_id: Unique profile identifier
            role: Message role (user, assistant, system, tool)
            content: Message content
            metadata: Optional metadata

        Returns:
            Message ID if successful, None otherwise
        """
        if not self.client:
            # In-memory fallback
            if profile_id not in self._in_memory_conversations:
                self._in_memory_conversations[profile_id] = []

            message = {
                "id": f"mem-{len(self._in_memory_conversations[profile_id])}",
                "profile_id": profile_id,
                "role": role,
                "content": content,
                "metadata": metadata or {},
                "created_at": datetime.now().isoformat()
            }
            self._in_memory_conversations[profile_id].append(message)
            logger.info("message_stored_in_memory", profile_id=profile_id, role=role)
            return message["id"]

        try:
            # Ensure profile exists first
            self.ensure_profile(profile_id)

            # Store message
            result = self.client.table("conversations").insert({
                "profile_id": profile_id,
                "role": role,
                "content": content,
                "metadata": metadata or {}
            }).execute()

            message_id = result.data[0]["id"] if result.data else None
            logger.info("message_stored", profile_id=profile_id, role=role, message_id=message_id)
            return message_id

        except Exception as e:
            logger.error("message_store_error", error=str(e), profile_id=profile_id)
            return None

    def get_conversation_history(
        self,
        profile_id: str,
        limit: int = 50
    ) -> List[Dict[str, str]]:
        """
        Retrieve conversation history for a profile

        Args:
            profile_id: Profile identifier
            limit: Maximum number of messages to retrieve

        Returns:
            List of messages in chronological order
        """
        if not self.client:
            # In-memory fallback
            messages = self._in_memory_conversations.get(profile_id, [])
            return [
                {"role": msg["role"], "content": msg["content"]}
                for msg in messages[-limit:]
            ]

        try:
            # Use the helper function
            result = self.client.rpc('get_conversation_history', {
                'p_profile_id': profile_id,
                'p_limit': limit
            }).execute()

            if result.data:
                return [
                    {"role": msg["role"], "content": msg["content"]}
                    for msg in result.data
                ]
            return []

        except Exception as e:
            logger.error("conversation_history_error", error=str(e), profile_id=profile_id)
            return []

    def log_analytics(
        self,
        profile_id: str,
        user_query: str,
        intent_detected: Optional[str] = None,
        tools_used: Optional[List[Dict]] = None,
        sections_retrieved: int = 0,
        tokens_used: int = 0,
        response_time_ms: int = 0,
        model: str = "gpt-5-nano",
        success: bool = True,
        error_message: Optional[str] = None
    ) -> Optional[str]:
        """
        Log query analytics

        Args:
            profile_id: Profile identifier
            user_query: The user's query
            intent_detected: Detected intent (if any)
            tools_used: List of tools that were called
            sections_retrieved: Number of legal sections retrieved
            tokens_used: Total tokens consumed
            response_time_ms: Response time in milliseconds
            model: Model used
            success: Whether the query was successful
            error_message: Error message (if failed)

        Returns:
            Analytics record ID if successful, None otherwise
        """
        if not self.client:
            # In-memory: just log
            logger.info(
                "analytics_in_memory",
                profile_id=profile_id,
                intent=intent_detected,
                tools_count=len(tools_used or []),
                sections=sections_retrieved,
                tokens=tokens_used,
                success=success
            )
            return None

        try:
            result = self.client.table("query_analytics").insert({
                "profile_id": profile_id,
                "user_query": user_query,
                "intent_detected": intent_detected,
                "tools_used": tools_used or [],
                "sections_retrieved": sections_retrieved,
                "tokens_used": tokens_used,
                "response_time_ms": response_time_ms,
                "model": model,
                "success": success,
                "error_message": error_message
            }).execute()

            analytics_id = result.data[0]["id"] if result.data else None
            logger.info("analytics_logged", profile_id=profile_id, analytics_id=analytics_id)
            return analytics_id

        except Exception as e:
            logger.error("analytics_log_error", error=str(e), profile_id=profile_id)
            return None

    def get_intent_analytics(self) -> List[Dict[str, Any]]:
        """
        Get analytics grouped by intent

        Returns:
            List of intent analytics
        """
        if not self.client:
            logger.info("analytics_not_available_in_memory")
            return []

        try:
            result = self.client.rpc('get_intent_analytics').execute()
            return result.data if result.data else []

        except Exception as e:
            logger.error("intent_analytics_error", error=str(e))
            return []


# Global Supabase service instance
_supabase_service: Optional[SupabaseService] = None


def get_supabase_service() -> SupabaseService:
    """
    Get global Supabase service instance
    Lazy initialization on first call
    """
    global _supabase_service
    if _supabase_service is None:
        _supabase_service = SupabaseService()
    return _supabase_service
