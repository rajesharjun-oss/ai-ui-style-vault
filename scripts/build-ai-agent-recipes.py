#!/usr/bin/env python3
"""Materialize agent-ready build recipes for the 3D/immersive library.

Coverage:
- 300 concrete design directions (30 scene archetypes x 10 art directions)
- 138 MotionSites public reference records
- 40 MotionSites-derived motion patterns

The output is vault-authored instruction material. External reference metadata is used only
as high-level inspiration; this script never imports proprietary prompts, source code or media.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
DESIGN_SYSTEM = ROOT / "packs/3d-immersive-web/design-combination-system.json"
REFERENCE_FILES = [
    ROOT / "3d/references/motionsites-public-catalog-2026-08-17.json",
    ROOT / "3d/references/motionsites-public-catalog-wave2-2026-08-17.json",
]
PATTERN_FILES = [
    ROOT / "3d/techniques/motionsites-motion-patterns.json",
    ROOT / "3d/techniques/motionsites-motion-patterns-wave2.json",
]
DEFAULT_OUTPUT = ROOT / "3d/generated/ai-agent-recipes.json"
EXPECTED_COUNTS = {"designDirection": 300, "reference": 138, "motionPattern": 40, "total": 478}

COMMON_ORIGINALITY = [
    "Create an original composition, visual system, copy and code; never clone an external reference.",
    "Do not copy proprietary prompts, source code, branded assets, models, textures, exact layout or choreography.",
    "Use references only for abstract hierarchy, pacing, interaction and implementation learnings.",
]
COMMON_ACCESSIBILITY = [
    "Keep navigation, copy, forms, prices, CTAs and status in semantic DOM rather than canvas-only UI.",
    "Provide a complete reduced-motion path and a static/2D fallback that preserves the primary task.",
    "Preserve keyboard/focus order, sufficient contrast, zoom usability and meaningful alternative text/content.",
]
COMMON_PERFORMANCE = [
    "Use progressive enhancement and load expensive media/runtime only after capability and intent checks.",
    "Choose the smallest sufficient medium before custom WebGL/WebGPU or XR.",
    "Design explicit loading, slow-network, unsupported-device and rendering-error states.",
]

CATEGORY_DOMAIN_RULES: list[tuple[tuple[str, ...], str]] = [
    (("pizza", "restaurant", "food", "ingredient"), "restaurant-food"),
    (("automotive", "driving", "car", "f1"), "automotive"),
    (("fashion", "jewelry", "beauty", "eyewear", "product", "ecommerce"), "fashion-retail"),
    (("real estate", "interior", "architecture", "spaces"), "real-estate-architecture"),
    (("travel", "jet", "hospitality", "guide", "voyage"), "travel-hospitality"),
    (("wellness", "health", "medicine", "mindfulness", "biotech"), "beauty-wellness"),
    (("finance", "fintech", "wealth", "lending", "defi", "venture"), "professional-services"),
    (("agency", "service", "consult", "operations"), "professional-services"),
    (("saas", "ai", "technology", "developer", "cyber", "security", "vpn", "data", "web3"), "technology-electronics"),
    (("education", "science", "lab"), "education-science"),
    (("wedding", "event", "celebration"), "wedding-celebration"),
    (("mapping", "logistics", "route"), "logistics-mobility"),
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def unique(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        clean = " ".join(str(item).split())
        if clean and clean not in seen:
            seen.add(clean)
            result.append(clean)
    return result


def title_from_id(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("__", " — ").replace("-", " ")).title()


def infer_domains(category: str, tags: list[str]) -> list[str]:
    haystack = " ".join([category, *tags]).lower()
    domains: list[str] = []
    for needles, domain in CATEGORY_DOMAIN_RULES:
        if any(needle in haystack for needle in needles):
            domains.append(domain)
    return unique(domains) or ["cross-domain"]


def medium_guidance(media: list[str] | None, summary: str = "") -> str:
    values = [m.lower() for m in (media or [])]
    text = " ".join(values + [summary.lower()])
    if "image sequence" in text or "frame" in text:
        return "Prefer a responsive image-sequence/canvas scrub with bounded preloading; use video as a simpler fallback."
    if "video" in text:
        return "Prefer compressed poster-first video or scroll-scrub video; upgrade to canvas only when frame precision is required."
    if "rive" in text:
        return "Use Rive for bounded vector/state animation while keeping controls and content in DOM."
    if "spline" in text:
        return "Use Spline only when its runtime cost is justified; lazy-load the scene and provide a still fallback."
    if "model-viewer" in text or "webxr" in text:
        return "Use model-viewer for product inspection/AR where possible; reserve custom WebXR for requirements it cannot satisfy."
    if "three.js" in text or "react three fiber" in text or "babylon" in text or "webgl" in text or "shader" in text:
        return "Use one lazy-loaded WebGL renderer, optimized geometry/textures and DOM overlays; avoid canvas-only essential UI."
    return "Start with DOM/CSS and progressive enhancement; add canvas/3D only where it materially improves the user task."


def base_acceptance() -> list[str]:
    return [
        "The primary user task remains usable with immersive media disabled.",
        "Desktop, tablet and mobile layouts are intentionally composed and do not overlap or hide essential controls.",
        "Reduced-motion mode removes scrubbing/parallax/camera movement without losing content or task completion.",
        "Loading, unsupported, slow-network and media/render failure states have designed fallbacks.",
        "No primary visual fails the vault semantic-relevance threshold.",
        "The final implementation is visibly original and cannot be mistaken for a clone of the source reference.",
    ]


def make_agent_prompt(recipe: dict[str, Any]) -> str:
    def bullets(values: list[str]) -> str:
        return "\n".join(f"- {value}" for value in values)

    domains = ", ".join(recipe.get("domains", [])) or "cross-domain"
    return f"""Use AI UI Style Vault recipe `{recipe['id']}` — {recipe['name']}.

