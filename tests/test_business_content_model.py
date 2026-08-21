import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate-business-content-model.py"
FRONT = ROOT / "scripts" / "vault-agent.py"


class BusinessContentModelTests(unittest.TestCase):
    def sample_report(self):
        return {
            "schemaVersion": "1.0.0",
            "source": {"type": "google-maps", "reference": "https://maps.example/jays", "accessStatus": "inspected", "capturedAt": None},
            "business": {
                "name": "Jay's Diner",
                "facts": {"address": "Falomo Square Mall, Lagos", "phone": "0915 522 2222", "rating": "4.4, shown together with \"505 reviews\""},
                "hours": ["Monday: 12:00 PM – 5:00 AM"],
                "offers": ["American-inspired comfort food"],
                "highlights": ["spaghetti", "buffalo wings"],
            },
            "assets": [{"id": "photo_01", "url": "https://assets.example/1.jpg", "alt": "Jay's Diner", "description": "Outdoor seating.", "evidenceStatus": "verified"}],
            "reviews": [{"author": "Scarlet", "rating": 4, "relativeTime": "4 months ago", "text": "Great food 🤭✨\n\nStill my favorite.", "verbatim": True}],
            "evidence": [{"claim": "Business identity", "sourceReference": "https://maps.example/jays", "status": "verified"}],
            "inference": {
                "businessCategory": "restaurant",
                "subcategories": ["late-night diner"],
                "audiences": ["late-night diners"],
                "primaryConversion": {"action": "visit or order", "channel": "phone", "evidenceStatus": "provisional"},
                "brandSignals": {"positioning": ["late-night comfort food"], "visualSignals": ["red", "neon"], "tone": ["energetic"]},
                "recommendedDomainPack": "fast-casual-commerce",
                "researchGaps": [],
                "prohibitedAssumptions": [],
                "confidence": {"score": 90, "rationale": "Strong source evidence across identity, hours, images and reviews."},
            },
            "contentPolicy": {"facts": "verbatim", "reviews": "verbatim", "assets": "allowlist-only", "unsupportedFields": "omit-or-empty"},
        }

    def test_generator_creates_public_and_admin_models(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            report = td / "BUSINESS_SOURCE_REPORT.json"
            report.write_text(json.dumps(self.sample_report(), ensure_ascii=False), encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(report), "--json"], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            for name in ["BUSINESS_ENTITY_MODEL.json", "PUBLIC_CONTENT_MODEL.json", "ADMIN_CMS_MODEL.json", "CMS_BUILD_CONTRACT.md", "content-model-summary.json"]:
                self.assertTrue((td / name).exists(), name)
            public = json.loads((td / "PUBLIC_CONTENT_MODEL.json").read_text(encoding="utf-8"))
            admin = json.loads((td / "ADMIN_CMS_MODEL.json").read_text(encoding="utf-8"))
            self.assertIn("reviews", public["sectionEligibility"])
            self.assertIn("gallery", public["sectionEligibility"])
            enabled = {x["id"] for x in admin["enabledModules"]}
            self.assertIn("hours", enabled)
            self.assertIn("reviews", enabled)

    def test_reviews_are_moderation_only_and_verbatim(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            report = td / "BUSINESS_SOURCE_REPORT.json"
            data = self.sample_report()
            report.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            subprocess.run([sys.executable, str(SCRIPT), str(report)], cwd=ROOT, check=True, capture_output=True, text=True)
            model = json.loads((td / "BUSINESS_ENTITY_MODEL.json").read_text(encoding="utf-8"))
            review = next(e for e in model["entities"] if e["type"] == "review")
            self.assertEqual(review["adminCapability"], "moderation-only")
            self.assertEqual(review["fields"]["text"], data["reviews"][0]["text"])

    def test_unsupported_operational_modules_are_not_generated(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            report = td / "BUSINESS_SOURCE_REPORT.json"
            report.write_text(json.dumps(self.sample_report(), ensure_ascii=False), encoding="utf-8")
            subprocess.run([sys.executable, str(SCRIPT), str(report)], cwd=ROOT, check=True, capture_output=True, text=True)
            admin = json.loads((td / "ADMIN_CMS_MODEL.json").read_text(encoding="utf-8"))
            forbidden = set(admin["forbiddenSyntheticModules"])
            self.assertTrue({"orders", "revenue", "inventory", "bookings", "system-health", "security-log"}.issubset(forbidden))
            enabled = {x["id"] for x in admin["enabledModules"]}
            self.assertFalse(enabled & forbidden)

    def test_front_door_exposes_model_command(self):
        result = subprocess.run([sys.executable, str(FRONT), "--help"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("model", result.stdout)


if __name__ == "__main__":
    unittest.main()
