# Domain Pack Router

Domain packs extend the core AI UI Style Vault with product-specific page blueprints, components, state models, content rules, asset standards, code contracts, privacy requirements and implementation prompts.

Agents must follow `AGENTS.md` first. A domain pack adds requirements; it never replaces the core product-design, content-design, accessibility, asset, validation, originality or truthfulness rules.

For real businesses, product-domain selection happens only after `BUSINESS_RESEARCH.md` and `business-profile.json` establish what the business actually does. Validate the profile with `python scripts/validate-business-understanding.py <business-profile.json>` before design selection.

## Automatic routing

| Product or task | Required pack | Required task prompt |
|---|---|---|
| 3D, WebGL/WebGPU, Three.js/R3F/Babylon/Spline, configurator, showroom, digital twin, spatial portfolio, globe, AR or WebXR | `packs/3d-immersive-web/` plus matching product-domain pack | `prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md` |
| Fashion, couture, tailoring, bespoke atelier, corporate wear, kaftans, traditional wear, occasion wear or made-to-order fashion | `packs/fashion-couture/` | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| Accounting, audit, tax, legal, consulting, advisory, engineering consulting, architecture practice or other expertise-led professional services | `packs/professional-services/` | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| Property developer, estate agency, brokerage, residential/commercial property, property listings, off-plan or mixed-use development | `packs/real-estate/` | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| Wedding, Nikkah, engagement, anniversary, save-the-date, RSVP, couple story, gift registry, private celebration or post-event gallery | `packs/celebration-event-microsite/` | `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md` |
| Restaurant, food ordering, takeaway, delivery, menu, quick-service, fast-casual, cafe, bakery, or multi-branch food commerce | `packs/fast-casual-commerce/` | `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` |

The most specific route wins. The machine-readable router is `packs/pack-index.json`, and `scripts/plan-vault-build.py` provides business-profile-driven selection.

## Product-domain and capability packs

Select one product-domain pack and add capability packs when needed. A 3D couture site uses Fashion & Couture plus 3D & Immersive Web; a 3D property experience uses Real Estate plus 3D & Immersive Web only when a model/site/spatial interaction materially helps evaluation.

## Fashion & Couture Pack

Use `packs/fashion-couture/` for couture houses, bespoke tailors, fashion ateliers, corporate tailoring, kaftans, traditional wear, occasion wear and made-to-order fashion.

- Research the business before choosing luxury/editorial styling.
- Prioritise garment categories, craftsmanship, fit, material quality, process and enquiry/order conversion.
- Use official or owner-supplied garment photography first; generated media is concept-only and must not be presented as client work.
- Do not invent prices, lead times, delivery coverage, measurements, fabric origins, client lists or awards.
- If 3D is used, it must relate directly to garments, tailoring, textile/materials, atelier process or verified brand cues.
- Transform editorial layouts intentionally for mobile and preserve garment inspection and conversion with reduced motion.

Read all paths listed in the pack index before implementation.

## Professional Services Pack

Use `packs/professional-services/` for accounting, audit, tax, legal, consulting, advisory, engineering consulting, architecture practices and similar expertise-led firms.

- Lead with exact service scope, client fit, proof and engagement path—not generic consulting slogans.
- Never invent clients, awards, rankings, memberships, credentials, years in business, staff counts or case outcomes.
- Anonymous case studies must be clearly described as anonymised.
- Distinguish firm credentials from individual credentials.
- Keep regulated/legal/tax/financial statements current and sourceable.
- Use real team/process/project evidence where possible; stock/generated people are never staff or client proof.
- 3D is exceptional and must directly support the service, process, project, architecture, engineering object or verified data.

## Real Estate Pack

Use `packs/real-estate/` for property developers, estate agencies, brokerages, residential/commercial listings, off-plan projects and mixed-use developments.

- Keep location, property/development name, type, availability, price status, key specifications and enquiry/viewing action close to the primary media.
- Never invent prices, availability, dimensions, completion dates, title status, amenities, travel times, yields or financing terms.
- Distinguish actual photography from architectural CGI/renders, stock and generated illustrative media.
- Do not present stock homes as listed property or renders as completed reality.
- Avoid false scarcity unless connected to a current source of truth.
- Maps require textual location fallbacks; galleries and floorplans require keyboard/touch/mobile access.
- 3D property models must correspond to the actual project or be clearly labelled illustrative, with a static gallery/floorplan fallback.

## 3D & Immersive Web capability pack

**Semantic relevance is a hard gate.** Complete `THREE_D_RELEVANCE_CONTRACT.md` before asset selection. A 3D object, video or background must directly match the business/product/page purpose; unrelated spectacle is rejected.

Use `packs/3d-immersive-web/` for purposeful real-time depth, model inspection/configuration, camera storytelling, spatial worlds, digital twins, maps or AR/XR. Prove the need, compare simpler media, build the fallback first, keep controls/content in DOM, define capability tiers, measure budgets and record every asset licence. External galleries remain reference-only unless separate terms grant reuse.

## Celebration & Event Microsite Pack

Use the pack for wedding, Nikkah, engagement, anniversary, save-the-date, RSVP, couple story, gifting, private celebration, event-day and post-event lifecycle experiences. Follow its privacy, guest-access, media, lifecycle and content rules; never copy another couple's identity, photographs, story, financial information or exact layout.

## Fast-Casual Commerce Pack

Use the pack for branch-aware food menus, fulfilment selection, product configuration, cart, checkout, loyalty and tracking. Treat menu browsing and ordering as the product; keep products, prices, branch, fulfilment, availability and cart state visible and do not clone another food brand.

## Minimal invocation

```text
Use the AI UI Style Vault and automatically apply the appropriate domain pack.
Build a premium experience for: <COUPLE, EVENT, BUSINESS LINK OR BRIEF>.
Follow PACKS.md, PROMPTS.md and all required visual-QA steps.
```
