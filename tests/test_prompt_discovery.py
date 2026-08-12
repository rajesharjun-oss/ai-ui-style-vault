from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PromptDiscoveryTests(unittest.TestCase):
    def test_root_discovery_files_exist(self) -> None:
        for name in ["PRD.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md", "PROMPTS.md"]:
            self.assertTrue((ROOT / name).is_file(), name)

    def test_platform_adapters_route_to_canonical_rules(self) -> None:
        for name in ["CLAUDE.md", "GEMINI.md"]:
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("AGENTS.md", text)
            self.assertIn("BUILD_PREMIUM_BUSINESS_WEBSITE.md", text)
            self.assertIn("VISUAL_QA_AND_REVISION.md", text)

    def test_prompt_index_is_complete_and_resolvable(self) -> None:
        payload = json.loads((ROOT / "prompts" / "prompt-index.json").read_text(encoding="utf-8"))
        prompts = payload["prompts"]
        self.assertGreaterEqual(len(prompts), 4)
        ids = [item["id"] for item in prompts]
        self.assertEqual(len(ids), len(set(ids)))
        for item in prompts:
            self.assertTrue((ROOT / item["path"]).is_file(), item["path"])

    def test_business_prompt_contains_research_assets_qa_and_truthful_localhost(self) -> None:
        text = (ROOT / "prompts" / "BUILD_PREMIUM_BUSINESS_WEBSITE.md").read_text(encoding="utf-8")
        lowered = text.lower()
        for phrase in [
            "business_research.md",
            "asset_plan.md",
            "vault_selection.md",
            "verified facts",
            "repeated imagery",
            "1440×1000",
            "390×844",
            "remote or isolated environment",
            "do not claim that your `localhost` is reachable",
        ]:
            self.assertIn(phrase, lowered)

    def test_visual_qa_prompt_requires_revision_not_only_reporting(self) -> None:
        text = (ROOT / "prompts" / "VISUAL_QA_AND_REVISION.md").read_text(encoding="utf-8")
        lowered = text.lower()
        for phrase in [
            "source-code inspection is not a visual review",
            "revision loop",
            "do not stop after listing problems",
            "sticky or fixed headers",
            "horizontal overflow",
            "reduced-motion",
        ]:
            self.assertIn(phrase, lowered)

    def test_agents_routes_business_work_and_visual_qa(self) -> None:
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Prompt Discovery and Routing", text)
        self.assertIn("BUILD_PREMIUM_BUSINESS_WEBSITE.md", text)
        self.assertIn("VISUAL_QA_AND_REVISION.md", text)
        self.assertIn("Localhost Truthfulness Rule", text)


if __name__ == "__main__":
    unittest.main()
