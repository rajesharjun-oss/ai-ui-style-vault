# Hungry Tiger - Style Reference

Hungry Tiger is a dark, rust-toned, typographic food brand system. It behaves less like a conventional ecommerce page and more like a spice-market poster: a warm brown canvas, massive condensed display text, pill-shaped controls, dotted gold dividers, small product jars, and low-contrast botanical texture. The identity is loud, warm, and flat.

## Theme

- Theme mode: dark.
- Visual temperature: hot, earthy, roasted, and monochrome-warm.
- Surface logic: ember canvas, spice cards, charred core, tiger-gold signal.
- Energy: maximalist, poster-first, condiment-label confidence.

## Core Principles

1. Make type the first read in every viewport.
2. Use `#faae33` as the only large chromatic accent.
3. Use `#d1255c` only for rare heat-level badges.
4. Keep the palette warm brown and gold.
5. Use full pills for every button, badge, input, and icon container.
6. Use 6px radius only on cards.
7. Do not use box shadows, glow effects, or gradients.
8. Keep product photography raw on the canvas, not inside frames.

## Color System

| Name | Value | Role |
| --- | --- | --- |
| Tiger Gold | `#faae33` | Primary action, filled buttons, active nav, display type, icon strokes |
| Ember Rust | `#823513` | Dominant page canvas, hero backdrop, primary section surface |
| Saffron Glow | `#9f531b` | Secondary warm accent, mid-tone type, decorative borders |
| Chili Red | `#d1255c` | Rare heat-level badge fill or alert accent |
| Charred Clove | `#281006` | Deepest surface, modal scrim, high-contrast button text |
| Dark Spice | `#402011` | Card surfaces, ghost fills, input fields, body/support text |
| Cardamom Brown | `#6b2e12` | Input borders, subtle dividers, muted inline elements |

## Typography

Primary type is Salmond. Use it almost everywhere, from massive display type to small nav labels. Fallbacks: Druk Wide, Antonio, Bebas Neue for display; Inter or Untitled Sans for small UI.

Graphikx is restricted to 13px functional microcopy, button labels, and inline meta where Salmond feels too loud. Fallbacks: Inter, Geist, Untitled Sans.

The tracking rule is inverse to size:

- Huge display: negative tracking.
- Small labels: slight positive tracking.
- No secondary display face.

Recommended scale:

| Token | Size | Weight | Line Height | Letter Spacing |
| --- | ---: | ---: | ---: | ---: |
| Caption | 11px | 500 | 1.2 | 0.02em |
| Subheading | 18px | 500 | 1.2 | 0.01em |
| Heading Small | 29px | 500 or 700 | 1.1 | -0.005em |
| Heading | 65px | 700 | 0.95 | -0.01em |
| Heading Large | 101px | 700 | 0.9 | -0.016em |
| Display | 195px | 700 | 0.8 | -0.02em |
| Display XL | 213px | 700 | 0.8 | -0.02em |

Rules:

- Hero and section display type should usually sit between 130px and 213px.
- Use line-height 0.80 to 0.90 for the largest type.
- Small UI labels can use 11px to 18px with 0.01em to 0.02em tracking.
- Body copy should not exceed 18px or line-height 1.4.

## Spacing And Shape

- Density: comfortable.
- Max width: 1440px, but many sections are full bleed.
- Section gap: 80px to 120px.
- Card padding: 12px to 16px.
- Element gap: 10px.
- Spacing values: 4, 6, 8, 9, 10, 12, 14, 16, 17, 20, 24, 26, 28, 32, 42, 192.

Radius:

- Cards: 6px.
- Badges: 9999px.
- Inputs: 9999px.
- Buttons: 9999px.
- Icon containers: 9999px.
- Do not use 6px radius on buttons, badges, inputs, or icons.

## Elevation

The system is flat.

- No box shadows.
- No drop shadows.
- No glows.
- No gradients.
- Depth comes from brown surface shifts: `#823513`, `#402011`, `#281006`.

## Layout

- Use full-bleed Ember Rust across the whole page.
- Avoid alternating section background colors.
- Each major band should feel like a poster.
- Crown each viewport with massive type first.
- Product jars are small anchored objects below or beside the huge text.
- Use asymmetric two-column compositions.
- Use dotted Tiger Gold horizontal rules between major viewports.
- Navigation is a minimal top bar with ghost pill buttons and a centered brand mark.
- Floating circular icon buttons can dock in the bottom-right corner.

## Motifs

- Dotted gold dividers.
- Low-opacity botanical watermarks, such as fern, leaf, and floral forms.
- Raw product bottle photography on transparent backgrounds.
- Thin gold line icons.

## Imagery

Preferred imagery:

- Studio-lit product jars.
- Transparent or minimally treated product PNGs.
- Small product bottles anchored on rust canvas.
- Low-contrast botanical watermarks.

Avoid:

- Lifestyle photography.
- Hands, kitchens, or table scenes.
- Product cards with frames.
- Rounded product images.
- Abstract graphics.
- 3D renders.

## Motion

Motion should not fight the poster character.

- Use simple border-color changes on inputs.
- Use subtle color and opacity shifts on controls.
- Avoid glow, shadow, bounce, or parallax.
- Keep the poster composition stable.

