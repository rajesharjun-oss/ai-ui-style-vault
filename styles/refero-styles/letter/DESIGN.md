# Letter - Style Reference

Theme: mixed

Letter's Refero style combines private-banking restraint with gallery-like presentation. The first impression is a black vault stage with sculptural 3D artifacts. The body shifts into white and mist-white editorial sections with square tinted product panels. The system is polished, quiet, and flat. Depth comes from metallic/prismatic renders, not UI shadows.

## Core Principles

- Open with a full-bleed dark vault hero.
- Use a serif display face for all meaningful headlines.
- Use an extended grotesque for navigation, buttons, descriptions, labels, and supporting UI.
- Keep buttons and inputs nearly square at 2px radius.
- Use colored filled buttons only for action moments.
- Pair each filled action with a matching ghost text link.
- Let 3D objects float unmasked in negative space.
- Do not use shadows, glows, gradients, or rounded friendly UI.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Vault Ink | `#191b1f` | `--color-vault-ink` | Dark hero stage, dark navigation, and vault surfaces. |
| Paper White | `#ffffff` | `--color-paper-white` | Main page canvas, light cards, inverse text on dark. |
| Mist White | `#f6f9f9` | `--color-mist-white` | Soft alternating section background. |
| Fog Gray | `#9fabad` | `--color-fog-gray` | Muted helper copy, secondary labels, and metadata. |
| Hairline | `#e6ebec` | `--color-hairline` | Low-contrast dividers, outlines, and button strokes. |
| Obsidian | `#000000` | `--color-obsidian` | Highest-contrast text, marks, and pure black moments. |
| Peach Wall | `#fcede1` | `--color-peach-wall` | Warm tinted feature panel. |
| Mint Wall | `#eefcef` | `--color-mint-wall` | Cool tinted feature panel. |
| Lavender Wall | `#e6def0` | `--color-lavender-wall` | Soft violet tinted feature panel. |
| Deep Teal | `#186f64` | `--color-deep-teal` | Primary filled action and matching ghost link. |
| Electric Violet | `#536eff` | `--color-electric-violet` | Secondary filled action and selected state. |
| Royal Violet | `#644bc4` | `--color-royal-violet` | Deeper violet state and accent border. |
| Sapphire Blue | `#154ea5` | `--color-sapphire-blue` | Tertiary filled action for card/checking moments. |

## Typography

### Fonts

- Display: Albra Sans-style high-contrast serif.
- Display fallback: GT Sectra, Tiempos Headline, Canela, Playfair Display, Georgia, serif.
- UI/body: Neufile Grotesk Extended-style sans.
- UI/body fallback: Sohne, Inter, IBM Plex Sans, system-ui, sans-serif.

### Type Scale

| Role | Size | Weight | Line Height | Tracking | Use |
| --- | --- | --- | --- | --- | --- |
| caption | 13px | 400 | 1.4 | 0 | Nav links, labels, metadata. |
| body | 16px | 400 | 1.4 | 0 | Paragraphs, card text, links. |
| subheading | 22px | 600 | 1.2 | 0.44px | Serif product panel headings. |
| heading-sm | 28px | 400 or 500 | 1.3 | 0 | Sans subheads or emphasized UI headings. |
| heading | 46px | 600 | 1.2 | 0.92px | Section headings. |
| display | 80px | 600 | 1.1 | 1.6px | Hero headline only. |

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | comfortable |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 64-96px |
| Card padding | 32px |
| Element gap | 16px |
| Button padding | 12px vertical, 27px horizontal |

### Spacing Scale

`8px`, `12px`, `16px`, `24px`, `32px`, `48px`, `64px`, `72px`

### Radius

| Element | Value |
| --- | --- |
| cards | 0px |
| tags | 2px |
| inputs | 2px |
| buttons | 2px |

## Components

### Navigation Bar Dark

Transparent or flat `#191b1f` bar over the hero. White extended-grotesque nav links at 13px. The join action is a ghost button with white border and 2px radius; sign-in remains a text link.

### Navigation Bar Light

White navigation on light sections with vault-ink text. The join action becomes a dark filled button with white text and 2px radius.

### Teal Filled Button

Primary conversion button for investment or deposit flows. Use `#186f64` background, white 16px medium extended-grotesque text, 2px radius, 12px vertical padding, 27px horizontal padding, and no shadow.

### Violet Filled Button

Secondary conversion button for borrowing or credit flows. Use `#536eff` background with the same button geometry and typography.

### Blue Filled Button

Tertiary action for card, checking, or account moments. Use `#154ea5` background with the same button geometry.

### Ghost Text Link

Text-only companion link that sits beside a filled action. Match the filled button color: teal with teal, violet with violet, blue with blue.

### Tinted Feature Card

Product panel using peach, mint, or lavender wall color. Use 0px card radius, no shadow, no border, 32px padding, serif 22px heading, 16px body text, a colored filled button, a matching ghost link, and a large 3D render.

### Dark Hero Stage

Full-bleed `#191b1f` hero with centered 80px serif display headline, a smaller serif subhead, and a large metallic/prismatic render occupying much of the lower viewport. No card surface or frame.

### Split Content Section

Centered 1200px two-column section. Text goes left, 3D render goes right. Background alternates between white and mist white.

### 3D Abstract Render

Signature visual element. Use polished chrome, dichroic glass, liquid metal, iridescent facets, lens flare, caustic lighting, and gallery spotlight cues. The render should float raw in space.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Vault Ink | `#191b1f` | Hero, dark nav, and dark stage. |
| 1 | Paper White | `#ffffff` | Page canvas and light content surface. |
| 2 | Mist White | `#f6f9f9` | Alternating section background. |
| 3 | Tinted Gallery Walls | `#fcede1`, `#eefcef`, `#e6def0` | Product panels around 3D renders. |

## Imagery

Use 3D abstract renders, not photography. The visual material should feel expensive and museum-lit: chrome, prismatic glass, liquid metal, faceted crystals, and glossy artifacts. Keep renders unmasked, unframed, and large enough to command 40-60% of a major section.

## Layout

Use a full-bleed dark hero, then transition into centered white and mist-white sections. Preferred rhythm: dark hero, white split section, tinted product card row, white split section, tinted product card row. Keep text left and renders right in split layouts. Use two-column cards for product panels.

## Do

- Use the serif display face for all headlines.
- Cap hero display at 80px and section headings at 46px.
- Keep controls at 2px radius.
- Pair filled colored actions with a matching ghost text link.
- Use tinted cards only for product panels.
- Let 3D renders create the depth.
- Use flat surfaces without shadows.

## Don't

- Do not set headlines in a sans-serif.
- Do not add rounded cards, pill buttons, or circular avatar treatments.
- Do not use brand action colors for body text, large backgrounds, or ordinary borders.
- Do not use the tinted wall colors as full-page backgrounds.
- Do not apply gradients to UI components.
- Do not use box shadows or drop shadows on UI.
- Do not mask or frame the 3D renders.

