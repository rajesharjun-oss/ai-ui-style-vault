#!/usr/bin/env python3
"""Validate Celebration & Event Microsite pack discovery, contracts and sample data."""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

ROOT = Path(__file__).resolve().parents[1]
PACK_ID = "celebration-event-microsite"
PACK_ROOT = ROOT / "packs" / PACK_ID
PROMPT_ID = "build-celebration-event-microsite"
PROMPT_PATH = "prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md"

EXPECTED_BLUEPRINTS = {
    "celebration-invitation-home",
    "meet-the-couple",
    "story-timeline",
    "event-details",
    "dress-code-colours",
    "memory-gallery",
    "rsvp",
    "gifting-registry",
    "travel-accommodation",
    "event-faq",
    "post-event-thank-you-gallery",
}

EXPECTED_COMPONENTS = {
    "event-hero",
    "couple-monogram",
    "event-countdown",
    "event-status-banner",
    "event-schedule",
    "event-details-card",
    "dress-code-palette",
    "couple-profile",
    "profile-quick-facts",
    "relationship-timeline",
    "story-chapter",
    "memory-gallery",
    "photo-lightbox",
    "accessible-video-dialog",
    "venue-map",
    "directions-card",
    "accommodation-card",
    "guest-lookup",
    "rsvp-form",
    "rsvp-confirmation",
    "rsvp-closed-state",
    "gift-options",
    "registry-card",
    "secure-gift-details",
    "whatsapp-contact",
    "faq-accordion",
    "mobile-event-menu",
    "petal-motion-layer",
    "post-event-gallery",
}

EXPECTED_STATES = {
    "save-the-date",
    "invitation-announced",
    "rsvp-not-open",
    "rsvp-open",
    "rsvp-submitting",
    "rsvp-confirmed",
    "rsvp-editing",
    "rsvp-error",
    "rsvp-deadline-passed",
    "event-upcoming",
    "event-today",
    "event-in-progress",
    "event-completed",
    "post-event-gallery",
    "site-archived",
    "guest-not-found",
    "guest-code-required",
    "guest-code-invalid",
    "guest-limit-reached",
    "gallery-loading",
    "gallery-empty",
    "media-unavailable",
    "gift-details-hidden",
    "gift-details-revealed",
    "offline-read-only",
}

EXPECTED_THEMES = {
    "romantic-editorial",
    "traditional-celebration",
    "luxury-minimal-celebration",
    "modern-playful-celebration",
    "faith-centred-ceremony",
}

REQUIRED_FILES = [
    "README.md",
    "pack.json",
    "production-themes.json",
    "page-blueprints.json",
    "component-manifest.json",
    "state-vocabulary.json",
    "content-and-storytelling.md",
    "photography-and-video-standard.md",
    "privacy-and-guest-access.md",
    "accessibility-and-responsive.md",
    "motion-guidance.md",
    "implementation-prompt.md",
    "schemas/couple-event.schema.json",
    "schemas/guest-rsvp.schema.json",
    "sample-data/wedding.sample.json",
    "templates/EVENT_BUILD_CONTRACT.md",
    "templates/COUPLE_CONTENT_PLAN.md",
    "templates/ASSET_PLAN.example.md",
    "templates/design-recipe.example.json",
    "code/event-types.ts",
    "code/event-lifecycle.ts",
    "code/README.md",
]


