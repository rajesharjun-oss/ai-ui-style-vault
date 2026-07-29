# Factory - Design Reference

> Stark black engineering interface with flat instrument panels, tight Geist typography, and small
> orange/green data accents reserved for status and metrics.

## Theme

Factory reads like a midnight terminal command center. The interface is almost entirely monochrome:
black canvas, warm gray text, hairline borders, and a single high-contrast light card or product frame
used as the main figure against the dark ground.

The system should feel technical, still, precise, and anti-decorative. It creates hierarchy through
figure/ground contrast, spacing, tight typography, and thin lines rather than gradients, shadows, glows,
or saturated UI chrome.

## Core Visual Rules

- Keep the page canvas dark, usually `#101010`.
- Use light cards or product frames sparingly as the primary contrast move.
- Use orange and green only for live status, build states, charts, and metric signals.
- Keep buttons neutral; do not turn accent colors into CTA fills.
- Use low radii: `3px` controls, `10px` cards, `20px` large panels.
- Prefer flat borders and negative space over shadow-based elevation.
- Use Geist for most UI and Geist Mono for terminal/instrument labels.

## Quick References

- **Canvas:** `#101010`
- **Raised dark surface:** `#1d1a18`
- **Hairline border:** `#3d3a39`
- **Muted text:** `#8a8380`
- **Primary text / light card:** `#eeeeee`
- **High light fill:** `#fafafa`
- **Signal orange:** `#ee6018`
- **Metric green:** `#a0ca92`
- **Page max width:** `1200px`
- **Section gap:** `96px`
- **Card padding:** `24px`
- **Element gap:** `24px`
- **Control radius:** `3px`
- **Card radius:** `10px`

## Implementation Notes

Start from `code/css-variables.css` or `code/tailwind-v4.css`. Build reusable primitives for neutral
buttons, ghost links, light surface cards, dashboard frames, metric tiles, status pulses, trust strips,
feature rows, and a column-based footer.

For original work, keep the system logic but replace source-specific brand marks, screenshots, names,
copy, and exact compositions.

