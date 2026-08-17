# Domain Pack Router

Domain packs extend the core AI UI Style Vault with product-specific page blueprints, components, state models, content rules, asset standards, code contracts, privacy requirements and implementation prompts.

Agents must follow `AGENTS.md` first. A domain pack adds requirements; it never replaces the core product-design, content-design, accessibility, asset, validation, originality or truthfulness rules.

For real businesses, product-domain selection happens only after `BUSINESS_RESEARCH.md` and `business-profile.json` establish what the business actually does. Validate the profile with `python scripts/validate-business-understanding.py <business-profile.json>` before design selection.

## Automatic routing

| Product or task | Required pack | Required task prompt |
|---|---|---|
| 3D, WebGL/WebGPU, Three.js/R3F/Babylon/Spline, configurator, showroom, digital twin, spatial portfolio, globe, AR or WebXR | `packs/3d-immersive-web/` plus matching product-domain pack | `prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md` |
| Fashion, couture, tailoring, bespoke atelier, corporate wear, kaftans, traditional wear, occasion wear or made-to-order fashion | `packs/fashion-couture/` | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| Wedding, Nikkah, engagement, anniversary, save-the-date, RSVP, couple story, gift registry, private celebration or post-event gallery | `packs/celebration-event-microsite/` | `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md` |
| Restaurant, food ordering, takeaway, delivery, menu, quick-service, fast-casual, cafe, bakery, or multi-branch food commerce | `packs/fast-casual-commerce/` | `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` |

The most specific route wins. The machine-readable router is `packs/pack-index.json`.

## Product-domain and capability packs

Select one product-domain pack and add capability packs when needed. A 3D couture site uses Fashion & Couture plus 3D & Immersive Web; a 3D restaurant configurator uses Fast-Casual Commerce plus 3D & Immersive Web.

## Fashion & Couture Pack

Use `packs/fashion-couture/` for couture houses, bespoke tailors, fashion ateliers, corporate tailoring, kaftans, traditional wear, occasion wear and made-to-order fashion.

Read in this order:

1. `packs/fashion-couture/pack.json`
2. `packs/fashion-couture/production-themes.json`
3. `packs/fashion-couture/page-blueprints.json`
4. `packs/fashion-couture/component-manifest.json`
5. `packs/fashion-couture/state-vocabulary.json`
6. `packs/fashion-couture/content-and-merchandising.md`
7. `packs/fashion-couture/photography-and-material-standard.md`
8. `packs/fashion-couture/motion-guidance.md`
9. `packs/fashion-couture/accessibility-and-responsive.md`
10. `packs/fashion-couture/implementation-prompt.md`
11. `packs/fashion-couture/templates/FASHION_BUILD_CONTRACT.md`

### Fashion selection rules

- Research the business before choosing luxury/editorial styling.
- Prioritise garment categories, craftsmanship, fit, material quality, process and enquiry/order conversion.
- Use official or owner-supplied garment photography first; generated media is concept-only and must not be presented as client work.
- Do not invent prices, lead times, delivery coverage, measurements, fabric origins, client lists or awards.
- If 3D is used, it must relate directly to garments, tailoring, textile/materials, atelier process or verified brand cues.
- Do not treat fashion as permission for unrelated cars, jewellery, architecture or futuristic spectacle.
- Transform editorial layouts intentionally for mobile and preserve garment inspection and conversion with reduced motion.

## 3D & Immersive Web capability pack

**Semantic relevance is a hard gate.** Complete `THREE_D_RELEVANCE_CONTRACT.md` before asset selection. A 3D object, video or background must directly match the business/product/page purpose; unrelated spectacle is rejected.

Use `packs/3d-immersive-web/` for purposeful real-time depth, model inspection/configuration, camera storytelling, spatial worlds, digital twins, maps or AR/XR. Read `pack.json`, all required reads, `3d/source-catalog.json`, `3d/techniques/` and `3d/references/`.

Prove the need, compare simpler media, build the fallback first, keep controls/content in DOM, define capability tiers, measure budgets and record every asset licence. Refs.Gallery, MotionSites and other galleries are reference-only unless separate terms grant reuse.

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
