# Hyper Tria

Source: [Refero Style](https://styles.refero.design/style/6665a3dd-606f-4fd1-80dd-a84e3b3a6226)
Reference site: [https://hypertria.com](https://hypertria.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:43:42.170Z
Refero modified: 2026-06-05T09:50:58.401Z
Theme: mixed
Category: Agency

## Style Summary

Explore Hyper Tria's mixed Agency design system: Ember Red #ee3a49, Hyper Green #0fa64b colors, Aeonik, -apple-system typography, and DESIGN.md for AI agents.

North star: chrome monolith in a white gallery

## What To Borrow

- Ember Red `#ee3a49` for Wordmark, navigation text, kicker labels, and the single chromatic accent that makes the otherwise monochrome system read as a brand. The warmth against pure black and white creates editorial urgency without tipping into alarm
- Hyper Green `#0fa64b` for Reserved for the rotating circular brand badge and high-prominence brand moments. A single saturated spot of color in an otherwise achromatic system - used sparingly so it lands as identity, not decoration
- Signal Blue `#007bff` for Outlined/ghost action border, image frame accent, and link underline. Functions as the system's cool counterweight to the warm Ember Red - used for bordered interactive elements rather than filled buttons
- Obsidian `#000000` for Page canvas in the hero, primary text color in light sections, and the dominant border color across all UI elements. Carries the heaviest weight in the system - defines edges, type, and spatial structure
- Paper `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces.
- Graphite `#666666` for Secondary navigation text and border color for tertiary UI elements. The middle tone that prevents the black/white binary from feeling stark in repetitive nav and list contexts

- Aeonik `--font-aeonik` for Primary typeface for all display, heading, and body text. Weight 300 at 75-90px with line-heights near 0.90-1.00 creates the system's signature sculptural headlines - letterforms lock together through aggressive negative tracking (-0.053em) rather than spacing. Mid-weight 400-500 handles body and UI at 19-20px with 1.45-1.70 line-height for generous readability.
- -apple-system `--font-apple-system` for System fallback for nav items, footer micro-copy, and supporting UI text where the custom Aeonik isn't loaded. Carries no distinctive role - purely a graceful degradation layer.

## Avoid

- Never add border-radius to any element - the sharp-edged geometry is a defining system constraint
- Never use a filled button background as a CTA - the system signals actions through outlined/ghost borders or typographic arrows only
- Never use shadows or box-elevation for depth - rely on background color contrast and typographic scale instead
- Never apply Ember Red (#ee3a49) to large background fills - it is an accent color for text and small marks only
- Never set display headline letter-spacing to 0 or positive values - the aggressive negative tracking on large type is signature
- Never use multiple chromatic colors in the same view - the system is monochrome with single-color punctuation per section
- Never use illustrations, abstract graphics, or decorative imagery - product photography and 3D type are the only visual elements

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
