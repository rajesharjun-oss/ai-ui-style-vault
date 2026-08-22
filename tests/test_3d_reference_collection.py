from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NORMALIZER = ROOT / "scripts" / "normalize-3d-reference-catalog.py"
spec = importlib.util.spec_from_file_location("normalize_3d", NORMALIZER)
normalizer = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(normalizer)


class ThreeDReferenceCollectionTests(unittest.TestCase):
    def test_seed_catalogue_is_deep_and_includes_refs_gallery(self) -> None:
        data = json.loads((ROOT / "3d/references/collection-seeds.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(data["seeds"]), 30)
        ids = {item["id"] for item in data["seeds"]}
        self.assertIn("refs-gallery-3d", ids)
        self.assertIn("three-examples", ids)
        self.assertIn("polyhaven", ids)

    def test_normalizer_removes_tracking_and_deduplicates(self) -> None:
        first = normalizer.normalize_record(
            {"title":"A", "projectPage":"https://example.com/project/?utm_source=test", "sourceType":"reference-gallery"},
            "test", "2026-08-16T00:00:00Z",
        )
        second = normalizer.normalize_record(
            {"title":"A copy", "projectPage":"https://example.com/project/", "sourceType":"reference-gallery"},
            "test", "2026-08-16T00:00:00Z",
        )
        self.assertEqual(first["projectPage"], second["projectPage"])
        self.assertEqual(first["usagePolicy"], "reference-only")

    def test_normalizer_rejects_copied_code_and_embedded_media(self) -> None:
        with self.assertRaises(ValueError):
            normalizer.normalize_record(
                {"title":"Bad", "projectPage":"https://example.com/x", "html":"<html>copied</html>"},
                "test", "now",
            )
        with self.assertRaises(ValueError):
            normalizer.normalize_record(
                {"title":"Bad", "projectPage":"https://example.com/y", "description":"data:image/png;base64,AAAA"},
                "test", "now",
            )

    def test_refs_gallery_zero_collection_is_reported_truthfully(self) -> None:
        data = json.loads((ROOT / "3d/references/refs-gallery-collection-summary.json").read_text(encoding="utf-8"))
        catalogue = json.loads((ROOT / "3d/references/refs-gallery-3d.json").read_text(encoding="utf-8"))
        self.assertEqual(catalogue["total"], len(catalogue["references"]))
        if catalogue["total"] == 0:
            text = json.dumps(data).lower()
            self.assertTrue("0" in text or "zero" in text or "unavailable" in text or "blocked" in text or "access" in text)


if __name__ == "__main__":
    unittest.main()
