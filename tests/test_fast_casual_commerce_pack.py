from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_ROOT = ROOT / "packs" / "fast-casual-commerce"
VALIDATOR = ROOT / "scripts" / "validate-domain-packs.py"


class FastCasualCommercePackTests(unittest.TestCase):
    def load(self, relative: str) -> dict:
        return json.loads((ROOT / relative).read_text(encoding="utf-8"))

    def test_domain_pack_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("DOMAIN_PACK_VALIDATION=PASS", result.stdout)

    def test_expected_blueprints_components_and_states_exist(self) -> None:
        blueprints = {
            item["id"]
            for item in self.load("packs/fast-casual-commerce/page-blueprints.json")["blueprints"]
        }
        components = {
            item["id"]
            for item in self.load("packs/fast-casual-commerce/component-manifest.json")["components"]
        }
        states = {
            item["id"]
            for item in self.load("packs/fast-casual-commerce/state-vocabulary.json")["states"]
        }

        for expected in [
            "restaurant-ordering-home",
            "menu-catalog",
            "product-customizer",
            "cart-review",
            "checkout",
            "order-confirmation",
            "order-tracking",
            "deals-promotions",
            "loyalty-program",
            "branch-locator",
            "delivery-zone-checker",
        ]:
            self.assertIn(expected, blueprints)

        for expected in [
            "commerce-product-card",
            "product-customizer",
            "cart-drawer",
            "order-summary",
            "payment-method-selector",
            "order-status-timeline",
        ]:
            self.assertIn(expected, components)

        for expected in [
            "store-closed",
            "outside-delivery-zone",
            "cart-recalculated",
            "payment-pending",
            "order-confirmed",
            "offline-cart",
        ]:
            self.assertIn(expected, states)

    def test_prompt_and_platform_discovery(self) -> None:
        prompt_index = self.load("prompts/prompt-index.json")
        restaurant_prompt = next(
            item
            for item in prompt_index["prompts"]
            if item["id"] == "build-restaurant-commerce-experience"
        )
        self.assertEqual(
            restaurant_prompt["path"],
            "prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md",
        )
        self.assertEqual(restaurant_prompt["requiresDomainPack"], "fast-casual-commerce")

        for relative in ["AGENTS.md", "PROMPTS.md", "CLAUDE.md", "GEMINI.md"]:
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md", text)
            self.assertIn("fast-casual-commerce", text)

    def test_sample_menu_references_are_consistent(self) -> None:
        sample = self.load("packs/fast-casual-commerce/sample-data/menu.sample.json")
        product_ids = {product["id"] for product in sample["products"]}
        category_ids = {category["id"] for category in sample["categories"]}
        currency = sample["meta"]["currency"]

        for category in sample["categories"]:
            self.assertTrue(set(category["productIds"]).issubset(product_ids))
        for product in sample["products"]:
            self.assertIn(product["categoryId"], category_ids)
            self.assertIsInstance(product["basePrice"]["amountMinor"], int)
            self.assertEqual(product["basePrice"]["currency"], currency)
            self.assertTrue(product["images"])
            for group in product["optionGroups"]:
                self.assertLessEqual(group["minimumSelections"], group["maximumSelections"])
                for value in group["values"]:
                    self.assertIsInstance(value["priceDelta"]["amountMinor"], int)
                    self.assertEqual(value["priceDelta"]["currency"], currency)

    def test_code_contract_states_server_boundary(self) -> None:
        cart_engine = (PACK_ROOT / "code" / "cart-engine.ts").read_text(encoding="utf-8")
        types = (PACK_ROOT / "code" / "commerce-types.ts").read_text(encoding="utf-8")
        self.assertIn("amountMinor", cart_engine)
        self.assertIn("idempotency", cart_engine.lower())
        self.assertIn("server", cart_engine.lower())
        self.assertIn("PaymentState", types)
        self.assertIn("OrderStatus", types)


if __name__ == "__main__":
    unittest.main()
