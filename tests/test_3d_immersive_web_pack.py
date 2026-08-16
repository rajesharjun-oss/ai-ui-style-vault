from __future__ import annotations
import json, subprocess, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ThreeDImmersiveWebPackTests(unittest.TestCase):
    def load(self, relative): return json.loads((ROOT / relative).read_text(encoding="utf-8"))
    def test_validator_passes(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/validate-3d-immersive-pack.py")], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("THREE_D_PACK_VALIDATION=PASS", result.stdout)
    def test_catalogue_depth(self):
        self.assertGreaterEqual(len(self.load("packs/3d-immersive-web/style-families.json")["families"]), 20)
        self.assertGreaterEqual(len(self.load("packs/3d-immersive-web/page-blueprints.json")["blueprints"]), 10)
        self.assertGreaterEqual(len(self.load("packs/3d-immersive-web/component-manifest.json")["components"]), 25)
        self.assertGreaterEqual(len(self.load("packs/3d-immersive-web/interaction-patterns.json")["patterns"]), 30)
        self.assertGreaterEqual(len(self.load("3d/source-catalog.json")["sources"]), 25)
        self.assertGreaterEqual(len(self.load("3d/techniques/technique-catalog.json")["techniques"]), 30)
    def test_reference_policy(self):
        payload = self.load("3d/references/refs-gallery-3d.json")
        self.assertEqual(payload["sourceUrl"], "https://refs.gallery/category/3d")
        self.assertEqual(payload["total"], len(payload["references"]))
        for item in payload["references"]: self.assertEqual(item["usagePolicy"], "reference-only")
    def test_routing(self):
        prompt = next(item for item in self.load("prompts/prompt-index.json")["prompts"] if item["id"] == "build-3d-immersive-web-experience")
        self.assertEqual(prompt["requiresCapabilityPack"], "3d-immersive-web")
        for relative in ["AGENTS.md", "PROMPTS.md", "PACKS.md", "CLAUDE.md", "GEMINI.md"]:
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md", text)
            self.assertIn("3d-immersive-web", text)
    def test_selector(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/select-3d-references.py"), "premium product configurator", "--style-family", "product-configurator", "--limit", "5"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertGreater(json.loads(result.stdout)["count"], 0)
if __name__ == "__main__": unittest.main()
