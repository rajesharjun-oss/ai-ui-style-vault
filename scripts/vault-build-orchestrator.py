#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DEFAULT_SECTIONS = ["hero","proof","services","gallery","process","cta","footer"]


def run_json(script, args):
    cmd = [sys.executable, str(SCRIPTS / script), *args]
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    try:
        payload = json.loads(proc.stdout)
    except Exception:
        payload = {"status":"error","command":cmd,"stdout":proc.stdout,"stderr":proc.stderr,"returncode":proc.returncode}
    return proc.returncode, payload


def evidence_from_profile(profile):
    evidence = []
    evidence.extend(x.get("name", "") for x in profile.get("offers", []))
    evidence.extend(profile.get("brandSignals", {}).get("visualSignals", []))
    evidence.extend(profile.get("brandSignals", {}).get("positioning", []))
    evidence.extend(k for k,v in profile.get("operationalFacts", {}).items() if v not in (None,"",False))
    return [str(x) for x in evidence if str(x).strip()]


def main():
    p = argparse.ArgumentParser(description="Master AI UI Style Vault build orchestrator. Produces a deterministic planning bundle after the business research gate is ready.")
    p.add_argument("profile", help="Path to validated business-profile.json")
    p.add_argument("--asset-readiness", choices=["strong","adequate","limited","none"], default="limited")
    p.add_argument("--performance-priority", choices=["normal","high"], default="normal")
    p.add_argument("--density", choices=["sparse","balanced","informational","data-dense"], default="balanced")
    p.add_argument("--section", action="append", choices=["hero","proof","services","gallery","process","pricing","team","faq","cta","footer"])
    p.add_argument("--3d", dest="use_3d", action="store_true")
    p.add_argument("--3d-subject-class", choices=["assembled-product","vehicle","architecture-property","garment-textile","food-product","spatial-data","abstract-concept"])
    p.add_argument("--3d-goal")
    p.add_argument("--3d-interaction", action="append", default=[])
    p.add_argument("--output", default="vault-build-plan.json")
    args = p.parse_args()

    profile_path = Path(args.profile).resolve()
    profile = json.loads(profile_path.read_text(encoding="utf-8"))

    rc_validate, validation = run_json("validate-business-understanding.py", [str(profile_path), "--json"])
    if rc_validate != 0:
        blocked = {"status":"blocked","stage":"business-understanding","validation":validation}
        print(json.dumps(blocked, indent=2)); return 2

    planner_args = [str(profile_path)] + (["--3d"] if args.use_3d else [])
    rc_plan, base_plan = run_json("plan-vault-build.py", planner_args)
    if rc_plan != 0 or base_plan.get("status") != "ready":
        blocked = {"status":"blocked","stage":"domain-routing","basePlan":base_plan}
        print(json.dumps(blocked, indent=2)); return 3

    domain = base_plan.get("domainPack")
    if not domain:
        blocked = {"status":"blocked","stage":"domain-routing","reason":"No product-domain pack could be selected. Add evidence or an explicit recommendedDomainPack."}
        print(json.dumps(blocked, indent=2)); return 4

    rc_theme, theme_plan = run_json("score-design-selection.py", [str(profile_path), "--domain-pack", domain, "--asset-readiness", args.asset_readiness, "--performance-priority", args.performance_priority, "--top", "3"])
    if rc_theme != 0:
        blocked = {"status":"blocked","stage":"theme-selection","themePlan":theme_plan}
        print(json.dumps(blocked, indent=2)); return 5

    sections = args.section or DEFAULT_SECTIONS
    section_args = [str(profile_path), "--domain-pack", domain, "--density", args.density, "--top", "2"]
    for section in sections:
        section_args.extend(["--section", section])
    for item in evidence_from_profile(profile):
        section_args.extend(["--evidence", item])
    rc_sections, section_plan = run_json("select-section-recipes.py", section_args)
    if rc_sections != 0:
        blocked = {"status":"blocked","stage":"section-selection","sectionPlan":section_plan}
        print(json.dumps(blocked, indent=2)); return 6

    three_d_plan = {"status":"not-requested"}
    if args.use_3d:
        if not args.__dict__.get("3d_subject_class") or not args.__dict__.get("3d_goal"):
            three_d_plan = {
                "status":"blocked",
                "reason":"3D was requested, but subject class and goal were not supplied. The vault refuses generic 3D selection.",
                "required":["--3d-subject-class","--3d-goal"]
            }
        else:
            interaction_args = [str(profile_path), "--subject-class", args.__dict__["3d_subject_class"], "--goal", args.__dict__["3d_goal"]]
            for rid in args.__dict__.get("3d_interaction", []):
                interaction_args.extend(["--requested", rid])
            rc_3d, three_d_plan = run_json("select-3d-interaction-plan.py", interaction_args)
            if rc_3d != 0:
                three_d_plan["orchestratorStatus"] = "requires-review-before-implementation"

    hard_block = args.use_3d and three_d_plan.get("status") == "blocked"
    final = {
        "status":"blocked" if hard_block else "ready",
        "schemaVersion":"1.1.0",
        "business":{
            "name":profile.get("officialName"),
            "category":profile.get("businessCategory"),
            "primaryConversion":profile.get("primaryConversion"),
            "confidence":profile.get("confidence")
        },
        "researchGate":validation,
        "domain":base_plan,
        "assets":{"readiness":args.asset_readiness,"evidence":evidence_from_profile(profile),"researchGaps":profile.get("researchGaps",[])},
        "designIntelligence":{
            "themeSelection":theme_plan,
            "sectionSelection":section_plan,
            "density":args.density,
            "componentIntelligenceIndex":"references/component-intelligence-index.json",
            "componentContractResolver":"python scripts/resolve-component-contract.py \"<component or alias>\"",
            "selectionRule":"Use the winning theme only when it passes score/margin rules; use section recipes and component contracts as behavior/composition contracts, not copyable templates."
        },
        "threeD":three_d_plan,
        "requiredArtifacts":["BUSINESS_RESEARCH.md","business-profile.json","VAULT_SELECTION.md","BUILD_CONTRACT.md","CONTENT_PLAN.md","ASSET_PLAN.md","design-recipe.json","VISUAL_QA_OBSERVATIONS.json","DESIGN_CRITIC_OBSERVATIONS.json","VISUAL_QA_REPORT.md","design-critic-result.json"],
        "implementationOrder":["complete pack-specific contract","resolve owner-confirmation gaps that affect claims or conversion","resolve canonical component contracts for important interactions","materialize selected visual direction","implement semantic DOM/static fallback","implement sections and component states","add justified motion/3D only after static task works","render required viewports and states","run anti-generic visual QA gate","run Design Critic against plan and component contracts","revise until both gates pass","handoff with evidence"],
        "handoffGate":{"antiGenericMinimumScore":75,"designCriticMinimumScore":80,"mustHaveRenderedQA":True,"mustHaveVerifiedPrimaryCTA":True,"mustHaveMobileOverflowClearance":True,"mustPassComponentSemanticReview":True}
    }

    output = Path(args.output)
    if not output.is_absolute():
        output = Path.cwd() / output
    output.write_text(json.dumps(final, indent=2), encoding="utf-8")
    print(json.dumps({"status":final["status"],"output":str(output),"domainPack":domain,"themeStatus":theme_plan.get("status"),"threeDStatus":three_d_plan.get("status")}, indent=2))
    return 0 if final["status"] == "ready" else 7


if __name__ == "__main__":
    raise SystemExit(main())