Act as a senior product designer, content designer, art director, accessibility specialist and performance-focused front-end engineer. Build an original experience for the verified business brief; do not clone any source/reference.

Target domains: {domains}.
Design objective: {recipe['designObjective']}
Implementation approach: {recipe['implementationApproach']}

When to use:
{bullets(recipe['whenToUse'])}

Do not use when:
{bullets(recipe['whenNotToUse'])}

Composition:
{bullets(recipe['compositionInstructions'])}

Motion:
{bullets(recipe['motionInstructions'])}

Assets:
{bullets(recipe['assetInstructions'])}

Responsive behavior:
{bullets(recipe['responsiveBehavior'])}

Performance:
{bullets(recipe['performanceLimits'])}

Accessibility and fallback:
{bullets(recipe['accessibilityAndFallback'])}

Originality rules:
{bullets(recipe['originalityRules'])}

Before coding, complete the semantic-relevance contract and reject unrelated spectacle. Keep essential navigation, copy, forms, prices, CTAs and status in semantic DOM. Use progressive enhancement and the smallest sufficient medium.

Acceptance criteria:
{bullets(recipe['acceptanceCriteria'])}

At handoff, report the recipe ID, any supporting recipe IDs, implementation medium, performance tier, fallback and any deliberate deviations."""


def design_recipes() -> list[dict[str, Any]]:
    data = load_json(DESIGN_SYSTEM)
    recipes: list[dict[str, Any]] = []
    for scene in data["sceneArchetypes"]:
        for art in data["artDirections"]:
            recipe_id = f"design:{scene['id']}__{art['id']}"
            domains = list(scene["domains"])
            recipe = {
                "id": recipe_id,
                "kind": "designDirection",
                "name": f"{scene['name']} — {art['name']}",
                "source": {
                    "type": "vault-design-system",
                    "sceneArchetype": scene["id"],
                    "artDirection": art["id"],
                },
                "domains": domains,
                "whenToUse": [
                    scene["purpose"],
                    f"Use when the verified brand/product supports {art['bestWhen'].rstrip('.').lower()}.",
                    "Use only when the immersive treatment improves comprehension, confidence, storytelling or conversion over a simpler composition.",
                ],
                "whenNotToUse": [
                    f"Do not use when {art['avoid'].rstrip('.').lower()}.",
                    "Do not use when the subject, environment or props do not directly match the verified business/domain.",
                    "Do not use when the same user outcome is better served by ordinary DOM, photography or a lightweight video.",
                ],
                "designObjective": f"{scene['purpose']} Apply the {art['name']} treatment without sacrificing task clarity, factual accuracy or accessibility.",
                "compositionInstructions": [
                    f"Make the {scene['name'].lower()} the single dominant focal system; keep supporting copy concise and spatially separated.",
                    f"Translate these art-direction traits into an original system: {', '.join(art['traits'])}.",
                    "Reserve clean visual zones for headline, primary CTA and critical controls; do not place text over the highest-motion focal area.",
                    "Use clear section hierarchy and visual rest after the primary immersive moment rather than repeating the same effect everywhere.",
                ],
                "motionInstructions": [
                    "Use motion to reveal information or change viewpoint/state, not as constant decoration.",
                    "Prefer deterministic scroll or direct manipulation for the primary interaction and restrained entrance/hover motion elsewhere.",
                    "Avoid simultaneous camera, object, text and background motion unless the hierarchy remains immediately legible.",
                    "Cap the page at one primary immersive choreography plus at most three supporting motion patterns unless the brief justifies more.",
                ],
                "implementationApproach": medium_guidance(scene.get("typicalMedia")),
                "assetInstructions": [
                    "Complete `THREE_D_RELEVANCE_CONTRACT.md` before searching for models, video, environments or textures.",
                    "Use verified product/place/process geometry or media where the experience represents something real; otherwise treat the visualization as conceptual internally.",
                    f"Preferred media candidates: {', '.join(scene.get('typicalMedia', [])) or 'DOM/CSS first'}.",
                    f"Required fallback: {scene['fallback']}.",
                    "Validate subject, environment, props, materials, lighting, camera motion and fallback as one semantically coherent scene.",
                ],
                "responsiveBehavior": [
                    "Desktop may use the full composition only when viewport and capability allow it.",
                    "Tablet reduces simultaneous layers and pinned distance while preserving the same information sequence.",
                    "Mobile uses an intentionally recomposed layout with simplified camera/object motion, larger touch targets and a low-motion/static path.",
                ],
                "performanceLimits": list(COMMON_PERFORMANCE) + [
                    "Use one renderer where possible and dispose textures, geometries, listeners and animation loops on teardown.",
                    "Measure first useful frame, transferred media, texture/GPU memory, draw calls/triangles where applicable and sustained interaction smoothness.",
                ],
                "accessibilityAndFallback": list(COMMON_ACCESSIBILITY) + [f"Fallback visual/content direction: {scene['fallback']}."],
                "originalityRules": list(COMMON_ORIGINALITY),
                "acceptanceCriteria": base_acceptance() + [
                    f"The result clearly expresses `{scene['id']}` plus `{art['id']}` without relying on unrelated spectacle.",
                    "The art direction supports the business and never obscures real product color, dimensions or information users need to decide.",
                ],
            }
            recipe["agentPrompt"] = make_agent_prompt(recipe)
            recipes.append(recipe)
    return recipes


def reference_recipes() -> list[dict[str, Any]]:
    recipes: list[dict[str, Any]] = []
    for path in REFERENCE_FILES:
        data = load_json(path)
        for record in data["records"]:
            tags = [str(tag) for tag in record.get("tags", [])]
            category = str(record.get("category", "Reference"))
            domains = infer_domains(category, tags)
            tag_phrase = ", ".join(tags) if tags else "the reference's high-level interaction idea"
            recipe = {
                "id": f"reference:{record['id']}",
                "kind": "reference",
                "name": f"Reference abstraction — {record['name']}",
                "source": {
                    "type": "external-reference-metadata",
                    "provider": data.get("source", "MotionSites"),
                    "recordId": record["id"],
                    "sourcePage": record.get("sourcePage"),
                    "usagePolicy": data.get("usagePolicy", "reference-only"),
                },
                "domains": domains,
                "whenToUse": [
                    f"Use as abstract inspiration when the requested page purpose is compatible with `{category}`.",
                    f"Use when verified business context supports these high-level cues: {tag_phrase}.",
                    "Use only after selecting a vault-native design direction that gives the page its own hierarchy and visual identity.",
                ],
                "whenNotToUse": [
                    "Do not reproduce the reference's exact layout, copy, assets, brand identity, proprietary prompt or choreography.",
                    "Do not use when the source category/tags conflict with the target business, audience or task.",
                    "Do not use a reference merely because it appears fashionable, premium or technically impressive.",
                ],
                "designObjective": f"Extract a small number of transferable interaction/composition lessons from a `{category}` reference while producing a materially original design for the target business.",
                "compositionInstructions": [
                    "Start from the target business's content hierarchy and conversion/task requirements, not the reference's screen structure.",
                    f"Translate only abstract cues from `{tag_phrase}` into a new grid, typography system, spacing rhythm and focal hierarchy.",
                    "Use one dominant visual idea; supporting sections should become calmer, clearer and more task-oriented.",
                    "Keep content density concise and prevent decorative media from competing with the main CTA or decision information.",
                ],
                "motionInstructions": [
                    "Infer motion only from high-level tags/category and pair it with vault-native motion patterns; do not reconstruct source choreography.",
                    "Use deterministic triggers, clear start/end states and restrained easing rather than perpetual animation.",
                    "Keep text readable while media moves; reserve a media-safe empty zone around the main focal subject where required.",
                ],
                "implementationApproach": medium_guidance(None, " ".join(tags + [category])),
                "assetInstructions": [
                    "Do not download or reuse source screenshots, videos, models, textures, logos or branded imagery unless separately licensed and explicitly required.",
                    "Source or generate business-relevant media independently and record provenance/licence where applicable.",
                    "Run every primary visual through the semantic-relevance contract before implementation.",
                ],
                "responsiveBehavior": [
                    "Preserve the target page's information hierarchy on all breakpoints rather than copying the reference's breakpoint behavior.",
                    "On mobile, replace fragile hover/pinned interactions with touch-safe, shorter and lower-motion equivalents.",
                    "Ensure moving media never covers headline, CTA, form fields or sticky navigation on narrow screens.",
                ],
                "performanceLimits": list(COMMON_PERFORMANCE),
                "accessibilityAndFallback": list(COMMON_ACCESSIBILITY),
                "originalityRules": list(COMMON_ORIGINALITY) + [
                    "Treat the source URL as audit provenance only; the finished design must stand independently without it.",
                ],
                "acceptanceCriteria": base_acceptance() + [
                    "A reviewer can identify the abstract design lesson used but cannot map the finished page to the source's exact composition.",
                    "The reference is secondary to verified business content and a vault-native design direction.",
                ],
            }
            recipe["agentPrompt"] = make_agent_prompt(recipe)
            recipes.append(recipe)
    return recipes


def pattern_specific_guidance(pattern_id: str, summary: str) -> tuple[str, list[str], list[str]]:
    text = f"{pattern_id} {summary}".lower()
    motion: list[str] = []
    performance: list[str] = []
    if "scrub" in text or "scroll" in text:
        motion += [
            "Map normalized scroll progress to a bounded animation timeline; clamp values and avoid raw scroll-event rendering.",
            "Interpolate visual progress in `requestAnimationFrame` when direct scroll mapping produces jitter.",
        ]
        performance += ["Pause or simplify scrub logic when the section is outside the active viewport."]
    if "video" in text:
        performance += ["Ship a compressed poster first; preload only the video metadata/required range and avoid autoplay dependency for core content."]
    if "frame" in text or "image-sequence" in text:
        performance += ["Bound decoded-frame memory, preload a sliding window and release frames that are no longer needed on constrained devices."]
    if "parallax" in text or "camera" in text or "3d" in text:
        motion += ["Use depth/camera motion sparingly and keep the focal subject inside a protected composition zone across the full timeline."]
    if "hover" in text or "pointer" in text or "glow" in text:
        motion += ["Mirror hover affordances with keyboard focus states and do not make pointer tracking necessary to understand or activate the control."]
    if "sticky" in text or "pinned" in text:
        motion += ["Give the pinned region an explicit start/end boundary and ensure content exits naturally without trapping scroll."]
    return medium_guidance(None, text), unique(motion), unique(performance)


def pattern_recipes() -> list[dict[str, Any]]:
    recipes: list[dict[str, Any]] = []
    for path in PATTERN_FILES:
        data = load_json(path)
        for pattern in data["patterns"]:
            best_for = [str(item) for item in pattern.get("bestFor", [])]
            summary = str(pattern.get("summary", ""))
            implementation, extra_motion, extra_performance = pattern_specific_guidance(pattern["id"], summary)
            domains = infer_domains(" ".join(best_for), best_for)
            recipe = {
                "id": f"motion:{pattern['id']}",
                "kind": "motionPattern",
                "name": pattern["name"],
                "source": {
                    "type": "vault-authored-pattern-abstraction",
                    "provider": data.get("source", "MotionSites public examples and tutorials"),
                    "patternId": pattern["id"],
                    "usagePolicy": data.get("usagePolicy", "reference-only abstraction"),
                },
                "domains": domains,
                "whenToUse": [
                    summary,
                    f"Best suited to: {', '.join(best_for) if best_for else 'a page where the interaction materially improves comprehension or task flow'}.",
                    "Use as a supporting interaction only when it strengthens the selected primary design direction.",
                ],
                "whenNotToUse": [
                    "Do not use when the pattern adds motion without improving comprehension, navigation, confidence or conversion.",
                    "Do not use when it conflicts with reduced-motion, device capability or the semantic reading order.",
                    "Do not stack it with multiple competing motion systems in the same viewport.",
                ],
                "designObjective": f"Implement `{pattern['name']}` as a controlled, accessible interaction that supports the page narrative/task: {summary}",
                "compositionInstructions": [
                    "Define the focal subject, protected text/control zone and start/end visual states before animating.",
                    "Keep a clear DOM hierarchy beneath/alongside the motion layer so the section still reads without animation.",
                    "Use spacing and section boundaries to give the interaction enough room to complete without crowding adjacent content.",
                ],
                "motionInstructions": unique([
                    summary,
                    "Use explicit triggers, bounded progress and predictable easing; avoid endless decorative loops unless the asset is purely ambient and subtle.",
                    "Keep entrance/hover effects secondary to the primary interaction and maintain clear visual rest states.",
                    *extra_motion,
                ]),
                "implementationApproach": implementation,
                "assetInstructions": [
                    "Use only assets directly related to the verified business/product/process/place.",
                    "Provide a poster/still or ordinary DOM equivalent before enabling motion-heavy media.",
                    "Do not copy source media or proprietary implementation from reference sites/tutorials.",
                ],
                "responsiveBehavior": [
                    "Desktop may use the full interaction when performance is stable and content remains legible.",
                    "Tablet shortens travel distance, reduces layers and avoids precision hover dependencies.",
                    "Mobile preserves the intended story/task with a shorter timeline, simpler transform set or static replacement.",
                ],
                "performanceLimits": unique([*COMMON_PERFORMANCE, *extra_performance]),
                "accessibilityAndFallback": list(COMMON_ACCESSIBILITY),
                "originalityRules": list(COMMON_ORIGINALITY),
                "acceptanceCriteria": base_acceptance() + [
                    f"The `{pattern['id']}` interaction has deterministic start/end states and no layout jump at activation or release.",
                    "Disabling JavaScript/motion-heavy media still leaves coherent content and a usable primary task.",
                ],
            }
            recipe["agentPrompt"] = make_agent_prompt(recipe)
            recipes.append(recipe)
    return recipes


def validate_recipe(recipe: dict[str, Any]) -> None:
    required = [
        "id", "kind", "name", "source", "domains", "whenToUse", "whenNotToUse", "designObjective",
        "compositionInstructions", "motionInstructions", "implementationApproach", "assetInstructions",
        "responsiveBehavior", "performanceLimits", "accessibilityAndFallback", "originalityRules",
        "acceptanceCriteria", "agentPrompt",
    ]
    missing = [key for key in required if key not in recipe]
    if missing:
        raise ValueError(f"{recipe.get('id', '<unknown>')} missing fields: {missing}")
    for key in [
        "domains", "whenToUse", "whenNotToUse", "compositionInstructions", "motionInstructions",
        "assetInstructions", "responsiveBehavior", "performanceLimits", "accessibilityAndFallback",
        "originalityRules", "acceptanceCriteria",
    ]:
        if not isinstance(recipe[key], list) or not recipe[key]:
            raise ValueError(f"{recipe['id']} requires non-empty list field `{key}`")
    if len(recipe["agentPrompt"].strip()) < 500:
        raise ValueError(f"{recipe['id']} agentPrompt is unexpectedly short")


def build_catalog() -> dict[str, Any]:
    recipes = [*design_recipes(), *reference_recipes(), *pattern_recipes()]
    ids = [recipe["id"] for recipe in recipes]
    if len(ids) != len(set(ids)):
        duplicates = sorted({item for item in ids if ids.count(item) > 1})
        raise ValueError(f"Duplicate recipe IDs: {duplicates}")
    for recipe in recipes:
        validate_recipe(recipe)

    counts = {
        "designDirection": sum(r["kind"] == "designDirection" for r in recipes),
        "reference": sum(r["kind"] == "reference" for r in recipes),
        "motionPattern": sum(r["kind"] == "motionPattern" for r in recipes),
        "total": len(recipes),
    }
    if counts != EXPECTED_COUNTS:
        raise ValueError(f"Recipe coverage drift: expected {EXPECTED_COUNTS}, got {counts}")

    return {
        "name": "AI Agent Recipe Registry",
        "schemaVersion": "1.0.0",
        "purpose": "Deterministically materialize every current 3D design direction, MotionSites public reference record and MotionSites-derived motion pattern into an executable, original, accessible build recipe.",
        "usagePolicy": "vault-authored instructions; external references remain reference-only",
        "counts": counts,
        "requiredRecipeFields": [
            "whenToUse", "whenNotToUse", "designObjective", "compositionInstructions", "motionInstructions",
            "implementationApproach", "assetInstructions", "responsiveBehavior", "performanceLimits",
            "accessibilityAndFallback", "originalityRules", "acceptanceCriteria", "agentPrompt",
        ],
        "recipes": recipes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Generated JSON output path")
    parser.add_argument("--check", action="store_true", help="Validate full coverage without writing output")
    parser.add_argument("--stdout", action="store_true", help="Print generated JSON to stdout")
    args = parser.parse_args()

    catalog = build_catalog()
    payload = json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"
    if args.stdout:
        print(payload, end="")
    if not args.check:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
        print(f"Wrote {catalog['counts']['total']} recipes to {output.relative_to(ROOT)}")
    else:
        print(f"Validated {catalog['counts']['total']} recipes: {catalog['counts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
