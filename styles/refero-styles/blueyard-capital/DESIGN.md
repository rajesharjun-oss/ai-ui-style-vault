# BlueYard Capital - Style Reference

## Positioning

BlueYard Capital feels like a printed monograph for frontier technology. The system is quiet, sharp, and spacious: a white canvas, a single grotesque typeface, very tight tracking, hard edges, and pale card-only color. It should not feel like a colorful startup SaaS page or a luxury brand. It should feel like an editorial observatory.

## Theme

- Theme: light
- Mood: sunset editorial observatory
- Best fit: venture capital, frontier tech, research labs, investment essays, portfolio systems, science and deep-tech editorial pages

## Visual Principles

1. Keep the canvas mostly white.
2. Let warm near-black type and borders carry nearly all structure.
3. Use pale tints only for cards, borders, or full-bleed section fields.
4. Keep every corner sharp at 0px.
5. Use no shadows, glows, or elevated surfaces.
6. Make the hero image large, unframed, and atmospheric.
7. Let whitespace and scale create hierarchy.

## Color System

| Token | Value | Role |
| --- | --- | --- |
| Canvas White | `#ffffff` | Page background, card surfaces, ghost button fill |
| Graphite Ink | `#3a3a3e` | Primary text, links, icon strokes, borders |
| Deep Carbon | `#090b11` | Strongest text and high-contrast card borders |
| Ash Veil | `#b5b0b0` | Warm gray section bands and soft borders |
| Apricot Wash | `#ffcf9e` | Warm card fills and hairline card borders |
| Iris Mist | `#babfff` | Lavender card borders and paired portfolio accents |
| Fuchsia Bloom | `#e3a2ef` | Single vivid card fill or highlight block |
| Polar Blue | `#bfe0f7` | Cool section tint or rare soft surface field |

## Typography

Instrument Sans is the only typeface. Use it for every headline, paragraph, caption, button, label, wordmark, and UI element. Weight 400 is the default for body and display. Weight 500 is used sparingly for nav labels, the wordmark, and small emphasis.

Use tight negative tracking at every size. The display size at 54px should feel compressed and editorial, not loose or friendly.

Recommended fallback:

- `Instrument Sans`, `Inter`, `Sohne`, `General Sans`, `ui-sans-serif`, `system-ui`

### Type Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Micro | 7px | 1 | 500 | tight |
| Tiny Label | 9px | 1.5 | 500 | tight |
| Small Label | 11px | 1 | 500 | tight |
| Caption | 12px | 1.5 | 400 | -0.36px |
| Body | 24px | 1.5 | 500 | -0.24px |
| Heading | 48px | 1.2 | 400 | -0.54px |
| Display | 54px | 1 | 400 | -1.62px |

## Spacing And Shape

- Density: compact
- Base unit: 4px
- Page max width: 1200px
- Section gap: 90px
- Card padding: 12px
- Element gap: 5px
- Radius: 0px on tags, cards, buttons, navigation, and images
- Elevation: none

## Layout

Use a full-bleed page model with content centered or left-aligned inside an implied 1200px width. The hero is the key pattern: a massive centered headline in the upper third and a large 3D object occupying the lower half, bleeding off the bottom edge. Below the hero, alternate white sections with soft tinted bands such as Ash Veil or Polar Blue. Use 90px vertical padding to let each section breathe.

Navigation should be minimal: a tiny stacked wordmark in the top-left and a single square hamburger control in the top-right. Do not add a normal horizontal nav bar.

## Imagery

Use large, uncaptioned rendered 3D objects, especially spherical or planetary forms with particle detail. Set them against a soft apricot-to-white atmospheric wash. The artwork should feel like a magazine cover plate and occupy a large share of the viewport.

Avoid photography, stock illustration, decorative icon packs, product screenshots, and framed images.

## Components

### Centered Editorial Headline

Large centered Instrument Sans headline at 54px, weight 400, line-height 1, tight tracking, and Graphite Ink. Place it high in the viewport with generous top padding.

### Apricot-Bordered Card

White surface, 1px Apricot Wash border, 12px padding, 0px radius, no shadow. Use the peach border as a quiet editorial mark.

### Apricot Fill Card

Solid Apricot Wash background, 12px padding, 0px radius, Graphite Ink text. Use sparingly to mark a single highlighted item.

### Lavender-Bordered Card

White surface with 1px Iris Mist border, 12px padding, 0px radius. Pair with apricot cards for a warm/cool portfolio rhythm.

### Fuchsia Fill Card

Solid Fuchsia Bloom background, 12px padding, 0px radius, Deep Carbon text. This is the most saturated object and should appear as a single block, not a repeated grid style.

### Polar Blue Surface Band

Full-bleed Polar Blue section background with no border and no radius. Use as a cool pause between warmer areas.

### Wordmark Lockup

Two-line uppercase wordmark, 12px Instrument Sans weight 500, line-height 1, tight tracking, Graphite Ink. No symbol and no containing badge.

### Hamburger Menu Button

40px by 40px white square with 1px Graphite Ink border, 0px radius, and a centered three-line hamburger icon.

### Ghost Link

Text link in Graphite Ink, no underline by default, 1px underline on hover. It inherits the surrounding type size and stays weight 400.

### Full-Bleed 3D Artwork Stage

Large rendered sphere or abstract planetary object in the lower half of the hero. No caption, frame, border, or card. It can bleed off the viewport.

### Hairline Divider

1px Graphite Ink line spanning the content width. No double lines, dots, or ornamental dividers.

## Rules

- Keep nearly all text and borders in Graphite Ink.
- Use chromatic tints only for cards, borders, and soft section fields.
- Do not use chromatic colors for text, icons, or primary buttons.
- Set every radius to 0px.
- Use Instrument Sans only.
- Use weight 400 for display and most content.
- Use weight 500 only for wordmark, nav labels, and small emphasis.
- Use negative tracking everywhere.
- Use 90px vertical section spacing.
- Do not add shadows, glows, or elevated surfaces.
- Do not add decorative gradients to UI components.
