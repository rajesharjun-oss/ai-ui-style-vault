# Palmer

Source: [Refero Style](https://styles.refero.design/style/7cae43cd-dd0e-4658-86e6-d66935cfb213)
Reference site: [https://www.palmer-dinnerware.com](https://www.palmer-dinnerware.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:34:29.946Z
Refero modified: 2026-06-05T08:19:19.139Z
Theme: light
Category: E-commerce

## Style Summary

Explore Palmer's light E-commerce design system: Gallery Cream #f5f6ee, Ink #222222 colors, TWK Lausanne typography, and DESIGN.md for AI agents.

North star: Ceramic gallery in soft daylight - the interface is the wall, the objects are the art.

## What To Borrow

- Gallery Cream `#f5f6ee` for Page canvas and base surface - a warm off-white that flatters glazed ceramics more than pure white would
- Ink `#222222` for Primary text, hairline borders, card outlines, icon strokes - the entire structural skeleton runs through this one near-black
- Bone `#ffffff` for Product image backgrounds, occasional inverse surface when a card needs to sit forward of the cream canvas
- Fog `#a1a19c` for Muted secondary borders and low-priority text - used when Ink would be too heavy for a structural divider
- Lampblack `#000000` for Reserved for the rare filled element (active nav background, weight anchors) - used sparingly so Ink remains the default voice

- TWK Lausanne `--font-twk-lausanne` for Sole typeface - handles everything from micro-labels to 120px editorial display. Weight 300 carries display and large headings (whisper-thin Swiss grotesque that lets the ceramics dominate), weight 400-500 for body and UI, weight 600-700 reserved for active states and filter labels. The tight letter-spacing (-0.04em at display, -0.02em at body) is signature: characters nestle together, giving even 11px labels a compressed, considered feel rather than airy defaults.

## Avoid

- Don't introduce any chromatic accent color - the ceramics supply all the color, the UI stays grayscale
- Don't add drop shadows to cards, buttons, or nav - borders alone define depth
- Don't use corner radius above 100px or below 3px - the three tiers (3px, 9px, 100px) are the complete system
- Don't set type at weight 600+ in display sizes - it would overwhelm the whisper-thin signature of the 120px tier
- Don't use pure black (#000000) for text - Ink (#222222) is the text color; black is reserved for filled active states
- Don't add background color to the main canvas behind product photography - flat cream is non-negotiable
- Don't use letter-spacing 0 or positive values - all text tracks negative

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
