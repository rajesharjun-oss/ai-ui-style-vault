#!/usr/bin/env python3
"""Initialize a target repository with the vault's mandatory planning artifacts."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Sequence

BUILD_TYPES = [
    "marketing-website", "professional-services-website", "saas-web-app",
    "internal-tool", "dashboard", "ai-workspace", "ecommerce",
    "mobile-style-app", "other",
]
DENSITIES = ["sparse", "balanced", "informational", "data-dense"]


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(description="Create the mandatory AI UI Style Vault project contract files.")
    value.add_argument("target", type=Path)
    value.add_argument("--product", required=True)
    value.add_argument("--build-type", choices=BUILD_TYPES, required=True)
    value.add_argument("--primary-user", action="append", required=True)
    value.add_argument("--top-task", action="append", required=True)
    value.add_argument("--domain", default="")
    value.add_argument("--content-density", choices=DENSITIES, default="balanced")
    value.add_argument("--force", action="store_true")
    return value


def copy_file(source: Path, destination: Path, force: bool) -> str:
    if destination.exists() and not force:
        return f"SKIP {destination.name} (already exists)"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return f"WRITE {destination.name}"


def recipe(args: argparse.Namespace) -> dict:
    is_app = args.build_type in {"saas-web-app", "internal-tool", "dashboard", "ai-workspace", "mobile-style-app"}
    required_states = ["loading", "empty", "error", "success", "disabled", "permission-denied"] if is_app else ["default", "mobile", "reduced-motion"]
    primary_action = args.top_task[0]
    return {
        "schemaVersion": "1.0.0",
        "product": {
            "name": args.product,
            "type": args.build_type,
            "domain": args.domain,
            "primaryUsers": args.primary_user,
            "secondaryUsers": [],
            "topTasks": args.top_task,
            "primaryOutcome": f"Enable {args.primary_user[0]} to {primary_action.lower()} with clarity and confidence.",
            "trustLevel": "high",
            "riskLevel": "medium",
            "successSignals": [],
        },
        "experience": {
            "primaryJourney": ["enter", primary_action, "confirm outcome"],
            "pages": [{
                "id": "primary-page",
                "purpose": f"Help {args.primary_user[0]} {primary_action.lower()}.",
                "audience": args.primary_user,
                "primaryAction": primary_action,
                "secondaryActions": [],
                "blueprint": "TO SELECT",
                "requiredInformation": [],
                "deferredInformation": [],
                "requiredStates": required_states,
            }],
        },
        "content": {
            "density": args.content_density,
            "tone": ["clear", "specific", "professional"],
            "readingStyle": "plain-business",
            "progressiveDisclosure": True,
            "preferVisualExplanation": True,
            "copyBudgets": {"heroHeadlineWordsMax": 12, "heroSupportWordsMax": 35, "featureDescriptionWordsMax": 45, "paragraphWordsMax": 70, "majorSectionsMax": 8},
            "messageHierarchy": [],
            "prohibitedPatterns": ["generic AI marketing language", "repeated benefits", "paragraph-heavy cards"],
            "industryTerminology": [],
        },
        "visualDirection": {
            "productionTheme": "TO SELECT",
            "primaryStyle": {"name": "TO SELECT", "path": "TO SELECT"},
            "supportingReferences": [],
            "tone": ["professional", "deliberate"],
            "colorMode": "light",
            "radiusAttitude": "restrained",
            "surfaceAttitude": "TO COMPLETE",
            "typographyAttitude": "TO COMPLETE",
            "originalityStatement": "Create an original interface using reference principles only; do not copy protected assets, exact text, layouts, or animation sequences.",
        },
        "layout": {
            "navigation": "TO COMPLETE",
            "interfaceDensity": "medium",
            "contentWidth": "standard",
            "responsiveStrategy": ["Define desktop, laptop, and mobile transformations before implementation."],
            "tableMobileStrategy": "TO COMPLETE",
            "firstViewportGoal": "Show the product outcome and primary action without paragraph-heavy copy.",
        },
        "components": {
            "required": ["button", "navigation-shell"],
            "requiredStates": required_states,
            "reusePolicy": "Use shared semantic components and do not duplicate the same behavior with inconsistent styling.",
            "dataPatterns": [],
            "formPatterns": [],
        },
        "motion": {
            "model": "quiet-premium",
            "intensity": "subtle",
            "primitives": ["button-press"],
            "primaryTool": "CSS transitions unless the product requires more",
            "assetSources": [],
            "reducedMotionPlan": "Remove nonessential spatial movement and show final states immediately while preserving all content and feedback.",
        },
        "accessibility": {"target": "WCAG-2.2-AA", "keyboard": True, "focusVisible": True, "contrast": True, "zoom": True, "screenReader": True, "motionSensitivity": True, "notes": []},
        "performance": {"mobileFirstPaintPriority": True, "lazyLoadOffscreenMedia": True, "avoidLayoutAnimation": True, "bundleDiscipline": "Use the smallest libraries necessary and avoid heavy motion dependencies for simple transitions.", "budgets": {}},
        "assetPolicy": {"allowed": ["user-provided assets", "original local assets", "generated assets", "clearly licensed media"], "prohibited": ["copied target-site media", "protected logos", "exact reference layouts", "premium prompt text"], "licenseNotesRequired": True},
        "quality": {"requiredViewports": ["1440x1000", "1280x800", "390x844"], "requiredCommands": ["lint", "typecheck", "tests", "build", "content/design validator"], "requiredEvidence": ["completed planning artifacts", "desktop and mobile review", "state coverage review", "asset audit"], "rejectConditions": ["paragraph-heavy first viewport", "generic AI copy", "missing critical states", "obvious responsive overlap"]},
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    target = args.target.resolve()
    target.mkdir(parents=True, exist_ok=True)
    vault_root = Path(__file__).resolve().parents[1]

    outputs = []
    for source_name, destination_name in [
        ("templates/VAULT_SELECTION.md", "VAULT_SELECTION.md"),
        ("templates/BUILD_CONTRACT.md", "BUILD_CONTRACT.md"),
        ("templates/CONTENT_PLAN.md", "CONTENT_PLAN.md"),
        ("prompts/SENIOR_PRODUCT_TEAM_PROMPT.md", "AI_IMPLEMENTATION_INSTRUCTIONS.md"),
    ]:
        outputs.append(copy_file(vault_root / source_name, target / destination_name, args.force))

    recipe_path = target / "design-recipe.json"
    if recipe_path.exists() and not args.force:
        outputs.append("SKIP design-recipe.json (already exists)")
    else:
        recipe_path.write_text(json.dumps(recipe(args), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        outputs.append("WRITE design-recipe.json")

    for output in outputs:
        print(output)
    print("NEXT: Replace all TO SELECT / TO COMPLETE values, choose vault references, and finish the three Markdown contracts before coding.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
