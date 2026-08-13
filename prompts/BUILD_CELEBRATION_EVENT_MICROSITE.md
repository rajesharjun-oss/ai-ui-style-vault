# Build a Premium Celebration & Couple Microsite

Use this prompt when the user asks for a wedding, Nikkah, engagement, anniversary, save-the-date, RSVP or private celebration website.

This prompt is mandatory together with `AGENTS.md`, `PRD.md`, `PACKS.md`, `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` when the project represents a real service or event brand, `prompts/VISUAL_QA_AND_REVISION.md`, and every required file in `packs/celebration-event-microsite/`.

## Role

Act as a coordinated:

- Senior event-experience product designer.
- Senior content and storytelling designer.
- Privacy-aware guest-journey designer.
- Senior brand-aware front-end engineer.
- Accessibility and visual-QA reviewer.

The goal is not to fill a generic wedding template. The goal is to create a deeply specific, accurate, culturally relevant, responsive and trustworthy experience for this couple or celebration.

## Phase 1 — Inspect and classify

1. Inspect the target repository, stack, routes, components, build commands and available integrations.
2. Read the vault root instructions and the complete Celebration & Event Microsite pack.
3. Determine whether the agent can research public event/vendor information, process user-supplied media, render a browser, capture screenshots and run tests.
4. Confirm whether the work is on the user's computer or in a remote environment.
5. Classify the site as public, public-summary/private-details, guest-code, authenticated-guest or fully private.

Do not code yet.

## Phase 2 — Gather verified event inputs

Create or complete:

- `EVENT_BUILD_CONTRACT.md`
- `COUPLE_CONTENT_PLAN.md`
- `ASSET_PLAN.md`

Document:

- Couple or host names and preferred order.
- Event type and approved public title.
- Dates, times and IANA timezone.
- Every event, venue, address and attendance scope.
- Guest rules, plus-one and children policy.
- Dress code and named colours.
- Couple profiles and relationship story.
- Faith and cultural terminology.
- RSVP opening, deadline and edit policy.
- Travel and accommodation information.
- Gift preferences and verification contact.
- Public/private content boundary.
- Post-event mode and retention plan.

Separate:

```text
verified-couple-content
requires-couple-confirmation
private-do-not-index
prototype-only
```

Do not invent names, dates, venues, family roles, relationship milestones, scriptures, prayers, bank details, dress-code colours, guest rules or travel arrangements.

## Phase 3 — Define the guest journey

Map the journey:

```text
arrival
→ identify event
→ understand date and place
→ review invitation-specific details
→ learn about couple/hosts when desired
→ RSVP or recover
→ plan travel/dress code
→ optional gifting
→ event-day information
→ post-event thank-you/gallery
```

Give every page one purpose and one primary action. Use only the page blueprints the event needs.

The homepage must answer who, what, when, where and what next without displaying the complete biography or story.

## Phase 4 — Define the full lifecycle

Use verified ISO instants and the event's IANA timezone. Define:

```text
save-the-date
invitation-announced
rsvp-not-open
rsvp-open
rsvp-deadline-passed
event-upcoming
event-today
event-in-progress
event-completed
post-event-gallery
site-archived
```

Test each state. Never leave the site saying “Today is the day” after the final event end. After completion, replace countdown and RSVP urgency with a thank-you, gallery or archive experience.

## Phase 5 — Define privacy and integrations

Classify every capability:

```text
verified-and-integrated
design-only-prototype
requires-integration
requires-host-confirmation
out-of-scope
```

Cover:

- Guest lookup.
- RSVP persistence.
- Email, SMS or WhatsApp confirmation.
- Maps and directions.
- Calendar download.
- Media hosting.
- Guest uploads.
- Gift registry.
- Protected financial details.
- Analytics.

Guest lookup must resist enumeration and use server-side authorisation. Do not download the guest list to the browser. Do not show a success confirmation until the RSVP source of truth accepts the response.

Sensitive gift, travel, contact and media information must follow the privacy model. `noindex` is not an access-control mechanism.

## Phase 6 — Select the design direction

Create `VAULT_SELECTION.md` and `design-recipe.json`.

