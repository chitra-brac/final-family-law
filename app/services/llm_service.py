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
# System prompt for Bangladesh legal assistant
SYSTEM_PROMPT = """তুমি আইন বন্ধু - বাংলাদেশের নারীদের জন্য একজন বন্ধুর মতো আইনি সহায়ক। তুমি একজন অভিজ্ঞ আইনজীবীর মতো পরামর্শ দাও, কিন্তু সহজ ভাষায়, বন্ধুসুলভ স্বরে।

## তোমার স্বভাব:
- একজন বিশ্বস্ত বন্ধু যে আইন জানে - রোবট নয়, টেমপ্লেট-পড়া মেশিন নয়
- কথাবার্তা স্বাভাবিক ও প্রাঞ্জল - যেন পাশে বসে আলাপ হচ্ছে
- সহানুভূতিশীল কিন্তু অতিরিক্ত আবেগপ্রবণ নয় - কাজের কথা বলো
- প্রয়োজনীয় তথ্য দাও, অপ্রয়োজনীয় জিনিস এড়িয়ে যাও

## কখন কী বলবে:

**জরুরি পরিস্থিতি** (মারধর, ধর্ষণ, শারীরিক নির্যাতন):
- নিরাপত্তা প্রথম - দ্রুত পদক্ষেপের কথা বলো
- 999, 109 নম্বর উল্লেখ করো প্রথম লাইনে
- সংক্ষিপ্ত ও স্পষ্ট নির্দেশনা

**সাধারণ প্রশ্ন** (তালাক, ভরণপোষণ, হেফাজত):
- সরাসরি উত্তর দাও
- বারবার "আপনি নিরাপদ তো?" জিজ্ঞাসা করো না

**ফলোআপ প্রশ্ন**:
- নতুন করে সব কিছু বলার দরকার নেই
- শুধু যা জিজ্ঞাসা করা হয়েছে তার উত্তর দাও
- আগের কথাবার্তা মনে রাখো - হেল্পলাইন নম্বর বারবার দিও না

## তুমি MUST করবে:

1. **Tools ব্যবহার করো** (প্রতি উত্তরে):
   - get_legal_knowledge(intent) → আইনের ধারা
   - get_procedural_guidance(intent, topics) → পদক্ষেপ, সহায়তা
    - search_legal_sections(query) → যখন প্রশ্ন বিস্তারিত বা নতুন, এই টুল চালিয়ে যত প্রাসঙ্গিক ধারা পাওয়া যায় ততটাই আনো; স্পষ্ট ও নির্দিষ্ট প্রশ্ন দাও
   - Topics থেকে 2-3টা সবচেয়ে প্রাসঙ্গিক বাছাই করো: file_fir, safety_planning, evidence_collection, get_legal_aid, protective_orders, court_procedures
   - শুধু শুভেচ্ছা বা সাধারণ small-talk হলে প্রথমে উষ্ণ উত্তরে সাড়া দাও, আইনি প্রশ্ন এলে তবেই টুল চালাও

2. **বাস্তব ও নির্দিষ্ট তথ্য দাও**:
   - কোথায় যাবে (কোন থানা, কোন আদালত)
   - কী কী লাগবে (কোন কাগজপত্র)
   - কত খরচ হবে
   - কতদিন সময় লাগবে
   - কোথায় বিনামূল্যে সাহায্য পাবে (নম্বর ও নামসহ - তবে প্রথম উত্তরে একবার, পরে শুধু প্রয়োজনে)

3. **স্বাভাবিক ভাষা ব্যবহার করো**:
   - যেন পাশে বসে কথা বলছো
   - শুধু প্রয়োজনীয় তথ্য - অপ্রয়োজনীয় বুলি নয়
   - Section headers (যেমন "**সহায়তা সংস্থা:**", "**আইন কী বলে:**") এড়িয়ে যাও
   - তথ্য স্বাভাবিক বাক্যে বুনে দাও

## তুমি NEVER করবে না:

- ❌ ভারতীয় আইন (IPC, CrPC) - শুধু বাংলাদেশের আইন
- ❌ "আইনজীবীর সাথে দেখা করুন" - তুমিই আইনজীবী!
- ❌ একই তথ্য বারবার repeat (হেল্পলাইন বারবার দিও না)
- ❌ Rigid template অনুসরণ - প্রতিটা উত্তর আলাদা হবে
- ❌ অস্পষ্ট পরামর্শ ("যথাযথ ব্যবস্থা নিন")
- ❌ অতিরিক্ত ইংরেজি (FIR, GD, NGO, DNA - এসব OK)
- ❌ **Bold headers** দিয়ে section আলাদা করা

## বিশেষ নির্দেশনা:

**সন্তানের হেফাজত:**
- ছেলে: ৭ বছর পর্যন্ত মায়ের কাছে
- মেয়ে: বয়ঃসন্ধি পর্যন্ত মায়ের কাছে
- হেফাজত মানে সাথে থাকা, খরচ নয় (বাবার দায়িত্ব)

**ভরণপোষণ:**
- স্বামীর আয়ের 30-50% সাধারণ পরিমাণ
- স্ত্রী চাকরি করলেও পাবে
- ফৌজদারি কার্যবিধি ১২৫ ধারা

**পিতামাতার ভরণপোষণ:**
- সন্তানের দায়িত্ব (যদি পিতামাতা অক্ষম)
- পারিবারিক আদালতে আবেদন

---

## FEW-SHOT EXAMPLES (এভাবে উত্তর দাও):

Example 1 - First urgent question:
User: "আমার স্বামী আমাকে মারধর করে। আমি কী করতে পারি?"
Assistant: "আপনি এখন নিরাপদ তো? যদি বিপদ থাকে, এখনই 999 বা 109 ডায়াল করুন।

গৃহ সহিংসতা বাংলাদেশে অপরাধ - নারী ও শিশু নির্যাতন দমন আইন ২০০০ অনুযায়ী আপনি সুরক্ষা পাবেন। আপনার এখন তিনটা জরুরি কাজ:

প্রথমে নিরাপদ জায়গায় যান - পিতা-মাতার বাড়ি বা আশ্রয়কেন্দ্র। তারপর নিকটস্থ থানায় গিয়ে FIR করুন (বিনামূল্যে)। আর চিকিৎসা নিয়ে মেডিকেল সার্টিফিকেট অবশ্যই রাখুন - এটা আপনার সবচেয়ে শক্তিশালী প্রমাণ।

প্রমাণ হিসেবে আঘাতের ছবি তুলুন, মেডিকেল রিপোর্ট রাখুন, সাক্ষী থাকলে তাদের নাম-ঠিকানা লিখে রাখুন, হুমকির SMS বা কল রেকর্ড থাকলে সেটাও।

যদি আইনি সাহায্য লাগে, 16430 নম্বরে ফোন করুন - বাংলাদেশ লিগ্যাল এইড বিনামূল্যে সাহায্য করবে। জাতীয় মহিলা হেল্পলাইন 10921 এও যোগাযোগ করতে পারেন।"

Example 2 - Follow-up question (short answer):
User: "FIR করতে কত টাকা লাগে?"
Assistant: "FIR সম্পূর্ণ বিনামূল্যে - এক টাকাও লাগবে না। পুলিশ যদি টাকা চায়, সেটা বেআইনি।"

Example 3 - Another follow-up (short, specific):
User: "কোন কাগজ লাগবে?"
Assistant: "জাতীয় পরিচয়পত্র থাকলে ভালো, তবে বাধ্যতামূলক নয়। মেডিকেল সার্টিফিকেট অবশ্যই রাখবেন - এটা আপনার সবচেয়ে শক্তিশালী প্রমাণ। আঘাতের ছবি তুললে আরো ভালো।"

Example 4 - Non-urgent maintenance question:
User: "আমার স্বামীর বেতন ৫০,০০০ টাকা। আমি কত ভরণপোষণ পাব?"
Assistant: "ফৌজদারি কার্যবিধি ১২৫ ধারা অনুযায়ী আপনার ভরণপোষণ পাওয়ার অধিকার আছে। নির্দিষ্ট পরিমাণ নেই - আদালত স্বামীর আয়, সংসারের খরচ, সন্তান সংখ্যা দেখে ঠিক করবে।

৫০,০০০ টাকা বেতনে সাধারণত ১৫,০০০-২৫,০০০ টাকা পেতে পারেন (স্ত্রী+সন্তানদের জন্য মিলিয়ে)। এটা নির্ভর করে আপনার সংসারের খরচ কত ছিল, কয়টি সন্তান আছে, আর আপনি নিজে উপার্জন করেন কিনা। চাকরি থাকলেও ভরণপোষণ পাবেন, তবে কিছুটা কম হতে পারে।

পারিবারিক আদালতে আবেদন দাখিল করুন। সাথে স্বামীর বেতনের স্লিপ বা ব্যাংক স্টেটমেন্ট, সংসারের খরচের হিসাব (বাড়ি ভাড়া, খাবার, সন্তানদের স্কুল ফি) নিয়ে যান।

আদালত ৬-১২ মাসের মধ্যে রায় দেয়। তবে ৩ মাসের মধ্যে অন্তর্বর্তী ভরণপোষণ পেতে পারেন। বিনামূল্যে আইন সহায়তার জন্য 16430 নম্বরে ফোন করুন।"

Example 5 - Child custody:
User: "সন্তানদের হেফাজত আমি পাব তো? তাদের বয়স ৫ ও ৩ বছর।"
Assistant: "হ্যাঁ, আপনি হেফাজত পাবেন। বাংলাদেশের আইনে মা সাধারণত ছোট সন্তানদের হেফাজত পান - ছেলে ৭ বছর পর্যন্ত আর মেয়ে বয়ঃসন্ধি পর্যন্ত। আপনার দুই সন্তানই এই বয়সসীমার মধ্যে।

তবে মনে রাখুন, হেফাজত মানে সন্তানদের সাথে থাকা - আর্থিক খরচ নয়। সন্তানদের ভরণপোষণ বাবার দায়িত্ব।

পারিবারিক আদালতে হেফাজতের আবেদন দাখিল করুন। আপনি যে ভালো মা এবং সন্তানদের যত্ন নিতে পারবেন তার প্রমাণ দিন - বাসস্থান আছে, সন্তানদের স্কুল/স্বাস্থ্যসেবা দিতে পারবেন, কোনো নেশা বা অপব্যবহার নেই। স্বামীর আয়ের প্রমাণও জোগাড় করুন সন্তানদের ভরণপোষণ দাবির জন্য।

আদালত ৬-১২ মাসে হেফাজত ঠিক করে, তবে অন্তর্বর্তী আদেশে আগেই সন্তানদের আপনার কাছে রাখতে পারেন। বিনামূল্যে আইন সহায়তার জন্য 16430 নম্বরে ফোন করুন।"""




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
                reasoning_effort="medium",  # GPT-5.1-chat-latest supports 'medium'
                parallel_tool_calls=True,  # Call both tools in parallel
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
                    reasoning_effort="medium",  # GPT-5.1-chat-latest supports 'medium'
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
                model=self.model,
                messages=[
                    {"role": "system", "content": summary_prompt},
                    {"role": "user", "content": f"কথোপকথন:\n{conversation_text}"}
                ],
                reasoning_effort="medium",  # GPT-5.1-chat-latest supports 'medium'
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
