#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

DOMAIN_RULES = [
    ("fashion-couture", {"fashion","couture","tailor","tailoring","atelier","corporate wear","suit","kaftan","traditional wear","occasion wear","made to order","made-to-order","fabric"}),
    ("beauty-wellness", {"beauty","salon","spa","barber","barbershop","wellness","skincare","skin clinic","aesthetic clinic","nail studio","massage","makeup studio","grooming"}),
    ("hospitality", {"hotel","resort","serviced apartment","guest house","guesthouse","lodge","accommodation","hospitality","rooms","room booking","stay"}),
    ("saas-technology", {"saas","software","technology","tech platform","ai product","ai platform","developer tool","api","workflow software","automation platform","cloud software","b2b software"}),
    ("professional-services", {"accounting","audit","tax","law firm","legal","consulting","consultancy","advisory","assurance","architecture","engineering consulting","professional services"}),
    ("real-estate", {"real estate","property","property developer","developer","estate agency","brokerage","residential","commercial property","apartments","land sales","office space"}),
    ("fast-casual-commerce", {"restaurant","cafe","bakery","food","pizza","takeaway","delivery","menu","quick service","fast casual"}),
    ("celebration-event-microsite", {"wedding","nikkah","engagement","anniversary","save the date","rsvp","celebration"}),
]

def text_blob(profile: dict) -> str:
    parts = [profile.get("businessCategory", ""), *profile.get("subcategories", []), *profile.get("audiences", [])]
    parts.extend(o.get("name", "") for o in profile.get("offers", []))
    return " ".join(str(p).lower() for p in parts)

def choose_domain(profile: dict) -> str | None:
    explicit = profile.get("recommendedDomainPack")
    if explicit:
        return explicit
    blob = text_blob(profile)
    scored = []
    for pack, terms in DOMAIN_RULES:
        score = sum(1 for term in terms if term in blob)
        scored.append((score, pack))
    scored.sort(reverse=True)
    return scored[0][1] if scored and scored[0][0] else None

def main() -> int:
    parser = argparse.ArgumentParser(description="Plan a Vault build from a validated business profile.")
    parser.add_argument("profile", help="Path to business-profile.json")
    parser.add_argument("--3d", dest="use_3d", action="store_true", help="Add 3D & Immersive Web capability")
    parser.add_argument("--asset-readiness", choices=["strong","adequate","limited","none"], default="limited")
    args = parser.parse_args()
    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    if profile.get("status") != "ready" or not profile.get("designSelectionAllowed"):
        print(json.dumps({"status":"blocked","reason":"Business research gate is not ready. Design selection is prohibited."}, indent=2))
        return 2
    domain = choose_domain(profile)
    profile_ref = str(Path(args.profile))
    theme_command = f"python scripts/score-design-selection.py {profile_ref} --domain-pack {domain} --asset-readiness {args.asset_readiness}" if domain else None
    section_command = f"python scripts/select-section-recipes.py {profile_ref} --domain-pack {domain} --section hero --section proof --section services --section cta --section footer" if domain else None
    plan = {
        "status": "ready",
        "business": profile.get("officialName"),
        "businessCategory": profile.get("businessCategory"),
        "primaryConversion": profile.get("primaryConversion"),
        "domainPack": domain,
        "capabilityPacks": ["3d-immersive-web"] if args.use_3d else [],
        "requiredPrompts": ["prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md"] + (["prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md"] if args.use_3d else []) + ["prompts/VISUAL_QA_AND_REVISION.md"],
        "researchGaps": profile.get("researchGaps", []),
        "designSelection": {
            "method": "scored, evidence-based selection; aesthetic preference alone is not sufficient",
            "themeScoringCommand": theme_command,
            "sectionRecipeCommand": section_command,
            "recordIn": ["VAULT_SELECTION.md", "design-recipe.json"]
        },
        "visualQualityGate": {
            "observationsTemplate": "quality/VISUAL_QA_OBSERVATIONS.template.json",
            "command": "python scripts/validate-anti-generic-visual.py <site-root> <VISUAL_QA_OBSERVATIONS.json> --json-out <visual-qa-score.json>",
            "minimumScore": 75
        },
        "next": [
            "read selected pack requiredReads",
            "create pack-specific build contract",
            "plan assets and establish asset readiness",
            "run scored production-theme selection",
            "select section recipes by purpose instead of repeating one layout",
            "record selection evidence in VAULT_SELECTION.md and design-recipe.json",
            "implement only after contracts are complete",
            "render desktop and mobile",
            "complete structured visual QA observations",
            "pass the anti-generic visual QA gate before handoff"
        ]
    }
    print(json.dumps(plan, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
