from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_ROOT = ROOT / "packs" / "celebration-event-microsite"
VALIDATOR = ROOT / "scripts" / "validate-celebration-pack.py"


class CelebrationEventMicrositePackTests(unittest.TestCase):
    def load(self, relative: str) -> dict:
        return json.loads((ROOT / relative).read_text(encoding="utf-8"))

    def test_celebration_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("CELEBRATION_PACK_VALIDATION=PASS", result.stdout)

    def test_expected_blueprints_components_states_and_themes_exist(self) -> None:
        blueprints = {
            item["id"]
            for item in self.load("packs/celebration-event-microsite/page-blueprints.json")["blueprints"]
        }
        components = {
            item["id"]
            for item in self.load("packs/celebration-event-microsite/component-manifest.json")["components"]
        }
        states = {
            item["id"]
            for item in self.load("packs/celebration-event-microsite/state-vocabulary.json")["states"]
        }
        themes = {
            item["id"]
            for item in self.load("packs/celebration-event-microsite/production-themes.json")["themes"]
        }

        for expected in [
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
        ]:
            self.assertIn(expected, blueprints)

        for expected in [
            "event-hero",
            "event-countdown",
            "relationship-timeline",
            "accessible-video-dialog",
            "guest-lookup",
            "rsvp-form",
            "secure-gift-details",
            "post-event-gallery",
        ]:
            self.assertIn(expected, components)

        for expected in [
            "rsvp-open",
            "event-today",
            "event-in-progress",
            "event-completed",
            "post-event-gallery",
            "guest-code-invalid",
            "gift-details-hidden",
        ]:
            self.assertIn(expected, states)

        for expected in [
            "romantic-editorial",
            "traditional-celebration",
            "luxury-minimal-celebration",
            "modern-playful-celebration",
            "faith-centred-ceremony",
        ]:
            self.assertIn(expected, themes)

    def test_prompt_and_platform_discovery(self) -> None:
        prompt_index = self.load("prompts/prompt-index.json")
        prompt = next(
            item
            for item in prompt_index["prompts"]
            if item["id"] == "build-celebration-event-microsite"
        )
        self.assertEqual(prompt["path"], "prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md")
        self.assertEqual(prompt["requiresDomainPack"], "celebration-event-microsite")

        pack_index = self.load("packs/pack-index.json")
        pack = next(
            item for item in pack_index["packs"] if item["id"] == "celebration-event-microsite"
        )
        self.assertEqual(pack["requiredPrompt"], "prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md")

        for relative in ["AGENTS.md", "PROMPTS.md", "PACKS.md", "CLAUDE.md", "GEMINI.md"]:
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("BUILD_CELEBRATION_EVENT_MICROSITE.md", text)
            self.assertIn("celebration-event-microsite", text)

    def test_sample_is_fictional_and_consistent(self) -> None:
        sample = self.load("packs/celebration-event-microsite/sample-data/wedding.sample.json")
        self.assertTrue(sample["meta"]["fictional"])
        self.assertEqual(sample["meta"]["timezone"], "Africa/Lagos")

        media_ids = {item["id"] for item in sample["media"]}
        event_starts = [item["startsAt"] for item in sample["events"]]
        event_ends = [item["endsAt"] for item in sample["events"]]

        for host in sample["hosts"]:
            self.assertIn(host["portraitMediaId"], media_ids)
        for milestone in sample["story"]:
            self.assertTrue(set(milestone["mediaIds"]).issubset(media_ids))

        self.assertEqual(sample["lifecycle"]["primaryEventStart"], min(event_starts))
        self.assertEqual(sample["lifecycle"]["primaryEventEnd"], max(event_ends))
        self.assertIn(sample["privacy"]["model"], {
            "public",
            "public-summary-private-details",
            "guest-code",
            "authenticated-guest",
            "fully-private",
        })
        self.assertTrue(sample["privacy"]["retention"]["guestData"])
        self.assertTrue(sample["privacy"]["retention"]["site"])

    def test_schemas_and_lifecycle_security_boundary(self) -> None:
        for relative in [
            "packs/celebration-event-microsite/schemas/couple-event.schema.json",
            "packs/celebration-event-microsite/schemas/guest-rsvp.schema.json",
        ]:
            schema = self.load(relative)
            self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")

        lifecycle = (PACK_ROOT / "code" / "event-lifecycle.ts").read_text(encoding="utf-8")
        types = (PACK_ROOT / "code" / "event-types.ts").read_text(encoding="utf-8")
        for signal in [
            "event-today",
            "event-in-progress",
            "event-completed",
            "post-event-gallery",
            "site-archived",
            "server",
        ]:
            self.assertIn(signal, lifecycle)
        self.assertIn("PrivacyModel", types)
        self.assertIn("RSVPSubmission", types)
        self.assertIn("CapabilityStatus", types)

    def test_pack_contains_privacy_accessibility_and_motion_rules(self) -> None:
        privacy = (PACK_ROOT / "privacy-and-guest-access.md").read_text(encoding="utf-8").lower()
        accessibility = (PACK_ROOT / "accessibility-and-responsive.md").read_text(encoding="utf-8").lower()
        motion = (PACK_ROOT / "motion-guidance.md").read_text(encoding="utf-8").lower()

        for signal in ["enumeration", "rate limit", "financial", "retention", "analytics"]:
            self.assertIn(signal, privacy)
        for signal in ["keyboard", "visible focus", "reduced-motion", "no-javascript", "dialog"]:
            self.assertIn(signal, accessibility)
        for signal in ["petals", "prefers-reduced-motion", "scroll reveal", "pointer events"]:
            self.assertIn(signal, motion)


if __name__ == "__main__":
    unittest.main()
