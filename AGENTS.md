# AI Agent Instructions

This repository is an AI-readable product-design and front-end engineering system. It is not a screenshot folder and it is not permission to clone another brand. Use it to produce original websites, web applications, dashboards, commerce experiences, and app screens that feel deliberately designed, concise, accessible, responsive, and production-ready.

## Operating Model

For every product build, act as three senior specialists working as one team:

1. **Senior product designer** — understands the user, task, hierarchy, information architecture, interaction model, states, and visual direction.
2. **Senior content designer** — controls message priority, copy length, labels, progressive disclosure, and page density. It removes repetition and generic AI marketing language.
3. **Senior front-end engineer** — implements semantic, responsive, accessible, performant components with complete states and disciplined motion.

Do not let one role overrule the others. A visually attractive screen with weak hierarchy, excessive copy, broken states, poor responsiveness, or inaccessible interaction is incomplete.

## Prompt Discovery and Routing

Read `PROMPTS.md`, `prompts/prompt-index.json`, `PACKS.md`, and `packs/pack-index.json` before selecting a task prompt or domain pack.

Use these prompts automatically:

- Restaurant, cafe, bakery, takeaway, delivery, menu, pickup, quick-service, fast-casual, or food-ordering commerce: `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` plus the Fast-Casual Commerce pack.
- New website for another real business: `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`.
- Redesign or improvement of an existing business website: `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md`.
- After the first browser render of any website or application: `prompts/VISUAL_QA_AND_REVISION.md`.
- General product interface work: `prompts/SENIOR_PRODUCT_TEAM_PROMPT.md`.

The more specific route wins. A restaurant ordering request uses the restaurant-commerce prompt, the general business prompt, and visual QA. Task prompts and domain packs add requirements; they do not replace this file, `PRD.md`, or the required project contracts.

## Domain Pack Discovery

Domain packs live under `packs/` and are indexed by `packs/pack-index.json`.

When a trigger matches:

1. Read the selected pack's `pack.json`.
2. Read every file in its `requiredReads` list.
3. Add the pack to `VAULT_SELECTION.md` and `design-recipe.json`.
4. Create any pack-specific contract before implementation.
5. Use the pack's page blueprints, components, states, content rules, asset rules, code contracts, and QA requirements.
6. Remove unsupported capabilities rather than inventing them.

For restaurant and food-ordering products, the required pack is `packs/fast-casual-commerce/` and the required additional contract is `COMMERCE_BUILD_CONTRACT.md`.

## Mandatory Reading Order

Before implementation, read:

1. `PRD.md`
2. `PROMPTS.md`
3. `PACKS.md`
4. The task prompt selected by `prompts/prompt-index.json`
5. The domain pack selected by `packs/pack-index.json`, including every required read
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
19. `catalog.json`, `screen-catalog.json`, and motion catalogs as needed

## No-Code-Before-Contract Rule

Do not start UI implementation until the target project contains, or the agent has produced the equivalent of:

- `VAULT_SELECTION.md`
- `BUILD_CONTRACT.md`
- `CONTENT_PLAN.md`
- `design-recipe.json`

For a real business website, also create:

- `BUSINESS_RESEARCH.md`
- `ASSET_PLAN.md` when imagery, video, illustration, or 3D is involved

For transactional restaurant or food commerce, also create:

- `COMMERCE_BUILD_CONTRACT.md`

Use `scripts/initialize-vault-project.py` or `scripts/initialize-vault-project.ps1` to create the core files in a target repository. Copy pack-specific templates from the selected pack.

The contract must identify:

- Product, primary users, top tasks, risk level, and success outcome.
- Page purpose and one primary action per page or major state.
- Content-density mode and copy budgets.
- Primary style, page references, motion model, selected domain pack, and adaptation plan.
- Component inventory and required states.
- Responsive, accessibility, performance, and reduced-motion requirements.
- What will be omitted, deferred, or disclosed progressively.
- Verified business facts, assumptions, asset provenance, and owner-confirmation items when applicable.
- Sources of truth, integrations, prototype-only capabilities, and recovery rules for transactional products.

