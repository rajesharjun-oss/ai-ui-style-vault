import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

score_mod = load_script("score_design", "scripts/score-design-selection.py")
section_mod = load_script("section_select", "scripts/select-section-recipes.py")

class DesignSelectionEngineTests(unittest.TestCase):
    def setUp(self):
        self.model = json.loads((ROOT / "system/design-selection-scoring.json").read_text())
        self.themes = json.loads((ROOT / "system/production-theme-archetypes.json").read_text())["themes"]

    def profile(self, category, offers, action, tone, trust="medium"):
        return {
            "status":"ready","designSelectionAllowed":True,"officialName":"Example Co",
            "businessCategory":category,"subcategories":[],"audiences":["customers"],
            "offers":[{"name":x,"evidenceStatus":"owner-confirmed"} for x in offers],
            "primaryConversion":{"action":action,"channel":"web","evidenceStatus":"owner-confirmed"},
            "brandSignals":{"positioning":[],"visualSignals":[],"tone":tone},
            "trustLevel":trust,"contentDensity":"balanced"
        }

    def rank(self, profile, domain, assets="adequate"):
        results=[]
        for theme in self.themes:
            score, breakdown, _ = score_mod.theme_score(theme, profile, domain, self.model, assets, "normal")
            results.append((score,theme["id"],breakdown))
        return sorted(results, reverse=True)

    def test_professional_services_prefers_domain_appropriate_theme(self):
        ranked=self.rank(self.profile("tax advisory",["tax compliance","advisory"],"Book a consultation",["credible","precise"],"high"),"professional-services")
        self.assertIn(ranked[0][1], {"quiet-professional","executive-finance","modern-editorial"})

    def test_hospitality_does_not_default_to_ai_workspace(self):
        ranked=self.rank(self.profile("boutique hotel",["rooms","stays"],"Book a stay",["premium","visual"]),"hospitality","strong")
        self.assertNotEqual(ranked[0][1], "ai-workspace")
        self.assertIn(ranked[0][1], {"cinematic-product","luxury-minimal","modern-editorial"})

    def test_saas_prefers_product_or_technical_theme(self):
        ranked=self.rank(self.profile("B2B SaaS",["workflow automation"],"Request a demo",["technical","polished"]),"saas-technology")
        self.assertIn(ranked[0][1], {"premium-enterprise","technical-developer","ai-workspace"})

    def test_section_library_has_forty_recipes(self):
        catalog=json.loads((ROOT / "system/section-recipes.json").read_text())["recipes"]
        self.assertEqual(len(catalog),40)
        self.assertEqual(set(r["section"] for r in catalog), {"hero","proof","services","gallery","process","pricing","team","faq","cta","footer"})

    def test_section_selector_prefers_product_demo_for_saas_hero(self):
        profile=self.profile("B2B SaaS",["workflow software"],"Start a trial",["technical"])
        catalog=json.loads((ROOT / "system/section-recipes.json").read_text())["recipes"]
        scored=[]
        for r in catalog:
            s=section_mod.score_recipe(r,"hero","saas-technology","trial","balanced",["real workflow","product ui"])
            if s is not None: scored.append((s,r["id"]))
        scored.sort(reverse=True)
        self.assertEqual(scored[0][1],"hero-product-demo")

if __name__ == "__main__":
    unittest.main()
