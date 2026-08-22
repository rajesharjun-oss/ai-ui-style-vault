import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/build-ai-agent-recipes.py"

spec = importlib.util.spec_from_file_location("build_ai_agent_recipes", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class AIAgentRecipeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = module.build_catalog()
        cls.recipes = {recipe["id"]: recipe for recipe in cls.catalog["recipes"]}

    def test_recipe_catalog_has_exact_full_coverage(self):
        self.assertEqual(
            self.catalog["counts"],
            {"designDirection": 300, "reference": 138, "motionPattern": 40, "total": 478},
        )
        self.assertEqual(len(self.catalog["recipes"]), 478)
        self.assertEqual(len(self.recipes), 478)

    def test_every_recipe_is_agent_ready(self):
        required = set(self.catalog["requiredRecipeFields"])
        for recipe in self.catalog["recipes"]:
            self.assertTrue(required.issubset(recipe), recipe["id"])
            for field in [
                "whenToUse",
                "whenNotToUse",
                "compositionInstructions",
                "motionInstructions",
                "assetInstructions",
                "responsiveBehavior",
                "performanceLimits",
                "accessibilityAndFallback",
                "originalityRules",
                "acceptanceCriteria",
            ]:
                self.assertTrue(recipe[field], f"{recipe['id']}:{field}")
            self.assertGreaterEqual(len(recipe["agentPrompt"]), 500, recipe["id"])
            prompt = recipe["agentPrompt"].lower()
            self.assertIn("semantic-relevance", prompt, recipe["id"])
            self.assertIn("original", prompt, recipe["id"])
            self.assertIn("reduced-motion", prompt, recipe["id"])
            self.assertIn("acceptance criteria", prompt, recipe["id"])

    def test_design_direction_examples_materialize_to_prompts(self):
        key = "design:ingredient-component-orbit__warm-material"
        self.assertIn(key, self.recipes)
        recipe = self.recipes[key]
        self.assertEqual(recipe["kind"], "designDirection")
        self.assertIn("restaurant-food", recipe["domains"])
        self.assertIn("Ingredient or Component Orbit", recipe["name"])
        self.assertIn("Warm Material", recipe["name"])

    def test_motionsites_references_are_reference_only_and_originality_gated(self):
        key = "reference:ms-scroll-landing-page"
        self.assertIn(key, self.recipes)
        recipe = self.recipes[key]
        self.assertEqual(recipe["kind"], "reference")
        self.assertEqual(recipe["source"]["usagePolicy"], "reference-only")
        joined = " ".join(recipe["originalityRules"]).lower()
        self.assertIn("never clone", joined)
        self.assertIn("proprietary prompts", joined)

    def test_motion_pattern_has_implementation_and_fallback_instructions(self):
        key = "motion:scroll-scrub-video"
        self.assertIn(key, self.recipes)
        recipe = self.recipes[key]
        self.assertEqual(recipe["kind"], "motionPattern")
        self.assertIn("scroll", " ".join(recipe["motionInstructions"]).lower())
        self.assertIn(
            "poster",
            " ".join(recipe["performanceLimits"] + recipe["assetInstructions"]).lower(),
        )
        self.assertIn("static", " ".join(recipe["accessibilityAndFallback"]).lower())


if __name__ == "__main__":
    unittest.main()
