import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "references/heroui-v3/component-catalog.json"
HOOKS = ROOT / "references/heroui-v3/hooks-catalog.json"
SELECTOR = ROOT / "scripts/select-heroui-components.py"


class HeroUIReferenceTests(unittest.TestCase):
    def test_all_82_component_families_are_catalogued(self):
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        names = [name for values in data["categories"].values() for name in values]
        self.assertEqual(len(names), 82)
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(data["upstream"]["componentCount"], 82)

    def test_all_10_public_hooks_are_catalogued(self):
        data = json.loads(HOOKS.read_text(encoding="utf-8"))
        self.assertEqual(data["hookCount"], 10)
        self.assertEqual(len(data["hooks"]), 10)

    def test_selector_returns_search_and_table_primitives(self):
        result = subprocess.run(
            [sys.executable, str(SELECTOR), "search filters table"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        selected = {item["component"] for item in payload["selected"]}
        self.assertIn("search-field", selected)
        self.assertIn("table", selected)

    def test_non_react_uses_behavior_contract_only(self):
        result = subprocess.run(
            [sys.executable, str(SELECTOR), "settings dialog", "--stack", "non-react"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["adoptionMode"], "behavior-contract-only")


if __name__ == "__main__":
    unittest.main()
