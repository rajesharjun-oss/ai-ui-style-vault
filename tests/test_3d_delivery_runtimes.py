import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / "scripts" / "3d-delivery-runtimes.py"


class ThreeDDeliveryRuntimeTests(unittest.TestCase):
    def run_engine(self, *args):
        r = subprocess.run([sys.executable, str(ENGINE), *args], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return json.loads(r.stdout)

    def test_validate(self):
        data = self.run_engine("validate")
        self.assertEqual(data["runtime"], "google-model-viewer")
        self.assertGreaterEqual(data["profiles"], 5)
        self.assertEqual(data["source"], "google/model-viewer")

    def test_basic_inspection_selects_model_viewer(self):
        data = self.run_engine("select", "rotate zoom and inspect the verified product", "--format", "glb")
        self.assertEqual(data["decision"], "model-viewer")
        self.assertEqual(data["recommended"]["id"], "model-viewer-basic-inspector")

    def test_ar_selects_ar_profile(self):
        data = self.run_engine("select", "view this verified chair in my room with AR placement", "--format", "glb", "--ar")
        self.assertEqual(data["decision"], "model-viewer")
        self.assertEqual(data["recommended"]["id"], "model-viewer-ar-placement")

    def test_annotations_select_annotated_profile(self):
        data = self.run_engine("select", "show verified dimensions and feature annotation hotspots", "--format", "glb")
        self.assertEqual(data["recommended"]["id"], "model-viewer-annotated-inspector")

    def test_complex_world_escalates(self):
        data = self.run_engine("select", "navigable multi object world with custom physics and object interaction", "--format", "glb")
        self.assertEqual(data["decision"], "escalate")
        self.assertEqual(data["target"], "custom-3d-runtime")

    def test_skill_records_peer_and_asset_boundary(self):
        r = subprocess.run([sys.executable, str(ENGINE), "skill", "model-viewer-ar-placement"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("@google/model-viewer", r.stdout)
        self.assertIn("three ^0.183.0", r.stdout)
        self.assertIn("not automatically cleared", r.stdout)


if __name__ == "__main__":
    unittest.main()
