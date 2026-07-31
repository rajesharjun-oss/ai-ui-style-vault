# Components

### Display Headline Block
**Role:** The page-defining typographic element - site title rendered as a monolithic shape

Helvetica LT Pro 400 at 137px, line-height 0.79, letter-spacing -0.05em. Color is Olive Ink (#4f503e) - always dark regardless of canvas color. Text fills 2-4 lines of full-bleed width at the top of the page. No line breaks are manually constrained; the type wraps naturally to create a dense rectangular block. Padding: 0px from edges. This block is the visual signature.

### Section Subtitle
**Role:** Short descriptive line that sits directly under the display headline

Helvetica LT Pro 400 at 21px, line-height 1.2, letter-spacing -0.05em. Olive Ink (#4f503e). Set as a single sentence in all-caps, full-bleed or near-full-bleed width. Acts as the typographic period after the display headline.

### Album Cover Tile
**Role:** Unframed square image in the content grid

1:1 aspect ratio, 0px border-radius, 0px border, no padding, no shadow. Sits directly on the canvas with no gap treatment - the colored field bleeds between tiles. Sizing scales with viewport but tiles are uniform within a row.

### Refresh Record Button
**Role:** The only interactive control - a small circular record/disc icon that triggers a full page color change

Olive Ink (#4f503e) icon on the canvas background. Small, top-right corner. Functions as both the CTA and a visual metaphor (vinyl record). 0px border-radius (sharp) or true circle depending on icon shape - the icon itself is a simple disc with a center dot.

### Rotated Side Label
**Role:** Vertical instructional text - tells the user the page mechanic

Set in Helvetica LT Pro 400 at 16px, line-height 1.6, letter-spacing -0.05em. Olive Ink (#4f503e). Rotated 90 (reads bottom-to-top). Positioned flush to the right edge of the viewport. Acts as a micro-copy label rather than a control.

### Outlined Action Border
**Role:** Chromatic border treatment for interactive elements (links, tags, light buttons)

1px border in Olive Ink (#4f503e). No background fill. Padding ~20px. 0px border-radius. Pairs with Olive Ink text. This is the only 'button' variant - the site never uses filled buttons because the canvas color would clash with any solid fill.

### Body Caption
**Role:** Small helper text used in metadata, tags, or footnotes

Helvetica LT Pro 400 at 16px, line-height 1.6, letter-spacing -0.05em. Olive Ink (#4f503e) when on the orange canvas; Paper (#ffffff) when on dark album tiles or dark canvas states.

### Subheading Link
**Role:** In-text or tag-style link element

Helvetica LT Pro 400 at 21px, line-height 1.2, letter-spacing -0.05em. Olive Ink (#4f503e) with 1px Olive Ink underline. No hover state change beyond opacity reduction. Behaves like a static text label.
