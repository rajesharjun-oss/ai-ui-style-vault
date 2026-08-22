#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK_INDEX = ROOT / "research" / "source-playbooks" / "index.json"


def is_url(value: str) -> bool:
    try:
        parsed = urlparse(value)
        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)
    except Exception:
        return False


def write_json(path: Path, payload):
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_playbook_index():
    return json.loads(PLAYBOOK_INDEX.read_text(encoding="utf-8"))


def detect_source_type(url: str):
    parsed = urlparse(url)
    haystack = f"{parsed.netloc.lower()}{parsed.path.lower()}"
    index = load_playbook_index()
    ordered = sorted(index["playbooks"], key=lambda item: item.get("priority", 0), reverse=True)
    fallback = None
    for item in ordered:
        if item.get("fallback"):
            fallback = item
            continue
        if any(signal.lower() in haystack for signal in item.get("hostSignals", [])):
            return item
    return fallback or ordered[-1]


def validate_report(report):
    errors = []
    for key in ["schemaVersion", "source", "business", "assets", "reviews", "evidence", "inference", "contentPolicy"]:
        if key not in report:
            errors.append(f"missing top-level field: {key}")
    if errors:
        return errors
    if report.get("schemaVersion") != "1.0.0":
        errors.append("schemaVersion must be 1.0.0")
    source = report.get("source", {})
    for key in ["type", "reference", "accessStatus"]:
        if not source.get(key):
            errors.append(f"source.{key} is required")
    if source.get("accessStatus") not in {"inspected", "user-supplied", "partial", "blocked"}:
        errors.append("source.accessStatus is invalid")
    business = report.get("business", {})
    if not business.get("name"):
        errors.append("business.name is required")
    if not isinstance(business.get("facts"), dict):
        errors.append("business.facts must be an object")
    if not isinstance(business.get("hours"), list):
        errors.append("business.hours must be an array")
    assets = report.get("assets", [])
    if not isinstance(assets, list):
        errors.append("assets must be an array")
    else:
        ids = []
        for i, asset in enumerate(assets):
            for key in ["id", "url", "alt", "description", "evidenceStatus"]:
                if key not in asset:
                    errors.append(f"assets[{i}].{key} is required")
            if asset.get("evidenceStatus") not in {"verified", "user-supplied", "provisional"}:
                errors.append(f"assets[{i}].evidenceStatus is invalid")
            ids.append(asset.get("id"))
        if len(ids) != len(set(ids)):
            errors.append("asset ids must be unique")
    reviews = report.get("reviews", [])
    if not isinstance(reviews, list):
        errors.append("reviews must be an array")
    else:
        for i, review in enumerate(reviews):
            for key in ["author", "rating", "relativeTime", "text", "verbatim"]:
                if key not in review:
                    errors.append(f"reviews[{i}].{key} is required")
            if review.get("verbatim") is not True:
                errors.append(f"reviews[{i}].verbatim must be true")
    if not report.get("evidence"):
        errors.append("at least one evidence record is required")
    inference = report.get("inference", {})
    for key in ["businessCategory", "audiences", "primaryConversion", "brandSignals", "confidence"]:
        if key not in inference:
            errors.append(f"inference.{key} is required")
    confidence = inference.get("confidence", {})
    score = confidence.get("score")
    if not isinstance(score, int) or not 0 <= score <= 100:
        errors.append("inference.confidence.score must be an integer from 0 to 100")
    policy = report.get("contentPolicy", {})
    if policy.get("reviews") != "verbatim":
        errors.append("contentPolicy.reviews must be verbatim")
    if policy.get("unsupportedFields") != "omit-or-empty":
        errors.append("contentPolicy.unsupportedFields must be omit-or-empty")
    return errors


def research_request(url, output_dir):
    playbook = detect_source_type(url)
    index = load_playbook_index()
    source_type = playbook["id"]
    request = {
        "schemaVersion": "1.1.0",
        "status": "research-required",
        "source": {"reference": url, "typeHint": source_type},
        "playbook": {
            "id": source_type,
            "path": playbook["path"]
        },
        "instruction": "Inspect the source with available web/browser/connectors using the selected source-specific playbook, then create a Business Source Report conforming to research/business-source-report.schema.json. Preserve exact factual strings and verbatim reviews. Do not invent missing fields or substitute assets.",
        "requiredReads": [
            "prompts/BUSINESS_SOURCE_INGESTION.md",
            "research/business-source-report.schema.json",
            playbook["path"]
        ],
        "requiredExtraction": [
            "official business name",
            "contact/location/website/rating facts shown by the source",
            "hours exactly as shown when available",
            "offers/highlights supported by evidence",
            "permitted business assets with provenance and ownership/use status",
            "reviews verbatim when selected",
            "evidence records for important claims",
            "business category/audience/conversion inference separated from verified facts",
            "research gaps, source conflicts and prohibited assumptions"
        ],
        "sharedHardRules": index["sharedRules"],
        "blockedSourceRule": "If this source is blocked or partial, mark access accurately and use other public/user-supplied sources only as separate evidence records. Never claim blocked content was inspected.",
        "nextCommand": "python scripts/vault-agent.py ingest <BUSINESS_SOURCE_REPORT.json>"
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / "business-source-request.json", request)
    return request


