from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = ROOT / "packs/3d-immersive-web/design-combination-system.json"
SELECTOR = ROOT / "scripts/select-3d-design-ideas.py"


class ThreeDDesignCombinationSystemTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(SYSTEM.read_text(encoding="utf-8"))

    def test_exactly_three_hundred_base_directions(self) -> None:
        scenes = self.data["sceneArchetypes"]
        treatments = self.data["artDirections"]
        self.assertEqual(len(scenes), 30)
        self.assertEqual(len(treatments), 10)
        self.assertEqual(len(scenes) * len(treatments), 300)
        self.assertEqual(self.data["combinationCount"], 300)
        self.assertEqual(len({item["id"] for item in scenes}), 30)
        self.assertEqual(len({item["id"] for item in treatments}), 10)

    def run_selector(self, brief: str, limit: int = 12) -> dict:
        result = subprocess.run(
            [sys.executable, str(SELECTOR), brief, "--limit", str(limit)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def test_pizza_shortlist_only_contains_food_compatible_scenes(self) -> None:
        payload = self.run_selector("premium pizza restaurant with delivery and menu", 20)
        self.assertEqual(payload["detectedDomain"], "restaurant-food")
        self.assertEqual(payload["libraryDirections"], 300)
        self.assertGreater(payload["compatibleDirections"], 0)
        for item in payload["results"]:
            self.assertIn("restaurant-food", item["domains"])
            self.assertEqual(item["semanticGate"], "mandatory")

    def test_tax_firm_does_not_get_product_turntable_or_car_specific_scene(self) -> None:
        payload = self.run_selector("tax accounting audit consulting professional services firm", 40)
        self.assertEqual(payload["detectedDomain"], "professional-services")
        ids = {item["sceneArchetype"] for item in payload["results"]}
        self.assertNotIn("turntable-product-view", ids)
        self.assertNotIn("ar-placement-preview", ids)
        self.assertTrue(ids <= {
            "spatial-timeline",
            "isometric-process-map",
            "globe-network",
            "data-constellation",
            "layered-system-architecture",
            "document-to-data-morph",
            "floating-card-world",
        })

    def test_all_results_include_fallback(self) -> None:
        payload = self.run_selector("real estate architecture property building", 50)
        for item in payload["results"]:
            self.assertTrue(item["fallback"])
            self.assertTrue(item["purpose"])


if __name__ == "__main__":
    unittest.main()
