#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "packs/real-estate"
REQUIRED = [
    "pack.json","production-themes.json","page-blueprints.json","component-manifest.json",
    "state-vocabulary.json","content-and-listing-standard.md","property-media-standard.md",
    "motion-guidance.md","accessibility-and-responsive.md","implementation-prompt.md",
    "templates/REAL_ESTATE_BUILD_CONTRACT.md"
]
JSON_FILES = ["pack.json","production-themes.json","page-blueprints.json","component-manifest.json","state-vocabulary.json"]

def main() -> int:
    errors = []
    for rel in REQUIRED:
        path = PACK / rel
        if not path.exists():
            errors.append(f"missing: {path.relative_to(ROOT)}")
    for rel in JSON_FILES:
        path = PACK / rel
        if path.exists():
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"invalid JSON {rel}: {exc}")
    if not errors:
        pack = json.loads((PACK / "pack.json").read_text(encoding="utf-8"))
        if pack.get("id") != "real-estate":
            errors.append("pack id must be real-estate")
        if "business-profile.json" not in pack.get("requiredPlanningArtifacts", []):
            errors.append("business-profile.json must be required")
        states = set(json.loads((PACK / "state-vocabulary.json").read_text())["states"])
        for required in {"available","reserved","sold","availability-unknown","price-on-request"}:
            if required not in states:
                errors.append(f"missing property state: {required}")
        if not pack.get("rejectConditions"):
            errors.append("rejectConditions must not be empty")
    if errors:
        print("REAL ESTATE PACK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("REAL ESTATE PACK: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
