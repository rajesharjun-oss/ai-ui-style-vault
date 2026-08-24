#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "3d" / "mode-classification.json"
INTENT = ROOT / "3d" / "interaction-intent-system.json"


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def tok(value):
    if value is None:
        return set()
    if isinstance(value, dict):
        out = set()
        for k, v in value.items():
            out |= tok(k)
            out |= tok(v)
        return out
    if isinstance(value, (list, tuple, set)):
        out = set()
        for item in value:
            out |= tok(item)
        return out
    return set(re.findall(r"[a-z0-9]+", str(value).lower()))


def normalize(value):
    return re.sub(r"\s+", " ", str(value).strip().lower())


def validate():
    data = load(CATALOG)
    required = {
        "level", "id", "label", "summary", "signals", "userControl", "assetRequirement",
        "preferredDelivery", "nextStage", "examples", "avoid"
    }
    levels = []
    ids = []
    for mode in data["modes"]:
        missing = required - set(mode)
        if missing:
            raise ValueError(f"{mode.get('id', '?')} missing {sorted(missing)}")
        levels.append(mode["level"])
        ids.append(mode["id"])
    if sorted(levels) != list(range(7)):
        raise ValueError("3D mode levels must be exactly 0 through 6")
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate 3D mode ids")
    if data.get("assetFormatPolicy", {}).get("rule") is None:
        raise ValueError("asset-format policy is required")
    return {"status": "valid", "modes": len(ids), "levels": [0, 1, 2, 3, 4, 5, 6]}


PHRASE_BOOSTS = {
    "interactive-world": [
        "interactive world", "game-like", "game like", "multiple interactive objects",
        "multi-object", "multi object", "character control", "digital twin", "custom physics",
        "custom shader", "large spatial data", "complex interaction"
    ],
    "spatial-exploration": [
        "walk through", "walkthrough", "property tour", "explore space", "first person",
        "room to room", "spatial navigation", "virtual showroom", "navigate the building"
    ],
    "configurable-object": [
        "configurator", "configure", "change colour", "change color", "change fabric",
        "switch material", "switch colour", "switch color", "material variant", "product variant",
        "customize", "customise", "swatch"
    ],
    "inspectable-object": [
        "360", "360 degree", "360-degree", "all angles", "turn around", "rotate",
        "swipe", "drag", "inspect", "zoom", "front side back", "front and back"
    ],
    "authored-animation": [
        "cinematic", "scroll scrub", "scroll-scrub", "camera path", "auto rotate",
        "automatic rotation", "authored animation", "assembly sequence", "scroll animation"
    ],
    "visual-only": [
        "3d hero", "hero 3d", "3d background", "floating object", "decorative 3d", "ambient 3d",
        "3d visual", "depth effect"
    ],
    "none": ["no 3d", "without 3d", "image is enough", "video is enough"]
}


MODE_GOALS = {
    "none": set(),
    "visual-only": {"story", "orient", "explain"},
    "authored-animation": {"story", "explain", "show-process", "explain-construction"},
    "inspectable-object": {"inspect", "compare", "show-material", "explain-layout", "explain-construction"},
    "configurable-object": {"configure", "compare", "show-material"},
    "spatial-exploration": {"navigate-space", "navigate", "explore-data", "explain-layout", "inspect"},
    "interactive-world": {"navigate-space", "navigate", "explore-data", "monitor", "story", "configure"}
}


def score_mode(mode, need):
    text = normalize(need)
    tokens = tok(text)
    if mode["id"] == "none":
        base = 0
    else:
        overlap = sorted(tokens & tok(mode["signals"]))
        base = min(8, len(overlap) * 2)
    matched_phrases = [p for p in PHRASE_BOOSTS.get(mode["id"], []) if p in text]
    phrase_weight = 9 if mode["id"] in {"interactive-world", "spatial-exploration", "configurable-object"} else 5
    value = base + min(24, len(matched_phrases) * phrase_weight)
    return {
        "id": mode["id"],
        "label": mode["label"],
        "level": mode["level"],
        "score": value,
        "matchedPhrases": matched_phrases[:6],
        "userControl": mode["userControl"],
        "assetRequirement": mode["assetRequirement"],
        "preferredDelivery": mode["preferredDelivery"],
        "nextStage": mode["nextStage"]
    }


def subject_context(subject_class, mode_id):
    if not subject_class:
        return {"subjectClass": None, "compatibility": "not-evaluated", "warnings": []}
    data = load(INTENT)
    subject = next((x for x in data["subjectClasses"] if x["id"] == subject_class), None)
    if subject is None:
        return {"subjectClass": subject_class, "compatibility": "unknown-subject-class", "warnings": ["Unknown 3D subject class; run the interaction-intent selector or use a declared class."]}
    mode_goals = MODE_GOALS.get(mode_id, set())
    valid = set(subject.get("validGoals", []))
    compatible = bool(mode_goals & valid) or mode_id in {"none", "visual-only", "authored-animation"}
    warnings = []
    if not compatible:
        warnings.append(
            f"Mode {mode_id} does not obviously match valid goals for {subject_class}: {', '.join(subject.get('validGoals', []))}. Review before implementation."
        )
    return {
        "subjectClass": subject_class,
        "compatibility": "compatible" if compatible else "review",
        "validGoals": subject.get("validGoals", []),
        "allowedInteractions": subject.get("allowedInteractions", []),
        "warnings": warnings
    }


