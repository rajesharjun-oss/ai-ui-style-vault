#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "3d-delivery-runtimes" / "runtime-catalog.json"
SOURCES = ROOT / "3d-delivery-runtimes" / "source-policy.json"
MODE_IDS = {
    "none", "visual-only", "authored-animation", "inspectable-object",
    "configurable-object", "spatial-exploration", "interactive-world"
}


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


def validate():
    data = load(CATALOG)
    sources = load(SOURCES)
    source_ids = {x["id"] for x in sources["sources"]}
    runtime = data["runtime"]
    if runtime["sourceId"] not in source_ids:
        raise ValueError("runtime source is not declared")
    required = {
        "id", "label", "summary", "compatibleModes", "goals", "signals", "requires", "features",
        "performanceTier", "mobile", "fallback", "avoid"
    }
    ids = []
    for item in data["profiles"]:
        missing = required - set(item)
        if missing:
            raise ValueError(f"{item.get('id', '?')} missing {sorted(missing)}")
        if not item["fallback"] or not item["mobile"]:
            raise ValueError(f"{item['id']} missing fallback/mobile strategy")
        unknown_modes = set(item["compatibleModes"]) - MODE_IDS
        if unknown_modes:
            raise ValueError(f"{item['id']} has unknown compatible modes {sorted(unknown_modes)}")
        if not item["compatibleModes"]:
            raise ValueError(f"{item['id']} must declare at least one compatible mode")
        ids.append(item["id"])
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate runtime profile ids")
    if data["selectionPolicy"].get("noneIsValid") is not True:
        raise ValueError("none must remain valid")
    if data["selectionPolicy"].get("modeGateRequired") is not True:
        raise ValueError("3D mode gate must remain required")
    source = next(x for x in sources["sources"] if x["id"] == runtime["sourceId"])
    if source["license"] != "Apache-2.0":
        raise ValueError("model-viewer license provenance mismatch")
    if source["package"] != "@google/model-viewer":
        raise ValueError("model-viewer package provenance mismatch")
    if "three" not in source.get("peerDependencies", {}):
        raise ValueError("tested Three.js peer dependency must be recorded")
    return {"status": "valid", "profiles": len(ids), "runtime": runtime["id"], "source": source["repository"], "modeGate": True}


def score(item, need, asset_format, ar_required, mode_id):
    text = tok(need)
    overlap = sorted(text & tok(item["signals"] + item["goals"] + item["features"]))
    compatible = mode_id in set(item["compatibleModes"])
    value = 6 if compatible else -100
    reasons = [f"mode: {mode_id}"] if compatible else []
    value += min(12, len(overlap) * 3)
    if overlap:
        reasons.append("signals: " + ", ".join(overlap[:6]))
    if asset_format and asset_format.lower() in {"glb", "gltf"}:
        value += 3
        reasons.append(f"format: {asset_format.lower()}")
    if ar_required:
        if item["id"] == "model-viewer-ar-placement" and compatible:
            value += 8
            reasons.append("AR explicitly required")
        else:
            value -= 3
    if "ar" in text and item["id"] == "model-viewer-ar-placement" and compatible:
        value += 5
    return {
        "id": item["id"],
        "label": item["label"],
        "score": value,
        "compatibleModes": item["compatibleModes"],
        "performanceTier": item["performanceTier"],
        "features": item["features"],
        "reason": "; ".join(reasons) or "incompatible with selected 3D mode",
        "mobileStrategy": item["mobile"],
        "fallback": item["fallback"]
    }


def select(need, mode_id, asset_format=None, ar_required=False):
    if mode_id not in MODE_IDS:
        raise ValueError(f"unknown 3D mode: {mode_id}")
    data = load(CATALOG)
    runtime = data["runtime"]

    if mode_id in {"none", "visual-only"}:
        return {
            "status": "ready", "decision": "none", "recommended": None,
            "mode": mode_id,
            "reason": "Selected 3D mode does not require a user-manipulable model-viewer runtime. Keep the simpler visual/non-3D delivery path.",
            "candidates": []
        }
    if mode_id in {"spatial-exploration", "interactive-world"}:
        return {
            "status": "ready", "decision": "escalate", "recommended": None,
            "mode": mode_id,
            "target": data["selectionPolicy"]["escalationTarget"],
            "reason": "Selected 3D mode requires a custom spatial/world runtime; do not force it into <model-viewer>.",
            "candidates": []
        }
    if not asset_format or asset_format.lower() not in {"glb", "gltf"}:
        return {
            "status": "blocked", "decision": "none", "recommended": None,
            "mode": mode_id,
            "reason": "No approved GLB/glTF delivery asset was declared. Keep the classified interaction mode and route to 3D production-resource intelligence before runtime selection.",
            "candidates": []
        }

    text = tok(need)
    escalate_hits = []
    for rule in runtime["escalateWhen"]:
        words = tok(rule)
        if len(text & words) >= 3:
            escalate_hits.append(rule)
    if escalate_hits:
        return {
            "status": "ready",
            "decision": "escalate",
            "recommended": None,
            "mode": mode_id,
            "target": data["selectionPolicy"]["escalationTarget"],
            "reason": "Need appears to exceed a bounded <model-viewer> interaction even though the classified mode is bounded enough to evaluate.",
            "matchedEscalationRules": escalate_hits[:3],
            "candidates": []
        }

    compatible = [x for x in data["profiles"] if mode_id in set(x["compatibleModes"])]
    items = [score(x, need, asset_format, ar_required, mode_id) for x in compatible]
    items.sort(key=lambda x: (-x["score"], x["id"]))
    items = items[:data["selectionPolicy"]["maxRecommendations"]]
    if not items or items[0]["score"] < data["selectionPolicy"]["minimumScore"]:
        return {
            "status": "ready", "decision": "none", "recommended": None,
            "mode": mode_id,
            "reason": "No model-viewer delivery profile cleared the threshold for the already-classified 3D mode. Keep the mode and evaluate a custom or simpler implementation without changing the interaction requirement.",
            "candidates": items
        }
    return {
        "status": "ready", "decision": "model-viewer", "runtime": runtime["id"],
        "mode": mode_id,
        "recommended": items[0],
        "reason": "A <model-viewer> profile compatible with the mandatory 3D mode gate cleared the threshold; generate its skill and validate the real asset/browser path.",
        "candidates": items
    }


