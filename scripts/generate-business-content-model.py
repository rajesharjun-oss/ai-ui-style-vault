#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path


def load_report(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    required = {"source", "business", "assets", "reviews", "inference", "contentPolicy"}
    missing = sorted(required - set(data))
    if missing:
        raise ValueError(f"missing report fields: {', '.join(missing)}")
    return data


def entity(entity_id, entity_type, fields, source_status="verified", public="public", admin="editable-with-provenance"):
    return {
        "id": entity_id,
        "type": entity_type,
        "sourceStatus": source_status,
        "publicVisibility": public,
        "adminCapability": admin,
        "fields": fields,
    }


def build_entities(report):
    business = report["business"]
    source = report["source"]
    status = "verified" if source["accessStatus"] == "inspected" else "user-supplied" if source["accessStatus"] == "user-supplied" else "provisional"
    entities = [
        entity(
            "business_identity",
            "business",
            {"name": business["name"], **business.get("facts", {})},
            source_status=status,
            admin="editable-with-provenance",
        )
    ]
    if business.get("hours"):
        entities.append(entity(
            "business_hours",
            "hours",
            {"lines": business["hours"]},
            source_status=status,
            admin="editable-with-provenance",
        ))
    if business.get("offers"):
        entities.append(entity(
            "business_offers",
            "offers",
            {"items": business["offers"]},
            source_status=status,
            admin="editable-with-provenance",
        ))
    if business.get("highlights"):
        entities.append(entity(
            "business_highlights",
            "highlights",
            {"items": business["highlights"]},
            source_status=status,
            admin="editable-with-provenance",
        ))
    for i, asset in enumerate(report.get("assets", []), start=1):
        entities.append(entity(
            asset.get("id") or f"asset_{i:02d}",
            "media_asset",
            {
                "url": asset["url"],
                "alt": asset["alt"],
                "description": asset["description"],
            },
            source_status=asset["evidenceStatus"],
            admin="asset-management",
        ))
    for i, review in enumerate(report.get("reviews", []), start=1):
        entities.append(entity(
            f"review_{i:02d}",
            "review",
            review,
            source_status=status,
            admin="moderation-only",
        ))
    inference = report.get("inference", {})
    entities.append(entity(
        "design_inference",
        "inference",
        {
            "businessCategory": inference.get("businessCategory"),
            "subcategories": inference.get("subcategories", []),
            "audiences": inference.get("audiences", []),
            "primaryConversion": inference.get("primaryConversion"),
            "brandSignals": inference.get("brandSignals"),
        },
        source_status="inferred",
        public="hidden",
        admin="not-managed",
    ))
    return entities


def build_public_model(report, entities):
    business = report["business"]
    facts = business.get("facts", {})
    available = {
        "identity": True,
        "contact": any(k.lower() in {"phone", "email", "website", "address", "location"} for k in facts),
        "hours": bool(business.get("hours")),
        "offers": bool(business.get("offers")),
        "highlights": bool(business.get("highlights")),
        "gallery": bool(report.get("assets")),
        "reviews": bool(report.get("reviews")),
    }
    return {
        "availableContent": available,
        "entityIds": [e["id"] for e in entities if e["publicVisibility"] == "public"],
        "sectionEligibility": [k for k, v in available.items() if v],
        "primaryConversion": report["inference"].get("primaryConversion"),
        "rules": [
            "Only render sections whose evidence-backed content exists.",
            "Do not create a menu, team, awards, pricing, booking, ordering, delivery or social section unless the source report supports it.",
            "Reviews remain verbatim.",
            "Source assets obey the asset manifest policy.",
        ],
    }


def admin_module(module_id, entity_types, capabilities, enabled, reason):
    return {
        "id": module_id,
        "entityTypes": entity_types,
        "capabilities": capabilities if enabled else [],
        "enabled": enabled,
        "reason": reason,
    }


def build_admin_model(report, entities):
    business = report["business"]
    facts = business.get("facts", {})
    modules = [
        admin_module("business-profile", ["business"], ["view", "edit-with-provenance"], True, "Core business identity exists."),
        admin_module("hours", ["hours"], ["view", "edit-with-provenance"], bool(business.get("hours")), "Enabled only when source hours exist."),
        admin_module("gallery", ["media_asset"], ["view", "reorder", "visibility", "replace-with-approved-asset"], bool(report.get("assets")), "Enabled only when approved media exists."),
        admin_module("reviews", ["review"], ["view", "feature", "hide-from-site"], bool(report.get("reviews")), "Review text itself is immutable; moderation controls only visibility/featuring."),
        admin_module("offers", ["offers", "highlights"], ["view", "edit-with-provenance"], bool(business.get("offers") or business.get("highlights")), "Enabled only for evidenced offers/highlights."),
        admin_module("contact", ["business"], ["view", "edit-with-provenance"], any(k.lower() in {"phone", "email", "website", "address", "location"} for k in facts), "Enabled when contact/location fields exist."),
    ]
    forbidden = [
        "Do not generate orders, revenue, conversion, stock, availability, customer, booking, security-event or system-health records unless the source or owner explicitly provides those operational datasets.",
        "Do not invent admin sample rows or dashboard statistics.",
        "Do not let admin edits silently overwrite source provenance; retain original source value and change history in a real implementation.",
        "Review copy is verbatim and must not be rewritten from the admin panel.",
    ]
    return {
        "enabledModules": [m for m in modules if m["enabled"]],
        "disabledModules": [m for m in modules if not m["enabled"]],
        "forbiddenSyntheticModules": ["orders", "revenue", "inventory", "bookings", "customers", "system-health", "security-log"],
        "rules": forbidden,
    }


def build_contract(report, model):
    enabled = "\n".join(f"- {m['id']}: {m['reason']}" for m in model["adminModel"]["enabledModules"])
    disabled = "\n".join(f"- {m['id']}: {m['reason']}" for m in model["adminModel"]["disabledModules"]) or "- None"
    return f"""# CMS Build Contract — {report['business']['name']}

## Purpose

Build admin/CMS functionality only for entities supported by the source report. The admin is an operational editor for evidenced content, not a license to invent business systems.

## Enabled modules

{enabled}

## Disabled modules

{disabled}

## Hard rules

- Never invent admin records, sample rows, timestamps, sales/order totals, stock quantities, bookings, user accounts, security logs or system health statistics.
- Preserve source provenance for editable factual values.
- Reviews are moderation-only: feature/hide is permitted, rewriting is not.
- Approved media may be reordered or hidden; replacement must use another approved/user-supplied asset unless the asset policy explicitly allows generated concept media.
- Public page architecture must be driven by `PUBLIC_CONTENT_MODEL.json`, not by empty CMS modules.
- A disabled module stays absent from both frontend and admin until evidence or owner requirements justify it.
"""


def main():
    p = argparse.ArgumentParser(description="Generate evidence-backed public content and admin/CMS models from a Business Source Report.")
    p.add_argument("source", help="BUSINESS_SOURCE_REPORT.json or ingestion directory containing it")
    p.add_argument("--output-dir")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    source = Path(args.source)
    if source.is_dir():
        report_path = source / "BUSINESS_SOURCE_REPORT.json"
        out = Path(args.output_dir) if args.output_dir else source
    else:
        report_path = source
        out = Path(args.output_dir) if args.output_dir else source.parent
    if not report_path.exists():
        print(json.dumps({"status": "error", "reason": "BUSINESS_SOURCE_REPORT.json not found", "path": str(report_path)}, indent=2), file=sys.stderr)
        return 2
    try:
        report = load_report(report_path)
    except Exception as exc:
        print(json.dumps({"status": "error", "reason": str(exc)}, indent=2), file=sys.stderr)
        return 3

    out.mkdir(parents=True, exist_ok=True)
    entities = build_entities(report)
    model = {
        "schemaVersion": "1.0.0",
        "businessName": report["business"]["name"],
        "sourceReference": report["source"]["reference"],
        "entities": entities,
        "publicModel": build_public_model(report, entities),
        "adminModel": build_admin_model(report, entities),
        "rules": [
            "Evidence creates entities; missing evidence does not create placeholder entities.",
            "Inference may guide design but does not become an editable verified fact.",
            "Admin capability must match entity semantics and provenance.",
        ],
    }
    (out / "BUSINESS_ENTITY_MODEL.json").write_text(json.dumps(model, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "PUBLIC_CONTENT_MODEL.json").write_text(json.dumps(model["publicModel"], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "ADMIN_CMS_MODEL.json").write_text(json.dumps(model["adminModel"], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "CMS_BUILD_CONTRACT.md").write_text(build_contract(report, model), encoding="utf-8")
    summary = {
        "status": "ready",
        "entityCount": len(entities),
        "enabledAdminModules": [m["id"] for m in model["adminModel"]["enabledModules"]],
        "publicSectionsEligible": model["publicModel"]["sectionEligibility"],
        "outputDirectory": str(out),
        "nextCommand": f"python scripts/vault-agent.py plan {out / 'business-profile.json'} --output {out / 'vault-build-plan.json'}",
    }
    (out / "content-model-summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False) if args.json else f"CONTENT_MODEL_STATUS=ready\nOUTPUT_DIR={out}\nNEXT={summary['nextCommand']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
