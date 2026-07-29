# Dash Digital Studio - Style Reference

> Editorial museum on warm paper. A gallery where giant whisper-weight typography floats over off-white walls and full-bleed product photography does the talking.

**Theme:** light

Dash Digital Studio is a strictly achromatic editorial system. It uses warm off-white canvases, near-black type, and no chromatic accent. Every visual signal comes from type scale, weight, spacing, hairline structure, and tonal shifts between Bone, Linen, Parchment, and Carbon Black.

The brand feeling is architectural and gallery-like. Display type is giant, uppercase, tightly tracked, and compressed. Work is presented in a 2-up product-photography grid with almost no UI decoration. Actions are small solid dark pills. Cards and images stay square-edged, flat, and shadowless.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Carbon Black | `#2a2a2a` | `--color-carbon-black` | Primary text, nav links, body copy, badge text, footer copy, and structural borders. |
| Bone | `#f0f0f0` | `--color-bone` | Default page canvas and primary surface. |
| Ink | `#000000` | `--color-ink` | Maximum-contrast emphasis and hard borders. |
| Linen | `#fafafa` | `--color-linen` | Slightly elevated sheet surface and subtle section separation. |
| Ash | `#d6d6d6` | `--color-ash` | Muted fills, hairline borders, disabled and inactive surfaces. |
| Parchment | `#f0edea` | `--color-parchment` | Alternate warm section band. |
| Stone | `#bcbcb4` | `--color-stone` | Deep low-emphasis gray for dim supporting details. |
| Clay | `#ccc4b9` | `--color-clay` | Warm mid-gray transition between Bone and Parchment. |

## Tokens - Typography

### Founders Grotesk

- **Token:** `--font-founders-grotesk`
- **Substitute:** Sohne, Inter, GT America, Neue Haas Grotesk
- **Weights:** 300, 400
- **Sizes:** 12, 14, 16, 17, 22, 40, 70, 101
- **Line height:** 0.80-1.20
- **Letter spacing:** -0.0600em at 101px, -0.0300em at 70px, -0.0230em at 40px, -0.0200em at 22px, -0.0180em at 12-17px
- **OpenType features:** `"ss01" on, "ss02" on, "tnum" on`
- **Role:** Sole brand grotesque. Weight 300 is for display sizes 40px and above. Weight 400 is for body, navigation, labels, meta, and project descriptions.

### Editorial Neue

- **Token:** `--font-editorial-neue`
- **Substitute:** Tiempos Text, Lyon Display, Source Serif Pro
- **Weights:** 400
- **Sizes:** 16
- **Line height:** 0.90
- **Letter spacing:** -0.0600em
- **Role:** Sparse editorial serif counterpoint for rare pull-text or body-accent moments.

### Type Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| caption | 12px | 1.17 | 400 | -0.018px | `--text-caption` |
| body-sm | 14px | 1.2 | 400 | -0.018px | `--text-body-sm` |
| body | 16px | 1 | 400 | -0.018px | `--text-body` |
| body-lg | 17px | 1.2 | 400 | -0.018px | `--text-body-lg` |
| subheading | 22px | 1.17 | 400 | -0.02px | `--text-subheading` |
| heading-sm | 40px | 0.9 | 300 | -0.023px | `--text-heading-sm` |
| display | 70px | 0.88 | 300 | -0.03px | `--text-display` |
| display-xl | 101px | 0.8 | 300 | -0.06px | `--text-display-xl` |

## Tokens - Spacing And Shapes

**Base unit:** 4px

**Density:** comfortable

| Purpose | Value |
|---------|-------|
| Max width | 1440px |
| Section gap | 80-120px |
| Major section gap | 115px |
| Card padding | 20-24px |
| Element gap | 12-20px |
| Nav row padding / case-study column gap | 29px |
| Meta-to-title gap | 20px |

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 4 | 4px | `--spacing-4` |
| 12 | 12px | `--spacing-12` |
| 20 | 20px | `--spacing-20` |
| 24 | 24px | `--spacing-24` |
| 29 | 29px | `--spacing-29` |
| 32 | 32px | `--spacing-32` |
| 80 | 80px | `--spacing-80` |
| 115 | 115px | `--spacing-115` |
| 120 | 120px | `--spacing-120` |

### Radius

| Element | Value | Token |
|---------|-------|-------|
| cards | 0px | `--radius-cards` |
| images | 0px | `--radius-images` |
| inputs | 4px | `--radius-inputs` |
| tags | 999px | `--radius-tags` |
| buttons | 999px | `--radius-buttons` |

## Components

### Pill Action Button

Solid Carbon Black background, Linen text, Founders Grotesk 400 at 12px, uppercase label, 999px radius, about 14px horizontal padding and 4px vertical padding. No border, no shadow, no color accent.

### Text Nav Link