def load_json(path: Path, errors: list[str]) -> Any:
    if not path.is_file():
        errors.append(f"Missing JSON file: {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}


def require_file(path: Path, errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"Missing required file: {path.relative_to(ROOT)}")


def unique_ids(items: list[dict[str, Any]], label: str, errors: list[str]) -> set[str]:
    values: list[str] = []
    for index, item in enumerate(items):
        identifier = item.get("id")
        if not isinstance(identifier, str) or not identifier.strip():
            errors.append(f"{label}[{index}] is missing a non-empty id")
            continue
        values.append(identifier)
    duplicates = sorted({value for value in values if values.count(value) > 1})
    if duplicates:
        errors.append(f"Duplicate {label} ids: {', '.join(duplicates)}")
    return set(values)


def parse_datetime(value: Any, label: str, errors: list[str]) -> datetime | None:
    if not isinstance(value, str) or not value:
        errors.append(f"{label} must be a non-empty ISO date-time")
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{label} is not a valid ISO date-time: {value}")
        return None
    if parsed.tzinfo is None:
        errors.append(f"{label} must include an explicit timezone offset")
        return None
    return parsed


def validate_sample(data: Any, errors: list[str]) -> dict[str, int]:
    if not isinstance(data, dict):
        errors.append("Celebration sample root must be an object")
        return {"hosts": 0, "events": 0, "media": 0, "milestones": 0}

    meta = data.get("meta") or {}
    if meta.get("fictional") is not True:
        errors.append("Celebration sample must be explicitly fictional")

    timezone = meta.get("timezone")
    if not isinstance(timezone, str):
        errors.append("Sample meta.timezone must be a string")
    else:
        try:
            ZoneInfo(timezone)
        except ZoneInfoNotFoundError:
            errors.append(f"Sample uses an invalid IANA timezone: {timezone}")

    hosts = data.get("hosts") or []
    events = data.get("events") or []
    media = data.get("media") or []
    milestones = data.get("story") or []

    if len(hosts) < 1:
        errors.append("Celebration sample must contain at least one host")
    if len(events) < 1:
        errors.append("Celebration sample must contain at least one event")

    host_ids = unique_ids(hosts, "sample host", errors)
    event_ids = unique_ids(events, "sample event", errors)
    media_ids = unique_ids(media, "sample media", errors)
    milestone_ids = unique_ids(milestones, "sample milestone", errors)

    for host in hosts:
        if host.get("contentStatus") not in {
            "verified-couple-content",
            "requires-couple-confirmation",
        }:
            errors.append(f"Host {host.get('id')} has invalid contentStatus")
        portrait = host.get("portraitMediaId")
        if portrait and portrait not in media_ids:
            errors.append(f"Host {host.get('id')} references missing portrait {portrait}")

    starts: list[datetime] = []
    ends: list[datetime] = []
    for event in events:
        start = parse_datetime(event.get("startsAt"), f"Event {event.get('id')} startsAt", errors)
        end = parse_datetime(event.get("endsAt"), f"Event {event.get('id')} endsAt", errors)
        if start and end:
            if end <= start:
                errors.append(f"Event {event.get('id')} must end after it starts")
            starts.append(start)
            ends.append(end)
        if event.get("timezone") != timezone:
            errors.append(f"Event {event.get('id')} timezone must match sample meta.timezone")
        if event.get("status") not in {"confirmed", "provisional", "cancelled"}:
            errors.append(f"Event {event.get('id')} has invalid status")

    lifecycle = data.get("lifecycle") or {}
    primary_start = parse_datetime(lifecycle.get("primaryEventStart"), "lifecycle.primaryEventStart", errors)
    primary_end = parse_datetime(lifecycle.get("primaryEventEnd"), "lifecycle.primaryEventEnd", errors)
    if primary_start and starts and primary_start != min(starts):
        errors.append("lifecycle.primaryEventStart must equal the earliest sample event start")
    if primary_end and ends and primary_end != max(ends):
        errors.append("lifecycle.primaryEventEnd must equal the latest sample event end")
    if primary_start and primary_end and primary_end <= primary_start:
        errors.append("lifecycle.primaryEventEnd must follow primaryEventStart")

    rsvp = data.get("rsvp") or {}
    rsvp_open = parse_datetime(rsvp.get("opensAt"), "rsvp.opensAt", errors)
    rsvp_close = parse_datetime(rsvp.get("closesAt"), "rsvp.closesAt", errors)
    if rsvp_open and rsvp_close and rsvp_close <= rsvp_open:
        errors.append("RSVP close must follow RSVP open")
    if rsvp_close and primary_start and rsvp_close >= primary_start:
        errors.append("Sample RSVP deadline should precede the primary event start")

    privacy = data.get("privacy") or {}
    if privacy.get("model") not in {
        "public",
        "public-summary-private-details",
        "guest-code",
        "authenticated-guest",
        "fully-private",
    }:
        errors.append("Sample privacy model is invalid")
    retention = privacy.get("retention") or {}
    if not retention.get("guestData") or not retention.get("site"):
        errors.append("Sample privacy retention must define guestData and site")

    allowed_provenance = {
        "couple-provided",
        "host-provided",
        "photographer-licensed",
        "licensed-third-party",
        "decorative-generated-asset",
        "original",
    }
    for item in media:
        if item.get("provenance") not in allowed_provenance:
            errors.append(f"Media {item.get('id')} has invalid provenance")
        if item.get("consentStatus") not in {"confirmed", "pending", "restricted"}:
            errors.append(f"Media {item.get('id')} has invalid consentStatus")
        if item.get("access") not in {"public", "guest-only", "host-only"}:
            errors.append(f"Media {item.get('id')} has invalid access")

    sequences: list[int] = []
    for milestone in milestones:
        sequence = milestone.get("sequence")
        if not isinstance(sequence, int) or sequence < 1:
            errors.append(f"Milestone {milestone.get('id')} has invalid sequence")
        else:
            sequences.append(sequence)
        for media_id in milestone.get("mediaIds") or []:
            if media_id not in media_ids:
                errors.append(f"Milestone {milestone.get('id')} references missing media {media_id}")
    if len(sequences) != len(set(sequences)):
        errors.append("Sample milestones must have unique sequence values")

    if not host_ids or not event_ids:
        errors.append("Sample host and event identifiers are required")

    return {
        "hosts": len(host_ids),
        "events": len(event_ids),
        "media": len(media_ids),
        "milestones": len(milestone_ids),
    }


def main() -> int:
    errors: list[str] = []

    for relative in [
        "AGENTS.md",
        "PROMPTS.md",
        "PACKS.md",
        "CLAUDE.md",
        "GEMINI.md",
        "prompts/prompt-index.json",
        "packs/pack-index.json",
        PROMPT_PATH,
    ]:
        require_file(ROOT / relative, errors)

    for relative in REQUIRED_FILES:
        require_file(PACK_ROOT / relative, errors)

    pack_index = load_json(ROOT / "packs/pack-index.json", errors)
    packs = pack_index.get("packs") if isinstance(pack_index, dict) else []
    if not isinstance(packs, list):
        errors.append("packs/pack-index.json packs must be an array")
        packs = []
    pack_ids = unique_ids(packs, "domain pack", errors)
    if PACK_ID not in pack_ids:
        errors.append("Celebration & Event Microsite pack is not registered")
    pack_entry = next((item for item in packs if item.get("id") == PACK_ID), {})
    if pack_entry.get("requiredPrompt") != PROMPT_PATH:
        errors.append("Celebration pack index has the wrong requiredPrompt")
    for relative in pack_entry.get("requiredReads") or []:
        require_file(ROOT / relative, errors)

    pack = load_json(PACK_ROOT / "pack.json", errors)
    if pack.get("id") != PACK_ID:
        errors.append("Celebration pack.json has the wrong id")
    if pack.get("requiredPrompt") != PROMPT_PATH:
        errors.append("Celebration pack.json has the wrong requiredPrompt")
    for artifact in ["EVENT_BUILD_CONTRACT.md", "COUPLE_CONTENT_PLAN.md", "ASSET_PLAN.md"]:
        if artifact not in (pack.get("requiredPlanningArtifacts") or []):
            errors.append(f"Celebration pack is missing planning artifact {artifact}")

    blueprints_data = load_json(PACK_ROOT / "page-blueprints.json", errors)
    blueprint_ids = unique_ids(blueprints_data.get("blueprints") or [], "celebration blueprint", errors)
    missing = sorted(EXPECTED_BLUEPRINTS - blueprint_ids)
    if missing:
        errors.append(f"Missing celebration blueprints: {', '.join(missing)}")

    components_data = load_json(PACK_ROOT / "component-manifest.json", errors)
    component_ids = unique_ids(components_data.get("components") or [], "celebration component", errors)
    missing = sorted(EXPECTED_COMPONENTS - component_ids)
    if missing:
        errors.append(f"Missing celebration components: {', '.join(missing)}")

    states_data = load_json(PACK_ROOT / "state-vocabulary.json", errors)
    state_ids = unique_ids(states_data.get("states") or [], "celebration state", errors)
    missing = sorted(EXPECTED_STATES - state_ids)
    if missing:
        errors.append(f"Missing celebration states: {', '.join(missing)}")

    themes_data = load_json(PACK_ROOT / "production-themes.json", errors)
    theme_ids = unique_ids(themes_data.get("themes") or [], "celebration theme", errors)
    missing = sorted(EXPECTED_THEMES - theme_ids)
    if missing:
        errors.append(f"Missing celebration themes: {', '.join(missing)}")

    for relative in [
        "schemas/couple-event.schema.json",
        "schemas/guest-rsvp.schema.json",
        "templates/design-recipe.example.json",
    ]:
        data = load_json(PACK_ROOT / relative, errors)
        if relative.startswith("schemas/") and data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            errors.append(f"{relative} must use JSON Schema draft 2020-12")

    sample = load_json(PACK_ROOT / "sample-data/wedding.sample.json", errors)
    sample_counts = validate_sample(sample, errors)

    prompt_index = load_json(ROOT / "prompts/prompt-index.json", errors)
    prompts = prompt_index.get("prompts") if isinstance(prompt_index, dict) else []
    prompt_entry = next((item for item in prompts or [] if item.get("id") == PROMPT_ID), None)
    if not prompt_entry:
        errors.append("Celebration build prompt is not registered")
    else:
        if prompt_entry.get("path") != PROMPT_PATH:
            errors.append("Celebration prompt index path is incorrect")
        if prompt_entry.get("requiresDomainPack") != PACK_ID:
            errors.append("Celebration prompt does not require the celebration pack")

    discoverability = {
        "AGENTS.md": [PROMPT_PATH, PACK_ID, "EVENT_BUILD_CONTRACT.md"],
        "PROMPTS.md": [PROMPT_PATH, PACK_ID],
        "PACKS.md": ["packs/pack-index.json", PACK_ID],
        "CLAUDE.md": [PROMPT_PATH, PACK_ID],
        "GEMINI.md": [PROMPT_PATH, PACK_ID],
    }
    for relative, needles in discoverability.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append(f"{relative} does not reference {needle}")

    lifecycle_code = PACK_ROOT / "code" / "event-lifecycle.ts"
    if lifecycle_code.is_file():
        text = lifecycle_code.read_text(encoding="utf-8")
        for signal in [
            "event-today",
            "event-in-progress",
            "event-completed",
            "post-event-gallery",
            "site-archived",
            "IANA",
            "server",
        ]:
            if signal not in text:
                errors.append(f"event-lifecycle.ts is missing lifecycle/security signal: {signal}")

    privacy_text = (PACK_ROOT / "privacy-and-guest-access.md").read_text(encoding="utf-8") if (PACK_ROOT / "privacy-and-guest-access.md").is_file() else ""
    for signal in ["enumeration", "rate limit", "financial", "retention", "analytics"]:
        if signal.lower() not in privacy_text.lower():
            errors.append(f"privacy-and-guest-access.md is missing signal: {signal}")

    print(f"CELEBRATION_BLUEPRINTS={len(blueprint_ids)}")
    print(f"CELEBRATION_COMPONENTS={len(component_ids)}")
    print(f"CELEBRATION_STATES={len(state_ids)}")
    print(f"CELEBRATION_THEMES={len(theme_ids)}")
    print(f"SAMPLE_HOSTS={sample_counts['hosts']}")
    print(f"SAMPLE_EVENTS={sample_counts['events']}")
    print(f"SAMPLE_MEDIA={sample_counts['media']}")
    print(f"SAMPLE_MILESTONES={sample_counts['milestones']}")

    if errors:
        print("CELEBRATION_PACK_VALIDATION=FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("CELEBRATION_PACK_VALIDATION=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
