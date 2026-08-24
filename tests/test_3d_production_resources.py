import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / "scripts" / "3d-production-resources.py"
CATALOG = ROOT / "3d-production-resources" / "resource-catalog.json"
POLICY = ROOT / "3d-production-resources" / "source-policy.json"
MCP = ROOT / "scripts" / "vault-mcp.py"


class ThreeDProductionResourceTests(unittest.TestCase):
    def run_engine(self, *args):
        result = subprocess.run([sys.executable, str(ENGINE), *args], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def test_validate_and_catalog_depth(self):
        result = self.run_engine("validate")
        data = json.loads(result.stdout)
        self.assertGreaterEqual(data["categories"], 18)
        self.assertGreaterEqual(data["resourceCandidates"], 50)

    def test_photogrammetry_need_routes_correctly(self):
        result = self.run_engine("select", "photogrammetry scan of an approved resort exterior", "--domain", "hospitality")
        data = json.loads(result.stdout)
        self.assertEqual(data["decision"], "3d-production-resource")
        self.assertEqual(data["recommended"]["id"], "photogrammetry-reconstruction")

    def test_terrain_need_routes_to_terrain(self):
        result = self.run_engine("select", "terrain heightmap and landscape for a verified property site", "--domain", "real-estate")
        data = json.loads(result.stdout)
        self.assertEqual(data["recommended"]["id"], "procedural-terrain")

    def test_source_list_license_does_not_flow_to_candidates(self):
        policy = json.loads(POLICY.read_text(encoding="utf-8"))
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        self.assertEqual(policy["sources"][0]["sourceLicense"], "CC0-1.0")
        self.assertFalse(policy["linkedResourcePolicy"]["inheritSourceLicense"])
        for category in catalog["categories"]:
            for candidate in category["resourceCandidates"]:
                self.assertNotEqual(candidate["licenseStatus"], "CC0-1.0")

    def test_skill_contains_rights_and_web_delivery_gates(self):
        result = self.run_engine("skill", "materials-texturing")
        self.assertIn("Rights and provenance gate", result.stdout)
        self.assertIn("Web-delivery gate", result.stdout)
        self.assertIn("discovery candidates, not approved dependencies/assets", result.stdout)

    def test_mcp_surface_includes_3d_production_tools(self):
        result = subprocess.run([sys.executable, str(MCP), "--list-tools"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        tools = {x["name"] for x in json.loads(result.stdout)["tools"]}
        expected = {"get_3d_production_resource", "select_3d_production_resource", "get_3d_production_skill"}
        self.assertTrue(expected.issubset(tools), (expected, tools))


if __name__ == "__main__":
    unittest.main()
