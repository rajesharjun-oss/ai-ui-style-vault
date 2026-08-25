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
        self.assertTrue(data["modeGate"])

    def test_basic_inspection_selects_model_viewer(self):
        data = self.run_engine(
            "select", "rotate zoom and inspect the verified product",
            "--mode", "inspectable-object", "--format", "glb"
        )
        self.assertEqual(data["decision"], "model-viewer")
        self.assertEqual(data["recommended"]["id"], "model-viewer-basic-inspector")

    def test_ar_selects_ar_profile(self):
        data = self.run_engine(
            "select", "view this verified chair in my room with AR placement",
            "--mode", "inspectable-object", "--format", "glb", "--ar"
        )
        self.assertEqual(data["decision"], "model-viewer")
        self.assertEqual(data["recommended"]["id"], "model-viewer-ar-placement")

    def test_annotations_select_annotated_profile(self):
        data = self.run_engine(
            "select", "show verified dimensions and feature annotation hotspots",
            "--mode", "inspectable-object", "--format", "glb"
        )
        self.assertEqual(data["recommended"]["id"], "model-viewer-annotated-inspector")

    def test_configurable_mode_only_considers_config_profiles(self):
        data = self.run_engine(
            "select", "switch verified material variants",
            "--mode", "configurable-object", "--format", "glb"
        )
        self.assertEqual(data["decision"], "model-viewer")
        self.assertEqual(data["recommended"]["id"], "model-viewer-variant-configurator-lite")

    def test_complex_world_mode_escalates_without_forcing_model_viewer(self):
        data = self.run_engine(
            "select", "navigable multi object world with custom physics and object interaction",
            "--mode", "interactive-world", "--format", "glb"
        )
        self.assertEqual(data["decision"], "escalate")
        self.assertEqual(data["target"], "custom-3d-runtime")

    def test_visual_only_mode_does_not_become_rotatable_because_glb_exists(self):
        data = self.run_engine(
            "select", "cinematic decorative hero",
            "--mode", "visual-only", "--format", "glb"
        )
        self.assertEqual(data["decision"], "none")
        self.assertIn("does not require", data["reason"])

    def test_missing_web_asset_blocks_model_viewer_without_changing_mode(self):
        data = self.run_engine(
            "select", "rotate and inspect the garment",
            "--mode", "inspectable-object", "--format", "other"
        )
        self.assertEqual(data["status"], "blocked")
        self.assertEqual(data["mode"], "inspectable-object")
        self.assertIn("production-resource", data["reason"])

    def test_skill_records_mode_gate_peer_and_asset_boundary(self):
        r = subprocess.run([sys.executable, str(ENGINE), "skill", "model-viewer-ar-placement"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Mandatory 3D mode gate", r.stdout)
        self.assertIn("@google/model-viewer", r.stdout)
        self.assertIn("three ^0.183.0", r.stdout)
        self.assertIn("not automatically cleared", r.stdout)


if __name__ == "__main__":
    unittest.main()
