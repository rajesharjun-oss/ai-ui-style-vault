# Slash Style Reference

Slash is a midnight fintech system with editorial luxury. A near-black vault canvas supports white and bone text, copper category punctuation, a rare white conversion button, and financial charts accented by a warm gilded line. Ivy Presto gives the brand its high-contrast ledger feel; Inter keeps the product UI usable.

## Theme

Dark, fintech, editorial, premium SaaS, data-rich, compact, ledger-like.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Onyx | `#040406` | `--color-onyx` | Card surface and secondary backdrop, one step deeper than the page. |
| Obsidian | `#08080a` | `--color-obsidian` | Page canvas, footer background, and deepest surface. |
| Carbon | `#121317` | `--color-carbon` | Elevated panels, dropdowns, input fills, and subtle UI fills. |
| Graphite | `#1c1d22` | `--color-graphite` | Borders, dividers, icon containers, sliders, and hairline structure. |
| Slate | `#2e3038` | `--color-slate` | Secondary borders, muted icon strokes, and content dividers. |
| Smoke | `#464853` | `--color-smoke` | Tertiary borders and inactive navigation items. |
| Ash | `#5e616e` | `--color-ash` | Muted body text, placeholders, and secondary metadata. |
| Steel | `#777a88` | `--color-steel` | Button borders, icon strokes, secondary text, and ghost outlines. |
| Fog | `#9194a1` | `--color-fog` | Navigation text, helper text, descriptions, and readable gray copy. |
| Mist | `#acafb9` | `--color-mist` | Supplementary text and lower-emphasis paragraphs. |
| Silver | `#c7c9d1` | `--color-silver` | Light body text and medium-emphasis paragraphs. |
| Bone | `#e2e3e9` | `--color-bone` | Default readable UI text, dense data labels, and body copy. |
| Paper White | `#ffffff` | `--color-paper-white` | Headings, active nav, and the scarce primary action button fill. |
| Copper | `#cc9166` | `--color-copper` | Category labels, editorial links, and warm accent punctuation. |
| Gilded Gradient | `linear-gradient(103deg, rgb(174, 147, 87), rgb(255, 240, 204) 40%, rgb(174, 147, 87) 70%, rgba(189, 157, 79, 0))` | `--gradient-gilded` | Chart line stroke and financial data accent only. |

## Typography

### Ivy Presto

Use for display and heading text at 28px and above only.

- Token: `--font-ivy-presto`
- Fallback: Playfair Display, DM Serif Display, Libre Caslon Display
- Weights: 400, 500
- Sizes: 28px, 44px, 52px, 64px, 88px
- Line height: 1.0 to 1.38
- Letter spacing: 0.01em

The serif is the brand identity. Do not replace it with Inter for display text.

### Inter

Use for all UI and body copy.

- Token: `--font-inter`
- Fallback: Inter
- Weights: 300, 400, 500, 600, 700
- Sizes: 12px, 13px, 14px, 15px, 16px, 18px, 20px, 24px, 48px
- Line height: 1.0 to 1.56
- Letter spacing: -0.04em to 0.01em

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Eyebrow | 13px | 1.00 | -0.26px | `--text-eyebrow` |
| Body XS | 16px | 1.50 | 0 | `--text-body-xs` |
| Body SM | 18px | 1.38 | -0.36px | `--text-body-sm` |
| Body | 20px | 1.38 | -0.8px | `--text-body` |
| Subheading | 24px | 1.00 | -0.31px | `--text-subheading` |
| Heading SM | 44px | 1.38 | 0.44px | `--text-heading-sm` |
| Heading | 52px | 1.13 | 0.52px | `--text-heading` |
| Heading LG | 64px | 1.13 | 0.64px | `--text-heading-lg` |
| Display | 88px | 1.00 | 0.88px | `--text-display` |

## Spacing And Shape

- Density: compact.
- Max width: 1216px.
- Section gap: 160px.
- Card padding: 24px.
- Element gap: 8px.

### Spacing Scale

`4, 6, 8, 9, 10, 12, 14, 16, 20, 22, 24, 32, 40, 48, 105, 224`

### Radius Scale

| Element | Radius |
|---|---:|
| Nav underline | 2px |
| Cards | 10px |
| Buttons | 9999px |
| Inputs | 9999px |
| Tags | 9999px |
| Icons | 9999px |
| Status indicators | 9999px |

## Components

### Primary Action Button

White fill, black text, 9999px radius, Inter 14px/500, 10px by 20px padding, no border. Use only once per viewport for the single most important action.

### Ghost Outline Button

Transparent fill, 1px Paper White border, Paper White text, 9999px radius, Inter 14px/500, 10px by 20px padding. Use for secondary actions.

### Pill Tag Button

Transparent fill, 1px Steel border, 9999px radius, 6px by 10px padding, Inter 12px to 14px. This is subdued and secondary, not a CTA.

### Hero Chart Card

Onyx surface, 10px radius, no visible border. Contains balance header, period filter pill, gilded gradient chart line, and spend-limit input.

### Transaction List Card

Transparent or Onyx panel with 10px radius. Rows include circular icon wells, merchant names, and right-aligned amounts. Use dense vertical rhythm and Slate hairline borders.

### Testimonial Video Card

10px radius, full-bleed image, dark bottom gradient overlay, white name text, and muted title/company text. No border and no shadow.

### Blog Post Card

10px radius, transparent fill, no border. Image on top, Copper category label, date, Inter 18px to 20px title, and Mist read-time metadata.

### Email Capture Input

Transparent fill, 1px Paper White border, 9999px radius, placeholder in Steel, 10px top/bottom padding, larger left padding. Pair it visually with the primary white pill.

### Navigation Link

No background, no border. Inter 14px in Fog inactive and Paper White active. Hover underline uses 2px radius.

### Stat Display

Large number in Ivy Presto 28px to 44px, Paper White. Caption below in Inter 14px/Fog.

### Data Table Row

Transparent fill, 1px Graphite bottom border, compact cells, Fog headers, Bone values, right-aligned numerics. Avoid container-heavy tables.

## Layout

Use a centered 1216px max-width with 160px vertical section gaps. The hero is split: left column with an Ivy Presto headline and email capture; right column with dark product UI card and chart. Later sections use centered serif headlines, Inter subtitles, 3-column grids, testimonial cards, blog cards, stat callouts, and dense data tables.

## Imagery

Use editorial, naturalistic founder/team photography in real environments, slightly desaturated and warm. Product UI appears in dark mode. Article thumbnails may mix photography and editorial concepts. Icons are monochrome 1px strokes and should not be filled with brand color.

## Do

- Use Ivy Presto for all headings at 28px and above.
- Use Inter for body, nav, controls, tables, and forms.
- Set default body copy in Bone, not pure white.
- Use the white filled pill once per viewport.
- Use Copper only for category labels and editorial links.
- Use Graphite or Slate hairline borders.
- Use 160px desktop section gaps.
- Reserve the gilded gradient for charts and financial data accents.

## Don't

- Do not substitute Inter for Ivy Presto in display text.
- Do not introduce blue, green, or other chromatic accents.
- Do not use white for long-form body copy.
- Do not use the white filled CTA more than once per viewport.
- Do not add drop shadows.
- Do not set Inter body text above 20px.
- Do not apply the gilded gradient outside data visualization.