def asset_plan(mode, asset_format, asset_readiness):
    fmt = (asset_format or "none").lower()
    readiness = asset_readiness or "none"
    requires_real_geometry = mode["level"] >= 3
    if not requires_real_geometry:
        return {
            "formatObserved": fmt,
            "readiness": readiness,
            "requiresRealGeometry": False,
            "action": "choose-lowest-complexity-delivery",
            "note": "The file format does not upgrade this mode. A GLB may still be used only as an authored visual/animation source."
        }
    if fmt in {"glb", "gltf"} and readiness in {"adequate", "strong"}:
        action = "validate-web-asset-and-select-runtime"
    else:
        action = "produce-or-source-approved-3d-asset"
    return {
        "formatObserved": fmt,
        "readiness": readiness,
        "requiresRealGeometry": True,
        "action": action,
        "note": "Interaction mode was selected from the user goal. Asset format only determines whether production work is still required."
    }


def classify(need, subject_class=None, asset_format=None, asset_readiness="none"):
    data = load(CATALOG)
    scored = [score_mode(m, need) for m in data["modes"]]
    priority = {mode_id: i for i, mode_id in enumerate(data["tieBreakPriority"])}
    scored.sort(key=lambda x: (-x["score"], priority.get(x["id"], 999)))
    top = scored[0]

    if top["score"] < 4:
        return {
            "status": "needs-clarification",
            "decision": "none",
            "mode": None,
            "reason": "The request does not state a clear 3D interaction goal. Do not infer rotatable GLB/GLTF behavior from the word 3D or from an available model file.",
            "formatDoesNotDetermineMode": True,
            "candidates": scored[:4]
        }

    mode = next(m for m in data["modes"] if m["id"] == top["id"])
    subject = subject_context(subject_class, mode["id"])
    assets = asset_plan(mode, asset_format, asset_readiness)

    if mode["id"] in {"inspectable-object", "configurable-object"}:
        if assets["action"] == "validate-web-asset-and-select-runtime":
            runtime_guidance = f"Run 3d-runtime selection with --mode {mode['id']}. Prefer <model-viewer> for bounded single-model inspection/configuration when it clears the runtime gate."
        else:
            runtime_guidance = "Keep this interaction mode, but route to 3D production-resource intelligence first to create/source an approved web-ready model."
    elif mode["id"] in {"spatial-exploration", "interactive-world"}:
        runtime_guidance = "Route to a custom Three.js/R3F/Babylon/WebGPU runtime plan; model-viewer is not the default for spatial/world interaction."
    elif mode["id"] == "authored-animation":
        runtime_guidance = "Choose between video/image sequence/model-viewer animation/custom Three.js based on fidelity and interaction needs; free rotation is not implied."
    elif mode["id"] == "visual-only":
        runtime_guidance = "Choose the lowest-cost visual medium. No user-controlled rotation is implied even if a GLB exists."
    else:
        runtime_guidance = "Use the normal non-3D build path."

    return {
        "status": "ready",
        "decision": "3d-mode",
        "mode": {
            "level": mode["level"],
            "id": mode["id"],
            "label": mode["label"],
            "summary": mode["summary"]
        },
        "userControl": mode["userControl"],
        "assetRequirement": mode["assetRequirement"],
        "preferredDelivery": mode["preferredDelivery"],
        "nextStage": mode["nextStage"],
        "assetPlan": assets,
        "subject": subject,
        "runtimeGuidance": runtime_guidance,
        "formatDoesNotDetermineMode": True,
        "reason": f"Selected {mode['id']} from explicit interaction signals: {', '.join(top['matchedPhrases']) or 'token match'}.",
        "candidates": scored[:4]
    }


def main():
    p = argparse.ArgumentParser(description="Classify an approved 3D request into one explicit interaction mode before runtime selection.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    sub.add_parser("list")
    s = sub.add_parser("classify")
    s.add_argument("need")
    s.add_argument("--subject-class")
    s.add_argument("--asset-format", choices=["glb", "gltf", "other", "none"], default="none")
    s.add_argument("--asset-readiness", choices=["strong", "adequate", "limited", "none"], default="none")
    args = p.parse_args()
    try:
        if args.cmd == "validate":
            print(json.dumps(validate(), indent=2)); return 0
        if args.cmd == "list":
            print(json.dumps(load(CATALOG)["modes"], indent=2, ensure_ascii=False)); return 0
        if args.cmd == "classify":
            print(json.dumps(classify(args.need, args.subject_class, args.asset_format, args.asset_readiness), indent=2, ensure_ascii=False)); return 0
    except Exception as exc:
        print(json.dumps({"status": "error", "reason": str(exc)}, indent=2), file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
