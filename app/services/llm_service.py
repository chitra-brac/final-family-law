"""
LLM Service
Handles OpenAI GPT-5.1 Instant integration with tool calling
"""

import json
import os
from typing import List, Dict, Any, Optional, Iterator
from openai import OpenAI
import structlog

from app.tools.legal_tools import LEGAL_TOOLS, execute_tool

logger = structlog.get_logger()

# Short, clear system prompt (following Mustavi's advice)
SYSTEM_PROMPT = """তুমি একজন বাংলাদেশী আইনজীবী।তুমি পারিবারিক আইন, নারী অধিকার, এবং সহিংসতা সম্পর্কিত মামলায় বিশেষজ্ঞ।

তোমার কাজ:
1. ব্যবহারকারীর সমস্যা বুঝো
2. প্রাসঙ্গিক আইনি ধারা খুঁজে দাও (tools ব্যবহার করে)
3. স্পষ্ট, সহজ বাংলায় পরামর্শ দাও
4. ধাপে ধাপে কী করতে হবে বলো

মনে রাখো:
- সহজ ভাষা ব্যবহার করো (আইনি শব্দ এড়িয়ে চলো)
- সহানুভূতিশীল হও
- নিরাপত্তা প্রথম
- Practical পদক্ষেপ দাও"""


class LLMService:
    """Service for interacting with OpenAI GPT-5.1 Instant"""

    def __init__(self):
        """Initialize OpenAI client"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")

        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4-turbo")  # Default to gpt-4-turbo if GPT-5.1 not available yet
        logger.info("llm_service_initialized", model=self.model)

    def chat(
        self,
        user_message: str,
        conversation_history: Optional[List[Dict[str, str]]] = None,
        stream: bool = False
    ) -> Dict[str, Any]:
        """
        Send a chat message and get response with tool calling

        Args:
            user_message: The user's message
            conversation_history: Previous messages in conversation
            stream: Whether to stream the response

        Returns:
            Dict with response, tools_used, tokens_used, etc.
        """
        # Build messages array
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        # Add conversation history
        if conversation_history:
            messages.extend(conversation_history)

        # Add current user message
        messages.append({"role": "user", "content": user_message})

        # Track tools used
        tools_used = []
        total_tokens = 0

        logger.info("chat_request", user_message=user_message[:100], history_length=len(conversation_history or []))

        try:
            # First API call with tools
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=LEGAL_TOOLS,
                tool_choice="auto",
                # Note: gpt-5 only supports default temperature (1)
            )

            # Check if model wants to use tools
            message = response.choices[0].message
            total_tokens += response.usage.total_tokens

            # Tool calling loop
            while message.tool_calls:
                # Add assistant's tool call message to history
                messages.append(message.model_dump())

                # Execute each tool call
                for tool_call in message.tool_calls:
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)

                    logger.info("executing_tool", tool=function_name, args=function_args)

                    # Execute the tool
                    tool_result = execute_tool(function_name, function_args)

                    # Track usage
                    tools_used.append({
                        "tool": function_name,
                        "args": function_args,
                        "sections_count": tool_result.get("sections_count", 0)
                    })

                    # Add tool result to messages
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": function_name,
                        "content": json.dumps(tool_result, ensure_ascii=False)
                    })

                # Get final response from model
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    # Note: gpt-5 only supports default temperature (1)
                )

                message = response.choices[0].message
                total_tokens += response.usage.total_tokens

            # Get final text response
            final_response = message.content

            logger.info(
                "chat_response_complete",
                tools_used_count=len(tools_used),
                total_tokens=total_tokens,
                response_length=len(final_response)
            )

            return {
                "response": final_response,
                "tools_used": tools_used,
                "tokens_used": total_tokens,
                "model": self.model,
                "success": True
            }

        except Exception as e:
            logger.error("chat_error", error=str(e), error_type=type(e).__name__)
            return {
                "response": "দুঃখিত, একটি সমস্যা হয়েছে। অনুগ্রহ করে আবার চেষ্টা করুন।",
                "error": str(e),
                "tools_used": tools_used,
                "tokens_used": total_tokens,
                "success": False
            }

    def chat_stream(
        self,
        user_message: str,
        conversation_history: Optional[List[Dict[str, str]]] = None
    ) -> Iterator[str]:
        """
        Stream chat response (simplified version without tool calling)
        For MVP, we'll use non-streaming with tools, then stream the final response

        Args:
            user_message: The user's message
            conversation_history: Previous messages

        Yields:
            Response chunks
        """
        # For now, get full response then yield it
        # TODO: Implement proper streaming with tool calls
        result = self.chat(user_message, conversation_history, stream=False)

        if result["success"]:
            # Yield response word by word for streaming effect
            words = result["response"].split()
            for i, word in enumerate(words):
                if i == len(words) - 1:
                    yield word
                else:
                    yield word + " "
        else:
            yield result["response"]


# Global LLM service instance
_llm_service: Optional[LLMService] = None


def get_llm_service() -> LLMService:
    """
    Get global LLM service instance
    Lazy initialization on first call
    """
    global _llm_service
    if _llm_service is None:
        _llm_service = LLMService()
    return _llm_service
