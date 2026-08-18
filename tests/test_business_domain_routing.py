import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("planner", ROOT / "scripts/plan-vault-build.py")
planner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(planner)

class BusinessDomainRoutingTests(unittest.TestCase):
    def profile(self, category, offers):
        return {"businessCategory": category, "subcategories": [], "audiences": [], "offers": [{"name": x} for x in offers]}

    def test_tax_firm_routes_to_professional_services(self):
        self.assertEqual(planner.choose_domain(self.profile("Tax and advisory firm", ["Tax consulting","Audit"])), "professional-services")

    def test_property_developer_routes_to_real_estate(self):
        self.assertEqual(planner.choose_domain(self.profile("Real estate developer", ["Residential apartments","Property development"])), "real-estate")

    def test_couture_still_routes_to_fashion(self):
        self.assertEqual(planner.choose_domain(self.profile("Fashion couture", ["Kaftan","Corporate suits"])), "fashion-couture")

if __name__ == "__main__":
    unittest.main()
