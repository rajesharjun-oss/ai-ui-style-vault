import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "3d-asset-quality.py"


class ThreeDAssetQualityTests(unittest.TestCase):
    def run_obs(self, data):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "obs.json"
            p.write_text(json.dumps(data), encoding="utf-8")
            r = subprocess.run([sys.executable, str(SCRIPT), str(p)], cwd=ROOT, capture_output=True, text=True)
            return r, json.loads(r.stdout)

    def base(self):
        return {
            "mode": "inspectable-object",
            "target": "publish",
            "exactCommercialProductRepresentation": True,
            "referenceCoverage": {"front": True, "back": True, "left": True, "right": True},
            "visual": {
                "silhouetteAccuracy": 4.5,
                "garmentConstructionDetail": 4.5,
                "materialResponse": 4.0,
                "anatomyAndProportion": 4.2,
                "severePrimitiveProxy": False,
                "detachedBodyOrGarmentParts": False,
                "severeGarmentClipping": False,
                "misleadingUnverifiedBackOrSideDetails": False
            },
            "technical": {
                "loads": True,
                "normalsValid": True,
                "fallbackPresent": True,
                "desktopMeasured": True,
                "mobileMeasured": True
            },
            "diagnostics": {"vertices": 18000, "triangles": 32000}
        }

    def test_publish_grade_passes(self):
        r, data = self.run_obs(self.base())
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(data["result"], "pass")

    def test_blocky_placeholder_is_blocked_even_if_glb_loads(self):
        x = self.base()
        x["visual"].update({
            "silhouetteAccuracy": 1,
            "garmentConstructionDetail": 1,
            "materialResponse": 1,
            "anatomyAndProportion": 1,
            "severePrimitiveProxy": True,
            "detachedBodyOrGarmentParts": True
        })
        x["diagnostics"] = {"vertices": 420, "triangles": 780}
        r, data = self.run_obs(x)
        self.assertEqual(r.returncode, 1)
        self.assertEqual(data["result"], "block")
        self.assertIn("severePrimitiveProxy", data["failures"])
        self.assertIn("detachedBodyOrGarmentParts", data["failures"])
        self.assertIn("Preserve the selected 3D mode", data["nextAction"])

    def test_missing_back_and_side_references_blocks_exact_360_publish(self):
        x = self.base()
        x["referenceCoverage"] = {"front": True, "back": False, "left": False, "right": False}
        r, data = self.run_obs(x)
        self.assertEqual(r.returncode, 1)
        self.assertTrue(any("missing reference coverage" in f for f in data["failures"]))

    def test_prototype_can_pass_with_incomplete_reference_coverage_when_labelled(self):
        x = self.base()
        x["target"] = "prototype"
        x["exactCommercialProductRepresentation"] = False
        x["referenceCoverage"] = {"front": True, "back": False, "left": False, "right": False}
        for k in ("silhouetteAccuracy", "garmentConstructionDetail", "materialResponse", "anatomyAndProportion"):
            x["visual"][k] = 2.5
        r, data = self.run_obs(x)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(data["result"], "pass")


if __name__ == "__main__":
    unittest.main()
