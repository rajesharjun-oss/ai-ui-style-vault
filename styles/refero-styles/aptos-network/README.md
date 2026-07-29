# Aptos Network

Source: [Refero Style](https://styles.refero.design/style/9a23d457-a23a-404a-9f75-12007ea7eb0f) 
Reference site: [https://aptosnetwork.com](https://aptosnetwork.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:40:48.500Z 
Refero modified: 2026-06-03T20:32:43.164Z 
Theme: light 
Category: Crypto

## Style Summary

Explore Aptos Network's light Crypto design system: Ink #0f0e0b, Bone #f9f9f0 colors, Season Serif typography, and DESIGN.md for AI agents.

North star: Earth-toned code atelier - a sage-walled observatory where terracotta, sand, and powder-blue panels hold monospaced code beside serif prose, framed by 1px ink hairlines.

## What To Borrow

- Ink `#0f0e0b` for Primary text, hairline borders, icon strokes, nav outlines - the near-black that carries 90% of all foreground weight. Not pure black: a warm brown-black that feels printed, not screened
- Bone `#f9f9f0` for Page canvas, card surfaces, nav-pill fill, button text on dark - a warm off-white with the faintest yellow-green cast that matches the sage and sand sections without competing
- Ash `#6d6c67` for Secondary text, subtle borders, muted metadata - a mid neutral that sits between Ink and the page; used when primary text would be too heavy
- Charcoal `#21201c` for Filled CTA buttons, active markers - slightly warmer than Ink; the button fill that reads as a dense matte stamp rather than a flat black
- Graphite `#555450` for Tertiary text, low-emphasis borders - for labels and helper text that should recede further than Ash
- Mist `#84837d` for Heading borders, de-emphasized dividers - the lightest neutral that still registers as a line on Bone
- Deep Earth `#3d3b34` for Alternate surface for code-adjacent panels and inset blocks - a warm dark that bridges Ink and the mid neutrals
- Soft Sand `#ccc5a3` for Secondary section background, 1px sand-colored hairline dividers, striped-pattern accent - the warm neutral that lives between the chromatic sections and true gray
- Warm Stone `#9d937c` for Khaki section background, tonal counterpoint to Sage - the muted olive-khaki that fills body-text sections and grounds the palette's middle register
- Sage `#d5fad3` for Hero section background, signature accent - a desaturated mint that signals freshness without being loud; the only color bold enough to hold a 120px headline
- Powder Blue `#badbee` for Code-panel background, striped-pattern accent, 1px blue hairlines - the cool counterweight to all the warm earth tones; appears wherever monospace code or technical data lives

- Season Serif `--font-season-serif` for Sole typeface - display, headings, body, nav, buttons, footer, code labels. Custom variable serif with fractional weights (no standard 300/400/700 scale) that allow whisper-light display at 335-340 and confident body at 420-444.

## Avoid

- Do not use any sans-serif typeface. Season Serif carries everything, including buttons, nav, and code labels.
- Do not use drop shadows. The system is flat by design - all line work is 1px inset.
- Do not use border-radius on cards, panels, code blocks, or images. Only buttons and the nav pill are rounded (9999px).
- Do not use bright or saturated colors. Every chromatic value is muted: sage, khaki, sand, powder blue. Saturation above 40% breaks the system.
- Do not use smooth gradients. The decorative right-side panels are hard-edge striped patterns implemented with sharp linear-gradient color stops.
- Do not use standard font weights (300, 400, 700). Season Serif uses fractional weights (335, 340, 420, 444) - pick from the available scale.
- Do not place text on both halves of a split section. The right side is always decorative (striped pattern or code panel), never text.

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
