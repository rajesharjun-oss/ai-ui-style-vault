import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "references/component-gallery/component-catalog.json"
SYSTEMS = ROOT / "references/component-gallery/design-system-summary.json"
SELECTOR = ROOT / "scripts/select-component-intelligence.py"


class ComponentGalleryReferenceTests(unittest.TestCase):
    def test_sixty_canonical_components(self):
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        items = data["components"]
        self.assertEqual(len(items), 60)
        self.assertEqual(len({x["id"] for x in items}), 60)
        self.assertEqual(data["source"]["componentCount"], 60)
        self.assertEqual(data["source"]["designSystemCount"], 95)
        self.assertEqual(data["source"]["exampleCount"], 2671)

    def test_design_system_summary_has_cross_system_depth(self):
        data = json.loads(SYSTEMS.read_text(encoding="utf-8"))
        self.assertEqual(data["designSystems"], 95)
        self.assertGreaterEqual(data["technologyCounts"]["React"], 50)
        self.assertGreaterEqual(data["featureCounts"]["Code examples"], 79)
        self.assertGreaterEqual(len(data["highSignalSystems"]), 10)

    def test_autosuggest_maps_to_combobox_and_heroui(self):
        result = subprocess.run(
            [sys.executable, str(SELECTOR), "autosuggest"], cwd=ROOT, capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["selected"][0]["component"], "combobox")
        self.assertTrue({"combo-box", "autocomplete"} & set(payload["selected"][0]["heroUIMatches"]))

    def test_dropdown_menu_is_not_select(self):
        result = subprocess.run(
            [sys.executable, str(SELECTOR), "dropdown menu actions"], cwd=ROOT, capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        ids = [x["component"] for x in payload["selected"][:3]]
        self.assertIn("dropdown-menu", ids)


if __name__ == "__main__":
    unittest.main()
