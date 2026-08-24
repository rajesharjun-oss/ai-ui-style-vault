import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "classify-3d-mode.py"


class ThreeDModeClassificationTests(unittest.TestCase):
    def run_script(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=ROOT, capture_output=True, text=True)

    def classify(self, need, *args):
        r = self.run_script("classify", need, *args)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return json.loads(r.stdout)

    def test_validate_catalog(self):
        r = self.run_script("validate")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        data = json.loads(r.stdout)
        self.assertEqual(data["modes"], 7)
        self.assertEqual(data["levels"], list(range(7)))

    def test_fashion_mannequin_swipe_is_inspectable(self):
        data = self.classify(
            "3D mannequin wearing the dress; customers can swipe or drag to rotate 360 and inspect the front, sides and back",
            "--subject-class", "garment-textile"
        )
        self.assertEqual(data["mode"]["id"], "inspectable-object")
        self.assertEqual(data["userControl"], "bounded-orbit-drag-swipe-zoom")
        self.assertIn("model-viewer", data["preferredDelivery"])
        self.assertEqual(data["assetPlan"]["action"], "produce-or-source-approved-3d-asset")
        self.assertTrue(data["formatDoesNotDetermineMode"])

    def test_ready_glb_changes_asset_action_not_mode(self):
        data = self.classify(
            "customers can drag and rotate the dress mannequin 360 to inspect it",
            "--subject-class", "garment-textile",
            "--asset-format", "glb",
            "--asset-readiness", "strong"
        )
        self.assertEqual(data["mode"]["id"], "inspectable-object")
        self.assertEqual(data["assetPlan"]["action"], "validate-web-asset-and-select-runtime")

    def test_glb_does_not_force_rotation_for_cinematic_story(self):
        data = self.classify(
            "cinematic scroll animation with an authored camera path around the fashion model",
            "--subject-class", "garment-textile",
            "--asset-format", "glb",
            "--asset-readiness", "strong"
        )
        self.assertEqual(data["mode"]["id"], "authored-animation")
        self.assertNotEqual(data["userControl"], "bounded-orbit-drag-swipe-zoom")

    def test_configuration_outranks_inspection(self):
        data = self.classify(
            "rotate the dress 360 and change fabric colour using verified swatches",
            "--subject-class", "garment-textile",
            "--asset-format", "glb",
            "--asset-readiness", "strong"
        )
        self.assertEqual(data["mode"]["id"], "configurable-object")

    def test_property_walkthrough_is_spatial_even_with_glb(self):
        data = self.classify(
            "walk through the verified apartment room to room as a property tour",
            "--subject-class", "architecture-property",
            "--asset-format", "glb",
            "--asset-readiness", "strong"
        )
        self.assertEqual(data["mode"]["id"], "spatial-exploration")
        self.assertEqual(data["nextStage"], "custom-3d-runtime")

    def test_generic_3d_request_does_not_infer_rotation(self):
        data = self.classify("make it 3D")
        self.assertEqual(data["status"], "needs-clarification")
        self.assertIsNone(data["mode"])
        self.assertIn("Do not infer rotatable GLB/GLTF", data["reason"])

    def test_3d_hero_defaults_visual_only_not_rotatable(self):
        data = self.classify("make the hero 3D")
        self.assertEqual(data["mode"]["id"], "visual-only")
        self.assertEqual(data["userControl"], "none-or-passive-pointer-response")
        self.assertNotIn("model-viewer", data["preferredDelivery"])


if __name__ == "__main__":
    unittest.main()
