# 247Studio Design Reference

## North Star

Build a monochrome branding-studio experience that feels like a printed architecture monograph translated to the web. The page should be quiet, confident, sparse, and exact: white space, black type, large typographic gestures, gray supporting copy, rounded editorial cards, and almost no visible UI decoration.

The design should never feel like generic SaaS. It is a studio portfolio where typography, spacing, and restraint are the product.

## Theme

- Mode: light.
- Canvas: pure white.
- Text: black ink.
- Accent: gray only.
- Geometry: large rounded cards and pill controls.
- Depth: flat, border-led, and print-like.
- Motion: slow editorial transitions if needed.

## Color System

Core colors:

- Pure White: `#ffffff` for the page canvas, cards, and inverted text on dark sections.
- Ink Black: `#000000` for primary headings, logo, strokes, labels, borders, and strongest UI.
- Obsidian: `#1f1f1f` for dark sections, footer surfaces, and inverted editorial moments.
- Graphite Wash: `#333333` for elevated dark panels and dark overlays.
- Slate: `#666666` for secondary body copy and subdued interface text.
- Steel: `#808080` for tertiary text, logo placeholders, captions, and quiet strokes.
- Fog: `#999999` for muted hero lines, inactive indicators, and pale supporting copy.
- Pale Mist: `#cccccc` for hairline borders, disabled states, dividers, and field outlines.
- Vapor: `#e6e6e6` for soft card fill, light dividers, inputs, and placeholders.
- Ash: `#f2f2f2` for alternating section bands, image placeholders, and quiet containers.

Do not introduce a brand color. The absence of color is part of the system.

## Typography

Display and brand family: `247 grotesk`.  
Body and utility family: `Ntbau`.

Use fallbacks like Inter, Neue Haas Grotesk, Sohne, Untitled Sans, or system sans when the custom faces are unavailable.

247 grotesk:

- Use for logo, hero headlines, section titles, nav, labels, and short display copy.
- Enable the `ss01` stylistic alternate for the brand feeling.
- Use weight 400 for most large display text.
- Use weight 500 for labels, buttons, and compact emphasis.
- Use italic sparingly for the muted second hero line.
- Let large display text stay light and calm.

Ntbau:

- Use for body copy, descriptions, addresses, captions, and dense metadata.
- Use 400 for body, 500 for small emphasis, and 700 only where source content needs a strong data point.
- Add a small positive letter spacing around `0.019em` for compact labels and metadata.

Type scale:

- Caption: 10px, line-height 1.3.
- Small label: 11px, line-height 1.14.
- Small body: 12px, line-height 1.3.
- Body: 14px, line-height 1.25 to 1.89 depending on measure.
- Body large: 16px, line-height 1.25.
- Subheading: 19px, line-height 1.2.
- Heading small: 28px, line-height 1.14.
- Heading: 35px, line-height 1.14.
- Heading large: 52px, line-height 1.
- Display: 73px, line-height 1.

## Layout

- Page max width: 1440px.
- Main content rail: around 1200px with a strong left offset.
- Left margin for hero and major labels: around 120px on desktop.
- Hero headline: two flush-left lines.
- Hero supporting copy: narrow 350px measure.
- Section gaps: 80-120px.
- Card padding: 24-40px.
- Element gaps: 8-16px.
- Client logo grids: wide, low cells with small number labels.

The layout should feel intentionally underfilled. Do not occupy every row with content.

## Shape

- Tags: 33.76px radius.
- Cards: 33.76px radius.
- Image placeholders: 33.76px radius.
- Buttons: 42.96px radius.
- Logo and marks: crisp, no border radius unless the asset requires it.

Rounded corners are large but not bubbly. The surrounding system stays flat and severe.

## Elevation

Avoid shadows entirely unless a platform component requires a subtle focus ring.

Use depth through:

- White, ash, vapor, and dark-surface transitions.
- 1px gray borders.
- Large internal padding.
- Hairline dividers.
- The contrast between oversized display type and small metadata.

## AI Build Notes

Start with a pure white page, a large two-line `247 grotesk` headline, a narrow `Ntbau` paragraph, and a sparse nav. Add client logos and office/contact cards only after the typographic hierarchy works. If the page starts to feel decorative, remove elements before adding more.

