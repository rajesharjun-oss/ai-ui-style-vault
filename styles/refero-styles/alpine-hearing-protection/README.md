# Alpine Hearing Protection

Source: [Refero Style](https://styles.refero.design/style/76c761d8-4af1-4ed5-ba93-eeb60f7006b5) 
Reference site: [https://www.alpinehearingprotection.com](https://www.alpinehearingprotection.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T22:34:45.428Z 
Refero modified: 2026-06-03T21:52:56.978Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore Alpine Hearing Protection's light E-commerce design system: Cocoa Ink #200e0e, Signal Red #ed212d colors, Antarctica, GTStandard-M typography, and...

North star: Sunlit Scandinavian editorial. A cinnamon-ink wordmark on warm cream paper, with one red exclamation - the rest is photography and generous whitespace.

## What To Borrow

- Cocoa Ink `#200e0e` for Primary text, filled action buttons, card text, icon strokes, card borders - warm near-black replaces pure black throughout, giving every label a roasted, tactile quality
- Signal Red `#ed212d` for Red decorative accent for icons, marks, and small graphic details.
- Canvas White `#ffffff` for Page background, nav text, button labels on dark surfaces - the neutral base all warm tones sit on
- Blush Cream `#f8f0ec` for Card surfaces, soft elevated sections, product detail backgrounds - the warm secondary layer beneath the white canvas
- Rose Stone `#f3e7e2` for Badge backgrounds, subtle card elevation, border tints on light cards - a step warmer than Blush Cream for tag/label contexts
- Apricot Wash `#fde3d6` for Decorative illustration panels, soft highlight washes on icons and product imagery backgrounds
- Warm Gray `#d2cfcf` for Hairline borders, dividers, input field outlines on neutral surfaces
- Deep Espresso `#202020` for Secondary card backgrounds for dark product variants - used sparingly as a near-black with slight warmth
- Sage Mist `#9ac9b5` for Product color swatch - specific earplug variant color, not a system-wide token
- Dusty Rose `#dbb0b3` for Product color swatch - specific earplug variant color, not a system-wide token

- Antarctica `--font-antarctica` for Sole typeface across all UI: navigation, buttons, product cards, body, and display headlines. Custom geometric sans with slight warmth in the terminals. Medium-weight (545) is the workhorse for body and UI; 600 carries CTAs and product names; 400 appears in secondary metadata. Headlines compress with -0.02em tracking to feel editorial rather than airy.
- GTStandard-M `--font-gtstandard-m` for GTStandard-M - detected in extracted data but not described by AI

## Avoid

- Do not add box-shadows to any component - elevation comes from background-color shifts, never from blur or offset
- Do not round corners beyond 2.23px - no pill buttons, no large radii; the near-sharp aesthetic defines the system
- Do not use Signal Red (#ed212d) for buttons, links, or hover states - it is brand-identity color, not an action color
- Do not introduce drop shadows, gradients, or glassmorphism - the design is deliberately flat and print-like
- Do not use the product color swatches (Sage Mist #9ac9b5, Dusty Rose #dbb0b3) as system-wide accent tokens - they are product variant colors only
- Do not center-align body paragraphs or use fonts other than Antarctica (or its substitute); the single-typeface discipline is what makes the system feel like one publication
- Do not use pure black (#000000) for text or icons - always use Cocoa Ink (#200e0e) to maintain the warm tonal harmony

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
