# 11x Digital Workers

Source: [Refero Style](https://styles.refero.design/style/850ee61c-4ecd-4558-9c0c-fab99721b34c)  
Reference site: [https://www.11x.ai](https://www.11x.ai)  
Captured: 2026-07-29  
Refero published: 2026-05-08T18:56:28.795Z  
Refero modified: 2026-06-03T15:53:42.550Z  
Theme: mixed  
Category: AI

## Style Summary

Explore 11x Digital workers's mixed AI design system: Obsidian #000000, Paper White #ffffff colors, ES Allianz typography, and DESIGN.md for AI agents.

North star: Cinematic editorial desert full-bleed terrain photography against monumental serif headlines, where the page reads like a luxury magazine spread.

## What To Borrow

- Obsidian `#000000` as Primary action buttons on light surfaces, body text, headlines, card borders the universal ink of the system
- Paper White `#ffffff` as Page canvas on light sections, card surfaces, text on dark backgrounds, button text on filled buttons
- Deep Teal `#0b252a` as Dark section backgrounds the only large chromatic surface, used for narrative bands between editorial spreads
- Bone `#f6f5f5` as Card surfaces and hairline borders on light sections the warm off-white that prevents starkness
- Sandstone `#f5ece5` as Warm card surface tint, section backgrounds in cream/peach areas desert-hour warmth
- Ash Blush `#ede2d7` as Soft warm card surface, secondary peach accent on portrait cards
- ES Allianz Primary typeface for all UI text a high-contrast didone-influenced serif used at dramatic display sizes (74152px) for headlines, and at body sizes (1619px) for running text. The tight letter-spacing (-0.045em at display, -0.02em at body) tightens the serifs into a modern editorial stance. Weight 400 carries most copy; 700 for hero impact; 500 for navigation and subheadings. This serif does the heavy lifting that a sans-serif system would spread across three families. `--font-es-allianz` for the source typography voice
- 8px base spacing with compact density
- Source radius system: cards 16px, badges 8px, buttons 999px, smallBadges 2px

## Avoid

- Do not use sans-serif typefaces anywhere the serif is non-negotiable and defines the editorial identity
- Do not use blue, red, green, or yellow as functional UI colors the palette is restricted to neutrals, deep teal, and the four muted pastels
- Do not add drop shadows to cards or buttons elevation is communicated through tonal contrast and 1px hairline borders only
- Do not use sharp corners (under 8px radius) on interactive elements pills, rounded cards, and soft radii are the norm
- Do not center-align body paragraphs longer than two lines left-align running text for editorial readability
- Do not introduce gradients on UI components the only gradient is a subtle warm fade (#f8f9f7 #d7cecd) used minimally
- Do not stack more than one pastel card tint adjacent to another alternate pastel cards with white space to preserve the airy feel

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
