# Mode - Style Reference

## Positioning

Mode feels like business intelligence moved into a sunlit greenhouse. It keeps the clarity of a data product, but swaps cold grays for sage paper, deep forest text, and a sharp chartreuse action accent. It should feel intellectual, warm, editorial, and confident.

## Theme

- Theme: light
- Mood: sunlit greenhouse editorial
- Best fit: analytics, BI, dashboards, data notebooks, metrics platforms, reporting tools, data teams, research products

## Visual Principles

1. Use Pale Sage as the page canvas.
2. Use Paper White only for elevated surfaces.
3. Use Deep Forest for text and dark sections.
4. Use Chartreuse Lime as the single action accent.
5. Use Grenette for display and section headings at 36px and above.
6. Use Graphik for body and UI.
7. Use color layers instead of shadows.
8. Keep radii strictly split: 4px for small controls, 16px for larger surfaces.

## Color System

| Token | Value | Role |
| --- | --- | --- |
| Pale Sage | `#eef2e3` | Page canvas, light cards, eyebrow backgrounds, hero photo mats |
| Paper White | `#fcfcfc` | Elevated cards, nav, modals, footer |
| Ink Black | `#000000` | Text, icon strokes, hairline borders, ghost outlines |
| Charcoal | `#242423` | Secondary text and muted icon fills |
| Deep Forest | `#043f2e` | Brand primary, body text on sage, dark sections, stat cards |
| Chartreuse Lime | `#c8f169` | Filled CTA, accent highlights, tags, badge backgrounds |
| Forest Mid | `#2a6f2b` | Hover and active state for green surfaces |
| Vivid Green | `#78c51c` | Data visualization support and secondary chart strokes |

## Typography

Use Grenette for display and section headlines at 36px and above. It should stay weight 400 with tight negative tracking. Do not use Graphik for display headlines.

Use Graphik for body, UI, buttons, navigation, and eyebrow labels. Weight 600 is reserved for nav and button labels. Body and display should stay weight 400.

Recommended fallbacks:

- Display serif: `Grenette`, `Fraunces`, `Source Serif 4`, `Tiempos Headline`, `serif`
- UI sans: `Graphik`, `Inter`, `Sohne`, `Untitled Sans`, `ui-sans-serif`, `system-ui`
- System fallback only: `Times New Roman`, `serif`

## Type Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Caption | 12px | 1.2 | 500 | 0.72px |
| Body Small | 14px | 1.3 | 400 | 0 |
| Body | 16px | 1.3 | 400 | 0 |
| Subheading | 18px | 1.44 | 400 | 0 |
| Heading Small | 22px | 1.2 | 600 | 0 |
| Heading | 36px | 1.1 | 400 | -0.72px |
| Heading Large | 56px | 1.1 | 400 | -1.68px |
| Display | 96px | 0.9 | 400 | -2.98px |

## Spacing And Shape

- Base unit: 4px
- Density: comfortable
- Page max width: 1200px
- Section gap: 56px to 80px
- Card padding: 16px to 24px
- Element gap: 12px to 20px
- Buttons: 4px radius
- Inputs: 4px radius
- Tags: 4px or 9999px depending on variant
- Cards: 16px radius
- Image blocks: 16px radius
- Large surfaces: 16px radius

## Layout

Use a full-bleed Pale Sage canvas with centered 1200px content. The hero can use an asymmetric two-column split: documentary photo on one side, large serif headline and stat card on the other. Alternate white and sage sections with generous vertical gaps. Feature sections work well as two-column text and image layouts.

Navigation should be minimal: left logo, centered links, right CTA pair.

## Imagery

Use warm, documentary, human workplace photography: people at desks, teams reviewing screens, candid collaboration, and naturally lit workspace scenes. Do not use staged stock, duotone treatments, overlays, or decorative filters. Let the sage mat make the photo feel editorial.

## Components

### Display Headline

Grenette at 56px to 96px, weight 400, line-height 0.9 to 1.1, tight negative tracking, Deep Forest on sage or Ink Black on white. Never bold and never italic.

### Section Heading

Grenette at 36px, weight 400, -0.72px tracking, line-height 1.1. Invert to Paper White on Deep Forest sections.

### Filled CTA Button

Chartreuse Lime fill, Ink Black text, 4px radius, 12px by 20px padding, Graphik 16px weight 500. No border. Hover can move toward Forest Mid.

### Ghost CTA Button

Transparent fill, 1px Ink Black border, 4px radius, 12px by 20px padding, Graphik 16px weight 500. Invert border and text to Paper White on dark sections.

### Navigation Pill Button

Transparent nav link with Graphik 16px weight 500, horizontal padding, and subtle active underline or weight shift. Do not turn nav into chunky cards.

### Pale Sage Card

Pale Sage background, 16px radius, 24px padding, no border, no shadow. Usually content-defined rather than elevation-defined.

### Forest Stat Card

Deep Forest background, 16px radius, 24px padding, Paper White text, dense layout, and optional Chartreuse label. Used for hero metrics and featured statistics.

### Paper White Elevated Card

Paper White background, 16px radius, 24px padding, optional 1px hairline border. Use when a surface needs to lift off sage without shadow.

### Announcement Banner

Full-width top strip on Pale Sage or Paper White. Centered Graphik 14px text and an optional Chartreuse small link or pill.

### Eyebrow Label

Graphik 12px to 14px weight 500, uppercase, 0.06em positive tracking, Deep Forest or Ink Black. Place above section headings.

### Tag Or Badge

Chartreuse or Pale Sage fill, Ink Black text, 4px radius or pill variant, small padding, Graphik 12px to 14px weight 500.

### Hero Image Block

Warm documentary photo inside a 16px radius sage card. Avoid overlays and filters.

### Icon

Stroke-based 1.5px to 2px icons in Ink Black or Deep Forest. Invert to Paper White on dark surfaces.

## Rules

- Use Pale Sage for the page canvas.
- Use Paper White only for elevated cards, nav, modals, and footer.
- Use Deep Forest for all primary text on sage or paper.
- Use Grenette for all display and section headings at 36px and above.
- Use Chartreuse Lime as the only filled CTA color.
- Use no more than one chromatic accent per viewport.
- Use 16px radius for cards, image blocks, and large surfaces.
- Use 4px radius for buttons, inputs, and small tags.
- Do not use 8px, 12px, or 20px radii.
- Do not add box shadows.
- Do not use pure white as the page background.
- Do not apply bold weights to body or display text.
- Do not use the serif below 36px.
