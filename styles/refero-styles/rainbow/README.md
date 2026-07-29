# Rainbow

Source: https://styles.refero.design/style/1680693c-aed8-47e8-917a-04eb89497b09

Product/site reference: https://rainbow.me

## Snapshot

- **Mood:** Soft consumer wallet with rounded utility, tiny rainbow sparks, and confident black actions.
- **Theme:** Light, friendly, mobile-first, compact.
- **Core grammar:** Near-white canvas, pure white cards, black primary buttons, muted gray copy, 20px cards, 12px controls, 9999px badges.
- **Best for:** Crypto wallets, consumer fintech, onboarding flows, account dashboards, web3 tools, friendly mobile-first products.

Rainbow is a soft light product system. It uses almost-white surfaces, compact Inter typography, high-radius cards, and black primary controls. The "rainbow" part is not a full multicolor interface; color appears as small app-icon accents, status chips, and localized gradients while the core UI remains neutral and legible.

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

- Use `#f9fafb` or `#f7f8fa` for the page canvas.
- Use white cards with `1px rgba(0,0,0,0.06)` borders.
- Use black primary buttons with white text.
- Use Inter throughout.
- Keep cards around `20px` radius and controls around `12px`.
- Use rainbow color only in small badges, icons, and token accents.
- Keep UI compact and touch-friendly.
