import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ProfessionalServicesPackTests(unittest.TestCase):
    def test_validator_passes(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/validate-professional-services-pack.py")], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_pack_is_business_research_gated(self):
        pack = json.loads((ROOT / "packs/professional-services/pack.json").read_text())
        self.assertIn("business-profile.json", pack["requiredPlanningArtifacts"])
        self.assertTrue(any("invented" in item.lower() for item in pack["rejectConditions"]))

    def test_core_inventory_depth(self):
        blueprints = json.loads((ROOT / "packs/professional-services/page-blueprints.json").read_text())["blueprints"]
        components = json.loads((ROOT / "packs/professional-services/component-manifest.json").read_text())["components"]
        self.assertGreaterEqual(len(blueprints), 6)
        self.assertGreaterEqual(len(components), 8)

if __name__ == "__main__":
    unittest.main()
