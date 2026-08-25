#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run(script, args):
    return subprocess.run([sys.executable, str(SCRIPTS / script), *args], cwd=ROOT).returncode


def main():
    p = argparse.ArgumentParser(description="Compact front door for AI agents using the AI UI Style Vault.")
    sub = p.add_subparsers(dest="command", required=True)

    ingest = sub.add_parser("ingest", help="Ingest a business source URL or evidence report into strict source-of-truth artifacts.")
    ingest.add_argument("source")
    ingest.add_argument("--output-dir", default="business-ingestion")
    ingest.add_argument("--json", action="store_true")

    model = sub.add_parser("model", help="Generate evidence-backed public content and admin/CMS entity models from an ingestion bundle.")
    model.add_argument("source", help="BUSINESS_SOURCE_REPORT.json or ingestion directory")
    model.add_argument("--output-dir")
    model.add_argument("--json", action="store_true")

    plan = sub.add_parser("plan", help="Create a complete vault build plan from a validated business profile.")
    plan.add_argument("profile")
    plan.add_argument("--output", default="vault-build-plan.json")
    plan.add_argument("--asset-readiness", choices=["strong", "adequate", "limited", "none"], default="limited")
    plan.add_argument("--performance-priority", choices=["normal", "high"], default="normal")
    plan.add_argument("--density", choices=["sparse", "balanced", "informational", "data-dense"], default="balanced")
    plan.add_argument("--3d", dest="use_3d", action="store_true")
    plan.add_argument("--3d-subject-class")
    plan.add_argument("--3d-goal")

    component = sub.add_parser("component", help="Resolve a component need to its canonical semantic contract.")
    component.add_argument("need")
    component.add_argument("--compact", action="store_true")

    effect = sub.add_parser("effect", help="Select a semantically justified interactive effect for a page section, or deliberately return none.")
    effect.add_argument("profile")
    effect.add_argument("--section", default="hero")
    effect.add_argument("--performance-priority", choices=["normal", "high"], default="normal")
    effect.add_argument("--asset-readiness", choices=["strong", "adequate", "limited", "none"], default="limited")

    effect_skill = sub.add_parser("effect-skill", help="Generate a Skill.md implementation contract for one selected interactive effect.")
    effect_skill.add_argument("effect_id")
    effect_skill.add_argument("--output")

    effect_qa = sub.add_parser("effect-qa", help="Grade measured effect performance/accessibility observations.")
    effect_qa.add_argument("effect_id")
    effect_qa.add_argument("observations")
    effect_qa.add_argument("--json-out")

    immersive = sub.add_parser("immersive", help="Select an immersive website architecture from a validated business profile and user goal, or return none.")
    immersive.add_argument("profile")
    immersive.add_argument("--goal", required=True)
    immersive.add_argument("--level", type=int, choices=[1, 2, 3, 4])
    immersive.add_argument("--performance-priority", choices=["normal", "high"], default="normal")
    immersive.add_argument("--asset-readiness", choices=["strong", "adequate", "limited", "none"], default="limited")

    immersive_skill = sub.add_parser("immersive-skill", help="Generate a Skill.md implementation contract for one selected immersive template.")
    immersive_skill.add_argument("template_id")
    immersive_skill.add_argument("--output")

    mode = sub.add_parser("3d-mode", help="Classify an already-justified 3D request into an explicit interaction mode before production/runtime selection.")
    mode.add_argument("need")
    mode.add_argument("--subject-class")
    mode.add_argument("--asset-format", choices=["glb", "gltf", "other", "none"], default="none")
    mode.add_argument("--asset-readiness", choices=["strong", "adequate", "limited", "none"], default="none")

    asset_qa = sub.add_parser("3d-asset-qa", help="Grade 3D asset fidelity/reference/technical observations before delivery or publish handoff.")
    asset_qa.add_argument("observations")

    resource = sub.add_parser("3d-resource", help="Select a 3D production-resource category for a defined asset/production need.")
    resource.add_argument("need")
    resource.add_argument("--domain")
    resource.add_argument("--max", dest="max_items", type=int, choices=range(1, 9))

    resource_skill = sub.add_parser("3d-resource-skill", help="Generate a Skill.md production contract for one selected 3D production-resource category.")
    resource_skill.add_argument("category_id")
    resource_skill.add_argument("--output")

    runtime = sub.add_parser("3d-runtime", help="Select the smallest sufficient 3D browser-delivery profile after mandatory 3D mode classification.")
    runtime.add_argument("need")
    runtime.add_argument("--mode", required=True, choices=[
        "none", "visual-only", "authored-animation", "inspectable-object",
        "configurable-object", "spatial-exploration", "interactive-world"
    ])
    runtime.add_argument("--format", choices=["glb", "gltf", "other"])
    runtime.add_argument("--ar", action="store_true")

    runtime_skill = sub.add_parser("3d-runtime-skill", help="Generate a Skill.md implementation contract for one selected 3D delivery-runtime profile.")
    runtime_skill.add_argument("profile_id")
    runtime_skill.add_argument("--output")

    studio = sub.add_parser("studio-index", help="Build the compact metadata index for the future Vault Studio browser.")
    studio.add_argument("--output", default="studio/catalog-index.json")

    critic = sub.add_parser("critic", help="Run the Design Critic against a rendered-review observation file.")
    critic.add_argument("plan")
    critic.add_argument("observations")
    critic.add_argument("--benchmark-id")
    critic.add_argument("--json-out", default="design-critic-result.json")

    args = p.parse_args()

    if args.command == "ingest":
        forwarded = [args.source, "--output-dir", args.output_dir]
        if args.json:
            forwarded.append("--json")
        return run("ingest-business-source.py", forwarded)

    if args.command == "model":
        forwarded = [args.source]
        if args.output_dir:
            forwarded += ["--output-dir", args.output_dir]
        if args.json:
            forwarded.append("--json")
        return run("generate-business-content-model.py", forwarded)

    if args.command == "plan":
        forwarded = [
            args.profile, "--output", args.output, "--asset-readiness", args.asset_readiness,
            "--performance-priority", args.performance_priority, "--density", args.density
        ]
        if args.use_3d:
            forwarded.append("--3d")
        if args.__dict__.get("3d_subject_class"):
            forwarded += ["--3d-subject-class", args.__dict__["3d_subject_class"]]
        if args.__dict__.get("3d_goal"):
            forwarded += ["--3d-goal", args.__dict__["3d_goal"]]
        return run("vault-build-orchestrator.py", forwarded)

    if args.command == "component":
        forwarded = [args.need]
        if args.compact:
            forwarded.append("--compact")
        return run("resolve-component-contract.py", forwarded)

    if args.command == "effect":
        return run("interactive-effects.py", [
            "select", args.profile, "--section", args.section,
            "--performance-priority", args.performance_priority,
            "--asset-readiness", args.asset_readiness
        ])

    if args.command == "effect-skill":
        forwarded = ["skill", args.effect_id]
        if args.output:
            forwarded += ["--output", args.output]
        return run("interactive-effects.py", forwarded)

    if args.command == "effect-qa":
        forwarded = ["qa", args.effect_id, args.observations]
        if args.json_out:
            forwarded += ["--json-out", args.json_out]
        return run("interactive-effects.py", forwarded)

    if args.command == "immersive":
        forwarded = [
            "select", args.profile, "--goal", args.goal,
            "--performance-priority", args.performance_priority,
            "--asset-readiness", args.asset_readiness
        ]
        if args.level:
            forwarded += ["--level", str(args.level)]
        return run("immersive-templates.py", forwarded)

    if args.command == "immersive-skill":
        forwarded = ["skill", args.template_id]
        if args.output:
            forwarded += ["--output", args.output]
        return run("immersive-templates.py", forwarded)

    if args.command == "3d-mode":
        forwarded = [
            "classify", args.need,
            "--asset-format", args.asset_format,
            "--asset-readiness", args.asset_readiness
        ]
        if args.subject_class:
            forwarded += ["--subject-class", args.subject_class]
        return run("classify-3d-mode.py", forwarded)

    if args.command == "3d-asset-qa":
        return run("3d-asset-quality.py", [args.observations])

    if args.command == "3d-resource":
        forwarded = ["select", args.need]
        if args.domain:
            forwarded += ["--domain", args.domain]
        if args.max_items:
            forwarded += ["--max", str(args.max_items)]
        return run("3d-production-resources.py", forwarded)

    if args.command == "3d-resource-skill":
        forwarded = ["skill", args.category_id]
        if args.output:
            forwarded += ["--output", args.output]
        return run("3d-production-resources.py", forwarded)

    if args.command == "3d-runtime":
        forwarded = ["select", args.need, "--mode", args.mode]
        if args.format:
            forwarded += ["--format", args.format]
        if args.ar:
            forwarded.append("--ar")
        return run("3d-delivery-runtimes.py", forwarded)

    if args.command == "3d-runtime-skill":
        forwarded = ["skill", args.profile_id]
        if args.output:
            forwarded += ["--output", args.output]
        return run("3d-delivery-runtimes.py", forwarded)

    if args.command == "studio-index":
        return run("build-vault-studio-index.py", ["--output", args.output])

    if args.command == "critic":
        forwarded = [args.plan, args.observations, "--json-out", args.json_out]
        if args.benchmark_id:
            forwarded += ["--benchmark-id", args.benchmark_id]
        return run("run-design-critic.py", forwarded)

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
