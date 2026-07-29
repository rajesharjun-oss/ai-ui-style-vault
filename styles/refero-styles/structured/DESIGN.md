# Structured - Style Reference

> Renaissance gallery on putty paper

**Theme:** mixed

Structured treats finance like a gallery exhibition: warm putty-beige canvas, stark black rooms, classical painting imagery, and a huge serif wordmark that behaves more like an artwork than a logo. The system uses Davinci-style serif type for emotional scale and Helvetica Now style grotesk for utility, stats, nav, and compact action labels.

The page has almost no saturated color. Drama comes from size, cropping, hard light/dark section cuts, circular image vignettes, hexagonal indicators, and the contrast between warm neutrals and ink black. Everything is flat. There are no shadows or gradients. The interface should feel like a Renaissance folio translated into a premium finance product.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Putty | `#c4c3b6` | `--color-putty` | Dominant warm gray-beige canvas for hero and most light sections. |
| Ink | `#000000` | `--color-ink` | Dark sections, borders, separators, text, and filled pill CTAs. |
| Bone | `#e7e5e4` | `--color-bone` | Elevated cards and secondary light surfaces. |
| Chalk | `#ebebeb` | `--color-chalk` | Footer and lightest surface tier. |
| Vellum | `#dfdcd5` | `--color-vellum` | Hairline borders and printed-page edge details. |
| Graphite | `#595855` | `--color-graphite` | Muted secondary text and subtle image backgrounds. |
| Ash | `#808080` | `--color-ash` | Cool gray for image placeholders and mid-neutral surfaces. |
| Paper | `#ffffff` | `--color-paper` | Reverse text on dark sections, white icon strokes, and rare accent fills. |

## Tokens - Typography

### Davinci

- **Token:** `--font-davinci`
- **Substitute:** Canela, Tiempos Headline, GT Super, Playfair Display
- **Weights:** 400, 500
- **Sizes:** 16, 24, 34, 52, 94, 374px
- **Line height:** 0.84, 1.00, 1.10, 1.33, 1.50
- **Letter spacing:** -0.0090em, -0.0050em, -0.0010em
- **Role:** Display and heading serif. It carries the 374px hero wordmark, 94px section titles, and 52px sub-headings.

### Helvetica Now

- **Token:** `--font-helvetica-now`
- **Substitute:** Inter, Neue Haas Grotesk, Sohne, Helvetica Neue
- **Weights:** 400, 500
- **Sizes:** 9, 12, 15, 16, 22, 24, 26, 43px
- **Line height:** 1.25, 1.50
- **Role:** Utility grotesk for body copy, nav labels, button text, stats, and caption micro-text.

### Type Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| micro | 9px | 1.25 | 400 | 0 | `--text-micro` |
| body-sm | 15px | 1.5 | 400 | 0 | `--text-body-sm` |
| body | 16px | 1.5 | 400 | 0 | `--text-body` |
| subheading | 22px | 1.33 | 400 | -0.11px | `--text-subheading` |
| heading-sm | 26px | 1.33 | 400 | -0.13px | `--text-heading-sm` |
| heading | 43px | 1.1 | 400 | -0.215px | `--text-heading` |
| heading-lg | 52px | 1 | 500 | -0.47px | `--text-heading-lg` |
| section-display | 94px | 0.84 | 500 | -0.85px | `--text-section-display` |
| display | 374px | 0.84 | 500 | -3.37px | `--text-display` |

## Tokens - Spacing And Shapes

**Base unit:** 4px

**Density:** compact

| Purpose | Value |
|---------|-------|
| Section gap | 80px |
| Card padding | 24px |
| Element gap | 6px |
| Feature column gap | 28px |
| Circular vignette diameter | 200px |
| Product card size | 400px |
| Header height | 40px |

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 4 | 4px | `--spacing-4` |
| 6 | 6px | `--spacing-6` |
| 16 | 16px | `--spacing-16` |
| 20 | 20px | `--spacing-20` |
| 28 | 28px | `--spacing-28` |
| 32 | 32px | `--spacing-32` |
| 36 | 36px | `--spacing-36` |
| 40 | 40px | `--spacing-40` |
| 52 | 52px | `--spacing-52` |
| 60 | 60px | `--spacing-60` |
| 80 | 80px | `--spacing-80` |
| 96 | 96px | `--spacing-96` |
| 168 | 168px | `--spacing-168` |

### Radius

| Element | Value | Token |
|---------|-------|-------|
| links | 2px | `--radius-links` |
| cards | 9px | `--radius-cards` |
| buttons | 28.8px | `--radius-buttons` |
| circles | 9999px | `--radius-circles` |

## Components

### Pill Action Button

Filled Ink pill with Paper text, Helvetica Now style 12px weight 400, 9px vertical and 17px horizontal padding, 28.8px radius, no border, no shadow. Use only one strong CTA per viewport.

### Ghost Text Link

