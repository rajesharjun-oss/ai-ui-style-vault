#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

REQUIRED_TOP = [
    "status","officialName","businessCategory","offers","audiences","primaryConversion",
    "evidenceSources","brandSignals","operationalFacts","researchGaps","confidence"
]

def validate(profile: dict) -> list[str]:
    errors = []
    for key in REQUIRED_TOP:
        if key not in profile:
            errors.append(f"missing required field: {key}")
    if errors:
        return errors
    if profile["status"] not in {"ready","blocked","needs-owner-confirmation"}:
        errors.append("status must be ready, blocked, or needs-owner-confirmation")
    if not str(profile["officialName"]).strip():
        errors.append("officialName is empty")
    if not str(profile["businessCategory"]).strip():
        errors.append("businessCategory is empty")
    if not profile["offers"]:
        errors.append("at least one offer is required")
    if not profile["audiences"]:
        errors.append("at least one audience is required")
    conversion = profile["primaryConversion"]
    if not conversion.get("action") or not conversion.get("channel"):
        errors.append("primaryConversion action and channel are required")
    usable_sources = [s for s in profile["evidenceSources"] if s.get("accessStatus") in {"inspected","user-supplied","partial"}]
    if not usable_sources:
        errors.append("at least one usable evidence source is required")
    signals = profile["brandSignals"]
    for key in ("positioning","visualSignals","tone"):
        if not signals.get(key):
            errors.append(f"brandSignals.{key} must not be empty")
    score = profile["confidence"].get("score", -1)
    if not isinstance(score, int) or not 0 <= score <= 100:
        errors.append("confidence.score must be an integer from 0 to 100")
    allowed = profile.get("designSelectionAllowed", profile["status"] == "ready")
    if profile["status"] == "ready":
        if score < 70:
            errors.append("ready profiles require confidence.score >= 70")
        if not allowed:
            errors.append("ready profile must set designSelectionAllowed=true")
    else:
        if allowed:
            errors.append("non-ready profile must not allow design selection")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Vault business-understanding research gate.")
    parser.add_argument("profile", help="Path to business-profile.json")
    args = parser.parse_args()
    path = Path(args.profile)
    profile = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(profile)
    if errors:
        print("BUSINESS UNDERSTANDING: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"BUSINESS UNDERSTANDING: PASS ({profile['status']}, confidence={profile['confidence']['score']})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
