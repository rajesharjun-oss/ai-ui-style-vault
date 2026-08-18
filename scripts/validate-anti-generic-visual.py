#!/usr/bin/env python3
import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES = json.loads((ROOT / "quality/anti-generic-visual-rules.json").read_text(encoding="utf-8"))


def collect_text(site_root: Path):
    html = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in site_root.rglob("*.html"))
    css = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in site_root.rglob("*.css"))
    js = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in site_root.rglob("*.js"))
    return html, css, js


def count_images(html):
    sources = re.findall(r'<img[^>]+src=["\']([^"\']+)', html, flags=re.I)
    counts = Counter(sources)
    return max(counts.values(), default=0)


def score(site_root: Path, observations: dict):
    html, css, js = collect_text(site_root)
    combined = (html + "\n" + css + "\n" + js).lower()
    penalties = []
    hard_fails = []
    points = 100
    pmap = RULES["penalties"]
    heur = RULES["sourceHeuristics"]

    generic_hits = [phrase for phrase in RULES["genericPhrases"] if phrase in combined]
    if generic_hits:
        amount = min(16, len(generic_hits) * pmap["genericMarketingPhrase"])
        points -= amount; penalties.append(("genericMarketingPhrase", amount, generic_hits))

    backdrop = len(re.findall(r'backdrop-filter\s*:', css, flags=re.I))
    if backdrop > heur["maxBackdropFilterDeclarations"]:
        points -= pmap["excessiveGlass"]; penalties.append(("excessiveGlass", pmap["excessiveGlass"], backdrop))

    gradients = len(re.findall(r'linear-gradient\s*\(', css, flags=re.I))
    purple_blue = len(re.findall(r'(purple|violet|indigo|#7c3aed|#6366f1|#8b5cf6|#4f46e5)', css, flags=re.I))
    if gradients > heur["maxLinearGradientDeclarations"] and purple_blue >= 3:
        points -= pmap["defaultPurpleBlueGradient"]; penalties.append(("defaultPurpleBlueGradient", pmap["defaultPurpleBlueGradient"], {"gradients":gradients,"purpleBlueSignals":purple_blue}))

    large_sizes = [float(x) for x in re.findall(r'font-size\s*:\s*([0-9.]+)px', css, flags=re.I)]
    if large_sizes and max(large_sizes) > heur["maxVeryLargeHeadingPx"]:
        points -= pmap["giantHeroType"]; penalties.append(("giantHeroType", pmap["giantHeroType"], max(large_sizes)))

    pill_count = len(re.findall(r'border-radius\s*:\s*(?:999|9999|10000)px', css, flags=re.I))
    if pill_count > heur["maxBorderRadiusPillDeclarations"]:
        points -= pmap["tooManyPills"]; penalties.append(("tooManyPills", pmap["tooManyPills"], pill_count))

    repeated_image = count_images(html)
    if repeated_image > heur["maxRepeatedImageSource"] or observations.get("sameImageRepeated"):
        points -= pmap["sameImageRepeated"]; penalties.append(("sameImageRepeated", pmap["sameImageRepeated"], repeated_image))

    if "prefers-reduced-motion" not in css.lower() and not observations.get("reducedMotionVerified"):
        points -= pmap["missingReducedMotion"]; penalties.append(("missingReducedMotion", pmap["missingReducedMotion"], True))

    negative_flags = [
        ("productHiddenBelowMarketing", "productHiddenBelowMarketing"),
        ("desktopOnlyComposition", "desktopOnlyComposition"),
        ("motionEverywhere", "motionEverywhere"),
        ("genericFeatureCardCopy", "genericFeatureCardCopy")
    ]
    for obs_key, penalty_key in negative_flags:
        if observations.get(obs_key):
            amount = pmap[penalty_key]; points -= amount; penalties.append((penalty_key, amount, True))

    required = RULES["requiredObservationFields"]
    missing_or_false = [key for key in required if observations.get(key) is not True]
    if missing_or_false:
        amount = min(30, len(missing_or_false) * 3)
        points -= amount; penalties.append(("incompleteVisualEvidence", amount, missing_or_false))

    if observations.get("noHorizontalOverflow") is not True:
        hard_fails.append("mobile horizontal overflow not cleared")
    if observations.get("mediaProvenanceVerified") is not True:
        hard_fails.append("media provenance not verified")
    if observations.get("primaryActionVisible") is not True:
        hard_fails.append("primary action visibility not verified")

    points = max(0, points)
    passed = points >= RULES["minimumPassingScore"] and not hard_fails
    return {"status":"pass" if passed else "fail","score":points,"minimumPassingScore":RULES["minimumPassingScore"],"hardFails":hard_fails,"penalties":[{"signal":a,"points":b,"evidence":c} for a,b,c in penalties],"sourceMetrics":{"backdropFilterDeclarations":backdrop,"linearGradients":gradients,"purpleBlueSignals":purple_blue,"maxHeadingPx":max(large_sizes, default=0),"pillDeclarations":pill_count,"maxRepeatedImageCount":repeated_image}}


def main():
    p = argparse.ArgumentParser(description="Anti-generic visual QA gate combining source heuristics with structured rendered-review evidence.")
    p.add_argument("site_root")
    p.add_argument("observations", help="Path to VISUAL_QA_OBSERVATIONS.json created after rendered desktop/mobile review")
    p.add_argument("--json-out")
    args = p.parse_args()
    site_root = Path(args.site_root)
    observations = json.loads(Path(args.observations).read_text(encoding="utf-8"))
    result = score(site_root, observations)
    rendered = json.dumps(result, indent=2)
    print(rendered)
    if args.json_out:
        Path(args.json_out).write_text(rendered + "\n", encoding="utf-8")
    return 0 if result["status"] == "pass" else 2

if __name__ == "__main__":
    raise SystemExit(main())
