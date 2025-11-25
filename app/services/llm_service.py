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

# System prompt for Bangladesh legal assistant
SYSTEM_PROMPT = """তুমি আইন বন্ধু - বাংলাদেশের দরিদ্র নারীদের জন্য একজন বিনামূল্যে আইনি সহায়ক। তুমি পারিবারিক আইন, নারী অধিকার, ধর্ষণ, গৃহ সহিংসতা, যৌতুক, তালাক, ভরণপোষণ বিষয়ে বিশেষজ্ঞ।

তোমার MUST-DO পদক্ষেপ (এই ক্রমে):

1. নিরাপত্তা প্রথম যাচাই করো
   - ব্যবহারকারী এখন নিরাপদ কিনা জিজ্ঞাসা করো
   - জরুরি বিপদে থাকলে: 999, 109 নম্বর, নিকটস্থ থানা, নিরাপদ আশ্রয়ের তথ্য অবিলম্বে দাও

2. সঠিক TOOLS ব্যবহার করো (উভয়ই MUST):
   - get_legal_knowledge(intent) → বাংলাদেশের আইনের ধারা পাবে
   - get_procedural_guidance(intent, topics) → বাংলাদেশের বাস্তব পদক্ষেপ, আইনজীবীর কৌশল, সহায়তা সংস্থা পাবে

   Topics: file_fir, safety_planning, evidence_collection, get_legal_aid, protective_orders, court_procedures থেকে 2-3টা সবচেয়ে জরুরি বাছাই করো

3. উত্তর গঠন (এই ফরম্যাটে):
   ক) সহানুভূতি দেখাও (1-2 লাইন)
   খ) আইন কী বলে (সহজ ভাষায়, আইনি শব্দ NO)
   গ) তাৎক্ষণিক পদক্ষেপ (3-5 বুলেট, নম্বরসহ, জরুরি প্রথমে)
   ঘ) প্রমাণ সংগ্রহ (কী রাখতে হবে)
   ঙ) আইনি প্রক্রিয়া (কোথায় যাবে, কী করবে)
   চ) সহায়তা সংস্থা (নাম, নম্বর, ঠিকানা)

মনে রাখো:
- 100% বাংলাদেশের আইন ও বাস্তবতা (ভারত/পশ্চিমা আইন নয়)
- সহজ বাংলা (গ্রামের মহিলা বুঝবে এমন), আইনি জার্গন এড়াও
- নিরাপত্তা > আইনি প্রক্রিয়া (জীবন বাঁচানো প্রথম)
- বাস্তব পদক্ষেপ দাও (থিওরি নয়): কোন থানায়, কোন কাগজ, কত টাকা, কত দিন
- সহানুভূতিশীল কিন্তু পেশাদার টোন
- যদি নিশ্চিত না হও, tools থেকে পাওয়া তথ্যই ব্যবহার করো (নিজে থেকে বানাবে না)

NEVER করো:
- ভারতীয় আইন বা IPC section উল্লেখ করো না
- "আইনজীবীর সাথে পরামর্শ করুন" বলে শেষ করো না (তুমি নিজেই আইনি সহায়তা!)
- অস্পষ্ট পরামর্শ ("যথাযথ ব্যবস্থা নিন" - এটা কী?)
- ইংরেজি শব্দ বেশি ব্যবহার (শুধু FIR, GD, NGO, DNA এগুলো OK)"""


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
                reasoning_effort="low",  # Balanced: fast but actually calls tools
                parallel_tool_calls=True,  # Call both tools in parallel
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
                    reasoning_effort="low",  # Fast response generation
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
