# Layout & Imagery

## Layout

Max-width 1200px centered canvas on a pure white background. Pages follow a vertical scroll rhythm: hero split (text-left, device-right) centered serif section heading feature card grid (asymmetric, 1-2 cards per row) article feed (4-column card grid). Section gaps are 80px, generous and consistent. No alternating dark bands, no full-bleed imagery. Navigation is a single top bar with no sticky behavior. The layout reads top-to-bottom like a magazine spread: open white space, serif headline, sparse content, repeat.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#ffffff` | Page background - the sheet |
| 1 | Card | `#ffffff` | Content cards on the same white sheet, defined by 1px warm-taupe borders |
| 2 | Recessed | `#ededed` | Badge and inactive panel backgrounds |

## Elevation

- **Navigation pill:** `rgba(0, 0, 0, 0.05) 0px 1px 2px 0px, rgba(0, 0, 0, 0.02) 0px 0px 4px 0px`
- **Active/focused nav item:** `rgba(61, 122, 245, 0.4) 0px 0px 0px 1px inset, rgba(207, 222, 252, 0.3) 0px 1px 0px 0px inset, rgba(10, 71, 194, 0.2) 0px -1px 0px 0px inset, rgba(13, 89, 242, 0.15) 0px 0px 16px 0px`
- **Article card hover:** `rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px`

## Imagery

Photography is absent - Paragraph uses a literary publication visual language built entirely from typography and layout. The only photographic content is user-uploaded cover images on article cards, which the system treats as raw content rather than styled brand imagery. The sole product visual is a phone-frame mockup in the hero containing a simulated app UI with a vibrant blue-to-magenta gradient banner (user-generated content, not brand asset). Icons are minimal line-art in Ink Black at 16px stroke. No decorative graphics, no abstract shapes, no 3D elements. The system trusts whitespace and serif headlines to do all atmospheric work.
