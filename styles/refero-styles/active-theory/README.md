# Active Theory

Source: https://styles.refero.design/style/3416bd14-96bb-4c23-bd01-b2ea178ba5ce

Product/site reference: https://activetheory.net

## Snapshot

- **Mood:** Cosmic void command deck where the rendered WebGL world is the interface.
- **Theme:** Dark, immersive, cinematic, minimal.
- **Core grammar:** Pure black canvas, translucent ghost chrome, hairline gray borders, one muted violet CTA, geometric micro UI text, editorial serif body copy.
- **Best for:** WebGL portfolios, immersive creative studio sites, interactive 3D experiences, cinematic dark brand pages.

Active Theory is built around restraint. The UI does not decorate the scene; it barely confirms that it exists. A pure black canvas carries a full-viewport rendered world, while navigation, consent, cards, and CTAs float as whispered translucent elements. Color is rationed to one muted violet accent so the 3D scene keeps all chromatic drama.

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

- Use `#000000` as the only page canvas.
- Use translucent overlays instead of solid card fills.
- Use `#343755` only for singular dominant CTAs.
- Use `#4d4d4d` for card borders and dividers.
- Use `backdrop-filter: blur(4px)` for overlays.
- Use nbarchitekt or a geometric sans for nav and UI chrome.
- Use Times-style serif for longer body copy.
- Do not use shadows, UI gradients, or extra accent colors.
