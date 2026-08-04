# Agent Usage

Use this guide when an AI builder is given a target GitHub repository and asked to choose a design direction from this vault.

## Goal

The vault should help an agent make a deliberate design choice, not randomly copy a nice screenshot. The agent should inspect the target product, select references from this repo, and produce an original implementation that fits the actual use case.

For landing pages and motion graphics websites, the agent should also choose a motion direction, pattern set, and reduced-motion plan before coding.

## Recommended Workflow

1. Inspect the target repository.
   - Identify framework, styling stack, routing, component system, existing design tokens, package manager, and build commands.
   - Identify the product type, user roles, required pages, density, data shape, risk level, and motion needs.

2. Read the vault indexes.
   - Start with `agent-index.json` for the machine-readable workflow.
   - Read `guides/AGENT_BUILD_CHECKLIST.md` for required asset, motion, and visual QA gates.
   - Read `guides/SITE_INTERACTION_PATTERNS.md` when the site needs rotating hero imagery, dropdowns, mega menus, category browsing, brand grids, or top-nav interaction.
   - Read `motion/LANDING_PAGE_MOTION_GUIDE.md` when the site needs a landing page, cinematic hero, product tour, scroll story, animated UI, WebGL, Lottie, Rive, GSAP, or motion graphics feel.
   - Use `catalog.json` to find global style systems.
   - Use `screen-catalog.json` to find page-type examples.
   - Use `motion/motion-catalog.json` to find motion references, patterns, and implementation resources.
   - Use `CAPTURED_STYLES.md`, `SCREEN_REFERENCES.md`, and `motion/MOTION_REFERENCES.md` when a human-readable scan is faster.

3. Run the automated selectors for a first pass.
   - Use `scripts/select-vault-style.ps1` with `-Brief` and, after cloning/inspecting a target repo, `-ProjectPath`.
   - Use `scripts/select-motion-references.ps1` when the brief mentions landing pages, motion, animation, cinematic, product tours, scroll stories, video, canvas, WebGL, Lottie, Rive, GSAP, or animated dashboards.
   - Review generated reports instead of accepting them blindly.
   - Visual example: `powershell -ExecutionPolicy Bypass -File .\scripts\select-vault-style.ps1 -Brief "Premium B2B analytics dashboard with login, pricing, integrations, and contacts" -ProjectPath <target-repo> -OutputPath <target-repo>\VAULT_SELECTION.generated.md`.
   - Motion example: `powershell -ExecutionPolicy Bypass -File .\scripts\select-motion-references.ps1 -Brief "Cinematic SaaS landing page with scroll product story and animated product tour" -ProjectPath <target-repo> -OutputPath <target-repo>\MOTION_SELECTION.generated.md`.

4. Shortlist candidates.
   - Pick 3 to 5 style bundles whose `category`, `bestFor`, `tags`, `theme`, and `northStar` match the product.
   - Pick page-specific screen references for dashboard, login, product details, pricing/paywall, catalog, profile, 404, blog, developers, integrations, contacts, careers, or media kit pages as needed.
   - Pick motion references and 2 to 5 motion patterns only when they help explain the product, strengthen hierarchy, or improve perceived quality.

5. Choose references.
   - Select 1 primary style bundle.
   - Select up to 2 supporting style bundles only when they solve a clear missing need.
   - Select 1 screen reference per important page type.
   - Select 1 primary motion model for landing-page or motion-heavy builds.

6. Create the selection record.
   - Copy `templates/VAULT_SELECTION.md` into the generated project or target repo.
   - Fill in the primary style, supporting references, motion references when relevant, fit rationale, adaptation plan, asset policy, reduced-motion plan, and QA plan before implementation.

7. Read the selected folders deeply.
   - For styles, read `README.md`, `DESIGN.md`, `implementation-prompt.md`, `style.json`, `tokens/`, and `code/`.
   - For screens, read `README.md`, `implementation-prompt.md`, `screen.json`, `tokens/`, and `code/`.
   - For motion, read `motion/LANDING_PAGE_MOTION_GUIDE.md`, `motion/MOTION_REFERENCES.md`, `motion/motion-catalog.json`, and selected style folders with motion signals.

8. Implement in the target repo.
   - Use the target repo's existing stack and conventions.
   - Translate vault tokens into the target design system.
   - Build complete, responsive, accessible UI.
   - Add loading, empty, error, focus, disabled, hover, active, and reduced-motion states.
   - Use one primary animation approach instead of mixing every library.

9. Verify.
   - Run lint, typecheck, tests, and build when available.
   - Run `scripts/validate-generated-site.ps1` for static or browser-rendered outputs.
   - Check mobile and desktop layouts.
   - Check section anchors, forms, legends, sticky or fixed headers, text wrapping, autoplay controls, scroll scenes, video/canvas fallbacks, and reduced-motion behavior.
   - Confirm no target-site images, logos, screenshots, videos, exact animation sequences, or exact page layouts were copied.
   - Confirm the result is inspired by the references but not a brand clone.

## Prompt Pattern

```text
Use ai-ui-style-vault as the design reference source.

First inspect this target repo and summarize the app type, audience, pages, stack, existing UI conventions, and motion needs.
Then run scripts/select-vault-style.ps1 with the brief and target repo path, read the generated selection report, and select one primary style bundle plus page-specific screen references.
If the build is a landing page, cinematic site, product tour, scroll story, animated dashboard, WebGL page, or motion graphics website, also run scripts/select-motion-references.ps1 and read motion/LANDING_PAGE_MOTION_GUIDE.md.
Explain why those references fit.
Create or review a VAULT_SELECTION.md / VAULT_SELECTION.generated.md record before implementation.
Implement an original UI using the selected tokens, rhythm, component rules, page patterns, and motion patterns.
Do not copy protected logos, screenshots, videos, brand assets, exact copy, proprietary layouts, or exact animation sequences.
Run the generated-site validator, visual QA, motion QA, and available project checks. Summarize the result.
```

## What "Exact Design" Means Here

Use exact captured tokens and rules when they are available, such as colors, spacing, typography scale, border radius, component states, layout rhythm, and motion constraints.

Do not use exact protected brand expression, such as the same logos, images, product text, videos, brand-specific compositions, animation sequences, or screen-by-screen clones.

The correct result should feel like the chosen style system was professionally adapted to the user's product.

## Interaction Pattern Add-On

When a target site needs richer navigation, browse-driven discovery, or multiple first-screen messages, also consult `guides/SITE_INTERACTION_PATTERNS.md`.

Useful add-ons include rotating editorial heroes, product taxonomy mega menus, brand logo mega menus, split utility menus, and icon category drawers. Use these as interaction patterns only; pair them with the selected visual style and adapt the content, media, and structure to the target product.

## Motion Add-On

When a target site needs landing-page polish or motion graphics, also consult `motion/LANDING_PAGE_MOTION_GUIDE.md` and run `scripts/select-motion-references.ps1`.

Useful add-ons include kinetic hero type, scroll product stories, cinematic media heroes, animated product UI tours, Lottie illustration systems, Rive interactive controls, Three.js product stages, microinteraction systems, motion-safe mega menus, and animated data proof. Use these as choreography patterns only; pair them with selected style tokens and build original motion from licensed or owned assets.
