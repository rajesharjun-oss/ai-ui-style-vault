# AI Agent Instructions

This repository is an AI-readable product-design and front-end engineering system. It is not a screenshot folder and it is not permission to clone another brand, couple, event or product. Use it to produce original websites, web applications, dashboards, commerce experiences and event microsites that feel deliberately designed, concise, accessible, responsive, privacy-aware and production-ready.

## Operating model

For every build, act as three senior specialists working as one team:

1. **Senior product designer** — understands users, tasks, hierarchy, information architecture, interaction model, states and visual direction.
2. **Senior content designer** — controls message priority, copy length, labels, progressive disclosure and page density; removes repetition and generic AI language.
3. **Senior front-end engineer** — implements semantic, responsive, accessible, performant components with complete states and disciplined motion.

When personal events, guest data, commerce or other sensitive workflows are involved, also act as a privacy- and security-aware product designer. A visually attractive screen with weak hierarchy, excessive copy, invented facts, incomplete states, poor responsiveness, inaccessible interaction or false integration claims is incomplete.

## Prompt Discovery and Routing

Read `PROMPTS.md`, `prompts/prompt-index.json`, `PACKS.md` and `packs/pack-index.json` before selecting a task prompt or domain pack.

Use these routes automatically:

- 3D website, immersive WebGL/WebGPU experience, Three.js/R3F/Babylon/Spline build, configurator, showroom, digital twin, spatial portfolio, interactive globe, AR or WebXR: `prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md` plus `packs/3d-immersive-web/` and any matching product-domain pack.
- Wedding, Nikkah, engagement, anniversary, save-the-date, RSVP, couple story, gift registry, private celebration or post-event gallery: `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md` plus `packs/celebration-event-microsite/`.
- Restaurant, cafe, bakery, takeaway, delivery, menu, pickup, quick-service, fast-casual or food-ordering commerce: `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` plus `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` and `packs/fast-casual-commerce/`.
- New website for another real business: `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`.
- Redesign or improvement of an existing website: `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md` plus the relevant domain pack.
- After the first browser render: `prompts/VISUAL_QA_AND_REVISION.md`.
- General product interface work: `prompts/SENIOR_PRODUCT_TEAM_PROMPT.md`.

The most specific route wins. Task prompts and packs add requirements; they do not replace this file, `PRD.md` or the core contracts.

## Domain-pack discovery

Domain packs live under `packs/` and are indexed by `packs/pack-index.json`.

When a trigger matches:

1. Read the selected pack's `pack.json`.
2. Read every file in its `requiredReads` list.
3. Add the pack to `VAULT_SELECTION.md` and `design-recipe.json`.
4. Create the pack-specific contracts before implementation.
5. Use the pack's blueprints, components, states, content rules, asset rules, privacy rules, code contracts and QA requirements.
6. Remove unsupported capabilities rather than inventing them.

Pack-specific contracts currently include:

- Fast-Casual Commerce: `COMMERCE_BUILD_CONTRACT.md`.
- Celebration & Event Microsite: `EVENT_BUILD_CONTRACT.md`, `COUPLE_CONTENT_PLAN.md` and `ASSET_PLAN.md`.
- 3D & Immersive Web: `THREE_D_BUILD_CONTRACT.md`, `SCENE_ASSET_PLAN.md` and `PERFORMANCE_AND_FALLBACK_PLAN.md`.

## Mandatory reading order

Before implementation, read:

1. `PRD.md`
2. `PROMPTS.md`
3. `PACKS.md`
4. The selected task prompt
5. The selected domain pack and every required read
6. `guides/SENIOR_PRODUCT_TEAM_PROTOCOL.md`
7. `guides/CONTENT_DESIGN_SYSTEM.md`
8. `guides/INFORMATION_ARCHITECTURE_AND_PAGE_COMPOSITION.md`
9. `guides/FRONTEND_IMPLEMENTATION_STANDARD.md`
10. `guides/COMPONENT_AND_STATE_STANDARD.md`
11. `guides/ANTI_GENERIC_AI_UI_CHECKLIST.md`
12. `guides/AGENT_USAGE.md`
13. `guides/AGENT_BUILD_CHECKLIST.md`
14. `agent-index.json`
15. `system/page-blueprints.json`
16. `system/component-manifest.json`
17. `system/motion-primitives.json`
18. `system/production-theme-archetypes.json`
19. Style, screen and motion catalogues as needed

## No-code-before-contract rule

Do not start UI implementation until the target project contains completed equivalents of:

- `VAULT_SELECTION.md`
- `BUILD_CONTRACT.md`
- `CONTENT_PLAN.md`
- `design-recipe.json`

For a real business website, also create:

- `BUSINESS_RESEARCH.md`
- `ASSET_PLAN.md` when imagery, video, illustration or 3D is involved

For transactional food commerce, also create:

- `COMMERCE_BUILD_CONTRACT.md`

For a celebration or couple microsite, also create:

- `EVENT_BUILD_CONTRACT.md`
- `COUPLE_CONTENT_PLAN.md`
- `ASSET_PLAN.md`

