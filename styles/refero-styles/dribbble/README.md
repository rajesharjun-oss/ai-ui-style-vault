# Dribbble

Source: [Refero Style](https://styles.refero.design/style/b8ce0a90-40c6-4518-940c-8c97ccf9c1a0)  
Reference site: [https://dribbble.com](https://dribbble.com)  
Captured: 2026-07-29  
Refero published: 2026-02-10T10:54:18.000Z  
Refero modified: 2026-06-05T05:18:12.682Z  
Theme: light  
Category: Design

## Style Summary

Explore Dribbble's light Design design system: Dribbble Pink #ea4c89, Midnight Ink #0d0c22 colors, Mona Sans typography, and DESIGN.md for AI agents.

North star: gallery wall at design week a quiet white room where one magenta spotlight circles each piece

## What To Borrow

- Dribbble Pink `#ea4c89` as Brand signature accent search submit button, PRO badge, logo mark, active heart, hover pulses one vivid magenta against the monochrome canvas makes the brand unmistakable at any size
- Midnight Ink `#0d0c22` as Primary text, filled primary buttons, dark surface fills, icon strokes a near-black with a cool blue undertone that reads warmer than pure black against white
- Deep Plum `#060318` as Navigation bar fill, darkest text tokens, logo wordmark slightly cooler and deeper than Midnight Ink for the fixed header band
- Charcoal Plum `#3d3d4e` as Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Smoke `#6e6d7a` as Secondary/muted body text, helper labels, view-count and heart-count numbers carries the dense meta layer beneath thumbnails
- Fog `#9e9ea7` as Tertiary text, placeholder text, disabled icons, checkbox idle state the lightest readable neutral
- Mona Sans Sole typeface across the product Mona Sans is a custom geometric humanist sans drawn by GitHub, used for everything from 9px meta labels to 48px hero headlines. Its openness keeps dense 4-column grids readable, and the 450/500 mid-weights carry the designer's brand without shouting `--font-mona-sans` for the source typography voice
- 4px base spacing with compact density
- Source radius system: cards 8px, badges 12px, inputs 12px, buttons 8px

## Avoid

- Don't use #ea4c89 for body text, icons, borders, or large fills it loses its meaning when overused.
- Don't add drop shadows to cards, buttons, or the navigation the system relies on color contrast and 8px radii for hierarchy.
- Don't use any color other than Midnight Ink or Deep Plum for filled dark buttons avoid #3d3d4 for primary CTAs.
- Don't apply radii above 16px to standard UI thumbnails are 8px, hero frames are 16px, and anything rounder reads as wrong.
- Don't introduce a second accent color the palette is monochrome plus one magenta, and a second accent will dilute the brand signal.
- Don't set body copy below 12px or above 16px the system compresses information at 1314px and reserves 48px for the hero only.
- Don't decorate the dark navigation with gradients, glows, or transparency keep it a flat #060318 band.

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
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
