import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "ingest-business-source.py"
FRONT = ROOT / "scripts" / "vault-agent.py"


class BusinessSourceIngestionTests(unittest.TestCase):
    def sample_report(self):
        return {
            "schemaVersion": "1.0.0",
            "source": {
                "type": "google-maps",
                "reference": "https://maps.example/jays-diner",
                "accessStatus": "inspected",
                "capturedAt": None,
            },
            "business": {
                "name": "Jay's Diner",
                "facts": {
                    "address": "Falomo Square Mall, Lagos",
                    "phone": "0915 522 2222",
                    "website": "https://jaysdinerng.com/",
                    "rating": "4.4, shown together with \"505 reviews\"",
                },
                "hours": ["Monday: 12:00 PM – 5:00 AM", "Tuesday: 12:00 PM – 5:00 AM"],
                "offers": ["American-inspired comfort food"],
                "highlights": ["spaghetti", "buffalo wings"],
            },
            "assets": [
                {
                    "id": "photo_01",
                    "url": "https://assets.example/jays.jpg",
                    "alt": "Jay's Diner",
                    "description": "Outdoor seating with red benches.",
                    "evidenceStatus": "verified",
                }
            ],
            "reviews": [
                {
                    "author": "Scarlet",
                    "rating": 4,
                    "relativeTime": "4 months ago",
                    "text": "Tried my favorite spaghetti spot in person today and it did not disappoint 🤭✨\n\nAlways spicy, always hitting right.",
                    "verbatim": True,
                }
            ],
            "evidence": [
                {
                    "claim": "The source identifies the business as Jay's Diner.",
                    "sourceReference": "https://maps.example/jays-diner",
                    "status": "verified",
                }
            ],
            "inference": {
                "businessCategory": "restaurant",
                "subcategories": ["late-night diner"],
                "audiences": ["late-night diners", "families and friends"],
                "primaryConversion": {
                    "action": "visit or order",
                    "channel": "website/phone",
                    "evidenceStatus": "provisional",
                },
                "brandSignals": {
                    "positioning": ["late-night comfort food"],
                    "visualSignals": ["red", "neon", "outdoor seating"],
                    "tone": ["energetic", "casual"],
                },
                "recommendedDomainPack": "fast-casual-commerce",
                "researchGaps": [],
                "prohibitedAssumptions": ["Do not invent a menu beyond evidenced highlights."],
                "confidence": {
                    "score": 92,
                    "rationale": "The source provides identity, contact, hours, reviews and business imagery with strong consistency.",
                },
            },
            "contentPolicy": {
                "facts": "verbatim",
                "reviews": "verbatim",
                "assets": "allowlist-only",
                "unsupportedFields": "omit-or-empty",
            },
        }

    def test_url_mode_creates_research_request_without_fake_scraping(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "https://maps.example/jays", "--output-dir", str(out), "--json"],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 3, result.stdout + result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["status"], "research-required")
            self.assertTrue((out / "business-source-request.json").exists())
            self.assertIn("does not pretend", (ROOT / "prompts" / "BUSINESS_SOURCE_INGESTION.md").read_text(encoding="utf-8"))

    def test_report_materializes_all_source_of_truth_artifacts(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            report_path = td / "report.json"
            report_path.write_text(json.dumps(self.sample_report(), ensure_ascii=False), encoding="utf-8")
            out = td / "materialized"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(report_path), "--output-dir", str(out), "--json"],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            expected = {
                "BUSINESS_SOURCE_REPORT.json",
                "CONTENT_SOURCE_OF_TRUTH.json",
                "ASSET_MANIFEST.json",
                "BUSINESS_RESEARCH.md",
                "business-profile.json",
                "BUILD_PROMPT.md",
                "ingestion-summary.json",
            }
            self.assertTrue(expected.issubset({p.name for p in out.iterdir()}))
            profile = json.loads((out / "business-profile.json").read_text(encoding="utf-8"))
            self.assertEqual(profile["officialName"], "Jay's Diner")
            self.assertTrue(profile["designSelectionAllowed"])
            self.assertEqual(profile["recommendedDomainPack"], "fast-casual-commerce")

    def test_verbatim_reviews_and_asset_allowlist_survive_unchanged(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            report = self.sample_report()
            report_path = td / "report.json"
            report_path.write_text(json.dumps(report, ensure_ascii=False), encoding="utf-8")
            out = td / "out"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(report_path), "--output-dir", str(out)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            truth = json.loads((out / "CONTENT_SOURCE_OF_TRUTH.json").read_text(encoding="utf-8"))
            manifest = json.loads((out / "ASSET_MANIFEST.json").read_text(encoding="utf-8"))
            self.assertEqual(truth["reviews"][0]["text"], report["reviews"][0]["text"])
            self.assertEqual(manifest["policy"], "allowlist-only")
            self.assertEqual(manifest["assets"][0]["url"], report["assets"][0]["url"])
            prompt = (out / "BUILD_PROMPT.md").read_text(encoding="utf-8")
            self.assertIn("🤭✨\n\nAlways spicy", prompt)
            self.assertIn("Do not silently substitute", prompt)

    def test_front_door_exposes_ingest_command(self):
        result = subprocess.run([sys.executable, str(FRONT), "--help"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("ingest", result.stdout)


if __name__ == "__main__":
    unittest.main()
