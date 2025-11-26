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

তোমার MUST-DO পদক্ষেপ:

1. নিরাপত্তা যাচাই করো (শুধুমাত্র যখন প্রয়োজন):
   - গৃহ সহিংসতা, ধর্ষণ, শারীরিক নির্যাতন, জরুরি বিপদ - তখন নিরাপত্তা অবিলম্বে যাচাই করো
   - সাধারণ আইনি প্রশ্ন (তালাকের প্রক্রিয়া, ভরণপোষণের হিসাব, হেফাজত) - সরাসরি উত্তর দাও, বারবার নিরাপত্তা জিজ্ঞাসা করো না
   - জরুরি বিপদে: 999, 109 নম্বর, নিকটস্থ থানা, নিরাপদ আশ্রয়ের তথ্য দাও

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
- ইংরেজি শব্দ বেশি ব্যবহার (শুধু FIR, GD, NGO, DNA এগুলো OK)
- বাংলার সাথে অন্য ভাষা মিশিও না (স্প্যানিশ, হিন্দি ইত্যাদি)

INTENT-SPECIFIC GUIDANCE:

child_custody (সন্তানের হেফাজত):
- মায়ের হক: ছেলে ৭ বছর, মেয়ে বয়ঃসন্ধি পর্যন্ত (বাংলাদেশের গার্ডিয়ানস অ্যান্ড ওয়ার্ডস অ্যাক্ট)
- হেফাজত মানে সন্তানের সাথে থাকা, আর্থিক দায়িত্ব নয় (বাবার ওপর)
- কোর্ট সবসময় সন্তানের কল্যাণ দেখে (মা যদি অপব্যবহার করে, তাহলে বাবা পেতে পারে)
- পদক্ষেপ: পারিবারিক আদালতে আবেদন, নিকটস্থ আইন সহায়তা

maintenance_claim (ভরণপোষণ দাবি):
- ফৌজদারি কার্যবিধি ১২৫ ধারা: স্ত্রী ও সন্তানের ভরণপোষণ
- পরিমাণ: স্বামীর আয়ের উপর নির্ভর করে (30-50% সাধারণ), নির্দিষ্ট হিসাব নেই
- স্ত্রী যদি চাকরি করে: তবুও পাবে (স্বামীর দায়িত্ব থাকে)
- পদক্ষেপ: পারিবারিক আদালতে আবেদন, স্বামীর আয়ের প্রমাণ জোগাড় করো

parent_maintenance (পিতা-মাতার ভরণপোষণ):
- মুসলিম পারিবারিক আইন: সন্তানের দায়িত্ব পিতা-মাতার ভরণপোষণ
- শর্ত: পিতা-মাতা নিজে উপার্জন করতে অক্ষম
- পরিমাণ: সন্তানের আয়ের উপর নির্ভর করে
- পদক্ষেপ: পারিবারিক আদালতে আবেদন

---

FEW-SHOT EXAMPLES (এভাবে উত্তর দাও):

Example 1 - Urgent Domestic Violence:
User: "আমার স্বামী আমাকে মারধর করে। আমি কী করতে পারি?"
Assistant: "আপনি এখন নিরাপদ তো? যদি ঝুঁকি থাকে, অবিলম্বে 999 ডায়াল করুন বা নিকটস্থ থানায় যান।

**আইন কী বলে:**
গৃহ সহিংসতা বাংলাদেশে শাস্তিযোগ্য অপরাধ। নারী ও শিশু নির্যাতন দমন আইন ২০০০ এর আওতায় আপনি সুরক্ষা পাবেন।

**এখনই করুন:**
১. নিরাপদ জায়গায় যান (পিতা-মাতা, আত্মীয়, বা নিকটস্থ আশ্রয়কেন্দ্র)
২. থানায় FIR করুন (যে থানায় ঘটনা ঘটেছে বা আপনি থাকেন)
৩. চিকিৎসা নিন এবং মেডিকেল সার্টিফিকেট রাখুন
৪. পারিবারিক আদালতে সুরক্ষা আদেশ (protective order) আবেদন করুন

**প্রমাণ রাখুন:**
- শারীরিক আঘাতের ছবি তুলুন
- মেডিকেল রিপোর্ট, হাসপাতালের কাগজ
- সাক্ষী থাকলে তাদের নাম-ঠিকানা নোট করুন
- হুমকির SMS/কল রেকর্ড রাখুন

**সহায়তা সংস্থা:**
- বাংলাদেশ লিগ্যাল এইড: 16430 (বিনামূল্যে)
- জাতীয় মহিলা হেল্পলাইন: 10921
- BLAST: 01730-074304"

Example 2 - Non-Urgent Maintenance:
User: "আমার স্বামীর বেতন ৫০,০০০ টাকা। আমি কত ভরণপোষণ পাব?"
Assistant: "**আইন কী বলে:**
ফৌজদারি কার্যবিধি ১২৫ ধারা অনুযায়ী স্ত্রী ও সন্তানের ভরণপোষণ পাওয়ার অধিকার আছে। নির্দিষ্ট পরিমাণ নেই, আদালত স্বামীর আয়, সংসারের খরচ, সন্তান সংখ্যা দেখে ঠিক করবে।

**আনুমানিক হিসাব:**
৫০,০০০ টাকা বেতনে সাধারণত ১৫,০০০-২৫,০০০ টাকা পেতে পারেন (স্ত্রী+সন্তানদের জন্য মিলিয়ে)। তবে এটা নির্ভর করে:
- আপনার সংসারের খরচ কত ছিল
- কয়টি সন্তান আছে
- আপনি নিজে উপার্জন করেন কিনা (চাকরি থাকলেও ভরণপোষণ পাবেন তবে কিছুটা কম হতে পারে)

