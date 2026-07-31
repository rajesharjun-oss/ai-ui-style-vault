# Quicken

Source: [Refero Style](https://styles.refero.design/style/75eb47d6-2526-4936-b15a-7474cf4cdc69)
Reference site: [https://www.quicken.com](https://www.quicken.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:55:10.555Z
Refero modified: 2026-06-05T09:00:44.784Z
Theme: mixed
Category: Fintech

## Style Summary

Explore Quicken's mixed Fintech design system: Voltage Violet #471cff, Deep Iris #0f0733 colors, Haffer typography, and DESIGN.md for AI agents.

North star: electric violet on white marble

## What To Borrow

- Voltage Violet `#471cff` for Primary action buttons, active nav items, key links, brand emphasis - the single chromatic pulse of the interface; everything else defers to it
- Deep Iris `#0f0733` for Dark section backgrounds, hero canvas, high-contrast text on light surfaces - the midnight counterpart that anchors alternating dark bands
- Signal Red `#eb0130` for Promotional accents, sale/urgency indicators, highlight strokes - used sparingly to flag attention without competing with the primary violet
- Lilac Whisper `#dbd3ff` for Soft card and container borders - a low-contrast violet edge that brands outlines without adding visual weight
- Periwinkle Mist `#bbc5fa` for Cooler card border tone for grouping and container edges - second step in the violet border scale for layered cards
- Coral Burst `#ff5a43` for Error and warning badge fills, alert pills - warm contrast against the cool violet system
- Aqua Pop `#7ae7fb` for Decorative badge backgrounds, hero trust-pill fill - cool cyan that brightens dark sections
- Ink Black `#18181f` for Primary body and heading text, dominant border color, icon strokes - the near-black that carries all readable content
- Carbon `#494949` for Secondary text, muted nav, supporting borders - the mid-gray step between ink and white
- Pure White `#ffffff` for Page and card backgrounds, text on dark surfaces, button fills for ghost variants
- Frost Blue `#f0f5fa` for Subtle surface tint for alternating bands, header backgrounds - barely-there cool wash
- Linen Gray `#eaecf7` for Table dividers, hairline borders in data-heavy layouts - a cool neutral that doesn't fight the violet palette

- Haffer `--font-haffer` for Single-family system for everything from body to display. Weight 400 carries body, nav, and table text; weight 600 handles headings, buttons, and emphasis. The custom geometric construction gives a contemporary financial-tech voice - rounder apertures than Inter, tighter terminals than Geist.

## Avoid

- Don't introduce new hues - the system is binary: violet accents on white, or white on Deep Iris
- Don't use drop shadows on components other than the pricing card stack - depth should come from color and border
- Don't use sharp 0px or minimal 4px corner radii on cards - 16px is the minimum card radius and buttons must stay pill-shaped
- Don't place body text below 14px or above 18px - the system avoids both micro-copy and large body type
- Don't use #18181f and #000000 interchangeably - #000000 is reserved for navigation chrome; body text uses #18181f
- Don't add gradients - the system is flat by design; depth comes from violet-to-Deep-Iris section contrast
- Don't use weight 400 for headings or weight 600 for body - the binary weight assignment is part of the typographic signature

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
