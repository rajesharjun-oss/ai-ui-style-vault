# Celebration & Event Microsite Pack

This domain pack helps AI coding agents create original, premium and privacy-aware websites for weddings, Nikkah ceremonies, engagements, anniversaries, birthdays, graduations, memorials and invitation-only celebrations.

It translates the useful principles of strong event websites—personal photography, culturally relevant art direction, clear event details, storytelling, galleries, RSVP flows and atmospheric motion—into reusable product, content and engineering contracts. It is not permission to copy another couple's photographs, identity, story, financial details, wording, page composition or proprietary assets.

## Use this pack when

- Building a wedding, Nikkah, engagement or anniversary website.
- Creating a save-the-date or invitation microsite.
- Presenting couple profiles, a relationship story or an event timeline.
- Publishing ceremony, reception, dress-code, venue or travel information.
- Implementing guest lookup, RSVP, confirmation or attendance management.
- Supporting gift registries, protected gifting or physical-gift coordination.
- Transitioning to a post-event thank-you, gallery or memories website.

## Required experience model

Design the complete event lifecycle rather than only the attractive pre-event homepage:

```text
save-the-date
→ invitation announced
→ RSVP not open
→ RSVP open
→ RSVP closed
→ event upcoming
→ event today / in progress
→ event completed
→ post-event gallery
→ archived
```

Never leave a site displaying “Today is the day” after the event has passed. Every event date must use an explicit IANA timezone and the interface must define future, same-day, in-progress and completed states.

## Read order

1. `pack.json`
2. `production-themes.json`
3. `page-blueprints.json`
4. `component-manifest.json`
5. `state-vocabulary.json`
6. `content-and-storytelling.md`
7. `photography-and-video-standard.md`
8. `privacy-and-guest-access.md`
9. `accessibility-and-responsive.md`
10. `motion-guidance.md`
11. `implementation-prompt.md`
12. `schemas/`, `code/`, `sample-data/` and `templates/`

Also follow the repository-level `AGENTS.md`, `PROMPTS.md`, `PACKS.md`, senior product-team protocol and rendered visual-QA prompt.

## Required planning artifacts

Before implementation, complete equivalents of:

- `EVENT_BUILD_CONTRACT.md`
- `COUPLE_CONTENT_PLAN.md`
- `ASSET_PLAN.md`
- `VAULT_SELECTION.md`
- `BUILD_CONTRACT.md`
- `CONTENT_PLAN.md`
- `design-recipe.json`

When RSVP, guest lookup, gifting or private media are included, classify every capability as:

```text
verified-and-integrated
design-only-prototype
requires-integration
requires-host-confirmation
out-of-scope
```

## Non-negotiable rules

- Do not invent names, dates, venues, guest rules, family details, personal stories, bank details or travel information.
- Do not present generated people as the real couple.
- Use user-provided, owned or clearly licensed couple photographs and videos.
- Generated media may support florals, patterns, textures or abstract backgrounds, but it must not impersonate the couple or venue.
- Keep the homepage concise; route biographies, timelines and long practical information to dedicated pages or progressive disclosure.
- Use semantic buttons and accessible dialogs for galleries and videos.
- Support keyboard operation, visible focus, reduced motion and a no-animation content fallback.
- Protect guest information, gifting details and private media according to the selected privacy model.
- Make post-event behaviour explicit.
- Build an original experience adapted to the couple, culture, faith, event type, venue and available photography.

## Minimal invocation

```text
Use the AI UI Style Vault and automatically apply the Celebration & Event Microsite pack.
Build a premium Nikkah and wedding-reception website for this couple using the supplied content and media.
Follow PACKS.md, PROMPTS.md and the rendered visual-QA workflow.
```
