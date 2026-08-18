# Domain Pack Router

Domain packs extend the core AI UI Style Vault with product-specific page blueprints, components, state models, content rules, asset standards, code contracts, privacy requirements and implementation prompts.

Agents must follow `AGENTS.md` first. A domain pack adds requirements; it never replaces the core product-design, content-design, accessibility, asset, validation, originality or truthfulness rules.

For real businesses, product-domain selection happens only after `BUSINESS_RESEARCH.md` and `business-profile.json` establish what the business actually does. Validate the profile with `python scripts/validate-business-understanding.py <business-profile.json>` before design selection.

## Automatic routing

| Product or task | Required pack | Required task prompt |
|---|---|---|
| 3D, WebGL/WebGPU, Three.js/R3F/Babylon/Spline, configurator, showroom, digital twin, spatial portfolio, globe, AR or WebXR | `packs/3d-immersive-web/` plus matching product-domain pack | `prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md` |
| Fashion, couture, tailoring, bespoke atelier, corporate wear, kaftans, traditional wear, occasion wear or made-to-order fashion | `packs/fashion-couture/` | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| Beauty salon, spa, barber, grooming, skincare/aesthetic clinic, nail or wellness studio | `packs/beauty-wellness/` | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| Hotel, resort, serviced apartment, guest house, lodge or accommodation-led hospitality | `packs/hospitality/` | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| SaaS, software platform, AI product, developer tool, API platform, workflow or enterprise software | `packs/saas-technology/` | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| Accounting, audit, tax, legal, consulting, advisory, architecture or engineering consulting | `packs/professional-services/` | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| Property developer, estate agency, brokerage, residential/commercial listings or off-plan development | `packs/real-estate/` | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| Wedding, Nikkah, engagement, anniversary, save-the-date, RSVP, couple story, gift registry, private celebration or post-event gallery | `packs/celebration-event-microsite/` | `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md` |
| Restaurant, food ordering, takeaway, delivery, menu, quick-service, fast-casual, cafe, bakery, or multi-branch food commerce | `packs/fast-casual-commerce/` | `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` |

The most specific route wins. The machine-readable router is `packs/pack-index.json`.

## Product-domain and capability packs

Select one product-domain pack and add capability packs when needed. A 3D couture site uses Fashion & Couture plus 3D & Immersive Web; a hotel virtual tour uses Hospitality plus 3D & Immersive Web; an interactive software topology may use SaaS & Technology plus 3D only when the visualisation is semantically justified.

## Beauty & Wellness Pack

Use `packs/beauty-wellness/` for salons, spas, barbers, skincare/aesthetic clinics, nail studios, makeup studios and appointment-led wellness businesses.

Prioritise service clarity, practitioner trust, verified pricing/duration where available, booking path, location/policies and consented work/results. Never invent medical outcomes, qualifications, prices, before-and-after results or booking availability. Generated people cannot be presented as real clients or staff.

## Hospitality Pack

Use `packs/hospitality/` for hotels, resorts, serviced apartments, guest houses, lodges and accommodation-led businesses.

Prioritise rooms, real property media, location, capacity, amenities, rate/availability status, stay policies and booking. Never infer amenities from category or present stock/generated rooms as the property. Distinguish live booking integration, external booking and prototype availability.

## SaaS & Technology Pack

Use `packs/saas-technology/` for software, SaaS, AI products, developer tools, API platforms, workflow systems and enterprise technology.

Show the product workflow rather than relying on generic technology aesthetics. Never fabricate dashboards, customers, metrics, pricing, integrations, uptime, certifications or security posture. Mark beta, planned and conceptual functionality clearly. Abstract gradients, chrome blobs and 3D objects are not product proof.

## Professional Services Pack

Use `packs/professional-services/` for trust-heavy expertise businesses. Prioritise service scope, client fit, people, credentials, evidence and a credible engagement path. Do not invent clients, outcomes, rankings, awards or qualifications.

## Real Estate Pack

Use `packs/real-estate/` for developers, brokerages and property listings. Keep property facts, media provenance, location, price/availability status, floorplans and viewing/enquiry paths explicit. Distinguish photography, CGI, stock and generated media.

## Fashion & Couture Pack

Use `packs/fashion-couture/` for couture houses, bespoke tailors, fashion ateliers, corporate tailoring, kaftans, traditional wear, occasion wear and made-to-order fashion. Prioritise garments, craftsmanship, materials, fit and enquiry/order conversion; generated fashion media is concept-only unless explicitly owner-approved as such.

## 3D & Immersive Web capability pack

**Semantic relevance is a hard gate.** Complete `THREE_D_RELEVANCE_CONTRACT.md` before asset selection. A 3D object, video or background must directly match the business/product/page purpose; unrelated spectacle is rejected.

Use `packs/3d-immersive-web/` for purposeful real-time depth, model inspection/configuration, camera storytelling, spatial worlds, digital twins, maps or AR/XR. Prove the need, compare simpler media, build the fallback first, keep controls/content in DOM, define capability tiers, measure budgets and record every asset licence.

## Celebration & Event Microsite Pack

Use the pack for wedding, Nikkah, engagement, anniversary, save-the-date, RSVP, couple story, gifting, private celebration, event-day and post-event lifecycle experiences. Follow its privacy, guest-access, media, lifecycle and content rules.

## Fast-Casual Commerce Pack

Use the pack for branch-aware food menus, fulfilment selection, product configuration, cart, checkout, loyalty and tracking. Treat menu browsing and ordering as the product and do not clone another food brand.

## Minimal invocation

```text
Use the AI UI Style Vault and automatically apply the appropriate domain pack.
Build a premium experience for: <COUPLE, EVENT, BUSINESS LINK OR BRIEF>.
Follow PACKS.md, PROMPTS.md and all required visual-QA steps.
```
