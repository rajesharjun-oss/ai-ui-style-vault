from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate-content-design.py"
INITIALIZER = ROOT / "scripts" / "initialize-vault-project.py"


GOOD_HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><style>
button { transition: transform 120ms ease; }
@media (prefers-reduced-motion: reduce) { button { transition: none; } }
</style></head><body><main><section><h1 class="text-9xl">Review tax exceptions with less manual work</h1>
<p>Upload transaction schedules, confirm flagged items, and export a documented review.</p>
<button>Upload schedule</button></section>
<section><h2>Prioritise material exceptions</h2><p>See loading, empty, error, success, disabled, permission, and retry states.</p></section>
</main></body></html>"""

BAD_HTML = """<!doctype html><html><body><main>
<section><h1 class="text-9xl">Revolutionize your workflow and unlock your potential with the next-generation all-in-one platform built for the future</h1>
<p>Our seamless and powerful solution is a game-changing platform designed to transform your business, empower your team, supercharge productivity, drive innovation, unlock new possibilities, and take your business to the next level while offering a robust and scalable experience that effortlessly streamlines every imaginable activity across your entire organisation. This paragraph intentionally continues with repetitive, generic, unspecific language so the validator can prove that long copy, generic marketing language, and the absence of a concrete product outcome are detected as a serious content-design failure rather than accepted as polished website copy. It also adds more filler about efficiency, innovation, growth, collaboration, visibility, agility, optimisation, transformation, confidence, opportunity, scalability, adaptability, and success without giving the user a concrete task, measurable result, named workflow, trustworthy proof, or meaningful product detail.</p>
<button>Learn more</button>
""" + "\n".join(f'<div class="card rounded-3xl backdrop-blur">Feature card {i}</div>' for i in range(24)) + """
</section><style>.hero{background:linear-gradient(#55f,#80f)} .card{box-shadow:0 20px 60px #0004}</style></main></body></html>"""


def completed_recipe() -> dict:
    return {
        "schemaVersion": "1.0.0",
        "product": {"type": "saas-web-app"},
        "experience": {},
        "content": {},
        "visualDirection": {},
        "layout": {},
        "components": {},
        "motion": {},
        "accessibility": {},
        "performance": {},
        "assetPolicy": {},
        "quality": {},
    }


def write_completed_artifacts(root: Path) -> None:
    body = (
        "Completed product contract. Primary users, tasks, page purpose, content hierarchy, "
        "selected visual direction, component states, responsive behavior, accessibility, "
        "reduced motion, asset policy, and quality evidence are documented for implementation."
    )
    for name in ["VAULT_SELECTION.md", "BUILD_CONTRACT.md", "CONTENT_PLAN.md"]:
        (root / name).write_text(f"# {name}\n\n{body}\n", encoding="utf-8")
    (root / "design-recipe.json").write_text(json.dumps(completed_recipe()), encoding="utf-8")


class ContentDesignValidatorTests(unittest.TestCase):
    def run_validator(self, root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(root), *extra],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_good_fixture_has_no_errors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_completed_artifacts(root)
            (root / "index.html").write_text(GOOD_HTML, encoding="utf-8")
            result = self.run_validator(root)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("ERRORS=0", result.stdout)
            self.assertIn("VALIDATION=PASS", result.stdout)

    def test_bad_fixture_fails_for_content_and_visual_risk(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "index.html").write_text(BAD_HTML, encoding="utf-8")
            result = self.run_validator(root, "--allow-missing-artifacts")
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("GENERIC_AI_PHRASE", result.stdout)
            self.assertIn("PARAGRAPH_TOO_LONG", result.stdout)
            self.assertIn("CARD_SOUP", result.stdout)
            self.assertIn("GENERIC_VISUAL_RISK", result.stdout)

    def test_json_report_is_written(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "site"
            root.mkdir()
            write_completed_artifacts(root)
            (root / "index.html").write_text(GOOD_HTML, encoding="utf-8")
            report = Path(tmp) / "report.json"
            result = self.run_validator(root, "--json-output", str(report), "--quiet")
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(payload["summary"]["errors"], 0)
            self.assertGreater(payload["sourceFilesScanned"], 0)

    def test_initializer_creates_contract_files_without_overwriting(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            command = [
                sys.executable,
                str(INITIALIZER),
                str(target),
                "--product",
                "Review Tool",
                "--build-type",
                "saas-web-app",
                "--primary-user",
                "reviewer",
                "--top-task",
                "Review exceptions",
            ]
            first = subprocess.run(command, text=True, capture_output=True, check=False)
            self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
            for name in [
                "VAULT_SELECTION.md",
                "BUILD_CONTRACT.md",
                "CONTENT_PLAN.md",
                "design-recipe.json",
                "AI_IMPLEMENTATION_INSTRUCTIONS.md",
            ]:
                self.assertTrue((target / name).exists(), name)
            marker = "DO NOT OVERWRITE"
            (target / "CONTENT_PLAN.md").write_text(marker, encoding="utf-8")
            second = subprocess.run(command, text=True, capture_output=True, check=False)
            self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
            self.assertEqual((target / "CONTENT_PLAN.md").read_text(encoding="utf-8"), marker)


if __name__ == "__main__":
    unittest.main()
