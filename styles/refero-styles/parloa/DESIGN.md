# Parloa Style Reference

Parloa is a warm editorial product system. It pairs a cream paper canvas with ink-black UI structure, thin serif display headings, exact grotesque interface text, flat white cards, and a highlighter-orange accent that marks rather than fills. The feeling should be confident, human, and print-inspired.

## Theme

Light, warm editorial, AI SaaS, paper, serif display, dark nav, flat cards, highlighter accent, photography-led.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Ink Black | `#1f1c1b` | `--color-ink-black` | Primary text, filled buttons, dark navigation, and dark surfaces. |
| Paper White | `#ffffff` | `--color-paper-white` | Card surfaces and white text on dark fills. |
| Canvas Cream | `#ebe9e1` | `--color-canvas-cream` | Main page background and warm paper field. |
| Linen | `#f5f4f0` | `--color-linen` | Navigation fill, subtle bands, and lighter cream layers. |
| Stone | `#a69b92` | `--color-stone` | Muted text, secondary copy, input borders, and understated labels. |
| Hairline | `#d9d6ce` | `--color-hairline` | Card borders, link underlines, and subtle dividers. |
| Espresso | `#2d2724` | `--color-espresso` | Announcement bar, dark surface accents, and input fills. |
| Charcoal | `#000000` | `--color-charcoal` | SVG icon fills only when absolute black is required. |
| Cobblestone | `#c7c1b7` | `--color-cobblestone` | Secondary dividers and borders with slightly more presence. |
| Highlighter Orange | `#ff7714` | `--color-highlighter-orange` | Links, outlines, icon strokes, small dots, and decorative marks only. |

## Typography

### Exposure30

Use for display headings only.

- Token: `--font-exposure30`
- Fallback: Fraunces, Playfair Display, DM Serif Display
- Weights: 350, 400
- Sizes: 24px, 28px, 42px, 82px, 96px
- Line height: 1.00 to 1.30
- Letter spacing: -0.01em at display sizes, 0.01em at 24px to 28px
- Role: thin editorial authority for large headlines.

### Geist

Use for body text, UI, nav, buttons, labels, metadata, and forms.

- Token: `--font-geist`
- Fallback: Inter, Manrope, system-ui
- Weights: 300, 400, 500, 600
- Sizes: 10px, 11px, 13px, 14px, 16px, 18px
- Line height: 1.20 to 1.50
- Letter spacing: 0.01em at 14px to 16px, 0.02em at 10px to 11px
- Role: precise workhorse grotesque for every non-heading element.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 10px | 1.20 | 0.2px | `--text-caption` |
| Body | 16px | 1.50 | 0.16px | `--text-body` |
| Subheading | 18px | 1.40 | 0.18px | `--text-subheading` |
| Heading SM | 24px | 1.30 | 0.24px | `--text-heading-sm` |
| Heading | 42px | 1.10 | -0.42px | `--text-heading` |
| Heading LG | 82px | 1.05 | -0.82px | `--text-heading-lg` |
| Display | 96px | 1.00 | -0.96px | `--text-display` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Max width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

### Spacing Scale

`4, 8, 12, 16, 20, 24, 32, 40, 48, 60, 64, 72`

### Radius Scale

| Element | Radius |
|---|---:|
| Cards | 0px |
| Tags | 2px |
| Inputs | 2px |
| Buttons | 2px |
| Maximum allowed | 4px |

## Components

### Top Announcement Bar

Espresso full-bleed bar, Geist 14px text, Highlighter Orange headline/link accents, white supporting copy, and compact 8px vertical padding.

### Primary Navigation

Dark full-width navigation using Ink Black or Espresso. Logo left, center nav links in white Geist 14px, and search/language/demo controls on the right. Keep the bar flat and compact.

### Hero With Image Overlay

Full-viewport warm-lit portrait photography with a diagonal gradient fade into Canvas Cream. Large Exposure30 82px to 96px headline sits over the bottom-left image area. No card around the text.

### Logo Trust Bar

Horizontal grayscale logo row on Canvas Cream. No card backgrounds. Keep it quiet and evenly spaced.

### Feature Split Section

Two-column editorial block. Left column uses Exposure30 42px heading, Geist body copy, and a dark CTA. Right column uses a Paper White card with Hairline border and product/abstract preview content.

### Industry Solution Card

Paper White surface, 0px radius, 1px Hairline border, 24px padding, outlined icon, Exposure30 24px heading, Geist 14px Stone body. Use a small orange dot or outlined mark only on the featured/first card.

### Primary CTA Button

Ink Black fill, Paper White text, Geist 14px/500, 12px vertical padding, 11px horizontal padding, 2px radius. No shadow or lift.

### Ghost Text Button

No background, Ink Black text, Geist 14px/400, 2px radius, minimal padding, often with an orange arrow or underline.

### Navigation CTA Button

Outlined white button on dark nav: 1px white border, white text, 2px radius, compact 8px by 12px padding.

### Outlined Accent Element

Highlighter Orange border or stroke, transparent fill, used for links, icon badges, accents, or callouts. Never filled.

### Section Heading

Exposure30 42px/400, Ink Black, line-height 1.10, slight negative tracking. Let the serif shape carry the drama without extra decoration.

### Product Preview Card

Paper White, 0px radius, 1px Hairline border, 24px padding. Use a small abstract/product graphic and Geist description text.

## Layout

Use max-width 1200px centered content, but keep the hero, announcement bar, and dark nav full-bleed. The hero is full height with warm photography and overlaid serif headline. Below it, alternate cream and white bands with 80px section gaps. Use two-column splits and horizontal 4-card rows. Keep density spacious and editorial.

## Imagery

Photography is the main asset. Use warm-lit human portraiture, close crops, natural expressions, and golden-hour tones. Blend hero images into the cream page with a diagonal gradient overlay. Avoid abstract hero graphics, 3D renders, generic corporate stock, multicolor icons, and cool-toned section backgrounds. Icons should be outlined strokes, mostly Ink Black or orange.

## Do

- Use Exposure30 weight 350 for display headings at 42px and above.
- Use Ink Black filled buttons for primary actions.
- Use Highlighter Orange only for outlines, links, icon strokes, and small marks.
- Layer Paper White cards on Canvas Cream with 1px Hairline borders.
- Keep body text in Geist 16px/400 with 1.50 line-height.
- Use 4px spacing rhythm with 16px element gaps and 24px card padding.
- Let warm photography carry the hero.

## Don't

- Do not use orange as a filled button or large background.
- Do not introduce box shadows or drop shadows.
- Do not use bold weights for serif headings.
- Do not use border-radius above 4px.
- Do not use pure black for body text or large surfaces.
- Do not add cool colored section backgrounds.
- Do not use orange for paragraph text.
