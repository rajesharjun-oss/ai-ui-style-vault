# Zora

Source: [Refero Style](https://styles.refero.design/style/5c4eb249-fa38-4254-81e0-a32ee22766e2)
Reference site: [https://zora.co](https://zora.co)
Captured: 2026-07-31
Refero published: 2026-01-20T18:56:34.000Z
Refero modified: 2026-06-05T10:47:22.591Z
Theme: light
Category: Crypto

## Style Summary

Explore Zora's light Crypto design system: Void Black #121212, Graphite #4d4d4d colors, MonumentGrotesk typography, and DESIGN.md for AI agents.

North star: Neon gallery on graphite glass.\n\n{

## What To Borrow

- Void Black `#121212` for Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color
- Graphite `#4d4d4d` for Secondary text, body copy, icons, nav labels, metadata
- Fog Gray `#878787` for Muted helper text, tertiary metadata, inactive icon strokes
- Ash `#cacaca` for Placeholder text, light borders, disabled strokes
- Hairline `#e6e6e6` for Input borders, dividers, subtle separators
- Pure White `#ffffff` for Canvas background, card surfaces, button text on dark fills
- Reactor Green `#00df00` for Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Voltage Pink `#ff00f0` for Secondary accent for live indicators, countdown timers, hot tags, creator highlights
- Onyx `#000000` for Icon fills, logo mark, maximum-contrast text on light backgrounds

- MonumentGrotesk `--font-monumentgrotesk` for Sole typeface across all UI: nav labels, body text, button text, metadata, card titles. The custom geometric grotesque's compressed forms and uniform 410-500 weights create a label-density voice rather than a reading voice; it treats copy as UI chrome, not as prose. No display-weight contrast is used - hierarchy is achieved through size and color, not weight amplitude.

## Avoid

- Don't add shadows to cards - surfaces sit flat against the canvas, elevation is expressed by background contrast only
- Don't introduce additional accent colors beyond #00df00 and #ff00f0 - the two-color neon system is deliberately limited
- Don't use weights above 600 - the type system is calibrated for label density, not editorial display
- Don't center-align body text or card titles - left-align everything except hero headlines
- Don't use border-radius values other than 8px (buttons/inputs), 12px (cards), or 9999px (pills) - mixing radii breaks the system
- Don't add gradients to UI chrome - the gray gradient is reserved for skeleton/loading states only
- Don't use color to indicate state on form inputs - use border color shift (#cacaca #121212) instead of fills

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
