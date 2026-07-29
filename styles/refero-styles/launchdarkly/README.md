# LaunchDarkly

Source: https://styles.refero.design/style/18a75348-513a-49d8-94f5-e2df8c118b6b

Product/site reference: https://launchdarkly.com

## Snapshot

- **Mood:** Neon control room for feature flags and release governance.
- **Theme:** Dark, technical, developer-led, confident.
- **Core grammar:** Midnight canvas, Carbon panels, violet-to-blue gradient glows, 30px pill-soft components, 60px floating nav pill, bright white product screenshots.
- **Best for:** Developer tools, release platforms, AI control planes, DevOps products, dashboard-led SaaS pages.

LaunchDarkly feels like a dark cockpit for software delivery. The system uses deep charcoal panels, cool violet-blue signals, white product screenshots, mono code surfaces, and large display type. The important distinction is that color is mostly an electronic pulse: glows, active states, headline emphasis, and button fills.

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

- Use `#0e0e0e` as the full-page canvas.
- Use `#191919` for nav pills, cards, code blocks, and footer panels.
- Use `#405bff` for filled primary CTAs.
- Use `#7084ff` for headline accents, outlines, underlines, and glow endpoints.
- Use the `179deg` gradient from `#405bff` to `#7084ff` for ambient glows.
- Use 30px radius for buttons, tags, cards, and tabs.
- Use 60px radius for the floating nav pill.
- Render real product screenshots as bright white panels on the dark canvas.
