# Cursor Style Reference

Cursor is a warm parchment developer-product system. It combines cream paper surfaces, warm ink text, compact 4px geometry, whisper-weight headings, and a single ember accent for text emphasis. The result should feel like a refined technical journal wrapped around product UI, not a glossy marketing template.

## Theme

Light, parchment, editorial, developer-tool, compact, warm-neutral, product-led, restrained.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Parchment | `#f7f7f4` | `--color-parchment` | Page background and primary canvas. |
| Bone | `#f2f1ed` | `--color-bone` | Product cards, mockup frames, and elevated paper surfaces. |
| Linen | `#e6e5e0` | `--color-linen` | Secondary button fill, logo tiles, and higher paper surfaces. |
| Stone | `#cdcdc9` | `--color-stone` | Hairline borders, separators, and outlines. |
| Mist | `#a1a19f` | `--color-mist` | Captions, helper text, and tertiary UI copy. |
| Driftwood | `#84847e` | `--color-driftwood` | Secondary body text and quieter table copy. |
| Ash | `#7a7974` | `--color-ash` | Icon fills, metadata, and subdued labels. |
| Ink | `#26251e` | `--color-ink` | Primary text, nav text, primary action fill, and core UI chrome. |
| Ember | `#f54e00` | `--color-ember` | Inline links, tags, and short text emphasis only. |
| Amber | `#c08532` | `--color-amber` | Small in-product action buttons and accent icon strokes. |
| Forest | `#34785c` | `--color-forest` | Focused product actions and selected states. |
| Verdant | `#1f8a65` | `--color-verdant` | Supporting green text accents. |
| Crimson | `#cf2d56` | `--color-crimson` | Supporting red text accents. |
| Selection Blue | `#8bc4f8` | `--color-selection-blue` | Browser text selection only. |

## Typography

### CursorGothic

Use for headings, navigation, body, product UI, and most interface text.

- Token: `--font-cursorgothic`
- Fallback: Inter, system-ui, Helvetica Neue
- Weights: 400, 500
- Sizes: 11px, 13px, 14px, 16px, 22px, 26px, 36px, 72px
- Line height: 1.00 to 1.50
- Letter spacing: loose at small sizes, progressively tighter at display sizes.
- Role: the main voice of the interface. Headings should look precise and quiet, never bold.

### EB Garamond

Use selectively for editorial subheadings, prose blocks, and table-like editorial content.

- Token: `--font-eb-garamond`
- Fallback: Iowan Old Style, Palatino Linotype, ui-serif, Georgia
- Weights: 400, 500
- Sizes: 16px, 17px, 19px
- Line height: 1.35 to 1.50
- Letter spacing: normal
- Role: adds literary texture inside an otherwise geometric UI shell.

### berkeleyMono

Use for code, file paths, CLI snippets, model names, metadata, and technical labels.

- Token: `--font-berkeleymono`
- Fallback: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas
- Weights: 400, 500
- Sizes: 12px, 13px
- Line height: 1.43 to 1.67
- Role: the technical voice for developer-facing surfaces.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Eyebrow | 12px | 1.63 | 0 | `--text-eyebrow` |
| Body SM | 14px | 1.50 | 0.14px | `--text-body-sm` |
| Body | 16px | 1.35 | 0 | `--text-body` |
| Editorial | 17px | 1.35 | 0 | `--text-editorial` |
| Editorial LG | 19px | 1.50 | 0 | `--text-editorial-lg` |
| Heading SM | 22px | 1.30 | -0.11px | `--text-heading-sm` |
| Heading | 26px | 1.25 | -0.312px | `--text-heading` |
| Heading LG | 36px | 1.20 | -0.72px | `--text-heading-lg` |
| Display | 72px | 1.10 | -2.16px | `--text-display` |

## Spacing And Shape

- Density: compact.
- Base unit: 4px.
- Max width: 1300px.
- Section gap: 64px to 96px.
- Card padding: 24px.
- Element gap: 8px.

### Spacing Scale

`4, 8, 12, 16, 20, 24, 32, 48, 56, 64`

### Radius Scale

| Element | Radius |
|---|---:|
| Cards | 4px |
| Tiles | 4px |
| Inputs | 4px |
| Buttons | 4px |
| Modals | 8px |

## Components

### Primary Filled Button

Ink fill, Parchment text, 4px radius, compact vertical padding, CursorGothic 14px/400. Use this for the highest-contrast action.

### Secondary Filled Button

Linen fill, Ink text, 4px radius, matching compact padding. Pair it beside the dark primary action when a secondary option is needed.

### Ghost Text Button

Transparent background, muted Ink text, 4px focus radius, no border, underline on hover. Use for nav items, inline actions, and skip-like actions.

### Amber Action Button

Amber fill, light cream text, 4px radius, compact product-UI sizing. Use inside mockups or IDE-like chrome, not as a page-level hero CTA.

### Forest Action Button

Forest fill, Parchment text, matching green border, 4px radius. Use for selected states and focused product actions.

### Product Mockup Card

Bone surface, 4px radius, warm hairline border, 24px padding, and soft warm shadow. It should frame a macOS-style product screenshot or IDE window.

### Logo Trust Tile

Linen surface with monochrome Ink logo at reduced opacity. Keep the tile compact and paper-like. Use in a single row for social proof.

### Window Mockup Frame

Use macOS chrome with muted control dots, centered title text, small file tabs, and berkeleyMono labels. The window itself should feel nested inside a Bone card.

### Navigation Bar

Transparent 52px top bar with logo left, compact center links, and right-side actions. Avoid sticky shadows.

### Terminal Input Field

Transparent or Bone background, hairline Ink-tinted border, 4px radius, 10px by 12px padding, berkeleyMono 12px, muted prompt glyph.

### Footer Link Column

No card. Heading uses CursorGothic 14px/500 in Ink. Links use 13px muted Ash with tight 8px row rhythm.

### Mono Metadata Tag

Transparent background, no border, no radius, berkeleyMono 12px Ash. Use inline for file names, status labels, and model names.

## Layout

Use a centered 1300px content rail with 24px outer padding. Keep the top navigation thin and transparent. The hero should lead with left-aligned light-weight display type and paired CTAs, then show a wide product mockup card. Trust logos sit in one horizontal strip. Feature sections alternate text and screenshot columns with 64px to 96px vertical breathing room. Footer uses a simple multi-column link grid.

## Imagery

Product screenshots and IDE mockups carry the page. Show file tabs, terminal snippets, diffs, agents, chat integrations, and code views. Product windows sit inside warm Bone cards with soft paper elevation. Customer logos are monochrome. A subtle warm landscape image can sit behind the hero, but avoid lifestyle photography, decorative illustrations, abstract graphics, or color-heavy icons.

## Do

- Use Parchment for the page canvas and Bone for card surfaces.
- Keep all headings at weight 400 unless the text is a small label.
- Tighten letter spacing as heading size increases.
- Keep Ember as inline text punctuation only.
- Use 4px radius for almost every component.
- Use warm hairline borders before adding shadow.
- Use EB Garamond sparingly for editorial prose.
- Use berkeleyMono 12px for developer metadata and command snippets.

## Don't

- Do not use pure white or pure black as the foundation.
- Do not bold display headings.
- Do not use pill buttons or rounded cards.
- Do not use gradients, glows, or large color washes.
- Do not make shadows blue or glassy.
- Do not use Ember as a background fill.
- Do not use system-ui for headings.
- Do not stack more than two button styles in one action group.
