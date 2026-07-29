# Airbnb - Style Reference

Airbnb is a white-canvas, photography-first marketplace system. The interface itself stays almost entirely monochrome so property images can carry the mood. One coral-red accent, Rausch, marks the logo, search submit, wishlist state, and primary action moments.

## Theme

- Theme mode: light.
- Visual temperature: soft white, travel gallery, photograph-led.
- Surface logic: Faint canvas, White cards, Bebe dividers, Hof text, Rausch action.
- Energy: calm, browseable, image-forward, rounded, compact.

## Core Principles

1. Let property photography carry the experience.
2. Use Rausch only for the logo, search action, active wishlist hearts, and one primary action per surface.
3. Keep listing cards flat, borderless, and shadowless.
4. Use 9999px radius for the search bar and circular/pill controls.
5. Use 12px radius for listing cards and images.
6. Use compact 14px body copy as the content backbone.
7. Use value contrast and whitespace instead of chrome.

## Color System

| Name | Value | Role |
| --- | --- | --- |
| Rausch | `#ff385c` | Logo, search submit, active wishlist hearts, primary action punctuation |
| Rausch 600 | `#e00b41` | Pressed or active accent variant |
| Hof | `#222222` | Primary text, headings, icon strokes, inverse backgrounds |
| Foggy | `#6a6a6a` | Secondary text, metadata, helper copy, disabled icons |
| Grey 500 | `#c1c1c1` | Disabled text, placeholders, muted icon strokes |
| Deco | `#dddddd` | Muted card states and skeleton placeholders |
| Bebe | `#ebebeb` | Hairline borders, dividers, input underlines |
| Faint | `#f7f7f7` | Page canvas, footer, hover states |
| White | `#ffffff` | Listing cards, input surfaces, modals, overlays |

## Typography

Primary type is Airbnb Cereal VF. Fallbacks: Circular, Inter, DM Sans, system-ui, sans-serif. Enable `salt` alternates where supported.

Rules:

- Body content is 14px, weight 400, line-height 1.43.
- UI labels are 16px, weight 500.
- Section headings are 22px, weight 500, tracking -0.02em.
- Page titles can be 28px, weight 700.
- Avoid body and metadata weight 700.
- Keep typography compact and readable.

Recommended scale:

| Token | Size | Weight | Line Height | Letter Spacing |
| --- | ---: | ---: | ---: | ---: |
| Caption | 11px | 400 | 1.18 | 0 |
| Metadata | 12px | 400 | 1.33 | 0 |
| Small | 13px | 400 | 1.23 | 0 |
| Body | 14px | 400 | 1.43 | 0 |
| UI | 16px | 500 | 1.25 | 0 |
| Subheading | 20px | 600 | 1.2 | -0.18px |
| Heading Small | 22px | 500 | 1.18 | -0.44px |
| Card Title Emphasis | 21px | 700 | 1.43 | 0 |
| Heading | 28px | 700 | 1.43 | 0 |

## Spacing And Shape

- Density: compact.
- Base unit: 4px.
- Max width: 1440px where a constrained width is needed.
- Many marketplace pages are full-width with around 40px desktop horizontal padding.
- Section gap: 48px.
- Card padding: 12px.
- Element gap: 12px.
- Spacing values: 4, 8, 12, 16, 20, 24, 28, 32, 40, 44, 48.

Radius:

- Inputs: 8px.
- Ghost buttons: 8px.
- Cards and listing images: 12px to 14px.
- Search bar: 9999px.
- Buttons, badges, avatars, icon buttons, and hearts: 9999px.

## Elevation

Keep most surfaces flat.

- No shadows on listing cards.
- Search bar gets a layered soft shadow.
- Dropdowns, modals, popovers, and tooltips can use soft overlay shadows.
- Listing rows rely on white cards against Faint canvas.

## Layout

- Top nav is fixed, white, around 80px high.
- Logo sits left in Rausch.
- Center nav contains tab-style category items.
- Right side contains Become a host, language selector, and hamburger menu.
- Search bar is the hero: a centered floating capsule rather than a headline-led hero.
- Listing sections are stacked vertical rows with horizontal scrolling card grids.
- Each section has a 22px title and carousel controls.
- Footer uses a 3-column link grid on Faint.

## Imagery

Preferred imagery:

- Real property photos.
- Warm, well-lit interiors and exteriors.
- 1:1 listing card crops.
- Full-bleed images inside card frames.
- Minimal monochrome navigation icons.

Avoid:

- Illustrations.
- 3D renders.
- Abstract graphics.
- Heavy filters or duotones.
- Decorative borders around photos.
- Non-photographic hero art.

## Motion

Motion is quiet and utility-first.

- Use simple color and background hover changes.
- Search overlay and popovers can animate softly.
- Listing cards should not lift.
- Wishlist state can switch heart fill to Rausch.

