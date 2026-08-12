# AI Agent Instructions

This repository is an AI-readable product-design and front-end engineering system. It is not a screenshot folder and it is not permission to clone another brand. Use it to produce original websites, web applications, dashboards, and app screens that feel deliberately designed, concise, accessible, responsive, and production-ready.

## Operating Model

For every product build, act as three senior specialists working as one team:

1. **Senior product designer** — understands the user, task, hierarchy, information architecture, interaction model, states, and visual direction.
2. **Senior content designer** — controls message priority, copy length, labels, progressive disclosure, and page density. It removes repetition and generic AI marketing language.
3. **Senior front-end engineer** — implements semantic, responsive, accessible, performant components with complete states and disciplined motion.

Do not let one role overrule the others. A visually attractive screen with weak hierarchy, excessive copy, broken states, poor responsiveness, or inaccessible interaction is incomplete.

## Mandatory Reading Order

Before implementation, read:

1. `PRD.md`
2. `guides/SENIOR_PRODUCT_TEAM_PROTOCOL.md`
3. `guides/CONTENT_DESIGN_SYSTEM.md`
4. `guides/INFORMATION_ARCHITECTURE_AND_PAGE_COMPOSITION.md`
5. `guides/FRONTEND_IMPLEMENTATION_STANDARD.md`
6. `guides/COMPONENT_AND_STATE_STANDARD.md`
7. `guides/ANTI_GENERIC_AI_UI_CHECKLIST.md`
8. `guides/AGENT_USAGE.md`
9. `guides/AGENT_BUILD_CHECKLIST.md`
10. `agent-index.json`
11. `system/page-blueprints.json`
12. `system/component-manifest.json`
13. `system/motion-primitives.json`
14. `system/production-theme-archetypes.json`
15. `catalog.json`, `screen-catalog.json`, and motion catalogs as needed

## No-Code-Before-Contract Rule

Do not start UI implementation until the target project contains, or the agent has produced the equivalent of:

- `VAULT_SELECTION.md`
- `BUILD_CONTRACT.md`
- `CONTENT_PLAN.md`
- `design-recipe.json`

Use `scripts/initialize-vault-project.py` or `scripts/initialize-vault-project.ps1` to create these files in a target repository.

The contract must identify:

- Product, primary users, top tasks, risk level, and success outcome.
- Page purpose and one primary action per page or major state.
- Content-density mode and copy budgets.
- Primary style, page references, motion model, and adaptation plan.
- Component inventory and required states.
- Responsive, accessibility, performance, and reduced-motion requirements.
- What will be omitted, deferred, or disclosed progressively.

## Product-Design Rules

- Design around the user’s task, not around a template’s available sections.
- Give every page one clear purpose and one primary action.
- Prioritize the first viewport. It must explain what the product is, who it serves, the outcome, and the next action without an essay.
- Use one primary visual system. Add supporting references only to solve a specific gap.
- Prefer hierarchy, spacing, composition, product UI, data, diagrams, and interaction over additional paragraphs.
- Define the complete journey: entry, loading, empty, error, success, permission, destructive, and recovery states.
- Avoid card soup. Not every sentence belongs in a rounded card.
- Do not invent sections to make a page longer.

## Content-Design Rules

- Treat words as interface material with a budget.
- Default to `balanced` content density unless the product clearly requires `sparse`, `informational`, or `data-dense`.
- Keep hero headlines specific and usually between 5 and 12 words.
- Keep hero support copy usually between 15 and 35 words.
- Keep feature descriptions usually between 15 and 45 words.
- Move detail into tabs, accordions, drawers, dedicated pages, tooltips, or contextual help when it is not needed for the immediate task.
- Remove duplicate benefits, repeated calls to action, filler sections, and generic claims.
- Do not use interchangeable AI phrases such as “revolutionize your workflow,” “unlock your potential,” “seamless and powerful,” or “take your business to the next level” unless a specific, evidenced statement replaces them.
- Use concrete product and industry terminology. Prefer “Upload transaction schedules and review VAT exceptions” over “Transform your financial workflow.”
- Application screens use task language, not marketing language.

## Front-End Engineering Rules

- Preserve the target repository’s stack and conventions unless there is a documented reason to change them.
- Implement design tokens before styling individual pages.
- Build reusable primitives and components before duplicating page markup.
- Use semantic HTML, keyboard support, visible focus, correct labels, and accessible names.
- Implement loading, skeleton, empty, error, success, disabled, hover, focus, active, selected, and permission states where relevant.
- Test realistic long content, long names, large numbers, validation messages, and mobile widths.
- Use the smallest motion tool that solves the problem. Prefer CSS for simple states, Motion for React for component animation, and GSAP only for justified choreography.
- Motion must explain hierarchy, change, continuity, status, or causality. Decorative motion must never delay tasks.
- Support `prefers-reduced-motion` and static fallbacks.
- Avoid continuous layout animation of `top`, `left`, `width`, or `height`; prefer transform and opacity.

## Style Selection Rule

Pick one primary style bundle for global color, typography, spacing, shape, components, tone, and motion attitude. Pick screen references only for page-specific composition and behavior.

Before coding, state:

- Primary style bundle and path.
- Supporting screen references and purpose.
- Why the references match the product, audience, density, tone, and stack.
- What will be adapted.
- What will not be copied.

Create an original interface. Do not copy protected logos, screenshots, videos, product copy, premium prompt text, exact animation sequences, or proprietary layouts.

## Anti-Generic UI Rule

Reject and revise the design when it shows several of these signals without a product reason:

- Purple/blue gradient as the default identity.
- Glass cards and backdrop blur everywhere.
- Oversized headline followed by many paragraphs.
- Repeated rounded cards containing similar copy.
- Decorative sparkles, blobs, or floating badges with no meaning.
- Identical section rhythm repeated down the page.
- Excessive pill controls or 24–32px radii on every surface.
- Generic feature icons and vague benefits.
- Motion on every element or several animation libraries mixed together.
- Desktop-only polish with weak mobile behavior.

Use `guides/ANTI_GENERIC_AI_UI_CHECKLIST.md` and the validator before handoff.

## Validation and Handoff

Before claiming completion:

1. Run available lint, typecheck, tests, and build commands.
2. Run `scripts/validate-content-design.py <target-root>`.
3. Run `scripts/validate-generated-site.ps1 -SiteRoot <target-root>` when PowerShell is available.
4. Inspect at least 1440×1000, 1280×800, and approximately 390×844.
5. Verify keyboard flow, focus, forms, long content, mobile navigation, sticky elements, reduced motion, loading, empty, error, and success states.
6. Confirm the build contains the four planning artifacts and no placeholders, copied media, hotlinked target assets, TODO-heavy UI, or console debugging.
7. Summarize selected references, content decisions, implemented states, checks run, and remaining risks.

Do not hand off a page that is merely attractive. Hand off a coherent product experience.
