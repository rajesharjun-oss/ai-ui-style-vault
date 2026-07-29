# New Form - Style Reference

## Positioning

New Form feels like a financial broadsheet redesigned for the web. The system is bold, oversized, and typographic. It should feel editorial and institutional, with neon green acting like a marker strike across an otherwise monochrome newspaper surface.

## Theme

- Theme: light
- Mood: editorial broadsheet in a green room
- Best fit: venture capital, crypto funds, financial research, investment thesis pages, institutional editorial, typographic launch pages

## Visual Principles

1. Use Bone White, not pure white, as the canvas.
2. Make typography the primary visual object.
3. Use Highlighter Green as the only saturated accent.
4. Treat photography as printed inserts, not full-color content.
5. Keep buttons sharp and editorial, not pill-round.
6. Use micro-labels instead of heavy UI chrome.
7. Close pages with a full-bleed green signature band.

## Color System

| Token | Value | Role |
| --- | --- | --- |
| Bone White | `#fafffa` | Page canvas, cards, text on dark sections |
| Press Black | `#121613` | Headline color, footer background, dominant dark surface |
| Typesetter Ink | `#000000` | Primary text, body, icons on light surfaces |
| Slate Verdant | `#232924` | Secondary dark surface and bordered sections |
| Newsprint Gray | `#516254` | Muted captions, helper text, editorial data |
| Muted Sage | `#c8d2c8` | Light text on dark surfaces and inverse labels |
| Highlighter Green | `#2bee4b` | Primary action fill, active underline, footer band |
| Shadow Moss | `#93b799` | Green-tinted button shadow and supporting detail |
| Echo Green | `#c4e4c9` | Low-frequency supporting green-gray accent |

## Typography

Use TWK Lausanne for UI, nav, body, micro-labels, grotesque headings, and button labels. Use PP Mondwest for the largest editorial serif headlines. Use Editorial New for lighter secondary editorial passages. Times can be used for old-school underlined inline links and body-adjacent details.

Recommended fallbacks:

- UI: `TWK Lausanne`, `Inter`, `Sohne`, `Neue Haas Grotesk`, `ui-sans-serif`, `system-ui`
- Main display serif: `PP Mondwest`, `GT Sectra`, `Tiempos Headline`, `Recoleta`, `serif`
- Secondary display: `Editorial New`, `GT Super`, `Domaine Display`, `Canela`, `serif`
- Link serif: `Times`, `Times New Roman`, `serif`

### Type Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Caption | 11px | 1.1 | 550 | 0.11px |
| Body Small | 14px | 1.1 | 350 | 0.14px |
| Body | 18px | 1 | 400 | -0.36px |
| Subheading | 60px | 0.9 | 300 | -1.2px |
| Heading Small | 72px | 1 | 550 | -1.44px |
| Heading | 96px | 1 | 550 | -1.92px |
| Heading Large | 155px | 1 | 550 | -6.2px |
| Display | 295px | 0.9 | 400 | -11.8px |

## Font Roles

### TWK Lausanne

Primary UI and navigation face. Use 11px weight 550 uppercase with small positive tracking for micro-labels, 16px to 18px body copy, and 72px to 155px grotesque headlines with tight tracking.

### PP Mondwest

Main display serif for the largest hero headlines. Use 165px to 295px, weight 400, line-height 0.9, and -0.04em tracking. It should read as one dense block of printed ink.

### Editorial New

Secondary display face for lighter, italic-leaning editorial passages. Use 60px to 240px, weight 300, line-height 0.9, and slightly less aggressive negative tracking.

### Times

Old-school browser serif used for underlined inline links and small editorial details.

## Spacing And Shape

- Density: spacious
- Page max width: 1400px
- Section gap: 80px
- Card padding: 0px
- Element gap: 20px
- Buttons: 5px radius
- Pills and ghost outline blocks: 10px radius
- Images: 14px radius
- Avoid 9999px pill buttons for primary actions

## Shadows

Only the green action button gets elevation, and the shadow must be green-tinted.

```css
--shadow-lg: rgba(16, 94, 29, 0.45) 1px 8px 20px 0px;
--shadow-lg-2: rgba(18, 146, 39, 0.25) 1px 8px 20px 0px;
```

## Layout

Use a wide 1400px broadsheet canvas. Hero sections should be dominated by enormous display text, with small filtered photos inserted inline between lines of type. Dark editorial sections can switch to Press Black with Bone White type. The page should close with a full-width Highlighter Green band before the footer.

## Imagery

Photographs are rectangular editorial inserts. Apply a grayscale plus green hue treatment so all images belong to the same tonal family. They should interrupt the type flow rather than sit in standard grids.

Recommended CSS filter:

```css
filter: grayscale(1) saturate(1) invert(0.27) sepia(0.07) saturate(10.67) hue-rotate(80deg) brightness(1.02) contrast(0.83);
```

## Components

### Highlighter Green Action Button

Highlighter Green fill, black uppercase TWK Lausanne label, 5px radius, 20px by 30px padding, and green-tinted shadow. This is the only saturated filled button.

### Ghost Outline Button

Transparent fill, 1px Bone White border, Bone White uppercase label, 10px radius. The tall padding can make it feel more like a full-height menu item than a compact button.

### Underlined Text Link

No fill and no border. Times 16px with a 1px underline that sits close to the baseline. Do not change weight or color on hover.

### Editorial Photo Insert

Small rectangular grayscale-green photo tile, 14px radius, placed inline between display text lines. Do not place these in a standard image grid.

### Stat Callout

Large editorial metric set in Newsprint Gray with no extra decoration. Muted color makes the metric read as data, not marketing.

### Category Tag

Muted Sage uppercase TWK Lausanne label, around 14px weight 350, no background and no border.

### Navigation Wordmark

TWK Lausanne bold wordmark with a 2px Highlighter Green underline under the first word. The underline is the logo treatment.

### Full-Bleed Accent Band

Edge-to-edge Highlighter Green band before the footer, roughly poster-scale in height. It functions as the closing signature.

### Dark Editorial Section

Press Black background with Bone White type. Use large TWK Lausanne headings and light body copy. Filled green CTAs can be replaced by ghost buttons here.

### Footer

Press Black background with Bone White small-caps columns and light body contact lines, followed by the green band signature.

## Rules

- Use Highlighter Green as the only saturated accent.
- Use the green-tinted shadow on green buttons, not a gray shadow.
- Keep the canvas Bone White.
- Use micro-labels in TWK Lausanne 11px uppercase with positive tracking.
- Use PP Mondwest for huge 165px to 295px hero type.
- Apply the grayscale-green filter to photography.
- Place image tiles inline with display type.
- Use the full-bleed green band before the footer.
- Do not use 9999px radius on primary actions.
- Do not use box-shadow on cards or content blocks.
- Do not render photos in full color.
- Do not set body copy larger than 18px.
