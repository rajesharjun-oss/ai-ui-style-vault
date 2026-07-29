# Revolut - Style Reference

> Monochrome editorial banking on cloud photography.

Theme: light

Revolut uses a high-contrast but restrained fintech language. The actual UI is nearly achromatic: white surfaces, near-black text, recessed light-gray groups, and thin gray dividers. Color mostly comes from full-bleed sky and cloud photography. In the UI itself, the one vivid moment is a blue promotional gradient, reserved for the top offer strip.

The brand feeling comes from huge medium-weight display type, aggressive tracking compression, and pill-shaped controls. The interface should feel confident, consumer-friendly, polished, and commercial without becoming playful or colorful.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Ink | `#1f1f1f` | `--color-ink` | Main text, dark nav, footer, dark section bands, and filled dark buttons. |
| Pure Black | `#000000` | `--color-pure-black` | Maximum-contrast text or black blocks where needed. |
| Bone | `#ffffff` | `--color-bone` | Page canvas, cards, white buttons, and text on dark surfaces. |
| Ash Grey | `#c9c9cd` | `--color-ash-grey` | Hairline dividers, disabled borders, and edge separation. |
| Mist | `#f7f7f7` | `--color-mist` | Recessed list groups and secondary containers. |
| Slate | `#717173` | `--color-slate` | Muted text, badges, quiet state feedback, and soft section headers. |
| Graphite | `#4c4c4c` | `--color-graphite` | Tertiary copy and minor muted surfaces. |
| Cobalt Wash | `linear-gradient(to right, #1227fd, #6fa0ff)` | `--gradient-cobalt-wash` | Only chromatic UI accent, used for the promotional strip. |

## Tokens - Typography

### Aeonik Pro

Marketing display and heading face.

- Substitute: Inter, DM Sans, Manrope, system-ui, sans-serif
- Weights: 400, 500
- Sizes: 16px, 18px, 24px, 32px, 40px, 52px, 88px
- Line heights: tight, from 1.0 to about 1.38
- Letter spacing: tighten from about -0.024em at 88px to -0.010em around 24px to 40px
- Rule: headings should feel large and precise, not bold. Do not exceed weight 500.

### Inter

Product UI and body face.

- Substitute: system-ui, sans-serif
- Weights: 400, 600, 700
- Sizes: 12px, 14px, 16px
- Line heights: 1.20, 1.50, 1.57
- Letter spacing: slight negative tracking for body, positive tracking for 12px uppercase labels
- Rule: use for buttons, labels, nav, badges, form text, and normal body copy.

### Type Scale

| Role | Size | Weight | Line Height | Tracking | Font |
| --- | --- | --- | --- | --- | --- |
| caption | 12px | 600 | 18px | 0.18px | Inter |
| body-sm | 14px | 400 | 22px | -0.07px | Inter |
| body | 16px | 400 | 19.2px | 0 | Inter |
| subheading | 18px | 400 | 24px | 0 | Aeonik Pro |
| heading-sm | 24px | 500 | 28px | -0.24px | Aeonik Pro |
| heading | 32px | 500 | 38px | -0.32px | Aeonik Pro |
| heading-lg | 40px | 500 | 48px | -0.4px | Aeonik Pro |
| display | 52px | 500 | 52px | -0.624px | Aeonik Pro |
| display-xl | 88px | 500 | 88px | -2.112px | Aeonik Pro |

## Tokens - Spacing And Shape

- Density: compact
- Base unit: 8px
- Page max width: 1200px
- Section gap: 80px
- Card padding: 24px
- Element gap: 8px
- Scale: 8, 16, 24, 32, 40, 56, 64, 80, 232px

### Radius

| Element | Value |
| --- | --- |
| Buttons | 9999px |
| Tags | 9999px |
| Inputs | 9999px |
| Small controls | 12px |
| Lists | 20px |
| Cards | 22.5px |

### Elevation

Standard cards and buttons should not use shadows. Separate surfaces with color shifts, 1px to 2px `#c9c9cd` borders, and dark section bands. Save shadows for popovers, dialogs, and modals only.

## Components

### Pill Button - Light

White background, `#1f1f1f` text, 2px dark border, full pill radius, 10px by 24px padding, and 16px Inter semibold text. Use on light hero and content surfaces.

### Pill Button - Dark

`#1f1f1f` background, white text, full pill radius, compact horizontal padding, and vertically centered 16px Inter semibold text. Use for primary app-download or sign-up actions, especially over light sky photography.

### Pill Button - Ghost On Photo

Translucent white background, white text, white 1px border, full pill radius, and 10px by 24px padding. Use only when a control sits over photography.

### Pill Text Link

Transparent small interactive element with near-black text at reduced emphasis and a 12px radius. Use inside copy or dense UI where a full CTA would be too loud.

### Promo Gradient Bar

Top-of-page offer strip with the cobalt gradient, white 16px text, and an underlined white inline link. Height should be around 32px to 40px. This is the only chromatic UI surface.

### Navigation Header

Dark `#1f1f1f` bar with white wordmark on the left, centered 16px nav items, and account actions on the right. Pair text login with a sign-up pill.

### Location Selector Pill

White utility pill for country or region switching. Use full radius, compact Inter text, and a small flag or location mark.

### Phone Preview Card

Product UI appears inside an iPhone-like white card overlay. Use 22.5px top radius, square bottom edge when overlapping a photo boundary, and a clean white internal product UI.

### Pricing Tier Card

White card on a dark `#1f1f1f` section. Use 22.5px radius, 24px to 40px padding, Aeonik medium tier names and prices, and muted Inter descriptions. Arrange in a three-column comparison where possible.

### Trust Badge Block

Transparent grid cell with centered logo or badge, then 12px to 14px Inter caption in `#717173`. Use large gaps so the trust grid feels editorial, not dense.

### Muted Section Header

24px to 40px Aeonik Pro at weight 500 in Slate `#717173`. The muted heading is intentional and keeps the page calm between high-impact hero moments.

### List Container

Recessed `#f7f7f7` group with 20px radius and 16px to 24px padding. Use for feature lists, FAQs, and grouped rows.

## Layout

Use full-bleed photography for hero sections and let white text sit directly over the image with generous negative space. Below hero areas, return to white editorial sections with 1200px max-width content and 80px section spacing.

Pricing and conversion moments can flip to `#1f1f1f` backgrounds with white cards. The dark/light contrast is a major Revolut pattern. Keep grids measured, symmetrical, and conversion-oriented.

## Imagery

Photography is the primary source of color. Use high-key sky and cloud images with soft blues and whites. Human subjects should feel candid, naturally lit, and editorial. Leave enough negative space for large white display text.

Avoid decorative graphics, 3D renders, illustrations, loud gradients, and flat product screenshot blocks. Product UI should appear in phone-frame overlays, not as loose screenshots.

## Do

- Use 9999px radius for buttons, tags, and input controls.
- Keep display headings at weight 500 or lower.
- Reserve the blue gradient for the promo strip.
- Use hairline borders instead of card shadows.
- Let photography carry color while UI remains neutral.
- Tighten tracking across display sizes.
- Use dark pricing bands with white cards.

## Do Not

- Do not introduce extra chromatic colors.
- Do not use shadows on cards or buttons.
- Do not set Aeonik headings above weight 500.
- Do not reuse the promo gradient on cards, buttons, or hero sections.
- Do not use square primary actions.
- Do not mix Inter and Aeonik at the same visual level.
- Do not use color as the main state indicator on neutral surfaces.

