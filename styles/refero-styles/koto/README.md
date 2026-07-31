# Koto

Source: [Refero Style](https://styles.refero.design/style/a88fa835-1d5e-4b8e-b3d5-602597870563)
Reference site: [https://koto.com](https://koto.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:24:25.496Z
Refero modified: 2026-06-05T12:11:15.024Z
Theme: dark
Category: Agency

## Style Summary

Explore Koto's dark Agency design system: Void Black #060606, Graphite Surface #141414 colors, gtKotoheim, gtKotoheimCondensed typography, and DESIGN.md for...

North star: Obsidian gallery at midnight. A near-black stage where a single yellow mark is the only warm light, and condensed type floats in vast negative space like exhibition placards.

## What To Borrow

- Void Black `#060606` for Primary page canvas - the dominant background where all content floats; not pure black, but a warmthless near-black that keeps contrast at AAA
- Graphite Surface `#141414` for Elevated card and icon backgrounds - one step lighter than canvas, used to subtly separate surfaces without breaking the dark mood
- Smoke Border `#202020` for Hairline borders and dividers - barely visible structural lines that define regions without adding visual weight
- Iron Mute `#595959` for Muted text and secondary borders - body text at reduced emphasis, footer meta, tertiary labels
- Ash Gray `#989898` for Secondary body text and medium-emphasis borders - the most-used neutral after white, for body copy and structural outlines
- Silver Whisper `#b4b4b4` for Light body text - softer than white for inline body content where pure white would feel too sharp
- Paper White `#ffffff` for Primary text, heading strokes, and all key borders - the brightest mark in the system, reserved for content that must read first
- Signal Yellow `#ffe800` for Yellow decorative accent for icons, marks, and small graphic details.

- gtKotoheim `--font-gtkotoheim` for All UI, body, navigation, button, and small-display text. Custom monospace-feeling sans with 'salt' alternate glyphs - weight 350 is the default body, 400 for slightly stronger emphasis. The only typeface for everything below display size.
- gtKotoheimCondensed `--font-gtkotoheimcondensed` for Display headings only. Condensed cut at weight 300 with tight 1.0-1.1 leading and -0.01em tracking - these headlines whisper rather than shout, letting the vast negative space amplify their presence. Reserved for hero statements and section titles.

## Avoid

- Don't introduce any color outside the neutral scale and Signal Yellow; the system is 0% colorful by design
- Don't use filled buttons or colored CTAs; interactive elements are ghost/outlined with #ffffff borders on transparent fills
- Don't apply shadows, gradients, or blur effects to any element - the flat void treatment is non-negotiable
- Don't use radius values other than 2px, 6px, or 10px; mixing radii breaks the geometric discipline
- Don't set body copy in gtKotoheimCondensed or display in gtKotoheim regular; the two families are strictly separated by size and role
- Don't use pure #ffffff for body text - reserve it for headings, borders, and the UTC indicator; body copy uses #b4b4b4
- Don't add icons, illustrations, or imagery to the base layout; the page is typographic-first and visual assets should only appear inside Dark Surface Cards

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
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
