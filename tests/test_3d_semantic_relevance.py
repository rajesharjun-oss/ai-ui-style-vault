from __future__ import annotations
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "packs/3d-immersive-web/code/semantic-relevance.py"
spec = importlib.util.spec_from_file_location("semantic_relevance", MODULE)
semantic = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(semantic)

class SemanticRelevanceTests(unittest.TestCase):
    def test_pizza_accepts_food_subject(self):
        result = semantic.subject_relevance("pizza restaurant food delivery", "pepperoni pizza and oven")
        self.assertEqual(result["decision"], "candidate")
        self.assertGreaterEqual(result["score"], 4)

    def test_pizza_rejects_ferrari(self):
        result = semantic.subject_relevance("pizza restaurant food delivery", "red Ferrari sports car")
        self.assertEqual(result["decision"], "reject")
        self.assertEqual(result["score"], 0)

    def test_professional_services_rejects_sports_car(self):
        result = semantic.subject_relevance("tax accounting consulting firm", "luxury sports car")
        self.assertEqual(result["decision"], "reject")

    def test_pizza_rejects_unrelated_showroom_background(self):
        result = semantic.scene_relevance(
            "pizza restaurant food delivery",
            {"product":"pepperoni pizza", "environment":"luxury sports car showroom"},
        )
        self.assertEqual(result["decision"], "reject")
        self.assertIn("environment", result["rejectedLayers"])

    def test_pizza_scene_accepts_food_context(self):
        result = semantic.scene_relevance(
            "pizza restaurant food delivery",
            {"product":"pepperoni pizza", "environment":"restaurant interior", "prop":"pizza oven"},
        )
        self.assertEqual(result["decision"], "candidate")

    def test_pack_requires_relevance_contract(self):
        pack = json.loads((ROOT / "packs/3d-immersive-web/pack.json").read_text(encoding="utf-8"))
        self.assertIn("THREE_D_RELEVANCE_CONTRACT.md", pack["requiredPlanningArtifacts"])
        self.assertEqual(pack["semanticRelevanceGate"]["primaryMinimumScore"], 4)

if __name__ == "__main__": unittest.main()
