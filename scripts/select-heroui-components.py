#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "references/heroui-v3/component-catalog.json"

TASK_HINTS = {
    "form": ["form","input","textfield","textarea","label","description","field-error","fieldset","button"],
    "search": ["search-field","autocomplete","combo-box","list-box","list-box-item","empty-state","spinner"],
    "table": ["table","pagination","skeleton","empty-state","alert"],
    "dialog": ["modal","alert-dialog","drawer","button","close-button"],
    "navigation": ["breadcrumbs","tabs","link","menu","menu-item","dropdown"],
    "selection": ["select","checkbox","checkbox-group","radio","radio-group","switch","switch-group","tag","tag-group"],
    "date": ["date-field","date-picker","date-range-picker","calendar","range-calendar","calendar-year-picker","time-field"],
    "feedback": ["alert","toast","progress-bar","progress-circle","spinner","skeleton","empty-state"],
    "settings": ["switch","switch-group","select","slider","color-picker","color-field","button"],
    "otp": ["input-otp","field-error","label","description","button"],
    "command": ["autocomplete","list-box","list-box-item","kbd","popover","search-field"],
    "filters": ["select","checkbox-group","tag-group","slider","date-range-picker","button"],
    "profile": ["avatar","badge","card","tabs","button","link"],
    "wizard": ["progress-bar","form","button","alert","field-error"],
    "toolbar": ["toolbar","button","button-group","toggle-button","toggle-button-group","tooltip"],
    "color": ["color-area","color-field","color-picker","color-slider","color-swatch","color-swatch-picker"],
}


def flatten(catalog):
    out = {}
    for category, names in catalog["categories"].items():
        for name in names:
            out[name] = category
    return out


def main():
    parser = argparse.ArgumentParser(description="Shortlist HeroUI v3 primitives for an interface task without making HeroUI the visual direction.")
    parser.add_argument("task", help="Task description, e.g. 'search filters table', 'booking date form', 'settings dialog'")
    parser.add_argument("--max", type=int, default=16)
    parser.add_argument("--stack", choices=["react-tailwind4","react-other","non-react"], default="react-tailwind4")
    args = parser.parse_args()

    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    component_to_category = flatten(catalog)
    text = args.task.lower()
    scores = {name: 0 for name in component_to_category}
    reasons = {name: [] for name in component_to_category}

    for hint, names in TASK_HINTS.items():
        if hint in text:
            for rank, name in enumerate(names):
                if name in scores:
                    points = max(3, 10 - rank)
                    scores[name] += points
                    reasons[name].append(f"task:{hint}")

    # Direct component-name mentions receive strongest priority.
    for name in component_to_category:
        phrase = name.replace("-", " ")
        if name in text or phrase in text:
            scores[name] += 15
            reasons[name].append("direct-match")

    ranked = sorted(
        ((score, name) for name, score in scores.items() if score > 0),
        key=lambda item: (-item[0], item[1]),
    )[: max(1, args.max)]

    adoption = {
        "react-tailwind4": "dependency-preferred",
        "react-other": "compatibility-review",
        "non-react": "behavior-contract-only",
    }[args.stack]

    selected = []
    for score, name in ranked:
        category = component_to_category[name]
        selected.append({
            "component": name,
            "category": category,
            "score": score,
            "reasons": reasons[name],
            "statesToPreserve": catalog["stateFamilies"].get(category, ["default"]),
            "sourcePath": catalog["upstream"]["sourcePathTemplate"].replace("{component}", name),
            "stylePath": catalog["upstream"]["stylePathTemplate"].replace("{component}", name),
        })

    print(json.dumps({
        "status": "ready",
        "task": args.task,
        "stack": args.stack,
        "adoptionMode": adoption,
        "upstreamPackage": catalog["upstream"]["package"],
        "selected": selected,
        "rule": "HeroUI primitives accelerate implementation; Vault domain, theme, section, content and visual QA rules remain authoritative."
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
