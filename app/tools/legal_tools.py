"""
Legal Tools for OpenAI Function Calling
Provides access to legal knowledge and procedural guidance
"""

from typing import Dict, Any, List
from app.services.data_loader import get_data_loader
from app.services.semantic_search import get_search_service


# OpenAI function definitions
LEGAL_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_legal_knowledge",
            "description": "Get the actual law text (legal sections) for a specific intent. Call this to know what the law says about family law, violence, or rights.",
            "parameters": {
                "type": "object",
                "properties": {
                    "intent": {
                        "type": "string",
                        "description": "The legal intent category",
                        "enum": [
                            "rape_sexual_violence",
                            "domestic_violence_general",
                            "dowry",
                            "child_marriage",
                            "custody",
                            "maintenance",
                            "divorce_talaq",
                            "polygamy_second_marriage",
                            "inheritance_succession",
                            "marriage_registration",
                            "dower_mehr",
                            "parent_maintenance",
                            "sexual_harassment",
                            "cybercrime",
                            "hindu_separation"
                        ]
                    }
                },
                "required": ["intent"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_procedural_guidance",
            "description": "Get intent-specific procedural guidance (definitions, key laws, step-by-step actions, punishments, timelines) and general procedures for handling a legal situation. This tells you HOW to use the law and WHAT to do.",
            "parameters": {
                "type": "object",
                "properties": {
                    "intent": {
                        "type": "string",
                        "description": "The legal intent category",
                        "enum": [
                            "rape_sexual_violence",
                            "domestic_violence_general",
                            "dowry",
                            "child_marriage",
                            "custody",
                            "maintenance",
                            "divorce_talaq",
                            "polygamy_second_marriage",
                            "inheritance_succession",
                            "marriage_registration",
                            "dower_mehr",
                            "parent_maintenance",
                            "sexual_harassment",
                            "cybercrime",
                            "hindu_separation"
                        ]
                    },
                    "topics": {
                        "type": "array",
                        "description": "Optional: select 2-3 most relevant general procedures (filing FIR, safety planning, etc). If not specified, only intent-specific guidance is returned.",
                        "items": {
                            "type": "string",
                            "enum": [
                                "file_fir",
                                "file_gd",
                                "get_legal_aid",
                                "court_process",
                                "safety_planning",
                                "evidence_collection",
                                "emergency_helplines",
                                "police_refuses"
                            ]
                        },
                        "minItems": 0,
                        "maxItems": 3
                    }
                },
                "required": ["intent"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_legal_sections",
            "description": "Search all 1,512 legal sections across 58 Bangladesh acts to find relevant law for ANY family law question. Use this when the question doesn't fit predefined intents or when you need broader legal context. Returns 3-5 most relevant sections. Available acts: 9=Hindu Widow's Re-marriage Act 1856, 20=Divorce Act 1869, 25=Special Marriage Act 1872, 27=Christian Marriage Act 1872, 30=Married Women's Property Act 1874, 33=Majority Act 1875, 56=Births Deaths Marriages Registration Act 1886, 64=Guardians and Wards Act 1890, 68=Partition Act 1893, 83=Foreign Marriage Act 1903, 92=Anand Marriage Act 1909, 101=Mussalman Wakf Validating Act 1913, 105=Hindu Disposition of Property Act 1916, 122=Maintenance Orders Enforcement Act 1921, 138=Succession Act 1925, 147=Hindu Inheritance (Removal of Disabilities) Act 1928, 148=Hindu Law of Inheritance (Amendment) Act 1929, 149=Child Marriage Restraint Act 1929, 152=Hindu Gains of Learning Act 1930, 168=Parsi Marriage and Divorce Act 1936, 171=Hindu Women's Rights to Property Act 1937, 172=Arya Marriage Validation Act 1937, 173=Muslim Personal Law (Shariat) Application Act 1937, 178=Cutchi Memons Act 1938, 180=Dissolution of Muslim Marriages Act 1939, 201=Hindu Women's Rights to Property (Agricultural Land) Act 1943, 207=Orphanages and Widows' Homes Act 1944, 214=Hindu Married Women's Right to Separate Residence and Maintenance Act 1946, 215=Hindu Marriage Disabilities Removal Act 1946, 290=Claims for Maintenance (Recovery Abroad) Ordinance 1959, 305=Muslim Family Laws Ordinance 1961, 470=Children Act 1974, 476=Muslim Marriages and Divorces (Registration) Act 1974, 529=Public Servants (Marriage with Foreign Nationals) Ordinance 1976, 607=Dowry Prohibition Act 1980, 621=Bangladesh Abandoned Children (Special Provisions) (Repeal) Ordinance 1982, 660=Hindu Religious Welfare Trust Ordinance 1983, 661=Buddhist Religious Welfare Trust Ordinance 1983, 673=Bangladesh Women's Rehabilitation and Welfare Foundation (Repeal) Ordinance 1984, 682=Family Courts Ordinance 1985, 749=জাতীয় মহিলা সংস্থা আইন ১৯৯১, 835=নারী ও শিশু নির্যাতন দমন আইন ২০০০, 921=জন্ম ও মৃত্যু নিবন্ধন আইন ২০০৪, 956=কারাগারে আটক সাজাপ্রাপ্ত নারীদের বিশেষ সুবিধা আইন ২০০৬, 1063=পারিবারিক সহিংসতা আইন ২০১০, 1105=হিন্দু বিবাহ নিবন্ধন আইন ২০১২, 1109=ওয়াক্‌ফ সম্পত্তি হস্তান্তর আইন ২০১৩, 1119=শিশু আইন ২০১৩, 1132=পিতা-মাতার ভরণ-পোষণ আইন ২০১৩, 1172=গণকর্মচারী বিদেশি বিবাহ আইন ২০১৫, 1207=বাল্যবিবাহ নিরোধ আইন ২০১৭, 1256=যৌতুক নিরোধ আইন ২০১৮, 1351=নারী ও শিশু নির্যাতন দমন (সংশোধন) আইন ২০২০, 1375=শিশু দিবাযত্ন কেন্দ্র আইন ২০২১, 1444=পারিবারিক আদালত আইন ২০২৩, 1488=গ্রাম আদালত (সংশোধন) আইন ২০২৪, 1524=নারী ও শিশু নির্যাতন দমন (সংশোধন) অধ্যাদেশ ২০২৫, 1543=জুলাই গণঅভ্যুত্থানে শহিদ পরিবার কল্যাণ অধ্যাদেশ ২০২৫",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The user's question or legal issue in Bengali (e.g., 'কর্মক্ষেত্রে যৌন হয়রানি', 'সাইবার ক্রাইম')"
                    },
                    "act_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional: specific act_ids to search within (skip act discovery). Use when you know which act applies."
                    }
                },
                "required": ["query"]
            }
        }
    }
]


