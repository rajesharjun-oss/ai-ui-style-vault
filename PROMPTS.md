# Prompt Router

This file is the human-readable entry point for task prompts in the AI UI Style Vault.

Agents must first follow `AGENTS.md`. The prompts below add task-specific instructions; they do not replace the canonical product, content, engineering, accessibility, asset, domain-pack, privacy and validation rules.

Read `PACKS.md` and `packs/pack-index.json` whenever a product-specific pack may apply.

## Mandatory real-business research gate

Whenever the target is a real business, brand, creator, organisation, venue, product or service, read `guides/BUSINESS_RESEARCH_GATE.md` before selecting any style, production theme, screen reference, 3D scene, motion pattern or AI-agent recipe.

The required order is:

`environment inspection → business research → business-profile.json → research gate → product/content strategy → asset strategy → domain/style/3D recipe selection → contracts → implementation → render → visual QA → validation → handoff`

The agent must understand the business first. Do not design from a business name, social handle, logo or inaccessible link alone. Create `business-profile.json` using `research/business-profile.schema.json` and validate it with `python scripts/validate-business-understanding.py <path-to-business-profile.json>`.

If supplied Instagram, TikTok or other sources are blocked, try alternative current public sources. If the business's core offer, audience and primary website task still cannot be established reliably, set the profile status to `blocked`, set `designSelectionAllowed` to `false`, stop before design selection, and ask the user for screenshots, screen recording, bio, service/product information or other evidence. Do not build a generic concept to fill the gap.

## Automatic routing

| User request | Required prompt and pack |
|---|---|
| Build a 3D website, immersive WebGL/WebGPU, Three.js/R3F/Babylon/Spline, configurator, showroom, digital twin, spatial portfolio, globe, AR or WebXR | `prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md` + `packs/3d-immersive-web/` + matching product-domain pack |
| Build a fashion, couture, bespoke tailoring, atelier, corporate wear, kaftan, traditional wear, occasion wear or made-to-order fashion website | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` + `packs/fashion-couture/` |
| Build a wedding, Nikkah, engagement, anniversary, save-the-date, RSVP, couple story, gift registry, private celebration or post-event gallery website | `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md` + `packs/celebration-event-microsite/` |
| Build a restaurant, cafe, bakery, takeaway, pickup, delivery, menu, quick-service, fast-casual, or food-ordering website/application | `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` + `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` + `packs/fast-casual-commerce/` |
| Build a new website for another real business from Maps, Instagram, an existing site, a brief, or other public sources | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| Redesign, improve, modernise, or fix an existing business or event website | `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md` + the relevant domain pack |
| Review the first rendered implementation, screenshots, or localhost build | `prompts/VISUAL_QA_AND_REVISION.md` |
| Build any product interface, web app, dashboard, or app screen | `prompts/SENIOR_PRODUCT_TEAM_PROMPT.md` |

The most specific product-domain route wins. Capability prompts such as 3D may be added alongside it.

For a 3D build, use the 3D prompt, all pack reads, the matching product-domain pack and visual QA. When the 3D target is a real business, the business research gate comes before recipe selection.

For a fashion/couture build, the agent must use:

1. `guides/BUSINESS_RESEARCH_GATE.md`
2. `research/business-profile.schema.json` and a validated `business-profile.json`
3. `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`
4. `packs/fashion-couture/pack.json` and every required read
5. `prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md` only when 3D/motion capability is requested or justified
6. `prompts/VISUAL_QA_AND_REVISION.md` after the first render

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
5. `prompts/VISUAL_QA_AND_REVISION.md` after the first render

For another new business website, the agent must use:

1. `guides/BUSINESS_RESEARCH_GATE.md`
2. `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`
3. `prompts/VISUAL_QA_AND_REVISION.md` after the first render

For a redesign, the agent must use:

1. `guides/BUSINESS_RESEARCH_GATE.md` when the target is a real business
2. `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md`
3. The relevant domain pack when one matches
4. `prompts/VISUAL_QA_AND_REVISION.md` after the first render

## Minimal human invocation

A user can give an agent the vault repository and write:

```text
Use this vault as the mandatory design and engineering system.
Build a premium website for: <COUPLE, EVENT, BUSINESS LINK OR BRIEF>.
Follow the automatic prompt and domain-pack routing in PROMPTS.md and PACKS.md.
```

For a real business, the agent must first research and understand the business, produce and validate `business-profile.json`, pass the research gate, then discover the relevant prompt and pack, create the contracts, select the design, build, render, inspect, revise and provide evidence.

## Required truthfulness

The agent must not:

- Claim that a remote sandbox's `localhost` is reachable from the user's computer.
- Claim that a page is visually correct without rendering it.
- Present generated or stock imagery as official business or couple photography.
- Present assumptions as verified business or event facts.
- Infer a business model merely from a social handle, logo, category guess or inaccessible source.
- Continue to visual design when the minimum business research gate is blocked.
- Invent couple stories, event details, guest rules, scriptures, travel arrangements or financial details.
- Present prototype RSVP, guest lookup, cart, payment, delivery, loyalty or tracking functions as real integrations.
- Expose private guest, media or gifting information contrary to the selected privacy contract.
- Claim a quality check passed when it was not run.
