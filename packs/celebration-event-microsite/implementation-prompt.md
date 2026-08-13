# Celebration & Event Microsite Implementation Prompt

Use this file together with `AGENTS.md`, `PROMPTS.md`, `PACKS.md`, `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md` and every required file in this pack.

```text
Act as a coordinated senior product designer, senior content designer, privacy-aware event-experience designer and senior front-end engineer.

Build an original celebration microsite from the verified couple/host content, event details, privacy model and supplied media. Do not reproduce another couple's website or fill a generic wedding template.

Before coding:
1. Inspect the target repository and available integrations.
2. Complete EVENT_BUILD_CONTRACT.md, COUPLE_CONTENT_PLAN.md, ASSET_PLAN.md, VAULT_SELECTION.md, BUILD_CONTRACT.md, CONTENT_PLAN.md and design-recipe.json.
3. Classify every personal fact, date, venue, photograph, video, contact, guest rule and gift detail by verification and privacy status.
4. Choose one production theme from production-themes.json and explain why it fits the couple, culture, faith, venue, attire and media.
5. Define the complete event lifecycle in a verified IANA timezone.
6. Define the public/private boundary and guest-access model.
7. State which RSVP, guest lookup, messaging, map, calendar, gifting, media and analytics capabilities are integrated, prototype-only, require integration or are out of scope.
8. Select only the page blueprints needed for this event.

Content requirements:
- The first viewport identifies the couple or hosts, event, date, place summary and primary guest action without an essay.
- Do not invent personal stories, family roles, dates, venues, dress codes, scriptures, bank details or travel arrangements.
- Move full biographies and long story chapters behind summaries, dedicated pages or progressive disclosure.
- Keep practical guest information explicit and consistent.
- Preserve names, diacritics, faith terminology and cultural language accurately.
- Gifting must be optional in wording and hierarchy.

Media requirements:
- Use user-provided, owned or clearly licensed couple media.
- Never present generated people as the real couple, family or guests.
- Generated media may support decorative florals, patterns or textures only when recorded as conceptual.
- Plan desktop/mobile crops, focal points, alt text, captions, consent, access and retention.
- Use responsive formats and prevent layout shift.

Interaction requirements:
- Implement semantic navigation, buttons, disclosures and dialogs.
- Gallery and video viewers require focus trap, Escape close, focus restoration, captions/alternatives and reachable controls.
- RSVP requires persistent labels, grouped choices, server-authoritative validation, error recovery and truthful confirmation.
- Guest lookup must resist enumeration and enforce access server-side.
- Sensitive gift details require deliberate disclosure or verified access according to the contract.
- Provide calendar, directions, messaging and external actions only when their destinations are verified.

Lifecycle requirements:
- Support save-the-date, invitation announced, RSVP not open, RSVP open, deadline passed, upcoming, today, in progress, completed, post-event gallery and archive states.
- Never display “Today is the day” after the final event ends.
- After completion, replace RSVP/countdown urgency with thank-you, gallery or archive behaviour.

Responsive and accessibility requirements:
- Deliberately compose desktop, laptop, tablet when relevant and approximately 390×844 mobile.
- Protect portrait focal points and attire details.
- Use summaries before long biographies on mobile.
- Convert timelines to one clear chronological column.
- Support keyboard operation, visible focus, high zoom and reduced motion.
- All scroll-reveal content remains visible if JavaScript or animation initialisation fails.

Motion requirements:
- Choose one motion attitude and no more than five recurring primitives.
- Motion supports ceremony, anticipation, memory, hierarchy or feedback.
- Petals/confetti are decorative, pointer-transparent and disabled for reduced motion.
- Do not animate practical forms or details continuously.

Before handoff:
1. Run project tests, build, content validation and celebration-pack validation.
2. Render the page/state matrix required by accessibility-and-responsive.md.
3. Inspect desktop and mobile screenshots for clipping, unreadable overlays, cropped faces, text density, timeline order, sticky-header overlap, modal controls and privacy leakage.
4. Test future, today, in-progress and completed event instants.
5. Test RSVP default, error, submitting, confirmed and closed states.
6. Test guest-code and gift-detail states.
7. Test keyboard, focus, reduced motion and no-animation fallback.
8. Distinguish verified content, provisional content, private content, generated decoration, licensed media, real integrations and prototypes.
9. Provide truthful deployment or local-access instructions.

Reject the build as incomplete when it is merely romantic or visually attractive but lacks accurate event information, full lifecycle behaviour, privacy, accessible interactions, responsive content strategy or validation evidence.
```
