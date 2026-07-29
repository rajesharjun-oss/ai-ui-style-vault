# Components

### Top Navigation Bar
**Role:** Persistent global navigation

Single-row header: logo ('artu' lowercase, weight 400, 18-20px, black) at the left edge, then PRODUCTS, STORES, ABOUT, NEWS, CONTACTS in all-caps at 400 weight with 0.022em tracking, separated by commas not pipes. Right edge: EN, CART (0), MENU, same weight and case. No background fill, no border, 17px padding-top, 32px column-gap between items, sits directly on white.

### Full-bleed Hero Image
**Role:** Opening viewport statement

Edge-to-edge product photography with no caption, no overlay, no button. 0px radius, no border, spans full viewport width. The image IS the hero - the only frame is a 1px black hairline (border-bottom on the section) separating it from the next block.

### Editorial Image Grid
**Role:** Scrolling product gallery

Asymmetric multi-column layout mixing 1:1, 3:4, and 2:3 ratio product shots at varying sizes (roughly 3-4 columns, images sized 40-55% of viewport). White gutters between images, no captions or titles, 0px radius, no borders. Composition feels curated, not gridded.

### Hairline Divider
**Role:** Section separator

1px solid black (#000000) horizontal rule, full-width or content-width, used between major page sections. Carries the visual structure that padding and gaps do elsewhere.

### Decorative Red Border
**Role:** Editorial graphic accent

Thin red (#ff1313) stroked lines used sparingly inside content blocks and around icons - a graphic mark, not a container. Contrast is intentionally below WCAG; it exists to be seen as a line, not read as text.

### Carousel Arrows
**Role:** Image slider controls

Two simple black arrows ( ) at 18-20px, positioned bottom-right of the hero image block, on the white margin between the image and the hairline divider. No circle, no fill - just the glyph in #000000 at 1px stroke weight.

### Lime Footer Band
**Role:** Page terminal / site footer

Full-width band filled #d7ff66, no text inside, acts as a colored wall that closes the page. Sits below all content, height set by footer padding (~24-32px). The vivid green is the only color that occupies real estate in the layout.

### Footer Link Row
**Role:** Secondary navigation

If present, sits just above the lime band: all-caps, 400 weight, 18px, comma-separated links in #000000 with 29-37px margin-bottom between rows. Inherits the nav's all-caps typographic system.

### Image Thumbnail Link
**Role:** Product teaser

Unframed product image, 0px radius, optional 1px black border, no caption beneath. Behaves as a visual link in a gallery - the image is the affordance, not a button.
