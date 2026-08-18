#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "packs/professional-services"
REQUIRED = [
    "pack.json","production-themes.json","page-blueprints.json","component-manifest.json",
    "state-vocabulary.json","content-and-trust.md","photography-and-proof-standard.md",
    "motion-guidance.md","accessibility-and-responsive.md","implementation-prompt.md",
    "templates/PROFESSIONAL_SERVICES_BUILD_CONTRACT.md"
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
        if pack.get("id") != "professional-services":
            errors.append("pack id must be professional-services")
        if "business-profile.json" not in pack.get("requiredPlanningArtifacts", []):
            errors.append("business-profile.json must be required")
        if len(json.loads((PACK / "page-blueprints.json").read_text())["blueprints"]) < 6:
            errors.append("professional-services pack needs at least 6 blueprints")
        if len(json.loads((PACK / "component-manifest.json").read_text())["components"]) < 8:
            errors.append("professional-services pack needs at least 8 components")
        if not pack.get("rejectConditions"):
            errors.append("rejectConditions must not be empty")
    if errors:
        print("PROFESSIONAL SERVICES PACK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PROFESSIONAL SERVICES PACK: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