Text-only link in Ink, Helvetica Now style 12-16px weight 400, no background, no border. Underline only on hover.

### Circular Feature Vignette

Circular crop of a classical painting, about 200px diameter, no border, no shadow. Pair with a Davinci-style 22-24px caption and a hexagonal indicator beneath.

### Notched Product Card

Dark card around 400px square with notched or hexagonal corner cuts, Ink background, Paper micro-label at 9px Helvetica Now style type, and no shadow. Use 9px primary edge radius before the notches.

### Hero Wordmark

Davinci-style serif at 374px, weight 500, Ink, -3.37px tracking, 0.84 line-height. It should extend beyond the visible viewport and crop at the edges.

### Stat Pair

Inline TVL/APY style data pairs in Helvetica Now style 16px weight 500, Ink, uppercase label/value format, with about 28px separation.

### Hexagonal Nav Indicator

Small 12px hexagonal outline shapes, transparent fill, Ink stroke on light sections or Paper stroke on dark sections. Use in groups of three beneath circular features.

### Logo Mark

Minimal circled S monogram, about 32px diameter, thin Ink stroke, transparent fill. Use as the only graphic mark in the header.

### Section Header

Davinci-style 94px weight 500, 0.84 line-height, centered, Ink on light or Paper on dark. Often paired with tiny uppercase section labels in the corners.

### Classical Painting Panel

Full-bleed Renaissance or Baroque painting reproduction, no border, no overlay, no radius, no crop container decoration. It functions as atmosphere, not explanatory product imagery.

## Do's And Don'ts

### Do

- Use Davinci-style serif at 52px and above for section headings.
- Set the hero wordmark around 374px and intentionally crop it at viewport edges.
- Alternate Putty light sections and Ink dark sections with hard cuts.
- Use 28.8px pill radius for filled CTAs.
- Use circular crops for feature imagery.
- Use Helvetica Now style utility type at 9-16px for nav, stats, labels, and buttons.
- Use hexagonal indicators as the secondary geometric brand motif.

### Don't

- Do not introduce saturated color.
- Do not use shadows or gradients.
- Do not use stock photography or modern digital illustration.
- Do not use the serif for ordinary body text below 34px.
- Do not use standard radius values like 4px, 8px, or 12px for main components.
- Do not add a visible menu bar or heavy navigation chrome.
- Do not let Helvetica Now style utility type take display duty.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Putty Canvas | `#c4c3b6` | Default background for light sections. |
| 1 | Bone Card | `#e7e5e4` | Elevated cards and secondary light surfaces. |
| 2 | Chalk Footer | `#ebebeb` | Lightest tier for footer and section bases. |
| 3 | Ink Room | `#000000` | Dark section canvas for feature and explainer blocks. |

## Elevation

The system is flat. Depth comes from hard section contrast, full-bleed imagery, circular crops, and scale. Do not use box shadows.

## Imagery

Use classical oil paintings: Renaissance or Baroque landscapes, architecture, clouds, still-life studies, and antique folio atmosphere. Use full-bleed painting panels or circular crops only. Avoid product screenshots, lifestyle photography, stock photography, modern 3D art, and generic illustrations.

## Layout

Use full-bleed sections with no normal max-width content container. The hero has a small centered type cluster above a huge cropped serif wordmark. Middle sections can use full-bleed painting backgrounds with one centered dark notched card. Feature sections can use black canvas, a centered 94px serif heading, and a 3-column grid of circular painting vignettes.

## Agent Prompt Guide

### Quick Color Reference

- Light background: `#c4c3b6`
- Dark background: `#000000`
- Card surface: `#e7e5e4`
- Primary text: `#000000` on light, `#ffffff` on dark
- Muted text: `#595855`
- Border: `#dfdcd5`
- Primary action: black pill, not a colored CTA

### Example Component Prompts

1. Hero wordmark section: full-bleed Putty background, small centered finance copy, TVL/APY stat row, black pill CTA, and a 374px cropped Davinci-style wordmark across the lower viewport.
2. Dark feature section: Ink background, centered 94px Paper serif heading, 3-column circular painting vignettes, and Paper hexagonal indicator dots.
3. Floating product card over painting: full-bleed classical landscape with one centered Ink notched square card and a tiny Paper `SCROLL` label.
4. Stat display block: inline TVL and APY pairs in Helvetica Now style 16px weight 500 with 28px gap.
5. Minimal header: 40px tall row with a circled S mark left and one Helvetica Now style text link right.

## Typographic Philosophy

The system uses size and tracking for drama. Davinci-style serif display at 94-374px should feel carved, cropped, and larger than the screen. Helvetica Now style utility type should stay functional and small. The serif does emotional work; the grotesk does systems work.

## Similar Reference Families

- Framework style serif/grotesk pairing on warm neutral canvas.
- Aesop style restrained beige gallery presentation.
- Older Vercel style minimal header and oversized wordmark.
- Museum sites using classical painting as atmospheric content.

