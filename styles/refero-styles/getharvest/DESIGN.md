# Getharvest Style Reference

Getharvest is a warm productivity-workspace system. It uses cream paper, white floating product cards, one orange action color, rounded tactile components, and warm shadows. The style should feel approachable and useful rather than decorative.

## Theme

Light, productivity, warm SaaS, cream canvas, orange accent, product screenshots, friendly B2B, tactile cards.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Harvest Flame | `#fa5d00` | `--color-harvest-flame` | Primary CTA fill, active states, links, icon accents, and brand borders. |
| Marigold Glow | `#fee3b5` | `--color-marigold-glow` | Soft warm highlight wash on cards and decorative glow behind product UI. |
| Parchment Shadow | `#e3d6c5` | `--color-parchment-shadow` | Warm-tinted card and image shadow color. |
| Ink Black | `#1d1e1c` | `--color-ink-black` | Primary text, icon strokes, nav borders, and card headings. |
| Ironwood | `#4a4a47` | `--color-ironwood` | Strong secondary text and emphasized muted labels. |
| Warm Stone | `#615f5c` | `--color-warm-stone` | Secondary body text, list items, and muted icon strokes. |
| Ash | `#777571` | `--color-ash` | Helper text, placeholders, and low-priority borders. |
| Driftwood | `#8e8b87` | `--color-driftwood` | Tertiary body text, decorative strokes, and subtle metadata. |
| Graphite | `#999999` | `--color-graphite` | List borders and tertiary structural lines. |
| Smoke | `#a5a19c` | `--color-smoke` | Disabled text and very low-priority separators. |
| Bone | `#c0bbb6` | `--color-bone` | Input borders and form field outlines at rest. |
| Mist Gray | `#d9d9d9` | `--color-mist-gray` | Hairline dividers and subtle borders on neutral surfaces. |
| Cream Canvas | `#fff8f1` | `--color-cream-canvas` | Page background, hero base, and nav backdrop. |
| Paper White | `#ffffff` | `--color-paper-white` | Card surfaces, input fields, elevated panels, and text on orange fills. |

## Typography

### MuotoWeb

Use for navigation, buttons, body copy, subheadings, product cards, and most headings.

- Token: `--font-muotoweb`
- Fallback: Inter, Sohne, system-ui
- Weights: 400, 500, 600, 700
- Sizes: 13px to 50px
- Line height: 1.15 to 1.50
- Letter spacing: 0.015em
- Role: warm geometric workhorse with enough friendliness for productivity software.

### Monarch

Use only for hero-grade emotional display headlines.

- Token: `--font-monarch`
- Fallback: GT Super, Tiempos Headline, Georgia
- Weight: 400
- Size: 72px
- Line height: 1.20
- Role: a single editorial contrast moment in the hero or page title.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 13px | 1.35 | 0.2px | `--text-caption` |
| Subheading | 18px | 1.40 | 0.27px | `--text-subheading` |
| Heading SM | 20px | 1.30 | 0.3px | `--text-heading-sm` |
| Heading | 24px | 1.26 | 0.36px | `--text-heading` |
| Heading LG | 28px | 1.20 | 0.42px | `--text-heading-lg` |
| Display | 48px | 1.15 | 0.72px | `--text-display` |
| Display LG | 72px | 1.20 | 0 | `--text-display-lg` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Max width: 1200px.
- Section gap: 64px to 80px.
- Card padding: 32px to 40px.
- Element gap: 16px to 24px.

### Spacing Scale

`4, 5, 7, 10, 14, 15, 16, 20, 22, 25, 30, 35, 40, 50, 100, 113`

### Radius Scale

| Element | Radius |
|---|---:|
| Tags | 999px |
| Images | 16px |
| Inputs | 16px |
| Buttons | 16px |
| Cards | 20px |

### Elevation

| Name | Token | Value |
|---|---|---|
| Button lift | `--shadow-sm` | `rgba(0, 0, 0, 0.2) 0px 1px 4px 0px` |
| Warm card glow | `--shadow-lg` | `rgba(250, 166, 0, 0.25) 6px 4px 24px 0px` |

Use warm-tinted depth. Avoid cold neutral or blue shadows.

## Components

### Primary CTA Button

Harvest Flame fill, Paper White text, MuotoWeb 16px/600, 0.015em tracking, 12px by 24px padding, 16px radius, and subtle black lift. Use for the primary action only.

### Ghost Text Link

No fill, no border, Harvest Flame text, MuotoWeb 16px/500, optional small arrow. Underline on hover.

### Email Input Field

Paper White fill, 1px Bone border, 16px radius, 14px by 20px padding, Driftwood placeholder, and Harvest Flame focus outline.

### Feature Card

Cream or Paper White fill, 20px radius, 32px to 40px padding, optional warm orange glow. Use Ink Black icon, 20px to 24px heading, Warm Stone body, and orange link.

### Integration Logo Circle

48px Paper White circle containing a literal third-party logo. External brand colors can appear only inside these logo assets.

### Navigation Bar

Cream Canvas background, Harvest wordmark, MuotoWeb 16px nav links in Ink Black, dropdown chevrons where needed, sign-in ghost link, and primary orange CTA.

### Dashboard Preview Card

Paper White product screenshot container, 16px radius, warm soft shadow, showing timesheets, reports, charts, or invoicing UI.

### Section Heading

Small uppercase orange eyebrow, followed by MuotoWeb 34px to 48px title in Ink Black and optional Warm Stone subtitle.

### Trust Badge Logo Row

Uppercase label in Warm Stone, optional orange number highlight, and grayscale partner logos in Ink Black at reduced opacity.

### Hero Gradient Wash

Soft organic background wash using Harvest Flame, Marigold Glow, and peach tones at low opacity behind product preview cards. Decorative only.

### Feature Grid

Two-column product block or three-card feature grid. Keep cream canvas visible and place white product cards above it.

## Layout

Use a centered 1200px max-width container on a full-bleed Cream Canvas. The hero is centered and editorial: Monarch display headline, short subtitle, email capture or CTA, warm orange glow, and floating product preview cards. Sections alternate between centered text blocks, three-column cards, and two-column text plus screenshot blocks. Keep 64px to 80px vertical rhythm and generous horizontal padding.

## Imagery

Use real product screenshots: timesheets, dashboards, reports, budget charts, invoicing, and integrations. Put screenshots in white cards with 16px radius and warm shadows. Use dark geometric icons in feature cards. Keep partner logos grayscale. Avoid lifestyle photography, abstract 3D, cool-toned shadows, and broad saturated backgrounds.

## Do

- Use Cream Canvas as every page background.
- Use Harvest Flame as the only brand accent.
- Use Harvest Flame for primary CTAs, active states, links, and small brand marks.
- Use Monarch only for 72px hero-grade display.
- Use MuotoWeb for all headings 50px and below.
- Use 16px radius for buttons, inputs, and images.
- Use 20px radius for cards.
- Use warm-tinted shadows and glows.
- Keep partner logos grayscale.

## Don't

- Do not use Paper White as the page background.
- Do not introduce a second accent color.
- Do not use Harvest Flame for body text or large background fills.
- Do not use Monarch for body, labels, subheads, or small headings.
- Do not use sharp 0px to 4px corners on cards or buttons.
- Do not use cool blue or neutral gray shadows.
- Do not use pure black for text.
- Do not rely on stock photography for hero visuals.
