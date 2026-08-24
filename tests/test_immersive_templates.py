import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "immersive-templates.py"


class ImmersiveTemplateTests(unittest.TestCase):
    def profile(self, domain="saas-technology", extra=None):
        data = {
            "status": "ready",
            "designSelectionAllowed": True,
            "businessCategory": "software",
            "subcategories": ["AI automation platform"],
            "offers": ["workflow automation"],
            "audiences": ["business teams"],
            "primaryConversion": {"action": "request demo", "channel": "website", "evidenceStatus": "verified"},
            "brandSignals": {"positioning": ["technology", "innovation"], "visualSignals": [], "tone": ["confident"]},
            "operationalFacts": {},
            "recommendedDomainPack": domain
        }
        if extra:
            data["offers"].extend(extra)
        return data

    def run_script(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=ROOT, capture_output=True, text=True)

    def test_validate(self):
        r = self.run_script("validate")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        data = json.loads(r.stdout)
        self.assertEqual(data["templates"], 6)
        self.assertEqual(data["sources"], 6)

    def test_select_scroll_story(self):
        with tempfile.TemporaryDirectory() as td:
            profile = Path(td) / "profile.json"
            profile.write_text(json.dumps(self.profile(extra=["brand story", "product journey"])), encoding="utf-8")
            r = self.run_script("select", str(profile), "--goal", "continuous scroll product storytelling", "--asset-readiness", "adequate")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            data = json.loads(r.stdout)
            self.assertEqual(data["decision"], "immersive-template")
            self.assertEqual(data["recommended"]["id"], "continuous-scroll-narrative")

    def test_goal_does_not_count_as_business_signal(self):
        with tempfile.TemporaryDirectory() as td:
            p = {
                "status": "ready",
                "designSelectionAllowed": True,
                "businessCategory": "",
                "subcategories": [],
                "offers": [],
                "audiences": [],
                "primaryConversion": {},
                "brandSignals": {},
                "operationalFacts": {},
                "recommendedDomainPack": "saas-technology"
            }
            profile = Path(td) / "profile.json"
            profile.write_text(json.dumps(p), encoding="utf-8")
            r = self.run_script("select", str(profile), "--goal", "storytelling", "--asset-readiness", "adequate")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            data = json.loads(r.stdout)
            self.assertEqual(data["decision"], "none")
            narrative = next(x for x in data["candidates"] if x["id"] == "continuous-scroll-narrative")
            self.assertEqual(narrative["score"], 15)
            self.assertNotIn("business signals: storytelling", narrative["reason"])

    def test_high_performance_rejects_level4_high_cost(self):
        with tempfile.TemporaryDirectory() as td:
            p = self.profile(domain="hospitality", extra=["nature retreat", "landscape"])
            profile = Path(td) / "profile.json"
            profile.write_text(json.dumps(p), encoding="utf-8")
            r = self.run_script("select", str(profile), "--goal", "living nature world", "--performance-priority", "high", "--asset-readiness", "strong")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            data = json.loads(r.stdout)
            self.assertNotEqual((data.get("recommended") or {}).get("id"), "procedural-living-world")

    def test_reference_only_boundary_in_skill(self):
        r = self.run_script("skill", "procedural-living-world")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("reference-only-no-reuse-license", r.stdout)
        self.assertIn("Do not cross this reuse boundary", r.stdout)


if __name__ == "__main__":
    unittest.main()
