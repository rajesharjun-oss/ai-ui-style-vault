#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = ROOT / "packs/3d-immersive-web/design-combination-system.json"
DOMAIN_MAP = ROOT / "3d/subject-domain-map.json"


def norm(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", value.lower()))


def words(value: str) -> set[str]:
    return set(norm(value).split())


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def detect_domain(brief: str, domain_map: dict) -> str | None:
    hay = norm(brief)
    scored: list[tuple[int, str]] = []
    for domain in domain_map["domains"]:
        score = 0
        for signal in domain.get("signals", []):
            signal_norm = norm(signal)
            if signal_norm and signal_norm in hay:
                score += max(1, len(signal_norm.split()))
        scored.append((score, domain["id"]))
    scored.sort(reverse=True)
    return scored[0][1] if scored and scored[0][0] > 0 else None


def direction(scene: dict, treatment: dict, domain: str | None, brief_words: set[str]) -> dict:
    scene_words = words(scene["name"] + " " + scene["purpose"] + " " + " ".join(scene.get("domains", [])))
    treatment_words = words(treatment["name"] + " " + " ".join(treatment.get("traits", [])) + " " + treatment.get("bestWhen", ""))
    score = len(brief_words & scene_words) * 3 + len(brief_words & treatment_words)
    if domain:
        if domain in scene.get("domains", []):
            score += 30
        else:
            score -= 100
    return {
        "id": f"{scene['id']}__{treatment['id']}",
        "name": f"{scene['name']} — {treatment['name']}",
        "sceneArchetype": scene["id"],
        "artDirection": treatment["id"],
        "domains": scene.get("domains", []),
        "purpose": scene["purpose"],
        "typicalMedia": scene.get("typicalMedia", []),
        "fallback": scene["fallback"],
        "treatmentTraits": treatment.get("traits", []),
        "semanticGate": "mandatory",
        "score": score,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Select domain-relevant 3D design directions.")
    parser.add_argument("brief", help="Business/product/page brief")
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--all", action="store_true", help="Return all compatible combinations")
    args = parser.parse_args()

    system = load(SYSTEM)
    domain_map = load(DOMAIN_MAP)
    domain = detect_domain(args.brief, domain_map)
    brief_words = words(args.brief)

    candidates = [
        direction(scene, treatment, domain, brief_words)
        for scene in system["sceneArchetypes"]
        for treatment in system["artDirections"]
    ]

    compatible = [item for item in candidates if item["score"] > -50]
    compatible.sort(key=lambda item: (-item["score"], item["name"]))
    selected = compatible if args.all else compatible[: max(1, args.limit)]

    print(json.dumps({
        "brief": args.brief,
        "detectedDomain": domain,
        "libraryDirections": system["combinationCount"],
        "compatibleDirections": len(compatible),
        "warning": "This selector shortlists scene/treatment directions only. THREE_D_RELEVANCE_CONTRACT.md must still approve the actual object, environment, props, lighting, motion and fallback media.",
        "results": selected,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
