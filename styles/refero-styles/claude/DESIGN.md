# Claude Style Reference

Claude is a warm-paper editorial product system. The design reads like ink on a printed artifact: parchment canvas, layered white and stone cards, careful serif headings, functional sans text, and one clay-orange chromatic accent used only as a small brand flourish.

## Theme

Light, warm-paper, editorial, AI product, monochrome, humane, calm, printed, rounded paper cards.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Bone Parchment | `#f8f8f6` | `--color-bone-parchment` | Page canvas, large backgrounds, nav bar, and secondary cards. |
| Paper White | `#ffffff` | `--color-paper-white` | Elevated cards and primary content surfaces above the canvas. |
| Soft Stone | `#efeeeb` | `--color-soft-stone` | Nested cards, subtle surface variation, and alternate section bands. |
| Carbon Ink | `#121212` | `--color-carbon-ink` | Primary text, headings, icon fills, and dark buttons. |
| Graphite | `#373734` | `--color-graphite` | Secondary headings, button text, nav text, and inline links. |
| Ashen | `#7b7974` | `--color-ashen` | Helper text, captions, fine print, and disclaimer copy. |
| Pebble | `#9c9a92` | `--color-pebble` | Tertiary text, copyright, and low-priority labels. |
| Mist | `#b7b7b5` | `--color-mist` | Hairline nav dividers, input borders, and subtle rules. |
| Chalk | `#e7e6e1` | `--color-chalk` | Soft border lines, illustration fills, and pale background tints. |
| Obsidian | `#000000` | `--color-obsidian` | Footer background only; avoid for body text. |
| Clay | `#d97757` | `--color-clay` | Decorative marks, icons, dots, and illustration details only. |

## Typography

### Anthropic Serif

Use only for display and editorial headlines.

- Token: `--font-anthropic-serif`
- Fallback: Source Serif 4, Charter, Georgia
- Weight: 400
- Sizes: 24px, 30px
- Line height: 1.20 to 1.33
- Letter spacing: normal
- Role: editorial authority. It should whisper through contrast, not shout through bold weight.

### Anthropic Sans

Use for all interface and functional text.

- Token: `--font-anthropic-sans`
- Fallback: Inter, IBM Plex Sans, system-ui
- Weights: 400, 500, 550, 580, 600
- Sizes: 11px, 12px, 14px, 15px, 16px, 24px
- Line height: 1.33 to 1.63
- Letter spacing: normal
- Role: body copy, navigation, buttons, cards, links, labels, inputs, FAQs, captions, and prices.

### Type Scale

| Role | Size | Line Height | Weight | Token |
|---|---:|---:|---:|---|
| Caption | 11px | 1.50 | 400 | `--text-caption` |
| Tiny | 12px | 1.33 | 400 | `--text-tiny` |
| Body | 14px | 1.50 | 400 | `--text-body` |
| Body LG | 15px | 1.50 | 400 | `--text-body-lg` |
| Article | 16px | 1.63 | 400 | `--text-article` |
| Heading SM | 24px | 1.33 | 580 | `--text-heading-sm` |
| Heading | 30px | 1.20 | 400 | `--text-heading` |

## Spacing And Shape

- Density: compact.
- Base unit: 8px.
- Max width: 1200px.
- Section gap: 64px to 80px.
- Card padding: 32px.
- Element gap: 8px to 12px.

### Spacing Scale

`8, 16, 24, 32, 40, 64, 80, 96`

### Radius Scale

| Element | Radius |
|---|---:|
| Nav controls | 8px |
| Inputs | 8px |
| Buttons | 8px |
| Cards | 16px |
| Elevated cards | 24px |

### Elevation

| Name | Token | Value |
|---|---|---|
| Feature hover | `--shadow-feature-hover` | `rgba(0, 0, 0, 0.04) 0px 4px 20px 0px` |
| Pricing hover | `--shadow-pricing-hover` | `rgba(35, 30, 24, 0.1) 0px 4px 24px 0px` |

Use elevation rarely. The default state is flat, with paper layering and hairline borders.

## Components

### Filled Dark Button

Carbon Ink fill, Bone Parchment or Paper White text, 8px radius, 8px vertical and 20px horizontal padding, Anthropic Sans 15px/500. Use as the primary CTA on light surfaces. Do not use Clay.

### Pill Navigation Button

Transparent background, Graphite text, no border, 8px radius, Anthropic Sans 15px/500. Sits on the parchment nav canvas with generous horizontal padding.

### Pricing Tier Card

Paper White surface on Bone Parchment, 24px radius, 32px padding. Plan name uses Anthropic Serif 24px to 30px. Price uses Carbon Ink, description uses Ashen. Default is flat; hover or featured tier may use the soft warm shadow.

### Feature Benefit Card

Soft Stone or Paper White surface, 16px radius, 24px to 32px padding. Checkmark icons use Carbon Ink, body text uses 14px Graphite. Keep flat.

### Editorial Section Header

Anthropic Serif 30px/400, Carbon Ink, line-height 1.2. Follow with short Anthropic Sans body copy in Ashen or Graphite. Place after generous 64px to 80px section spacing.

### Footer Band

Full-width Obsidian footer, the only true-black surface. Use muted Pebble links and compact 14px sans link columns.

### Inline Link

Graphite by default, Carbon Ink on hover, underline for clarity. Do not use Clay or blue link coloring.

### Input Field

Transparent or Paper White fill, 1px Mist border, 8px radius, 14px Anthropic Sans. Focus state can use a soft inset ring and subtle outer glow; avoid dramatic color shifts.

### FAQ Accordion Item

Borderless or hairline-separated item, question in Graphite 14px to 16px, body in Carbon Ink 14px. Use 24px vertical padding and no serif in the FAQ body.

### Clay Accent Mark

Small Clay dot, ornament, icon detail, or illustration mark. It is non-interactive and decorative only.

### Status Badge

Small 11px to 12px sans label with 8px radius and low-contrast warm-gray background. Prefer monochrome status treatment.

## Layout

Use a 1200px centered content rail on Bone Parchment. Hero sections are centered editorial stacks with generous whitespace, sometimes paired with a full-width product or editorial image below. Sections alternate between the parchment canvas, Paper White cards, and Soft Stone bands. Pricing uses a 3-column card grid with one elevated or featured tier. FAQs and CTAs use centered stacks. Navigation is minimal: logo left, links clustered right or centered, with no heavy border or fill.

## Imagery

Imagery is sparse, warm, editorial, and used as punctuation. Use product visuals or calm illustrations in rounded 16px to 24px containers. Clay may appear in small illustration details. Icons are monochrome Carbon Ink. Avoid gradients, glows, 3D renders, multicolor icons, and dense dashboards.

## Do

- Use Bone Parchment as the page canvas.
- Use Anthropic Serif 24px to 30px at weight 400 for editorial headings.
- Keep Anthropic Sans mostly between 400 and 580.
- Use Paper White cards over Bone Parchment for a layered paper effect.
- Use Clay only for small decorative marks.
- Use 24px radius for elevated cards and 16px for nested cards.
- Use 8px radius for buttons, inputs, and nav controls.
- Keep section spacing at 64px to 80px.

## Don't

- Do not use Clay for button fills, links, or major CTA surfaces.
- Do not use pure black for body text.
- Do not set headings at 700 or heavier.
- Do not use cool blue, green, or red as brand accents.
- Do not use heavy shadows.
- Do not set large display headings in Anthropic Sans.
- Do not add decorative gradients.
