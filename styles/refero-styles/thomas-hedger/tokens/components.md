# Components

### Top Navigation Bar
**Role:** Sticky primary header spanning full viewport width

White background, 3-column flex layout: left-aligned 'THOMAS HEDGER' at 26px Diatype Variable 700, center-aligned 'CONTACT' at 26px Diatype Variable 500, right-aligned cluster of three icons (Behance, Instagram, cart) at 26px. All nav text is uppercase. No border, no shadow, no background fill - sits directly on canvas white.

### Portfolio Grid Tile
**Role:** Single project image cell in the 3-column mosaic

Full-bleed image contained in a rectangle with 3px internal padding and a 1px #000000 border. No border-radius. Images are flush against each other - no inter-tile gap visible at viewport scale. Each tile owns its own aspect ratio; the grid is masonry-like, not uniform.

### 3-Column Mosaic Grid
**Role:** Page-level layout for the portfolio body

Three equal-width columns extending edge-to-edge, no max-width container. Tiles stack vertically within each column. The grid is the page - there is no surrounding wrapper, no margin, no padding outside the tiles.

### Social Icon Link
**Role:** Utility icon in the top-right of the nav

Behance glyph, Instagram glyph, and shopping cart glyph rendered as inline SVG or icon font at 26px in #000000. No background, no border, no hover state styling visible - the link is the icon itself.

### Footer
**Role:** Minimal page-end credit line

Centered single line: '(C)Thomas Hedger 2026' on the left and 'Thanks for looking ' on the right, both at 9px Diatype 400 in #000000. Sits directly on canvas white with no separator above it - the grid simply ends.

### Nav Text Link
**Role:** Uppercase navigation label

26px Diatype Variable 500, #000000, uppercase, no underline, no hover decoration. The link and the text are indistinguishable - type is the interface.