Founders Grotesk 400 at 12-14px, uppercase, Carbon Black. No underline, no fill, no border. Hover can shift to Ink. Separate nav items with about 29px horizontal spacing.

### Brand Mark Wordmark

Text-only wordmark in Founders Grotesk 400 at 12-14px. Use Carbon Black. If a legal mark is needed, render it as plain text such as `(R)` or through the actual brand asset only when licensed.

### Editorial Display Heading

Founders Grotesk 300 at 70-101px, uppercase, Carbon Black, line-height 0.80-0.88, letter-spacing -0.0300em to -0.0600em. Set across wide content width and avoid ornamental supporting visuals.

### Case Study Card

Two-up grid tile. Top block contains uppercase meta tags at 12px, then a 20px gap, then a 22px uppercase project title. The image below is full-bleed, product-focused, 0px radius, no border, no shadow.

### Meta Tag Row

Uppercase 12px Founders Grotesk, Carbon Black. Join multiple disciplines with slash, plus, or text separators. No background or border.

### Brand List Row

Full-width row with a 1px Carbon Black bottom border. Left side is the brand name, right side is service tags and a `MORE +` pill. No alternating fills.

### Project Image Frame

Raw rectangular product photography holder with 0px radius, no border, no overlay, and no shadow. The photograph is the visual content.

### Section Divider Rule

1px solid Carbon Black or Ink. Use sparingly. Prefer 80-120px whitespace for most section separation.

### Footer Wordmark

Minimal text signature at 12-14px with a hairline rule above. No social icon cluster and no repeated heavy navigation.

### Text Input

1px Carbon Black border, 4px corner radius, no fill, Founders Grotesk 400 at 16px. Focus can shift to Ink border; avoid colored rings.

## Do's And Don'ts

### Do

- Set hero and section titles in Founders Grotesk 300 at 70-101px.
- Use 0.80-0.88 line-height and tight negative tracking for display type.
- Use only Carbon Black for running text and Bone for the main background.
- Use 999px radius only for pill buttons and tags.
- Keep images, cards, and content blocks at 0px radius.
- Separate sections with 80-120px vertical gaps.
- Use 29px as a key spacing value for nav rhythm and case-study grid gaps.
- Render action labels in uppercase 12px text inside solid dark pills.
- Place discipline tags above project titles with about 20px of vertical space.

### Don't

- Do not introduce chromatic color.
- Do not use weight 300 for body text.
- Do not apply drop shadows, glows, gradients, or soft depth effects.
- Do not round image corners.
- Do not use line-height above 1.20.
- Do not underline text links.
- Do not use colored CTA buttons.
- Do not add decorative icons or illustrations.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Bone Canvas | `#f0f0f0` | Default page background. |
| 1 | Linen Sheet | `#fafafa` | Elevated sheet and section surface. |
| 2 | Parchment Block | `#f0edea` | Alternate warm section band. |
| 3 | Ash Mat | `#d6d6d6` | Muted inactive or disabled fill. |

## Elevation

The system is deliberately shadowless. Surface separation comes from tonal shifts between Bone, Linen, and Parchment plus occasional 1px hairline borders.

## Imagery

Full-bleed product photography is the only imagery. Avoid illustration, icons, decorative graphics, overlays, duotone treatment, rounded image masks, or lifestyle photography. Use tight editorial-grade product crops and let the work itself carry the visual energy.

## Layout

Use a full-bleed light page with a centered max-width content track around 1440px. The hero is a typographic block: massive uppercase headline, small uppercase tag line, and no hero image. Below, use a 2-up case study grid with large product photographs and meta/title blocks. Later sections can use client rows, brand lists, and sparse hairline rules.

## Agent Prompt Guide

### Quick Color Reference

- Text: `#2a2a2a`
- Background: `#f0f0f0`
- Surface: `#fafafa`
- Border: `#2a2a2a`
- Accent: none
- Primary action: dark monochrome pill

### Example Component Prompts

1. Case study card: 2-up grid, 29px gap, uppercase meta row at 12px, 20px gap, 22px uppercase title, full-bleed 0px-radius product photo, no border, no shadow, dark pill action.
2. Editorial hero: full-width Bone background, 101px uppercase Founders Grotesk style headline at weight 300, line-height 0.80, tracking -0.0600em, no hero image.
3. Brand list row: full-width row with 1px Carbon Black bottom border, uppercase brand left, service tags and `MORE +` pill right.
4. Top nav: text-only wordmark left, uppercase links right, 12-14px type, 29px spacing, no underline, no background.
5. Section divider: 1px solid Carbon Black, used sparingly after major content bands.

## Similar Reference Families

- Locomotive style monochrome editorial agency systems.
- Pentagram style grid-based case study presentation.
- Manual style off-white canvas and hairline rule discipline.
- Resn style gallery-like work presentation with minimal UI chrome.

