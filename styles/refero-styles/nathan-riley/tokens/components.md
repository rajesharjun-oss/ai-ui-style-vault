# Components

### Image Grid Tile
**Role:** Primary content unit - each cell of the mosaic

A 3D-rendered image or photograph filling its grid cell edge-to-edge. No padding, no border, no radius, no shadow. Tiles abut directly with 2px black gutter lines or hairline gaps acting as the only separation. The image is the surface - no container chrome.

### Central Name Card
**Role:** The artist's identity card anchored over the grid

Fixed-position card centered on the viewport with #e8c4c0 dusty-rose background and 38px padding all sides. Contains the display serif name at 238px weight 300-400 italic, line-height 0.80, letter-spacing -0.04em. Below: a bio paragraph at 14-16px weight 400, charcoal text, tight 1.10 line-height. A small 'PROFILE >' link in monospace-style caps at 12px. No border, no shadow, no radius - the color contrast alone separates it from the image grid.

### Pill Navigation Chip
**Role:** Social/contact link in the bottom bar

White (#ffffff) background, no visible border, 9999px border-radius for a fully rounded pill shape. Text is 12-14px weight 400 in uppercase tracking, black (#000000). Chips sit in a horizontal row with 6px gap between them. No fill state, no hover color shift evident - the pill shape and size do all the work.

### Profile Link
**Role:** Secondary text link inside the name card

Small uppercase or mono-style text at 12px, likely with a '>' or arrow glyph. Functions as a tertiary navigation affordance, styled as a text label rather than a button. No underline, no color change - spatial relationship to surrounding text is the only hierarchy cue.

### Masonry Grid Container
**Role:** Page-level layout structure

Full-bleed CSS grid covering the entire viewport. No max-width constraint, no centering, no margins. Image tiles arranged in a masonry-like pattern with varying row heights to accommodate different aspect ratios. Black 2px lines or minimal gaps form the grid lattice. The grid is the page - there is no header, no footer bar, no sidebar.

### Image Gutter Divider
**Role:** Hairline separation between grid cells

2px black (#000000) lines or minimal gap between adjacent image tiles. Functions as a gallery wall mount system - thin, structural, invisible until you look for it. No decorative role, purely organizational.

### Bio Description Block
**Role:** Text body inside the central name card

14-16px custom body serif, weight 400, line-height 1.10, color #393939 or #000000. Uppercase or small-caps treatment with -0.025em tracking. Reads as a credit line or exhibition wall text - compressed, label-like, not narrative prose. Max-width constrained within the card to maintain a narrow text column beside or below the oversized name.
