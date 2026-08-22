#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "interactive-effects" / "effects.json"
THREEUI = ROOT / "references" / "threeui-community.json"

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
        for x in value:
            out |= tok(x)
        return out
    return set(re.findall(r"[a-z0-9]+", str(value).lower()))

def profile_tokens(profile):
    return tok([
        profile.get("businessCategory"), profile.get("subcategories", []),
        profile.get("offers", []), profile.get("audiences", []),
        profile.get("primaryConversion", {}), profile.get("brandSignals", {}),
        profile.get("operationalFacts", {}),
    ])

def validate():
    data = load(CATALOG)
    ref = load(THREEUI)
    required = {"id", "label", "family", "summary", "sections", "domains", "signals", "runtime", "tier", "assetMode", "mobile", "reducedMotion", "controls", "avoid"}
    ids = []
    for effect in data["effects"]:
        missing = required - set(effect)
        if missing:
            raise ValueError(f"{effect.get('id', '?')} missing {sorted(missing)}")
        ids.append(effect["id"])
        if effect["tier"] not in data["performanceTiers"]:
            raise ValueError(f"{effect['id']} has unknown tier")
        if not effect["reducedMotion"]:
            raise ValueError(f"{effect['id']} missing reduced-motion fallback")
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate effect ids")
    if data["selectionPolicy"].get("noneIsValid") is not True:
        raise ValueError("none must be valid")
    refs = [x["id"] for x in ref["referencePatterns"]]
    if any("pro" in x.lower() or "beta" in x.lower() for x in refs):
        raise ValueError("restricted ThreeUI record")
    if "do not copy" not in ref["licenseBoundary"]["proAndBeta"].lower():
        raise ValueError("missing Pro/Beta boundary")
    return {"status": "valid", "effects": len(ids), "threeUIReferences": len(refs)}

def score(effect, profile, section, performance_priority, asset_readiness, data):
    if section not in effect["sections"]:
        return None
    domain = profile.get("recommendedDomainPack")
    p = profile_tokens(profile)
    signals = tok(effect["signals"])
    overlap = sorted(p & signals)
    value = 8
    reasons = [f"supports {section}"]
    if domain in effect["domains"]:
        value += 8
        reasons.append(f"matches {domain}")
    elif effect["domains"]:
        value -= 3
    if overlap:
        value += min(8, len(overlap) * 2)
        reasons.append("signals: " + ", ".join(overlap[:6]))
    if effect["assetMode"] == "required" and asset_readiness == "none":
        return None
    if effect["assetMode"] == "required" and asset_readiness == "limited":
        value -= 5
        reasons.append("limited assets")
    if performance_priority == "high":
        if effect["tier"] == "high":
            return None
        if effect["tier"] == "balanced":
            value -= 3
            reasons.append("performance penalty")
    if domain in data["selectionPolicy"].get("restrainedDomains", []) and len(overlap) < 2:
        value -= 10
        reasons.append("restrained domain needs explicit signals")
    return {"id": effect["id"], "label": effect["label"], "score": value, "runtime": effect["runtime"], "performanceTier": effect["tier"], "reason": "; ".join(reasons), "controlDefaults": effect["controls"], "mobileStrategy": effect["mobile"], "reducedMotionFallback": effect["reducedMotion"]}

def select(profile, section="hero", performance_priority="normal", asset_readiness="limited"):
    data = load(CATALOG)
    if profile.get("designSelectionAllowed") is not True:
        return {"status": "blocked", "decision": "none", "recommended": None, "reason": "business profile has not passed the research/design gate", "candidates": []}
    items = []
    for effect in data["effects"]:
        x = score(effect, profile, section, performance_priority, asset_readiness, data)
        if x:
            items.append(x)
    items.sort(key=lambda x: (-x["score"], x["id"]))
    items = items[: data["selectionPolicy"]["maxRecommendations"]]
    if not items or items[0]["score"] < data["selectionPolicy"]["minimumScore"]:
        return {"status": "ready", "decision": "none", "recommended": None, "section": section, "reason": "No effect cleared the semantic threshold; keep the normal static/component composition.", "candidates": items}
    return {"status": "ready", "decision": "effect", "recommended": items[0], "section": section, "reason": "Top effect cleared the semantic threshold; measured QA is still required.", "candidates": items}

def effect_by_id(effect_id):
    for x in load(CATALOG)["effects"]:
        if x["id"] == effect_id:
            return x
    raise KeyError(effect_id)

