# AI for Business Style Reference

AI for Business uses brutalist editorial logic on a warm gray showroom canvas. The interface is flat, high contrast, rounded at large scales, and driven almost entirely by typography. Mint and yellow appear as small functional sparks, while black, white, and warm gray do the structural work.

## Theme

Light, brutalist, editorial, enterprise AI, tactile, product showroom, flat.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Carbon Black | `#000000` | `--color-carbon-black` | Primary text, inverted card surfaces, filled blocks, and structural anchors. |
| Graphite | `#2f2f2f` | `--color-graphite` | Deep surface for code blocks or heavy accents. |
| Slate | `#444444` | `--color-slate` | Secondary body text, navigation labels, and subdued headings. |
| Smoke | `#979797` | `--color-smoke` | Secondary body text, meta labels, and icon strokes. |
| Ash | `#c6c6c6` | `--color-ash` | Borders, hairlines, disabled states, and neutral structure. |
| Warm Canvas | `#e5e5e5` | `--color-warm-canvas` | Page background, hero backdrop, and section canvas. |
| Mist Gray | `#f3f3f3` | `--color-mist-gray` | Secondary surface, nav pill background, and subtle panels. |
| Paper White | `#ffffff` | `--color-paper-white` | Card surfaces, inverted text on dark blocks, and icon fills. |
| Mint Chip | `#d1ffca` | `--color-mint-chip` | Tag pills, link backgrounds, and accent highlights. |
| Voltage Yellow | `#fff100` | `--color-voltage-yellow` | Email highlights, small accent dots, and decorative bursts. |

## Typography

### SuisseIntlCond

Use for display headings only.

- Token: `--font-suisseintlcond`
- Fallback: Anton, Bebas Neue, Barlow Condensed Bold
- Weight: 700
- Sizes: 48px, 64px, 80px, 130px
- Line height: 0.90
- Letter spacing: -0.03em
- Role: massive uppercase condensed display blocks.

### SuisseIntl

Use for body text, nav, subheads, buttons, and cards.

- Token: `--font-suisseintl`
- Fallback: Inter, Sohne, Neue Haas Grotesk
- Weights: 400, 450, 500
- Sizes: 14px, 16px, 18px, 20px, 28px, 40px
- Role: workhorse neo-grotesque for 90 percent of the UI.

### SuisseIntlMono

Use for labels, technical metadata, and numbered annotations.

- Token: `--font-suisseintlmono`
- Fallback: JetBrains Mono, IBM Plex Mono, Geist Mono
- Weight: 400
- Size: 12px
- Role: micro-copy and system labels.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 12px | 1.60 | -0.36px | `--text-caption` |
| Body SM | 14px | 1.30 | -0.154px | `--text-body-sm` |
| Body | 16px | 1.25 | 0 | `--text-body` |
| Subheading | 18px | 1.33 | 0 | `--text-subheading` |
| Subheading LG | 20px | 1.20 | 0 | `--text-subheading-lg` |
| Heading SM | 28px | 1.30 | -0.84px | `--text-heading-sm` |
| Heading | 40px | 1.10 | -0.8px | `--text-heading` |
| Heading LG | 48px | 0.90 | -1.44px | `--text-heading-lg` |
| Display | 80px | 0.90 | -2.4px | `--text-display` |
| Display XL | 130px | 0.90 | -3.9px | `--text-display-xl` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 8px.
- Max width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px to 24px.

### Spacing Scale

`8, 16, 24, 40, 64, 80, 96`

### Radius Scale

| Element | Radius |
|---|---:|
| Buttons | 4px to 8px |
| Cards | 24px to 32px |
| Nav pill | 48px |
| Tags | 64px |
| Large cards | 64px |

## Components

### Filled Dark Button

Carbon Black fill, Paper White text, 8px radius, 16px by 24px padding, SuisseIntl 16px/500. Use for primary actions such as schedule demo.

### Ghost Border Button

Transparent background, 1.5px Slate border, Slate text, 4px radius, SuisseIntl 16px/500. Use for secondary actions.

### Text Link Button

No background, no border, Carbon Black text, 0px to 4px radius, underline on hover, SuisseIntl 16px/500.

### Nav Pill

Paper White or Mist Gray pill with 48px radius, centered inside an 8rem top bar. It physically separates navigation from the canvas.

### Standard Card

Paper White fill, 24px to 32px radius, 24px padding, no shadow and no border. Separation comes from canvas contrast.

### Inverted Card

Carbon Black fill, Paper White text, 32px radius, no shadow. Use for dramatic contrast zones.

### Top Arc Card

64px top-left and top-right radius, 0px bottom radius. Use for hero-bottom cards and section openers in black or white.

### Mint Tag

Mint Chip fill, Carbon Black text, 64px radius, compact padding, SuisseIntlMono 12px. Use sparingly for taxonomy and status.

### Voltage Highlight

Voltage Yellow background or text on very small elements such as emails, dots, and decorative sparks.

### 3D Product Render

Photorealistic physical object render: textured concrete cubes, wood grain, colored protrusions, and brand labels. Use as hero imagery.

### Uppercase Display Heading

SuisseIntlCond 700 at 80px to 130px, uppercase, line-height 0.9, -0.03em tracking. This is the dominant editorial voice.

### Secondary Heading

SuisseIntl 450 at 40px, uppercase, line-height 1.1, -0.02em tracking.

### Mono Label

SuisseIntlMono 12px, letter-spacing -0.03em. Use for slide indicators, metadata, and system labels.

## Layout

Use full-bleed Warm Canvas with centered 1200px content. Hero is a split: huge 130px condensed headline on the left, 3D object render on the right. Navigation sits in a floating pill in an 8rem top bar. Sections alternate between gray canvas, white cards, and full-width black inverted blocks. Use 80px section gaps and 24px internal rhythm.

## Imagery

Use photorealistic 3D object renders on the warm gray canvas. The materiality matters: concrete texture, wood grain, branded labels, and small colored geometric protrusions. Avoid stock photos, lifestyle imagery, abstract gradients, and decorative illustration.

## Do

- Use SuisseIntlCond 700 at 48px to 130px for all display headings.
- Keep display headings uppercase and tightly tracked.
- Use Warm Canvas as the page background.
- Use 24px to 64px card radii deliberately.
- Reserve Mint Chip for tags and link backgrounds.
- Reserve Voltage Yellow for email highlights and micro-accents.
- Keep all cards flat.
- Use 16px/500 SuisseIntl for body and buttons.

## Don't

- Do not add shadows to cards or buttons.
- Do not use pure white as the page background.
- Do not use mint or yellow for large surfaces.
- Do not set display heading line-height above 0.95.
- Do not use mixed-case display headings.
- Do not use SuisseIntlCond below 48px.
- Do not add subtle borders to cards; prefer surface contrast.
