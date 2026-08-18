import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "references/component-gallery/component-catalog.json").read_text(encoding="utf-8"))
RULES = json.loads((ROOT / "references/component-gallery/contract-rules.json").read_text(encoding="utf-8"))
HEROUI = json.loads((ROOT / "references/heroui-v3/behavior-contracts.json").read_text(encoding="utf-8"))
RESOLVER = ROOT / "scripts/resolve-component-contract.py"


class CanonicalComponentContractTests(unittest.TestCase):
    def run_resolver(self, term):
        result = subprocess.run([sys.executable, str(RESOLVER), term], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(result.stdout)["contract"]

    def test_all_60_components_have_archetypes(self):
        items = CATALOG["components"]
        self.assertEqual(len(items), 60)
        for item in items:
            self.assertIn(item["id"], RULES["componentArchetypes"])
            self.assertIn(RULES["componentArchetypes"][item["id"]], RULES["archetypes"])

    def test_critical_distinctions_exist(self):
        distinctions = RULES["criticalDistinctions"]
        for key in ["button-vs-link","select-vs-dropdown-menu","tooltip-vs-popover","alert-vs-toast","tabs-vs-segmented-control","spinner-vs-progress-bar","accordion-vs-tree-view"]:
            self.assertIn(key, distinctions)

    def test_alias_resolves_to_correct_component(self):
        self.assertEqual(self.run_resolver("autosuggest")["id"], "combobox")
        self.assertEqual(self.run_resolver("snackbar")["id"], "toast")
        self.assertEqual(self.run_resolver("dropzone")["id"], "file-upload")

    def test_select_and_menu_have_different_contracts(self):
        select = self.run_resolver("select")
        menu = self.run_resolver("dropdown menu")
        self.assertEqual(select["archetype"], "selection")
        self.assertEqual(menu["archetype"], "overlay")

    def test_heroui_behavior_contracts_are_deep(self):
        items = HEROUI["components"]
        self.assertGreaterEqual(len(items), 25)
        by_id = {x["id"]: x for x in items}
        for component in ["button","modal","table","select","tabs","autocomplete","date-picker","toast"]:
            self.assertIn(component, by_id)
            self.assertGreaterEqual(len(by_id[component]["requiredBehavior"]), 3)
            self.assertGreaterEqual(len(by_id[component]["states"]), 2)


if __name__ == "__main__":
    unittest.main()
