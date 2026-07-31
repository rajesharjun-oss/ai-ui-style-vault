# Components

### Top Navigation Bar
**Role:** Site-wide persistent header

Full-bleed #000000 bar, ~48px tall, 16px horizontal padding. Three zones: left = 'Studio Oker' wordmark in NextBook 16px #ffffff; center = timestamp/date in NextBook 16px #a0a0a0 ('2758.22.57:55'); right = nav links (Work, Feed, Studio, Contact) in NextBook 16px #ffffff with 16px gaps, followed by a 2x2 grid expand icon. No background fill beyond black, no border-bottom - the bar blends into the canvas.

### Project Tile Card
**Role:** Grid cell in the work showcase

Aspect-ratio-locked tile (varies per tile, appears ~1:1, ~3:4, and ~4:3) with 0px radius. Content is either a brand mark on white (#ffffff background, black logo) or a full-bleed photograph. Tiles are separated by 16px gutters on a #000000 canvas. No border, no shadow, no padding - the edge of the photograph IS the edge of the card.

### Full-Bleed Red Panel
**Role:** Hero-scale statement tile (e.g. 'Think Big.')

Single tile spanning roughly one full grid column at large height, #000000 background, displaying oversized type in #e4002b. The text is NextBook weight 300, approximately 120-160px, set tight. A small red dot ( ) followed by 'Read more' in NextBook 400 16px #ffffff sits at the bottom-left with 16px padding. This is the system's only place where color shouts.

### Brand Color Swatch Panel
**Role:** A literal brand-system reveal inside a project tile

One tile is dedicated to a 6-stop pink-to-black gradient (#f5a5a5 #e85a5a #d42020 #7a0a0a #2a0606 #000000), split into vertical bars of equal width. The tile IS the gradient - no labels, no copy. Functions as a self-portrait of the brand's color DNA.

### Typography Specimen Tile
**Role:** A client's font system displayed inside a project card

White (#f5f5f5 or #ffffff) tile containing 'Circular Std' and 'Book Bold' labels in small caps, followed by 'AaBbCc' and '1234' in large display sizes. Used to show a brand's typographic identity at a glance. Zero radius, tight margins.

### Section Heading
**Role:** Top-of-section title for Feed, Studio, etc.

Left-aligned, NextBook weight 300 or 400, 80px, line-height 1.0, letter-spacing -1.6px, #ffffff on #000000. Sits with 120px margin-bottom to its content. The size commands the room; the weight keeps it from shouting.

### Studio Stat Block
**Role:** Compact label/value pairs in the About/Studio section

Two-column layout. Labels ('Established', 'Location', 'Employees', 'Clients') in NextBook 400 16px #a0a0a0. Values ('2018.08.05', 'Stavanger, Norway', '11', '66') in NextBook 400 16px #ffffff directly below, no gap. No borders, no boxes - typography does the structuring.

### Services List
**Role:** Vertical list of service offerings

Plain stack of strings - 'Brand strategy', 'Brand design', 'Digital experiences', 'Motion design', 'Spatial design' - each in NextBook 400 16px #ffffff with no bullets, no leading characters, line-height 1.25. Functions as raw copy, not a styled list.

### Project Showcase Card (Feed)
**Role:** Large format work card with image + caption

Full-width or half-width block, #000000 background, 0px radius. Image fills the upper portion (no padding, edge-to-edge). Below the image: client name in NextBook 400 ~24px #ffffff, then a short project description in NextBook 400 16px #a0a0a0, then a list of disciplines in 16px #a0a0a0. Caption block has ~16px padding. No border, no shadow - the photograph defines the card's boundary.

### Link with Red Dot
**Role:** Standalone call-to-action / read-more affordance

A 6px #e4002b circle followed by 16px text in NextBook 400 #ffffff. The dot is the only color element; the text is the only typographic element. No underline, no padding, no border - the dot does the work of a button without a button shape.

### Footer
**Role:** Page-bottom site info

#000000 background, 16px padding, 1px top border in #484848. Content in NextBook 400 16px #a0a0a0 (or #ffffff for the 'Studio Oker' mark). Minimal, quiet, no CTAs.
