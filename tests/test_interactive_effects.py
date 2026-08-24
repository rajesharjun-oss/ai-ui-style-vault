import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ENGINE=ROOT/"scripts"/"interactive-effects.py"
MCP=ROOT/"scripts"/"vault-mcp.py"

class InteractiveEffectTests(unittest.TestCase):
    def profile(self,domain="saas-technology"):
        if domain=="professional-services":
            return {"status":"ready","officialName":"Example Advisory","businessCategory":"accounting firm","subcategories":["tax advisory","audit"],"offers":["tax compliance"],"audiences":["businesses"],"primaryConversion":{"action":"contact","channel":"email","evidenceStatus":"verified"},"brandSignals":{"positioning":["trusted advice"],"visualSignals":["restrained"],"tone":["professional"]},"operationalFacts":{},"researchGaps":[],"prohibitedAssumptions":[],"confidence":{"score":90,"rationale":"test"},"recommendedDomainPack":domain,"designSelectionAllowed":True}
        return {"status":"ready","officialName":"Example AI","businessCategory":"software platform","subcategories":["workflow automation","data integration"],"offers":["API automation and analytics"],"audiences":["operations teams"],"primaryConversion":{"action":"book demo","channel":"web","evidenceStatus":"verified"},"brandSignals":{"positioning":["connected workflows"],"visualSignals":["technical"],"tone":["precise"]},"operationalFacts":{},"researchGaps":[],"prohibitedAssumptions":[],"confidence":{"score":90,"rationale":"test"},"recommendedDomainPack":domain,"designSelectionAllowed":True}

    def run_select(self,profile,*extra):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"profile.json"; p.write_text(json.dumps(profile),encoding="utf-8")
            r=subprocess.run([sys.executable,str(ENGINE),"select",str(p),*extra],cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stdout+r.stderr)
            return json.loads(r.stdout)

    def test_validator_and_threeui_boundary(self):
        r=subprocess.run([sys.executable,str(ENGINE),"validate"],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        data=json.loads(r.stdout)
        self.assertGreaterEqual(data["effects"],10)
        self.assertGreaterEqual(data["threeUIReferences"],20)

    def test_saas_hero_selects_effect(self):
        data=self.run_select(self.profile())
        self.assertEqual(data["decision"],"effect")
        self.assertIn(data["recommended"]["id"],{"ambient-particle-network","data-topology-field","orbital-product-accent"})

    def test_professional_services_defaults_none(self):
        data=self.run_select(self.profile("professional-services"))
        self.assertEqual(data["decision"],"none")

    def test_skill_contains_fallback_and_qa(self):
        r=subprocess.run([sys.executable,str(ENGINE),"skill","data-topology-field"],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertIn("Reduced motion",r.stdout)
        self.assertIn("effect-qa data-topology-field",r.stdout)

    def test_performance_qa_pass_and_fail(self):
        good={"effectId":"data-topology-field","desktop":{"fps":59,"slowFrameRatio":0.03},"mobile":{"fps":49,"slowFrameRatio":0.10},"reducedMotionFallback":True,"contextLossRecovery":True,"teardownClean":True,"consoleErrors":[]}
        bad={**good,"mobile":{"fps":31,"slowFrameRatio":0.40},"reducedMotionFallback":False}
        with tempfile.TemporaryDirectory() as td:
            goodp=Path(td)/"good.json"; badp=Path(td)/"bad.json"
            goodp.write_text(json.dumps(good)); badp.write_text(json.dumps(bad))
            r1=subprocess.run([sys.executable,str(ENGINE),"qa","data-topology-field",str(goodp)],cwd=ROOT,capture_output=True,text=True)
            r2=subprocess.run([sys.executable,str(ENGINE),"qa","data-topology-field",str(badp)],cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(r1.returncode,0,r1.stdout+r1.stderr)
            self.assertEqual(r2.returncode,1,r2.stdout+r2.stderr)

    def test_mcp_tool_surface(self):
        r=subprocess.run([sys.executable,str(MCP),"--list-tools"],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr)
        tools={x["name"] for x in json.loads(r.stdout)["tools"]}
        expected={"search_vault","get_effect_contract","select_interactive_effect","get_effect_skill"}
        self.assertTrue(expected.issubset(tools), tools)

if __name__=="__main__":
    unittest.main()
