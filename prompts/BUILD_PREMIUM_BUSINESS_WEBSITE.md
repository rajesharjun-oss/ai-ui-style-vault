# Build a Premium Business Website

Use this prompt when the user provides a business link, Maps listing, social profile, existing website, company name, or business brief and asks for a new website.

This prompt is mandatory together with `AGENTS.md`, `PRD.md`, and the relevant vault guides.

## Inputs

Collect or infer only when safe:

- Business source links.
- Target repository or output folder.
- Intended audience and market.
- Desired primary conversion action.
- Available brand assets and photographs.
- Required pages, integrations, languages, and constraints.
- Whether the agent is operating on the user’s computer or in a remote sandbox.

Do not block useful work when public research can resolve a missing detail. Record unresolved matters as assumptions or content requiring owner confirmation.

## Role

Act as a coordinated:

- Senior product designer.
- Senior content designer.
- Senior brand-aware front-end engineer.
- Visual QA reviewer.

The goal is not to fill a template. The goal is to create an original, credible, conversion-focused digital experience for this specific business.

## Phase 1 — Inspect the environment

1. Inspect the target repository, framework, package manager, routes, components, design tokens, tests, and build commands.
2. Confirm that the full vault repository is accessible.
3. Read the root instructions and the mandatory files listed in `AGENTS.md`.
4. Determine whether browser automation, screenshots, image generation, web research, and local server execution are available.
5. State any tool limitation that affects the result.

Do not code yet.

## Phase 2 — Research the business

Use reliable current public sources and create `BUSINESS_RESEARCH.md`.

Document:

- Official business name and category.
- Locations and service area.
- Products or services.
- Opening hours, contact methods, and ordering or booking paths.
- Customer types and likely top tasks.
- Distinctive business strengths supported by evidence.
- Reviews or public signals that reveal customer priorities.
- Competitor or category expectations.
- Verified facts with source references.
- Assumptions and owner-confirmation items.

Treat the business’s existing website, Maps listing, and social pages as factual context. Do not copy protected text, page structure, logos, photographs, video, or proprietary interactions unless the user supplies or licenses them.

## Phase 3 — Define the product and content strategy

Create or complete:

- `BUILD_CONTRACT.md`.
- `CONTENT_PLAN.md`.
- `design-recipe.json`.

Define:

- The website’s primary audience.
- One primary conversion action.
- The top customer questions the site must answer.
- The user journey from arrival to conversion.
- The purpose and primary action of each page.
- Content-density mode.
- Copy budgets.
- Required practical information.
- Information that belongs on dedicated pages or behind progressive disclosure.
- Trust and proof requirements.
- SEO and structured-data requirements where relevant.

### Content rules

- The first viewport must communicate the offer, relevance, proof, and next action without an essay.
- Use specific business language rather than generic phrases.
- Do not repeat the same benefit in multiple sections.
- Do not create sections merely to make the page longer.
- Do not place every paragraph in a card.
- Use practical labels such as “View menu”, “Book a consultation”, “Get directions”, or “Upload schedule” instead of vague “Learn more” buttons.
- A local-business site must make location, hours, contact, and conversion paths easy to find.
- A restaurant or retail site must prioritise products, prices or price guidance, availability, ordering, location, hours, and service modes.
- A professional-services site must prioritise service scope, client fit, evidence, engagement path, and contact.

## Phase 4 — Plan the assets

Create `ASSET_PLAN.md` before implementing image-heavy sections.

For every major visual, record:

- Purpose.
- Required subject.
- Source or generation method.
- Licence or ownership status.
- Aspect ratio and crop.
- Art direction.
- Mobile treatment.
- Fallback.

### Asset rules

- Use user-provided, original, generated, owned, or clearly licensed media.
- Do not hotlink target-business assets.
- Do not present generated or stock imagery as official business photography.
- Use realistic product imagery for food, hospitality, retail, property, beauty, automotive, and other product-led businesses unless the requested art direction is explicitly illustrative.
- Use a consistent photography system: lighting, angle, crop, background, colour treatment, and resolution.
- Do not repeat one photograph across unrelated sections merely to fill space.
- Use process imagery to prove process claims. For example, an “open kitchen” section should show preparation or the kitchen—not another finished-product hero.
- Replace low-resolution, distorted, mismatched, or obviously synthetic product imagery before handoff.
- Keep text legible over media and provide meaningful alternatives.

## Phase 5 — Select the vault direction

Create `VAULT_SELECTION.md`.

