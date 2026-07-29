# T1 Energy Style Reference

## Summary

T1 Energy is a precision manufacturing system on warm vellum. It feels like a technical specification sheet rendered as a website: quiet, monochrome, spacious, and architectural. Scale, spacing, geometry, and industrial photography replace decorative color.

The site should feel engineered, not flashy. Do not introduce accent colors. Do not make it app-like. Let Carbon Warm and factory imagery do all the work.

## Theme

Light.

## Personality

- Industrial
- Monochrome
- Precise
- Quiet
- Engineered
- Warm
- Specification-like
- Factory-scale

## Color System

This is a near-monochrome system. There is no CTA accent color.

| Name | Value | Token | Use |
| --- | --- | --- | --- |
| Vellum | `#f0efe9` | `--color-vellum` | Page canvas and section backgrounds |
| Paper White | `#ffffff` | `--color-paper-white` | Hairline borders, input outlines, card edges, circular icon fill |
| Carbon Warm | `#322d2a` | `--color-carbon-warm` | Text, borders, filled buttons, nav pill, dark panels |
| Onyx Depth | `#0f0e12` | `--color-onyx-depth` | Footer surface and deepest dark layer |
| Mercury | `#8b8b8b` | `--color-mercury` | Muted text, disabled states, subtle surface layers |
| Pure Black | `#000000` | `--color-pure-black` | SVG icon fills and monochrome graphics only |

## Typography

Use T1 Sans everywhere. If unavailable, use Inter or Sohne-like geometric sans, but keep the weight light.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Display | 52px | 300 | 1 | 0.52px |
| Heading | 32px | 300 | 1.2 | 0.32px |
| Subheading | 22px | 400 | 1.3 | 0.22px |
| Body | 16px | 400 | 1.4 | 0.16px |
| Body Small | 14px | 400 | 1.3 | 0.14px |
| Label | 12px | 400 | 1.3 | 0.12px |

## Font Rules

- Use T1 Sans as the sole typeface.
- Use weight 300 for all display headlines.
- Use weight 400 for body, labels, nav, and buttons.
- Do not use semibold or bold.
- Use universal `letter-spacing: 0.01em`.
- Keep display headline line-height exactly 1.

## Spacing And Shape

- Base unit: 4px
- Density: comfortable
- Max width: 1200px
- Section gap: 48px
- Card padding: 22px
- Element gap: 8px
- Small radius: 8px
- Body radius: 12px
- Nav radius: 16px
- Button radius: 16px for nav-like controls
- Image/card radius: 80px
- Pill radius: 100px

## Surfaces

| Level | Surface | Value | Role |
| --- | --- | --- | --- |
| 0 | Vellum Canvas | `#f0efe9` | Base page background and most sections |
| 1 | Paper White | `#ffffff` | Cards, floating panels, icon buttons |
| 2 | Carbon Warm | `#322d2a` | Navigation pill, buttons, case-study card |
| 3 | Onyx Depth | `#0f0e12` | Footer terminator |

## Elevation

No shadows. All hierarchy comes from flat tonal layering:

- Vellum canvas.
- Paper White panels.
- Carbon Warm controls.
- Onyx footer.

Do not use drop shadows, glows, gradients, or skeuomorphic elevation.

## Components

### Pill Navigation Bar

Dark Carbon Warm horizontal pill anchored top-right. Use 16px radius, about 36px vertical and 24px horizontal padding, white 14px T1 Sans links, and 24px gaps. The contrast against Vellum is the only elevation.

### Logo Mark

Geometric T1 wordmark in white when placed on the dark nav surface. Use simple constructed letterforms only.

### Filled Primary Button

Carbon Warm fill, Paper White text, 100px radius, 18px vertical and 22px horizontal padding, T1 Sans 14px weight 400. No border and no shadow.

### Ghost Outlined Button

Transparent fill, 1px Carbon Warm border, Carbon Warm text, 100px radius, 18px vertical and 22px horizontal padding. Match the filled button shape.

### Section Label

4px by 4px solid Carbon Warm square followed by uppercase 11px to 12px label text. Use weight 400, 0.12em tracking, Carbon Warm color. This square replaces icons or dots.

### Display Headline

T1 Sans 52px weight 300, line-height 1, 0.52px tracking, Carbon Warm on Vellum or Paper White on dark photography. It should feel etched and architectural.

### Case Study Card

Carbon Warm surface, 12px radius, about 16px padding, white label and headline, optional small map thumbnail. Use as an overlay on hero photography.

### Image Card

Full-bleed photo filling the container edge-to-edge. Radius is 80px. No caption, border, frame, or shadow. The image itself is the content.

### Accordion Item

Full-width row on Vellum. Carbon Warm label at 18px to 22px, circular icon button on the right. Icon button is 40px diameter, 100px radius, 1px Carbon Warm border, Paper White fill, plus or minus mark. Rows use 1px Carbon Warm hairline dividers.

### Hero Overlay

Full-viewport industrial photograph with bottom-left 52px weight 300 headline and filled Carbon Warm button below. No gradient or darkening overlay.

### Footer

Full-width Onyx Depth background, Paper White text, 14px weight 400, about 30px bottom padding.

## Layout

Use a 1200px centered content system, with hero sections breaking out full-bleed. The hero is a full-viewport industrial photograph with a bottom-left headline overlay. Below the hero, alternate single-column specification sections with two-column splits.

Image cards sit side by side as pairs with 80px radius. A technology section can split into a product render on one side and an accordion stack on the other. Navigation floats as a dark pill rather than a full-width header.

## Imagery

Use industrial documentary photography:

- Factory floors.
- Solar cell production lines.
- Robotic arms.
- Manufacturing surfaces.
- Product renders on vellum.

Images should be full-bleed inside their 80px rounded containers. Avoid overlays, duotones, stock lifestyle photography, abstract graphics, and illustrations.

## Do

- Use T1 Sans weight 300 at 52px for display headlines.
- Use Carbon Warm for all text, borders, and filled interactive elements.
- Use 80px radius on image containers.
- Use 100px radius on interactive pills.
- Maintain 48px section gaps and 22px card padding.
- Prefix section labels with a 4px Carbon Warm square.
- Keep the palette to vellum, white, carbon, and onyx.
- Set display line-height to exactly 1.

## Do Not

- Do not introduce accent colors, gradients, or decorative hues.
- Do not use Pure Black for text, backgrounds, or borders.
- Do not apply box shadows to cards, buttons, or navigation.
- Do not use bold or semibold headlines.
- Do not add icons or emoji to section labels.
- Do not frame or pad photographs.
- Do not use sharp corners below 8px.
