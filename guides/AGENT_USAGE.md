# Agent Usage

Use this guide when an AI builder is given a target GitHub repository and asked to choose a design direction from this vault.

## Goal

The vault should help an agent make a deliberate design choice, not randomly copy a nice screenshot. The agent should inspect the target product, select references from this repo, and produce an original implementation that fits the actual use case.

## Recommended Workflow

1. Inspect the target repository.
   - Identify framework, styling stack, routing, component system, existing design tokens, package manager, and build commands.
   - Identify the product type, user roles, required pages, density, data shape, and risk level.

2. Read the vault indexes.
   - Start with `agent-index.json` for the machine-readable workflow.
   - Read `guides/AGENT_BUILD_CHECKLIST.md` for required asset and visual QA gates.
   - Use `catalog.json` to find global style systems.
   - Use `screen-catalog.json` to find page-type examples.
   - Use `CAPTURED_STYLES.md` and `SCREEN_REFERENCES.md` when a human-readable scan is faster.

3. Shortlist candidates.
   - Pick 3 to 5 style bundles whose `category`, `bestFor`, `tags`, `theme`, and `northStar` match the product.
   - Pick page-specific screen references for dashboard, login, product details, pricing/paywall, catalog, profile, 404, blog, developers, integrations, contacts, careers, or media kit pages as needed.

4. Choose references.
   - Select 1 primary style bundle.
   - Select up to 2 supporting style bundles only when they solve a clear missing need.
   - Select 1 screen reference per important page type.

5. Create the selection record.
   - Copy `templates/VAULT_SELECTION.md` into the generated project or target repo.
   - Fill in the primary style, supporting references, fit rationale, adaptation plan, asset policy, and QA plan before implementation.

6. Read the selected folders deeply.
   - For styles, read `README.md`, `DESIGN.md`, `implementation-prompt.md`, `style.json`, `tokens/`, and `code/`.
   - For screens, read `README.md`, `implementation-prompt.md`, `screen.json`, `tokens/`, and `code/`.

7. Implement in the target repo.
   - Use the target repo's existing stack and conventions.
   - Translate vault tokens into the target design system.
   - Build complete, responsive, accessible UI.
   - Add loading, empty, error, focus, disabled, hover, and active states.

8. Verify.
   - Run lint, typecheck, tests, and build when available.
   - Run `scripts/validate-generated-site.ps1` for static or browser-rendered outputs.
   - Check mobile and desktop layouts.
   - Check section anchors, forms, legends, sticky or fixed headers, and text wrapping.
   - Confirm no target-site images, logos, screenshots, or exact page layouts were copied.
   - Confirm the result is inspired by the references but not a brand clone.

## Prompt Pattern

```text
Use ai-ui-style-vault as the design reference source.

First inspect this target repo and summarize the app type, audience, pages, stack, and existing UI conventions.
Then read the vault indexes and select one primary style bundle plus page-specific screen references.
Explain why those references fit.
Create a VAULT_SELECTION.md record before implementation.
Implement an original UI using the selected tokens, rhythm, component rules, and page patterns.
Do not copy protected logos, screenshots, brand assets, exact copy, or proprietary layouts.
Run the generated-site validator, visual QA, and available project checks. Summarize the result.
```

## What "Exact Design" Means Here

Use exact captured tokens and rules when they are available, such as colors, spacing, typography scale, border radius, component states, and layout rhythm.

Do not use exact protected brand expression, such as the same logos, images, product text, brand-specific compositions, or screen-by-screen clones.

The correct result should feel like the chosen style system was professionally adapted to the user's product.
