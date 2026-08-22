import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELECTOR = ROOT / "scripts/select-3d-interaction-plan.py"
ORCHESTRATOR = ROOT / "scripts/vault-build-orchestrator.py"


def profile(name, category, offers, positioning=None, recommended=None):
    data = {
        "status":"ready",
        "officialName":name,
        "businessCategory":category,
        "subcategories":[],
        "offers":[{"name":x,"evidenceStatus":"owner-confirmed"} for x in offers],
        "audiences":["customers"],
        "primaryConversion":{"action":"Enquire","channel":"website","evidenceStatus":"owner-confirmed"},
        "evidenceSources":[{"type":"brief","reference":"owner brief","accessStatus":"user-supplied"}],
        "brandSignals":{"positioning":positioning or [category],"visualSignals":["owner-supplied brand"],"tone":["premium","clear"]},
        "operationalFacts":{"contact":"verified"},
        "researchGaps":[],
        "confidence":{"score":95,"rationale":"Owner-supplied business brief establishes the offer, audience and conversion path."},
        "designSelectionAllowed":True
    }
    if recommended:
        data["recommendedDomainPack"] = recommended
    return data


class ThreeDInteractionIntentTests(unittest.TestCase):
    def run_selector(self, data, *args):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "business-profile.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = subprocess.run([sys.executable, str(SELECTOR), str(path), *args], cwd=ROOT, capture_output=True, text=True)
            return result.returncode, json.loads(result.stdout)

    def test_vehicle_assembly_is_valid_for_automotive_business(self):
        data = profile("Example Motors", "automotive manufacturer", ["cars", "vehicle engineering"])
        code, result = self.run_selector(data, "--subject-class", "vehicle", "--goal", "explain-construction")
        self.assertEqual(code, 0, result)
        ids = [x["id"] for x in result["selectedInteractions"]]
        self.assertIn("object-assembly", ids)
        self.assertIn("exploded-view", ids)

    def test_vehicle_is_blocked_for_tax_firm(self):
        data = profile("Example Tax", "tax advisory firm", ["tax compliance", "tax advisory"])
        code, result = self.run_selector(data, "--subject-class", "vehicle", "--goal", "inspect")
        self.assertNotEqual(code, 0)
        self.assertEqual(result["status"], "blocked")
        self.assertIn("not supported", result["reason"])

    def test_property_navigation_uses_spatial_interactions(self):
        data = profile("Example Homes", "real estate property developer", ["apartments", "property viewings"])
        code, result = self.run_selector(data, "--subject-class", "architecture-property", "--goal", "navigate-space")
        self.assertEqual(code, 0, result)
        ids = [x["id"] for x in result["selectedInteractions"]]
        self.assertIn("guided-world-nodes", ids)
        self.assertIn("camera-preset-navigation", ids)
        self.assertNotIn("object-assembly", ids)

    def test_garment_does_not_accept_mechanical_exploded_view(self):
        data = profile("Example Couture", "fashion couture tailoring", ["suits", "kaftans", "fabric sourcing"])
        code, result = self.run_selector(data, "--subject-class", "garment-textile", "--goal", "inspect", "--requested", "exploded-view")
        self.assertNotEqual(code, 0)
        self.assertTrue(result["rejectedRequests"])

    def test_orchestrator_requires_3d_subject_and_goal(self):
        data = profile("Example Couture", "fashion couture tailoring", ["suits", "kaftans"], recommended="fashion-couture")
        with tempfile.TemporaryDirectory() as td:
            profile_path = Path(td) / "business-profile.json"
            output_path = Path(td) / "vault-build-plan.json"
            profile_path.write_text(json.dumps(data), encoding="utf-8")
            result = subprocess.run([
                sys.executable, str(ORCHESTRATOR), str(profile_path), "--3d", "--output", str(output_path)
            ], cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            summary = json.loads(result.stdout)
            self.assertEqual(summary["status"], "blocked")
            plan = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(plan["threeD"]["status"], "blocked")

    def test_orchestrator_builds_subject_aware_fashion_plan(self):
        data = profile("Example Couture", "fashion couture tailoring", ["suits", "kaftans", "fabric sourcing"], recommended="fashion-couture")
        with tempfile.TemporaryDirectory() as td:
            profile_path = Path(td) / "business-profile.json"
            output_path = Path(td) / "vault-build-plan.json"
            profile_path.write_text(json.dumps(data), encoding="utf-8")
            result = subprocess.run([
                sys.executable, str(ORCHESTRATOR), str(profile_path), "--3d",
                "--3d-subject-class", "garment-textile", "--3d-goal", "inspect",
                "--output", str(output_path)
            ], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            plan = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(plan["status"], "ready")
            self.assertEqual(plan["threeD"]["subjectClass"], "garment-textile")
            self.assertEqual(plan["domain"]["domainPack"], "fashion-couture")


if __name__ == "__main__":
    unittest.main()
