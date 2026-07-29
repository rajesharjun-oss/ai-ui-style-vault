# Hyperstudio - Style Reference

> Obsidian editorial-tech studio

**Theme:** dark

Hyperstudio is a dark editorial-tech system built from near-black surfaces, sharp grid panels, white alpha hairlines, and restrained monochrome typography. The page feels like a technical studio operating system: sober, precise, spacious, and text-led.

The palette is almost entirely black and white. Compass Gold appears only in icon strokes and subtle intelligence marks. Pulse Green appears as a tiny status signal, not as a broad brand color. Interaction uses white pill CTAs and transparent nav links, while content panels remain square-edged and flat.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Obsidian | `#03050c` | `--color-obsidian` | Primary page background and deepest surface layer. |
| Deep Navy | `#060918` | `--color-deep-navy` | Slightly cooler dark surface for section depth. |
| Steel Ink | `#0b0b0b` | `--color-steel-ink` | Alternative black panel surface and footer base. |
| Paper | `#ffffff` | `--color-paper` | Primary text, CTA fill, and high-contrast strokes. |
| Muted White | `#ffffffb3` | `--color-muted-white` | Secondary text and softer paragraph copy. |
| Soft White | `#ffffff99` | `--color-soft-white` | Tertiary copy, footer links, and inactive nav. |
| Faint Line | `#ffffff2b` | `--color-faint-line` | Hairline borders and grid panel dividers. |
| Translucent White | `#ffffff40` | `--color-translucent-white` | Subtle separators and hover/focus borders. |
| Compass Gold | `#b49c46` | `--color-compass-gold` | Compass icon strokes, small AI marks, and restrained illustrative details. |
| Pulse Green | `#98ff38` | `--color-pulse-green` | Tiny status dots and live/available signals only. |

## Tokens - Typography

### Aeonik

- **Token:** `--font-aeonik`
- **Substitute:** Inter, Neue Haas Grotesk, Satoshi, ui-sans-serif
- **Weights:** 400, 500
- **Sizes:** 12, 14, 16, 18, 20, 24, 30, 32, 38, 46, 50, 67px
- **Line heights:** 1.01, 1.03, 1.07, 1.13, 1.17, 1.20, 1.25, 1.33, 1.42, 1.50
- **Letter spacing:** -0.0200em for headings and -0.0100em for body
- **Role:** Sole UI and editorial typeface. Use weight 400 for headings and body; weight 500 only for CTAs, nav emphasis, and form labels.

### Type Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| caption | 12px | 1.5 | 500 | -0.12px | `--text-caption` |
| body-sm | 14px | 1.42 | 400 | -0.14px | `--text-body-sm` |
| body | 16px | 1.25 | 400 | -0.16px | `--text-body` |
| subheading | 18px | 1.33 | 400 | -0.18px | `--text-subheading` |
| heading-sm | 24px | 1.25 | 400 | -0.48px | `--text-heading-sm` |
| heading | 30px | 1.07 | 400 | -0.6px | `--text-heading` |
| heading-lg | 38px | 1.03 | 400 | -0.76px | `--text-heading-lg` |
| display | 67px | 1.01 | 400 | -1.34px | `--text-display` |

## Tokens - Spacing And Shapes

**Base unit:** 4px

**Density:** compact

| Purpose | Value |
|---------|-------|
| Max width | 1200px |
| Section gap | 96px |
| Card padding | 24px |
| Element gap | 8px |
| Hero vertical padding | 144px |
| Grid panel padding | 36-48px |

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 4 | 4px | `--spacing-4` |
| 8 | 8px | `--spacing-8` |
| 12 | 12px | `--spacing-12` |
| 16 | 16px | `--spacing-16` |
| 18 | 18px | `--spacing-18` |
| 24 | 24px | `--spacing-24` |
| 36 | 36px | `--spacing-36` |
| 40 | 40px | `--spacing-40` |
| 48 | 48px | `--spacing-48` |
| 64 | 64px | `--spacing-64` |
| 96 | 96px | `--spacing-96` |
| 144 | 144px | `--spacing-144` |

### Radius

| Element | Value | Token |
|---------|-------|-------|
| cards | 0px | `--radius-cards` |
| grid-panels | 0px | `--radius-grid-panels` |
| nav-items | 8px | `--radius-nav-items` |
| buttons | 9999px | `--radius-buttons` |

## Components

### Primary Pill CTA

Paper fill, Obsidian text, Aeonik 14px weight 500, 9999px radius, compact 10px by 18px padding, no shadow. This is the only filled button language.

