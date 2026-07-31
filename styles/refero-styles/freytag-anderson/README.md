# Freytag Anderson

Source: [Refero Style](https://styles.refero.design/style/2d4fc4ba-2ea4-465f-8644-f3ff5c6713a2)
Reference site: [https://www.freytaganderson.com](https://www.freytaganderson.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:45:31.792Z
Refero modified: 2026-06-05T07:48:22.686Z
Theme: mixed
Category: Agency

## Style Summary

Explore Freytag Anderson's mixed Agency design system: Paper #fafafa, Ink #000000 colors, FAVORIT, Clarkson typography, and DESIGN.md for AI agents.

North star: cinema curtain rising on a single word.

## What To Borrow

- Paper `#fafafa` for Page canvas, base surface behind text - off-white, never pure white, to soften photographic edges
- Ink `#000000` for Primary text, hairline borders, link underlines - the only chromatic accent in the system is its absence of color
- Charcoal `#1c1c1c` for Dark content surface for text-only sections - warm-leaning black that softens contrast against pure ink
- Midnight Soil `#141109` for Deepest dark surface, used for the most recessed bands - barely distinguishable from charcoal but warmer
- Ash `#dcdcdc` for Hairline borders, disabled borders, subtle dividers - a neutral gray that whispers structure without drawing the eye
- Driftwood `#c2b5ae` for Warm taupe accent surface, used sparingly as a tonal break in dark sections - the only non-achromatic hint in the palette

- FAVORIT `--font-favorit` for The single typeface for everything: hero titles at 41px weight 400, body at 17px weight 400, captions at 15px weight 300. Weight 300 is the signature choice for secondary text - it creates hierarchy through restraint rather than bold contrast. Slight negative tracking (-0.02em to -0.022em) tightens the grotesque's default rhythm. The same family voices headlines, navigation, buttons, and body, which is unusual - most systems differentiate roles through typefaces. Here, FAVORIT's dual weight and tight letterforms carry the entire hierarchy alone.
- Clarkson `--font-clarkson` for Reserved for micro-copy or supporting text in specific contexts - appears at low frequency and never headlines. Could be a FAVORIT alternate cut rather than a true second family.
- halyard-display `--font-halyard-display` for Rare accent - appears in button or micro-label contexts. Functions as a display-only voice when FAVORIT needs to step aside.

## Avoid

- Do not add a chromatic accent color (blue, red, green) - the system is deliberately achromatic and a single hue would shatter the cinema metaphor.
- Do not add card shadows, drop shadows, or elevation tokens - the design is flat, relying on color contrast and whitespace for separation.
- Do not center text horizontally - the top-left anchor is the system's defining gesture.
- Do not add a traditional navigation bar with visible menu items - the hamburger is the only nav surface.
- Do not use multiple typefaces to create hierarchy - FAVORIT is the only voice, period.
- Do not frame or round images - photographs are presented raw, full-bleed, unbordered.
- Do not use bold (600+) weights - the system speaks at 300 and 400 only; heavier weights would break the whispered tone.

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
