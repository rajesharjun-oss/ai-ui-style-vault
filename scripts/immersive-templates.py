#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "immersive-templates" / "template-catalog.json"
SOURCES = ROOT / "immersive-templates" / "source-policy.json"


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


def profile_tokens(profile):
    return tok([
        profile.get("businessCategory"), profile.get("subcategories", []),
        profile.get("offers", []), profile.get("audiences", []),
        profile.get("primaryConversion", {}), profile.get("brandSignals", {}),
        profile.get("operationalFacts", {})
    ])


def validate():
    data = load(CATALOG)
    sources = load(SOURCES)
    source_ids = {x["id"] for x in sources["sources"]}
    required = {
        "id", "label", "level", "summary", "sourceId", "reuseMode", "domains", "goals", "signals",
        "blueprint", "runtimes", "performanceTier", "assetReadiness", "stateModel", "effects",
        "mobile", "reducedMotion", "fallback", "avoid"
    }
    ids = []
    for item in data["templates"]:
        missing = required - set(item)
        if missing:
            raise ValueError(f"{item.get('id', '?')} missing {sorted(missing)}")
        if item["sourceId"] not in source_ids:
            raise ValueError(f"{item['id']} references unknown source {item['sourceId']}")
        if item["level"] not in (1, 2, 3, 4):
            raise ValueError(f"{item['id']} invalid level")
        if not item["fallback"] or not item["reducedMotion"]:
            raise ValueError(f"{item['id']} missing fallback")
        ids.append(item["id"])
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate template ids")
    if data["selectionPolicy"].get("noneIsValid") is not True:
        raise ValueError("none must be valid")
    sylva = next(x for x in sources["sources"] if x["id"] == "sylva")
    if "no licence" not in sylva["license"].lower():
        raise ValueError("Sylva reuse boundary must remain explicit")
    fluid = next(x for x in sources["sources"] if x["id"] == "webgl-fluid-background")
    if fluid["license"] != "MIT" or fluid["reuse"] != "mit-reference-selective-adaptation":
        raise ValueError("fluid source provenance mismatch")
    return {"status": "valid", "templates": len(ids), "sources": len(source_ids)}


def score(item, profile, goal, requested_level, performance_priority, asset_readiness):
    if requested_level and item["level"] != requested_level:
        return None
    if asset_readiness not in item["assetReadiness"]:
        return None
    domain = profile.get("recommendedDomainPack")
    p = profile_tokens(profile) | tok(goal)
    overlap = sorted(p & tok(item["signals"] + item["goals"]))
    value = 4
    reasons = []
    if domain in item["domains"]:
        value += 8
        reasons.append(f"matches {domain}")
    elif item["domains"]:
        value -= 2
    goal_overlap = sorted(tok(goal) & tok(item["goals"] + item["signals"]))
    if goal_overlap:
        value += min(10, len(goal_overlap) * 3)
        reasons.append("goal: " + ", ".join(goal_overlap[:5]))
    if overlap:
        value += min(8, len(overlap) * 2)
        reasons.append("business signals: " + ", ".join(overlap[:6]))
    if performance_priority == "high":
        if item["performanceTier"] == "high":
            return None
        if item["performanceTier"] == "balanced":
            value -= 3
            reasons.append("performance penalty")
    if item["level"] == 4 and asset_readiness in {"none", "limited"}:
        return None
    return {
        "id": item["id"], "label": item["label"], "score": value, "level": item["level"],
        "blueprint": item["blueprint"], "runtimes": item["runtimes"],
        "performanceTier": item["performanceTier"], "reuseMode": item["reuseMode"],
        "recommendedEffects": item["effects"], "reason": "; ".join(reasons) or "general immersive fit",
        "mobileStrategy": item["mobile"], "reducedMotionFallback": item["reducedMotion"],
        "fallback": item["fallback"]
    }


