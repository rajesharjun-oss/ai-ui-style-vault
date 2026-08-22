# Prompt Router

This file is the human-readable entry point for task prompts in the AI UI Style Vault.

Agents must first follow `AGENTS.md`. The prompts below add task-specific instructions; they do not replace the canonical product, content, engineering, accessibility, asset, domain-pack, privacy and validation rules.

Read `PACKS.md` and `packs/pack-index.json` whenever a product-specific pack may apply.

## Mandatory real-business research gate

Whenever the target is a real business, brand, creator, organisation, venue, product or service, read `guides/BUSINESS_RESEARCH_GATE.md` before selecting any style, production theme, screen reference, 3D scene, motion pattern or AI-agent recipe.

The required order is:

`environment inspection → business research → business-profile validation → domain-pack selection → asset readiness → scored production-theme selection → section-recipe selection → contracts → implementation → render → visual QA → anti-generic score gate → handoff`

The agent must understand the business first. Do not design from a business name, social handle, logo or inaccessible link alone. Create `business-profile.json` using `research/business-profile.schema.json` and validate it with `python scripts/validate-business-understanding.py <path-to-business-profile.json>`.

If supplied Instagram, TikTok or other sources are blocked, try alternative current public sources. If the business's core offer, audience and primary website task still cannot be established reliably, set the profile status to `blocked`, set `designSelectionAllowed` to `false`, stop before design selection, and ask the user for screenshots, screen recording, bio, service/product information or other evidence. Do not build a generic concept to fill the gap.

After the research gate is ready, run `scripts/plan-vault-build.py`. Use its selected domain pack, then run `scripts/score-design-selection.py` and `scripts/select-section-recipes.py`. Production-theme and section composition must be evidence-based rather than selected by aesthetic preference.

## Automatic routing

| User request | Required prompt and pack |
|---|---|
| Build a 3D website, immersive WebGL/WebGPU, Three.js/R3F/Babylon/Spline, configurator, showroom, digital twin, spatial portfolio, globe, AR or WebXR | `prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md` + `packs/3d-immersive-web/` + matching product-domain pack |
| Build a fashion, couture, bespoke tailoring, atelier, corporate wear, kaftan, traditional wear, occasion wear or made-to-order fashion website | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` + `packs/fashion-couture/` |
| Build a wedding, Nikkah, engagement, anniversary, save-the-date, RSVP, couple story, gift registry, private celebration or post-event gallery website | `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md` + `packs/celebration-event-microsite/` |
| Build a restaurant, cafe, bakery, takeaway, pickup, delivery, menu, quick-service, fast-casual, or food-ordering website/application | `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` + `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` + `packs/fast-casual-commerce/` |
| Build a new website for another real business from Maps, Instagram, an existing site, a brief, or other public sources | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` + the product-domain pack selected after research |
| Redesign, improve, modernise, or fix an existing business or event website | `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md` + the relevant domain pack |
| Review the first rendered implementation, screenshots, or localhost build | `prompts/VISUAL_QA_AND_REVISION.md` |
| Build any product interface, web app, dashboard, or app screen | `prompts/SENIOR_PRODUCT_TEAM_PROMPT.md` |

The most specific product-domain route wins. Capability prompts such as 3D may be added alongside it.

## Design intelligence routing

For a real-business build after `business-profile.json` passes validation:

1. Run `python scripts/plan-vault-build.py business-profile.json` (add `--3d` only when requested/justified).
2. Run `python scripts/score-design-selection.py business-profile.json --domain-pack <pack-id> --asset-readiness <strong|adequate|limited|none>`.
3. Record the top scores, winning margin and rationale in `VAULT_SELECTION.md` and `design-recipe.json`.
4. Run `python scripts/select-section-recipes.py business-profile.json --domain-pack <pack-id>` for the sections actually needed by the page.
5. Record section recipe IDs in the page plan or `design-recipe.json`.
6. If production-theme scoring returns `tie-or-review`, resolve the tie deliberately before coding; do not pick the most visually dramatic option by default.
7. After rendered visual QA, complete `VISUAL_QA_OBSERVATIONS.json` and pass `scripts/validate-anti-generic-visual.py` with a score of at least 75.

## Product-domain routing

The current real-business product-domain packs include:

- `packs/fashion-couture/`
- `packs/beauty-wellness/`
- `packs/hospitality/`
- `packs/saas-technology/`
- `packs/professional-services/`
- `packs/real-estate/`
- `packs/fast-casual-commerce/`

Celebration/event work uses `packs/celebration-event-microsite/`. `packs/3d-immersive-web/` is a capability pack layered on top of the appropriate product-domain pack.

For a 3D build, use the 3D prompt, all pack reads, the matching product-domain pack and visual QA. When the 3D target is a real business, the business research gate and scored domain/theme selection come before 3D recipe selection.

For a celebration-event build, the agent must use:

1. `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md`
2. `packs/celebration-event-microsite/pack.json` and every required read
3. `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` only when the site also represents a real event-planning business or service offering
4. `prompts/VISUAL_QA_AND_REVISION.md` after the first render

For a restaurant-commerce build, the agent must use:

1. `guides/BUSINESS_RESEARCH_GATE.md`
2. `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md`
3. `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`
4. `packs/fast-casual-commerce/pack.json` and every required read
5. the scored theme/section selection tools
6. `prompts/VISUAL_QA_AND_REVISION.md` after the first render
7. the anti-generic visual QA gate before handoff

For another new business website, the agent must use:

1. `guides/BUSINESS_RESEARCH_GATE.md`
2. `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`
3. the selected product-domain pack and every required read
4. the scored theme/section selection tools
5. `prompts/VISUAL_QA_AND_REVISION.md` after the first render
6. the anti-generic visual QA gate before handoff

For a redesign, the agent must use:

1. `guides/BUSINESS_RESEARCH_GATE.md` when the target is a real business
2. `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md`
3. The relevant domain pack when one matches
4. the scored theme/section selection tools when visual direction changes materially
5. `prompts/VISUAL_QA_AND_REVISION.md` after the first render
6. the anti-generic visual QA gate before handoff

## Minimal human invocation

A user can give an agent the vault repository and write:

```text
Use this vault as the mandatory design and engineering system.
Build a premium website for: <COUPLE, EVENT, BUSINESS LINK OR BRIEF>.
Follow the automatic prompt and domain-pack routing in PROMPTS.md and PACKS.md.
```

For a real business, the agent must first research and understand the business, produce and validate `business-profile.json`, pass the research gate, select the domain pack, score the production themes, choose section recipes, create the contracts, build, render, inspect, revise, pass the anti-generic score gate and provide evidence.

## Required truthfulness

The agent must not:

- Claim that a remote sandbox's `localhost` is reachable from the user's computer.
- Claim that a page is visually correct without rendering it.
- Present generated or stock imagery as official business or couple photography.
- Present assumptions as verified business or event facts.
- Infer a business model merely from a social handle, logo, category guess or inaccessible source.
- Continue to visual design when the minimum business research gate is blocked.
- Select a lower-scoring production theme without documenting the product reason.
- Repeat one section composition across an entire page because it is easy to implement.
- Invent couple stories, event details, guest rules, scriptures, travel arrangements or financial details.
- Present prototype RSVP, guest lookup, cart, payment, delivery, loyalty or tracking functions as real integrations.
- Expose private guest, media or gifting information contrary to the selected privacy contract.
- Claim a quality check passed when it was not run.
- Hand off a real-business build that fails the anti-generic visual QA gate.
