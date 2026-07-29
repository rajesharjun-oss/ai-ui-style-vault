# Notion

Source: https://styles.refero.design/style/2bf4c61f-de10-4614-ba1b-20c0453bd2a9

Product/site reference: https://notion.so

## Snapshot

- **Mood:** Warm paper notebook with modern product UI and sparse color punctuation.
- **Theme:** Light, tactile, editorial, productivity-focused.
- **Core grammar:** Warm off-white canvas, white cards, 1px borders, 12px card radius, one blue primary action, accent color panels.
- **Best for:** SaaS workspaces, collaboration tools, document editors, AI productivity products, knowledge bases.

Notion's Refero style is a warm, paper-like product system. The page canvas is not white; it is `#f6f5f4`, with white cards sitting above it through hairline borders instead of shadows. Color is restrained: `#0075de` is the main action color, while amber, coral, blue, and midnight accents are mostly used for feature cards and highlight pills.

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

- Use `#f6f5f4` as the page background.
- Use `#ffffff` for cards and raised panels.
- Use `rgba(0,0,0,0.08)` borders instead of shadows for most cards.
- Use `#0075de` for the single main CTA.
- Use accent colors for panels, not for extra button variants.
- Use large sans headlines with negative tracking.
- Use a serif only for occasional editorial body or intro moments.
- Keep motion around `200ms` ease; reserve bouncy movement for small character marks.