def profile_by_id(profile_id):
    for item in load(CATALOG)["profiles"]:
        if item["id"] == profile_id:
            return item
    raise KeyError(profile_id)


def skill(item):
    data = load(CATALOG)
    source = next(x for x in load(SOURCES)["sources"] if x["id"] == data["runtime"]["sourceId"])
    avoid = "\n".join(f"- {x}" for x in item["avoid"])
    features = "\n".join(f"- `{x}`" for x in item["features"])
    requirements = "\n".join(f"- {x}" for x in item["requires"])
    compatible_modes = ", ".join(sorted(item["compatibleModes"]))
    return f'''---
name: implement-{item["id"]}
description: "Implement {item["label"]} with @google/model-viewer after 3D mode, relevance and asset-production approval."
---

# {item["label"]}

## Purpose
{item["summary"]}

## Mandatory 3D mode gate
- Compatible modes: {compatible_modes}
- Do not use this runtime profile unless the request has already been classified into one of those modes.
- A GLB/GLTF file does not determine the mode and does not by itself authorize free rotation, configuration or AR.

## Runtime
- Package: `@google/model-viewer`
- Observed upstream version at review: `{source["observedPackageVersion"]}`
- License: `{source["license"]}`
- Pin tested peer dependency: `three {source["peerDependencies"]["three"]}`
- Primary delivery formats: GLB / glTF

## Required inputs
{requirements}

## Approved capability set
{features}

## Mobile and fallback
- Mobile: {item["mobile"]}
- Fallback: {item["fallback"]}

## Implementation sequence
1. Confirm the business/subject passed the Vault 3D relevance and interaction-intent gates.
2. Confirm `python scripts/vault-agent.py 3d-mode ...` selected a compatible interaction mode.
3. Confirm the GLB/glTF and every visual/annotation/variant claim has provenance and usage rights.
4. Install/pin `@google/model-viewer` and its compatible Three.js peer; do not use `--legacy-peer-deps` as the default compatibility strategy.
5. Build the normal semantic content, CTA and fallback first.
6. Add only the approved capabilities above; keep controls/labels as semantic DOM where possible.
7. Use a poster and intentional loading strategy; preserve normal page scroll with touch interactions.
8. If AR is used, implement supported/unsupported/tracking-failure states and HTTPS requirements.
9. Test desktop/mobile browsers, reduced motion, keyboard/focus, loading failure and real device performance.
10. Escalate to custom Three.js/R3F/Babylon only if the classified mode or product task exceeds the bounded model-viewer contract.
11. Run 3D/performance QA and the Vault visual QA/Design Critic before handoff.

## Avoid
{avoid}

## Source boundary
The runtime is Apache-2.0 software from `{source["repository"]}` pinned for research at `{source["pinnedCommit"]}`. Shared demo models, environment maps and other upstream assets are not automatically cleared by the software licence; verify each asset separately.
'''


def main():
    p = argparse.ArgumentParser(description="Select the smallest sufficient 3D web delivery runtime after mandatory 3D mode classification.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    sub.add_parser("list")
    s = sub.add_parser("select")
    s.add_argument("need")
    s.add_argument("--mode", required=True, choices=sorted(MODE_IDS))
    s.add_argument("--format", choices=["glb", "gltf", "other"])
    s.add_argument("--ar", action="store_true")
    g = sub.add_parser("skill")
    g.add_argument("profile_id")
    g.add_argument("--output")
    args = p.parse_args()
    try:
        if args.cmd == "validate":
            print(json.dumps(validate(), indent=2)); return 0
        if args.cmd == "list":
            print(json.dumps([
                {"id": x["id"], "label": x["label"], "summary": x["summary"], "compatibleModes": x["compatibleModes"]}
                for x in load(CATALOG)["profiles"]
            ], indent=2)); return 0
        if args.cmd == "select":
            print(json.dumps(select(args.need, args.mode, args.format, args.ar), indent=2, ensure_ascii=False)); return 0
        if args.cmd == "skill":
            text = skill(profile_by_id(args.profile_id))
            if args.output:
                Path(args.output).write_text(text, encoding="utf-8")
            else:
                print(text, end="")
            return 0
    except Exception as exc:
        print(json.dumps({"status": "error", "reason": str(exc)}, indent=2), file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
