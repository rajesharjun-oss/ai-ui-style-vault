# Components

### Bordered Cell
**Role:** Fundamental layout unit - replaces cards/sections with hard-edged grid cells

White (#ffffff) background, 2px solid #292929 border on all sides, 0px radius, variable internal padding (commonly 43px top/bottom and 45px left/right for heading cells, 20px for content cells). This is the dominant container - every section, card, and panel uses this pattern instead of shadows or fill colors.

### Outline Button
**Role:** Primary interactive - text-style outlined action

Transparent background, 1-2px #292929 border, 0px radius, padding 0px 20px vertically centered (text-baseline alignment), text in #292929 at 12-14px S-Condensed weight 500 uppercase with +0.1em tracking. Buttons sit on grid lines and inherit the rectilinear grid rather than floating above it.

### Text Link
**Role:** In-flow navigation and reference link

No border, no background, #292929 text at 12px S-Condensed weight 300 uppercase, +0.2em tracking, 20px horizontal padding. Examples: EN/JP language toggle, ABOUT tag, Pre-order label.

### Inverse Text Button
**Role:** Highlighted action - white text on dark surface

#292929 or #000000 background, #ffffff text, 0px radius, no border, 12px S-Condensed uppercase. Used for active/selected nav states and inverse actions on dark cells (e.g., the 'MONO X7' label on the product image cell).

### Underline Input
**Role:** Single-line form field - brutalist minimal

White (#ffffff) background, 1px #000000 bottom border only (no full border), 0px radius, padding 8px 0, #000000 text. The hairline-bottom-only treatment replaces boxed inputs - text sits directly on the page grid.

### Display Headline
**Role:** Hero and section-defining copy

NH weight 300 at 43px, lineHeight 1.34, letter-spacing -0.02em (-0.86px), #292929. Large size with whisper-weight and tight tracking is the system's signature - anti-bolding, editorial register.

### Uppercase Label
**Role:** Section/metadata tag (e.g., ABOUT, services)

S-Condensed weight 400-500 at 12px, lineHeight 1.34, uppercase, letter-spacing +0.1em (+0.12px), #292929 on white or #ffffff on #292929 inverse. Functions like museum plaque text - identifies what each cell contains.

### Editorial Caption
**Role:** Rotated/aspirational taglines wrapped around imagery

S-Condensed or NH at 12-16px, #292929, often rotated or wrapped in a circle as decorative SVG text. The 'Digital canvas that elevates a space with the ease of...' treatment is a signature pattern.

### Vertical Sidebar Label
**Role:** Page-edge rotated text - brand/category markers

S-Condensed weight 300 at 12px, rotated 90 on the right edge of the page, #292929, uppercase, tracking +0.2em. Marks vertical navigation categories (Illustration, Creative Coding, Web Experiments, etc.).

### Product Hero Image
**Role:** Full-bleed product photograph as centerpiece

Renders without frame/border inside its grid cell, 0px radius, sits on pure white background, no shadow or mask - the product is shown raw within the bordered cell, not lifted off it.

### Footer Bar
**Role:** Copyright and utility nav row

Single horizontal row across page width, 2px top border #292929, 12px S-Condensed uppercase content with +0.2em tracking, 20px vertical padding, white background. Examples: '(C) FRM Inc. 2026 SHOP CONTACT PRESS CORPORATE'.

### Dark Inverse Cell
**Role:** Occasional dark surface for contrast

#292929 fill, #ffffff text and borders, 0px radius, 2px #292929 outer border (visually seamless to adjacent cells). Used sparingly for inverse panels and product overlay labels.
