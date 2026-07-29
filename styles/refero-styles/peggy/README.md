# Peggy

Source: [Refero Style](https://styles.refero.design/style/0ed4e85f-f3e9-438c-bc34-2a726863c602) 
Reference site: [https://peggy.com/royalties](https://peggy.com/royalties) 
Captured: 2026-07-29 
Refero published: 2026-04-30T03:57:40.285Z 
Refero modified: 2026-06-03T21:31:50.536Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore Peggy's light E-commerce design system: Gallery White #ffffff, Canvas Mist #f4f4f4 colors, Reckless, Inter typography, and DESIGN.md for AI agents.

North star: monochrome art gallery on a winter morning - the only color comes from the work on the walls

## What To Borrow

- Gallery White `#ffffff` for Card surfaces, input fields, button text on dark fills, nav surface over dark strips
- Canvas Mist `#f4f4f4` for Page background; also functions as the universal hairline border (borderColor 572 occurrences across every context) - the system draws structure with the canvas color itself
- Ink Black `#000000` for Primary text, logo, nav labels, body copy - the strongest type color, never used as a surface
- Charcoal `#141414` for High-contrast neutral action fill for primary buttons on light surfaces.
- Fog `#e2e8f0` for Muted accents, icon fills at rest, secondary surface tint, subtle dividers where Canvas Mist is too light
- Graphite `#666666` for Secondary/muted text - helper copy, metadata in transaction cards, footer body, link at rest

- Reckless `--font-reckless` for All display and heading copy. Weight 300 at the largest sizes (48-60px) is the signature move - most gallery/marketplace sites use 600-700 serif weights; the light cut reads as editorial restraint rather than shouting authority. Weight 400 takes over for 20-36px subheadings. Line-height collapses from 1.40 at 20px to 1.00 at 60px, letting large display text sit tight like a magazine cover.
- Inter `--font-inter` for All UI chrome: nav labels, button text, body paragraphs, helper copy, card metadata. Inter is deliberately invisible here - it serves Reckless by getting out of the way. Weight 500 appears in nav and active states; 400 is the body default. Line-height opens up to 1.50 at 16px for paragraph readability.
- Monument Grotesk `--font-monument-grotesk` for Footer column labels ('Product', 'Partners', 'Company', 'Support', 'Get the App') and the copyright line. Acts as a structural label typeface - small caps category architecture under a serif body. Strictly 12px, weight 400, used at 11 occurrences, signaling intentional scarcity.

## Avoid

- Do not add rounded corners (4px, 8px, 12px) to cards, buttons, or inputs - the system is deliberately sharp-edged, reserving curvature for pill-masked photography only
- Do not use colored badges, tags, or status pills (no green for success, no red for error) - the palette is grayscale only; communicate status through text or icon shape
- Do not use Reckless at weight 400 for display-size text; the serif loses its whisper quality and reads as ordinary at 60px
- Do not apply drop shadows, colored glows, or colored borders to elevate cards - elevation is expressed through surface color contrast (#f4f4f4 canvas vs #ffffff card), never through shadow
- Do not place CTAs anywhere except inside the top nav and as the primary action of a section; ghost links handle all secondary actions
- Do not use Monument Grotesk for body copy or headings - it is a 12px label-only typeface; using it elsewhere breaks the typographic hierarchy
- Do not introduce illustrations, icons with chromatic fills, or decorative gradients; the brushstroke curve is the only ornamental element and it should not be replicated

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
