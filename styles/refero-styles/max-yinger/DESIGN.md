# Max Yinger - Style Reference

Theme: dark

Max Yinger's Refero style is a midnight engineer terminal. The page is a single dark plane with warm bone-white type, a central 3D object, and text clusters pushed to the viewport corners. It is compact, technical, and edge-anchored. There is no normal card system, no marketing container, and no color palette beyond carbon, bone, charcoal, and a rose edge-light that belongs only to the 3D artifact.

## Core Principles

- Use Midnight Carbon as the page background.
- Use Bone Glow for essentially all text.
- Keep Rose Quartz Bloom out of UI chrome; it belongs only to 3D light bleed.
- Push content to corners and edges rather than centering a page column.
- Keep gaps extremely tight.
- Use 12px technical labels as the default metadata voice.
- Use 80px blocky display type for hero-scale readouts.
- Let the 3D artifact provide all visual depth.
- Avoid borders, cards, shadows, and extra accent colors.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Midnight Carbon | `#12130f` | `--color-midnight-carbon` | Full-bleed page canvas and dark plane. |
| Bone Glow | `#e4dfda` | `--color-bone-glow` | Primary text, headings, buttons, labels, and body copy. |
| Charcoal Vein | `#3c3c38` | `--color-charcoal-vein` | Secondary dividers and subdued UI chrome when absolutely needed. |
| Rose Quartz Bloom | `#f5c2c8` | `--color-rose-quartz-bloom` | Soft pink edge-light on 3D rendered objects only. |

## Typography

### Fonts

- Telemetry labels: Arbeit Technik.
- Telemetry fallback: JetBrains Mono, IBM Plex Mono, ui-monospace.
- Hero display: Inline VF.
- Hero fallback: Departure Mono, VT323, monospace.
- Prose and secondary display: Arbeit Contrast.
- Prose fallback: Inter, Sohne, Untitled Sans, system-ui.

### Type Scale

| Role | Size | Weight | Line Height | Tracking | Use |
| --- | --- | --- | --- | --- | --- |
| caption | 12px | 400 | 15px | -0.6px | Telemetry, status labels, annotations. |
| body | 16px | 400 | 20px | 0 | Bio text, inline links, readable prose. |
| subheading | 30px | 400 | 34px | 0 | AM suffix, small display group labels. |
| display | 80px | 400 | 56px | 0 | Time readout, masthead-scale display blocks. |

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | compact |
| Base unit | 4px |
| Section gap | 64px |
| Card padding | 12px |
| Element gap | 4px |

### Spacing Scale

`4px`, `8px`, `12px`, `64px`

### Radius

| Element | Value |
| --- | --- |
| buttons | 9999px |
| tags | 9999px |
| links | 2px |
| cards | 0px |

## Components

### Pill Link Button

Text-only external/social navigation. Use full pill radius, transparent background, Bone Glow text, no border, and 12px telemetry typography. Padding can be around 12px vertical and 16-20px horizontal. The button should sit flush near a viewport edge.

### Underlined Inline Link

Inline prose link with inherited Bone Glow text and a 2px Bone Glow underline. Use 2px radius only here. Do not use a color hover state.

### Telemetry Label

Arbeit Technik-style 12px label with tight negative tracking, line-height 1.25, all caps, and Bone Glow color. Use for time labels, location lines, status, section notes, and annotations.

### Digital Time Readout

Inline VF-style display at 80px, line-height 56px, weight 400, Bone Glow. Pair with a smaller 30px suffix if needed. It should feel live and operational.

### Masthead Wordmark

Compact blocky display stamp around 30-40px, Bone Glow, positioned top-left. It behaves like a brand stamp, not a decorative logo system.

### 3D Hero Artifact

Central isometric cube or chrome/bone object, mostly Bone Glow with soft Rose Quartz Bloom edge-lighting. No container, border, shadow, mask, or panel.

### Cluster Card

A dense grouping of labels and text with no visible background, no border, and no shadow. It is defined by 4px or 8px gaps only.

### Performance Annotation

Tiny technical metric near the time readout or artifact. Use 12px telemetry text, Bone Glow, and monospaced alignment.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 1 | Canvas | `#12130f` | Full-bleed background for all sections. |
| 2 | Recessed | `#12130f` | Content blocks sit flush on the same surface; spacing defines separation. |

## Elevation

No CSS elevation. No box shadows, drop shadows, glow effects, blurred panels, or material layering. Depth comes only from the 3D object.

## Imagery

Use one central 3D rendered artifact. It should be isometric, geometric, and lightly rose-edged. Avoid photography, product screenshots, illustrations, icons, and multiple hero visuals.

## Layout

Use a full-bleed edge-to-edge page. Top-left holds the masthead. Bottom-left holds time, telemetry, and bio. Bottom-right holds social pill links. The center holds the 3D artifact. Avoid max-width containers, centered columns, traditional navigation bars, and visual section dividers.

## Do

- Use Bone Glow for text and Midnight Carbon for the full page background.
- Use full pill radius on interactive social buttons and tags.
- Use 2px radius only for inline underlined links.
- Use 4px element gaps and 12px cluster padding.
- Use Inline VF-style display at 80px with compressed line-height.
- Use Arbeit Technik-style 12px labels with -0.6px tracking.
- Push content to viewport corners and edges.

## Don't

- Do not introduce new accent colors.
- Do not use Rose Quartz Bloom on UI controls.
- Do not use box shadows or drop shadows.
- Do not use line-height above 1.25.
- Do not center content in a max-width container.
- Do not use visible borders on cards or content clusters.
- Do not use bold or semibold weights.
- Do not use pure white or pure black.

