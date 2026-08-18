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
- New website for another real business: `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` plus the product-domain pack selected after the business research gate.
- Redesign or improvement of an existing website: `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md` plus the relevant domain pack.
- After the first browser render: `prompts/VISUAL_QA_AND_REVISION.md`.
- General product interface work: `prompts/SENIOR_PRODUCT_TEAM_PROMPT.md`.

The most specific route wins. Task prompts and packs add requirements; they do not replace this file, `PRD.md` or the core contracts.

## Business-understanding gate

For every real business, brand, organisation, venue, product or service, the agent must research and understand the business before selecting a theme, section composition, style, 3D scene or motion recipe.

Create `BUSINESS_RESEARCH.md` and `business-profile.json`, then validate:

```bash
python scripts/validate-business-understanding.py business-profile.json
```

The research status must be `ready` and `designSelectionAllowed` must be true before visual design selection. If the core offer, audience or primary conversion cannot be established, stop before design and request evidence rather than inventing a generic concept.

## Domain-pack discovery

Domain packs live under `packs/` and are indexed by `packs/pack-index.json`.

When a trigger matches:

1. Read the selected pack's `pack.json`.
2. Read every file in its `requiredReads` list.
3. Add the pack to `VAULT_SELECTION.md` and `design-recipe.json`.
4. Create the pack-specific contracts before implementation.
5. Use the pack's blueprints, components, states, content rules, asset rules, privacy rules, code contracts and QA requirements.
6. Remove unsupported capabilities rather than inventing them.

Current product-domain packs include Fast-Casual Commerce, Celebration & Event Microsite, Fashion & Couture, Beauty & Wellness, Hospitality, SaaS & Technology, Professional Services and Real Estate. `3d-immersive-web` is a capability pack that may be layered on when justified.

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
19. `system/design-selection-scoring.json`
20. `system/section-recipes.json`
21. Style, screen and motion catalogues as needed

## Scored design-selection rule

Production-theme selection must be evidence-based, not aesthetic preference.

After the business research gate and domain-pack selection, run:

```bash
python scripts/score-design-selection.py business-profile.json --domain-pack <pack-id> --asset-readiness <strong|adequate|limited|none>
```

The scoring model weighs domain fit, conversion fit, brand tone, content density, trust requirements, asset readiness and performance. Record the scores, winning margin and rationale in `VAULT_SELECTION.md` and `design-recipe.json`. Do not select a lower-scoring direction merely because it looks more dramatic unless a documented product reason resolves the difference.

If the winner does not meet the minimum score or the top two are within the configured winning margin, treat the result as `tie-or-review` and resolve it deliberately before coding.

## Section-level composition rule

Do not compose an entire page by repeating one visual pattern. Use `system/section-recipes.json` to select section-level composition according to purpose, domain, conversion, density and available evidence.

Example:

```bash
python scripts/select-section-recipes.py business-profile.json --domain-pack <pack-id> --section hero --section proof --section services --section cta --section footer
```

A page may use different section recipes when their purposes differ. Recipe selection is not permission to clone a fixed layout; adapt the composition to the verified business, content and assets. Record selected recipe IDs in the page plan or `design-recipe.json`.

## No-code-before-contract rule

Do not start UI implementation until the target project contains completed equivalents of:

- `VAULT_SELECTION.md`
- `BUILD_CONTRACT.md`
- `CONTENT_PLAN.md`
- `design-recipe.json`

For a real business website, also create:

- `BUSINESS_RESEARCH.md`
- `business-profile.json`
- `ASSET_PLAN.md` when imagery, video, illustration or 3D is involved

For transactional food commerce, also create `COMMERCE_BUILD_CONTRACT.md`.

For celebration/event work, also create `EVENT_BUILD_CONTRACT.md`, `COUPLE_CONTENT_PLAN.md` and `ASSET_PLAN.md`.

For 3D or immersive experiences, also create `THREE_D_BUILD_CONTRACT.md`, `SCENE_ASSET_PLAN.md` and `PERFORMANCE_AND_FALLBACK_PLAN.md`.

Add any other selected domain pack's required contract from its `pack.json`.

Contracts must identify product/event, primary users or guests, top tasks, risk and success outcome; page purpose and one primary action per page or state; content-density mode and copy budgets; primary style, scored production theme, section recipes, supporting references, motion model and selected pack; component inventory and required states; responsive, accessibility, performance and reduced-motion requirements; omitted/deferred information; verified facts, assumptions, private information, asset provenance, consent and owner-confirmation items; sources of truth, integrations, prototype-only capabilities and recovery rules.

## Product-design rules

