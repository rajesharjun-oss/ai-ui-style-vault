# Surfshark

Source: [Refero Style](https://styles.refero.design/style/4fc7a535-3c99-4ffe-8365-7d025d33274e)
Reference site: [https://surfshark.com](https://surfshark.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:47:50.547Z
Refero modified: 2026-06-05T10:46:21.276Z
Theme: light
Category: SaaS

## Style Summary

Explore Surfshark's light SaaS design system: Surfshark Teal #1ebfbf, Coral Pulse #fa3556 colors, Inter typography, and DESIGN.md for AI agents.

North star: crisp ocean horizon at golden hour - warm coral sun meets teal sea, all floating on white sand

## What To Borrow

- Surfshark Teal `#1ebfbf` for Brand mark icon, accent highlights, inline link emphasis - the signature chromatic thread that ties logo, headings, and accent text together
- Coral Pulse `#fa3556` for Primary action buttons, high-urgency CTAs - warm pink-red against the cool palette creates immediate conversion pull
- Promo Gold `#ffc200` for Promotional banner background, limited-time deal strips - golden yellow reserved exclusively for urgency framing
- Charcoal Ink `#16191c` for Primary text, dark hero backgrounds, footer surfaces, button text on coral - near-black with a hint of cool depth
- Pure White `#ffffff` for Page canvas, card surfaces, button text on dark fills, text on coral CTAs
- Fog White `#f9f9f9` for Alternate canvas surface, subtle card backgrounds, soft section differentiation from pure white
- Tide Tint `#e8f7f8` for Faint teal-tinted surface wash - barely-perceptible background variant for feature blocks
- Ash Gray `#dadadd` for Light borders, dividers, subtle separation lines - cooler-toned hairline color
- Mist Gray `#bfbfc0` for Secondary borders, disabled states, heavy-use divider color (highest neutral frequency after black)
- Slate `#5b6065` for Muted body text, secondary copy, icon strokes in resting state
- Graphite `#393e41` for Navigation borders, tertiary UI elements, slightly lighter than Charcoal for layered depth
- Carbon `#000000` for Maximum-contrast borders, SVG icon fills, structural strokes - used heavily for crisp 1px rules
- Deep Abyss `#1e2327` for Alternate dark surface - slightly bluer than Charcoal, used in distinct dark panels

- Inter `--font-inter` for Sole typeface across the entire product - 400 for body and descriptions, 600 for navigation, subheadings, and emphasis, 700 for display headlines and button labels. Inter's geometric neutrality and tall x-height keep the system legible at 12px captions while the 60px display weight holds authority without requiring a custom display face.

## Avoid

- Don't use #1ebfbf as a button fill - teal is for brand identity, icons, and inline accent text, not for conversion surfaces.
- Don't apply shadows to cards - the system relies on background contrast and 48px radius for elevation, not drop shadows.
- Don't use border-radius values outside the scale: 8, 12, 32, 48, 64, 96px. Intermediate values break the visual language.
- Don't place two coral CTAs in the same viewport - one coral per view, the rest dark or ghost.
- Don't use the yellow #ffc200 outside promotional banners - leaking it into feature blocks dilutes its urgency signal.
- Don't use serif, display, or decorative fonts - Inter at multiple weights covers the full hierarchy.
- Don't set body text below 16px on marketing pages; 14px is the minimum and only for captions and micro-copy.

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
