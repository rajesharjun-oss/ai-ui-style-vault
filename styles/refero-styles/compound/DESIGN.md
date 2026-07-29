# Compound - Style Reference

> Ink-on-paper wealth journal.

Theme: light

Compound is a quiet editorial finance system. It uses one typeface, one weight, an almost fully achromatic palette, and very soft shadows. The visual language is intentionally silent: white canvas, pale graphite borders, generous whitespace, and centered type-led sections. Hierarchy comes from scale and spacing, not from bold text or color.

The only warm color is a cream announcement strip at the top of the page. The main action is a near-black pill button. Product UI is shown in a centered preview card with 20px radius, a pale border, and a four-layer soft shadow. This card is the main object in an otherwise flat page.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Ink | `#171717` | `--color-ink` | Primary text, wordmark, filled pill buttons, navigation emphasis. |
| Paper | `#ffffff` | `--color-paper` | Page canvas, cards, product preview background. |
| Graphite Hairline | `#e5e7eb` | `--color-graphite-hairline` | Borders, dividers, card edges, input borders. |
| Vellum | `#f3f3f3` | `--color-vellum` | Secondary fills, hover washes, publication logo cards. |
| Slate | `#6f6f6f` | `--color-slate` | Secondary copy, metadata, tab labels, icon strokes. |
| Pewter | `#5e5e5e` | `--color-pewter` | Helper text and emphasized secondary captions. |
| Ash | `#a0a0a0` | `--color-ash` | Tertiary copy, placeholders, disabled text. |
| Carbon | `#222222` | `--color-carbon` | Decorative vector fills and icon strokes. |
| Stone | `#c7c7c7` | `--color-stone` | Abstract 3D forms, gradient endpoints, depth washes. |
| Cream Notice | `#ffe9bf` | `--color-cream-notice` | Announcement bar background and the single warm accent. |

## Tokens - Typography

### Monument Grotesk

Sole typeface for the whole system.

- Substitute: Inter, General Sans, Sohne, system-ui, sans-serif
- Weight: 400 only
- Sizes: 12px, 13px, 14px, 16px, 18px, 36px, 48px, 58px, 60px, 72px
- Line heights: 1.00 to 1.71
- OpenType: use kerning where available
- Rule: no bold, italic, light, serif, monospace, or second font. Scale is the hierarchy.

### Type Scale

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| caption | 12px | 400 | 1.5 | 0 |
| body-sm | 14px | 400 | 1.43 | 0 |
| body | 16px | 400 | 1.5 | 0 |
| subheading | 18px | 400 | 1.38 | 0 |
| heading-sm | 36px | 400 | 1.25 | 0 |
| heading | 48px | 400 | 1.11 | 0 |
| heading-lg | 60px | 400 | 1.1 | 0 |
| display | 72px | 400 | 1.0 | 0 |

## Tokens - Spacing And Shape

- Density: comfortable
- Base unit: 8px
- Page max width: 1200px
- Section gap: 80px
- Card padding: 24px
- Element gap: 8px
- Scale: 8, 16, 24, 32, 40, 48, 56, 64, 80, 112, 128, 160, 176px

### Radius

| Element | Value |
| --- | --- |
| Small cards | 8px |
| Cards | 20px |
| Large cards | 24px |
| List items | 28px |
| Buttons | 9999px |
| Icons | 9999px |

### Shadows

Use faint four-layer shadows. Opacity should stay between 0.01 and 0.10.

- Product preview: `rgba(207, 207, 207, 0.01) 0 132px 53px, rgba(207, 207, 207, 0.05) 0 74px 44px, rgba(207, 207, 207, 0.09) 0 33px 33px, rgba(207, 207, 207, 0.10) 0 8px 18px`
- List container: `rgba(194, 194, 194, 0.01) 0 168px 67px, rgba(194, 194, 194, 0.05) 0 94px 57px, rgba(194, 194, 194, 0.09) 0 42px 42px, rgba(194, 194, 194, 0.10) 0 10px 23px`
- Link hover lift: `rgba(0, 0, 0, 0.01) 0 128px 51px, rgba(0, 0, 0, 0.02) 0 72px 43px, rgba(0, 0, 0, 0.03) 0 32px 32px, rgba(0, 0, 0, 0.04) 0 8px 18px`

## Components

### Announcement Bar

Full-bleed Cream Notice strip at the very top. Use centered Ink text at 12px to 14px, 7px to 8px vertical padding, and a small dark pill button for "Read more" style actions. No border or shadow.

### Top Navigation

White nav with no border and no shadow. Wordmark on the left, centered 14px links, and a right-side sign-in link plus filled pill button. Keep the bar quiet and typographic.

### Filled Pill Button

Ink fill, white 14px text, full radius, 16px horizontal padding, 8px to 9px vertical padding. No border and no shadow. This is the only filled button style.

### Ghost Text Link

Text-only action with Ink text, 14px size, and a 1px underline. Use for nav, footer links, and inline secondary actions.

### Product Preview Card

White surface, 20px radius, 1px Graphite Hairline border, and four-layer soft shadow. Contains dashboard or product UI. This is the main elevated object in the system.

### Feature Service Card

Vellum or transparent surface, 20px radius, no border, 24px padding. Include a small indicator, Ink label, and Slate description. Arrange as a 4-column row.

### Publication Logo Card

Vellum surface, 20px radius, no border, no shadow, centered grayscale logo. Use in a 3-column press or credibility row.

### Section Divider

1px Graphite Hairline rule spanning the content width. Place a centered Slate label on the line, interrupting the stroke.

### Hero Display Headline

Centered 60px to 72px Monument Grotesk at weight 400, Ink color, tight line height, and no eyebrow. Keep it short, usually one sentence across two lines.

### Circular Icon Container

Full-radius 32px to 40px circle with Vellum or white background and a monochrome 16px to 20px icon.

### Stats Metric Row

Inline metric block with Slate label and large Ink value. Non-grayscale accents should be avoided except tiny semantic indicators inside product UI when unavoidable.

## Layout

Use a centered max-width layout around 1200px. The hero is a single centered display headline over a translucent gray 3D ribbon or helix form, followed by a centered product preview card. Below the fold, use a 4-column service row and a 3-column publication row.

Separate sections with 80px vertical gaps or hairline dividers with centered labels. Avoid sidebars, asymmetric collages, and overlapping content.

## Imagery

Imagery is restrained. Use a translucent gray abstract 3D ribbon behind the hero and one embedded dashboard preview. Use grayscale publication logos on Vellum cards.

Avoid photography, lifestyle imagery, human figures, colorful illustrations, and decorative image collages.

## Do

- Use only Monument Grotesk-style typography at weight 400.
- Use full radius for buttons, tags, and icon containers.
- Use 20px radius for cards.
- Use Graphite Hairline for borders and dividers.
- Use 80px vertical section gaps.
- Keep the palette achromatic except the cream announcement strip.
- Use very soft four-layer shadows for elevated elements.

## Do Not

- Do not introduce new chromatic accents.
- Do not add another typeface or another weight.
- Do not use sharp corners on cards or buttons.
- Do not use dark or heavy shadows.
- Do not use full-surface colors outside Paper, Vellum, and Cream Notice.
- Do not reduce major section gaps below 64px.
- Do not add decorative colored strokes or outlines to headings.