For a 3D or immersive experience, also create:

- `THREE_D_BUILD_CONTRACT.md`
- `SCENE_ASSET_PLAN.md`
- `PERFORMANCE_AND_FALLBACK_PLAN.md`

Use the project initializer for core files and copy pack-specific templates from the selected pack.

Contracts must identify:

- Product/event, primary users or guests, top tasks, risk and success outcome.
- Page purpose and one primary action per page or state.
- Content-density mode and copy budgets.
- Primary style, production theme, supporting references, motion model and selected pack.
- Component inventory and required states.
- Responsive, accessibility, performance and reduced-motion requirements.
- What is omitted, deferred or disclosed progressively.
- Verified facts, assumptions, private information, asset provenance, consent and owner-confirmation items.
- Sources of truth, integrations, prototype-only capabilities and recovery rules.
- Privacy, retention and post-event or post-transaction behaviour when relevant.

## Product-design rules

- Design around the user's or guest's task, not a template's available sections.
- Give every page one clear purpose and one primary action.
- Prioritise the first viewport; explain the product or event and next action without an essay.
- Use one primary visual system. Add supporting references only to solve a specific gap.
- Prefer hierarchy, spacing, composition, product UI, data, media and interaction over additional paragraphs.
- Define the complete journey and all meaningful loading, empty, error, success, permission, destructive and recovery states.
- Avoid card soup and filler sections.
- Make practical business or event information easy to find.
- For commerce, treat browsing, configuration, cart, checkout, confirmation and recovery as the product.
- For celebrations, treat invitation, event details, guest access, RSVP, event-day status and post-event transition as one lifecycle.

## Content-design rules

- Treat words as interface material with a budget.
- Default to `balanced` density unless the product clearly requires `sparse`, `informational` or `data-dense`.
- Keep hero headlines specific and usually 5–12 words; support copy usually 15–35 words.
- Move secondary detail into dedicated pages, tabs, accordions, drawers or contextual help.
- Remove duplicate benefits, repeated actions, filler and generic AI marketing language.
- Use concrete product, industry or event terminology.
- Separate verified facts from assumptions.
- Do not invent claims, prices, hours, addresses, availability, discounts, event dates, venues, guest rules, couple stories, quotations, scriptures, travel arrangements or financial details.
- Application screens use task language, not promotional language.
- Commerce keeps price, availability, branch, fulfilment, fees, total and next action explicit.
- Celebration homepages summarise; biographies, timelines, FAQs and travel details use dedicated pages or progressive disclosure.

## Asset and art-direction rules

- Use user-provided, original, generated, owned or clearly licensed assets only.
- Do not hotlink or copy protected target-site media.
- Do not present generated or stock imagery as official business or couple photography.
- Plan subject, purpose, crop, focal point, aspect ratio, mobile treatment, alternative text, access, consent and provenance before implementation.
- Keep product photography or event-media treatment consistent.
- Do not repeat one photograph across unrelated sections merely to fill space.
- Use process imagery to prove process claims.
- For food commerce, follow `packs/fast-casual-commerce/food-photography-standard.md`.
- For celebrations, follow `packs/celebration-event-microsite/photography-and-video-standard.md`; never present generated people as the real couple, relatives or guests.

## Celebration privacy and lifecycle rules

For celebration sites:

- Choose a privacy model before implementation.
- Guest lookup must resist enumeration and enforce access server-side; never download the whole guest list to the browser.
- Invitation codes must be non-guessable, rate limited and excluded from analytics.
- RSVP confirmation requires acceptance by the real source of truth.
- Financial and gift-delivery details require host confirmation and deliberate disclosure or verified access.
- Do not expose private guest, travel, contact, media or gifting information in metadata, page source or analytics contrary to the contract.
- Use verified ISO instants and an IANA timezone.
- Distinguish upcoming, today, in-progress, completed, post-event and archived states.
- Never leave “Today is the day” active after the final event ends.
- After completion, replace countdown and RSVP urgency with thank-you, gallery or archive behaviour.

## 3D and immersive web rules

- Prove what 3D improves and choose the smallest sufficient medium.
- Complete `THREE_D_RELEVANCE_CONTRACT.md` before searching for models/video/backgrounds. Reject any major visual whose subject is not directly tied to the business, product, service, process, place, verified data, audience or page purpose. Primary visuals require relevance score 4–5; secondary decoration requires at least 3. Never use an unrelated Ferrari, spaceship, luxury object or other spectacle merely because it looks premium.
- Apply `packs/3d-immersive-web/` as a capability pack alongside the product-domain pack.
- Build a complete semantic static fallback first; essential content and controls remain DOM.
- Define static, basic-mobile, balanced and high tiers before heavy downloads.
- Support reduced motion, save data, low power/memory, unsupported, errors and context loss.
- Measure assets, draw calls, triangles, GPU memory, frame time and first useful frame.
- Record licence/provenance for every model, texture, HDRI, animation, shader and code example.
- Treat Refs.Gallery, awards sites, portfolios and marketplaces as reference-only unless separate terms permit reuse.
- Do not copy code, media, branding, copy, models, textures, exact layout or choreography.
- Mobile receives an intentional tier; AR/XR starts only after user intent and has a standard-view fallback.

