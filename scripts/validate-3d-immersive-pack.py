#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "packs/3d-immersive-web"
def load(path, errors):
    if not path.is_file(): errors.append(f"Missing {path.relative_to(ROOT)}"); return {}
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc: errors.append(f"Invalid JSON {path.relative_to(ROOT)}: {exc}"); return {}
def ids(items, label, errors):
    values = [item.get("id") for item in items if isinstance(item, dict)]
    if any(not value for value in values): errors.append(f"Missing {label} id")
    if len(values) != len(set(values)): errors.append(f"Duplicate {label} ids")
    return set(values)
def main():
    errors = []
    required = ["README.md", "pack.json", "style-families.json", "production-themes.json", "page-blueprints.json", "component-manifest.json", "interaction-patterns.json", "state-vocabulary.json", "performance-budgets.json", "accessibility-and-fallbacks.md", "asset-and-model-standard.md", "lighting-and-material-standard.md", "camera-and-scroll-guidance.md", "mobile-3d-guidance.md", "implementation-prompt.md", "templates/THREE_D_BUILD_CONTRACT.md", "templates/SCENE_ASSET_PLAN.md", "templates/PERFORMANCE_AND_FALLBACK_PLAN.md", "templates/design-recipe.example.json", "schemas/immersive-experience.schema.json", "schemas/scene-asset.schema.json", "sample-data/immersive-product.sample.json", "code/capability-tiers.ts", "code/scene-budget.ts"]
    for relative in required:
        if not (PACK / relative).is_file(): errors.append(f"Missing packs/3d-immersive-web/{relative}")
    for relative in ["prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md", "3d/source-catalog.json", "3d/techniques/technique-catalog.json", "3d/references/refs-gallery-3d.json", "scripts/select-3d-references.py"]:
        if not (ROOT / relative).is_file(): errors.append(f"Missing {relative}")
    pack = load(PACK / "pack.json", errors)
    if pack.get("id") != "3d-immersive-web" or pack.get("packKind") != "capability": errors.append("Wrong 3D pack identity/kind")
    families = ids(load(PACK / "style-families.json", errors).get("families", []), "family", errors)
    blueprints = ids(load(PACK / "page-blueprints.json", errors).get("blueprints", []), "blueprint", errors)
    components = ids(load(PACK / "component-manifest.json", errors).get("components", []), "component", errors)
    interactions = ids(load(PACK / "interaction-patterns.json", errors).get("patterns", []), "interaction", errors)
    states = ids(load(PACK / "state-vocabulary.json", errors).get("states", []), "state", errors)
    sources = ids(load(ROOT / "3d/source-catalog.json", errors).get("sources", []), "source", errors)
    techniques = ids(load(ROOT / "3d/techniques/technique-catalog.json", errors).get("techniques", []), "technique", errors)
    refs = load(ROOT / "3d/references/refs-gallery-3d.json", errors)
    references = refs.get("references", [])
    ref_ids = ids(references, "reference", errors)
    thresholds = [(families, 20, "families"), (blueprints, 10, "blueprints"), (components, 25, "components"), (interactions, 30, "interactions"), (states, 35, "states"), (sources, 25, "sources"), (techniques, 30, "techniques")]
    for values, minimum, label in thresholds:
        if len(values) < minimum: errors.append(f"Too few {label}: {len(values)}")
    if refs.get("total") != len(references): errors.append("Refs.Gallery total mismatch")
    for item in references:
        if item.get("usagePolicy") != "reference-only": errors.append(f"Reference not reference-only: {item.get('id')}")
    budgets = load(PACK / "performance-budgets.json", errors)
    if {item.get("id") for item in budgets.get("tiers", [])} != {"static", "basic-mobile", "balanced", "high"}: errors.append("Missing performance tiers")
    pack_index = load(ROOT / "packs/pack-index.json", errors)
    entry = next((item for item in pack_index.get("packs", []) if item.get("id") == "3d-immersive-web"), None)
    if not entry or entry.get("packKind") != "capability": errors.append("3D pack not registered as capability")
    prompt_index = load(ROOT / "prompts/prompt-index.json", errors)
    prompt = next((item for item in prompt_index.get("prompts", []) if item.get("id") == "build-3d-immersive-web-experience"), None)
    if not prompt or prompt.get("requiresCapabilityPack") != "3d-immersive-web": errors.append("3D prompt routing missing")
    for relative in ["AGENTS.md", "PROMPTS.md", "PACKS.md", "CLAUDE.md", "GEMINI.md"]:
        text = (ROOT / relative).read_text(encoding="utf-8")
        for signal in ["BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md", "3d-immersive-web"]:
            if signal not in text: errors.append(f"{relative} missing {signal}")
    for relative in ["semantic-relevance-standard.md", "templates/THREE_D_RELEVANCE_CONTRACT.md", "schemas/semantic-relevance.schema.json"]:
        if not (PACK / relative).is_file(): errors.append(f"Missing semantic relevance file: {relative}")
    if not (ROOT / "3d/subject-domain-map.json").is_file(): errors.append("Missing 3d/subject-domain-map.json")
    semantic_schema = load(PACK / "schemas/semantic-relevance.schema.json", errors)
    if semantic_schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema": errors.append("Semantic relevance schema must use draft 2020-12")
    sample = load(PACK / "sample-data/immersive-product.sample.json", errors)
    if sample.get("meta", {}).get("fictional") is not True: errors.append("Sample must be fictional")
    if sample.get("fallback", {}).get("preservesPrimaryTask") is not True: errors.append("Fallback must preserve task")
    relevance_assets = sample.get("semanticRelevance", {}).get("assets", [])
    if not relevance_assets: errors.append("Sample must include semantic relevance records")
    for asset in relevance_assets:
        minimum = 4 if asset.get("role") == "primary" else 3
        if asset.get("decision") == "approve" and asset.get("relevanceScore", 0) < minimum: errors.append(f"Approved asset below relevance threshold: {asset.get('assetId')}")
    print(f"THREE_D_STYLE_FAMILIES={len(families)}")
    print(f"THREE_D_BLUEPRINTS={len(blueprints)}")
    print(f"THREE_D_COMPONENTS={len(components)}")
    print(f"THREE_D_INTERACTIONS={len(interactions)}")
    print(f"THREE_D_STATES={len(states)}")
    print(f"THREE_D_SOURCES={len(sources)}")
    print(f"THREE_D_TECHNIQUES={len(techniques)}")
    print(f"REFS_GALLERY_REFERENCES={len(ref_ids)}")
    if errors:
        print("THREE_D_PACK_VALIDATION=FAIL")
        for error in errors: print(f"- {error}")
        return 1
    print("THREE_D_PACK_VALIDATION=PASS")
    return 0
if __name__ == "__main__": raise SystemExit(main())
