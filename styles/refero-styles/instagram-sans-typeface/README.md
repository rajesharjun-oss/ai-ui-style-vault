# Instagram Sans Typeface

Source: [Refero Style](https://styles.refero.design/style/7d6a8722-a6f4-40de-a761-16ea479630a9)
Reference site: [https://about.instagram.com/brand/type](https://about.instagram.com/brand/type)
Captured: 2026-07-31
Refero published: 2026-04-30T01:43:26.461Z
Refero modified: 2026-06-05T08:24:39.157Z
Theme: mixed
Category: Media

## Style Summary

Explore Instagram Sans Typeface's mixed Media design system: Signal Pink #ff0169, Plasma Magenta #d300c5 colors, Instagram Sans, Instagram Sans Headline...

North star: Living type museum. Oversized black letterforms on slabs of neon, displayed like sculpture in a white room.

## What To Borrow

- Signal Pink `#ff0169` for Gradient origin - Instagram brand gradient start point, the chromatic anchor in the system
- Plasma Magenta `#d300c5` for Gradient midpoint - bridges hot pink into ultraviolet, used in the brand gradient only
- Ultraviolet `#7638fa` for Gradient terminus - deep violet end of the Instagram brand gradient, the cool counterweight
- Hot Magenta `#f689ff` for Full-bleed color panel - left half of the hero split, the loudest single surface in the system
- Lavender Mist `#c4a4f7` for Full-bleed accent band - right half of the hero split and secondary color sections, softens the magenta
- Graphite `#1c1e21` for Body text, button borders, list dividers, nav borders - the primary near-black for all text and hairline rules
- Pure Black `#000000` for Specimen letterforms, Instagram camera icon outlines, high-contrast graphic moments - flat black with no warmth
- Paper White `#ffffff` for Content canvas, text on color panels, button text, input backgrounds - the neutral ground that lets color panels pop
- Hairline Gray `#cccccc` for Subtle button borders and disabled-state rules
- Link Indigo `#385898` for Violet accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color

- Instagram Sans `--font-instagram-sans` for The brand's custom geometric sans. Used for everything from 12px captions to 389px specimen hero letterforms. Single weight 400 across the entire scale - the typeface achieves personality through geometry and tight negative tracking rather than weight contrast. Letter-spacing tightens as size grows: -0.02em at body, -0.03em at 32-46px, -0.035em at 62px and above.
- Instagram Sans Headline `--font-instagram-sans-headline` for Distinct variant for the 468px mega-specimen display - looser tracking (-0.006em) than the base family because at 468px the tight tracking would close letter apertures. Used only for the largest type specimen on the page.
- Helvetica `--font-helvetica` for System fallback appearing at 12px (likely OS-rendered small text) and 224px (possible secondary specimen). Treat as fallback only - Instagram Sans is the intended primary at all sizes.

## Avoid

- Do not use filled solid-color CTA buttons - the system expresses action through outlined Ghost buttons with Graphite borders
- Do not apply the brand gradient as a background wash, overlay, or card fill - it is reserved for the camera logo and the single signature gradient instance
- Do not use #385898 (Link Indigo) for buttons, fills, or large surface areas - it is a text-link color only
- Do not use font-weight 600+ or italic in Instagram Sans - the family ships weight 400 only
- Do not add drop shadows to specimen letterforms, cards, or panels - the system is flat, shadowless, and relies on scale contrast
- Do not use the Hot Magenta (#f689ff) as a text or small-icon color - it is a full-bleed surface panel color only
- Do not introduce additional typefaces - Helvetica appears only as a system fallback, never as an intentional design choice

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
