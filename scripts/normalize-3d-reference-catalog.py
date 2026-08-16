#!/usr/bin/env python3
"""Normalize metadata-only 3D reference imports without mirroring source media or code."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_KEYS = {
    "html", "sourceCode", "code", "css", "javascript", "shaderSource",
    "screenshot", "screenshots", "imageBase64", "videoBase64", "dataUrl",
    "binary", "archive", "modelFile", "textureFile", "mediaData",
}
ALLOWED_TYPES = {
    "reference-gallery", "awards-gallery", "official-documentation",
    "official-example", "implementation-demo", "community-demo",
    "template-marketplace", "asset-library", "owner-provided", "original",
}
TRACKING_KEYS = {"fbclid", "gclid"}


def canonical_url(value: str) -> str:
    parts = urlsplit(value.strip())
    if parts.scheme not in {"http", "https"} or not parts.netloc:
        raise ValueError(f"Invalid public URL: {value!r}")
    query = [
        (key, val)
        for key, val in parse_qsl(parts.query, keep_blank_values=True)
        if not key.lower().startswith("utm_") and key.lower() not in TRACKING_KEYS
    ]
    path = re.sub(r"/+$", "", parts.path) or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, urlencode(query), ""))


def clean_text(value: object, limit: int) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()[:limit]


def safe_id(value: str, url: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:72]
    if slug:
        return slug
    return "ref-" + hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]


def reject_forbidden_payload(record: dict) -> None:
    forbidden = sorted(FORBIDDEN_KEYS.intersection(record))
    if forbidden:
        raise ValueError("Forbidden copied/source-media fields: " + ", ".join(forbidden))
    serialized = json.dumps(record, ensure_ascii=False)
    if "data:image/" in serialized or "data:video/" in serialized:
        raise ValueError("Base64/data-URL media is not allowed")


def normalize_record(record: dict, source_id: str, retrieved_at: str) -> dict:
    reject_forbidden_payload(record)
    project_page = canonical_url(str(record.get("projectPage") or record.get("url") or ""))
    source_type = str(record.get("sourceType") or "reference-gallery")
    if source_type not in ALLOWED_TYPES:
        source_type = "reference-gallery"
    title = clean_text(record.get("title") or "Untitled 3D reference", 240)
    live_url = ""
    if record.get("liveUrl"):
        try:
            live_url = canonical_url(str(record["liveUrl"]))
        except ValueError:
            live_url = ""
    usage = str(record.get("usagePolicy") or "reference-only")
    if source_type in {"reference-gallery", "awards-gallery", "community-demo", "template-marketplace"}:
        usage = "reference-only" if usage not in {"owner-provided", "original"} else usage
    return {
        "id": safe_id(str(record.get("id") or title), project_page),
        "title": title,
        "sourceId": clean_text(record.get("sourceId") or source_id, 120),
        "sourceType": source_type,
        "projectPage": project_page,
        "liveUrl": live_url,
        "creator": clean_text(record.get("creator"), 200),
        "publishedText": clean_text(record.get("publishedText"), 120),
        "description": clean_text(record.get("description"), 500),
        "tags": sorted({clean_text(item, 80) for item in (record.get("tags") or []) if clean_text(item, 80)}),
        "styleFamily": clean_text(record.get("styleFamily") or "unclassified", 100),
        "interactionPatterns": sorted({clean_text(item, 100) for item in (record.get("interactionPatterns") or []) if clean_text(item, 100)}),
        "probableStack": sorted({clean_text(item, 80) for item in (record.get("probableStack") or ["unknown"]) if clean_text(item, 80)}),
        "performanceRisk": record.get("performanceRisk") if record.get("performanceRisk") in {"low", "medium", "high", "very-high", "unknown"} else "unknown",
        "mobileStrategy": clean_text(record.get("mobileStrategy") or "Review before use", 300),
        "accessibilityFallback": clean_text(record.get("accessibilityFallback") or "Define a semantic non-3D equivalent before implementation", 300),
        "usagePolicy": usage,
        "licencePosture": clean_text(record.get("licencePosture") or "Verify current source and per-item terms before reuse", 240),
        "copyPolicy": clean_text(record.get("copyPolicy") or "Do not copy code, media, branding, copy, models, textures or exact composition", 320),
        "retrievedAt": clean_text(record.get("retrievedAt") or retrieved_at, 80),
        "reviewStatus": record.get("reviewStatus") if record.get("reviewStatus") in {"unreviewed", "metadata-reviewed", "live-reviewed", "retired"} else "unreviewed",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    source_id = str(payload.get("sourceId") or "manual-import")
    retrieved_at = str(payload.get("retrievedAt") or "unknown")
    records = payload.get("records") or payload.get("references") or []
    if not isinstance(records, list):
        raise SystemExit("Input records must be an array")
    deduped: dict[str, dict] = {}
    for raw in records:
        if not isinstance(raw, dict):
            continue
        normalized = normalize_record(raw, source_id, retrieved_at)
        deduped[normalized["projectPage"]] = normalized
    result = {
        "name": "Normalized 3D Reference Catalogue",
        "policy": "3d/REFERENCE_COLLECTION_POLICY.md",
        "sourceId": source_id,
        "retrievedAt": retrieved_at,
        "total": len(deduped),
        "references": sorted(deduped.values(), key=lambda item: (item["title"].lower(), item["projectPage"])),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"NORMALIZED_3D_REFERENCES={len(deduped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
