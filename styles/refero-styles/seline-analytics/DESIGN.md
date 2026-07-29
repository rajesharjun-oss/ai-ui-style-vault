# Seline Analytics - Style Reference

> Quiet analyst's desk on warm paper

**Theme:** light

Seline Analytics is a calm editorial analytics system. It sits on a warm stone canvas, uses flat white cards and 1px stone borders as structure, and reserves vivid cyan for primary action, links, and a single highlighted phrase. The design avoids typical loud SaaS treatment: no gradients, no heavy color washes, no overexcited typography.

The signature is restraint. Roobert-style headings stay weight 400 with tight negative tracking. Inter handles body, navigation, captions, and dense UI. Most cards are flat and border-led; only the hero dashboard preview gets the deeper 45px shadow.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Stone Canvas | `#fafaf9` | `--color-stone-canvas` | Warm off-white page background that reads as paper. |
| Pure White | `#ffffff` | `--color-pure-white` | Card surfaces, elevated panels, nav, and input fills. |
| Stone Border | `#e8e6e5` | `--color-stone-border` | Hairline borders on cards, nav, and inputs. |
| Stone Muted | `#d6d3d1` | `--color-stone-muted` | Secondary borders, subtle tints, and decorative separators. |
| Ash Gray | `#a8a29e` | `--color-ash-gray` | Helper text, icon strokes, and disabled states. |
| Warm Gray | `#78716c` | `--color-warm-gray` | Body text, nav links, and secondary copy. |
| Ink Black | `#0c0a09` | `--color-ink-black` | Primary headings, emphasized body, and strong icons. |
| Soot | `#1c1917` | `--color-soot` | Dark tab pills and sparing inverted surfaces. |
| Sky Wash | `#c1e1f7` | `--color-sky-wash` | Soft wash behind highlighted text spans. |
| Cyan Signal | `#3ba6f1` | `--color-cyan-signal` | Primary CTA fill, active links, and brand icon strokes. |
| Cyan Edge | `#3398e1` | `--color-cyan-edge` | Outlined action border, linked labels, and lightweight interactive emphasis. |

## Tokens - Typography

### Roobert

- **Token:** `--font-roobert`
- **Substitute:** Inter Tight or Satoshi
- **Weights:** 400, 500
- **Sizes:** 18px, 20px, 32px, 52px
- **Line heights:** 1.12, 1.22, 1.25, 1.69
- **Letter spacing:** -0.025em at 32px, -0.021em at 52px, -0.017em at 18px
- **Role:** Display and heading typeface. Weight 400 at 52px is the signature.

### Inter

- **Token:** `--font-inter`
- **Substitute:** Inter
- **Weights:** 400, 500, 600
- **Sizes:** 10px, 12px, 13px, 14px, 15px, 16px, 18px
- **Line heights:** 1.33, 1.53, 1.64, 1.69, 2.3
- **Letter spacing:** 0.003em, 0.004em, 0.025em
- **Role:** Body, nav, UI, captions, and dense dashboard labels.

### Type Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| caption | 10px | 2.3 | 400 | 0 | `--text-caption` |
| body-sm | 14px | 1.64 | 400 | 0.056px | `--text-body-sm` |
| body-lg | 16px | 1.69 | 400 | 0.048px | `--text-body-lg` |
| subheading | 20px | 1.2 | 400 | -0.1px | `--text-subheading` |
| heading-sm | 32px | 1.25 | 400 | -0.8px | `--text-heading-sm` |
| display | 52px | 1.12 | 400 | -1.092px | `--text-display` |

## Tokens - Spacing And Shapes

**Base unit:** 4px

**Density:** compact

| Purpose | Value |
|---------|-------|
| Page max width | 1200px |
| Section gap | 96px |
| Card padding | 24px |
| Element gap | 8px |

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 4 | 4px | `--spacing-4` |
| 8 | 8px | `--spacing-8` |
| 12 | 12px | `--spacing-12` |
| 16 | 16px | `--spacing-16` |
| 24 | 24px | `--spacing-24` |
| 32 | 32px | `--spacing-32` |
| 40 | 40px | `--spacing-40` |
| 48 | 48px | `--spacing-48` |
| 64 | 64px | `--spacing-64` |
| 80 | 80px | `--spacing-80` |
| 96 | 96px | `--spacing-96` |
| 160 | 160px | `--spacing-160` |

### Radius

| Element | Value | Token |
|---------|-------|-------|
| tags | 9999px | `--radius-tags` |
| cards | 10px | `--radius-cards` |
| icons | 4px | `--radius-icons` |
| inputs | 6px | `--radius-inputs` |
| buttons | 9999px | `--radius-buttons` |
| feature-card | 16px | `--radius-feature-card` |

### Shadows

| Name | Value | Token |
|------|-------|-------|
| md | `rgba(0, 0, 0, 0.05) 0px 4px 16px 0px` | `--shadow-md` |
| sm | `rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px` | `--shadow-sm` |
| subtle | `rgba(0, 0, 0, 0.05) 0px 1px 2px 0px` | `--shadow-subtle` |
| xl | `rgba(17, 12, 46, 0.12) 0px 12px 45px 0px` | `--shadow-xl` |

