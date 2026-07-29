# Basedash - Style Reference

> Midnight data terminal with frosted type: a pure-black product stage where white pills, quiet serif headlines, and sparse violet or mint data signals carry the composition.

## Theme

Dark. Basedash should feel like a calm internal-tool cockpit, not a neon cyberpunk page. Most surfaces are black or nearly black. The brightest object is the white primary button.

## Design Story

Build around a centered, quiet product narrative. The page should look like a premium data interface floating in the void: large hero type, minimal navigation, subdued supporting copy, and a dashboard mockup that uses violet and mint as chart accents.

Cards do not need heavy elevation. Use one-step-lighter black surfaces, soft edges, and almost invisible borders. Let contrast, spacing, and product imagery create hierarchy.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Void Black | `#000000` | `--color-void-black` | Page canvas, hero background, deepest surface |
| Carbon Card | `#050607` | `--color-carbon-card` | Card and elevated surface background |
| Graphite | `#333333` | `--color-graphite` | Deep borders and separators |
| Steel Gray | `#808080` | `--color-steel-gray` | Borders, dividers, icon strokes, disabled text |
| Ash Gray | `#b3b3b3` | `--color-ash-gray` | Secondary body text, helper copy, table content |
| Bone White | `#e8eaee` | `--color-bone-white` | Subtle light washes and secondary light elements |
| Ghost White | `#ffffff` | `--color-ghost-white` | Primary text and filled CTA background |
| Lavender Pulse | `#9984d8` | `--color-lavender-pulse` | Violet data accent, focus edges, chart marks |
| Mint Signal | `#3fcb7f` | `--color-mint-signal` | Positive state, validation, data accent |

## Typography

Primary UI font: Inter.

- Use Inter for nav, buttons, cards, forms, badges, tables, captions, and body text.
- Use tight tracking around `-0.03em` for functional text.
- Use weights 400, 500, and 600.

Display font: Alpha Lyrae, with Cormorant Garamond, EB Garamond, or PT Serif as fallback.

- Use only for hero h1 and major section titles.
- Keep display headings at 48px, 400 weight, line-height 1.
- Do not use the serif for body copy, nav, buttons, tables, or labels.

Quote font: Iowan Old Style, with Source Serif Pro Light, Lora, or Palatino as fallback.

- Use only for testimonial pull quotes around 24px, 300 weight, line-height 1.25.

## Type Scale

| Token | Size | Weight | Line height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 12px | 400 | 1.5 | -0.36px |
| Body Small | 14px | 400 | 1.43 | -0.42px |
| Body | 16px | 400 | 1.5 | -0.48px |
| Body Large | 18px | 400 | 1.56 | -0.54px |
| Subheading | 24px | 300 | 1.25 | -0.6px |
| Heading Small | 30px | 400 | 1.2 | -0.9px |
| Heading | 34px | 400 | 1.2 | -1.02px |
| Display | 48px | 400 | 1 | 0 |

## Spacing And Shape

- Base spacing unit: 4px.
- Page max width: 1200px.
- Section rhythm: 80px to 120px vertical gaps.
- Card padding: 16px to 20px.
- Hero copy max width: about 640px.
- Card radius: 16px.
- Button radius: 6px.
- Pill and badge radius: 999px.

## Components

### Filled Primary Button

White background, black text, Inter 14px medium, 6px radius, 12px vertical padding, 20px horizontal padding. No shadow and no colored fill. The white-on-black inversion is the main action signal.

### Ghost Text Button

Transparent background, no border, white text, Inter 14px medium. Use beside the filled button for secondary actions like demos, login, or docs.

### Top Navigation

Transparent header over a black canvas. Use a small logo and wordmark on the left, muted center nav links, and auth actions on the right. Height should feel close to 64px. Avoid heavy borders.

### Hero Centered Stack

Announcement pill, serif headline, muted subhead, button row, trust line, then product mockup. The stack is centered and quiet. The product image is the main visual anchor.

### Dashboard Mockup Frame

Use a dark dashboard screenshot or recreated mockup with subtle perspective. Charts may use Lavender Pulse and Mint Signal. Let edges fade into the black canvas.

### Testimonial Card

Keep testimonials open on the black canvas rather than boxed. Use a circular avatar, serif quote text, muted attribution, and a ghost case-study link.

## Layout

The page is a centered, max-width landing structure on pure black. Use a minimal transparent top nav, a centered hero, a large product mockup, alternating centered text and card grids, two-column testimonials, and dense integration logo grids. There is no sidebar and no heavy mega-menu.

## Imagery

Use product screenshots and interface visuals. No lifestyle photography, no abstract illustration, and no decorative gradients. The product is the hero image. Icons should be simple, geometric, and rendered in white or gray line style around 16px to 20px.

## Rules

Do:

- Make the primary CTA a white pill on black.
- Keep violet and mint for data, state, and focus.
- Use the display serif only for large editorial headlines.
- Let black space and product visuals dominate.
- Keep cards barely lighter than the canvas.

Do not:

- Use neon gradients as backgrounds.
- Turn violet into the primary CTA color.
- Overuse the serif in functional UI.
- Add lifestyle imagery or illustrated mascots.
- Put heavy shadows on dark cards.
