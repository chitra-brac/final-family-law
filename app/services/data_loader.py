"""
Data Loader Service
Loads legal knowledge JSON files into memory for fast retrieval
"""

import json
import os
from typing import Dict, List, Any
from pathlib import Path


class DataLoader:
    """
    Loads and provides access to legal knowledge data
    All data loaded into memory for fast retrieval (<10ms)
    """

    def __init__(self, data_dir: str = "data"):
        """
        Initialize data loader

        Args:
            data_dir: Directory containing JSON data files
        """
        self.data_dir = Path(data_dir)
        self.sections: Dict[str, Dict[str, Any]] = {}  # family_laws_final.json
        self.intent_mappings: Dict[str, Any] = {}  # INTENT_MAPPINGS.json
        self.procedural_knowledge: Dict[str, Any] = {}  # procedural_knowledge.json
        self.act_summaries: Dict[str, Any] = {}  # act_summaries.json

        self._load_all()

    def _load_all(self):
        """Load all JSON files into memory"""
        print("Loading legal knowledge data...")

        # Load family_laws_final.json
        self._load_legal_sections()

        # Load INTENT_MAPPINGS.json
        self._load_intent_mappings()

        # Load procedural_knowledge.json
        self._load_procedural_knowledge()

        # Load act_summaries.json
        self._load_act_summaries()

        print(f"✓ Loaded {len(self.sections)} legal sections")
        print(f"✓ Loaded {len(self.intent_mappings)} intent mappings")
        print(f"✓ Loaded {len(self.act_summaries)} act summaries")
        print("✓ Legal knowledge data loaded successfully")

    def _load_legal_sections(self):
        """
        Load family_laws_final.json
        Organizes sections by act_id and section_number for fast lookup
        """
        file_path = self.data_dir / "family_laws_final.json"

        with open(file_path, "r", encoding="utf-8") as f:
            sections_list = json.load(f)

        # Organize by act_id and section_number for O(1) lookup
        for section in sections_list:
            act_id = section.get("act_id")
            section_number = section.get("section_number")

            if act_id and section_number:
                # Create nested dict structure: sections[act_id][section_number] = section
                if act_id not in self.sections:
                    self.sections[act_id] = {}
                self.sections[act_id][section_number] = section

    def _load_intent_mappings(self):
        """Load INTENT_MAPPINGS.json"""
        file_path = self.data_dir / "INTENT_MAPPINGS.json"

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Extract just the intents dictionary
            self.intent_mappings = data.get("intents", {})

    def _load_procedural_knowledge(self):
        """Load procedural_knowledge.json"""
        file_path = self.data_dir / "procedural_knowledge.json"

        with open(file_path, "r", encoding="utf-8") as f:
            self.procedural_knowledge = json.load(f)

    def _load_act_summaries(self):
        """Load act_summaries.json"""
        file_path = self.data_dir / "act_summaries.json"

        with open(file_path, "r", encoding="utf-8") as f:
            summaries_list = json.load(f)

        # Organize by act_id for fast lookup
        for summary in summaries_list:
            act_id = summary.get("act_id")
            if act_id:
                self.act_summaries[act_id] = summary

    def get_legal_knowledge(self, intent: str) -> Dict[str, Any]:
        """
        Get legal knowledge for a specific intent
        Returns sections, playbook, and procedural guidance

        Args:
            intent: Intent category (e.g., "rape_sexual_violence")

        Returns:
            Dict containing:
            - legal_sections: List of relevant legal section texts
            - lawyer_playbook: Strategic guidance for lawyers
            - procedural_guidance: Step-by-step procedures
            - support_organizations: List of organizations
        """
        result = {
            "legal_sections": [],
            "lawyer_playbook": {},
            "procedural_guidance": {},
            "support_organizations": [],
        }

        # 1. Get section references from INTENT_MAPPINGS
        if intent not in self.intent_mappings:
            return result  # Intent not found

        intent_data = self.intent_mappings[intent]
        mandatory_sections = intent_data.get("mandatory_sections", [])

        # 2. Fetch full section texts
        for section_ref in mandatory_sections:
            act_id = section_ref.get("act_id")
            section_number = section_ref.get("section_number")

            # Look up full section from family_laws_final
            if act_id in self.sections and section_number in self.sections[act_id]:
                full_section = self.sections[act_id][section_number]
                result["legal_sections"].append({
                    "act_id": act_id,
                    "act_title": full_section.get("act_title", ""),
                    "section_number": section_number,
                    "section_title": full_section.get("section_title", ""),
                    "section_text": full_section.get("section_text", ""),
                    "semantic_summary": full_section.get("semantic_summary", ""),
                })

        # 3. Get lawyer's playbook from procedural_knowledge
        intent_specific = self.procedural_knowledge.get("intent_specific", {})
        if intent in intent_specific:
            intent_knowledge = intent_specific[intent]
            result["lawyer_playbook"] = intent_knowledge.get("lawyer_playbook", {})
            result["procedural_guidance"] = intent_knowledge.get("legal_process", {})
            result["support_organizations"] = intent_knowledge.get("support_organizations", [])

        return result

    def get_procedural_guidance(self, topic: str) -> Dict[str, Any]:
        """
        Get general procedural guidance

        Args:
            topic: Topic name (e.g., "file_fir", "get_legal_aid")

        Returns:
            Dict with procedural steps and guidance
        """
        general_procedures = self.procedural_knowledge.get("general_procedures", {})
        return general_procedures.get(topic, {})

    def get_support_resources(self, resource_type: str = "all") -> Dict[str, Any]:
        """
        Get support resources (organizations, helplines)

        Args:
            resource_type: "legal_aid", "shelter", "helpline", or "all"

        Returns:
            Dict with organizations and emergency contacts
        """
        # Collect from procedural knowledge
        resources = {
            "organizations": [],
            "emergency_contacts": [],
        }

        # Get from general procedures (e.g., get_legal_aid)
        legal_aid_info = self.get_procedural_guidance("get_legal_aid")
        if "who_provides" in legal_aid_info:
            resources["organizations"].extend(legal_aid_info["who_provides"])

        # Get emergency contacts from safety_planning
        safety_info = self.get_procedural_guidance("safety_planning")
        if "immediate_safety" in safety_info:
            emergency_contacts = safety_info["immediate_safety"].get("emergency_contacts", [])
            resources["emergency_contacts"].extend(emergency_contacts)

        # Add common emergency numbers
        if not resources["emergency_contacts"]:
            resources["emergency_contacts"] = [
                {"name": "জাতীয় জরুরি", "number": "999", "available": "২৪/৭"},
                {"name": "মহিলা ও শিশু হেল্পলাইন", "number": "10921", "available": "২৪/৭"},
            ]

        # Filter by type if specified
        if resource_type != "all":
            # TODO: Implement filtering by resource type
            pass

        return resources

    def get_act_summary(self, act_id: str) -> Dict[str, Any]:
        """
        Get summary of a specific act

        Args:
            act_id: Act ID

        Returns:
            Dict with act summary
        """
        return self.act_summaries.get(act_id, {})


# Global data loader instance
_data_loader: DataLoader | None = None


def get_data_loader() -> DataLoader:
    """
    Get global data loader instance
    Lazy initialization on first call
    """
    global _data_loader
    if _data_loader is None:
        _data_loader = DataLoader()
    return _data_loader
