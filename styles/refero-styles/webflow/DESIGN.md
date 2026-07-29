# Webflow Design Reference

## North Star

Build a sharp website-builder product page: white canvas, blue actions, exact borders, controlled radius, strong display typography, and credible product UI screenshots inside browser chrome. The system should feel capable, technical, and legible rather than warm, decorative, or lifestyle-led.

## Theme

- Mode: light.
- Canvas: white.
- Text: near-black.
- Accent: one primary blue.
- Borders: cool neutral gray.
- Elevation: border-first; shadow appears only for hover states or browser-frame product mockups.

## Color System

Core colors:

- Webflow Blue: `#146ef5` for filled primary actions, active navigation, links, badges, and key emphasis.
- Indigo Ink: `#1366e2` for secondary blue emphasis and dark-surface alternatives.
- Canvas White: `#ffffff` for primary page background and cards.
- Ink Black: `#080808` for primary text and inverted sections.
- Border Gray: `#d8d8d8` for 1px resting borders.
- Muted Text: `#5a5a5a` for supporting copy and logo strips.
- Mercury Tint: `#f0f0f0` for alternating section bands and subtle background blocks.
- Soft Blue: `#6ca7ff` for inline illustration detail only.
- Mint Pulse: `#60ed76` for inline illustration detail only.
- Orange Marker: `#ffa666` for inline illustration detail only.

Only `#146ef5` should carry interactive weight. Green and orange should not become app state colors or primary UI accents.

## Typography

Primary: WF Visual Sans Variable.  
Mono: WF Visual Sans Mono.  
Fallback: Inter or system sans when the Webflow fonts are unavailable.

The signature type move is a large, weight-600 headline with tight tracking.

- Hero display: 56-80px, line-height 1.04, letter-spacing -0.01em, weight 600.
- Section heading: 40-56px, line-height 1.08, letter-spacing -0.01em, weight 600.
- Card heading: 20-24px, line-height 1.2, weight 600.
- Body large: 20px, line-height 1.45, weight 400, muted text.
- Body: 16px, line-height 1.5, weight 400.
- Small body: 14px, line-height 1.45, weight 400.
- Eyebrow: 13px, weight 500, letter-spacing 0.1em, uppercase, muted text.
- Badge: 10px, weight 600, letter-spacing 0.1em, uppercase.
- Mono label: 13px, line-height 1.4, WF Visual Sans Mono.

Do not use serif, decorative display, or casual rounded fonts.

## Layout

- Max page rail: 1200px.
- Desktop grid: 12 columns.
- Hero: centered text stack on white, no hero photograph.
- Hero follow-up: 3-column card row.
- Section rhythm: 80px vertical gaps.
- Card padding: 24px.
- Card/grid gap: 16px.
- Below fold: alternate centered text blocks and two-column text/product sections.
- Mobile: collapse to single-column stacks.

Use whitespace as the section separator. Avoid heavy dividers.

## Shape

- Buttons, inputs, tags: 4px radius.
- Cards, screenshots, large containers: 8px radius.
- Avoid 9999px pill buttons.
- Borders are usually 1px solid `#d8d8d8`.

## Imagery

Photography is not the main device. The style is UI-led.

Use:

- Product UI captures.
- Realistic browser chrome.
- Clean editor screenshots.
- Monochrome customer logo rows.
- Flat inline illustrations in the constrained blue, soft blue, mint, and orange palette.

Avoid:

- Lifestyle photography.
- 3D hero objects.
- Decorative abstract gradients.
- Full-color logo clutter.

## Elevation

Resting cards should use borders. Use shadow for:

- Card hover feedback.
- Browser-frame product mockups.
- Floating CTA or sticky elements.

Do not apply shadows to every surface. Shadow should signal interaction or product-display depth.

## AI Build Notes

Start with a clean white page, a centered hero, a strong blue CTA, and a browser mockup. If the page feels flat, add a better product UI composition before adding more color.