1. Run or follow the vault style selector.
2. Shortlist three coherent directions.
3. Choose one primary production-theme archetype.
4. Choose one primary style bundle.
5. Choose only page-specific supporting screen references.
6. Choose one motion model and no more than five purposeful motion primitives.
7. Explain why the selection fits the business, audience, content density, conversion task, and stack.
8. State exactly what will be adapted and what will not be copied.

Do not mix unrelated brand systems. Do not default to purple gradients, glass cards, giant type, repeated three-card grids, pill controls, or decorative motion.

## Phase 6 — Present the direction before coding

Provide a concise design-direction summary containing:

- Business understanding.
- Primary audience and action.
- Sitemap or page set.
- Content hierarchy.
- Selected style and motion direction.
- Asset approach.
- Key interaction ideas.
- Risks and owner-confirmation items.

When the user has delegated the full build and no approval checkpoint is required, record the direction in the contract files and proceed.

## Phase 7 — Implement

Build in the target repository’s existing stack unless a change is justified.

Implementation order:

1. Semantic design tokens.
2. Global typography and spacing.
3. App or site shell.
4. Accessible reusable components.
5. Page compositions.
6. Real content and assets.
7. Responsive transformations.
8. Complete interaction and system states.
9. Motion.
10. Performance optimisation.

### Engineering rules

- Use semantic HTML and correct landmarks.
- Provide keyboard operation and visible focus.
- Use responsive image sizing and prevent layout shift.
- Implement loading, error, success, empty, unavailable, and permission states where relevant.
- Make sticky headers account for section anchors and browser zoom.
- Test long headings, long names, translated copy, and narrow screens.
- Use the smallest motion library necessary.
- Support `prefers-reduced-motion`.
- Do not leave lorem ipsum, placeholder-only sections, TODOs, dead buttons, or console debugging.

## Phase 8 — Rendered visual QA

After the first render, stop adding features and execute `prompts/VISUAL_QA_AND_REVISION.md`.

At minimum:

- Render 1440×1000.
- Render 1280×800.
- Render approximately 390×844.
- Capture the first viewport and all major sections.
- Test navigation, primary conversion, forms, menus, drawers, tabs, and media controls.
- Inspect the screenshots rather than assuming the CSS is correct.
- Revise and recapture until blockers are resolved.

Pay special attention to:

- Oversized typography dominating useful content.
- Sticky navigation covering section headings or prior content.
- Repeated imagery.
- Inconsistent photography.
- Low-resolution or artificial-looking product images.
- Missing practical business information.
- Decorative sections that do not support conversion.
- Mobile overflow and unusable tables or menus.
- Inaccessible contrast, focus, labels, or motion.
- Claims that are not visually or factually supported.

## Phase 9 — Validation

Run available:

- Install or dependency checks.
- Lint.
- Typecheck.
- Unit and integration tests.
- Production build.
- `scripts/validate-content-design.py <target-root>`.
- Generated-site and asset checks.
- Accessibility checks.
- Link checks.
- Browser console checks.

Do not say a check passed unless it was run and its output was reviewed.

## Phase 10 — Localhost and handoff

### When operating on the user’s computer

- Start the server in that environment.
- Verify the exact URL and HTTP response.
- Keep the process alive.
- Report the exact command and port.
- When a preferred port is occupied, use and report the actual selected port.

### When operating in a remote or isolated environment

- Do not claim that your `localhost` is reachable from the user’s browser.
- Clearly explain the environment boundary.
- Provide a deployable ZIP, self-contained preview, or exact local start instructions.
- Verify the package contains all required files and assets.
- Do not fabricate a download path or server status.

### Final handoff must include

- What was built.
- Verified business facts and sources.
- Provisional content and owner-confirmation items.
- Selected vault references.
- Assets used and their status.
- Desktop and mobile screenshots.
- Commands and checks run.
- Exact local or deployed access instructions.
- Known limitations and remaining risks.

## Reject conditions

Do not hand off as complete when any of these remain:

- The first viewport is dominated by prose or decorative type.
- The design could be relabelled for an unrelated business.
- Important customer questions are unanswered.
- The same image is reused repeatedly without purpose.
- Product photography is visibly inconsistent or low quality.
- Sticky elements cover content.
- Mobile layout has overlap or horizontal overflow.
- Primary actions are unclear or broken.
- Motion ignores reduced-motion preferences.
- Business facts are invented or assumptions are presented as verified.
- The page has not been rendered and visually reviewed.
- The localhost or preview claim is not truthful.
