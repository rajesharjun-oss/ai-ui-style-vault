# Components

### Playing Card (Core Content Unit)
**Role:** The fundamental content container - white rectangle with black text, used for both product cards and content blocks

White (#ffffff) background, 13-20px border-radius, 2px black (#000000) inset border, 20px padding. Black text at weight 800. Functions as both literal product imagery and as the site's content card metaphor. When used as decorative background elements, cards are rotated at various angles and offset to create a scattered-table composition.

### Outlined Pill Button (Primary)
**Role:** Main action button on dark backgrounds

Transparent fill on #000000 surface. White (#ffffff) 2px border, 38-64px border-radius (pill shape). Text: Helvetica Neue LT weight 800, 14-16px, #ffffff. Padding: 12px vertical, 32px horizontal. The 2px inset shadow creates the border - no stroke property used. Sits as a physical object, not a flat UI element.

### Outlined Pill Button (On Light)
**Role:** Action button on white card surfaces

Transparent fill on #ffffff surface. Black (#000000) 2px inset border, 38-64px radius. Text: #000000, weight 800, 14-16px. Same padding and geometry as the dark variant - only the color polarity inverts.

### Bordered Accent Card
**Role:** Featured card with chromatic border for emphasis

White or transparent fill with 2px border in one of the three brand accent colors (Signal Red #fe2f2f, Royal Violet #7333f1, or Antique Gold #d7b73b). 13-20px radius. Used to draw the eye to specific cards in the scattered background or to highlight featured content.

### Pastel Card
**Role:** Colored playing card surface used in the scattered background composition

Filled card with one of the seven accent surface colors (Lemon, Lavender, Cobalt, Sky, Bubblegum, Mint, Tangerine). 13-20px radius, black text at weight 800. Functions purely as decorative atmosphere in the card-scatter background pattern.

### Cookie/Modal Dialog
**Role:** Overlay consent interface

Centered on the page with a darkened scrim behind. Black (#000000) background, white text, 13-20px radius. Contains a bold heading ("Cookie Settings"), descriptive body copy, checkbox controls, and a row of outlined pill buttons (Accept All / Reject All / Confirm My Choices). The dialog itself follows the card aesthetic - it looks like a card dealt face-up on the table.

### Top Navigation Bar
**Role:** Site header with brand and nav links

Transparent or dark (#000000) background, white text. Brand name "Cards Against Humanity" at left in weight 800, ~24px. Nav items (Shop, About) at right with small dropdown carets. Minimal - no background fill, no border-bottom. Sits cleanly on the dark canvas.

### Section Display Heading
**Role:** Hero-level typography for section openers like "Buy the game."

Helvetica Neue LT weight 800, 55-80px, line-height 0.98-1.05. Color inverts by section: white on dark sections, black on light sections. Extremely tight leading at this scale - words stack into an impactful block. No letter-spacing manipulation.

### Checkbox Control
**Role:** Form input within the cookie settings dialog

Small square checkbox (~16-18px), 2px white border on the dark dialog surface. Unchecked state is transparent fill; checked state shows white fill with black checkmark. Sits inline with label text at 14px weight 400.

### Badge / Tag
**Role:** Small accent labels, potentially for product variants or tags

One of the three brand accent colors as 2px border (Signal Red, Royal Violet, Antique Gold), transparent or matching-tinted fill. 38px border-radius (pill). Text in matching color, weight 800, 12-14px. Padding: ~10-20px horizontal.
