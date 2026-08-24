#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "3d-production-resources" / "resource-catalog.json"
POLICY = ROOT / "3d-production-resources" / "source-policy.json"


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
    policy = load(POLICY)
    source_ids = {x["id"] for x in policy["sources"]}
    required = {"id", "label", "summary", "sourceId", "domains", "needs", "outputs", "workflow", "resourceCandidates", "avoid"}
    ids = []
    candidates = 0
    for category in data["categories"]:
        missing = required - set(category)
        if missing:
            raise ValueError(f"{category.get('id', '?')} missing {sorted(missing)}")
        if category["sourceId"] not in source_ids:
            raise ValueError(f"{category['id']} references unknown source {category['sourceId']}")
        if not category["workflow"] or not category["outputs"] or not category["resourceCandidates"]:
            raise ValueError(f"{category['id']} must define workflow, outputs and candidates")
        for candidate in category["resourceCandidates"]:
            for field in ("name", "url", "role", "licenseStatus"):
                if not candidate.get(field):
                    raise ValueError(f"{category['id']} candidate missing {field}")
            if candidate["licenseStatus"] == "CC0-1.0":
                raise ValueError("linked resource must not inherit Awesome Blender CC0")
            candidates += 1
        ids.append(category["id"])
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate resource category ids")
    if data["selectionPolicy"].get("noneIsValid") is not True:
        raise ValueError("none must be valid")
    if policy["linkedResourcePolicy"].get("inheritSourceLicense") is not False:
        raise ValueError("linked resources must not inherit source-list license")
    awesome = next(x for x in policy["sources"] if x["id"] == "awesome-blender")
    if awesome["sourceLicense"] != "CC0-1.0":
        raise ValueError("Awesome Blender source-list licence mismatch")
    return {"status": "valid", "categories": len(ids), "resourceCandidates": candidates, "sources": len(source_ids)}


def score(category, need, domain=None):
    need_tokens = tok(need)
    signal_tokens = tok(category["needs"] + category["outputs"] + [category["label"], category["summary"]])
    overlap = sorted(need_tokens & signal_tokens)
    if not overlap:
        return None
    value = min(16, len(overlap) * 3)
    reasons = ["need: " + ", ".join(overlap[:8])]
    if domain:
        if domain in category["domains"]:
            value += 6
            reasons.append(f"matches {domain}")
        elif category["domains"]:
            value -= 1
    return {
        "id": category["id"],
        "label": category["label"],
        "score": value,
        "summary": category["summary"],
        "outputs": category["outputs"],
        "reason": "; ".join(reasons),
        "resourceCandidates": category["resourceCandidates"],
        "workflow": category["workflow"],
        "avoid": category["avoid"],
        "rightsGate": "Verify each candidate's own current licence/terms, compatibility and asset provenance before production use."
    }


def select(need, domain=None, limit=None):
    data = load(CATALOG)
    items = []
    for category in data["categories"]:
        result = score(category, need, domain)
        if result:
            items.append(result)
    items.sort(key=lambda x: (-x["score"], x["id"]))
    max_items = limit or data["selectionPolicy"]["maxRecommendations"]
    items = items[:max_items]
    if not items or items[0]["score"] < data["selectionPolicy"]["minimumScore"]:
        return {
            "status": "ready",
            "decision": "none",
            "recommended": None,
            "need": need,
            "domain": domain,
            "reason": "No production-resource category cleared the threshold. Define the required 3D asset/output more specifically before selecting tools.",
            "candidates": items
        }
    return {
        "status": "ready",
        "decision": "3d-production-resource",
        "recommended": items[0],
        "need": need,
        "domain": domain,
        "reason": "Top production category matches the stated need. External candidates still require their own licence, compatibility and provenance checks.",
        "candidates": items
    }


def category_by_id(category_id):
    for item in load(CATALOG)["categories"]:
        if item["id"] == category_id:
            return item
    raise KeyError(category_id)


def skill(category):
    candidates = "\n".join(
        f"- [{x['name']}]({x['url']}) — {x['role']} — licence/terms: `{x['licenseStatus']}`"
        for x in category["resourceCandidates"]
    )
    workflow = "\n".join(f"{i}. {step}" for i, step in enumerate(category["workflow"], 1))
    avoid = "\n".join(f"- {x}" for x in category["avoid"])
    domains = ", ".join(category["domains"]) if category["domains"] else "cross-domain"
    return f'''---
name: produce-{category["id"]}
description: "Use the Vault 3D production-resource layer to plan {category["label"]} work after 3D has already been justified."
---

# {category["label"]}

## Purpose
{category["summary"]}

## Eligibility
- Domain fit: {domains}
- Typical needs: {", ".join(category["needs"])}
- Expected outputs: {", ".join(category["outputs"])}

## Production workflow
{workflow}

## Representative discovery candidates
{candidates}

These are discovery candidates, not approved dependencies/assets. The Awesome Blender list is only the discovery source; each linked resource has its own licence/terms.

## Rights and provenance gate
1. Open the selected candidate's own official repository/site and verify current licence/terms.
2. Confirm commercial use, modification, redistribution, embedding and generated-output rights for this project.
3. Record provenance separately for code/add-ons and for every model, texture, HDRI, audio file, scan or dataset.
4. Check supported Blender version, maintenance status, export compatibility and security risk before installing or executing code.
5. Do not vendor paid, account-gated or restricted third-party assets into the Vault.
6. For real products/properties/places/facilities, use authoritative or owner-approved source data when accuracy matters.

## Web-delivery gate
- Raw Blender production scenes are not browser deliverables.
- Retopologize/decimate where needed, bake procedural/high-poly detail, compress textures and animations, and export only the smallest sufficient representation.
- Validate the asset in the actual browser runtime and preserve the existing mobile, reduced-motion and non-WebGL fallback contracts.

## Avoid
{avoid}
'''


def main():
    p = argparse.ArgumentParser(description="3D production resource selector, validator and Skill.md generator.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    sub.add_parser("list")
    s = sub.add_parser("select")
    s.add_argument("need")
    s.add_argument("--domain")
    s.add_argument("--max", dest="max_items", type=int, choices=range(1, 9))
    g = sub.add_parser("skill")
    g.add_argument("category_id")
    g.add_argument("--output")
    args = p.parse_args()
    try:
        if args.cmd == "validate":
            print(json.dumps(validate(), indent=2))
            return 0
        if args.cmd == "list":
            print(json.dumps([
                {"id": x["id"], "label": x["label"], "summary": x["summary"], "outputs": x["outputs"]}
                for x in load(CATALOG)["categories"]
            ], indent=2))
            return 0
        if args.cmd == "select":
            result = select(args.need, args.domain, args.max_items)
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return 0
        if args.cmd == "skill":
            text = skill(category_by_id(args.category_id))
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
