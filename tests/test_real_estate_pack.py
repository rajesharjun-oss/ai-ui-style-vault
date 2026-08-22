import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RealEstatePackTests(unittest.TestCase):
    def test_validator_passes(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/validate-real-estate-pack.py")], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_property_truth_states_exist(self):
        states = set(json.loads((ROOT / "packs/real-estate/state-vocabulary.json").read_text())["states"])
        self.assertTrue({"available","reserved","sold","availability-unknown","price-on-request"}.issubset(states))

    def test_media_truthfulness_is_explicit(self):
        media = (ROOT / "packs/real-estate/property-media-standard.md").read_text().lower()
        self.assertIn("render", media)
        self.assertIn("stock", media)
        self.assertIn("generated", media)
        self.assertIn("actual photography", media)

if __name__ == "__main__":
    unittest.main()
