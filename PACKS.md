# Domain Pack Router

Domain packs extend the core AI UI Style Vault with product-specific page blueprints, components, state models, content rules, asset standards, code contracts, privacy requirements and implementation prompts.

Agents must follow `AGENTS.md` first. A domain pack adds requirements; it never replaces the core product-design, content-design, accessibility, asset, validation, originality or truthfulness rules.

## Automatic routing

| Product or task | Required pack | Required task prompt |
|---|---|---|
| Wedding, Nikkah, engagement, anniversary, save-the-date, RSVP, couple story, gift registry, private celebration or post-event gallery | `packs/celebration-event-microsite/` | `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md` |
| Restaurant, food ordering, takeaway, delivery, menu, quick-service, fast-casual, cafe, bakery, or multi-branch food commerce | `packs/fast-casual-commerce/` | `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` |

The most specific route wins. The machine-readable router is `packs/pack-index.json`.

## Celebration & Event Microsite Pack

Use the pack when the product needs any combination of:

- Wedding, Nikkah, engagement, anniversary or save-the-date presentation.
- Couple or host profiles and a relationship/event story.
- Multi-event schedules, venues, directions, dress code or travel guidance.
- Personal photo galleries, proposal/engagement video or post-event media.
- Guest-code access, invitation-specific details or private media.
- RSVP, confirmation, response editing or deadline states.
- Optional gift registry, protected gifting or physical-gift coordination.
- Event lifecycle from announcement through post-event gallery and archive.

Read in this order:

1. `packs/celebration-event-microsite/pack.json`
2. `packs/celebration-event-microsite/production-themes.json`
3. `packs/celebration-event-microsite/page-blueprints.json`
4. `packs/celebration-event-microsite/component-manifest.json`
5. `packs/celebration-event-microsite/state-vocabulary.json`
6. `packs/celebration-event-microsite/content-and-storytelling.md`
7. `packs/celebration-event-microsite/photography-and-video-standard.md`
8. `packs/celebration-event-microsite/privacy-and-guest-access.md`
9. `packs/celebration-event-microsite/accessibility-and-responsive.md`
10. `packs/celebration-event-microsite/motion-guidance.md`
11. `packs/celebration-event-microsite/implementation-prompt.md`
12. `packs/celebration-event-microsite/code/`, `schemas/`, `sample-data/` and `templates/`

### Celebration selection rules

- Derive the design from verified couple/host content, culture, faith, venue, attire and approved media.
- Do not default every event to burgundy, scripts, petals or the same timeline.
- Do not invent names, stories, dates, venues, guest rules, quotations, financial details or travel arrangements.
- Do not present generated people as the actual couple, relatives or guests.
- Keep the homepage concise; progressively disclose biographies and long story chapters.
- Define the entire lifecycle, including event completion and post-event mode.
- Protect guest data, private media and gifting details according to a selected privacy model.
- Use semantic gallery/video controls, real form states, reduced-motion support and a no-animation content fallback.
- Never copy another couple's photographs, personal story, wording, financial information, exact layout or proprietary assets.

## Fast-Casual Commerce Pack

Use the pack when the product needs any combination of:

- Branch-aware menus and opening status.
- Delivery, pickup, dine-in, or takeaway selection.
- Product categories, visible prices, availability, and modifiers.
- Product customisation, quantity, cart, coupons, checkout, or payments.
- Deals, loyalty, order confirmation, and order tracking.
- Delivery-zone or service-area checks.

Read in this order:

1. `packs/fast-casual-commerce/pack.json`
2. `packs/fast-casual-commerce/production-theme.json`
3. `packs/fast-casual-commerce/page-blueprints.json`
4. `packs/fast-casual-commerce/component-manifest.json`
5. `packs/fast-casual-commerce/state-vocabulary.json`
6. `packs/fast-casual-commerce/content-and-merchandising.md`
7. `packs/fast-casual-commerce/food-photography-standard.md`
8. `packs/fast-casual-commerce/accessibility-and-responsive.md`
9. `packs/fast-casual-commerce/implementation-prompt.md`
10. `packs/fast-casual-commerce/code/` and `packs/fast-casual-commerce/templates/`

### Commerce selection rules

- Use one primary visual system and adapt it to the business.
- Treat menu browsing and ordering as the main product journey, not as a decorative section below a marketing hero.
- Keep products, prices, service mode, branch, availability, and cart status close to the user.
- Use realistic, consistently art-directed product photography unless the brief explicitly requests illustration.
- Do not clone Dodo Pizza or another food brand. Do not copy logos, proprietary code, exact page composition, product text, photography, promotions, or checkout flows.
- Use the pack as an original commerce architecture and interaction system.

## Minimal invocation

```text
Use the AI UI Style Vault and automatically apply the appropriate domain pack.
Build a premium experience for: <COUPLE, EVENT, BUSINESS LINK OR BRIEF>.
Follow PACKS.md, PROMPTS.md and all required visual-QA steps.
```