def skill(effect):
    avoid = "\n".join(f"- {x}" for x in effect["avoid"]) if effect["avoid"] else "- None"
    return f'''---
name: implement-{effect["id"]}
description: "Implement {effect["label"]} only after Vault semantic selection."
---

# {effect["label"]}

## Purpose
{effect["summary"]}

## Eligibility
- Sections: {", ".join(effect["sections"])}
- Domain packs: {", ".join(effect["domains"])}
- Signals: {", ".join(effect["signals"])}
- Runtime: `{effect["runtime"]}`
- Performance tier: `{effect["tier"]}`
- Asset mode: `{effect["assetMode"]}`

## Default controls
```json
{json.dumps(effect["controls"], indent=2)}
```

## Mobile and fallback
- Mobile: {effect["mobile"]}
- Reduced motion: {effect["reducedMotion"]}

## Avoid
{avoid}

## Implementation
1. Confirm the validated business profile, domain pack and selected section recipe.
2. Re-run `python scripts/vault-agent.py effect <profile> --section <section>` if context changed.
3. Use the lowest-complexity compatible runtime; do not increase spectacle by default.
4. Preserve keyboard, touch, focus, readable content and the reduced-motion fallback.
5. Do not introduce fake telemetry, fake places, unapproved real-business media or unsupported claims.
6. Record measured desktop/mobile observations in `EFFECT_QA_OBSERVATIONS.json`.
7. Run `python scripts/vault-agent.py effect-qa {effect["id"]} EFFECT_QA_OBSERVATIONS.json`.
8. Route to the 3D interaction-intent system if the subject becomes explorable/configurable/spatially informative.

## Provenance
The effect contract is Vault-authored. ThreeUI Community is a public research/reference source for interaction-system ideas; restricted Pro/Beta source and remote catalog media are outside the Vault's reuse boundary.
'''

def qa(effect_id, obs):
    data = load(CATALOG)
    effect = effect_by_id(effect_id)
    tier = data["performanceTiers"][effect["tier"]]
    checks = []
    def add(name, passed, detail):
        checks.append({"check": name, "passed": bool(passed), "detail": detail})
    if obs.get("effectId") and obs["effectId"] != effect_id:
        add("effect-id", False, obs["effectId"])
    else:
        add("effect-id", True, effect_id)
    for target in ("desktop", "mobile"):
        sample = obs.get(target, {})
        minimum = tier[f"{target}MinFps"]
        ratio = sample.get("slowFrameRatio")
        fps = sample.get("fps")
        add(f"{target}-fps", isinstance(fps, (int, float)) and fps >= minimum, f"{fps} observed; {minimum} required")
        limit = tier["maxSlowFrameRatio"]
        add(f"{target}-slow-frames", isinstance(ratio, (int, float)) and ratio <= limit, f"{ratio} observed; <= {limit} required")
    add("reduced-motion", obs.get("reducedMotionFallback") is True, "required")
    if tier.get("contextLoss"):
        add("context-loss", obs.get("contextLossRecovery") is True, "required for this tier")
    add("teardown", obs.get("teardownClean") is True, "continuous runtime resources released")
    errors = obs.get("consoleErrors", [])
    add("console", isinstance(errors, list) and not errors, f"{len(errors) if isinstance(errors, list) else 'invalid'} errors")
    passed = all(x["passed"] for x in checks)
    return {"status": "pass" if passed else "fail", "effectId": effect_id, "performanceTier": effect["tier"], "checks": checks, "fallbackRequired": not passed, "fallback": None if passed else effect["reducedMotion"]}

def main():
    p = argparse.ArgumentParser(description="Interactive Effect Intelligence: validate, select, generate a skill, or grade performance QA.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    s = sub.add_parser("select")
    s.add_argument("profile")
    s.add_argument("--section", default="hero")
    s.add_argument("--performance-priority", choices=["normal", "high"], default="normal")
    s.add_argument("--asset-readiness", choices=["strong", "adequate", "limited", "none"], default="limited")
    g = sub.add_parser("skill")
    g.add_argument("effect_id")
    g.add_argument("--output")
    q = sub.add_parser("qa")
    q.add_argument("effect_id")
    q.add_argument("observations")
    q.add_argument("--json-out")
    args = p.parse_args()
    try:
        if args.cmd == "validate":
            print(json.dumps(validate(), indent=2)); return 0
        if args.cmd == "select":
            result = select(load(args.profile), args.section, args.performance_priority, args.asset_readiness)
            print(json.dumps(result, indent=2, ensure_ascii=False)); return 0 if result["status"] == "ready" else 2
        if args.cmd == "skill":
            text = skill(effect_by_id(args.effect_id))
            if args.output: Path(args.output).write_text(text, encoding="utf-8")
            else: print(text, end="")
            return 0
        if args.cmd == "qa":
            result = qa(args.effect_id, load(args.observations)); text = json.dumps(result, indent=2)
            if args.json_out: Path(args.json_out).write_text(text + "\n", encoding="utf-8")
            print(text); return 0 if result["status"] == "pass" else 1
    except Exception as exc:
        print(json.dumps({"status": "error", "reason": str(exc)}, indent=2), file=sys.stderr); return 2
    return 2

if __name__ == "__main__":
    raise SystemExit(main())
