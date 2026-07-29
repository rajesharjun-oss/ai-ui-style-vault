# Atlantic.vc Style Reference

Atlantic.vc is a stark dark command-center design system. The page feels like a venture intelligence terminal: black field, blue-white text, blue readouts, orange ignition edges, large Monument headlines, and monospace body copy with measured letter spacing.

## Theme

Dark, command center, venture, speculative technology, precise, minimal, high contrast.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Deep Midnight | `#000000` | `--color-deep-midnight` | Page background and immersive section surface. |
| Charcoal Canvas | `#0d0d0f` | `--color-charcoal-canvas` | Recessed card and section background. |
| Graphite Base | `#232529` | `--color-graphite-base` | Selected body sections and intermediate panels. |
| Cool Stone | `#2b2f33` | `--color-cool-stone` | Elevated cards and distinct content blocks. |
| Ghost Ink | `#d8eaff` | `--color-ghost-ink` | Primary text, link text, navigation, and outlined button borders. |
| Muted Ash | `#6c757f` | `--color-muted-ash` | Secondary text, helper copy, and neutral link borders. |
| Subtle Grey | `#565e66` | `--color-subtle-grey` | Decorative borders and lower-emphasis body text. |
| Pale Slate | `#565657` | `--color-pale-slate` | Dark separators and elevated-surface borders. |
| Electric Blue | `#1f58f2` | `--color-electric-blue` | Highlight terms, interactive states, small decorative bands, and blue readouts. |
| Ignition Orange | `#ff4105` | `--color-ignition-orange` | Action text, tag outlines, dividers, focused edges, and icon accents. |

## Typography

### Monument

Use for display headlines, navigation, and prominent textual elements.

- Token: `--font-monument`
- Fallback: Montserrat
- Weight: 400
- Sizes: 10px, 16px, 24px, 64px, 96px
- Letter spacing: negative tracking for display, about `-0.03em` at 64px and 96px

### Mono

Use for body copy, descriptive labels, technical text, and code-like content.

- Token: `--font-mono`
- Fallback: Space Mono
- Weight: 400
- Sizes: 10px, 12px, 14px
- Letter spacing: about `0.06em` for body/data, up to `0.16em` for tiny captions

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 10px | 0.80 | 0.16px | `--text-caption` |
| Body | 14px | 1.50 | 0.06px | `--text-body` |
| Heading | 24px | 1.24 | -0.01px | `--text-heading` |
| Heading LG | 64px | 1.46 | -0.03px | `--text-heading-lg` |
| Display | 96px | 1.50 | -0.03px | `--text-display` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Section gap: 50px.
- Card padding: 24px.
- Element gap: 16px.
- Layout: full-bleed or generously padded; avoid relying on one strict page max width.

### Spacing Scale

`4, 8, 12, 16, 20, 24, 32, 80, 100, 148, 200, 240`

### Radius Scale

| Element | Radius |
|---|---:|
| Buttons | 0px |
| Navigation | 0px |
| Links | 8px |
| Cards | 16px |
| Large cards | 24px |

## Components

### Ghost Navigation Link

Transparent background, no border, no radius, Monument 400, Ghost Ink text. Use for header navigation and secondary text actions.

### Outlined Action Button

Transparent fill, 1px Ghost Ink border, Ghost Ink text, 0px radius, Monument 16px. Use for primary CTAs. Do not fill it with blue.

### Text Accent Button

Transparent background, no border, 0px radius, Monument text in Ignition Orange. Use for focused action states and small high-signal actions.

### Standard Card

Cool Stone or Charcoal Canvas surface, 16px radius, no heavy border, no shadow. Padding may be minimal when content provides its own internal rhythm.

### Hero Large Card

Charcoal Canvas surface, 24px radius, large internal padding around 150px vertical and 110px horizontal. Use for major command-center statements or hero modules.

### Company Grid

Full-bleed or horizontally scrolling grid. Use dark surfaces, blue/noise treatment, and Ghost Ink labels. Avoid boxed-in light tiles.

### Sticky Top Bar

Minimal sticky nav on dark background. Keep links sparse, type precise, and CTA as text or orange accent rather than a broad filled button.

## Layout

Use full-bleed dark sections with generous inner padding and implied columns. The hero should be immersive: centered Monument headline over abstract digital/noise atmosphere, with a minimal CTA treatment. Sections can alternate centered text stacks, horizontal company grids, and soft cards. Rhythm should feel spacious, around 50px to 100px between blocks.

## Imagery

Use product/tech visuals, partner logos, abstract digital noise, and restrained blue-toned graphic textures. Team photography can be high-key, desaturated, tightly cropped, and placed inside structured grids. Icons should be minimal outlines using Electric Blue or Ignition Orange.

## Do

- Use dark backgrounds only.
- Prioritize Ghost Ink for primary text and interactive outlines.
- Use Electric Blue for key terms, readouts, and small interactive states.
- Use Ignition Orange for action edges, tags, dividers, and focused UI.
- Use Monument for display/nav and Mono for body/labels.
- Keep CTAs outlined or text-accented.
- Use 16px cards and 24px large cards.

## Don't

- Do not use light page backgrounds.
- Do not add bold colors beyond Electric Blue and Ignition Orange.
- Do not use heavy shadows or excessive elevation.
- Do not change the specified tracking character of Monument and Mono.
- Do not use large filled buttons.
- Do not round buttons.
- Do not force a strict page-level max width.
