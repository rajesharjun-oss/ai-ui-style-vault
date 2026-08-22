import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCHMARKS = ROOT / "benchmarks/component-benchmarks.json"
CRITIC = ROOT / "scripts/run-design-critic.py"


def load_critic():
    spec = importlib.util.spec_from_file_location("design_critic", CRITIC)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


class ComponentBenchmarksAndCriticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(BENCHMARKS.read_text(encoding="utf-8"))
        cls.by_id = {x["id"]: x for x in cls.data["benchmarks"]}
        cls.critic = load_critic()

    def test_suite_contains_ten_realistic_benchmarks(self):
        self.assertEqual(len(self.by_id), 10)
        self.assertIn("b02-saas-admin-data-table", self.by_id)
        self.assertIn("b10-automotive-3d-configurator", self.by_id)

    def test_every_benchmark_has_component_and_mobile_contracts(self):
        for item in self.by_id.values():
            self.assertGreaterEqual(len(item["requiredComponents"]), 5, item["id"])
            self.assertGreaterEqual(len(item["criticalStates"]), 3, item["id"])
            self.assertGreaterEqual(len(item["forbiddenSubstitutions"]), 2, item["id"])
            self.assertGreaterEqual(len(item["mobileExpectations"]), 2, item["id"])

    def test_automotive_benchmark_is_subject_aware(self):
        cfg = self.by_id["b10-automotive-3d-configurator"]["required3D"]
        self.assertEqual(cfg["subjectClass"], "vehicle")
        self.assertIn("bounded-orbit-inspection", cfg["allowedInteractions"])
        self.assertIn("material-switch", cfg["allowedInteractions"])

    def test_good_dashboard_observations_pass(self):
        benchmark = self.by_id["b02-saas-admin-data-table"]
        plan = {"threeD": {"status": "not-requested"}}
        components = []
        for cid in benchmark["requiredComponents"]:
            components.append({
                "id": cid,
                "semanticMatch": True,
                "keyboardVerified": True,
                "responsiveVerified": True,
            })
        observations = {
            "businessSpecificity": True,
            "primaryTaskVisible": True,
            "primaryConversionVerified": True,
            "selectedThemePreserved": True,
            "sectionRecipeDrift": False,
            "genericCardSubstitution": False,
            "componentContracts": components,
            "forbiddenSubstitutionsObserved": [],
            "verifiedStates": benchmark["criticalStates"],
            "mobile": {"intentionalTransformation": True, "noHorizontalOverflow": True, "criticalControlsReachable": True},
            "content": {"unsupportedClaims": [], "duplicatedMessages": False, "genericMarketingLanguage": False},
            "assets": {"provenanceVerified": True, "irrelevantPrimaryMedia": False, "generatedMediaPresentedAsOfficial": False},
            "threeD": {"used": False},
        }
        result = self.critic.evaluate(plan, observations, benchmark)
        self.assertEqual(result["status"], "pass", result)

    def test_semantic_component_misuse_hard_fails(self):
        benchmark = self.by_id["b01-professional-services-consultation"]
        plan = {"threeD": {"status": "not-requested"}}
        observations = {
            "businessSpecificity": True,
            "primaryTaskVisible": True,
            "primaryConversionVerified": True,
            "selectedThemePreserved": True,
            "componentContracts": [{"id": "select", "semanticMatch": False, "keyboardVerified": True, "responsiveVerified": True}],
            "forbiddenSubstitutionsObserved": ["dropdown-menu-as-select"],
            "verifiedStates": [],
            "mobile": {"intentionalTransformation": True, "noHorizontalOverflow": True, "criticalControlsReachable": True},
            "content": {"unsupportedClaims": []},
            "assets": {"provenanceVerified": True},
            "threeD": {"used": False},
        }
        result = self.critic.evaluate(plan, observations, benchmark)
        self.assertEqual(result["status"], "fail")
        self.assertTrue(any("semantic mismatch" in x for x in result["hardFails"]))
        self.assertTrue(any("forbidden substitution" in x for x in result["hardFails"]))

    def test_unplanned_3d_hard_fails(self):
        plan = {"threeD": {"status": "not-requested"}}
        observations = {
            "businessSpecificity": True,
            "primaryTaskVisible": True,
            "primaryConversionVerified": True,
            "selectedThemePreserved": True,
            "componentContracts": [],
            "verifiedStates": [],
            "forbiddenSubstitutionsObserved": [],
            "mobile": {"intentionalTransformation": True, "noHorizontalOverflow": True, "criticalControlsReachable": True},
            "content": {"unsupportedClaims": []},
            "assets": {"provenanceVerified": True},
            "threeD": {"used": True, "subjectClassVerified": False, "goalVerified": False, "interactionPlanFollowed": False, "staticFallbackVerified": False, "unrelatedSpectacle": True},
        }
        result = self.critic.evaluate(plan, observations)
        self.assertEqual(result["status"], "fail")
        self.assertGreaterEqual(len(result["hardFails"]), 4)


if __name__ == "__main__":
    unittest.main()
