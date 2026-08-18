#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

DOMAIN_RULES = [
    ("fashion-couture", {"fashion","couture","tailor","tailoring","atelier","corporate wear","suit","kaftan","traditional wear","occasion wear","made to order","made-to-order","fabric"}),
    ("real-estate", {"real estate","property","properties","developer","development","brokerage","estate agency","residential","commercial property","apartment","land","housing","office space","industrial property"}),
    ("professional-services", {"professional services","accounting","accountant","audit","auditing","tax","taxation","legal","law firm","lawyer","consulting","consultancy","advisory","engineering consulting","architecture firm","risk","assurance","strategy consulting"}),
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
    for priority, (pack, terms) in enumerate(DOMAIN_RULES):
        score = sum(1 for term in terms if term in blob)
        scored.append((score, -priority, pack))
    scored.sort(reverse=True)
    return scored[0][2] if scored and scored[0][0] else None

def main() -> int:
    parser = argparse.ArgumentParser(description="Plan a Vault build from a validated business profile.")
    parser.add_argument("profile", help="Path to business-profile.json")
    parser.add_argument("--3d", dest="use_3d", action="store_true", help="Add 3D & Immersive Web capability")
    args = parser.parse_args()
    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    if profile.get("status") != "ready" or not profile.get("designSelectionAllowed"):
        print(json.dumps({"status":"blocked","reason":"Business research gate is not ready. Design selection is prohibited."}, indent=2))
        return 2
    domain = choose_domain(profile)
    plan = {
        "status": "ready",
        "business": profile.get("officialName"),
        "businessCategory": profile.get("businessCategory"),
        "primaryConversion": profile.get("primaryConversion"),
        "domainPack": domain,
        "capabilityPacks": ["3d-immersive-web"] if args.use_3d else [],
        "requiredPrompts": ["prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md"] + (["prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md"] if args.use_3d else []) + ["prompts/VISUAL_QA_AND_REVISION.md"],
        "researchGaps": profile.get("researchGaps", []),
        "next": ["read selected pack requiredReads","create pack-specific build contract","plan assets","shortlist vault recipes","implement only after contracts are complete"]
    }
    print(json.dumps(plan, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
