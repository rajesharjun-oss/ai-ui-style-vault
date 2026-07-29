# Frontify - Style Reference

Frontify feels like a warm brand atelier: a cream museum-catalog canvas, precise ink rules, white product cards, a deep teal editorial stage, and one vivid orange accent used like a deliberate mark.

**Theme:** light

## Summary

Build this style with quiet restraint. The page should feel editorial, premium, and operational at the same time: large serif headings, crisp sans UI labels, generous cream sections, thin black borders, rounded media, and no decorative shadow system. Orange should appear rarely and intentionally.

## Tokens - Colors

| Name | Value | Token | Role |
|---|---:|---|---|
| Warm Parchment | `#f0f0eb` | `--color-warm-parchment` | Page canvas, large section fill, warm replacement for stark white |
| Gallery White | `#ffffff` | `--color-gallery-white` | Cards, elevated panels, button text on dark fills |
| Soft Linen | `#e1e1db` | `--color-soft-linen` | Secondary grouped surfaces and quiet card backgrounds |
| Mist Gray | `#d7d7cf` | `--color-mist-gray` | Subtle fills and body section dividers |
| Pale Stone | `#cbcbc5` | `--color-pale-stone` | Light hairline borders on neutral surfaces |
| Ash Gray | `#bfbfb8` | `--color-ash-gray` | Icon strokes, secondary borders, muted decoration |
| Graphite Warm | `#575753` | `--color-graphite-warm` | Secondary card text and muted labels |
| Charcoal Warm | `#464643` | `--color-charcoal-warm` | Body-level borders and secondary text |
| Ink | `#111110` | `--color-ink` | Primary text, hairline borders, filled buttons |
| Signal Orange | `#ff3b00` | `--color-signal-orange` | Sole chromatic accent for small functional highlights |
| Deep Teal | `#042a2b` | `--color-deep-teal` | Dark hero and editorial feature sections |

## Typography

Use `Cranny` for display and editorial headings. Keep it light, high contrast, and large. Use `ABC Diatype` for navigation, buttons, body copy, breadcrumbs, labels, and product UI. `Satoshi` can support small body moments, and `Cabinetgrotesk` can appear only as a heavier display counterpoint.

| Role | Font | Size | Weight | Line Height | Tracking |
|---|---|---:|---:|---:|---:|
| Hero display | Cranny | 80-96px | 300 | 0.86-0.9 | -0.008em |
| Section heading | Cranny | 40-61px | 300-400 | 0.95-1.0 | -0.006em |
| Subheading | Cranny | 24px | 400 | 1.1 | 0 |
| Body large | ABC Diatype | 18px | 400 | 1.43 | 0.010em |
| Body | ABC Diatype | 16px | 400 | 1.43 | 0.010em |
| Caption and UI | ABC Diatype | 12-14px | 400-500 | 1.3 | 0.010em |

## Spacing And Shape

- Density: comfortable
- Base unit: 8px
- Page max width: 1200px
- Section gap: 80px
- Card padding: 32px
- Element gap: 8-16px
- Card radius: 8px
- Image radius: 18px
- Nav pill radius: 32px
- Large button radius: 40px
- Small button radius: 24px

## Components

**Top Navigation Bar**

Warm Parchment background, about 64px tall. Left side holds the logo and dropdown-style nav items. Right side uses a pricing link, language selector, ghost login pill, and filled demo pill. Borders are 1px Ink; no shadows.

**Dark Hero Section**

Full-bleed Deep Teal with centered content. Use a 80-96px Cranny heading in white, ABC Diatype 18px support copy at reduced opacity, a two-button row, and an optional centered product preview image with 18px radius.

**Filled Dark Button**

Ink fill, white text, ABC Diatype 14px 500, radius 24px compact or 40px large, padding around 12px 20px. No border and no shadow.

**Ghost Button**

Transparent fill with 1px border. Use white border on dark sections and Ink border on light sections. Keep text 14px ABC Diatype with slight positive tracking.

**Logo Bar**

Horizontal partner logo strip on cream. Use black or grayscale logos with generous spacing and no cards.

**Feature Heading Block**

Centered Cranny heading with Graphite Warm supporting copy. Keep gaps at 16-24px and vertical section padding around 80px.

**Upload Drop Zone**

Cream background, 1px dashed Pale Stone border, 8px radius, centered icon and label stack, minimum height around 320px.

**Media Library Card**

White 8px-radius card with 32px padding. Include breadcrumb header, a 4x2 image grid, and small pill tags for asset metadata.

**Overlapping Image Tile**

Rounded media tile with 18px radius, no border, slight 2-3 degree rotation, and small overlaps to feel like a brand board rather than a rigid dashboard.

**Pill Tag**

White fill, 1px Pale Stone border, Ink text, ABC Diatype 12-14px, 9999px radius, 6px 12px padding.

**CTA Card With Glass Overlay**

Use a translucent white panel over photography with 18px radius. Signal Orange can appear as the small action control, ideally as an icon button rather than a large banner.

## Layout And Imagery

- Use a centered 1200px max-width container on Warm Parchment.
- Start with a full-bleed Deep Teal hero.
- Alternate cream editorial sections with white cards and asset previews.
- Use 80px vertical rhythm between major sections.
- Prefer real product imagery, brand assets, thumbnail grids, and lifestyle/creative-operations visuals.
- Keep images content-forward, warm-toned, and high contrast.
- Avoid flat illustration systems and decorative abstract backgrounds.

## Implementation Rules

Use thin Ink hairlines and neutral layering for structure. Do not add drop shadows, large gradients, extra accent colors, or overly rounded cards. Reserve orange for the one visual shout in the room.
