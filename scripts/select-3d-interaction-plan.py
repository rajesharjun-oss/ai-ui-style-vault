#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = ROOT / "3d/interaction-intent-system.json"
PATTERNS = ROOT / "packs/3d-immersive-web/interaction-patterns.json"


def norm(v):
    return str(v or "").strip().lower()


def get_subject(system, subject_class):
    for item in system["subjectClasses"]:
        if item["id"] == subject_class:
            return item
    return None


def business_blob(profile):
    parts = [profile.get("businessCategory", ""), *profile.get("subcategories", []), *profile.get("audiences", [])]
    parts.extend(x.get("name", "") for x in profile.get("offers", []))
    parts.extend(profile.get("brandSignals", {}).get("positioning", []))
    return norm(" ".join(str(x) for x in parts))


def subject_matches_business(subject, profile):
    signals = [norm(x) for x in subject.get("businessSignals", [])]
    if "any" in signals:
        return True, []
    blob = business_blob(profile)
    matched = [s for s in signals if s and s in blob]
    return bool(matched), matched


def main():
    p = argparse.ArgumentParser(description="Select a subject-aware 3D interaction plan. Never use interaction patterns as generic spectacle.")
    p.add_argument("profile", help="Validated business-profile.json")
    p.add_argument("--subject-class", required=True, choices=["assembled-product","vehicle","architecture-property","garment-textile","food-product","spatial-data","abstract-concept"])
    p.add_argument("--goal", required=True)
    p.add_argument("--requested", action="append", default=[], help="Requested interaction pattern id; may be repeated")
    p.add_argument("--max-patterns", type=int, default=4)
    args = p.parse_args()

    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    if profile.get("status") != "ready" or not profile.get("designSelectionAllowed"):
        print(json.dumps({"status":"blocked","reason":"Business research gate is not ready."}, indent=2))
        return 2

    system = json.loads(SYSTEM.read_text(encoding="utf-8"))
    subject = get_subject(system, args.subject_class)
    if not subject:
        print(json.dumps({"status":"blocked","reason":"Unknown subject class."}, indent=2))
        return 2

    relevant, matched_signals = subject_matches_business(subject, profile)
    if not relevant:
        print(json.dumps({
            "status":"blocked",
            "reason":f"3D subject class '{args.subject_class}' is not supported by the verified business profile.",
            "business":profile.get("officialName"),
            "businessCategory":profile.get("businessCategory"),
            "requiredBusinessSignals":subject.get("businessSignals", []),
            "rule":"The subject must be relevant before interaction style is considered."
        }, indent=2))
        return 3

    goal = norm(args.goal)
    valid_goals = [norm(x) for x in subject.get("validGoals", [])]
    if goal not in valid_goals:
        print(json.dumps({
            "status":"blocked",
            "reason":f"Goal '{args.goal}' is not valid for subject class '{args.subject_class}'.",
            "validGoals":subject.get("validGoals", []),
            "reject":subject.get("reject", [])
        }, indent=2))
        return 4

    catalog = {p["id"]: p for p in json.loads(PATTERNS.read_text(encoding="utf-8"))["patterns"]}
    allowed = list(subject.get("allowedInteractions", []))
    conditional = list(subject.get("conditionalInteractions", []))
    requested = args.requested or []
    rejected = []
    selected = []

    if requested:
        for rid in requested:
            if rid not in catalog:
                rejected.append({"id":rid,"reason":"Pattern does not exist in the canonical interaction catalog."})
            elif rid in allowed:
                selected.append(rid)
            elif rid in conditional:
                rejected.append({"id":rid,"reason":"Conditional interaction requires explicit verification of the subject structure/capability before use."})
            else:
                rejected.append({"id":rid,"reason":"Interaction is not semantically valid for this subject class and goal."})
    else:
        preference = {
            "inspect":["bounded-orbit-inspection","camera-preset-navigation","camera-look-at-focus","object-hotspots"],
            "explain-construction":["object-assembly","exploded-view","camera-look-at-focus","scroll-annotation-sync"],
            "configure":["material-switch","camera-preset-navigation","bounded-orbit-inspection","object-hotspots"],
            "compare":["camera-preset-navigation","material-switch","model-measurement","object-hotspots"],
            "story":["scroll-camera-path","camera-preset-navigation","timeline-scrub","scroll-annotation-sync"],
            "navigate-space":["guided-world-nodes","camera-preset-navigation","first-person-navigation","map-location-focus"],
            "explain-layout":["section-cut","camera-preset-navigation","model-measurement","object-hotspots"],
            "show-material":["material-switch","camera-look-at-focus","camera-preset-navigation"],
            "show-ingredients":["object-hotspots","camera-look-at-focus","camera-preset-navigation"],
            "show-process":["timeline-scrub","scroll-camera-path","camera-preset-navigation"],
            "explore-data":["data-driven-particles","map-location-focus","camera-preset-navigation"],
            "navigate":["map-location-focus","camera-preset-navigation","object-hotspots"],
            "monitor":["map-location-focus","data-driven-particles","object-hotspots"],
            "explain":["scroll-annotation-sync","camera-preset-navigation","scroll-camera-path"],
            "orient":["camera-preset-navigation","scroll-annotation-sync"]
        }.get(goal, [])
        selected = [x for x in preference if x in allowed][:max(1, args.max_patterns)]

    selected = selected[:max(1, args.max_patterns)]
    result = {
        "status":"ready" if selected and not rejected else "review-required" if selected else "blocked",
        "business":profile.get("officialName"),
        "businessRelevance":{"matched":True,"signals":matched_signals or ["any"]},
        "subjectClass":args.subject_class,
        "goal":args.goal,
        "selectedInteractions":[{"id":rid,"description":catalog[rid]["description"],"fallback":catalog[rid]["fallback"]} for rid in selected],
        "conditionalInteractions":conditional,
        "rejectedRequests":rejected,
        "cameraLanguage":subject.get("cameraLanguage", []),
        "requirements":subject.get("requirements", []),
        "reject":subject.get("reject", []),
        "hardRules":system["hardRules"],
        "implementationFamilies":system["implementationFamilies"]
    }
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "ready" else 5


if __name__ == "__main__":
    raise SystemExit(main())
