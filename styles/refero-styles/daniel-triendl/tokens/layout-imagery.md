# Layout & Imagery

## Layout

Full-bleed page on a white canvas, content constrained to a max-width around 1440px and centered. The header is a single thin row: avatar + Rza wordmark on the left, two ghost pill buttons (Explore, Index) on the right. The body is a dense masonry/grid of illustration cards - mixed tall and wide cells packed tightly with small 20px gutters. Each card stacks image-on-top, title-and-tags below. A floating pill nav (Work / About / Contact) sits fixed at the bottom-center of the viewport over the grid. Some grid cells are repurposed as text blocks (About, Live stories) so the grid is a mix of artwork and editorial copy. Vertical rhythm is tight - sections do not alternate light/dark, the whole page stays on white.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#ffffff` | Full-page background, card base, floating pill fill |
| 1 | Plaster | `#f2f2f2` | Tag chips, pill nav resting state, soft highlight wash |

## Elevation

The system is intentionally flat. There are no shadows on cards, no elevation on thumbnails, no z-axis depth on the grid. The single permitted shadow is the subtle drop on the floating bottom pill nav, which exists only to lift that one element off the artwork beneath it. All other structure is communicated through 1px black hairlines and whitespace.

## Imagery

The site is an illustration portfolio, so imagery IS the product. The visual system shows large-format illustration thumbnails in a masonry/grid - each piece is a full-color editorial or cover-style artwork (characters, landscapes, abstract 3D shapes, line art). Treatments vary wildly by piece (flat color, gradient, line work, 3D render) because the portfolio showcases range. In the UI layer, the only recurring image is a small circular personal avatar. Images are displayed edge-to-edge in their grid cells with a 1px black hairline frame, no rounded masking beyond the 10px thumbnail radius, no overlap. Photography is absent - everything is authored illustration.
