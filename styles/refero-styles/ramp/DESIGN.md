# Ramp - Style Reference

Ramp is a light editorial finance system. It uses a warm off-white page, white surfaces, hairline grey structure, near-black type, and a single highlighter yellow-green accent. The personality is precise, efficient, and financially alert: it should feel like a premium business publication that happens to contain product software.

## Theme

- Theme mode: light.
- Visual temperature: warm monochrome with one electric accent.
- Surface logic: paper canvas, white cards, grey borders, dark text, and one dark data band.
- Energy: focused and utility-first, not decorative.

## Core Principles

1. Keep the palette almost black and white.
2. Use `#e4f222` only for the most important money/action signal.
3. Prefer borders over shadows.
4. Use one type family at one weight.
5. Build hierarchy with size, spacing, alignment, and rhythm.
6. Keep all copy and content left aligned inside centered containers.
7. Use product screenshots and real UI frames instead of decorative artwork.

## Color System

| Name | Value | Role |
| --- | --- | --- |
| Highlighter Yellow | `#e4f222` | Primary CTA fill, live counter cue, active indicator, money signal |
| Ink | `#0c0a08` | Main text, headings, dark outlines, icon color |
| Obsidian | `#1a1919` | Inverted sections, nav/footer dark panels, counter strip |
| Ash | `#6d6c6b` | Secondary text, captions, muted labels |
| Smoke | `#d3d3d3` | Skeletons, quiet surfaces, subtle borders |
| Hairline | `#e5e7eb` | Card borders, dividers, grid lines, structural outlines |
| Bone | `#f4f2f0` | Page background, hover fills, wash cards |
| Paper | `#ffffff` | Cards, panels, modals, reversed text on dark backgrounds |

## Typography

Use one custom neo-grotesque family: `lausanne`. Fallbacks: `Inter`, `IBM Plex Sans`, `Sohne`, `Arial`, `sans-serif`.

Rules:

- Use weight `400` only.
- Do not use bold, semibold, or font-weight-based hierarchy.
- Enable OpenType feature `ss01`.
- Body type is efficient but not cramped.
- Display type is large, left aligned, and tightly line-heighted.
- Micro labels use uppercase, 10px type, and slight positive tracking.

Recommended scale:

| Token | Size | Line Height | Letter Spacing |
| --- | ---: | ---: | ---: |
| Micro Label | 10px | 2.2 | 0.018em |
| Small | 13px | 1.4 | 0 |
| Body | 16px | 1.5 | 0 |
| Subheading | 20px | 1.3 | 0 |
| Heading Small | 24px | 1.17 | 0 |
| Heading | 28px | 1.14 | 0 |
| Heading Large | 40px | 1.05 | 0 |
| Display | 64px | 1.0 | 0 |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Max content width: 1200px.
- Section rhythm: 64px to 128px.
- Card padding: 20px to 24px.
- Element gaps: 8px, 12px, 16px, and 24px.
- Radius scale: 6px, 10px, 12px, 16px.

Radius rules:

- Buttons and tags: 6px.
- Inputs: 10px.
- Wash cards: 12px.
- Content cards and testimonials: 16px.
- Avoid 4px corners.
- Avoid fully rounded pills.

## Elevation

Ramp is almost shadowless.

- Use `1px solid #e5e7eb` on cards and panels.
- Avoid normal box shadows on cards, modals, and feature blocks.
- The one acceptable effect is a very subtle inset white highlight on sticky navigation.

## Layout

- Use full-bleed page bands with centered 1200px content.
- Keep content left aligned inside those containers.
- Hero layout: typographic lead on the left, large product screenshot extending visually to the right.
- Feature layout: two-column text and product visual.
- Counter sections: one full-width dark strip.
- Logo grid: thin bordered cells, grayscale marks, around seven columns on desktop.
- Testimonials: card grid or scroll area, four columns on large screens.
- Page rhythm: generous light sections interrupted by a dark data band.

## Imagery

Preferred imagery:

- Product screenshots.
- Browser chrome frames.
- Finance dashboards, card UI, charts, and account panels.
- Grayscale customer logos.
- One dark product image can be used as a brand moment.

Avoid:

- Stock photography.
- Decorative illustrations.
- Large gradients.
- Lifestyle photos.
- Cute mascot or playful visual language.

## Motion

Motion should feel operational.

- Duration: 300ms to 400ms.
- Easing: ease-out.
- Animate color, background, border, fill, and stroke.
- Avoid theatrical transforms.
- Use opacity carefully for counters and subtle state changes.
- Backdrop blur can appear on sticky nav or overlays.

