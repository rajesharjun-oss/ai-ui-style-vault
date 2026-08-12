#!/usr/bin/env python3
"""Validate AI UI Style Vault domain-pack discovery, contracts, and sample data."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FAST_CASUAL_BLUEPRINTS = {
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
}

EXPECTED_FAST_CASUAL_COMPONENTS = {
    "commerce-app-shell",
    "fulfilment-toggle",
    "branch-selector",
    "delivery-address-field",
    "service-status-banner",
    "category-navigation",
    "commerce-product-card",
    "price-display",
    "availability-badge",
    "option-group",
    "modifier-grid",
    "quantity-stepper",
    "product-customizer",
    "cart-action",
    "cart-drawer",
    "cart-line-item",
    "order-summary",
    "promo-code-field",
    "deal-card",
    "loyalty-wallet",
    "checkout-step",
    "payment-method-selector",
    "order-status-timeline",
}

EXPECTED_FAST_CASUAL_STATES = {
    "out-of-stock",
    "temporarily-unavailable",
    "store-closed",
    "delivery-unavailable",
    "outside-delivery-zone",
    "minimum-order-not-met",
    "required-option-missing",
    "modifier-unavailable",
    "coupon-applied",
    "coupon-invalid",
    "coupon-expired",
    "location-changed",
    "cart-recalculated",
    "cart-conflict",
    "payment-pending",
    "payment-failed",
    "payment-authorised",
    "order-confirmed",
    "preparing",
    "ready-for-pickup",
    "out-for-delivery",
    "delivered",
    "cancelled",
    "offline-cart",
}


def load_json(path: Path, errors: list[str]) -> Any:
    if not path.is_file():
        errors.append(f"Missing JSON file: {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}


def require_file(relative: str, errors: list[str]) -> Path:
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"Missing required file: {relative}")
    return path


def require_directory(relative: str, errors: list[str]) -> Path:
    path = ROOT / relative
    if not path.is_dir():
        errors.append(f"Missing required directory: {relative}")
    return path


def unique_ids(items: list[dict[str, Any]], label: str, errors: list[str]) -> set[str]:
    identifiers: list[str] = []
    for index, item in enumerate(items):
        identifier = item.get("id")
        if not isinstance(identifier, str) or not identifier.strip():
            errors.append(f"{label}[{index}] is missing a non-empty id")
            continue
        identifiers.append(identifier)
    duplicates = sorted({identifier for identifier in identifiers if identifiers.count(identifier) > 1})
    if duplicates:
        errors.append(f"Duplicate {label} ids: {', '.join(duplicates)}")
    return set(identifiers)


def validate_sample_menu(path: Path, errors: list[str]) -> dict[str, int]:
    data = load_json(path, errors)
    if not isinstance(data, dict):
        errors.append("Sample menu root must be an object")
        return {"branches": 0, "categories": 0, "products": 0}

    branches = data.get("branches") or []
    categories = data.get("categories") or []
    products = data.get("products") or []

    if not branches:
        errors.append("Sample menu must contain at least one branch")
    if not categories:
        errors.append("Sample menu must contain at least one category")
    if not products:
        errors.append("Sample menu must contain at least one product")

    product_ids = unique_ids(products, "sample product", errors)
    category_ids = unique_ids(categories, "sample category", errors)
    branch_ids = unique_ids(branches, "sample branch", errors)

    declared_currency = ((data.get("meta") or {}).get("currency") or "").upper()
    if len(declared_currency) != 3:
        errors.append("Sample menu meta.currency must be a three-character code")

    for category in categories:
        for product_id in category.get("productIds") or []:
            if product_id not in product_ids:
                errors.append(
                    f"Category {category.get('id')} references missing product {product_id}"
                )

    for product in products:
        if product.get("categoryId") not in category_ids:
            errors.append(
                f"Product {product.get('id')} references missing category {product.get('categoryId')}"
            )
        base_price = product.get("basePrice") or {}
        if not isinstance(base_price.get("amountMinor"), int):
            errors.append(f"Product {product.get('id')} basePrice.amountMinor must be an integer")
        if base_price.get("currency") != declared_currency:
            errors.append(f"Product {product.get('id')} currency must match meta.currency")
        images = product.get("images") or []
        if not images:
            errors.append(f"Product {product.get('id')} must include an image contract")
        for image in images:
            if image.get("provenance") not in {
                "owner-provided",
                "original",
                "generated-concept",
                "licensed",
            }:
                errors.append(f"Product {product.get('id')} has invalid image provenance")
        group_ids: set[str] = set()
        for group in product.get("optionGroups") or []:
            group_id = group.get("id")
            if group_id in group_ids:
                errors.append(f"Product {product.get('id')} has duplicate option group {group_id}")
            group_ids.add(group_id)
            minimum = group.get("minimumSelections")
            maximum = group.get("maximumSelections")
            if not isinstance(minimum, int) or not isinstance(maximum, int) or minimum > maximum:
                errors.append(f"Product {product.get('id')} option group {group_id} has invalid limits")
            value_ids: set[str] = set()
            for value in group.get("values") or []:
                value_id = value.get("id")
                if value_id in value_ids:
                    errors.append(
                        f"Product {product.get('id')} option group {group_id} has duplicate value {value_id}"
                    )
                value_ids.add(value_id)
                price_delta = value.get("priceDelta") or {}
                if not isinstance(price_delta.get("amountMinor"), int):
                    errors.append(
                        f"Product {product.get('id')} option value {value_id} price delta must be integer minor units"
                    )
                if price_delta.get("currency") != declared_currency:
                    errors.append(
                        f"Product {product.get('id')} option value {value_id} currency mismatch"
                    )

    return {
        "branches": len(branch_ids),
        "categories": len(category_ids),
        "products": len(product_ids),
    }


def main() -> int:
    errors: list[str] = []

    for relative in [
        "AGENTS.md",
        "PROMPTS.md",
        "PACKS.md",
        "CLAUDE.md",
        "GEMINI.md",
        "prompts/prompt-index.json",
        "packs/pack-index.json",
    ]:
        require_file(relative, errors)

    pack_index = load_json(ROOT / "packs/pack-index.json", errors)
    packs = pack_index.get("packs") if isinstance(pack_index, dict) else None
    if not isinstance(packs, list) or not packs:
        errors.append("packs/pack-index.json must contain at least one pack")
        packs = []

    pack_ids = unique_ids(packs, "domain pack", errors)
    if "fast-casual-commerce" not in pack_ids:
        errors.append("Fast-Casual Commerce pack is not registered")

    fast_pack = next((pack for pack in packs if pack.get("id") == "fast-casual-commerce"), {})
    pack_root_relative = fast_pack.get("path", "packs/fast-casual-commerce")
    pack_root = require_directory(pack_root_relative, errors)

    for relative in fast_pack.get("requiredReads") or []:
        require_file(relative, errors)
    require_file(fast_pack.get("requiredPrompt", ""), errors)
    require_directory(fast_pack.get("templateRoot", ""), errors)
    require_directory(fast_pack.get("codeRoot", ""), errors)
    require_directory(fast_pack.get("sampleDataRoot", ""), errors)

    pack_contract = load_json(pack_root / "pack.json", errors)
    if pack_contract.get("id") != "fast-casual-commerce":
        errors.append("Fast-Casual Commerce pack.json has the wrong id")
    for relative in pack_contract.get("requiredPlanningArtifacts") or []:
        if relative == "COMMERCE_BUILD_CONTRACT.md":
            require_file(
                "packs/fast-casual-commerce/templates/COMMERCE_BUILD_CONTRACT.md",
                errors,
            )

    blueprint_data = load_json(pack_root / "page-blueprints.json", errors)
    blueprint_ids = unique_ids(blueprint_data.get("blueprints") or [], "commerce blueprint", errors)
    missing_blueprints = sorted(EXPECTED_FAST_CASUAL_BLUEPRINTS - blueprint_ids)
    if missing_blueprints:
        errors.append(f"Missing commerce blueprints: {', '.join(missing_blueprints)}")

    component_data = load_json(pack_root / "component-manifest.json", errors)
    component_ids = unique_ids(component_data.get("components") or [], "commerce component", errors)
    missing_components = sorted(EXPECTED_FAST_CASUAL_COMPONENTS - component_ids)
    if missing_components:
        errors.append(f"Missing commerce components: {', '.join(missing_components)}")

    state_data = load_json(pack_root / "state-vocabulary.json", errors)
    state_ids = unique_ids(state_data.get("states") or [], "commerce state", errors)
    missing_states = sorted(EXPECTED_FAST_CASUAL_STATES - state_ids)
    if missing_states:
        errors.append(f"Missing commerce states: {', '.join(missing_states)}")

    for relative in [
        "packs/fast-casual-commerce/production-theme.json",
        "packs/fast-casual-commerce/schemas/menu.schema.json",
        "packs/fast-casual-commerce/templates/design-recipe.example.json",
    ]:
        load_json(ROOT / relative, errors)

    sample_counts = validate_sample_menu(
        ROOT / "packs/fast-casual-commerce/sample-data/menu.sample.json",
        errors,
    )

    prompt_index = load_json(ROOT / "prompts/prompt-index.json", errors)
    prompt_entry = next(
        (
            prompt
            for prompt in prompt_index.get("prompts") or []
            if prompt.get("id") == "build-restaurant-commerce-experience"
        ),
        None,
    )
    if not prompt_entry:
        errors.append("Restaurant commerce prompt is not registered")
    elif prompt_entry.get("requiresDomainPack") != "fast-casual-commerce":
        errors.append("Restaurant commerce prompt does not require the Fast-Casual Commerce pack")

    discoverability_files = {
        "AGENTS.md": ["PACKS.md", "BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md", "fast-casual-commerce"],
        "PROMPTS.md": ["BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md", "fast-casual-commerce"],
        "PACKS.md": ["packs/pack-index.json", "fast-casual-commerce"],
        "CLAUDE.md": ["BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md", "fast-casual-commerce"],
        "GEMINI.md": ["BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md", "fast-casual-commerce"],
    }
    for relative, needles in discoverability_files.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append(f"{relative} does not reference {needle}")

    cart_engine = require_file("packs/fast-casual-commerce/code/cart-engine.ts", errors)
    if cart_engine.is_file():
        cart_text = cart_engine.read_text(encoding="utf-8")
        for needle in ["amountMinor", "idempotency", "server", "payment-pending"]:
            if needle not in cart_text:
                errors.append(f"cart-engine.ts is missing security or calculation signal: {needle}")

    print(f"DOMAIN_PACKS={len(pack_ids)}")
    print(f"FAST_CASUAL_BLUEPRINTS={len(blueprint_ids)}")
    print(f"FAST_CASUAL_COMPONENTS={len(component_ids)}")
    print(f"FAST_CASUAL_STATES={len(state_ids)}")
    print(f"SAMPLE_BRANCHES={sample_counts['branches']}")
    print(f"SAMPLE_CATEGORIES={sample_counts['categories']}")
    print(f"SAMPLE_PRODUCTS={sample_counts['products']}")

    if errors:
        print("DOMAIN_PACK_VALIDATION=FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("DOMAIN_PACK_VALIDATION=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
