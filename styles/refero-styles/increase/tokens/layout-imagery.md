# Layout & Imagery

## Layout

Max-width 1200px centered container with a 80-96px section gap between major bands. The hero is a split composition: left half holds the 90px headline, subtext, and two-button cluster; right half holds the dual-card visual stack (dark code card below, white form card above, both with a subtle 12px offset). Below the hero sits a centered trust-logo band, then a centered heading plus 4x2 product feature grid on Fog canvas, then alternating white/Fog content bands. Navigation is a single sticky top bar with a separate chartreuse announcement strip above it. Sections are separated by background-color alternation rather than dividers - vertical rhythm comes from canvas color, not rules.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Page Canvas | `#edf0f2` | Warm off-white field that holds all content sections; provides the neutral backdrop against which white cards and the chartreuse announcement bar gain their contrast. |
| 1 | Card Surface | `#ffffff` | Pure white for product cards, feature panels, nav, and inputs - the layer that floats above canvas with subtle tinted shadow. |
| 2 | Code Surface | `#0d1726` | Deepest surface in the system, used exclusively for code blocks and terminal demos; syntax colors (mint, blue, chartreuse) pop against it. |
| 3 | Announcement Surface | `#e4ff33` | Single-purpose full-bleed strip for time-sensitive messaging; the only surface in the system with native chromatic energy. |

## Elevation

- **Cards (standard):** `0px 6px 8px 0px rgba(12, 25, 39, 0.03), 0px 18px 22px 0px rgba(12, 25, 39, 0.09)`
- **Cards (elevated/feature):** `0px 6px 8px 0px rgba(12, 25, 39, 0.05), 0px 16px 20px 0px rgba(12, 25, 39, 0.06), 0px 50px 60px 0px rgba(12, 25, 39, 0.1)`
- **Buttons:** `0px 1px 3px 0px rgba(0, 0, 0, 0.1), 0px 1px 2px -1px rgba(0, 0, 0, 0.1)`

## Imagery

Imagery is sparse and product-driven. The hero is dominated by two UI cards (dark code block, light form) rather than photography, with a single 3D geometric gradient block floating behind - angular, faceted, no rounded edges or soft glows. Feature sections use iconography (mint-stroke line icons in tinted squares) rather than screenshots or photos. The trust band is a row of monochrome navy wordmarks. No lifestyle photography appears anywhere - the visual language is deliberately diagrammatic, closer to a financial terminal than a consumer fintech.
