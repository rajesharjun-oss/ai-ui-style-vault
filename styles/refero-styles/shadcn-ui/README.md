# shadcn/ui

Source: https://styles.refero.design/style/0fd67ec5-7e9c-4ca9-b368-5d9c7388477a

Product/site reference: https://ui.shadcn.com

## Snapshot

- **Mood:** White component studio with frosted gray depth and command-palette discipline.
- **Theme:** Light, monochrome, compact, developer-facing.
- **Core grammar:** Geist typography, white cards, subtle gray borders, compact 14px text, 18px control radius, 24px card radius, red only for destructive/error states.
- **Best for:** Developer tools, documentation sites, component galleries, admin panels, internal dashboards, settings-heavy apps.

This style is useful when you want an interface that feels engineered, calm, and highly composable. It avoids decorative color systems, large brand gradients, and expressive typography. The polish comes from disciplined spacing, gray surface hierarchy, rounded but not cute controls, and very precise text scale.

## Folder Map

- `DESIGN.md` - style summary and implementation guidance.
- `implementation-prompt.md` - prompt for an AI agent building in this direction.
- `source.md` - source link and capture notes.
- `tokens/` - markdown design tokens by category.
- `code/css-variables.css` - reusable CSS custom properties and example classes.
- `code/tailwind-v4.css` - Tailwind v4 theme variables and component helpers.
- `code/design-tokens.json` - structured tokens for AI/code ingestion.
- `screenshots/README.md` - screenshot capture notes.

## Fast Build Notes

- Use `#ffffff` as the page canvas and card surface.
- Use Geist Sans for almost everything.
- Use Geist Mono only for code, shortcuts, and command-like labels.
- Keep primary text at `#09090b` and muted text at `#71717b`.
- Use `1px #e4e4e7` borders for card and control separation.
- Use 18px radius for buttons, inputs, badges, tabs, and dropdowns.
- Use 24px radius for cards, modals, and command surfaces.
- Use `#e7000b` only for destructive or error moments.
