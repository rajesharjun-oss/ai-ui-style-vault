# Foodnoms

Source: [Refero Style](https://styles.refero.design/style/1e7dae3b-cb34-4fcf-8c32-051152aebbab)  
Reference site: [https://foodnoms.com](https://foodnoms.com)  
Captured: 2026-07-29  
Refero published: 2026-03-17T16:42:30.000Z  
Refero modified: 2026-06-05T01:48:30.157Z  
Theme: light  
Category: Productivity

## Style Summary

Explore Foodnoms's light Productivity design system: Ember Orange #ff5406, Verdant Green #00b33f colors, Aquawax Pro Medium, Aquawax Pro typography, and...

North star: Sunlit fruit market on white porcelain warm orange, fresh green, and generous rounded forms

## What To Borrow

- Ember Orange `#ff5406` as Orange supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Verdant Green `#00b33f` as Green supporting accent for decorative details and low-frequency emphasis
- Signal Red-Orange `#ff3400` as Secondary warm accent visible in app screen UI elements and supporting brand moments. Sits one step hotter than Ember Orange for emphasis on selected or active app states
- Sky Blue `#00a9dd` as Cool counter-accent for app-internal data categories (carbs/protein/other nutrient groupings). Balances the warm-dominant palette inside phone mockups
- Mist Blue `#72a2c5` as Muted cool accent softens Sky Blue for secondary data labels and chart backgrounds inside the app surfaces
- Sunset Orange `#ff6d00` as Warm accent for secondary headings and emphasis text within the marketing pages
- Aquawax Pro Medium Aquawax Pro Medium detected in extracted data but not described by AI `--font-aquawax-pro-medium` for the source typography voice
- Aquawax Pro Primary brand typeface used across all display, heading, and body contexts. The custom face has a wide x-height, rounded geometric forms, and friendly proportions. Bold (700) is used for the 60px display and 30px section headlines these are the system's typographic anchors. DemiBold (600) handles subheadings and button labels at 1416px. Medium (500) carries body copy at 1720px with generous 1.61.8 line-height for comfortable reading. `--font-aquawax-pro` for the source typography voice
- 8px base spacing with comfortable density
- Source radius system: tags 26px, cards 26px, inputs 26px, buttons 26px

## Avoid

- Don't use box-shadows or drop-shadows anywhere the system is deliberately flat
- Don't use a border-radius other than 26px on buttons, cards, tags, or inputs
- Don't call any color a 'CTA' or 'primary action' in the token system describe them by their brand role instead
- Don't use Aquawax Pro at sizes below 12px fall back to system sans-serif for micro UI
- Don't place chromatic text on a chromatic background always pair color text with white or Fog
- Don't use gradient backgrounds or gradient buttons the system is solid color only
- Don't introduce new chromatic colors for marketing pages the warm-primary + cool-accent + app-data palette is complete

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