def to_business_profile(report):
    business = report["business"]
    inference = report["inference"]
    source = report["source"]
    offers = business.get("offers", [])
    if not offers:
        offers = business.get("highlights", [])
    if not offers:
        offers = [inference["businessCategory"]]
    evidence_status = "verified" if source["accessStatus"] in {"inspected", "user-supplied"} else "provisional"
    confidence = inference["confidence"]
    ready = source["accessStatus"] != "blocked" and confidence["score"] >= 70
    return {
        "status": "ready" if ready else "needs-owner-confirmation",
        "officialName": business["name"],
        "businessCategory": inference["businessCategory"],
        "subcategories": inference.get("subcategories", []),
        "offers": [{"name": item, "evidenceStatus": evidence_status} for item in offers],
        "audiences": inference["audiences"],
        "primaryConversion": inference["primaryConversion"],
        "evidenceSources": [{
            "type": source["type"],
            "reference": source["reference"],
            "accessStatus": source["accessStatus"]
        }],
        "brandSignals": inference["brandSignals"],
        "operationalFacts": business.get("facts", {}),
        "researchGaps": inference.get("researchGaps", []),
        "prohibitedAssumptions": inference.get("prohibitedAssumptions", []),
        "confidence": confidence,
        "recommendedDomainPack": inference.get("recommendedDomainPack"),
        "designSelectionAllowed": ready
    }


def build_source_of_truth(report):
    return {
        "schemaVersion": "1.0.0",
        "businessName": report["business"]["name"],
        "sourceReference": report["source"]["reference"],
        "facts": report["business"].get("facts", {}),
        "hours": report["business"].get("hours", []),
        "offers": report["business"].get("offers", []),
        "highlights": report["business"].get("highlights", []),
        "reviews": report["reviews"],
        "rules": {
            "facts": report["contentPolicy"]["facts"],
            "reviews": "verbatim",
            "unsupportedFields": "omit-or-empty",
            "noPlaceholderRecords": True,
            "noDerivedSubstitutesForVerifiedValues": True
        }
    }


def build_asset_manifest(report):
    return {
        "schemaVersion": "1.0.0",
        "policy": report["contentPolicy"]["assets"],
        "sourceReference": report["source"]["reference"],
        "assets": report["assets"],
        "rules": [
            "Do not silently replace a failed allowlisted asset.",
            "Do not present generated concept media as verified business media.",
            "If the policy is allowlist-only or verified-only, use no unlisted images."
        ]
    }


def build_research_markdown(report):
    b = report["business"]
    inf = report["inference"]
    lines = [
        f"# Business Research — {b['name']}", "",
        f"Source: {report['source']['type']} — {report['source']['reference']}",
        f"Access status: {report['source']['accessStatus']}", "",
        "## Verified/source facts", ""
    ]
    for key, value in b.get("facts", {}).items():
        lines.append(f"- **{key}:** {value}")
    if b.get("hours"):
        lines += ["", "## Hours (preserve exactly)", ""] + [f"- {x}" for x in b["hours"]]
    lines += ["", "## Offers/highlights", ""]
    for x in b.get("offers", []):
        lines.append(f"- {x}")
    for x in b.get("highlights", []):
        lines.append(f"- {x}")
    lines += ["", "## Inference", "", f"- Category: {inf['businessCategory']}"]
    for audience in inf.get("audiences", []):
        lines.append(f"- Audience: {audience}")
    pc = inf["primaryConversion"]
    lines.append(f"- Primary conversion: {pc['action']} via {pc['channel']} ({pc['evidenceStatus']})")
    lines += ["", "## Research gaps", ""] + [f"- {x}" for x in inf.get("researchGaps", [])]
    lines += ["", "## Prohibited assumptions", ""] + [f"- {x}" for x in inf.get("prohibitedAssumptions", [])]
    lines += ["", "## Evidence", ""]
    for item in report["evidence"]:
        lines.append(f"- [{item['status']}] {item['claim']} — {item['sourceReference']}")
    return "\n".join(lines).rstrip() + "\n"


