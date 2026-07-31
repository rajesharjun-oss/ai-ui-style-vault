# Components

### Top Navigation Bar
**Role:** Persistent header across all sections

Transparent on the black hero, Paper on light sections. Left: small monogram logo (32px square, Obsidian or Paper fill). Right: 2-4 text links (FAQ, Agenda) at 16px Figma Sans Text weight 400, tracking 0.03em. 16px horizontal padding, 20px vertical. No background fill, no border.

### Hero Outlined Register Button
**Role:** Primary action on the dark hero

Full-width on the hero, 56-64px tall. 1px Paper border, no fill, Paper text. 0px radius. Text at 18-24px Figma Sans Text weight 400, centered. On hover, fills to Paper with Obsidian text.

### Eyebrow Label
**Role:** Section pre-heading (VIRTUAL, SPEAKERS, REGISTER)

12-13px Figma Sans Text weight 400 or 600, uppercase via CSS, tracking 0.03em. Color is Ink on light sections, Paper on dark. Sits 16-24px above the headline.

### Display Headline
**Role:** Section hero titles ('Schema by Figma', 'Meet our speakers!', 'Join us virtually!')

Figma Sans Display weight 400, 56-86px, line-height 0.90-1.00, letter-spacing -0.02em. Ink color on light sections, Paper on dark hero. No max-width constraint - fills available column.

### Geometric Mural Banner
**Role:** Decorative full-bleed section divider between hero and content

Full viewport width, ~200-300px tall. Flat 2D art: circles, rectangles, hexagons, chevrons in saturated palette (indigo #4a4afc, lavender #b8b3ff, teal #c7f8fb, maroon #7a2e2, orange #ff6b2c, emerald #24cb71, yellow #ffe74a). No gradients, no shadows. Edges are hard/rectilinear where blocks meet the canvas.

### Speaker Portrait Card
**Role:** Speaker in the grid

Square portrait image, 0px radius, fills a 4-column grid. Each portrait sits on a solid background color (mint, emerald, indigo, lavender, orange, yellow). Below: name in Figma Sans Text weight 600 at 18px, title/role in Figma Sans Text weight 400 at 16px - both in Ink. 24px gap between portrait and text, 48px between cards vertically.

### Event Status Notice
**Role:** Inline status banner ('Event ended')

Centered or right-aligned block. Small triangular warning icon (~24px, Ink fill) above label. Label in Figma Sans Text weight 600 at 18-24px, subtext at 16px weight 400. Sits on the cyan Mint Wash band.

### Full-Bleed Color Section
**Role:** Horizontal content band with colored background

Edge-to-edge, ~200-400px tall, Paper or Ink text depending on contrast. Internal padding 60px top/bottom, 24-48px left/right. No border, no radius, no shadow.

### Date/Time Metadata Block
**Role:** Event date and time under hero headline

Two lines: bold date (16-18px Figma Sans Text weight 600) above time range (16-18px weight 400). Inherit text color from section (Paper on dark hero). 8-16px gap between lines.

### Grid Section Header
**Role:** Section title block above card grid (e.g., "Meet our speakers!")

Eyebrow label + display headline, left-aligned. 24px gap between label and headline. Sits 48-60px above the grid.
