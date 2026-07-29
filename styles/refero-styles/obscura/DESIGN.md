# Obscura Design Reference

## North Star

Build a friendly privacy product that feels like an 8-bit arcade console set on a soft cloud-paper canvas. The interface should be playful and protective, not dark and defensive. Pixel display type supplies the brand voice, while Manrope keeps the product usable.

## Theme

- Mode: light.
- Canvas: full-bleed Cloud Mist.
- Cards: Paper White.
- Text: Graphite Ink.
- Accent: one Signal Orange.
- Footer: Ember Crust.
- Imagery: pixel clouds, pixel mascots, app-window mockups.

## Color System

Core colors:

- Signal Orange: `#ff5e24` for the primary CTA, hero emphasis, active nav, link hover, and card accent borders.
- Ember Crust: `#6c3200` for the footer and rare dark brand block.
- Cloud Mist: `#e3f1fe` for page canvas, card wash, secondary button borders, and pixel-art fill.
- Graphite Ink: `#232629` for primary text, nav links, icons, and body copy.
- Paper White: `#ffffff` for cards, app chrome, and nav backgrounds.
- Slate Pencil: `#5c6066` for secondary copy and muted icons.
- Ash Mist: `#989ea4` for tertiary copy, placeholders, and disabled details.
- Blush Shadow: `#dbced0` for warm-tinted shadow bases.
- Midnight Ink: `#101828` for strong headline or button text where orange needs high contrast.

Only Signal Orange should feel loud. Do not create a second accent system.

## Typography

Display family: Jersey 10.  
UI and body family: Manrope Variable.

Jersey 10 is for display and headings only:

- Heading small: 36px, line-height 1.11, letter-spacing -0.9px.
- Heading: 48px, line-height 0.85, letter-spacing -1.2px.
- Heading large: 60px, line-height 0.85, letter-spacing -1.5px.
- Display: 96px, line-height 0.8, letter-spacing -3px.

Manrope carries readable UI:

- Caption: 12px, line-height 1.5.
- Body small: 14px, line-height 1.43.
- Body: 16px, line-height 1.5.
- Subheading: 18px, line-height 1.56.
- Buttons and nav: 14-16px, weight 500.
- Body copy: weight 400.
- Emphasis: weight 600-700.

Never use Jersey 10 below 36px or for functional controls.

## Layout

- Page max width: 1200px.
- Base unit: 8px.
- Section gap: 48px.
- Card padding: 16px.
- Element gap: 16px.
- Hero: centered stack on Cloud Mist.
- Hero copy max width: around 560px.
- Card grids: 2 or 3 columns on desktop, 1 column on mobile.
- App mockup: large centered product window below the hero.
- Footer: full-width Ember Crust band.

There are no hard horizontal section dividers. Pixel cloud clusters act as visual breathers.

## Shape

- Buttons, nav, tags, links: 6px radius.
- Feature cards: 12px radius.
- Large app cards: 16px radius.
- Images: 24px radius.
- Feature panels: 32px radius.

This contrast matters: small controls are compact, cards are soft, and panels feel friendly.

## Shadows

Use soft blue-tinted and warm-tinted shadows to make cards float on cloud paper. Shadows should feel lightweight, not heavy.

Good uses:

- Feature cards.
- App-window mockup.
- Pressed primary button.

Avoid dark generic box shadows.

## Pixel Art Direction

All decorative graphics should be hand-authored 8-bit pixel art:

- Fixed 16x16 or 32x32 base grid.
- Flat fills with 1-3 colors per object.
- 1px darker-tone outline.
- No anti-aliasing.
- Clouds use Cloud Mist, Paper White, and Slate Pencil outlines.
- Sprites drift into corners and section gaps.

If a curve looks smooth, it is wrong for this style.

## AI Build Notes

Start with the Cloud Mist canvas, a centered pixel headline, one orange CTA, and two pixel cloud sprites. Add the product mockup after the first fold, then build feature cards with Jersey headings and Manrope body text.