def build_verbatim_reviews(reviews):
    if not reviews:
        return "(No review records supplied.)"
    chunks = []
    for i, review in enumerate(reviews, start=1):
        chunks.append(
            f"### Review {i}\n"
            f"Author: {review['author']}\n"
            f"Rating: {review['rating']}\n"
            f"Relative time: {review['relativeTime']}\n"
            f"Verbatim: true\n\n"
            f"{review['text']}"
        )
    return "\n\n---\n\n".join(chunks)


def build_prompt(report):
    b = report["business"]
    facts_json = json.dumps(b.get("facts", {}), indent=2, ensure_ascii=False)
    assets_json = json.dumps(report["assets"], indent=2, ensure_ascii=False)
    reviews_text = build_verbatim_reviews(report["reviews"])
    return f'''# Evidence-Constrained Build Prompt — {b['name']}

Build from the attached Vault plan and selected domain pack. Treat the source-of-truth below as authoritative.

## Hard content rules

1. Do not invent business facts, names, addresses, phone numbers, websites, ratings, hours, prices, claims, reviews, timestamps, social links, integrations, awards, locations or placeholder records.
2. When a field is unsupported, omit it or leave it empty.
3. Preserve every review marked `verbatim: true` exactly, including punctuation, casing, typos, emoji and blank lines.
4. Apply the asset policy exactly: `{report['contentPolicy']['assets']}`.
5. Keep verified/source facts separate from design/content inference.
6. Do not silently substitute an image when an allowlisted image fails.
7. The Vault determines page architecture from the business/domain; do not force a single-page or multi-page structure unless the selected plan requires it.

## Business name

{b['name']}

## Exact/source facts

```json
{facts_json}
```

## Hours — preserve each line exactly

```json
{json.dumps(b.get('hours', []), indent=2, ensure_ascii=False)}
```

## Asset manifest

```json
{assets_json}
```

## Reviews — verbatim literal text

{reviews_text}

## Design inference (not verified business facts)

```json
{json.dumps(report['inference'], indent=2, ensure_ascii=False)}
```
'''


def materialize(report, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / "BUSINESS_SOURCE_REPORT.json", report)
    write_json(output_dir / "CONTENT_SOURCE_OF_TRUTH.json", build_source_of_truth(report))
    write_json(output_dir / "ASSET_MANIFEST.json", build_asset_manifest(report))
    profile = to_business_profile(report)
    write_json(output_dir / "business-profile.json", profile)
    (output_dir / "BUSINESS_RESEARCH.md").write_text(build_research_markdown(report), encoding="utf-8")
    (output_dir / "BUILD_PROMPT.md").write_text(build_prompt(report), encoding="utf-8")
    summary = {
        "status": "ready" if profile["designSelectionAllowed"] else "needs-owner-confirmation",
        "business": report["business"]["name"],
        "sourceType": report["source"]["type"],
        "assetCount": len(report["assets"]),
        "reviewCount": len(report["reviews"]),
        "outputDirectory": str(output_dir),
        "nextCommand": f"python scripts/vault-agent.py plan {output_dir / 'business-profile.json'} --output {output_dir / 'vault-build-plan.json'}"
    }
    write_json(output_dir / "ingestion-summary.json", summary)
    return summary


def main():
    p = argparse.ArgumentParser(description="Normalize evidence from a business source into Vault source-of-truth and planning artifacts without inventing missing data.")
    p.add_argument("source", help="Business URL (creates a source-specific research request) or Business Source Report JSON file")
    p.add_argument("--output-dir", default="business-ingestion")
    p.add_argument("--json", action="store_true", help="Print machine-readable result")
    args = p.parse_args()
    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = Path.cwd() / output_dir

    if is_url(args.source):
        result = research_request(args.source, output_dir)
        print(json.dumps(result, indent=2, ensure_ascii=False) if args.json else f"RESEARCH_REQUIRED={output_dir / 'business-source-request.json'}")
        return 3

    source_path = Path(args.source)
    if not source_path.exists():
        print(json.dumps({"status": "error", "reason": "source file not found", "source": args.source}, indent=2), file=sys.stderr)
        return 2
    try:
        report = json.loads(source_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(json.dumps({"status": "error", "reason": f"invalid JSON: {exc}"}, indent=2), file=sys.stderr)
        return 2
    errors = validate_report(report)
    if errors:
        print(json.dumps({"status": "invalid", "errors": errors}, indent=2, ensure_ascii=False), file=sys.stderr)
        return 4
    summary = materialize(report, output_dir)
    print(json.dumps(summary, indent=2, ensure_ascii=False) if args.json else f"INGESTION_STATUS={summary['status']}\nOUTPUT_DIR={output_dir}\nNEXT={summary['nextCommand']}")
    return 0 if summary["status"] == "ready" else 5


if __name__ == "__main__":
    raise SystemExit(main())
