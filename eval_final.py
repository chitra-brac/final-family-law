"""
Comprehensive Evaluation for Ain Bandhu Legal Chatbot
Tests all 15 legal intents with realistic user scenarios
"""

import requests
import json
import time
from datetime import datetime
from typing import Dict, List
import uuid

API_URL = "http://localhost:8000/chat"

# Test cases covering all 15 legal intents with realistic scenarios
TEST_CASES = [
    # 1. Domestic Violence
    {
        "intent": "domestic_violence",
        "scenario": "Woman being beaten by husband",
        "messages": [
            "আমার স্বামী আমাকে মারধর করে। আমি কী করতে পারি?",
            "FIR করতে কত টাকা লাগে?",
            "আমি কি সরাসরি আদালতে যেতে পারি?",
        ],
        "expected": ["নিরাপদ", "FIR", "থানা", "পারিবারিক সহিংসতা আইন"],
    },

    # 2. Rape & Sexual Violence
    {
        "intent": "rape",
        "scenario": "Rape victim seeking help",
        "messages": [
            "আমি ধর্ষণের শিকার হয়েছি। কোথায় যাব?",
            "মেডিকেল পরীক্ষা কি বাধ্যতামূলক?",
        ],
        "expected": ["থানা", "মেডিকেল", "নারী ও শিশু নির্যাতন দমন আইন", "One Stop Crisis"],
    },

    # 3. Sexual Harassment
    {
        "intent": "sexual_harassment",
        "scenario": "Workplace harassment",
        "messages": [
            "অফিসে আমার বসের যৌন হয়রানির শিকার হচ্ছি। কী করব?",
            "কোম্পানির কাছে কমপ্লেইন করলে কি হবে?",
        ],
        "expected": ["হয়রানি প্রতিরোধ কমিটি", "লিখিত অভিযোগ", "নারী ও শিশু নির্যাতন দমন আইন"],
    },

    # 4. Dowry
    {
        "intent": "dowry",
        "scenario": "Dowry demand and harassment",
        "messages": [
            "শ্বশুরবাড়ি যৌতুক চাচ্ছে। আইন কি বলে?",
            "যৌতুকের জন্য মারধর হলে কী করব?",
        ],
        "expected": ["যৌতুক", "নিষিদ্ধ", "নারী ও শিশু নির্যাতন দমন আইন", "FIR"],
    },

    # 5. Child Marriage
    {
        "intent": "child_marriage",
        "scenario": "Underage marriage",
        "messages": [
            "আমার বোনের বয়স ১৬ কিন্তু বিয়ে দিতে চাচ্ছে। এটা কি আইনসম্মত?",
            "বাল্যবিবাহ বন্ধ করার উপায় কী?",
        ],
        "expected": ["১৮", "বাল্যবিবাহ", "থানা", "চেয়ারমান"],
    },

    # 6. Divorce/Talaq
    {
        "intent": "divorce",
        "scenario": "Divorce process",
        "messages": [
            "আমি তালাক চাই। কীভাবে তালাক নেব?",
            "খোলা কী? কত টাকা লাগে?",
            "তালাকের সময় ভরণপোষণ পাব?",
        ],
        "expected": ["খোলা", "তালাক", "Union Council", "ভরণপোষণ", "ইদ্দতকাল"],
    },

    # 7. Child Custody
    {
        "intent": "custody",
        "scenario": "Custody after divorce",
        "messages": [
            "তালাকের পর সন্তানের হেফাজত কে পাবে?",
            "ছেলে সন্তানের হেফাজত কত বছর পর্যন্ত মায়ের?",
            "আদালতে হেফাজতের মামলা করতে কত সময় লাগে?",
        ],
        "expected": ["হেফাজত", "হেজানত", "৭ বছর", "Family Court", "মায়ের"],
    },

    # 8. Maintenance
    {
        "intent": "maintenance",
        "scenario": "Wife's maintenance",
        "messages": [
            "স্বামী ভরণপোষণ দিচ্ছে না। আমি কী করতে পারি?",
            "ভরণপোষণের মামলা কোথায় করব?",
        ],
        "expected": ["ভরণপোষণ", "Family Court", "মুসলিম পারিবারিক আইন"],
    },

    # 9. Parent Maintenance
    {
        "intent": "parent_maintenance",
        "scenario": "Elderly parent maintenance",
        "messages": [
            "আমার ছেলে আমাকে দেখাশোনা করছে না। কী করব?",
            "পিতামাতার ভরণপোষণ পাওয়ার আইন আছে?",
        ],
        "expected": ["পিতামাতার ভরণপোষণ আইন", "২০১৩", "সন্তান"],
    },

    # 10. Polygamy
    {
        "intent": "polygamy",
        "scenario": "Second marriage without permission",
        "messages": [
            "স্বামী দ্বিতীয় বিয়ে করেছে। আমার কি করার আছে?",
            "দ্বিতীয় বিয়ের জন্য অনুমতি নেওয়া লাগে?",
        ],
        "expected": ["অনুমতি", "Union Council", "মুসলিম পারিবারিক আইন", "দণ্ড"],
    },

    # 11. Inheritance
    {
        "intent": "inheritance",
        "scenario": "Women's inheritance rights",
        "messages": [
            "বাবার সম্পত্তিতে মেয়ের কতটুকু অধিকার?",
            "ভাইরা আমাকে সম্পত্তি দিচ্ছে না। কী করব?",
        ],
        "expected": ["উত্তরাধিকার", "মুসলিম আইন", "সম্পত্তি"],
    },

    # 12. Marriage Registration
    {
        "intent": "marriage_registration",
        "scenario": "Marriage registration",
        "messages": [
            "বিয়ে রেজিস্ট্রি করতে হবে কেন?",
            "কাবিননামা হারিয়ে গেছে। কী করব?",
        ],
        "expected": ["রেজিস্ট্রি", "কাবিননামা", "Union Council"],
    },

    # 13. Dower/Mehr
    {
        "intent": "dower",
        "scenario": "Claiming dower",
        "messages": [
            "দেনমোহর কী? আমি কি চাইলেই পাব?",
            "তালাকের পর দেনমোহর পাওয়ার নিয়ম কী?",
        ],
        "expected": ["দেনমোহর", "কাবিননামা", "আদালত"],
    },

    # 14. Cybercrime
    {
        "intent": "cybercrime",
        "scenario": "Revenge porn and online harassment",
        "messages": [
            "আমার ছবি মরফ করে ফেসবুকে ছড়িয়ে দিয়েছে। কী করব?",
            "সাইবার ক্রাইমের অভিযোগ কোথায় করব?",
        ],
        "expected": ["ডিজিটাল নিরাপত্তা আইন", "থানা", "মরফ"],
    },

    # 15. Hindu Separation
    {
        "intent": "hindu_separation",
        "scenario": "Hindu marriage separation",
        "messages": [
            "হিন্দু আইনে কি তালাক আছে?",
            "হিন্দু নারী বিবাহ বিচ্ছেদ চাইলে কী করবে?",
        ],
        "expected": ["হিন্দু", "বিবাহ বিচ্ছেদ", "আদালত", "ভরণপোষণ"],
    },
]

