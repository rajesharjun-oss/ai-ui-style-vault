# Jeton - Style Reference

> Editorial fintech on warm marble

**Theme:** light

Jeton reads like a premium fintech editorial system: near-white canvas, large confident typography, a single hot orange-red accent, and warm near-black text. The UI feels intentionally flat, using whitespace and geometric rounding more than visible borders or deep elevation. It is not a dense SaaS dashboard; it is closer to a magazine spread for financial infrastructure.

The core tension is restraint plus punctuation. Most surfaces stay white or barely tinted, then Signal Orange appears in short bursts for headings, links, icons, and primary action moments. Feature cards can use coral, cobalt, or green accents, but those are category colors, not a general palette expansion.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Signal Orange | `#f73b20` | `--color-signal-orange` | Primary brand accent for links, key headings, icons, and main emphasis. |
| Brand Orange Tint | `#f84d35` | `--color-brand-orange-tint` | Slightly softer orange for small brand UI details and active indicators. |
| Ink Roast | `#360802` | `--color-ink-roast` | Warm near-black for primary body text, inputs, and editorial headings. |
| Paper White | `#ffffff` | `--color-paper-white` | Dominant page canvas and most card surfaces. |
| Carbon Black | `#000000` | `--color-carbon-black` | Utility icons, compact currency labels, and rare secondary details. |
| Ash Grey | `#ababab` | `--color-ash-grey` | Disabled states, placeholders, subtle divider marks, and low-emphasis meta. |
| Sand Wash | `#e7dcdb` | `--color-sand-wash` | Warm neutral wash for soft section or panel separation. |
| Linen Blush | `#fdedea` | `--color-linen-blush` | Pale orange-tinted card, input, and highlight surface. |
| Citrus Wash | `#f5ffbb` | `--color-citrus-wash` | Pale yellow-green surface tint for highlighted content. |
| Mint Wash | `#bcffbb` | `--color-mint-wash` | Green wash for emphasis bands and soft funding/add states. |
| Coral Red | `#fb2d54` | `--color-coral-red` | Exchange or currency category accent. |
| Cobalt Blue | `#477ee9` | `--color-cobalt-blue` | Send or transfer category accent. |
| Emerald Green | `#34c771` | `--color-emerald-green` | Add, funding, or positive category accent. |

## Tokens - Typography

### Sequel Sans

- **Token:** `--font-sequel-sans`
- **Substitute:** Inter, Manrope, or DM Sans
- **Weights:** 400, 450, 500
- **Sizes:** 12, 14, 16, 23, 33, 44, 72, 106, 110, 155
- **Line height:** 0.90 / 1.00 / 1.20 / 1.25 / 1.40 / 1.50
- **Letter spacing:** 0.0100em for display and headings, 0.0300em for small labels, nav, and buttons
- **Role:** A geometric grotesque carries the whole system. Hierarchy comes from scale and tight leading, not from bold weights.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 12px | 1.5 | 0.36px | `--text-caption` |
| body-sm | 14px | 1.4 | 0.42px | `--text-body-sm` |
| body | 16px | 1 | 0 | `--text-body` |
| subheading | 23px | 1.2 | 0.23px | `--text-subheading` |
| heading-sm | 33px | 1.2 | 0.33px | `--text-heading-sm` |
| heading | 44px | 1.2 | 0.44px | `--text-heading` |
| heading-lg | 72px | 1 | 0.72px | `--text-heading-lg` |
| display | 106px | 1 | 0 | `--text-display` |
| display-xl | 110px | 1 | 1.1px | `--text-display-xl` |
| display-hero | 155px | 0.9 | 1.55px | `--text-display-hero` |

## Tokens - Spacing And Shapes

**Base unit:** 4px

**Density:** comfortable

| Purpose | Value |
|---------|-------|
| Max width | 1200px |
| Section gap | 80px |
| Card padding | 16px |
| Element gap | 8px |

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 4 | 4px | `--spacing-4` |
| 8 | 8px | `--spacing-8` |
| 12 | 12px | `--spacing-12` |
| 16 | 16px | `--spacing-16` |
| 20 | 20px | `--spacing-20` |
| 24 | 24px | `--spacing-24` |
| 32 | 32px | `--spacing-32` |
| 48 | 48px | `--spacing-48` |
| 56 | 56px | `--spacing-56` |
| 160 | 160px | `--spacing-160` |

### Radius

| Element | Value | Token |
|---------|-------|-------|
| links | 8px | `--radius-links` |
| buttons | 12px | `--radius-buttons` |
| cards | 16px | `--radius-cards` |
| inputs | 16px | `--radius-inputs` |
| nav | 84px | `--radius-nav` |
| pills | 9999px | `--radius-pills` |

### Shadows

| Name | Value | Token |
|------|-------|-------|
| floating glass panel | `rgba(247, 59, 32, 0.1) 0px 8px 24px 0px, rgba(247, 59, 32, 0.05) 0px 2px 8px 0px` | `--shadow-lg` |
| content card | `rgba(0, 0, 0, 0.05) 0px -4px 16px 0px` | `--shadow-md` |

### Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#ffffff` | Main page background. |
| 1 | Card Surface | `#ffffff` | Standard card background with minimal lift. |
| 2 | Orange Tint | `#fdedea` | Warm highlight, input, and row surface. |
| 3 | Frosted Glass | `#ffffff1a` | Translucent floating panel overlay. |
| 4 | Category Tint | `#f73b200d` | Subtle orange-tinted feature card surface. |

## Components

### Primary Pill Button

Filled Signal Orange background, white text, 12px radius, 8px vertical and 16px horizontal padding. Use 14px Sequel Sans style type, weight 450, and 0.03em tracking. Reserve for the principal action on a screen.

### Ghost Text Link

No fill, Signal Orange text, 8px radius, and 8px padding. Works inline with body copy or as a standalone text link with a small arrow or chevron.

### White Ghost Button

Transparent surface, white text, 1px white border, 84px pill radius, and 16px horizontal padding. Best inside nav or over image/glass contexts.

### Outline Brand Button

Transparent background, Signal Orange text, 1px Signal Orange border, square-ish text-link treatment, and no heavy fill. Use sparingly for inline CTAs.

### Utility Icon Button

Transparent surface, Carbon Black text or icon, 16px radius, and 12px padding. Use for compact currency selectors, short labels, or toggles.

### Frosted Glass Card

Use `rgba(255,255,255,0.1)` with 16px radius, 16px padding, and backdrop blur between 20px and 40px. Add the orange-tinted large shadow only when the panel is floating above a hero or product visual.

### Feature Category Card

Use a pastel-tinted background, 16px radius, roomy padding, a large geometric icon, and a category heading. Color coding can use Signal Orange, Coral Red, Cobalt Blue, or Emerald Green, but keep each card focused on one accent.

### Floating Input Field

Use a `rgba(247,59,32,0.05)` background, Ink Roast text, 16px radius, and generous left padding for icons. The field should feel warm and editorial, not boxed-in or enterprise-heavy.

### Bordered Content Card

Use white surface, 16px radius, 16px padding, and the upward/inverted content shadow. Avoid thick borders unless they are required for accessibility contrast.

### Orange-Tinted Card

Use the orange alpha surface with 16px radius for promotional content, notifications, or soft emphasis without turning the whole section orange.

### Scroll Indicator

Use small numeric steps like 01, 02, 03, 04 with concise labels. Keep typography compact and geometric.

### Top Navigation Bar

Logo left, primary nav center, Personal/Business style toggle and language/CTA controls right. Use 14-16px type, subtle blur when layered, and pill-shaped actions.

## Do's And Don'ts

### Do

- Set display headlines at 72-155px with 0.9-1.0 line-height.
- Treat Signal Orange as the main chromatic voice.
- Keep blue, green, and coral for category cards only.
- Use 16px radius for cards, inputs, and most containers.
- Use pill geometry only for true pill buttons, tags, and nav controls.
- Pair warm-tinted surfaces with Ink Roast text.
- Use the inverted card shadow for lift, not heavy drop shadows.
- Keep white as the dominant canvas.
- Separate sections with whitespace before adding extra backgrounds.

### Don't

- Do not introduce a second typeface.
- Do not use 600+ font weights.
- Do not add shadows to text or buttons.
- Do not use pure black for body copy.
- Do not multiply accent colors across a single component.
- Do not set display line-height above 1.2.
- Do not use sharp corners on interactive surfaces.
- Do not build a dense table-first dashboard from this style.

## Imagery

The visual language depends more on typography and geometric UI than photography. When imagery appears, use abstract or product-adjacent forms, tight crops, warm color grading, and simple 3D particle or rounded geometric motifs. Avoid generic lifestyle photography.

## Layout

Use full-width sections with centered content up to 1200px. Lead with an oversized left-aligned hero headline, brief supporting copy, and a small orange CTA. Feature areas should breathe: two or three columns, large gutters, soft card rounding, minimal borders, and section gaps of about 80px or more.

## Agent Prompt Guide

### Quick Color Reference

- Text: `#360802` for body and headings, `#f73b20` for emphasis, `#000000` only for utility.
- Background: `#ffffff` canvas, `#fdedea` warm tint, `rgba(247,59,32,0.05)` brand tint.
- Border: `#e7dcdb` neutral, `rgba(247,59,32,0.1)` for glass-like warm tint.
- Accent: `#f73b20` primary, `#477ee9` send, `#34c771` add/funding, `#fb2d54` exchange.

### Example Component Prompts

1. Hero section: white background, left-aligned headline at 106px or larger, Sequel Sans style type, weight 500, Ink Roast color, line-height 1.0, and a short Signal Orange text link.
2. Feature category card: pale orange-tinted background, 16px radius, 24px padding, large geometric icon, 33px heading, and one category accent.
3. Floating input field: warm orange alpha background, Ink Roast text, 16px radius, 48px left padding for an icon, and no heavy border.
4. Navigation bar: white or lightly frosted background, 14-16px links, logo left, nav center, pill toggle and CTA on the right.
5. Content card: white surface, 16px radius, 16px padding, inverted upward shadow, 44px heading, and concise copy.

## Similar Reference Families

- Wise style fintech editorial systems with one warm accent and big type.
- Revolut style card-based fintech features with category-coded tiles.
- Stripe style restrained product hierarchy with premium spacing.
- Mercury style banking surfaces with warm tinted inputs and quiet elevation.

