# Superintelligence for work

Source: [Refero Style](https://styles.refero.design/style/1db2adc9-2f10-4f20-af1b-27fa4b25f729) 
Reference site: [https://sanalabs.com](https://sanalabs.com) 
Captured: 2026-07-29 
Refero published: 2026-04-30T00:16:29.774Z 
Refero modified: 2026-06-05T00:23:14.900Z 
Theme: light 
Category: AI

## Style Summary

Explore Superintelligence for work's light AI design system: Ink #090909, Pure Black #000000 colors, Sana Sans typography, and DESIGN.md for AI agents.

North star: Architectural monograph on vellum - where the only ornament is letter-spacing and the only color is a single electric blue pressed into white space.

## What To Borrow

- Ink `#090909` for Primary text, hairlines, card and input borders, list dividers, link underlines - the dominant dark anchor of the system
- Pure Black `#000000` for Icon fills, heading underlines, occasional deep accents where maximum weight is needed
- Bone `#ffffff` for Page background, card surface, text on filled buttons, button borders for ghost controls
- Linen `#efefed` for Section band background, elevated card surface, the warm neutral that gives the white space its temperature
- Ash `#d9d9d9` for Footer divider, hairline rules where Ink would be too heavy
- Cobalt Pulse `#0057f3` for Single primary action fill per page - the only chromatic punctuation, reserved for the decisive CTA and never used decoratively
- Ember Signal `#ff5102` for Rare secondary action or notification accent - a warm counterpoint to Cobalt Pulse, used at most once per surface

- Sana Sans `--font-sana-sans` for Sole typeface across the entire system - display headlines at 83px set weight 500 with -2.5% tracking for a carved, architectural feel; section headings at 48px weight 500 with -0.96px tracking; body copy at 15-16px weight 400 with barely-perceptible negative tracking. The font is geometric and humanist, and the refusal to go above weight 500 is deliberate: confidence comes from restraint, not boldness.

## Avoid

- Don't add box-shadow to any component - depth comes from surface color shifts, not elevation
- Don't use Cobalt Pulse decoratively on icons, illustrations, tags, or backgrounds - it is a CTA color only
- Don't introduce gradients - the system is built on flat, single-value surfaces
- Don't go above weight 500 in the type scale; bold/700 breaks the restrained voice
- Don't use #0000ee or any unstyled link blue - links inherit Ink #090909
- Don't add corner radii smaller than 6px or use sharp 0px corners on content blocks
- Don't place colored backgrounds under text - every text surface is white, linen, or photographic

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
