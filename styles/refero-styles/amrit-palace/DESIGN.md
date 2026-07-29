# Amrit Palace Style Reference

Amrit Palace treats the page as a curated restaurant spread: a warm parchment canvas, dark candlelit photography, sharp card geometry, editorial hairlines, and serif headlines that whisper at extreme sizes. Saffron is the only chromatic note, used like spice rather than paint.

## Theme

Light, restaurant, editorial, fine dining, parchment, warm, sharp, atmospheric.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Parchment | `#d8cbb8` | `--color-parchment` | Page canvas and primary card surfaces. |
| Linen | `#bfb4a3` | `--color-linen` | Secondary section tone and subtle surface layering. |
| Warm Stone | `#b6ab9c` | `--color-warm-stone` | Hairline borders and 1px section dividers. |
| Walnut | `#978e81` | `--color-walnut` | Muted helper text, captions, and metadata. |
| Espresso | `#615b53` | `--color-espresso` | Secondary body text and subhead copy. |
| Onyx Warm | `#2c2c2c` | `--color-onyx-warm` | Primary text, navigation, headings, and dark fills. |
| Midnight Roast | `#292622` | `--color-midnight-roast` | Deep dark overlay for hero and atmospheric photography. |
| Saffron Glow | `#d49653` | `--color-saffron-glow` | Sole chromatic accent for stars, active states, featured tags, and decorative punctuation. |

## Typography

### TT Ramillas Variable

Use for all display and section headings.

- Token: `--font-tt-ramillas-variable`
- Fallback: Cormorant Garamond, Playfair Display, DM Serif Display
- Weight: 300
- Sizes: 22px, 26px, 50px, 65px, 69px, 115px
- Line height: 0.80 to 1.20
- Letter spacing: very tight at large sizes, from -0.04em to -0.03em
- Role: whisper-weight uppercase editorial luxury.

### Satoshi

Use for navigation, buttons, body, labels, and structural UI.

- Token: `--font-satoshi`
- Fallback: Inter, DM Sans, Manrope
- Weights: 500, 700
- Sizes: 12px, 13px, 14px, 15px, 42px, 199px
- Role: confident geometric counterpoint to the airy serif.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 13px | 1.30 | -0.143px | `--text-caption` |
| Body | 15px | 1.40 | -0.15px | `--text-body` |
| Body LG | 26px | 1.20 | -0.156px | `--text-body-lg` |
| Subheading | 42px | 1.00 | -1.68px | `--text-subheading` |
| Heading SM | 50px | 0.90 | -1.5px | `--text-heading-sm` |
| Heading | 65px | 0.85 | -2.6px | `--text-heading` |
| Heading LG | 69px | 0.90 | -2.76px | `--text-heading-lg` |
| Display | 115px | 0.80 | -4.6px | `--text-display` |

## Spacing And Shape

- Density: compact.
- Max width: 1440px.
- Section gap: 120px to 160px.
- Card padding: 28px.
- Element gap: 12px to 16px.

### Spacing Scale

`4, 5, 6, 7, 8, 10, 12, 16, 17, 20, 24, 28, 32, 42, 92, 206`

### Radius Scale

| Element | Radius |
|---|---:|
| Cards | 0px |
| Sections | 0px |
| Image containers | 0px |
| Tags | 3px |
| Inputs | 3px |
| Buttons | 3px |

## Components

### Ghost Outlined Button

Transparent background, 1px border in Parchment on dark or Onyx Warm on light, uppercase Satoshi 14px/500, 3px radius, generous padding around 20px. No shadow and no filled color.

### Text Link Button

Text-only Satoshi 13px to 15px/500 uppercase. No background and no border. Use underline on hover. Color follows context: Parchment on dark overlays and Onyx Warm on parchment.

### Hero Wordmark Display

Satoshi 199px/500, uppercase, line-height 0.8, tight tracking, Parchment text over dark photographic overlay.

### Editorial Section Heading

TT Ramillas Variable 50px to 115px, weight 300, uppercase, line-height 0.8 to 0.9, tight tracking. Use Onyx Warm on parchment and Parchment on dark photography.

### Testimonial Card

Parchment background, same as canvas, 0px radius, no shadow, no border. Use Saffron 5-star row, Satoshi 14px body in Onyx Warm, source label top-right, author name in Walnut.

### Image Overlay Container

Full-viewport restaurant photograph with a dark Midnight Roast overlay. Text sits top-left or centered in Parchment. Use for hero and atmospheric transitions.

### Star Rating Display

Five Saffron stars, score in Satoshi 700, small source text in Satoshi 500. Can sit as a floating widget over photo or parchment.

### Menu Item Card

Transparent container, no border, no radius, food image plus dish name and description. Use internal 16px spacing, not card chrome.

### Navigation Bar

Transparent over hero. Logo left, nav links in Satoshi 14px uppercase, context-colored text, action links and square 3px icon buttons on the right. No background bar.

### Section Divider Rule

1px Warm Stone line across the section. Treat it as an editorial column rule.

### Caption Label

Satoshi 12px to 13px/500 uppercase, tight negative tracking, Walnut on parchment or Parchment on dark.

## Layout

Use full-bleed sections rather than a rigid centered app frame. Hero and atmospheric sections use dark full-bleed photography with overlaid type. Content-heavy sections unfold on the Parchment canvas with left-aligned editorial rhythm, 120px to 160px section gaps, horizontal testimonial rows, menu item spreads, and full-width divider rules.

## Motion

Motion should be minimal. Use 0.4s hover transitions with organic ease. The marquee animation is the one expressive motion and should be reserved for signature dish scrolling.

## Imagery

Use full-bleed, dark, warm restaurant interiors with candlelight, place settings, shallow depth of field, and food in sharp focus. Food photography should feel editorial and still-life, not stock. Avoid people shots, lifestyle images, abstract graphics, and CSS gradient atmospherics.

## Do

- Use TT Ramillas Variable at weight 300 for section headings.
- Use uppercase tight tracking on headings 50px and above.
- Use Saffron Glow only 2-3 times per fold.
- Keep cards, sections, and images at 0px radius.
- Use 3px radius only for buttons, tags, and controls.
- Use Warm Stone 1px dividers as editorial rules.
- Lead with dark full-bleed photography, then shift into parchment content.
- Keep body copy at 13px to 16px Satoshi.

## Don't

- Do not round card corners.
- Do not add shadows or elevation.
- Do not introduce a second chromatic accent.
- Do not center body paragraphs.
- Do not use filled chromatic buttons.
- Do not use pure black for text.
- Do not add gradients; atmosphere comes from photography.
- Do not bold the TT Ramillas serif headings.
