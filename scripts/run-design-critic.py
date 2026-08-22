#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = json.loads((ROOT / "references/component-gallery/contract-rules.json").read_text(encoding="utf-8"))


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def norm(v):
    return str(v or "").strip().lower()


def evaluate(plan, observations, benchmark=None):
    score = 100
    findings = []
    hard_fails = []

    def penalize(code, points, evidence, severity="important"):
        nonlocal score
        score -= points
        findings.append({"code": code, "severity": severity, "points": points, "evidence": evidence})

    for key, points in [
        ("businessSpecificity", 12),
        ("primaryTaskVisible", 12),
        ("primaryConversionVerified", 15),
        ("selectedThemePreserved", 6),
    ]:
        if observations.get(key) is not True:
            penalize(key, points, "Rendered review did not verify this requirement.")

    if observations.get("sectionRecipeDrift"):
        penalize("sectionRecipeDrift", 8, "Implementation drifted from the selected section composition contract.")
    if observations.get("genericCardSubstitution"):
        penalize("genericCardSubstitution", 10, "Purpose-specific composition was replaced by generic cards.")

    mobile = observations.get("mobile", {})
    if mobile.get("intentionalTransformation") is not True:
        penalize("mobileNotTransformed", 8, "Mobile appears merely stacked/shrunk.")
    if mobile.get("noHorizontalOverflow") is not True:
        hard_fails.append("mobile horizontal overflow not cleared")
    if mobile.get("criticalControlsReachable") is not True:
        hard_fails.append("critical mobile controls not verified reachable")

    content = observations.get("content", {})
    unsupported = content.get("unsupportedClaims", [])
    if unsupported:
        hard_fails.append("unsupported business/product claims remain")
        penalize("unsupportedClaims", min(20, len(unsupported) * 5), unsupported, "blocker")
    if content.get("duplicatedMessages"):
        penalize("duplicatedMessages", 5, True)
    if content.get("genericMarketingLanguage"):
        penalize("genericMarketingLanguage", 6, True)

    assets = observations.get("assets", {})
    if assets.get("provenanceVerified") is not True:
        hard_fails.append("asset provenance not verified")
    if assets.get("irrelevantPrimaryMedia"):
        hard_fails.append("primary media is irrelevant to the business/task")
    if assets.get("generatedMediaPresentedAsOfficial"):
        hard_fails.append("generated media is presented as official/real evidence")

    component_obs = {norm(x.get("id")): x for x in observations.get("componentContracts", []) if x.get("id")}
    required_components = []
    forbidden = []
    critical_states = []
    if benchmark:
        required_components = benchmark.get("requiredComponents", [])
        forbidden = benchmark.get("forbiddenSubstitutions", [])
        critical_states = benchmark.get("criticalStates", [])

    for cid in required_components:
        obs = component_obs.get(norm(cid))
        if not obs:
            penalize("missingComponentEvidence", 5, cid)
            continue
        if obs.get("semanticMatch") is not True:
            penalize("componentSemanticMismatch", 10, cid, "blocker")
            hard_fails.append(f"component semantic mismatch: {cid}")
        if obs.get("keyboardVerified") is not True and CONTRACTS["componentArchetypes"].get(cid) not in {"content", "layout", "media"}:
            penalize("keyboardContractUnverified", 4, cid)
        if obs.get("responsiveVerified") is not True:
            penalize("responsiveContractUnverified", 3, cid)

    implemented_substitutions = {norm(x) for x in observations.get("forbiddenSubstitutionsObserved", [])}
    for item in forbidden:
        if norm(item) in implemented_substitutions:
            hard_fails.append(f"forbidden substitution used: {item}")
            penalize("forbiddenComponentSubstitution", 12, item, "blocker")

    observed_states = {norm(x) for x in observations.get("verifiedStates", [])}
    for state in critical_states:
        if norm(state) not in observed_states:
            penalize("criticalStateMissing", 4, state)

    three_d_plan = plan.get("threeD", {}) if isinstance(plan, dict) else {}
    three_d_obs = observations.get("threeD", {})
    if three_d_obs.get("used"):
        if three_d_plan.get("status") not in {"ready", "review-required"}:
            hard_fails.append("3D used without an approved subject-aware plan")
        if three_d_obs.get("subjectClassVerified") is not True:
            hard_fails.append("3D subject class not verified")
        if three_d_obs.get("goalVerified") is not True:
            hard_fails.append("3D user goal not verified")
        if three_d_obs.get("interactionPlanFollowed") is not True:
            penalize("threeDInteractionDrift", 12, True, "blocker")
        if three_d_obs.get("staticFallbackVerified") is not True:
            hard_fails.append("3D static fallback not verified")
        if three_d_obs.get("unrelatedSpectacle"):
            hard_fails.append("unrelated 3D spectacle detected")

    score = max(0, score)
    passed = score >= 80 and not hard_fails
    return {
        "status": "pass" if passed else "fail",
        "score": score,
        "minimumPassingScore": 80,
        "hardFails": hard_fails,
        "findings": findings,
        "benchmarkId": benchmark.get("id") if benchmark else None,
    }


def find_benchmark(path, benchmark_id):
    data = load(path)
    for item in data.get("benchmarks", []):
        if item.get("id") == benchmark_id:
            return item
    raise SystemExit(f"Unknown benchmark id: {benchmark_id}")


def main():
    p = argparse.ArgumentParser(description="Compare a rendered build against the Vault build plan, component contracts and optional benchmark expectations.")
    p.add_argument("plan", help="vault-build-plan.json")
    p.add_argument("observations", help="DESIGN_CRITIC_OBSERVATIONS.json created after rendered review")
    p.add_argument("--benchmark-suite", default=str(ROOT / "benchmarks/component-benchmarks.json"))
    p.add_argument("--benchmark-id")
    p.add_argument("--json-out")
    args = p.parse_args()

    plan = load(args.plan)
    observations = load(args.observations)
    benchmark = find_benchmark(args.benchmark_suite, args.benchmark_id) if args.benchmark_id else None
    result = evaluate(plan, observations, benchmark)
    rendered = json.dumps(result, indent=2)
    print(rendered)
    if args.json_out:
        Path(args.json_out).write_text(rendered + "\n", encoding="utf-8")
    return 0 if result["status"] == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
