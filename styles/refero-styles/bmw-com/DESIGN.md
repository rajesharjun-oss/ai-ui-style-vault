# BMW.com Style Reference

> Automotive gallery wall on white canvas, where the interface steps back and sculptural product photography carries the color.

## Theme

Light.

BMW.com uses a quiet, luxury showroom language. The system has almost no decorative UI: white canvas, near-black typography, plain text navigation, full-width product imagery, and one dark footer band. Its premium feeling comes from restraint, whitespace, and a soft 300-weight display heading instead of heavy brand typography.

## Core Principles

1. Let photography be the color system.
2. Use typography and spacing as the primary interface.
3. Keep geometry squared at 0px radius.
4. Avoid shadows, borders, gradients, and accent colors.
5. Reserve the 60px light display style for one hero or section title.
6. Treat the footer as the only strong surface contrast moment.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Carbon | `#262626` | `--color-carbon` | Primary text, dark footer surface, heading color |
| Pure White | `#ffffff` | `--color-pure-white` | Page canvas, header background, inverted footer text |
| Fog | `#f1f1f1` | `--color-fog` | Quiet alternate section surface |
| Concrete | `#bbbbbb` | `--color-concrete` | Muted text, quiet dividers, secondary footer text |

## Typography

Use `BMWTypeNextLatin` when available. In product code, use `Inter`, `Neue Haas Grotesk`, or another restrained geometric sans fallback.

| Role | Size | Weight | Line Height | Use |
| --- | --- | --- | --- | --- |
| Display | 60px | 300 | 1.3 | One large centered section or page heading |
| Body | 18px | 900 | 1.3 | Strong brand or emphasis text only |
| Body small | 16px | 400 | 1.6 | Navigation, links, footer items, supporting copy |

Display typography should feel light and quiet. Do not bold the 60px heading. Body and navigation should remain plain and direct.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | compact |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 56px |
| Card padding | 24px |
| Element gap | 10px to 20px |
| Radius | 0px |

This system is square, flat, and precise. Use spacing to separate content instead of borders, cards, and elevation.

## Layout

Use a single-column vertical composition. Header content sits on a white canvas. Product images break out to full viewport width. Text sections return to a centered 1200px rail. The footer is full-width and dark.

Recommended rhythm:

1. Flat top navigation.
2. Full-bleed product image.
3. Centered 60px light display heading.
4. Centered inline text link.
5. Generous whitespace or a quiet Fog band.
6. Full-width Carbon footer.

Avoid sidebars, dense card grids, colorful CTA blocks, and complex app chrome.

## Components

### Top Navigation Bar

White background, no border, no shadow. Place the brand mark and tagline on the left. Put text links and a simple search icon on the right. Use 16px regular text in Carbon.

### Full-Bleed Hero Image

Edge-to-edge image with no overlay text, no rounded corners, no border, and no padding. The image is the showcase. Use dramatic product closeups with dark studio lighting, metal detail, and controlled contrast.

### Display Section Heading

Centered 60px light heading in Carbon. Keep line height tight at 1.3. Add one small centered inline link underneath after around 40px of space.

### Inline Arrow Link

Text-only action. Use a simple ASCII chevron or icon plus a 16px label. No pill, border, underline by default, filled background, or accent color.

### Dark Footer Band

Full-width Carbon background with white text. Inside, use a centered 1200px container and four simple text columns. Links are plain 16px regular text with modest row gaps.

### Language Switcher

Plain horizontal text links in the footer. Use no flags, badges, separators, borders, or selected-state chrome.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Canvas | `#ffffff` | Main page and header background |
| 1 | Subtle band | `#f1f1f1` | Optional quiet section background |
| 2 | Footer | `#262626` | Single strong contrast band |

## Elevation

Use no shadow elevation. Hierarchy comes from full-bleed imagery, empty space, type size, type weight, and surface contrast.

## Imagery

Use tightly cropped automotive or industrial product photography. The best images feel like sculptural artifacts: wheels, body panels, badges, grilles, glass, metal, and black studio backgrounds. Let blue-black metallic highlights and the object itself provide color.

Avoid lifestyle scenes, busy backgrounds, soft stock photography, interface overlays, and marketing badges on top of images.

## Do

- Use one 60px, 300-weight display heading as the signature type moment.
- Keep navigation and footer links as plain text.
- Make photography full-bleed and overlay-free.
- Use Carbon on white for almost all text.
- Keep all corners at 0px.
- Use the dark footer band as the main contrast surface.
- Use Fog only for subtle section separation.

## Don't

- Do not add accent colors, gradients, or colorful UI states.
- Do not round buttons, cards, badges, or images.
- Do not add shadows or elevation.
- Do not bold the display heading.
- Do not place UI controls over hero photography.
- Do not make CTA buttons unless the product requires a stronger action.
- Do not use the light display face for body text or small labels.

## AI Builder Notes

When implementing this style, start by removing UI decoration. If the layout starts to feel too plain, add better photography and more deliberate spacing before adding components. The premium signal is the absence of noise.
