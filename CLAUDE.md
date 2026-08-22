# Claude Code Project Instructions

@./AGENTS.md
@./PROMPTS.md
@./PACKS.md

Claude Code must treat `AGENTS.md` as the canonical operating system for this repository.

## Automatic task routing

- 3D website, immersive WebGL/WebGPU, Three.js/R3F/Babylon/Spline, configurator, showroom, digital twin, spatial portfolio, globe, AR or WebXR: read `prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md` and `packs/3d-immersive-web/pack.json`, plus the matching product-domain pack.
- Wedding, Nikkah, engagement, anniversary, save-the-date, RSVP, couple story, gift registry, private celebration or post-event gallery: read `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md` and every required file in `packs/celebration-event-microsite/pack.json`.
- Restaurant, cafe, bakery, takeaway, delivery, menu, pickup, quick-service, fast-casual or food-ordering commerce: read `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` and every required file in `packs/fast-casual-commerce/pack.json`.
- New website for another real business: read `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md`.
- Redesign, improve or refine an existing website: read `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md` and the relevant domain pack.
- After the first browser render: read and execute `prompts/VISUAL_QA_AND_REVISION.md`.
- General product or interface work: also use `prompts/SENIOR_PRODUCT_TEAM_PROMPT.md`.

Do not start implementation until the required core and pack-specific contracts are completed. Do not report completion until the rendered visual-QA loop and domain-pack state matrix have been performed.

For every 3D build, complete `THREE_D_RELEVANCE_CONTRACT.md` before asset selection and reject semantically unrelated 3D/video/background media.
