# Components

### Dark Pill Button (Primary Action)
**Role:** The only button style that matters - the system's single interactive punctuation mark

Filled with #1e1e1, white text in Soehne Mono 12px, 20px border-radius (distinctive squircle-pill, not full pill), 7px top padding + 8px bottom padding + 16px horizontal padding. Tracks tight at 0.3px letter-spacing. Label is always uppercase. No hover state changes color - it just feels like ink on paper.

### Ghost Outline Button
**Role:** Secondary action for less critical interactions

Transparent fill, 1px #1e1e1 border, #1e1e1 text in Soehne Mono 12px, 20px radius, 7-8px vertical padding, 16px horizontal padding. Shares the pill geometry with the dark variant.

### Section Kicker Label
**Role:** Tiny uppercase label that opens every content section like a magazine department header

Soehne Breit Buch 10px, weight 400, #1e1e1, letter-spacing 1.0px (0.1em), uppercase. Sits above headings with 10-12px gap. No punctuation. Examples of the pattern: 'TRANSFORMING SPACES', 'PROJECTS'.

### Editorial Display Headline
**Role:** The hero/cover headline that defines the page

Cardinal Fruit 132-180px, weight 500 at the largest sizes, #1e1e1 or #fbf9f3 (white-cream) when overlaid on photography. Letter-spacing -0.05em at 132-180px. Line-height 1.0 to 1.2. This is the only element allowed to be this large.

### Asymmetric Section Header
**Role:** Left-column header for split text+image sections

Cardinal Fruit 48px weight 500, #1e1e1, letter-spacing -0.025em. Sits above a body text block (Soehne Breit 14px, 1.5 line-height) with 20px gap. No horizontal rule - whitespace is the divider.

### Full-Bleed Hero with Overlay Type
**Role:** The page-opening canvas - atmospheric photography as backdrop, type as subject

Image fills 100vw x ~85vh, no border-radius, type overlays in light cream (#fbf9f3 or white) with a thin vertical divider line and downward arrow in #1e1e1e. No darkening overlay - the type sits on the raw image.

### Two-Column Image Grid
**Role:** Quick visual proof beneath introductory text

Two equal-width images side by side, 12-16px gap between them, zero radius, full-bleed within their column. Images are uncropped architectural/interior photography.

### Split Content Section (Text Left / Image Right)
**Role:** The primary content arrangement for project showcases and about sections

Two-column grid at roughly 40/60 or 35/65 ratio. Left column: kicker label, Cardinal Fruit heading, body text, pill button. Right column: large uncropped photography, zero radius. Background alternates between #ffffff and #fbf9f3. 100px vertical section padding.

### Minimal Navigation Header
**Role:** Persistent top bar - almost invisible by design

Sticky, white or transparent background, #1e1e1 elements. Left: small two-line wordmark logo (Soehne Breit 12-14px, stacked). Right: single hamburger icon. No nav links visible, no background bar - just floats on the page.

### Footer Single-Line
**Role:** Minimal page closure

Single line of metadata in Soehne Mono 12px, #1e1e1, tracking 0.6px. Left: project identifier or studio name. Right: small action link or credit. 32px bottom padding separates it from page edge.

### Scroll Indicator
**Role:** Vertical guide suggesting 'there's more below'

Thin 1px vertical line in #1e1e1, ~120px tall, centered, terminating in a small downward arrow (SVG). Centered in the hero, the only graphical element competing with the display type.
