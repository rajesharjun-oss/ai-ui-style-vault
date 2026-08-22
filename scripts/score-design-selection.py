#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES = ROOT / "system/production-theme-archetypes.json"
MODEL = ROOT / "system/design-selection-scoring.json"


def normalize(value):
    return str(value or "").strip().lower()


def contains_any(text, values):
    text = normalize(text)
    return any(normalize(v) in text or text in normalize(v) for v in values if v)


def infer_conversion(action):
    action = normalize(action)
    mapping = [
        ("book", ["book", "appointment", "reservation"]),
        ("enquire", ["enquire", "inquire", "quote", "consultation", "whatsapp"]),
        ("buy", ["buy", "purchase", "shop"]),
        ("order", ["order"]),
        ("trial", ["trial", "start free"]),
        ("signup", ["sign up", "signup", "register"]),
        ("demo", ["demo"]),
        ("viewing", ["viewing", "tour", "inspection"]),
        ("contact", ["contact", "call", "email"]),
    ]
    for key, terms in mapping:
        if any(term in action for term in terms):
            return key
    return "contact"


def theme_score(theme, profile, domain_pack, model, asset_readiness, performance_priority):
    weights = model["weights"]
    score = 0.0
    breakdown = {}
    theme_id = theme["id"]

    preferred = model["domainAffinities"].get(domain_pack, [])
    if theme_id in preferred:
        rank = preferred.index(theme_id)
        domain_points = weights["domainFit"] * (1.0 if rank == 0 else 0.8 if rank == 1 else 0.65)
    else:
        domain_blob = " ".join(theme.get("bestFor", []))
        category_blob = " ".join([profile.get("businessCategory", ""), *profile.get("subcategories", [])])
        domain_points = weights["domainFit"] * (0.45 if contains_any(category_blob, theme.get("bestFor", [])) or contains_any(domain_blob, profile.get("subcategories", [])) else 0.2)
    breakdown["domainFit"] = round(domain_points, 2)
    score += domain_points

    conversion = infer_conversion(profile.get("primaryConversion", {}).get("action"))
    conversion_pref = model["conversionAffinities"].get(conversion, [])
    conversion_points = weights["conversionFit"] * (1.0 if theme_id in conversion_pref[:1] else 0.8 if theme_id in conversion_pref[1:2] else 0.6 if theme_id in conversion_pref else 0.35)
    breakdown["conversionFit"] = round(conversion_points, 2)
    score += conversion_points

    desired_tone = set(normalize(x) for x in profile.get("brandSignals", {}).get("tone", []))
    theme_tone = set(normalize(x) for x in theme.get("tone", []))
    overlap = len(desired_tone & theme_tone)
    tone_ratio = min(1.0, overlap / max(1, min(3, len(desired_tone)))) if desired_tone else 0.6
    tone_points = weights["toneFit"] * max(0.35, tone_ratio)
    breakdown["toneFit"] = round(tone_points, 2)
    score += tone_points

    requested_density = normalize(profile.get("contentDensity") or profile.get("preferredContentDensity") or "balanced")
    theme_density = normalize(theme.get("contentDensity"))
    density_points = weights["contentDensityFit"] * (1.0 if requested_density == theme_density else 0.65 if {requested_density, theme_density} <= {"balanced","informational"} else 0.45)
    breakdown["contentDensityFit"] = round(density_points, 2)
    score += density_points

    trust = normalize(profile.get("trustLevel") or "medium")
    trust_pref = model["trustAffinities"].get(trust, [])
    trust_points = weights["trustFit"] * (1.0 if theme_id in trust_pref else 0.55)
    breakdown["trustFit"] = round(trust_points, 2)
    score += trust_points

    asset_heavy = theme_id in model.get("assetRequirements", {})
    if asset_heavy:
        asset_factor = {"strong":1.0,"adequate":0.8,"limited":0.45,"none":0.2}.get(asset_readiness, 0.45)
    else:
        asset_factor = 0.9 if asset_readiness in {"limited","none"} else 1.0
    asset_points = weights["assetFit"] * asset_factor
    breakdown["assetFit"] = round(asset_points, 2)
    score += asset_points

    if performance_priority == "high" and theme.get("motionModel") in {"cinematic-media", "immersive-3d"}:
        perf_factor = 0.45
    else:
        perf_factor = 1.0
    perf_points = weights["performanceFit"] * perf_factor
    breakdown["performanceFit"] = round(perf_points, 2)
    score += perf_points

    return round(score, 2), breakdown, conversion


def main():
    parser = argparse.ArgumentParser(description="Score Vault production themes from a validated business profile.")
    parser.add_argument("profile")
    parser.add_argument("--domain-pack", required=True)
    parser.add_argument("--asset-readiness", choices=["strong","adequate","limited","none"], default="limited")
    parser.add_argument("--performance-priority", choices=["normal","high"], default="normal")
    parser.add_argument("--top", type=int, default=3)
    args = parser.parse_args()

    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    if profile.get("status") != "ready" or not profile.get("designSelectionAllowed"):
        print(json.dumps({"status":"blocked","reason":"Business research gate is not ready."}, indent=2))
        return 2

    model = json.loads(MODEL.read_text(encoding="utf-8"))
    themes = json.loads(THEMES.read_text(encoding="utf-8"))["themes"]
    results = []
    conversion = None
    for theme in themes:
        score, breakdown, conversion = theme_score(theme, profile, args.domain_pack, model, args.asset_readiness, args.performance_priority)
        results.append({"themeId":theme["id"],"themeName":theme["name"],"score":score,"breakdown":breakdown,"motionModel":theme.get("motionModel")})
    results.sort(key=lambda x: x["score"], reverse=True)
    top = results[:max(1,args.top)]
    winner = top[0]
    runner_up = top[1] if len(top) > 1 else None
    margin = round(winner["score"] - runner_up["score"], 2) if runner_up else winner["score"]
    status = "selected" if winner["score"] >= model["minimumPassingScore"] and margin >= model["minimumWinningMargin"] else "tie-or-review"
    print(json.dumps({"status":status,"domainPack":args.domain_pack,"conversionType":conversion,"minimumPassingScore":model["minimumPassingScore"],"minimumWinningMargin":model["minimumWinningMargin"],"winningMargin":margin,"results":top}, indent=2))
    return 0 if winner["score"] >= model["minimumPassingScore"] else 3

if __name__ == "__main__":
    raise SystemExit(main())
