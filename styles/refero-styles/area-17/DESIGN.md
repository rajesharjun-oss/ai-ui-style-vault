# AREA 17 - Style Reference

## North Star

Build the interface like a typographic monolith on white marble, interrupted only once by electric yellow. The page should feel restrained, editorial, and highly intentional: left-aligned text, generous silence, flat surfaces, and cinematic media that breaks the grid.

## Theme

Light. Pure White is the canvas. Graphite is the main text color. Electric Yellow is the only permitted chromatic accent and should appear as a singular signal, not decoration.

## Color Tokens

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Pure White | `#ffffff` | `--color-pure-white` | Page canvas, input fields, inverse text on dark surfaces |
| Graphite | `#1a1a1a` | `--color-graphite` | Primary text, headlines, body copy, navigation links |
| True Black | `#000000` | `--color-true-black` | Logo mark fill, select borders, deepest shadow tone if needed |
| Hairline | `#e6e6e6` | `--color-hairline` | Borders, dividers, outlined control strokes, card edges |
| Fog | `#f2f2f2` | `--color-fog` | Secondary card surfaces, disabled button fills, quiet elevation layers |
| Cream Stone | `#f2ede9` | `--color-cream-stone` | Warm editorial feature-card surface |
| Muted | `#949494` | `--color-muted` | Secondary links, metadata, subdued captions |
| Dim | `#757575` | `--color-dim` | Tertiary text, low-priority helper copy |
| Disabled | `#cccccc` | `--color-disabled` | Disabled controls and inactive fills |
| Electric Yellow | `#fdf313` | `--color-electric-yellow` | Announcement bar and the only chromatic accent in the system |

## Typography

Use Suisse Intl if available. Fallback to Inter, Sohne, GT America, or Manrope.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 16px | 400 | 1.5 | 0.06px |
| Subheading | 20px | 500 | 1.4 | -0.28px |
| Heading Small | 32px | 500 | 1.15 | -0.42px |
| Heading | 42px | 500 | 1.15 | -0.59px |
| Display | 55px | 500 | 1.1 | -0.82px |

Rules:

- Use Suisse Intl as the workhorse for headlines, body, navigation, and UI.
- Use weight 400 for most text and 500 for navigation or emphasis.
- Use display headlines at 55px, 1.10 line-height, and tight negative tracking.
- Keep body and caption text close to normal tracking.
- Use system sans only as a fallback for forms or accessibility-sensitive UI.
- Do not use system-ui as the primary voice.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | Comfortable |
| Base unit | 8px |
| Max width | 1440px |
| Section gap | 80px to 192px |
| Card padding | 16px to 24px |
| Element gap | 8px to 16px |

Spacing scale: 8, 16, 24, 32, 48, 64, 80, 128, 192, 232.

Radius scale:

- Navigation: 4px.
- Cards: 8px.
- Images: 8px.
- Inputs: 8px.
- Buttons: 8px.
- Pills: 9999px.

Elevation:

- Use no shadows, glows, or blur effects.
- Communicate layering through surface color shifts: Pure White to Fog to Cream Stone.
- Borders should use Hairline and stay 1px.

## Components

### Announcement Bar

Use a full-width fixed bottom bar with Electric Yellow background and Graphite text. Set text in Suisse Intl 16px/1.5. Keep the bar about 40px to 48px high with 12px vertical and 24px horizontal padding. This should be the system's only bright chromatic surface.

### Top Navigation

Use transparent or Pure White background with no border. Place the A slash-style mark on the left and right-aligned links at 16px, 500 weight, Graphite. Use 64px to 84px nav height and 24px to 48px horizontal padding.

### Editorial Headline

Use Suisse Intl 55px or 42px, weight 400 to 500, 1.10 to 1.15 line-height, Graphite, and negative tracking. Left-align, keep max width around 900px, and avoid decorative elements.

### Ghost Text Link

Use no fill and no border. Text is Suisse Intl 16px, 500 weight, Graphite. Hover may shift to Muted or add underline. This should be the dominant interactive pattern.

### Outlined Button

Use transparent background, 1px Graphite border, 8px radius, 16px vertical and 24px horizontal padding, 16px 500-weight text. Hover inverts to Graphite background with Pure White text.

### Solid Neutral Button

Use Fog background, no border, 8px radius, 16px vertical and 24px horizontal padding, 16px 500-weight Graphite text. Keep it quiet and non-chromatic.

### Fog Card

Use Fog surface, no border, 8px radius, 16px to 24px padding, and no shadow. Use for low-weight content blocks.

### Cream Feature Card

Use Cream Stone surface, no border, 8px radius, 24px padding, and no shadow. Use sparingly for editorial feature content.

### Text Input

Use Pure White background, 1px Hairline border, 8px radius, 12px vertical and 16px horizontal padding, 16px Suisse Intl text, Graphite value text, Muted placeholder, and Graphite focus border.

### Full-Bleed Video Block

Use edge-to-edge media with no border and no radius when it breaks the typographic grid. Use 16:9 or wider aspect ratio. Do not add overlay text or decorative framing.

### Pill Element

Use 9999px radius only for rare status or tag metadata. Background is Fog or transparent, text is 16px 500-weight Suisse Intl.

### Footer

Use Pure White or Fog background, large 128px+ vertical padding, Graphite links, Muted copyright text, and no heavy decoration.

## Layout And Imagery

- Use a left-aligned editorial grid for type.
- Keep text blocks around 900px max width.
- Use 1440px as the outer page max width where constrained content is needed.
- Let media blocks go full-bleed to viewport edges.
- Alternate quiet white space, typographic sections, full-bleed media, and more whitespace.
- Keep content density low.
- Avoid centered marketing-style hero blocks.
- Use cinematic, naturalistic, human-centered photography and video.

## Do

- Use Suisse Intl 55px/1.10 with tight tracking for editorial headlines.
- Maintain the monochrome palette across all pages.
- Use Electric Yellow only as one singular accent.
- Use 8px radius for cards, buttons, images, and inputs.
- Use Hairline for all borders and dividers.
- Let section gaps range from 80px to 192px.
- Use ghost links and outlined buttons for most interactions.
- Left-align headlines and body copy.

## Do Not

- Do not add any chromatic colors beyond Electric Yellow.
- Do not use shadows, glows, or blur effects.
- Do not use system-ui as the primary typeface.
- Do not center-align editorial body or headline blocks.
- Do not use random radii outside 4px, 8px, and 9999px.
- Do not fill pages with imagery; use full-bleed media as punctuation.
- Do not loosen body letter spacing.
