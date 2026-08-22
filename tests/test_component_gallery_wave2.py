import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WAVE = ROOT / "references/component-gallery/comparative-wave2.json"


class ComponentGalleryWave2Tests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(WAVE.read_text(encoding="utf-8"))
        self.by_id = {item["id"]: item for item in self.data["components"]}

    def test_wave_contains_all_ten_target_components(self):
        expected = {
            "combobox", "datepicker", "dropdown-menu", "tabs", "toast",
            "tooltip", "popover", "tree-view", "carousel", "navigation"
        }
        self.assertEqual(set(self.by_id), expected)

    def test_semantic_distinctions_are_encoded(self):
        rules = " ".join(self.data["crossComponentHardRules"]).lower()
        self.assertIn("dropdown menu", rules)
        self.assertIn("select", rules)
        self.assertIn("tooltip", rules)
        self.assertIn("popover", rules)
        self.assertIn("tree view", rules)
        self.assertIn("accordion", rules)

    def test_every_component_has_behavior_and_responsive_contract(self):
        for item in self.data["components"]:
            self.assertTrue(item["purpose"], item["id"])
            self.assertGreaterEqual(len(item["requiredStates"]), 3, item["id"])
            self.assertGreaterEqual(len(item["keyboardModel"]), 2, item["id"])
            self.assertGreaterEqual(len(item["responsiveRules"]), 2, item["id"])
            self.assertGreaterEqual(len(item["antiPatterns"]), 2, item["id"])
            self.assertIn("heroUIMatches", item)

    def test_component_gallery_counts_are_preserved(self):
        expected = {
            "combobox": 37, "datepicker": 44, "dropdown-menu": 49, "tabs": 80,
            "toast": 41, "tooltip": 74, "popover": 50, "tree-view": 14,
            "carousel": 22, "navigation": 62,
        }
        for cid, count in expected.items():
            self.assertEqual(self.by_id[cid]["exampleCount"], count)


if __name__ == "__main__":
    unittest.main()
