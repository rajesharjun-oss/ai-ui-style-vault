# Layout & Imagery

## Layout

Full-bleed single-page layout: the tournament bracket spans the entire viewport width with no max-width container, organized as a symmetric double-elimination tree radiating from a central final match. The left half shows one side of the bracket, the right half mirrors it, and the center column holds the final with the 'VS' separator and date. The page reads as a single horizontal diagram rather than a scrolled stack of sections. Navigation is a thin top bar with two text tags (GROUP STAGE, LIVESTREAM) flanking the centered UNISWAP CUP wordmark. Below the fold, rounds stack vertically with consistent 8px gaps and 1px connectors. The entire layout is a grid: no cards, no padding buffers, no breathing room beyond what the bracket geometry requires.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 1 | Canvas | `#ffffff` | Full-bleed page background - the white field on which the bracket is drawn |
| 2 | Blush Panel | `#fef4ff` | Soft pink-tinted surface used behind highlighted match cards or accent zones - a whisper of the brand pink |
| 3 | Wire | `#f2f2f2` | Not a surface per se but the dominant structural color - used for hairline borders, connectors, and grid scaffolding at 660+ instances |

## Elevation

The design system is entirely flat - no shadows, no gradients, no blur. Depth is created exclusively through color contrast: filled black and pink nodes sit on the white canvas and read as elevated by their chromatic value alone. This diagrammatic flatness is a signature choice: the interface presents itself as a printed tournament chart, not a software application.

## Imagery

No photography, no illustration, no decorative imagery. The visual language is pure typographic and diagrammatic - team logos appear as small monochrome glyphs inside black squares, scored digits are typeset in monospace, and the bracket itself is drawn with 1px rules. The only graphic element is a faint concentric circle behind the final match (the 'pitch'), drawn in a hairline gray. Iconography is reduced to single-letter or two-letter abbreviations inside filled squares. Density is text-and-structure-dominant; visual space is occupied by the bracket geometry, not by images.
