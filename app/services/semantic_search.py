"""
Semantic Search Service
Uses GPT-4o-mini for fast, cheap act and section discovery
"""

from openai import OpenAI
from typing import List, Dict, Any
import json
from app.config import get_settings
from app.services.data_loader import get_data_loader

settings = get_settings()


class SemanticSearchService:
    """Fast semantic search using GPT-4o-mini"""

    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = "gpt-4o-mini"  # Cheap and fast
        self.loader = get_data_loader()

    def search_relevant_acts(self, user_query: str, top_k: int = 3) -> List[str]:
        """
        Find most relevant acts for a user query

        Args:
            user_query: The user's question in Bengali
            top_k: Number of acts to return (default 3)

        Returns:
            List of act_ids
        """
        # Get all act summaries
        act_summaries = []
        for act_id, summary_data in self.loader.act_summaries.items():
            act_summaries.append({
                "act_id": act_id,
                "title": summary_data.get("act_title", ""),
                "summary": summary_data.get("summary", ""),
            })

        # Create prompt for GPT-4o-mini
        prompt = f"""You are a legal research assistant. Given a user's question and a list of Bangladesh legal acts, identify the {top_k} most relevant acts.

User Question: {user_query}

Acts:
{json.dumps(act_summaries, ensure_ascii=False, indent=2)}

Return a JSON object with an "act_ids" array, like: {{"act_ids": ["1063", "835"]}}
Pick the {top_k} most relevant acts. Be precise."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a JSON-only assistant. Return only valid JSON arrays, no explanation."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                max_tokens=100,
                response_format={"type": "json_object"}
            )

            result = response.choices[0].message.content.strip()
            data = json.loads(result)

            # Extract act_ids from JSON object
            act_ids = data.get("act_ids", data.get("acts", []))

            return act_ids[:top_k]

        except Exception as e:
            print(f"Act search error: {e}")
            print(f"Response: {response.choices[0].message.content if 'response' in locals() else 'N/A'}")
            # Fallback to empty list
            return []

    def get_sections_from_act(
        self,
        act_id: str,
        user_query: str,
        top_k: int = 4
    ) -> List[Dict[str, Any]]:
        """
        Find most relevant sections from a specific act

        Args:
            act_id: The act ID to search within
            user_query: The user's question in Bengali
            top_k: Number of sections to return (default 4)

        Returns:
            List of full section objects
        """
        # Get all sections from this act
        if act_id not in self.loader.sections:
            return []

        act_sections = self.loader.sections[act_id]

        # Create lightweight section list with summaries
        section_list = []
        for section_num, section_data in act_sections.items():
            section_list.append({
                "section_number": section_num,
                "title": section_data.get("section_title", ""),
                "summary": section_data.get("semantic_summary", ""),
            })

        # Prompt for GPT-4o-mini
        prompt = f"""You are a legal research assistant. Given a user's question and a list of sections from a Bangladesh law, identify the {top_k} most relevant sections.

User Question: {user_query}

Sections:
{json.dumps(section_list, ensure_ascii=False, indent=2)}

Return a JSON object with a "section_numbers" array (as strings), like: {{"section_numbers": ["৩", "১৪", "২০"]}}
Pick the {top_k} most relevant sections. Be precise."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a JSON-only assistant. Return only valid JSON objects, no explanation."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                max_tokens=150,
                response_format={"type": "json_object"}
            )

            result = response.choices[0].message.content.strip()
            data = json.loads(result)
            section_numbers = data.get("section_numbers", data.get("sections", []))

            # Fetch full section data
            full_sections = []
            for section_num in section_numbers[:top_k]:
                if section_num in act_sections:
                    section_data = act_sections[section_num]
                    full_sections.append({
                        "act_id": act_id,
                        "act_title": section_data.get("act_title", ""),
                        "section_number": section_num,
                        "section_title": section_data.get("section_title", ""),
                        "section_text": section_data.get("section_text", ""),
                        "semantic_summary": section_data.get("semantic_summary", ""),
                    })

            return full_sections

        except Exception as e:
            print(f"Section search error: {e}")
            return []


# Singleton instance
_search_service = None


def get_search_service() -> SemanticSearchService:
    """Get singleton search service instance"""
    global _search_service
    if _search_service is None:
        _search_service = SemanticSearchService()
    return _search_service
