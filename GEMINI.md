# Gemini CLI Project Context

@./AGENTS.md
@./PROMPTS.md
@./PACKS.md

Gemini must treat `AGENTS.md` as the canonical operating system for this repository.

## Automatic task routing

- Wedding, Nikkah, engagement, anniversary, save-the-date, RSVP, couple story, gift registry, private celebration or post-event gallery: read `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md` and every required file in `packs/celebration-event-microsite/pack.json`.
- Restaurant, cafe, bakery, takeaway, delivery, menu, pickup, quick-service, fast-casual or food-ordering commerce: read `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` and every required file in `packs/fast-casual-commerce/pack.json`.
- New website for another real business: read `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`.
- Redesign, improve or refine an existing website: read `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md` and the relevant domain pack.
- After the first browser render: read and execute `prompts/VISUAL_QA_AND_REVISION.md`.
- General product or interface work: also use `prompts/SENIOR_PRODUCT_TEAM_PROMPT.md`.

Do not start implementation until the required core and pack-specific contracts are completed. Do not report completion until the rendered visual-QA loop and domain-pack state matrix have been performed.
