# AI Agent Instructions

This repository is an AI-readable UI reference vault. Use it to choose and adapt visual direction for original websites, web tools, dashboards, and app screens.

## First Read

When a user asks you to use this vault for a product build, read these files first:

1. `README.md`
2. `guides/AGENT_USAGE.md`
3. `guides/AGENT_BUILD_CHECKLIST.md`
4. `guides/STYLE_SELECTION_GUIDE.md`
5. `guides/WEB_TOOL_DESIGN_MATRIX.md`
6. `agent-index.json`
7. `catalog.json`
8. `screen-catalog.json`

## Selection Rule

Pick one primary style bundle for the global visual system, then pick screen references only for page-specific layout behavior.

- Use `styles/refero-styles/<style-slug>/` for color, typography, spacing, components, tone, and do/don't rules.
- Use `screens/refero/<channel>/<page-type>/<screen-slug>/` for page composition patterns.
- Use `implementation-prompt.md`, `DESIGN.md`, `tokens/`, and `code/` before making design decisions.

## Adaptation Rule

Create an original interface that fits the target product. Do not clone protected brands, logos, screenshots, exact product copy, or proprietary layouts.

You may preserve:

- Token logic
- Mood and pacing
- Spacing rhythm
- Typography relationships
- Component behavior patterns
- Page-type structure

You must tailor:

- Copy
- Information architecture
- Navigation
- Feature hierarchy
- Data density
- Accessibility
- Responsive behavior
- Target repo conventions

## Output Rule

Before implementation, state the selected references:

- Primary style bundle
- Supporting screen references
- Why they match the product
- What will be adapted
- What will not be copied

Create a `VAULT_SELECTION.md` record from `templates/VAULT_SELECTION.md` in the generated project or target repo before building.

Then implement using the target repository stack and conventions.

## QA Rule

Before handoff, run the visual, asset, and generated-site checks from `guides/AGENT_BUILD_CHECKLIST.md`.

For browser-rendered or static sites, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\validate-generated-site.ps1 -SiteRoot <site-root>
```

Do not hand off as complete if the build hotlinks target-site images, has missing vault selection notes, contains placeholders, or has obvious desktop/mobile overlap.
