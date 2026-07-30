# Components

### Hero Product Spotlight
**Role:** Full-bleed product reveal section

White (#ffffff) canvas, no card chrome. Product name in SF Pro Display 80px weight 600 #1d1d1f, letter-spacing -1.2px, centered. Tagline in SF Pro Display 28px weight 600 #1d1d1f. Single product render centered with generous whitespace - minimum 160px vertical padding above and below. No borders, no shadows, no decorative elements.

### Primary Blue Pill Button
**Role:** Single primary action per section

Background #0071e3, white (#ffffff) text, SF Pro Text 17px weight 400, border-radius 980px (full pill), padding 12px 22px, no border. Used at most once per viewport; if present, it is the only filled button. Saturated blue against pure white creates immediate focal weight.

### Text-Link Button
**Role:** Secondary or tertiary action - Apple's default

Transparent background, text #1d1d1f or #0066cc, SF Pro Text 17px weight 400, with right-arrow character ( ) appended. Zero padding, zero border, zero radius. The arrow is part of the text, not an icon - it inherits color. This is the dominant button type on the site.

### Outlined Pill Link
**Role:** Tertiary navigation-style action

Transparent fill, 1px border #1d1d1f, text #1d1d1f, border-radius 32px, padding 8px 18px, SF Pro Text 14px weight 400. Used for compact inline actions like 'Ver el video' where a contained affordance is needed without color emphasis.

### Feature Card (White)
**Role:** Product or feature showcase panel

Background #ffffff, border-radius 28px, zero shadow, zero border. Padding 40px minimum internal. Often contains a single product image, 28px headline, and one text-link button. Relies on container background contrast (sits on #f3f6f6 or #e8e8ed parent) for visual separation.

### Feature Card (Tinted)
**Role:** Secondary feature panel with subtle surface tint

Background #fafafc or #f3f6f6, border-radius 28px, zero shadow, zero border. Identical typography to the white card - the tint is the only differentiator. Used to create gentle banding when stacking multiple feature cards vertically.

### Global Navigation Bar
**Role:** Persistent top navigation

Background #ffffff (or #161617 in dark mode), height 44px, SF Pro Text 12px weight 400 #1d1d1f/#313131 nav items, 44px line-height, letter-spacing -0.01em. Apple logo left, centered item list, search and bag icons right. Backdrop filter saturate(1.8) blur(20px) when scrolled. Hamburger open state reveals #fafafc surface.

### Section Header Block
**Role:** Editorial section title with optional inline link

Left-aligned headline at SF Pro Display 48px or 56px weight 600 #1d1d1f, letter-spacing -0.003em to -0.005em. Optional right-aligned text link (17px #0066cc) on the same baseline. No eyebrow, no kicker - the headline is the sole title element. Vertical spacing 60-80px from preceding section.

### Eyebrow Label
**Role:** Small uppercase or sentence-case category label above headlines

SF Pro Text 14px weight 600 #1d1d1f or #0066cc, letter-spacing -0.016em. Pairs with a 56px headline. No decorative bullet, no separator - typographic hierarchy alone.

### Inline Text Link
**Role:** Hyperlink within paragraph copy

SF Pro Text 17px weight 400, color #0066cc, underline on hover only (no persistent underline). Sits inline within body text; no button chrome.

### Price Block
**Role:** Starting price display

SF Pro Text 17px weight 400 #6e6e73 with 'Desde' prefix. No decorative currency symbol treatment - the euro sign is inline at the same size and color. Sits below the CTA, vertically close (~8px).

### Badge (New / Limited)
**Role:** Product freshness indicator

Transparent background, text color #b64400 (ember orange), SF Pro Text 12px weight 400 or 14px weight 600, zero padding, zero radius. Inline with product name. No pill shape - the word 'Nuevo' is naked typographic punctuation.

### Footer Band
**Role:** Bottom regulatory and link surface

Background #f3f6f6, full-width, generous padding (~40px vertical). Link lists in SF Pro Text 12px weight 400 #6e6e73, dividers between columns are absent - spacing alone separates columns. Fine print and legal in same size and color, no smaller variant.

### Floating Video Play Badge
**Role:** Play button affordance on video thumbnails

Circular #ffffff badge (~40px) with concentric ring border, containing a play triangle in #0066cc. Floats over a card or image. Zero shadow - the white circle against the image is the elevation.