1. Choose one production theme from the pack.
2. Choose one primary style bundle from the vault.
3. Add only page-specific references that solve a clear gap.
4. Derive colour and material direction from approved attire, stationery, venue or décor.
5. Choose one motion attitude and no more than five recurring motion primitives.
6. Explain how the direction reflects the actual couple, culture, faith, venue and photographs.
7. State what will be adapted and what will not be copied.

Do not default every couple to burgundy, script typography, petals or the same timeline.

## Phase 7 — Plan media

For every major photograph or video, record:

- Source and creator.
- Consent and licence.
- Public or private access.
- Purpose.
- Focal point.
- Desktop and mobile crop.
- Alt text and caption.
- Format and performance treatment.
- Download permission.
- Retention plan.

Use user-provided, host-provided or licensed couple media. Never present generated people as the couple, relatives or guests. Generated assets may support decorative florals, patterns and textures when clearly recorded as conceptual.

## Phase 8 — Implement

Implementation order:

1. Data, privacy and lifecycle contracts.
2. Semantic design tokens.
3. Site shell and accessible navigation.
4. Event identity and status.
5. Event details and guest actions.
6. Couple/story content with progressive disclosure.
7. Gallery and accessible media dialogs.
8. RSVP and recovery states.
9. Travel, FAQ and optional gifting.
10. Responsive transformations.
11. Purposeful motion and reduced-motion fallback.
12. Post-event mode.
13. Performance and security hardening.

### Required engineering behaviour

- Use semantic HTML, labels, fieldsets, legends, dialog semantics and visible focus.
- Keep scroll-reveal content visible if JavaScript fails.
- Protect portrait focal points and attire details across breakpoints.
- Use responsive media and explicit dimensions.
- Preserve form values after validation or network failure.
- Use a trusted server clock for protected lifecycle and RSVP behaviour.
- Enforce guest limits and protected-resource access server-side.
- Do not expose invitation codes, guest names, RSVP values or gifting details to analytics.
- Support reduced motion and no-animation fallback.

## Phase 9 — Rendered visual and state QA

After the first render, execute `prompts/VISUAL_QA_AND_REVISION.md` and the matrix in the pack's accessibility guide.

At minimum inspect:

- Homepage on desktop, laptop and mobile.
- Upcoming, RSVP-open, event-today, in-progress and completed states.
- Meet-the-couple mobile content density.
- Story timeline order on desktop and mobile.
- Gallery, lightbox and video dialog.
- RSVP default, validation error, submitting, confirmed and closed.
- Guest-code required and invalid.
- Gift details hidden and revealed.
- Mobile menu open.
- Reduced-motion and no-animation fallback.
- Long names, long venues, translated copy and high zoom.

Correct clipping, sticky-header overlap, unreadable text over media, cropped faces, excessive prose, inaccessible controls, privacy leakage and stale lifecycle copy before handoff.

## Phase 10 — Validation and handoff

Run available:

- Lint.
- Typecheck.
- Unit and integration tests.
- Production build.
- Core content/design validator.
- `python scripts/validate-celebration-pack.py` in the vault.
- Accessibility checks.
- Link and browser-console checks.
- Media and consent audit.

Final handoff must include:

- What was built.
- Verified, provisional and private content.
- Selected theme, style references and pack.
- Media provenance and consent status.
- Implemented lifecycle and RSVP states.
- Integrated versus prototype-only capabilities.
- Desktop and mobile screenshots.
- Commands and checks run.
- Truthful local or deployed access instructions.
- Retention, post-event and owner-confirmation items.

## Reject conditions

Do not report completion when:

- The site is a generic romantic template.
- Personal facts or event details were invented.
- The homepage is packed with biographies or story text.
- Event-day logic remains active after completion.
- Gallery/video controls are clickable non-semantic elements.
- Reduced-motion or no-animation users lose content.
- RSVP confirmation is simulated as real.
- Guest lookup exposes or downloads the guest list.
- Sensitive gifting or private media is publicly exposed contrary to the contract.
- Mobile layouts crop faces, hide actions or create walls of text.
- The site has not been rendered and revised.
