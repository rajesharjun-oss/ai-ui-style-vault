# Superhuman - Style Reference

## North Star

Build the interface like a golden-hour editorial dashboard: warm parchment canvas, cinematic photography, maroon conversion moments, violet text links, translucent product UI floating over imagery, and quiet confident typography. The page should feel premium, fast, and considered.

## Theme

Light. Warm Parchment is the full-page canvas. Paper White is reserved for elevated cards and floating UI. Midnight Wine is the primary action color. Royal Violet is for inline links only.

## Color Tokens

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Midnight Wine | `#421d24` | `--color-midnight-wine` | Primary action buttons, announcement banner, footer, warm maroon anchor |
| Royal Violet | `#714cb6` | `--color-royal-violet` | Inline links, short emphasized phrases, text accents only |
| Lilac Mist | `#d4c7ff` | `--color-lilac-mist` | Secondary surface fills, light badges, ghost button backgrounds |
| Deep Lagoon | `#0c4243` | `--color-deep-lagoon` | Dark feature band background, used sparingly |
| Ink Charcoal | `#292827` | `--color-ink-charcoal` | Primary text, headings, icons, warm near-black |
| Stone Gray | `#666666` | `--color-stone-gray` | Secondary body text, helper copy, muted descriptions |
| Soft Mist | `#e3e3e2` | `--color-soft-mist` | Hairline borders, card outlines, dividers |
| Warm Parchment | `#f2f0eb` | `--color-warm-parchment` | Page canvas and dominant warm editorial surface |
| Paper White | `#ffffff` | `--color-paper-white` | Elevated cards, floating UI overlays, text on dark surfaces |

## Typography

Use Super Sans VF if available. Fallback to Inter, Sohne, or General Sans.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 12px | 500 | 1.5 | 0 |
| Body Small | 14px | 460 | 1.5 | 0 |
| Body | 16px | 460 | 1.2 | 0 |
| Label Bold | 19px | 700 | 1.5 | 0 |
| Subheading | 26px | 460 | 1.3 | 0 |
| Heading Small | 28px | 540 | 1.14 | -0.62px |
| Heading Large | 49px | 460 | 1.2 | -1.32px |
| Display | 64px | 540 | 0.96 | -1.8px |

Font role:

- Super Sans VF: the sole typeface across the system.
- Use weight 460 for all headlines at 28px and above unless a specific emphasis needs 540.
- Use 540 for body emphasis and 700 only for small labels.
- Enable `"ss01"` if supported by the font.
- Use tabular numerals in data-heavy product UI cards.

Tracking:

- 64px: about -0.028em.
- 49px: about -0.027em.
- 28px: about -0.022em.
- 22px: about -0.014em.
- 18px: about -0.008em.
- 20px: about -0.007em.
- 16px and below: 0.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | Comfortable |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 64px to 96px |
| Card padding | 16px |
| Element gap | 8px |

Spacing scale: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 48, 64, 80, 96.

Radius scale:

- Tabs: 8px.
- Small buttons: 8px.
- Cards: 16px.
- Buttons: 16px.
- Floating cards: 16px.
- Pills: 999px.

Elevation:

- Default to no drop shadows.
- Signature outline: `rgb(113, 76, 182) 0px 0px 0px 1px inset`.
- Header may use `backdrop-filter: blur(12px)` on scroll.
- Floating product cards rely on photo layering and translucent surfaces, not shadows.

## Components

### Primary Action Button

Use Midnight Wine background, Paper White text, no border, 16px radius, roughly 48px height, 12px horizontal padding, Super Sans 16px at 460 weight, and optional small arrow icon with 8px gap. This is the only chromatic filled button.

### Ghost Text Button

Use transparent background, Ink Charcoal text, no border, no radius, and underline on hover. Use for nav links, inline learn-more links, and low-emphasis actions.

### Outlined Light Button

Use Lilac Mist background, Ink Charcoal text, 1px Ink Charcoal border, 8px radius, and 6px vertical by 16px horizontal padding. This is secondary, not primary.

### Pill Announcement Banner

Use Midnight Wine background, Paper White text, 999px horizontal pill ends clipped to page edges, 12px vertical by 16px horizontal padding, a small icon, inline copy, and a bordered learn-more link.

### Floating Product Card

Use Paper White at about 85 percent opacity, 16px radius, 16px padding, and a 1px semi-transparent white border. No drop shadow. Place over cinematic photography so depth comes from compositing.

### Trust Logo Card

Use Paper White background, 1px Soft Mist border, square cell, no individual rounding, 24px vertical padding, monochrome Ink Charcoal logo centered. Arrange in a single row of 6 cells.

### Suite Tab Strip

Use a white 4-column horizontal strip with 8px outer radius. Each tab has 16px padding. Active tab uses Lilac Mist fill and a small chromatic icon. Inactive tabs are white with Ink Charcoal icons.

### Suite Product Card

Use Paper White background, 16px radius, 16px padding, no shadow. Include colored icon, product name, body text, and Royal Violet learn-more link.

### Navigation Header

Use transparent background with backdrop blur on scroll and a 1px Soft Mist bottom border that fades in. Logo left, center links at 16px/460, and auth controls right. Height about 64px.

### Dark Feature Band

Use full-bleed Deep Lagoon background. Pair geometric art on one side with Paper White headline/body on the other. Use this once for tonal contrast.

### Gradient Banner

Use layered atmospheric radial gradients as a background, not an interactive surface. Place Ink Charcoal headline and Paper White CTA in the composition. Use sparingly.

### Footer

Use Midnight Wine background, Paper White headings, body text at about 70 percent opacity, no radius, 64px vertical padding, and multi-column link layout.

### Link With Underline

Use Royal Violet text, no underline by default, underline on hover, 0.2s ease. Use the same size as surrounding text and weight 460.

### Section Heading

Use Super Sans VF weight 460, 48px, line-height 0.96, Ink Charcoal. No italic, no decoration, no text transform.

## Layout And Imagery

- Use a 1200px max-width centered container.
- Keep Warm Parchment as the page background.
- Use cinematic full-bleed hero photography.
- Float translucent product UI cards over hero images.
- Use white product cards on parchment only when a surface needs to lift.
- Use trust logo strips and suite tabs as structured product proof.
- Avoid centered body copy longer than two lines.
- Let photography and blur create depth.

## Do

- Use weight 460 for all headlines at 28px and above.
- Set body text to Ink Charcoal on Warm Parchment.
- Use Midnight Wine as the single primary action fill.
- Reserve Royal Violet exclusively for inline links.
- Float product cards over photography with 16px radius and no drop shadow.
- Apply header backdrop blur on scroll.
- Keep display tracking tight and body tracking neutral.

## Do Not

- Do not use weight 700+ for headlines.
- Do not place white surfaces directly on white page backgrounds.
- Do not add drop shadows to cards.
- Do not introduce blue, green, or red accents.
- Do not use violet as a button fill, badge, or icon stroke.
- Do not center body copy longer than two lines.
