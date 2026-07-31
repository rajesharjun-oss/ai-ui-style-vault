# Savee

Source: [Refero Style](https://styles.refero.design/style/c6d8490d-e3f2-45c8-aebf-fe5f11daf116)
Reference site: [https://savee.it](https://savee.it)
Captured: 2026-07-31
Refero published: 2026-01-22T15:00:06.000Z
Refero modified: 2026-06-05T11:13:37.642Z
Theme: dark
Category: Design

## Style Summary

Explore Savee's dark Design design system: Electric Indigo #1500ff, Obsidian #050505 colors, Savee Font typography, and DESIGN.md for AI agents.

North star: Black canvas for visual curators

## What To Borrow

- Electric Indigo `#1500ff` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Obsidian `#050505` for Page canvas, deepest background - the void that all content sits on
- Charcoal `#151515` for Elevated surface, product preview frames, secondary panels
- Graphite `#1e1e1e` for Deeper overlay surface, hover states on dark cards, input fields
- Paper `#fdfdfd` for Primary text, inverted surface, button text, high-contrast foreground
- Silver `#e5e5e5` for Hairline borders, dividers, subtle structural edges
- Pearl `#d4d4d4` for Secondary text, subdued headings, placeholder body copy
- Slate `#2f2f2f` for Footer borders, low-contrast dividers between dark zones
- Ash `#a3a3a3` for Muted helper text, inactive icons, de-emphasized metadata
- Stone `#737373` for Tertiary text, timestamps, supplementary labels

- Savee Font `--font-savee-font` for The sole typeface - a custom geometric sans used at every scale. Weight 400 carries the editorial body and nav; weight 500 appears on buttons and emphasized labels. The 96px display at 0.96 line-height with -0.04em tracking is the system's signature: it compresses into a dense confident block rather than stretching vertically, making the headline feel sculptural.

## Avoid

- Never use #1500ff for anything other than the primary CTA fill - not for links, not for icons, not for hover states, not for badges
- Never add drop shadows or elevation glows to cards - the system uses surface color shifts (#050505 #151515 #1e1e1e) for hierarchy, not shadows
- Never set body text below 16px for primary content - captions and metadata can go to 13-14px, but main copy stays large
- Never introduce additional accent colors, even in illustrations or partner logos - the partner strip stays grayscale to preserve the indigo's dominance
- Never use border-radius values between 0px and 9999px for buttons - the system is binary: fully rounded pills or 14px card corners, nothing in between
- Never apply gradients to backgrounds, buttons, or text - the system is flat monochrome with one solid color exception
- Never use line-height above 1.50 for any text size - the tight line-heights (0.96-1.38) are the system's editorial signature

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
