# Atoms

Source: [Refero Style](https://styles.refero.design/style/4433dfe7-315a-4459-bfd7-f59ccdc09bad) 
Reference site: [https://atoms.co](https://atoms.co) 
Captured: 2026-07-29 
Refero published: 2026-05-11T00:38:25.374Z 
Refero modified: 2026-06-03T18:52:37.329Z 
Theme: dark 
Category: AI

## Style Summary

Explore Atoms's dark AI design system: Champagne Gold #c8ad86, Candlelight Cream #fff7dd colors, Switzer, system-ui sans-serif typography, and DESIGN.md for...

North star: obsidian monolith in candlelight - a near-black canvas where a single warm champagne accent cuts like a blade through the darkness

## What To Borrow

- Champagne Gold `#c8ad86` for Accent headings, category tags, decorative borders - the only chromatic color in the system, used sparingly to mark emphasis and brand-bearing elements
- Candlelight Cream `#fff7dd` for Primary text, hairline borders, icon strokes - warm off-white reads softer than pure white against the black canvas
- Obsidian Black `#000000` for Page canvas, card surfaces, image backgrounds - absolute black dominates the visual field
- Ember Ash `#66635f` for Muted surface variation, secondary backgrounds, low-emphasis fills

- Switzer `--font-switzer` for Primary typeface for all headings, body, and navigation - a geometric sans with unusually tight tracking on display sizes (-0.042em at 44px) that creates a precision-engineered feel. Weight 400 for body, 500 for labels and tags. The negative letter-spacing on the 44px headline tightens the word shapes into compact, machined forms.
- system-ui sans-serif `--font-system-ui-sans-serif` for Fallback / system rendering for micro-UI and link text

## Avoid

- Do not use shadows, glows, or blur effects for elevation - define surfaces with borders only
- Do not introduce saturated colors beyond the champagne accent - no blues, greens, or reds
- Do not use pure white (#ffffff) for text - #fff7dd is warmer and on-brand
- Do not add background fills to cards or sections - they sit directly on the black canvas
- Do not use large border-radius values on cards (no 12px, 16px, 24px) - stay at 4px max for rectangles
- Do not apply letter-spacing to body text - keep tracking tight only on 16px+ sizes
- Do not animate color, position, or scale on load - the system is static and placed, not kinetic

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
