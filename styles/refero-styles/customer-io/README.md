# Customer.io

Source: [Refero Style](https://styles.refero.design/style/abbaa70a-5fe2-44a9-9c5f-272e68c450c3)
Reference site: [https://customer.io](https://customer.io)
Captured: 2026-07-30
Refero published: 2026-04-30T00:54:10.020Z
Refero modified: 2026-07-03T10:56:23.495Z
Theme: mixed
Category: SaaS

## Style Summary

Explore Customer.io's mixed SaaS design system: Spruce Abyss #00191c, Spruce 900 #032125 colors, Saans typography, and DESIGN.md for AI agents.

North star: dark spruce forest meeting cream paper

## What To Borrow

- Spruce Abyss `#00191c` for Deepest background - footer canvas, dramatic section breaks
- Spruce 900 `#032125` for Primary dark surface - headers, hero, main navigation background; dominant text color on light surfaces
- Spruce 700 `#0b363b` for Primary CTA fill on dark backgrounds, elevated card surfaces, border accent
- Spruce 500 `#437278` for Muted teal accent - illustration fills, secondary icon color
- Spruce 200 `#a1c2c6` for Decorative stroke, muted link text, icon outlines on dark surfaces
- Spruce Mist `#354d51` for Body text on light surfaces, secondary heading color
- Charcoal 100 `#ebebeb` for Hairline borders, dividers, subtle separators across the interface
- Charcoal Mist `#fafafa` for Alternate section background, subtle card backgrounds
- Cream Warm `#fffcf6` for Primary light surface - content sections, card backgrounds
- Pure White `#ffffff` for Elevated card surface, button text on dark fills, content blocks
- Verdant 300 `#abffae` for Interactive glow - CTA button fill, focus ring halo, active state border; vivid green signals action without aggression
- Verdant Whisper `#eafde8` for Primary page canvas and white card surfaces. Use as a supporting accent, not as a status color
- Wave 700 `#123a88` for Violet text accent for links, tags, and emphasized short phrases.
- Wave 500 `#0a6de6` for Heading accent color for keyword highlights in display text
- Wave Frost `#e2f4ff` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Use as a supporting accent, not as a status color
- Zest 700 `#863d1c` for Orange text accent for links, tags, and emphasized short phrases.
- Zest Blush `#fdf0e9` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Use as a supporting accent, not as a status color
- Mustard 700 `#83611c` for Yellow text accent for links, tags, and emphasized short phrases.

- Saans `--font-saans` for Custom display + body typeface used for everything. Weight 475 dominates - a near-medium voice that feels calm and confident rather than aggressive.

## Avoid

- Never use drop shadows for elevation - depth comes from colored 4px glow rings only
- Never use bold weights above 600 for display or heading text - the signature is the calm 475 voice
- Never use corner radius above 2px on non-button elements - sharp-cornered cards define this system
- Never use #0000ee or default browser blue for links - links use #032125 or #a1c2c6
- Never place #abffae on white or light backgrounds without sufficient contrast - it is a glow color, not a fill
- Never use more than 4 columns in content grids - the system favors generous spacing over density
- Never use the heading accent colors (#863d1c, #123a88, etc.) for UI chrome - they exist only for inline keyword coloring in display text

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
