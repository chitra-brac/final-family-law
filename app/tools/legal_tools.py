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
            "description": "Get legal sections, lawyer's playbook, and procedural guidance for a specific intent. Call this for any legal question about family law, violence, or rights.",
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
            "description": "Get step-by-step procedural guidance for specific legal tasks like filing FIR, getting legal aid, or safety planning.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The procedural topic",
                        "enum": [
                            "file_fir",
                            "get_legal_aid",
                            "court_procedures",
                            "safety_planning",
                            "evidence_collection",
                            "protective_orders"
                        ]
                    }
                },
                "required": ["topic"]
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
            "legal_sections": result.get("legal_sections", []),
            "lawyer_playbook": result.get("lawyer_playbook", {}),
            "procedural_guidance": result.get("procedural_guidance", {}),
            "support_organizations": result.get("support_organizations", [])
        }

    elif tool_name == "get_procedural_guidance":
        topic = arguments.get("topic")
        if not topic:
            return {"error": "Topic parameter is required"}

        result = loader.get_procedural_guidance(topic)

        if not result:
            return {
                "error": f"No procedural guidance found for topic: {topic}",
                "available_topics": [
                    "file_fir",
                    "get_legal_aid",
                    "court_procedures",
                    "safety_planning"
                ]
            }

        return {
            "topic": topic,
            "guidance": result
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
