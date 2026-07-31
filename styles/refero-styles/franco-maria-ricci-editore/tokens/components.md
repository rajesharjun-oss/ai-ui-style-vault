# Components

### Top Bar Navigation
**Role:** Primary site navigation

Single horizontal row, transparent over the vellum canvas. Logo monogram (circular emblem with serif letter) on the far left in #000000. Far right carries the wordmark "Franco Maria Ricci" in Bodoni 14px with the italic "Editore" subtitle in 12px beneath, followed by a thin-line shopping bag icon and a hamburger menu icon - both 16px, 1px stroke, no fill. No background fill, no border, no shadow. 40px vertical padding, 64px horizontal padding at the container level.

### Hero Headline Block
**Role:** Opening editorial statement

Left-aligned text block, 40% page width. Headline in Bodoni 42px, line-height 0.95, #000000. Sub-headline paragraph in Bodoni 16px, #000000, max-width ~320px. Followed by a bracketed call-to-action in Bodoni 14px with 1px #000000 bottom border: { ORDER NOW }. The opposite ~60% of the viewport is held for a large illustrative plate (the Art Deco portrait in the primary screenshot).

### Section Title with Gold Rule
**Role:** Section divider heading

Centered text in italic Bodoni 22px, #000000, followed by a 1px horizontal rule in #bc9c5c (Burnished Gold) spanning the full column width. Appears above each book-selection band (BEST SELLERS, OUR SELECTION, NEW RELEASES, FMR MAGAZINE). The gold rule is the system's only chromatic gesture and signals a new exhibition room.

### Three-Column Book Grid
**Role:** Product showcase

Three equal columns separated by 1px vertical rules in #000000. Each column has 40px internal padding and a #ffffff surface. Book covers sit centered with generous top/bottom whitespace; the cover itself carries the only imagery in the column. No card shadow, no border-radius, no hover effect - the book is the object, the grid is the gallery wall.

### Book Cover Plate
**Role:** Individual product object

Centered book cover image with 24px top margin from the column rule. No caption, no price, no add-to-cart button at the grid level - interaction is implied by the cover itself. Cover proportions are preserved; no cropping, no frames.

### Ghost Link / Editorial CTA
**Role:** Outlined action

Text link in Bodoni 14px, #000000, with 1px #000000 bottom border, 4px gap between text and rule. Active and hover states swap the border color to #bc9c5c (Burnished Gold) and shift the text to #bc9c5c. The bracketed variant - `{ ORDER NOW }` - wraps the label in literal curly braces as an editorial convention, not a styled border. No background fill at any state.

### Magazine Brand Block
**Role:** Branded section separator

Full-bleed horizontal band, height ~40% of viewport, with a #0a0a0a (Gallery Ink) surface. Left half holds a richly colored FMR magazine cover plate; right half centers the FMR wordmark in Bodoni 42px, white, with "MAGAZINE" set in Arial 12px, letter-spaced, directly beneath. Functions as a dark break in the otherwise all-light editorial scroll.

### Pagination Indicator
**Role:** Scroll progress marker

Bottom-right corner, Bodoni 14px in italic (or Arial 12px), #000000. Format: `2 / 5` flanked by thin arrow glyphs ( ) at 14px. No background, no border. Optional 1px #000000 divider above the counter, aligned to the page edge with 20px inset.

### Section Header Tab
**Role:** In-grid category label

Inline three-part label (e.g. I/o - BEST SELLERS - NEW RELEASES) split across the three-column grid: the active category in italic Bodoni 22px #000000, the inactive categories in roman Bodoni 22px at 40% opacity (#000000 at alpha 0.4). No underline on inactive items, 1px #bc9c5c underline only on the active label.