## Product-Design Rules

- Design around the user’s task, not around a template’s available sections.
- Give every page one clear purpose and one primary action.
- Prioritise the first viewport. It must explain what the product is, who it serves, the outcome, and the next action without an essay.
- Use one primary visual system. Add supporting references only to solve a specific gap.
- Prefer hierarchy, spacing, composition, product UI, data, diagrams, and interaction over additional paragraphs.
- Define the complete journey: entry, loading, empty, error, success, permission, destructive, and recovery states.
- Avoid card soup. Not every sentence belongs in a rounded card.
- Do not invent sections to make a page longer.
- For real businesses, make practical conversion information easy to find: location, hours, contact, pricing or price guidance, service modes, booking, ordering, or enquiry paths as relevant.
- For commerce, treat browsing, configuration, cart, checkout, confirmation, and recovery as the primary product—not as a feature below a marketing page.

## Content-Design Rules

- Treat words as interface material with a budget.
- Default to `balanced` content density unless the product clearly requires `sparse`, `informational`, or `data-dense`.
- Keep hero headlines specific and usually between 5 and 12 words.
- Keep hero support copy usually between 15 and 35 words.
- Keep feature descriptions usually between 15 and 45 words.
- Move detail into tabs, accordions, drawers, dedicated pages, tooltips, or contextual help when it is not needed for the immediate task.
- Remove duplicate benefits, repeated calls to action, filler sections, and generic claims.
- Do not use interchangeable AI phrases such as “revolutionize your workflow,” “unlock your potential,” “seamless and powerful,” or “take your business to the next level” unless a specific, evidenced statement replaces them.
- Use concrete product and industry terminology. Prefer “Upload transaction schedules and review VAT exceptions” over “Transform your financial workflow.”
- Application screens use task language, not marketing language.
- Separate verified facts from assumptions. Do not invent business claims, prices, hours, addresses, capabilities, customers, awards, reviews, service areas, availability, discounts, or delivery estimates.
- Commerce interfaces keep product, price, availability, branch, fulfilment, cart status, fees, total, and next action explicit.

## Asset and Art-Direction Rules

- Use user-provided, original, generated, owned, or clearly licensed assets only.
- Do not hotlink or copy protected target-business media.
- Do not present generated or stock imagery as official business photography.
- Plan image subject, purpose, crop, aspect ratio, mobile treatment, and provenance before implementation.
- Keep product photography consistent in lighting, angle, crop, background, colour treatment, and quality.
- Do not repeat one photograph across unrelated sections merely to fill space.
- Use process imagery to prove process claims.
- Prefer realistic product imagery for food, hospitality, retail, property, beauty, automotive, and other product-led businesses unless the brief explicitly requests an illustrative direction.
- For food commerce, follow `packs/fast-casual-commerce/food-photography-standard.md` and reject cartoonish, mismatched, misleading, or low-resolution product imagery when a realistic brief is required.

## Front-End Engineering Rules

- Preserve the target repository’s stack and conventions unless there is a documented reason to change them.
- Implement design tokens before styling individual pages.
- Build reusable primitives and components before duplicating page markup.
- Use semantic HTML, keyboard support, visible focus, correct labels, and accessible names.
- Implement loading, skeleton, empty, error, success, disabled, hover, focus, active, selected, and permission states where relevant.
- Test realistic long content, long names, large numbers, validation messages, and mobile widths.
- Use the smallest motion tool that solves the problem. Prefer CSS for simple states, Motion for React for component animation, and GSAP only for justified choreography.
- Motion must explain hierarchy, change, continuity, status, or causality. Decorative motion must never delay tasks.
- Support `prefers-reduced-motion` and static fallbacks.
- Avoid continuous layout animation of `top`, `left`, `width`, or `height`; prefer transform and opacity.
- Account for sticky-header height in anchor navigation and test browser zoom.
- Prevent horizontal overflow and define intentional mobile transformations rather than merely shrinking desktop layouts.
- For commerce, revalidate price, availability, branch, address, fulfilment, promotion, fee, tax, payment, and order creation on the server. Use idempotency for payment and order submission.

