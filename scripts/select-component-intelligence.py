#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "references/component-gallery/component-catalog.json"


def norm(v):
    return str(v or "").strip().lower()


def score(item, query):
    q = norm(query)
    name = norm(item["name"])
    aliases = [norm(x) for x in item.get("aliases", [])]
    purpose = norm(item.get("purpose"))
    points = 0
    if q == name or q == item["id"]:
        points += 100
    tokens = [t for t in q.replace("/", " ").replace("-", " ").split() if t]
    for token in tokens:
        if token in name or token in item["id"]:
            points += 35
        if any(token in alias for alias in aliases):
            points += 25
        if token in purpose:
            points += 8
    return points


def main():
    p = argparse.ArgumentParser(description="Resolve a UI need to Component Gallery canonical families and HeroUI-compatible primitives.")
    p.add_argument("query", help="Component name, alias or brief, e.g. 'autosuggest with keyboard options'")
    p.add_argument("--top", type=int, default=5)
    args = p.parse_args()

    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    ranked = []
    for item in data["components"]:
        s = score(item, args.query)
        if s:
            ranked.append({
                "component": item["id"],
                "name": item["name"],
                "score": s,
                "aliases": item.get("aliases", []),
                "purpose": item.get("purpose"),
                "exampleCount": item.get("examples"),
                "heroUIMatches": item.get("heroUIMatches", []),
                "next": "Review references/component-gallery/ADOPTION_STANDARD.md, then use HeroUI directly when a compatible React primitive exists or implement the behavior contract with an accessible alternative."
            })
    ranked.sort(key=lambda x: (-x["score"], -x["exampleCount"], x["component"]))
    print(json.dumps({
        "status": "ready" if ranked else "no-match",
        "query": args.query,
        "source": data["source"],
        "selected": ranked[:max(1, args.top)]
    }, indent=2))
    return 0 if ranked else 2


if __name__ == "__main__":
    raise SystemExit(main())
