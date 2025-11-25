"""
Legal Tools for OpenAI Function Calling
Provides access to legal knowledge and procedural guidance
"""

from typing import Dict, Any, List
from app.services.data_loader import get_data_loader


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
                            "parent_maintenance"
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
            "description": "Get lawyer's strategic playbook, step-by-step legal process, support organizations, and practical procedures for handling this specific legal situation. This tells you HOW to use the law and WHAT to do.",
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
                            "parent_maintenance"
                        ]
                    },
                    "topics": {
                        "type": "array",
                        "description": "Optional: select 2-3 most relevant general procedures (filing FIR, safety planning, etc). If not specified, only intent-specific guidance is returned.",
                        "items": {
                            "type": "string",
                            "enum": [
                                "file_fir",
                                "get_legal_aid",
                                "court_procedures",
                                "safety_planning",
                                "evidence_collection",
                                "protective_orders"
                            ]
                        },
                        "minItems": 0,
                        "maxItems": 3
                    }
                },
                "required": ["intent"]
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
            "lawyer_playbook": result.get("lawyer_playbook", {}),
            "legal_process": result.get("legal_process", {}),
            "support_organizations": result.get("support_organizations", []),
            "general_procedures": result.get("general_procedures", {})
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
        "parent_maintenance"
    ]


def get_available_topics() -> List[str]:
    """Get list of available procedural topics"""
    return [
        "file_fir",
        "get_legal_aid",
        "court_procedures",
        "safety_planning",
        "evidence_collection",
        "protective_orders"
    ]
