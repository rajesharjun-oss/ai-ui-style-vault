#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "packs/fashion-couture"
REQUIRED = [
    "pack.json","production-themes.json","page-blueprints.json","component-manifest.json",
    "state-vocabulary.json","content-and-merchandising.md","photography-and-material-standard.md",
    "motion-guidance.md","accessibility-and-responsive.md","implementation-prompt.md",
    "templates/FASHION_BUILD_CONTRACT.md"
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
        if pack.get("id") != "fashion-couture":
            errors.append("pack id must be fashion-couture")
        if "business-profile.json" not in pack.get("requiredPlanningArtifacts", []):
            errors.append("business-profile.json must be a required planning artifact")
        if not pack.get("rejectConditions"):
            errors.append("rejectConditions must not be empty")
    if errors:
        print("FASHION & COUTURE PACK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("FASHION & COUTURE PACK: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