# Quality criteria for evaluation
QUALITY_CRITERIA = {
    "safety_check": ["নিরাপদ", "বিপদ"],  # Safety check for urgent cases
    "legal_citation": ["আইন", "ধারা", "অধ্যাদেশ"],  # Cites actual laws
    "actionable_steps": ["যাব", "করব", "করতে হবে"],  # Gives next steps
    "bengali_quality": True,  # Response is in Bengali
    "empathy": ["বুঝি", "সহায়তা", "সাহায্য"],  # Shows empathy
    "no_repetition": True,  # Doesn't repeat info in follow-ups
}


def send_message(session_id: str, message: str) -> Dict:
    """Send message to chatbot API"""
    try:
        response = requests.post(
            API_URL,
            json={"session_id": session_id, "message": message},
            timeout=90,
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e), "success": False}


def evaluate_response(response: str, expected_keywords: List[str], is_first: bool) -> Dict:
    """Evaluate response quality"""
    scores = {
        "has_expected_keywords": 0,
        "has_legal_citation": 0,
        "has_actionable_steps": 0,
        "is_bengali": 1 if any(c in "আইউঊঋএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহড়ঢ়য়ৎংঃঁ" for c in response) else 0,
        "has_empathy": 0,
        "safety_check": 0,
    }

    # Check for expected keywords
    matched_keywords = sum(1 for kw in expected_keywords if kw in response)
    scores["has_expected_keywords"] = min(matched_keywords / len(expected_keywords), 1.0)

    # Check for legal citations
    if any(term in response for term in QUALITY_CRITERIA["legal_citation"]):
        scores["has_legal_citation"] = 1

    # Check for actionable steps
    if any(term in response for term in QUALITY_CRITERIA["actionable_steps"]):
        scores["has_actionable_steps"] = 1

    # Check for empathy (mainly in first response)
    if is_first and any(term in response for term in QUALITY_CRITERIA["empathy"]):
        scores["has_empathy"] = 1

    # Check for safety (for domestic violence, rape cases)
    if is_first and any(term in response for term in QUALITY_CRITERIA["safety_check"]):
        scores["safety_check"] = 1

    return scores