- Design around the user's or guest's task, not a template's available sections.
- Give every page one clear purpose and one primary action.
- Prioritise the first viewport; explain the product or event and next action without an essay.
- Use one primary visual system. Add supporting references only to solve a specific gap.
- Prefer hierarchy, spacing, composition, product UI, data, media and interaction over additional paragraphs.
- Define the complete journey and all meaningful loading, empty, error, success, permission, destructive and recovery states.
- Avoid card soup and filler sections.
- Make practical business or event information easy to find.

## Content-design rules

- Treat words as interface material with a budget.
- Default to `balanced` density unless the product clearly requires `sparse`, `informational` or `data-dense`.
- Keep hero headlines specific and usually 5–12 words; support copy usually 15–35 words.
- Move secondary detail into dedicated pages, tabs, accordions, drawers or contextual help.
- Remove duplicate benefits, repeated actions, filler and generic AI marketing language.
- Use concrete product, industry or event terminology.
- Separate verified facts from assumptions.
- Do not invent claims, prices, hours, addresses, availability, discounts, event dates, venues, guest rules, couple stories, quotations, travel arrangements or financial details.

## Asset and art-direction rules

- Use user-provided, original, generated, owned or clearly licensed assets only.
- Do not hotlink or copy protected target-site media.
- Do not present generated or stock imagery as official business or couple photography.
- Plan subject, purpose, crop, focal point, aspect ratio, mobile treatment, alternative text, access, consent and provenance before implementation.
- Keep product photography or event-media treatment consistent.
- Do not repeat one photograph across unrelated sections merely to fill space.
- Use process imagery to prove process claims.

## 3D and immersive web rules

- Prove what 3D improves and choose the smallest sufficient medium.
- Complete `THREE_D_RELEVANCE_CONTRACT.md` before searching for models/video/backgrounds. Reject any major visual whose subject is not directly tied to the business, product, service, process, place, verified data, audience or page purpose. Primary visuals require relevance score 4–5; secondary decoration requires at least 3.
- Never use an unrelated Ferrari, spaceship, luxury object or other spectacle merely because it looks premium.
- Build a complete semantic static fallback first; essential content and controls remain DOM.
- Define static, basic-mobile, balanced and high tiers before heavy downloads.
- Support reduced motion, save data, low power/memory, unsupported, errors and context loss.
- Record licence/provenance for every model, texture, HDRI, animation, shader and code example.
- Do not copy code, media, branding, copy, models, textures, exact layout or choreography from references.

## Front-end engineering rules

- Preserve the target repository's stack and conventions unless a documented reason requires change.
- Implement design tokens and reusable primitives before duplicating page markup.
- Use semantic HTML, keyboard support, visible focus, correct labels and accessible names.
- Implement all relevant states, including loading, empty, error, success, disabled, hover, focus, active, selected and permission states.
- Use the smallest motion tool that solves the problem.
- Support `prefers-reduced-motion` and static/no-animation fallbacks.
- Scroll-reveal content must remain visible when JavaScript or animation initialisation fails.
- Prevent horizontal overflow and deliberately transform mobile layouts.

## Anti-generic UI rule

Reject and revise designs with several unsupported signals: default purple/blue gradients or glass cards; oversized headlines followed by long paragraphs; repeated rounded cards containing similar copy; decorative sparkles, blobs or badges with no meaning; identical section rhythm; excessive pills/radii; generic icons and vague benefits; motion on every object; desktop-only polish; repeated/misleading imagery; or a design that could be relabelled for an unrelated business.

## Rendered visual-QA rule

A browser-rendered build is not complete from source inspection alone. After the first render, execute `prompts/VISUAL_QA_AND_REVISION.md`. Capture and inspect desktop, laptop and mobile views, record findings, fix them and recapture.

Copy `quality/VISUAL_QA_OBSERVATIONS.template.json` into the project, complete it from the rendered evidence and run:

```bash
python scripts/validate-anti-generic-visual.py <site-root> <VISUAL_QA_OBSERVATIONS.json> --json-out <visual-qa-score.json>
```

The minimum passing score is 75. Hard failures include uncleared mobile horizontal overflow, unverified media provenance and an unverified primary action. Do not hand off until the gate passes.

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
4. Inspect at least 1440×1000, 1280×800 and approximately 390×844; add pack-specific states and viewports.
5. Verify keyboard flow, focus, forms, long content, mobile navigation, sticky elements, reduced motion, no-animation fallback and meaningful error/success states.
6. Run the structured anti-generic visual QA gate and retain its score/evidence.
7. Confirm required planning artifacts exist and no placeholders, copied media, hotlinked assets, TODO-heavy UI or console debugging remain.
8. Summarise business research, selection scores, section recipes, references, pack, content, assets, states, integrations, checks, screenshots and risks.
9. Distinguish verified, provisional, private, generated, licensed, integrated and prototype-only content/capabilities.
10. Give truthful local or deployed access instructions.

Do not hand off a page that is merely attractive. Hand off a coherent, accurate, original and trustworthy product experience.
