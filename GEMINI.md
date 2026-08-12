# Gemini CLI Project Context

@./AGENTS.md
@./PROMPTS.md
@./PACKS.md

Gemini must treat `AGENTS.md` as the canonical operating system for this repository.

## Automatic task routing

- Restaurant, cafe, bakery, takeaway, delivery, menu, pickup, quick-service, fast-casual, or food-ordering commerce: read `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` and every required file in `packs/fast-casual-commerce/pack.json`.
- New website for another real business: read `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`.
- Redesign, improve, or refine an existing business website: read `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md` and the relevant domain pack.
- After the first browser render of any website or application: read and execute `prompts/VISUAL_QA_AND_REVISION.md`.
- General product or interface work: also use `prompts/SENIOR_PRODUCT_TEAM_PROMPT.md`.

Do not start implementation until the required core and pack-specific contracts are completed. Do not report completion until the rendered visual-QA loop has been performed.