### Ghost Nav Link

Transparent background, Paper or Soft White text, Aeonik 14px, no underline, subtle opacity change on hover. Use for header nav and footer links.

### Hero Headline

Aeonik 67px, weight 400, Paper, line-height 1.01, letter-spacing -1.34px. Keep it direct, editorial, and unadorned.

### Bordered Grid Card

Transparent or Deep Navy fill, 0px radius, 1px Faint Line border, 36-48px padding, no shadow. Used for service blocks, feature panels, and structured content.

### Email Input

Transparent or Steel Ink background, Paper text, 1px Faint Line border, 9999px radius when paired with a pill submit button, 14px text, 12px by 18px padding.

### Signal Dot

Tiny 6-8px Pulse Green circle, no label required only when context is obvious. Use for live/available/active states.

### Service Accordion Item

Full-width row with 1px Faint Line divider, Aeonik 24-30px label, muted body preview, plus icon or arrow on the right. No card rounding.

### Partner Logo Wordmark

Single-color Paper or Muted White wordmark, no container, no card. Keep logos in rows with generous gaps.

### Arrow Icon Button

Circular or pill touch target with Paper stroke arrow, transparent fill, Faint Line border. Use for carousel or next-step navigation.

### Footer Pill

Paper or transparent pill, 9999px radius, small Aeonik 12-14px label. Use for contact/status actions.

### Section Eyebrow

Aeonik 12px weight 500, uppercase or compact sentence case, Muted White, optional Compass Gold icon mark.

### Vertical Divider

1px Faint Line, full-height or section-height. Use to create editorial grid rhythm.

## Do's And Don'ts

### Do

- Use near-black backgrounds and white alpha borders.
- Keep cards and grid panels square-edged.
- Use pill radius only for buttons and inputs.
- Use Compass Gold only for icons and tiny marks.
- Use Pulse Green only for status dots.
- Keep typography weight mostly 400.
- Separate sections with hairline borders and grid lines, not shadows.
- Use large text blocks and quiet service grids.

### Don't

- Do not add gradients, glow effects, glassmorphism, or colored light blobs.
- Do not round cards.
- Do not use gold as a CTA fill.
- Do not turn green into a broad accent color.
- Do not introduce extra accent colors.
- Do not make the layout image-heavy.
- Do not use thick borders or heavy drop shadows.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Obsidian Canvas | `#03050c` | Primary page background. |
| 1 | Deep Navy Band | `#060918` | Section depth and secondary dark surfaces. |
| 2 | Steel Ink Panel | `#0b0b0b` | Dark card, input, and footer surfaces. |
| 3 | Faint Grid | `#ffffff2b` | Hairline dividers and panel borders. |

## Elevation

No shadows. Depth is created through hairline grids, dark surface shifts, and typography scale.

## Imagery

Use abstract technical motifs, thin-line icons, compass marks, partner wordmarks, and occasional schematic-style UI fragments. Avoid stock photography, large screenshots, decorative gradients, and illustrative blobs.

## Layout

Use a centered 1200px content track inside full-width dark sections. The hero is text-led with a compact pill CTA and optional small status signal. Follow with bordered service grids, partner wordmark rows, and editorial blocks separated by vertical and horizontal Faint Line dividers.

## Agent Prompt Guide

### Quick Color Reference

- Background: `#03050c`
- Secondary background: `#060918`
- Panel: `#0b0b0b`
- Text: `#ffffff`
- Muted text: `#ffffffb3`
- Border: `#ffffff2b`
- Icon accent: `#b49c46`
- Status dot: `#98ff38`

### Example Component Prompts

1. Hero: Obsidian background, 67px Aeonik-style white headline, muted supporting copy, white pill CTA, and tiny Pulse Green availability dot.
2. Service grid: 3-column square panels, 1px Faint Line borders, 0px radius, 36-48px padding, white headings, muted body.
3. Header: transparent dark header, left wordmark, ghost nav links, white pill CTA on the right.
4. Accordion: full-width rows with hairline dividers, 30px labels, muted descriptions, and a right arrow.
5. Partner strip: monochrome wordmarks in muted white, no containers, no logos in cards.

## Similar Reference Families

- Linear dark-mode restraint with sharper editorial panels.
- Resend dark minimal landing pages with monoline icon logic.
- Pentagram/agency editorial grids adapted to tech services.
- Vercel-style black canvas, simplified and more studio-like.