## Components

### Primary CTA Button

Pill shape, Cyan Signal fill, Cyan Edge 1px border, Pure White text, Inter 500, 8px vertical and 16px horizontal padding. Use once per viewport maximum.

### Secondary Ghost Button

Pill shape, transparent fill, 1px Stone Border, Ink Black text, Inter 400, 8px vertical and 16px horizontal padding. Use beside the primary CTA.

### Navigation Link

No fill, no border, 14px Inter weight 400, Warm Gray text, 0 12px padding, 32px height. Hover shifts to Ink Black.

### Signed-In Avatar Link

Stack of four overlapping 24px circular avatars with 2px ring offset and -8px overlap spacing. Use as proof-of-community in nav.

### Flat Content Card

Pure White fill, 10px radius, 1px Stone Border, 24px padding, and optional subtle md shadow. The border is the primary structure.

### Floating Dashboard Preview

Pure White surface, 16px radius, 8px internal padding, and `--shadow-xl`. Apply grayscale and slightly lowered contrast to dashboard imagery.

### Highlighted Text Span

Cyan Edge text with Sky Wash pill-shaped background. Use one highlighted phrase per headline maximum.

### Text Input

Pure White fill, 6px radius, 1px Stone Muted border, Warm Gray placeholder, 4px vertical and 12px horizontal padding. Focus ring uses Cyan Signal.

### Mascot Sticker Illustration

Grayscale line-art mascot sticker with small drop-shadow. Use once per section as a personality beat, not as repeated decoration.

### Logo Wordmark

Small black spark/flame glyph plus Seline wordmark in Inter 500 at 14px, Ink Black.

### Star Rating Display

Five small star glyphs in Ink Black or Warm Gray, inline with platform label in 14px Inter Warm Gray. No card chrome.

### Testimonial Card

No card chrome. Star row, 16px quote in Ink Black with optional cyan highlight, 32px avatar, name in 14px/500, role in Warm Gray.

### Tab Pill Group

Horizontal pill tabs below dashboard preview. Active: Soot fill, white text, full radius. Inactive: transparent, Ink Black text, Stone Border outline.

## Do's And Don'ts

### Do

- Use Roobert-style headings at weight 400.
- Use Stone Canvas as the page background and Pure White for cards.
- Use exactly one cyan highlight span per headline.
- Use 1px Stone Border as the structural device inside cards.
- Keep buttons pill-shaped with 8px by 16px padding.
- Set dominant body copy at 14px Inter weight 400 with 1.64 line-height.
- Use mascot stickers sparingly, about once per section.

### Don't

- Do not introduce new accent colors.
- Do not use heavy shadows on content cards.
- Do not set headlines in Inter.
- Do not use Pure White as the page background.
- Do not fill primary buttons with dark or neutral colors.
- Do not add gradients, glassmorphism, or decorative color washes.
- Do not stack multiple cyan highlight spans in one headline.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#fafaf9` | Full-page warm-stone background. |
| 1 | Card | `#ffffff` | Flat cards, nav, and input fills. |
| 2 | Floating Preview | `#ffffff` | Hero dashboard screenshot with deeper shadow. |
| 3 | Inverted Section | `#1c1917` | Dark tab pills and sparing inverted panels. |

## Imagery

Use product UI screenshots as the main imagery. The dashboard preview behaves like the hero object and should be muted with grayscale and contrast reduction. Avoid lifestyle photography, team shots, and environment imagery. Decorative icons should be 1px-outline style in Ink Black or Cyan Signal.

## Layout

Use a centered 1200px max-width page with 96px section gaps. The hero is left-aligned text with one cyan-highlighted phrase, dual pill CTAs, partner logos, a trust/rating line, and then a full-width floating dashboard preview that overlaps the next section. Below, use testimonials and feature sections with calm spacing and centered product visuals.

## Agent Prompt Guide

### Quick Color Reference

- Page background: `#fafaf9`
- Card surface: `#ffffff`
- Primary text: `#0c0a09`
- Secondary text: `#78716c`
- Border: `#e8e6e5`
- Accent: `#3ba6f1`
- Highlight wash: `#c1e1f7`

### Example Component Prompts

1. Hero: warm Stone Canvas, Roobert-style 52px heading, one Sky Wash/Cyan Edge highlighted phrase, 14px Inter body, cyan pill CTA, ghost pill CTA, and floating dashboard preview.
2. Flat card: Pure White fill, 10px radius, 1px Stone Border, 24px padding, light md shadow only if needed.
3. Dashboard preview: 16px radius, Pure White frame, 8px inner padding, shadow-xl, grayscale dashboard screenshot.
4. Tab group: pill tabs, active Soot fill with white text, inactive transparent with Stone Border.
5. Testimonial: no card chrome, star row, quote text, small avatar, name and role.

## Similar Reference Families

- Plausible Analytics style calm privacy-first analytics.
- Linear style quiet product proof with precise borders.
- PostHog style personality through mascot, with far less color.
- Fathom Analytics style simple and warm analytics pages.

