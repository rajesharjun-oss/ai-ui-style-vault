# Components

### Announcement Bar
**Role:** Top-of-page promotional strip

Full-bleed solid Fidele Blue (#1664eb) background, white text, 1px white internal border. Centered single-line text in BaselGrotesk Book 14px, line-height 1.5, tracking +0.88px. Height ~40px. Acts as the loudest brand-color beat on every page.

### Top Navigation Bar
**Role:** Primary site navigation

Paper White (#f8f7ef) background, no border. Three-column flex: left nav links (Shop, About, Journal) in Fidele Blue 14px; center wordmark 'Fidele Editions' where 'Fidele' is blue and 'Editions' is Press Black; right cluster (language selector, search icon, cart icon) in Fidele Blue. Nav links have 5px horizontal padding. Height ~56px. No dropdown menus visible - flat, link-only.

### Hero Image Block
**Role:** Full-bleed editorial photograph

Edge-to-edge image with no rounding and no overlay. Sits directly below the nav and announcement bar. May have a single-line headline in BaselGrotesk 32-37px Fidele Blue overlaid on the Paper White above the image, left-aligned with 14-24px padding.

### Product Card
**Role:** Grid tile for a book, zine, t-shirt, or blanket

Square product image, 1px Pure White (#ffffff) border, no rounding, Card Cream (#e2e2df) background behind image for letterboxing. Below image: product title in Press Black 14px, artist name in Press Black 14px, price right-aligned in Press Black 14px. 16px column-gap in the grid. Title and price sit on the Paper White canvas, not in a card surface.

### Product Grid
**Role:** Shop 'What's on: Latest' listing

5-column grid on desktop, uniform product cards, 16px column-gap, 32px row-gap. Section heading 'What's on: Latest' in BaselGrotesk 37-41px Fidele Blue above the grid, left-aligned with 24px left margin. No card backgrounds behind individual tiles - the grid floats on Paper White.

### Outlined Action Button
**Role:** Primary interactive control

1-2px solid Fidele Blue border, transparent or Paper White fill, Fidele Blue text in BaselGrotesk Book 14px, padding 12px 24px, 4px corner radius. No fill state - this system uses outlined actions, not filled ones. Hover: invert (blue fill, white text).

### Photo Strip Section
**Role:** Full-bleed editorial image band

Edge-to-edge row of 4-6 images, each ~16.6% width, no gaps, no rounding, no captions. Functions as a visual divider between content blocks. Sits on Paper White with no card treatment.

### Split Feature Section
**Role:** Two-column image+content block

50/50 split: one side holds a single large element (the giant blue asterisk SVG, or a photograph), the other holds supporting content. No background change between columns, no border - separation is purely spatial. The asterisk itself fills ~60% of its column as a 200-300px solid Fidele Blue shape.

### Giant Asterisk Mark
**Role:** Brand signature / decorative element

Solid Fidele Blue SVG of a 6-point asterisk (~200-300px), no stroke, no shadow, no rounding. Functions as a logo, section anchor, and visual punctuation - the system's most identifiable shape. Always rendered on Paper White, never on blue.

### Product Detail Link
**Role:** Title link under a product image

Press Black 14px BaselGrotesk Book, no underline, hovers to Fidele Blue. Sits flush-left under the image; price uses the same style, flush-right in a separate flex child.

### Language Selector
**Role:** Top-bar utility

Fidele Blue 14px text 'English' with a small downward chevron icon in Fidele Blue. No dropdown chrome visible - the control is text-only with the caret as the affordance.

### Icon Button (Search/Cart)
**Role:** Top-bar utility

Fidele Blue line icon (search lens, cart bag) at 20px, no button background, no border. Tap target extends to ~40px via padding. Icons are stroke-only, 1.5px weight, no fill.

### Footer Rule Line
**Role:** Section divider

1px solid Press Black or 60% Press Black horizontal line spanning the full content width, used to separate the product grid from the photo strip. 32-64px vertical margin on each side.
