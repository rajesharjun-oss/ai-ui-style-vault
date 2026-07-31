# Layout & Imagery

## Layout

Two-column asymmetric editorial grid with full-bleed outer margins and no centered constraint. The left column holds the wordmark and large project tiles; the right column holds additional project tiles, the agency statement, and the vertical running text pinned to the far-right edge. Images within the grid are intentionally offset vertically - a tile on the left may start at 200px from top while its right-column neighbor starts at 80px - creating a staggered z-pattern rather than a rigid table. The nav bar sits at the very top with no sticky behavior and no background fill. Content flows top-to-bottom as a single continuous scroll with no section dividers, no alternating background bands, and no contained max-width wrapper - the page breathes outward to the viewport edges. The overall rhythm is slow and gallery-like: one case study per viewport-height, large image, then title block, then breathing space.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 1 | Vellum Canvas | `#f2f2f2` | The page itself - a warm off-white that reads as paper stock rather than digital background. Everything floats on this surface with no card containers or elevated panels. |
| 2 | Ink Surface | `#000000` | Rare dark inversions for full-bleed campaign sections or video containers where the artwork demands a black surround. |

## Elevation

The design system has zero elevation. No shadows, no border-radius, no stacked z-axis. Every element lives on the same flat plane on the Vellum canvas - the only depth comes from the natural overlap of large positioned images, which creates perceived layering without any CSS shadow. This is a deliberate anti-SaaS choice: the page behaves like a printed gallery catalog where flatness signals editorial authority.

## Imagery

Imagery is the entire color system. The site hosts large, high-resolution CGI renders and product photography (crystal formations, metallic objects, liquid simulations, branded consumer products) that carry saturated violets, pinks, greens, and golds - colors that never appear elsewhere in the UI. Images are always sharp-edged rectangles (no radius, no masks, no duotone treatment), presented at native resolution without cropping overlays. The visual rule: the more vivid the artwork, the more monochrome and silent the surrounding UI must be. No illustrations, no icon system beyond simple glyphs, no abstract graphics - the case study renders ARE the visual identity.