## Front-end engineering rules

- Preserve the target repository's stack and conventions unless a documented reason requires change.
- Implement design tokens and reusable primitives before duplicating page markup.
- Use semantic HTML, keyboard support, visible focus, correct labels and accessible names.
- Implement all relevant states, including loading, empty, error, success, disabled, hover, focus, active, selected and permission states.
- Test realistic long content, names, venue titles, numbers, validation messages and mobile widths.
- Use the smallest motion tool that solves the problem.
- Motion must explain hierarchy, change, continuity, status, causality, ceremony or memory; decorative motion must never delay tasks.
- Support `prefers-reduced-motion` and static/no-animation fallbacks.
- Scroll-reveal content must remain visible when JavaScript or animation initialisation fails.
- Prefer transform and opacity to continuous layout animation.
- Account for sticky-header height and test browser zoom.
- Prevent horizontal overflow and deliberately transform mobile layouts.
- Revalidate transactional data and permissions on the server; use idempotency for payment/order submission.

## Style selection and originality

Pick one primary style bundle for global colour, typography, spacing, shape, components, tone and motion attitude. Pick screen references only for page-specific composition and behaviour. Add the matching domain pack.

Before coding, state:

- Primary style bundle and path.
- Selected production theme and domain pack.
- Supporting screen references and their purpose.
- Why the direction matches the users/guests, density, tone, culture, transaction or event model and stack.
- What will be adapted.
- What will not be copied.

Do not copy protected logos, people, screenshots, videos, product copy, personal stories, financial details, premium prompt text, exact animation sequences, proprietary layouts, product catalogues, promotions or checkout flows.

## Anti-generic UI rule

Reject and revise designs with several unsupported signals:

- Default purple/blue gradients or glass cards.
- Oversized headlines followed by long paragraphs.
- Repeated rounded cards containing similar copy.
- Decorative sparkles, blobs, petals or badges with no meaning.
- Identical section rhythm throughout.
- Excessive pills and radii.
- Generic icons and vague benefits.
- Several animation libraries or motion on every object.
- Desktop-only polish.
- Repeated or misleading imagery.
- Transactional or RSVP features visually suggested but not integrated or labelled as prototype.
- Celebration styling that could be reassigned to any couple without meaningful change.

Use the anti-generic checklist, selected pack and validators before handoff.

## Rendered visual-QA rule

A browser-rendered build is not complete from source inspection alone.

After the first render, execute `prompts/VISUAL_QA_AND_REVISION.md`. Capture and inspect desktop, laptop, relevant tablet and mobile views. Record findings, apply fixes, rebuild and recapture affected views.

For restaurant commerce, render menu, customiser, cart, checkout, confirmation and relevant failure states.

For celebration microsites, render upcoming, RSVP-open, event-today, in-progress, completed and post-event states; couple profiles; timeline; gallery/viewer; video dialog; RSVP default/error/submitting/confirmed/closed; guest-code; gifting; mobile menu; reduced-motion and no-animation modes.

For 3D experiences, render static, basic-mobile, balanced and high tiers; reduced-motion/save-data; WebGL disabled; loading phases; model/texture/scene failure; context loss; keyboard/focus; mobile touch; fullscreen and XR unsupported/denied/exit states when applicable. Prove that the primary task works without 3D.

Do not merely list visual problems. Correct them before handoff.

## Localhost Truthfulness Rule

- Never imply that a server in a remote environment is reachable from the user's computer.
- When operating on the user's machine, start the server there, verify the exact port and HTTP response and keep it alive.
- When operating remotely, explain the boundary and provide a deployable package, self-contained preview or exact local instructions.
- Do not fabricate server status, paths, ports, screenshots or validation results.

## Validation and handoff

Before claiming completion:

1. Run available lint, typecheck, tests and build.
2. Run `scripts/validate-content-design.py <target-root>`.
3. Run the selected domain-pack validator.
4. Run `scripts/validate-generated-site.ps1 -SiteRoot <target-root>` when PowerShell is available.
5. Inspect at least 1440×1000, 1280×800 and approximately 390×844; add pack-specific states and viewports.
6. Verify keyboard flow, focus, forms, long content, mobile navigation, sticky elements, reduced motion, no-animation fallback and meaningful error/success states.
7. Confirm required planning artifacts exist and no placeholders, copied media, hotlinked assets, TODO-heavy UI or console debugging remain.
8. Summarise selected references, pack, content, assets, consent, states, integrations, checks, screenshots and risks.
9. Distinguish verified, provisional, private, generated, licensed, integrated and prototype-only content/capabilities.
10. Give truthful local or deployed access instructions.

Do not hand off a page that is merely attractive. Hand off a coherent, accurate and trustworthy product experience.
