#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "references/component-gallery/component-catalog.json"
RULES = ROOT / "references/component-gallery/contract-rules.json"
HEROUI = ROOT / "references/heroui-v3/behavior-contracts.json"


def norm(value):
    return str(value or "").strip().lower()


def load():
    return (
        json.loads(CATALOG.read_text(encoding="utf-8")),
        json.loads(RULES.read_text(encoding="utf-8")),
        json.loads(HEROUI.read_text(encoding="utf-8")) if HEROUI.exists() else {"components": []},
    )


def find_component(query, catalog):
    q = norm(query)
    exact = []
    fuzzy = []
    for item in catalog["components"]:
        terms = [item["id"], item["name"], *item.get("aliases", [])]
        nt = [norm(x) for x in terms]
        if q in nt:
            exact.append(item)
        elif any(q in x or x in q for x in nt):
            fuzzy.append(item)
    pool = exact or fuzzy
    return pool[0] if pool else None


def build_contract(item, rules, heroui):
    archetype_id = rules["componentArchetypes"][item["id"]]
    archetype = rules["archetypes"][archetype_id]
    heroui_by_id = {x["id"]: x for x in heroui.get("components", [])}
    matches = []
    for match in item.get("heroUIMatches", []):
        matches.append({
            "id": match,
            "behaviorContract": heroui_by_id.get(match, {}).get("requiredBehavior", []),
            "states": heroui_by_id.get(match, {}).get("states", []),
        })
    return {
        "id": item["id"],
        "name": item["name"],
        "aliases": item.get("aliases", []),
        "purpose": item["purpose"],
        "referenceExampleCount": item["examples"],
        "archetype": archetype_id,
        "requiredStates": archetype["states"],
        "keyboardModel": archetype["keyboard"],
        "accessibilityChecks": archetype["a11y"],
        "responsiveChecks": archetype["responsive"],
        "avoid": archetype["avoid"],
        "universalRequirements": rules["universalRequirements"],
        "heroUI": matches,
        "selectionRule": "Use this component only when its semantics match the user task. Visual resemblance is not enough.",
    }


def main():
    p = argparse.ArgumentParser(description="Resolve a Component Gallery term into a Vault canonical component contract.")
    p.add_argument("component", help="Component name or alias, e.g. autosuggest, dropdown, dialog, snackbar")
    p.add_argument("--compact", action="store_true")
    args = p.parse_args()
    catalog, rules, heroui = load()
    item = find_component(args.component, catalog)
    if not item:
        print(json.dumps({"status":"not-found","query":args.component}, indent=2))
        return 2
    contract = build_contract(item, rules, heroui)
    if args.compact:
        contract = {k: contract[k] for k in ["id","name","purpose","archetype","requiredStates","heroUI","avoid"]}
    print(json.dumps({"status":"ready","contract":contract}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
