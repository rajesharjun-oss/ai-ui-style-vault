#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run(script, args):
    cmd = [sys.executable, str(SCRIPTS / script), *args]
    return subprocess.run(cmd, cwd=ROOT).returncode


def main():
    p = argparse.ArgumentParser(description="Compact front door for AI agents using the AI UI Style Vault.")
    sub = p.add_subparsers(dest="command", required=True)

    plan = sub.add_parser("plan", help="Create a complete vault build plan from a validated business profile.")
    plan.add_argument("profile")
    plan.add_argument("--output", default="vault-build-plan.json")
    plan.add_argument("--asset-readiness", choices=["strong","adequate","limited","none"], default="limited")
    plan.add_argument("--performance-priority", choices=["normal","high"], default="normal")
    plan.add_argument("--density", choices=["sparse","balanced","informational","data-dense"], default="balanced")
    plan.add_argument("--3d", dest="use_3d", action="store_true")
    plan.add_argument("--3d-subject-class")
    plan.add_argument("--3d-goal")

    component = sub.add_parser("component", help="Resolve a component need to its canonical semantic contract.")
    component.add_argument("need")
    component.add_argument("--compact", action="store_true")

    critic = sub.add_parser("critic", help="Run the Design Critic against a rendered-review observation file.")
    critic.add_argument("plan")
    critic.add_argument("observations")
    critic.add_argument("--benchmark-id")
    critic.add_argument("--json-out", default="design-critic-result.json")

    args = p.parse_args()

    if args.command == "plan":
        forwarded = [args.profile, "--output", args.output, "--asset-readiness", args.asset_readiness,
                     "--performance-priority", args.performance_priority, "--density", args.density]
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

    if args.command == "critic":
        forwarded = [args.plan, args.observations, "--json-out", args.json_out]
        if args.benchmark_id:
            forwarded += ["--benchmark-id", args.benchmark_id]
        return run("run-design-critic.py", forwarded)

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