def select(profile, goal, level=None, performance_priority="normal", asset_readiness="limited"):
    data = load(CATALOG)
    if profile.get("designSelectionAllowed") is not True:
        return {
            "status": "blocked", "decision": "none", "recommended": None,
            "reason": "business profile has not passed the research/design gate", "candidates": []
        }
    items = []
    for item in data["templates"]:
        result = score(item, profile, goal, level, performance_priority, asset_readiness)
        if result:
            items.append(result)
    items.sort(key=lambda x: (-x["score"], x["id"]))
    items = items[:data["selectionPolicy"]["maxRecommendations"]]
    if not items or items[0]["score"] < data["selectionPolicy"]["minimumScore"]:
        return {
            "status": "ready", "decision": "none", "recommended": None, "goal": goal,
            "reason": "No immersive architecture cleared the threshold; use the normal domain-pack website.",
            "candidates": items
        }
    return {
        "status": "ready", "decision": "immersive-template", "recommended": items[0], "goal": goal,
        "reason": "Top template cleared the semantic threshold; generate its skill and still validate effects/3D separately.",
        "candidates": items
    }


def template_by_id(template_id):
    for item in load(CATALOG)["templates"]:
        if item["id"] == template_id:
            return item
    raise KeyError(template_id)


def source_by_id(source_id):
    for item in load(SOURCES)["sources"]:
        if item["id"] == source_id:
            return item
    raise KeyError(source_id)


def skill(item):
    source = source_by_id(item["sourceId"])
    avoid = "\n".join(f"- {x}" for x in item["avoid"])
    states = " → ".join(item["stateModel"])
    effects = ", ".join(item["effects"]) if item["effects"] else "none"
    domains = ", ".join(item["domains"]) if item["domains"] else "signal/goal driven"
    return f'''---
name: build-{item["id"]}
description: "Build an original {item["label"]} experience after Vault business and domain selection."
---

# {item["label"]}

## Purpose
{item["summary"]}

## Eligibility
- Immersion level: {item["level"]}
- Domain packs: {domains}
- Goals: {", ".join(item["goals"])}
- Signals: {", ".join(item["signals"])}
- 3D blueprint: `{item["blueprint"]}`
- Runtimes: {", ".join(item["runtimes"])}
- Performance tier: `{item["performanceTier"]}`
- Suggested effect contracts: {effects}

## Experience state model
`{states}`

## Mobile / accessibility
- Mobile: {item["mobile"]}
- Reduced motion: {item["reducedMotion"]}
- Non-immersive fallback: {item["fallback"]}

## Source and reuse boundary
- Research source: `{source["repository"]}` pinned at `{source["pinnedCommit"]}`
- Source licence status: {source["license"]}
- Vault reuse mode: `{item["reuseMode"]}`
- Source note: {source["notes"]}

Do not cross this reuse boundary. Reference-only sources contribute interaction principles, not source code, branding, copy, artwork, assets or exact choreography.

## Build sequence
1. Confirm `business-profile.json` is validated and the correct domain pack is selected.
2. Confirm this template was selected by `python scripts/vault-agent.py immersive <profile> --goal "<goal>"`.
3. Use verified business content and approved assets; do not transplant the research source's identity or claims.
4. Implement the semantic DOM experience and fallback first.
5. Implement the state model with explicit deterministic transitions.
6. Add only the recommended effect/3D recipes that pass their own semantic selector.
7. Bound camera, pointer and scroll interactions; keyboard/touch navigation must remain usable.
8. Apply the mobile and reduced-motion transformations above.
9. Measure performance and complete effect/3D plus rendered visual QA.
10. Run the anti-generic visual gate and Design Critic before handoff.

## Avoid
{avoid}
'''


def main():
    p = argparse.ArgumentParser(description="Immersive template selector, validator and Skill.md generator.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    sub.add_parser("list")
    s = sub.add_parser("select")
    s.add_argument("profile")
    s.add_argument("--goal", required=True)
    s.add_argument("--level", type=int, choices=[1, 2, 3, 4])
    s.add_argument("--performance-priority", choices=["normal", "high"], default="normal")
    s.add_argument("--asset-readiness", choices=["strong", "adequate", "limited", "none"], default="limited")
    g = sub.add_parser("skill")
    g.add_argument("template_id")
    g.add_argument("--output")
    args = p.parse_args()
    try:
        if args.cmd == "validate":
            print(json.dumps(validate(), indent=2))
            return 0
        if args.cmd == "list":
            data = load(CATALOG)
            print(json.dumps([
                {"id": x["id"], "label": x["label"], "level": x["level"], "summary": x["summary"]}
                for x in data["templates"]
            ], indent=2))
            return 0
        if args.cmd == "select":
            result = select(load(args.profile), args.goal, args.level, args.performance_priority, args.asset_readiness)
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return 0 if result["status"] == "ready" else 2
        if args.cmd == "skill":
            text = skill(template_by_id(args.template_id))
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
