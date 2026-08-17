import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/build-ai-agent-recipes.py"

spec = importlib.util.spec_from_file_location("build_ai_agent_recipes", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def test_recipe_catalog_has_exact_full_coverage():
    catalog = module.build_catalog()
    assert catalog["counts"] == {
        "designDirection": 300,
        "reference": 138,
        "motionPattern": 40,
        "total": 478,
    }
    assert len(catalog["recipes"]) == 478
    assert len({recipe["id"] for recipe in catalog["recipes"]}) == 478


def test_every_recipe_is_agent_ready():
    catalog = module.build_catalog()
    required = set(catalog["requiredRecipeFields"])
    for recipe in catalog["recipes"]:
        assert required.issubset(recipe)
        assert recipe["whenToUse"]
        assert recipe["whenNotToUse"]
        assert recipe["compositionInstructions"]
        assert recipe["motionInstructions"]
        assert recipe["assetInstructions"]
        assert recipe["responsiveBehavior"]
        assert recipe["performanceLimits"]
        assert recipe["accessibilityAndFallback"]
        assert recipe["originalityRules"]
        assert recipe["acceptanceCriteria"]
        assert len(recipe["agentPrompt"]) >= 500
        prompt = recipe["agentPrompt"].lower()
        assert "semantic-relevance" in prompt
        assert "original" in prompt
        assert "reduced-motion" in prompt
        assert "acceptance criteria" in prompt


def test_design_direction_examples_materialize_to_prompts():
    recipes = {r["id"]: r for r in module.build_catalog()["recipes"]}
    key = "design:ingredient-component-orbit__warm-material"
    assert key in recipes
    recipe = recipes[key]
    assert recipe["kind"] == "designDirection"
    assert "restaurant-food" in recipe["domains"]
    assert "Ingredient or Component Orbit" in recipe["name"]
    assert "Warm Material" in recipe["name"]


def test_motionsites_references_are_reference_only_and_originality_gated():
    recipes = {r["id"]: r for r in module.build_catalog()["recipes"]}
    key = "reference:ms-scroll-landing-page"
    assert key in recipes
    recipe = recipes[key]
    assert recipe["kind"] == "reference"
    assert recipe["source"]["usagePolicy"] == "reference-only"
    joined = " ".join(recipe["originalityRules"]).lower()
    assert "never clone" in joined
    assert "proprietary prompts" in joined


def test_motion_pattern_has_implementation_and_fallback_instructions():
    recipes = {r["id"]: r for r in module.build_catalog()["recipes"]}
    key = "motion:scroll-scrub-video"
    assert key in recipes
    recipe = recipes[key]
    assert recipe["kind"] == "motionPattern"
    assert "scroll" in " ".join(recipe["motionInstructions"]).lower()
    assert "poster" in " ".join(recipe["performanceLimits"] + recipe["assetInstructions"]).lower()
    assert "static" in " ".join(recipe["accessibilityAndFallback"]).lower()
