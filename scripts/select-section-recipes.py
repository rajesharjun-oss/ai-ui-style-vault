#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "system/section-recipes.json"


def norm(v): return str(v or "").strip().lower()

def conversion_type(action):
    a = norm(action)
    for key, terms in {
        "book":["book","appointment","reservation"],"enquire":["enquire","inquire","quote","consultation","whatsapp"],
        "buy":["buy","purchase","shop"],"order":["order"],"trial":["trial"],"signup":["signup","sign up","register"],
        "demo":["demo"],"viewing":["viewing","tour","inspection"],"contact":["contact","call","email"]}.items():
        if any(t in a for t in terms): return key
    return "contact"


def score_recipe(recipe, section, domain, conversion, density, evidence):
    if recipe["section"] != section:
        return None
    score = 0
    domains = recipe.get("bestFor", [])
    score += 35 if domain in domains else 15 if "all" in domains else 5
    convs = recipe.get("conversion", [])
    score += 25 if conversion in convs else 15 if "any" in convs else 5
    densities = recipe.get("density", [])
    score += 20 if density in densities else 10
    required = recipe.get("requires", [])
    if not required:
        score += 20
    else:
        matched = sum(1 for r in required if any(token in norm(r) for token in evidence))
        score += min(20, 8 + matched * 4)
    return score


def main():
    p = argparse.ArgumentParser(description="Select section-level Vault recipes by purpose, domain, conversion and evidence.")
    p.add_argument("profile")
    p.add_argument("--domain-pack", required=True)
    p.add_argument("--section", action="append", required=True, choices=["hero","proof","services","gallery","process","pricing","team","faq","cta","footer"])
    p.add_argument("--density", choices=["sparse","balanced","informational","data-dense"], default="balanced")
    p.add_argument("--evidence", action="append", default=[])
    p.add_argument("--top", type=int, default=2)
    args = p.parse_args()
    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    if profile.get("status") != "ready" or not profile.get("designSelectionAllowed"):
        print(json.dumps({"status":"blocked","reason":"Business research gate is not ready."}, indent=2)); return 2
    conversion = conversion_type(profile.get("primaryConversion", {}).get("action"))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))["recipes"]
    evidence = [norm(e) for e in args.evidence]
    selected = {}
    for section in args.section:
        scored = []
        for recipe in catalog:
            score = score_recipe(recipe, section, args.domain_pack, conversion, args.density, evidence)
            if score is not None:
                scored.append({"id":recipe["id"],"score":score,"composition":recipe["composition"],"requires":recipe.get("requires",[]),"avoid":recipe.get("avoid",[])})
        scored.sort(key=lambda x: (-x["score"], x["id"]))
        selected[section] = scored[:args.top]
    print(json.dumps({"status":"ready","domainPack":args.domain_pack,"conversionType":conversion,"density":args.density,"selected":selected}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
