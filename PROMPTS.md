# Prompt Router

This file is the human-readable entry point for task prompts in the AI UI Style Vault.

Agents must first follow `AGENTS.md`. The prompts below add task-specific instructions; they do not replace the canonical product, content, engineering, accessibility, asset, domain-pack, and validation rules.

Read `PACKS.md` and `packs/pack-index.json` whenever a product-specific pack may apply.

## Automatic routing

| User request | Required prompt and pack |
|---|---|
| Build a restaurant, cafe, bakery, takeaway, pickup, delivery, menu, quick-service, fast-casual, or food-ordering website/application | `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` + `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` + `packs/fast-casual-commerce/` |
| Build a new website for another real business from Maps, Instagram, an existing site, a brief, or other public sources | `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` |
| Redesign, improve, modernise, or fix an existing business website | `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md` |
| Review the first rendered implementation, screenshots, or localhost build | `prompts/VISUAL_QA_AND_REVISION.md` |
| Build any product interface, web app, dashboard, or app screen | `prompts/SENIOR_PRODUCT_TEAM_PROMPT.md` |

The most specific route wins.

For a restaurant-commerce build, the agent must use:

1. `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md`
2. `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`
3. `packs/fast-casual-commerce/pack.json` and every required read
4. `prompts/VISUAL_QA_AND_REVISION.md` after the first render

For another new business website, the agent must use both:

1. `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`
2. `prompts/VISUAL_QA_AND_REVISION.md` after the first render

For a redesign, the agent must use both:

1. `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md`
2. The relevant domain pack when one matches
3. `prompts/VISUAL_QA_AND_REVISION.md` after the first render

## Minimal human invocation

A user can give an agent the vault repository and write:

```text
Use this vault as the mandatory design and engineering system.
Build a premium website or ordering experience for this business: <BUSINESS LINK OR BRIEF>.
Follow the automatic prompt and domain-pack routing in PROMPTS.md and PACKS.md.
```

The agent must then discover the relevant prompt and pack, conduct research, create the contracts, build, render, inspect, revise, and provide evidence.

## Required truthfulness

The agent must not:

- Claim that a remote sandbox’s `localhost` is reachable from the user’s computer.
- Claim that a page is visually correct without rendering it.
- Present generated or stock imagery as official business photography.
- Present assumptions as verified business facts.
- Present prototype cart, payment, delivery, loyalty, or tracking functions as real integrations.
- Claim a quality check passed when it was not run.