def run_evaluation():
    """Run comprehensive evaluation"""
    print("=" * 80)
    print("AIN BANDHU - FINAL EVALUATION")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print()

    results = []
    total_time = 0
    total_tokens = 0

    for i, test_case in enumerate(TEST_CASES, 1):
        print(f"\n[{i}/15] Testing: {test_case['intent'].upper()} - {test_case['scenario']}")
        print("-" * 80)

        session_id = str(uuid.uuid4())
        conversation_results = []

        for j, message in enumerate(test_case["messages"]):
            is_first = (j == 0)
            print(f"\n  Q{j+1}: {message}")

            start_time = time.time()
            response_data = send_message(session_id, message)
            response_time = time.time() - start_time

            if not response_data.get("success"):
                print(f"  ❌ ERROR: {response_data.get('error', 'Unknown error')}")
                conversation_results.append({
                    "question": message,
                    "error": True,
                    "response_time": response_time,
                })
                continue

            response = response_data["response"]
            tokens = response_data.get("tokens_used", 0)
            response_time_api = response_data.get("response_time_ms", 0) / 1000

            # Evaluate response quality
            scores = evaluate_response(response, test_case["expected"], is_first)

            # Calculate overall quality score (0-100)
            quality_score = (
                scores["has_expected_keywords"] * 30 +
                scores["has_legal_citation"] * 20 +
                scores["has_actionable_steps"] * 20 +
                scores["is_bengali"] * 10 +
                scores["has_empathy"] * 10 +
                scores["safety_check"] * 10
            )

            print(f"  ✓ Response ({len(response)} chars, {response_time_api:.1f}s, {tokens} tokens)")
            print(f"  Quality: {quality_score:.0f}/100")
            print(f"  A: {response[:150]}..." if len(response) > 150 else f"  A: {response}")

            conversation_results.append({
                "question": message,
                "response": response,
                "scores": scores,
                "quality_score": quality_score,
                "response_time": response_time_api,
                "tokens": tokens,
            })

            total_time += response_time_api
            total_tokens += tokens

            # Small delay between messages
            time.sleep(1)

        # Calculate average for this intent
        valid_results = [r for r in conversation_results if not r.get("error")]
        avg_quality = sum(r["quality_score"] for r in valid_results) / len(valid_results) if valid_results else 0
        avg_time = sum(r["response_time"] for r in valid_results) / len(valid_results) if valid_results else 0

        results.append({
            "intent": test_case["intent"],
            "scenario": test_case["scenario"],
            "conversation": conversation_results,
            "avg_quality": avg_quality,
            "avg_response_time": avg_time,
        })

        print(f"\n  📊 Intent Summary: Quality={avg_quality:.0f}/100, Avg Time={avg_time:.1f}s")

    # Overall summary
    print("\n" + "=" * 80)
    print("EVALUATION SUMMARY")
    print("=" * 80)

    all_quality_scores = []
    all_response_times = []

    for result in results:
        valid_convos = [c for c in result["conversation"] if not c.get("error")]
        if valid_convos:
            all_quality_scores.extend([c["quality_score"] for c in valid_convos])
            all_response_times.extend([c["response_time"] for c in valid_convos])

    avg_quality_overall = sum(all_quality_scores) / len(all_quality_scores) if all_quality_scores else 0
    avg_time_overall = sum(all_response_times) / len(all_response_times) if all_response_times else 0

    print(f"\nIntents Tested: 15/15")
    print(f"Total Queries: {len(all_quality_scores)}")
    print(f"Average Quality Score: {avg_quality_overall:.1f}/100")
    print(f"Average Response Time: {avg_time_overall:.1f}s")
    print(f"Total Tokens Used: {total_tokens:,}")
    print(f"Success Rate: {len(all_quality_scores)}/{sum(len(r['conversation']) for r in results)} ({len(all_quality_scores)/sum(len(r['conversation']) for r in results)*100:.1f}%)")

    print("\n📋 Intent Breakdown:")
    print("-" * 80)
    print(f"{'Intent':<25} {'Scenario':<35} {'Quality':<10} {'Time':<10}")
    print("-" * 80)

    for result in results:
        print(f"{result['intent']:<25} {result['scenario'][:33]:<35} {result['avg_quality']:>6.0f}/100  {result['avg_response_time']:>6.1f}s")

    # Save detailed results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"eval_results_{timestamp}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "intents_tested": 15,
                "total_queries": len(all_quality_scores),
                "avg_quality": avg_quality_overall,
                "avg_response_time": avg_time_overall,
                "total_tokens": total_tokens,
                "success_rate": len(all_quality_scores) / sum(len(r['conversation']) for r in results) if results else 0,
            },
            "results": results,
        }, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Detailed results saved to: {output_file}")
    print("\n" + "=" * 80)

    # Quality assessment
    print("\n🎯 QUALITY ASSESSMENT:")
    if avg_quality_overall >= 80:
        print("✅ EXCELLENT - Ready for production!")
    elif avg_quality_overall >= 70:
        print("✅ GOOD - Minor improvements recommended")
    elif avg_quality_overall >= 60:
        print("⚠️  FAIR - Significant improvements needed")
    else:
        print("❌ POOR - Major issues to address")

    print("=" * 80)


if __name__ == "__main__":
    print("\nStarting evaluation in 3 seconds...")
    print("Make sure the server is running at http://localhost:8000")
    time.sleep(3)

    try:
        run_evaluation()
    except KeyboardInterrupt:
        print("\n\n⚠️  Evaluation interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Evaluation failed: {e}")
        import traceback
        traceback.print_exc()
