#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "3d" / "asset-quality-gate.json"


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def clamp_score(value):
    try:
        return max(0, min(5, float(value)))
    except Exception:
        return 0


def grade(obs):
    policy = load(POLICY)
    mode = obs.get("mode")
    target = obs.get("target", "publish")
    if mode not in policy["modePolicy"]:
        raise ValueError(f"unknown mode: {mode}")
    if target not in policy["qualityTargets"]:
        raise ValueError(f"unknown target: {target}")

    visual = obs.get("visual", {})
    technical = obs.get("technical", {})
    coverage = obs.get("referenceCoverage", {})
    target_policy = policy["qualityTargets"][target]

    failures = []
    warnings = []
    scores = {}
    for key in policy["visualCriteria"]:
        scores[key] = clamp_score(visual.get(key))
        if scores[key] < target_policy["minVisualScore"]:
            failures.append(f"{key} below {target} threshold ({scores[key]:.1f}/5)")

    hard_map = {
        "severePrimitiveProxy": visual.get("severePrimitiveProxy") is True,
        "detachedBodyOrGarmentParts": visual.get("detachedBodyOrGarmentParts") is True,
        "severeGarmentClipping": visual.get("severeGarmentClipping") is True,
        "misleadingUnverifiedBackOrSideDetails": visual.get("misleadingUnverifiedBackOrSideDetails") is True,
        "brokenNormalsOrGeometry": technical.get("normalsValid") is not True,
        "assetFailsToLoad": technical.get("loads") is not True,
        "missingNon3DFallback": technical.get("fallbackPresent") is not True,
    }
    for name, hit in hard_map.items():
        if hit:
            failures.append(name)

    for key in ("desktopMeasured", "mobileMeasured"):
        if technical.get(key) is not True:
            failures.append(key + " must be true")

    exact_real_product = obs.get("exactCommercialProductRepresentation") is True
    if target_policy["requiresCompleteReferenceCoverage"] and exact_real_product:
        required = policy["referenceCoverage"]["commercialInspectableProduct"]
        missing = [x for x in required if coverage.get(x) is not True]
        substitute = coverage.get("ownerApprovedAlternativeSource") is True
        if missing and not substitute:
            failures.append("missing reference coverage: " + ", ".join(missing))
            warnings.append("Keep the asset labelled as a concept/prototype until unseen geometry is verified.")

    # Polygon count can help diagnose suspiciously simple assets, but it never proves quality.
    diagnostics = obs.get("diagnostics", {})
    triangles = diagnostics.get("triangles")
    vertices = diagnostics.get("vertices")
    if isinstance(triangles, (int, float)) and triangles < 2000 and mode in {"inspectable-object", "configurable-object"}:
        warnings.append("Very low triangle count for an inspectable product; review for primitive-proxy geometry.")
    if isinstance(vertices, (int, float)) and vertices < 1000 and mode in {"inspectable-object", "configurable-object"}:
        warnings.append("Very low vertex count for an inspectable product; review for primitive-proxy geometry.")

    result = "pass" if not failures else "block"
    return {
        "status": "ready",
        "result": result,
        "mode": mode,
        "target": target,
        "visualScores": scores,
        "failures": failures,
        "warnings": warnings,
        "nextAction": (
            "Asset may proceed to runtime/browser QA and final handoff."
            if result == "pass" else
            "Preserve the selected 3D mode and route back to 3D asset production. Do not downgrade the requested interaction just because the current asset failed quality."
        )
    }


def main():
    p = argparse.ArgumentParser(description="Grade observed 3D asset quality before runtime handoff/publishing.")
    p.add_argument("observations", help="JSON observation file")
    args = p.parse_args()
    try:
        result = grade(load(args.observations))
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result["result"] == "pass" else 1
    except Exception as exc:
        print(json.dumps({"status": "error", "reason": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
