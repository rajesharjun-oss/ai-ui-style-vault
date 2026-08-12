# Refine an Existing Business Website

Use this prompt when the user provides an existing site, screenshots, a localhost build, or source repository and asks for improvement, redesign, modernisation, or a more premium result.

Follow `AGENTS.md`, `PRD.md`, and the relevant vault guides.

## Objective

Preserve useful business truth and working functionality while correcting the hierarchy, content, visual system, assets, responsiveness, accessibility, and conversion path. Do not redesign merely for novelty.

## Phase 1 — Establish the baseline

1. Inspect the repository and run the existing site.
2. Capture current screenshots at 1440×1000, 1280×800, and approximately 390×844.
3. Inventory pages, components, assets, copy, interactions, integrations, and technical constraints.
4. Identify what already works and must be preserved.
5. Create `EXISTING_SITE_AUDIT.md`.

## Phase 2 — Audit the rendered experience

Review:

- First-viewport clarity.
- Primary conversion path.
- Navigation and information architecture.
- Content density and repeated messages.
- Typography scale and line length.
- Section rhythm and excessive card use.
- Image relevance, quality, consistency, crop, and repetition.
- Brand distinctiveness.
- Sticky header and anchor behaviour.
- Forms, labels, errors, success, and recovery.
- Keyboard, focus, contrast, zoom, and reduced motion.
- Desktop-to-mobile transformation.
- Performance and asset weight.
- Missing practical business information.
- Unsupported claims or invented content.

Classify findings as:

- Blocking.
- Important.
- Enhancement.
- Owner confirmation.

## Phase 3 — Define the refinement contract

Create or update:

- `BUSINESS_RESEARCH.md`.
- `ASSET_PLAN.md`.
- `VAULT_SELECTION.md`.
- `BUILD_CONTRACT.md`.
- `CONTENT_PLAN.md`.
- `design-recipe.json`.

State:

- What will be retained.
- What will be removed.
- What will be compressed.
- What will be restructured.
- What will be redesigned.
- What requires new assets.
- What requires business-owner confirmation.

## Phase 4 — Select one coherent direction

Use the vault to choose one primary style and restrained supporting references.

Do not layer a new theme over unresolved structure. Fix information architecture and content hierarchy first.

Avoid:

- Redesigning every component differently.
- Increasing visual noise to create “premium” appearance.
- Replacing one generic template with another.
- Retaining weak assets because they already exist.
- Copying a reference website’s exact layout or motion.

## Phase 5 — Implement in controlled passes

Recommended sequence:

1. Information architecture.
2. Content compression.
3. Design tokens.
4. Typography and spacing.
5. Navigation and shell.
6. Key conversion pages.
7. Assets and art direction.
8. Responsive behaviour.
9. States and accessibility.
10. Motion and polish.

Preserve working integrations and business-critical behaviour unless replacement is tested.

## Phase 6 — Mandatory visual revision loop

Execute `prompts/VISUAL_QA_AND_REVISION.md`.

Compare before and after screenshots. Verify that the new version is not only different but measurably clearer, more credible, more usable, and more specific to the business.

### Common issues that must be corrected

- Display type that occupies too much of the viewport.
- Sticky headers covering section content.
- Repeated hero imagery in several sections.
- Product images with mismatched lighting, angle, crop, or quality.
- Process claims illustrated with unrelated finished-product images.
- Missing prices, hours, location, contact, service modes, or booking/ordering information.
- Large decorative sections with little customer value.
- Mobile layouts that simply shrink desktop composition.
- Generic copy, vague buttons, or repeated calls to action.

## Handoff

Report:

- Baseline problems.
- What was preserved.
- What changed and why.
- Content removed or deferred.
- Assets replaced or still required.
- Before and after screenshots.
- Tests and validators run.
- Remaining owner-confirmation items.
- Exact local or deployment instructions.

Do not claim the redesign is complete without a rendered comparison and correction pass.
