#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def display_path(target):
    try:
        return str(target.relative_to(ROOT))
    except ValueError:
        return str(target)


def main():
    p = argparse.ArgumentParser(description="Build the compact data index consumed by the future Vault Studio browser.")
    p.add_argument("--output", default="studio/catalog-index.json")
    args = p.parse_args()
    effects = load(Path("interactive-effects/effects.json"))
    immersive = load(Path("immersive-templates/template-catalog.json"))
    modes = load(Path("3d/mode-classification.json"))
    production = load(Path("3d-production-resources/resource-catalog.json"))
    delivery = load(Path("3d-delivery-runtimes/runtime-catalog.json"))
    packs = load(Path("packs/pack-index.json"))
    sections = load(Path("system/section-recipes.json"))
    refs = load(Path("references/threeui-community.json"))
    product = [x for x in packs["packs"] if x.get("packKind") == "product-domain"]
    capability = [x for x in packs["packs"] if x.get("packKind") == "capability"]
    recipes = sections["recipes"]
    data = {
        "name": "AI UI Style Vault Studio Index",
        "version": "1.4.0",
        "browseKinds": [
            "domain-pack", "section-recipe", "interactive-effect", "immersive-template",
            "3d-mode", "3d-production-resource", "3d-delivery-runtime", "capability-pack", "reference-pattern"
        ],
        "counts": {
            "domainPacks": len(product),
            "capabilityPacks": len(capability),
            "sectionRecipes": len(recipes),
            "interactiveEffects": len(effects["effects"]),
            "immersiveTemplates": len(immersive["templates"]),
            "threeDModes": len(modes["modes"]),
            "productionResourceCategories": len(production["categories"]),
            "deliveryRuntimeProfiles": len(delivery["profiles"]),
            "referencePatterns": len(refs["referencePatterns"])
        },
        "domainPacks": [{"id": x["id"], "name": x["name"], "triggers": x.get("triggers", [])[:8]} for x in product],
        "capabilityPacks": [{"id": x["id"], "name": x["name"]} for x in capability],
        "sectionRecipes": [{"id": x["id"], "section": x["section"], "composition": x["composition"]} for x in recipes],
        "interactiveEffects": [
            {"id": x["id"], "label": x["label"], "family": x["family"], "sections": x["sections"], "domains": x["domains"], "runtime": x["runtime"], "performanceTier": x["tier"], "signals": x["signals"]}
            for x in effects["effects"]
        ],
        "immersiveTemplates": [
            {"id": x["id"], "label": x["label"], "level": x["level"], "domains": x["domains"], "goals": x["goals"], "blueprint": x["blueprint"], "runtimes": x["runtimes"], "performanceTier": x["performanceTier"], "reuseMode": x["reuseMode"]}
            for x in immersive["templates"]
        ],
        "threeDModes": [
            {
                "id": x["id"], "level": x["level"], "label": x["label"], "summary": x["summary"],
                "userControl": x["userControl"], "assetRequirement": x["assetRequirement"],
                "preferredDelivery": x["preferredDelivery"], "nextStage": x["nextStage"]
            }
            for x in modes["modes"]
        ],
        "productionResources": [
            {
                "id": x["id"], "label": x["label"], "summary": x["summary"],
                "domains": x["domains"], "needs": x["needs"], "outputs": x["outputs"],
                "candidateCount": len(x["resourceCandidates"])
            }
            for x in production["categories"]
        ],
        "deliveryRuntimes": [
            {
                "id": x["id"], "label": x["label"], "summary": x["summary"],
                "goals": x["goals"], "features": x["features"],
                "performanceTier": x["performanceTier"]
            }
            for x in delivery["profiles"]
        ],
        "referencePatterns": [{"id": x["id"], "family": x["family"], "runtime": x["runtime"], "reuse": x["reuse"]} for x in refs["referencePatterns"]],
        "rule": "Studio browsing never bypasses business research, semantic effect/immersive/3D selection or source/licence boundaries. 3D mode is classified before asset production or runtime selection; file format never determines interaction mode."
    }
    target = Path(args.output)
    if not target.is_absolute():
        target = ROOT / target
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "ready", "output": display_path(target), "counts": data["counts"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