def execute_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute a legal tool and return results

    Args:
        tool_name: Name of the tool to execute
        arguments: Tool arguments

    Returns:
        Dict with tool results
    """
    loader = get_data_loader()

    if tool_name == "get_legal_knowledge":
        intent = arguments.get("intent")
        if not intent:
            return {"error": "Intent parameter is required"}

        result = loader.get_legal_knowledge(intent)

        # Log which sections were retrieved
        sections_count = len(result.get("legal_sections", []))

        return {
            "intent": intent,
            "sections_count": sections_count,
            "legal_sections": result.get("legal_sections", [])
        }

    elif tool_name == "get_procedural_guidance":
        intent = arguments.get("intent")
        topics = arguments.get("topics", [])  # Optional

        if not intent:
            return {"error": "Intent parameter is required"}

        if topics and not isinstance(topics, list):
            return {"error": "Topics must be an array"}

        # Get procedural guidance
        result = loader.get_procedural_guidance(intent, topics)

        return {
            "intent": intent,
            "topics_requested": topics,
            "intent_guidance": result.get("intent_guidance", {}),
            "general_procedures": result.get("general_procedures", {})
        }

    elif tool_name == "search_legal_sections":
        query = arguments.get("query")
        if not query:
            return {"error": "Query parameter is required"}

        # Use semantic search service
        search_service = get_search_service()

        # If act_ids provided, skip act discovery
        act_ids = arguments.get("act_ids")
        if not act_ids:
            # Step 1: Find relevant acts via GPT-4o-mini
            act_ids = search_service.search_relevant_acts(query, top_k=2)

        if not act_ids:
            return {"error": "No relevant acts found", "legal_sections": []}

        # Step 2: Get sections from each act
        all_sections = []
        for act_id in act_ids:
            sections = search_service.get_sections_from_act(act_id, query)
            all_sections.extend(sections)

        return {
            "query": query,
            "acts_searched": act_ids,
            "sections_count": len(all_sections),
            "legal_sections": all_sections
        }

    else:
        return {"error": f"Unknown tool: {tool_name}"}


def get_available_intents() -> List[str]:
    """Get list of available intent categories"""
    return [
        "rape_sexual_violence",
        "domestic_violence_general",
        "dowry",
        "child_marriage",
        "custody",
        "maintenance",
        "divorce_talaq",
        "polygamy_second_marriage",
        "inheritance_succession",
        "marriage_registration",
        "dower_mehr",
        "parent_maintenance",
        "sexual_harassment",
        "cybercrime",
        "hindu_separation"
    ]


def get_available_topics() -> List[str]:
    """Get list of available procedural topics"""
    return [
        "file_fir",
        "file_gd",
        "get_legal_aid",
        "court_process",
        "safety_planning",
        "evidence_collection",
        "emergency_helplines",
        "police_refuses"
    ]
