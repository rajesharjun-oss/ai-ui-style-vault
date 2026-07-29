# Hyer Aviation Style Reference

Hyer Aviation is a luxury travel editorial system built around architectural type, a near-monochrome palette, one clay accent, and a sculptural aircraft hero. The design should feel like a premium aviation brand: restrained, spacious, high-contrast, and deliberately expensive.

## Theme

Mixed, aviation, luxury travel, editorial, monochrome, architectural, spacious, pill-action, product-hero.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Deep Ink | `#000d10` | `--color-deep-ink` | Primary text, footer, filled buttons, icon strokes, and brand structure. |
| Pure White | `#ffffff` | `--color-pure-white` | Page canvas, white content bands, card surfaces, and text on dark buttons. |
| Cool Ash | `#8e8e95` | `--color-cool-ash` | Secondary body copy, nav items, helper labels, and muted links. |
| Pebble | `#d5d3d4` | `--color-pebble` | Hairline dividers, borders, and subtle section edges. |
| Midnight Hull | `#0f0f1c` | `--color-midnight-hull` | Full-bleed dark sections and support bands. |
| Charcoal Deck | `#151623` | `--color-charcoal-deck` | Dark panels and deeper section layers. |
| Clay Ember | `#bc7155` | `--color-clay-ember` | One featured card, one highlighted offering, or a small decorative focal fill. |

## Typography

### HelveticaNowDisplay

Use as the sole major typeface across the system.

- Token: `--font-helveticanowdisplay`
- Fallback: Neue Haas Grotesk Display, Inter, Helvetica Neue
- Weights: 400, 700
- Sizes: 17px, 18px, 20px, 23px, 30px, 37px, 52px, 60px, 63px, 131px, 187px
- Line height: 0.80 at hero scale, 1.00 for headings, 1.61 for body.
- Role: turns display copy into a physical architectural object.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 17px | 1.00 | 0 | `--text-caption` |
| Body | 18px | 1.61 | 0 | `--text-body` |
| Nav | 20px | 1.00 | 0 | `--text-nav` |
| Subheading | 23px | 1.00 | -0.23px | `--text-subheading` |
| Heading SM | 30px | 1.00 | 0 | `--text-heading-sm` |
| Heading | 37px | 1.00 | -0.37px | `--text-heading` |
| Heading LG | 52px | 1.00 | -0.52px | `--text-heading-lg` |
| Display | 63px | 1.00 | -1.26px | `--text-display` |
| Display XL | 131px | 1.00 | -2.62px | `--text-display-xl` |
| Hero | 187px | 0.80 | -3.74px | `--text-hero` |

## Spacing And Shape

- Density: spacious.
- Base unit: 4px.
- Max width: 1200px.
- Section gap: 80px.
- Card padding: 22px.
- Element gap: 16px.

### Spacing Scale

`11, 13, 15, 16, 17, 21, 22, 23, 31, 34, 38, 52, 53, 59, 68, 119`

### Radius Scale

| Element | Radius |
|---|---:|
| Nav | 1000px |
| Buttons | 1000px |
| Decorative forms | 45px |
| Hero panels | 0px |
| Icon buttons | 100% |

## Components

### Filled Dark Pill Button

Deep Ink background, Pure White text, 1000px radius, 15px 22px 16px padding, HelveticaNowDisplay 17px/700. Use for confident primary actions on light backgrounds.

### Ghost White Pill Button

Transparent background, Pure White text, 1px white border, 1000px radius, matching pill padding. Use on dark bands or image-heavy hero contexts.

### Circular Icon Button

Deep Ink circular control with a white icon. Use for compact menu, navigation, or carousel affordances.

### Featured Clay Card

Clay Ember background, Pure White text, 0px radius, 53px 59px padding. Use once per page for the highlighted service or offer.

### Standard White Card

Pure White background, 0px radius, no border, no shadow. Use surrounding whitespace and Pebble hairlines for structure.

### Hero Wordmark

Oversized brand wordmark, around 131px, weight 700, tight tracking, Deep Ink, flush-left. Treat it as part of the hero architecture.

### Hero Headline

60px to 63px, weight 700, line-height 1.0, tight tracking, Deep Ink. End the main hero statement with a period.

### Section Headline

37px to 52px, weight 700, line-height 1.0, tight tracking, Deep Ink. Use short stacked lines.

### Feature Block

23px bold title in Deep Ink, 18px body in Cool Ash with 1.61 line-height, and a Pebble hairline above or between items. Arrange in 2x2 grids.

### Dark Content Section

Full-bleed Midnight Hull or Charcoal Deck background, white heading and body, right-aligned column. Use for support, contact, language, or terminal-like content.

### Footer Terminal

Full-bleed Deep Ink footer with large white wordmark, Cool Ash links, and multi-column navigation.

### Top Navigation

Transparent over the hero, with text links and a circular menu/action button. Items are large for nav, around 20px, and keep the system airy.

## Layout

Use full-bleed bands that alternate between pale atmospheric hero, Pure White content sections, and deep midnight sections. The hero is asymmetric: huge wordmark flush-left, headline to the right, and a clean private jet render floating through the lower center. Content sections can lean rightward with a heading and a 2x2 feature grid. Use 80px vertical rhythm and let color shifts separate sections instead of dividers.

## Imagery

Use a single hero aircraft image or 3D render as the star: white jet, dark striping, clean three-quarter banking pose, isolated against pale sky or white. Keep aircraft imagery product-like and precise. Avoid lifestyle scenes, airports, passengers, busy skies, generic travel stock, and decorative illustration. Icons should be minimal strokes in Deep Ink.

## Do

- Set headlines from 23px upward at weight 700.
- Use huge display type with tight tracking.
- Use Deep Ink as the structural text, CTA, icon, and footer color.
- Reserve Clay Ember for one featured card or one focal offer.
- Use 1000px radius for every button and nav pill.
- Keep body copy at 18px with generous 1.61 leading.
- Alternate white sections with dark midnight bands.
- End the main hero headline with a period.

## Don't

- Do not add shadows to cards or buttons.
- Do not introduce extra accent colors.
- Do not use Deep Ink as a light-section page background.
- Do not round the featured clay card.
- Do not set body copy below 18px.
- Do not use thin or light headings.
- Do not place two Clay Ember feature blocks in one viewport.
