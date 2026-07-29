# Lottielab

Source: [Refero Style](https://styles.refero.design/style/1f782141-d407-4c27-8cee-2246720a9f42) 
Reference site: [https://www.lottielab.com](https://www.lottielab.com) 
Captured: 2026-07-29 
Refero published: 2026-05-07T12:13:20.844Z 
Refero modified: 2026-06-03T22:00:45.943Z 
Theme: light 
Category: Design

## Style Summary

Explore Lottielab's light Design design system: Electric Violet #7270ff, Signal Blue #1560fb colors, Plus Jakarta Sans, Google Sans Code typography, and...

North star: Animation studio on bright paper

## What To Borrow

- Electric Violet `#7270ff` for Primary CTA buttons, active nav items, accent keywords in headlines, focus rings - the only chromatic element allowed to break the monochrome canvas, making every action feel switched on
- Signal Blue `#1560fb` for Secondary accent for interactive highlights, selected states in tool surfaces, and inline brand emphasis where a cooler note is needed
- Deep Indigo `#2f2b4a` for Primary text and headings - a near-black with a violet undertone that warms the monochrome palette and distinguishes the brand from flat-charcoal SaaS defaults
- Midnight Ink `#1c1a2c` for Heaviest text weight, section titles, and surface-dark contexts - a deeper step than Deep Indigo for maximum contrast moments
- Slate `#4b5563` for Secondary body text, descriptions, metadata - sits between Deep Indigo and Silver for layered reading hierarchy
- Silver `#9ca3af` for Muted helper text, placeholder copy, disabled labels, and icon secondary tones
- Fog `#d9dbda` for Icon strokes at rest, subtle surface borders, low-emphasis dividers
- Mist `#e5e7eb` for Primary hairline borders across cards, inputs, dividers, and component edges - the dominant structural neutral
- Paper `#ffffff` for Card surfaces, elevated panels, button text on violet fills, inverted icon strokes
- Bone `#f9fafb` for Alternate surface for nested panels, input fills, quiet sections within white pages
- Pebble `#f3f4f6` for Page canvas, section bands between white blocks, product mockup backgrounds, footer wash
- Sunset Gradient `#facc15` for Decorative gradient endpoint for marketing visuals and showcase cards
- Bloom Gradient `#ec4899` for Decorative gradient endpoint for showcase cards and hero illustration accents

- Plus Jakarta Sans `--font-plus-jakarta-sans` for Sole typeface across the product. Geometric humanist sans with subtly squared terminals - contemporary but not cold. Weight 700 carries display and headings for confident vertical presence; weight 500 serves UI controls and labels; weight 400 handles body and descriptions. The slight openness in counters at small sizes keeps labels legible on dense tool surfaces.
- Google Sans Code `--font-google-sans-code` for Google Sans Code - detected in extracted data but not described by AI

## Avoid

- Don't introduce additional brand hues - the palette is intentionally violet-only; resist adding teals, greens, or pinks to core UI.
- Don't use shadows, glows, or blur effects for elevation; rely on surface color stepping and 1px hairline borders instead.
- Don't set body text below 14px or use weights under 400 - the type system is calibrated for comfortable reading at 16px+.
- Don't apply gradient fills to buttons, inputs, or navigation - gradients are reserved for showcase and marketing visuals only.
- Don't use pure #000000 for text on light backgrounds; use Deep Indigo (#2f2b4a) to preserve the warm violet undertone of the brand.
- Don't break the 8px spacing grid - all padding, gaps, and margins should land on multiples of 8 (with 4px and 2px allowed only for micro-adjustments inside components).
- Don't stack multiple violet elements on a single screen - one chromatic moment per viewport keeps the accent meaningful.

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
