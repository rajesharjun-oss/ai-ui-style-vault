import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "agent-runtime-index.json"
START = ROOT / "AI_START_HERE.md"
AGENTS = ROOT / "AGENTS.md"
FRONT = ROOT / "scripts/vault-agent.py"


class AgentUsabilityTests(unittest.TestCase):
    def test_runtime_index_enforces_progressive_disclosure(self):
        data = json.loads(RUNTIME.read_text(encoding="utf-8"))
        self.assertIn("route", data["stages"])
        self.assertIn("plan", data["stages"])
        self.assertIn("qa", data["stages"])
        joined = " ".join(data["contextBudgetRules"]).lower()
        self.assertIn("never preload all 478", joined)
        self.assertIn("never preload all 2,671", joined)

    def test_start_here_exposes_one_front_door(self):
        text = START.read_text(encoding="utf-8")
        self.assertIn("scripts/vault-agent.py", text)
        self.assertIn("progressive disclosure", text.lower())
        self.assertIn("vault-build-plan.json", text)

    def test_agents_keeps_critical_contracts(self):
        text = AGENTS.read_text(encoding="utf-8")
        for required in [
            "EVENT_BUILD_CONTRACT.md",
            "COMMERCE_BUILD_CONTRACT.md",
            "THREE_D_RELEVANCE_CONTRACT.md",
            "VISUAL_QA_AND_REVISION.md",
            "Localhost Truthfulness Rule",
        ]:
            self.assertIn(required, text)

    def test_single_front_door_help_works(self):
        result = subprocess.run([sys.executable, str(FRONT), "--help"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("plan", result.stdout)
        self.assertIn("component", result.stdout)
        self.assertIn("critic", result.stdout)


if __name__ == "__main__":
    unittest.main()