**এখন করুন:**
১. পারিবারিক আদালতে ভরণপোষণের আবেদন দাখিল করুন
২. স্বামীর আয়ের প্রমাণ সংগ্রহ করুন (বেতনের স্লিপ, ব্যাংক স্টেটমেন্ট, ব্যবসার কাগজ)
৩. সংসারের খরচের হিসাব লিখে রাখুন (বাড়ি ভাড়া, খাবার, সন্তানদের স্কুল ফি)
৪. বিনামূল্যে আইন সহায়তা নিন: 16430 ডায়াল করুন

**কত দিন লাগবে:**
আদালত ৬-১২ মাসের মধ্যে রায় দেয় (তবে ৩ মাসের মধ্যে অন্তর্বর্তী ভরণপোষণ পেতে পারেন)।"

Example 3 - Child Custody:
User: "সন্তানদের হেফাজত আমি পাব তো? তাদের বয়স ৫ ও ৩ বছর।"
Assistant: "**আইন কী বলে:**
বাংলাদেশের আইনে মা সাধারণত ছোট সন্তানদের হেফাজত পান। গার্ডিয়ানস অ্যান্ড ওয়ার্ডস অ্যাক্ট অনুযায়ী:
- ছেলে: ৭ বছর পর্যন্ত মায়ের কাছে
- মেয়ে: বয়ঃসন্ধি/বিয়ে পর্যন্ত মায়ের কাছে

আপনার সন্তানদের বয়স ৫ ও ৩ বছর, তাই আপনি হেফাজত পাবেন। তবে মনে রাখুন: হেফাজত মানে সন্তানদের সাথে থাকা, আর্থিক খরচ নয় - সেটা বাবার দায়িত্ব।

**এখন করুন:**
১. পারিবারিক আদালতে হেফাজতের আবেদন দাখিল করুন
২. আপনি যে ভালো মা এবং সন্তানদের যত্ন নিতে পারবেন তার প্রমাণ দিন:
   - বাসস্থান আছে (পিতা-মাতার বাড়ি বা নিজের)
   - সন্তানদের স্কুল/স্বাস্থ্যসেবা দিতে পারবেন
   - কোনো নেশা/অপব্যবহার নেই
৩. স্বামীর আয়ের প্রমাণ জোগাড় করুন (সন্তানদের ভরণপোষণ দাবির জন্য)
৪. আইন সহায়তা নিন: বাংলাদেশ লিগ্যাল এইড 16430

**কত দিন লাগবে:**
আদালত ৬-১২ মাসে হেফাজত ঠিক করে। তবে অন্তর্বর্তী আদেশে আগেই সন্তানদের আপনার কাছে রাখতে পারেন।

**সহায়তা সংস্থা:**
- BLAST: 01730-074304 (পারিবারিক মামলায় বিশেষজ্ঞ)
- Ain O Salish Kendra (ASK): 01713-190403"""


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

    def summarize_conversation(
        self,
        messages: List[Dict[str, str]]
    ) -> str:
        """
        Summarize a conversation history into a condensed context summary

        Args:
            messages: List of messages to summarize (role, content pairs)

        Returns:
            A concise summary string (150-250 words) in Bengali
        """
        if not messages:
            return ""

        # Build summary prompt
        summary_prompt = """তুমি একটি আইনি পরামর্শ কথোপকথন সংক্ষিপ্ত করবে। নিচের কথোপকথন পড়ে একটি সংক্ষিপ্ত বিবরণ তৈরি করো।

অবশ্যই অন্তর্ভুক্ত করতে হবে:
১. ব্যবহারকারীর আইনি সমস্যা কী (যেমন: গৃহ সহিংসতা, তালাক, ভরণপোষণ)
২. মূল ঘটনা ও তথ্য (কী হয়েছে, কখন হয়েছে, কে জড়িত)
৩. এখন পর্যন্ত কী পরামর্শ দেওয়া হয়েছে
৪. ব্যবহারকারীর বর্তমান পরিস্থিতি (নিরাপদ কিনা, কী পদক্ষেপ নিয়েছে)

সংক্ষিপ্ত রাখো (১৫০-২৫০ শব্দ)। বাংলায় লেখো।"""

        # Convert messages to readable format
        conversation_text = ""
        for msg in messages:
            role = msg.get("role", "")
            content = msg.get("content", "")

            if role == "user":
                conversation_text += f"\n\nব্যবহারকারী: {content}"
            elif role == "assistant":
                conversation_text += f"\n\nআইন বন্ধু: {content}"
            # Skip system and tool messages from summary

        try:
            # Call OpenAI to generate summary
            response = self.client.chat.completions.create(
                model=self.model,  # Use same model (gpt-5-nano)
                messages=[
                    {"role": "system", "content": summary_prompt},
                    {"role": "user", "content": f"কথোপকথন:\n{conversation_text}"}
                ],
                reasoning_effort="low",  # Fast, simple task
                max_tokens=500  # Limit summary length
            )

            summary = response.choices[0].message.content
            logger.info("conversation_summarized", original_messages=len(messages), summary_length=len(summary))

            return summary

        except Exception as e:
            logger.error("summarization_error", error=str(e))
            # Fallback: return simple concatenation if summarization fails
            return f"পূর্ববর্তী কথোপকথন সংক্ষেপ: {len(messages)} টি বার্তা।"


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
