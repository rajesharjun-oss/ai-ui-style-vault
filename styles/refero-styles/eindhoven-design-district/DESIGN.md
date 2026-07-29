# Eindhoven Design District Style Reference

> A graphic modernist poster system: stark black and white, Helvetica-only typography, sharp rectangular imagery, and vivid color blocks used as punctuation.

## Theme

Light.

Eindhoven Design District is direct, graphic, and rectilinear. It relies on maximum contrast, strong type, and clean photographic rectangles. The style is almost entirely black and white, with only a narrow gray range and a few vivid accent colors reserved for content emphasis or decorative poster blocks.

## Core Principles

1. Use black and white as the primary visual system.
2. Treat typography as a graphic object.
3. Use Helvetica Now only, changing size and weight instead of changing typefaces.
4. Keep images and cards rectangular with 0px radius.
5. Use 1px black borders for crisp definition.
6. Make interactive buttons and tags large pills with 500px radius.
7. Use vivid red, pink, or blue only as occasional punctuation.
8. Avoid shadows, gradients, soft elevation, and decorative icon styles.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Canvas White | `#ffffff` | `--color-canvas-white` | Page background, cards, ghost button fill |
| Ink Black | `#000000` | `--color-ink-black` | Primary text, borders, icons, dark sections |
| Ash Gray | `#e8e8e8` | `--color-ash-gray` | Secondary card surface and subtle section break |
| Silver Thread | `#bfbfbf` | `--color-silver-thread` | Fine lines, quiet borders, low-emphasis text |
| Focus Red | `#ff0000` | `--color-focus-red` | Content emphasis and decorative accent |
| Blush Pink | `#ffc2eb` | `--color-blush-pink` | Decorative featured-section block |
| Electric Blue | `#0f26ed` | `--color-electric-blue` | Decorative high-energy block |

## Typography

Use Helvetica Now for everything. Inter can be used as a practical fallback, but do not mix in serif, mono, or display novelty faces.

| Role | Family | Fallback | Use |
| --- | --- | --- | --- |
| Primary | Helvetica Now | Inter | All headings, body, navigation, buttons, captions, and labels |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing |
| --- | --- | --- | --- | --- |
| Caption | 14px | 600 | 1.47 | 0.15px |
| Body | 16px | 600 | 1.31 to 1.4 | 0.005px |
| Subheading | 18px | 600 | 1.31 to 1.47 | -0.004px |
| Body large | 19px | 400 | 1.47 | -0.017px |
| Heading | 23px | 600 | 1.0 to 1.15 | -0.02em |
| Heading large | 35px | 600 | 1.0 | -0.024em |
| Display | 46px | 600 | 0.93 | -0.03em |
| Display large | 50px | 600 | 0.93 to 1.0 | -0.05em |

Large typography should feel architectural and poster-like. Tighten letter spacing as type grows.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | spacious |
| Max width | 1200px |
| Section gap | 35px |
| Card padding | 20px |
| Element gap | 20px |
| Card radius | 0px |
| Image radius | 0px |
| Button radius | 500px |
| Tag radius | 500px |
| Icon button radius | 100% |

The system is sharp for content containers and soft only for interactive pills.

## Layout

Use a max-width centered content container for most sections, with occasional full-bleed hero moments. The layout can shift between single-column text blocks, two-column text-and-image arrangements, and three-column article or feature grids.

Recommended flow:

1. Minimal top bar with utility icons or hamburger control.
2. Hero with large graphic headline and rectangular image.
3. Intro text or plain link area.
4. Two-column image/text section.
5. Three-column article or event card grid.
6. Featured block using Ash Gray or a vivid accent block.
7. Footer with stark black-and-white link groups.

## Components

### Ghost Button

Use for navigation, secondary actions, and inline actions. Canvas White fill or transparent fill, Ink Black text, 1px Ink Black border, 500px radius, compact 1px vertical and 15px horizontal padding.

### Primary Action Button

Use when an action needs more weight but should not introduce a CTA color. Canvas White background, Ink Black text, 1px Ink Black border, 500px radius. Use generous padding around 18px top, 21px bottom, and 35px horizontal.

### Icon Button

Circular utility control with Canvas White background, 1px Ink Black border, and 100% radius. Use simple monochrome line icons only.

### Plain Link Button

Ink Black text only. No background, border, or radius. Use inside text, article metadata, or low-hierarchy action rows.

### Article Card

Transparent background, no border, no shadow, no radius. The card is defined by a rectangular image and strong typography. Text is Ink Black.

### Gray Background Card

Ash Gray surface, 0px radius, no border or shadow. Use for content blocks that need a subtle break from Canvas White.

### Rectangular Image Block

0px radius, no shadow, no frame unless a 1px black border is structurally needed. Use urban, architectural, design, event, or candid cultural photography.

### Accent Color Block

Solid Focus Red, Blush Pink, or Electric Blue. Use as a poster-like section background, small content highlight, or visual punctuation. Do not combine all accents in one component.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Canvas White | `#ffffff` | Main page surface and default card surface |
| 1 | Ash Gray | `#e8e8e8` | Subtle secondary surface |
| 2 | Ink Black | `#000000` | Inverted hero or prominent display area |

## Elevation

No shadows or complex elevation. Separation comes from 1px borders, white space, rectangular image edges, and hard surface changes.

## Imagery

Use high-contrast photography, architectural details, urban landscapes, design objects, exhibition scenes, and candid people shots. Keep imagery unmasked and rectangular. Avoid illustration packs, 3D renders, glossy mockups, and rounded images.

## Do

- Use Ink Black for primary text and borders.
- Use Canvas White as the default background.
- Use Helvetica Now only.
- Use large tight display typography as a graphic element.
- Use 1px black borders for crisp UI definition.
- Use 500px pill radius for buttons and tags.
- Keep images and cards at 0px radius.
- Use accent colors only in controlled poster-like moments.

## Don't

- Do not introduce extra mid-tone grays.
- Do not use drop shadows or soft elevation.
- Do not use gradients.
- Do not round cards or images.
- Do not use generic colorful icon sets.
- Do not use vivid colors for general UI controls.
- Do not mix typefaces.

## AI Builder Notes

If the design feels too plain, increase typographic confidence or improve the photographic crop before adding decoration. This style gets its personality from scale, contrast, and strict geometry.
