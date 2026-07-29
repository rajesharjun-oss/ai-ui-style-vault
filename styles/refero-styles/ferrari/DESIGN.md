# Ferrari - Style Reference

Theme: dark

Ferrari's Refero style reads like a cinematic product gallery: black surfaces, full-viewport photography, tiny uppercase text, hairline structure, and a single restrained red for interaction. The UI should feel disciplined and editorial. The vehicle, product, or hero object carries the emotion; the interface stays flat, sharp, and quiet.

## Core Principles

- Use black as the primary environment, not as decoration.
- Let full-bleed photography occupy most of the viewport.
- Keep typography small, uppercase, and widely tracked.
- Use red only for hover, focus, active, or small signal moments.
- Keep corners sharp at 0px except for a rare full-radius category pill.
- Avoid shadows, soft panels, filled red buttons, gradients, and framed images.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Rosso Corsa | `#da291c` | `--color-rosso-corsa` | Interactive hover, focus, active state, and rare signal accent. |
| Rosso Scuro | `#9d2211` | `--color-rosso-scuro` | Deeper supporting red for small state accents. |
| Carbone Nero | `#000000` | `--color-carbone-nero` | Full-bleed hero panels and dark cinematic backgrounds. |
| Notte Profonda | `#181818` | `--color-notte-profonda` | Footer and secondary dark surfaces. |
| Grafite | `#303030` | `--color-grafite` | Hairline borders, dividers, and subtle dark structure. |
| Piombo | `#666666` | `--color-piombo` | Quiet supporting copy and subdued labels. |
| Fumo | `#8f8f8f` | `--color-fumo` | Muted body text, captions, and metadata. |
| Argento Chiaro | `#d2d2d2` | `--color-argento-chiaro` | Light-surface borders and disabled edges. |
| Cemento | `#ebebeb` | `--color-cemento` | Soft light section background. |
| Velo di Luce | `#f7f7f7` | `--color-velo-di-luce` | Near-white surface wash. |
| Bianco Ferrari | `#ffffff` | `--color-bianco-ferrari` | Primary text, icons, links, and white canvas. |

## Typography

### Fonts

- Primary: FerrariSans-style sans.
- Practical substitute: Inter, Helvetica Neue, Arial Narrow, system-ui.
- Body extraction token: Body-Font.
- Enable alternate glyph features when available with `font-feature-settings: "ss01" 1`.

### Type Scale

| Role | Size | Weight | Line Height | Tracking | Use |
| --- | --- | --- | --- | --- | --- |
| micro | 7px | 400 | 2 | 0.091em | Rare legal or dense technical labels only. |
| tiny | 9px | 400 | 1.78 | 0.091em | Metadata, small tags, minor controls. |
| caption | 11px | 400 | 1.78 | 0.083em | Nav, labels, footer links, captions. |
| body-sm | 12px | 400 | 1.78 | 0.083em | Buttons, filters, secondary labels. |
| body | 13px | 400 | 1.78 | 0.015em | Body copy and editorial paragraphs. |
| section-title | 16px | 500 | 1.4 | 0.005em | Hero headline, section title, featured card title. |

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | comfortable |
| Max width | 1440px where a constrained content area is required |
| Section gap | 64-96px |
| Card padding | 24-32px |
| Element gap | 10-16px |

### Spacing Scale

`4px`, `5px`, `6px`, `10px`, `15px`, `16px`, `20px`, `24px`, `25px`, `30px`, `32px`, `44px`, `50px`, `54px`, `60px`, `123px`

### Radius

| Element | Value |
| --- | --- |
| cards | 0px |
| buttons | 0px |
| tags | 0px |
| full pill | 9999px |

## Components

### Ghost Navigation Link

Transparent uppercase text, 11-12px, wide tracking, no background, no border, and 0px radius. Hover changes text color to red or white depending on context.

### Dark Cinematic Hero Panel

Full viewport section on `#000000` or `#181818`. Photography bleeds to every edge. Headline is centered or gently overlaid, uppercase, 16px, medium weight, white.

### Section Label Button

Text-only chip with uppercase 12px copy, wide tracking, transparent background, 0px radius, and an optional hairline underline on hover.

### Carousel Indicator Dot

Small 8-10px geometric indicator. Inactive state uses muted gray; active state uses white or red. Avoid labels and decorative animation.

### Footer Block

Full-width `#181818` block with small uppercase column headings and link lists. Use generous vertical spacing, white icons, and hairline separators only where structure is required.

### Featured Content Card

Flat rectangular editorial block on black or near-black. No radius, no shadow, no elevation, and no border. Image bleeds to card edges. Headline is uppercase 16px medium.

### Utility Icon Button

Search, close, menu, or social icon as a 16px white outlined SVG. Transparent background, no fill, no border, and 0px radius.

### Category Pill

The one rounded exception: a transparent 9999px pill with a 1px white hairline border and uppercase 9-11px label.

### Hairline Divider

Use 1px `#303030` on dark surfaces or 1px `#d2d2d2` on light surfaces. Keep dividers structural, not decorative.

### Full-Bleed Photography Frame

Image container with 0px radius, no padding, no border, and no caption chrome. The photograph itself forms the layout.

### Body Text Link

White uppercase text with no underline by default. Hover changes to `#da291c`.

### CTA Arrow Link

Uppercase 11-12px text with a simple arrow indicator. Do not wrap it in a filled button.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Void Black | `#000000` | Hero panels and full-bleed cinematic sections. |
| 1 | Night Surface | `#181818` | Footer and secondary dark panels. |
| 2 | Graphite Edge | `#303030` | Borders, dividers, and dark structure. |
| 3 | Canvas White | `#ffffff` | Light section background and primary text. |
| 4 | Smoke Wash | `#f7f7f7` | Nearly white surface shift. |
| 5 | Concrete | `#ebebeb` | Light alternate section tone. |

## Imagery

Use cinematic product photography, preferably vehicles or precision objects in dark environments. Images should fill 70-90% of a section and should reach the viewport edge without padding or rounding. Avoid lifestyle scenes, abstract graphics, illustrations, screenshots, and framed thumbnails.

## Layout

Favor single-column vertical storytelling. The first viewport should be a full-bleed photograph or black hero panel with minimal centered copy. Navigation floats flat over the hero and should not introduce chrome. Later sections can use editorial cards, but they remain flush, sharp, and dark.

## Do

- Use black and near-black full-width sections.
- Use white and muted gray text for almost everything.
- Reserve red for hover, focus, active state, or tiny status accents.
- Keep interface text uppercase with generous letter spacing.
- Use 1px hairlines instead of shadows or elevation.
- Let photography bleed edge-to-edge.

## Don't

- Do not use red as a filled CTA background.
- Do not add rounded cards, rounded buttons, or soft panels.
- Do not add drop shadows, glow, glass, gradients, or raised surfaces.
- Do not place padding or frames around hero imagery.
- Do not use colorful text beyond white, muted gray, and red interaction states.
- Do not make the UI compete with the product photography.