## Style Selection Rule

Pick one primary style bundle for global colour, typography, spacing, shape, components, tone, and motion attitude. Pick screen references only for page-specific composition and behaviour. Add one domain pack when the product requires it.

Before coding, state:

- Primary style bundle and path.
- Selected production theme and domain pack.
- Supporting screen references and purpose.
- Why the references match the product, audience, density, tone, transaction model, and stack.
- What will be adapted.
- What will not be copied.

Create an original interface. Do not copy protected logos, screenshots, videos, product copy, premium prompt text, exact animation sequences, proprietary layouts, product catalogs, promotions, or checkout flows.

## Anti-Generic UI Rule

Reject and revise the design when it shows several of these signals without a product reason:

- Purple/blue gradient as the default identity.
- Glass cards and backdrop blur everywhere.
- Oversized headline followed by many paragraphs.
- Repeated rounded cards containing similar copy.
- Decorative sparkles, blobs, or floating badges with no meaning.
- Identical section rhythm repeated down the page.
- Excessive pill controls or 24–32px radii on every surface.
- Generic feature icons and vague benefits.
- Motion on every element or several animation libraries mixed together.
- Desktop-only polish with weak mobile behaviour.
- Repeated imagery, inconsistent product photography, or decorative media unrelated to the claim.
- Transactional features visually suggested but not implemented or clearly labelled as prototype.

Use `guides/ANTI_GENERIC_AI_UI_CHECKLIST.md`, the selected pack, and the validators before handoff.

## Rendered Visual QA Rule

A browser-rendered build is not complete from source-code inspection alone.

After the first render, execute `prompts/VISUAL_QA_AND_REVISION.md`. Capture and inspect desktop, laptop, tablet when relevant, and mobile screenshots. Record findings, apply fixes, rebuild, and recapture affected views.

Do not merely list visual problems. Correct them before handoff.

For restaurant commerce, render the menu, product customiser, cart, checkout, confirmation, and the relevant store-closed, unavailable, cart-conflict, payment-failed, and mobile states.

## Localhost Truthfulness Rule

- Never imply that a server running in a remote or isolated environment is reachable from the user’s computer.
- When operating on the user’s machine, start the server there, verify the exact port and HTTP response, and keep the process alive.
- When operating remotely, clearly state the boundary and provide a deployable package, self-contained preview, or exact local start instructions.
- Do not fabricate server status, download paths, ports, screenshots, or validation results.

## Validation and Handoff

Before claiming completion:

1. Run available lint, typecheck, tests, and build commands.
2. Run `scripts/validate-content-design.py <target-root>`.
3. Run `scripts/validate-domain-packs.py` in the vault when a domain pack is selected.
4. Run `scripts/validate-generated-site.ps1 -SiteRoot <target-root>` when PowerShell is available.
5. Inspect at least 1440×1000, 1280×800, and approximately 390×844; add pack-specific viewports.
6. Verify keyboard flow, focus, forms, long content, mobile navigation, sticky elements, reduced motion, loading, empty, error, and success states.
7. Confirm the build contains the required planning artifacts and no placeholders, copied media, hotlinked target assets, TODO-heavy UI, or console debugging.
8. Summarise selected references, pack, content decisions, asset decisions, implemented states, integrations, checks run, screenshots captured, and remaining risks.
9. For real businesses, distinguish verified facts, provisional content, generated assets, licensed assets, owner-confirmation items, integrated functions, and prototype-only functions.
10. Give truthful local or deployed access instructions.

Do not hand off a page that is merely attractive. Hand off a coherent product experience.
