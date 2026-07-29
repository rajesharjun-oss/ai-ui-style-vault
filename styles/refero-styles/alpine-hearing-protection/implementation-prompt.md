# AI Implementation Prompt

Build a Alpine Hearing Protection-inspired interface using this source-derived style bundle.

Reference site: https://www.alpinehearingprotection.com
Theme: light
Category: E-commerce
North star: Sunlit Scandinavian editorial. A cinnamon-ink wordmark on warm cream paper, with one red exclamation - the rest is photography and generous whitespace.

Use these palette anchors:

- Cocoa Ink `#200e0e` for Primary text, filled action buttons, card text, icon strokes, card borders - warm near-black replaces pure black throughout, giving every label a roasted, tactile quality
- Signal Red `#ed212d` for Red decorative accent for icons, marks, and small graphic details.
- Canvas White `#ffffff` for Page background, nav text, button labels on dark surfaces - the neutral base all warm tones sit on
- Blush Cream `#f8f0ec` for Card surfaces, soft elevated sections, product detail backgrounds - the warm secondary layer beneath the white canvas
- Rose Stone `#f3e7e2` for Badge backgrounds, subtle card elevation, border tints on light cards - a step warmer than Blush Cream for tag/label contexts
- Apricot Wash `#fde3d6` for Decorative illustration panels, soft highlight washes on icons and product imagery backgrounds
- Warm Gray `#d2cfcf` for Hairline borders, dividers, input field outlines on neutral surfaces
- Deep Espresso `#202020` for Secondary card backgrounds for dark product variants - used sparingly as a near-black with slight warmth
- Sage Mist `#9ac9b5` for Product color swatch - specific earplug variant color, not a system-wide token
- Dusty Rose `#dbb0b3` for Product color swatch - specific earplug variant color, not a system-wide token

Use these typography anchors:

- Antarctica `--font-antarctica` for Sole typeface across all UI: navigation, buttons, product cards, body, and display headlines. Custom geometric sans with slight warmth in the terminals. Medium-weight (545) is the workhorse for body and UI; 600 carries CTAs and product names; 400 appears in secondary metadata. Headlines compress with -0.02em tracking to feel editorial rather than airy.
- GTStandard-M `--font-gtstandard-m` for GTStandard-M - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1280px.
- Section gap: 64px.
- Card padding: 15px.
- Element gap: 8px.

Build these component patterns where relevant:

- Red Brand Bar: Slim brand-identity header
- Guarantee Announcement Bar: Trust signal above the fold
- Hero Photograph Section: Full-bleed marketing hero
- Category Navigation Bar: Horizontal category selector
- Help Me Choose Pill: Outlined contextual action
- Product Card: E-commerce product tile
- Top Seller Badge: Product status tag
- Color Swatch Row: Product variant selector
- Star Rating Display: Social proof indicator
- Hero CTA Button: Primary filled action
- Advice Card: Editorial content tile
- Carousel Navigation Arrows: Horizontal scroll control

Do:

- Use Cocoa Ink (#200e0e) for all body text, icons, and borders - never use pure #000000 or charcoal grays; the warm undertone is the brand
- Apply 2.23px radius to every surface - cards, buttons, badges, inputs, images; sharp corners are non-negotiable
- Use Signal Red (#ed212d) only in three places: the brand bar, the guarantee bar, and product status badges - never on CTAs, links, or body text
- Compress display headlines to letter-spacing -0.02em (e.g. -0.84px at 42px) for editorial tightness; body and below stays at normal tracking
- Alternate white (#ffffff) and Blush Cream (#f8f0ec) section backgrounds to create rhythm without using shadows
- Center-align the category navigation row and the 'Help Me Choose' button - left-aligned navigation would break the print-catalogue feel
- Use full-bleed lifestyle photography (portrait crops, natural light, shallow DOF) for heroes and editorial sections; product-only shots on solid color backgrounds for the grid

Avoid:

- Do not add box-shadows to any component - elevation comes from background-color shifts, never from blur or offset
- Do not round corners beyond 2.23px - no pill buttons, no large radii; the near-sharp aesthetic defines the system
- Do not use Signal Red (#ed212d) for buttons, links, or hover states - it is brand-identity color, not an action color
- Do not introduce drop shadows, gradients, or glassmorphism - the design is deliberately flat and print-like
- Do not use the product color swatches (Sage Mist #9ac9b5, Dusty Rose #dbb0b3) as system-wide accent tokens - they are product variant colors only
- Do not center-align body paragraphs or use fonts other than Antarctica (or its substitute); the single-typeface discipline is what makes the system feel like one publication
- Do not use pure black (#000000) for text or icons - always use Cocoa Ink (#200e0e) to maintain the warm tonal harmony

Source prompt cues:

**Quick Color Reference**
- Text: #200e0e (Cocoa Ink)
- Background: #ffffff (Canvas White)
- Border: #200e0e or #d2cfcf (hairline)
- Accent: #ed212d (Signal Red - brand only)
- Surface: #f8f0ec (Blush Cream)
- primary action: #200e0e (filled action)

**Example Component Prompts**

1. *Product Card*: 2.23px border in #200e0e, no shadow. Square product image on a solid colored background filling the top 75%. Below: product name in Antarctica 600 16px #200e0e, feature line in Antarctica 400 13px #200e0e, 5-star rating in #200e0e with '394 reviews' in 13px, price in Antarctica 600 16px #200e0e. Card padding 15px. No hover lift.

2. *Hero Section*: Full-bleed lifestyle photograph (portrait crop, natural light, shallow depth of field). Bottom-left overlay: headline in Antarctica 500 42px white, letter-spacing -0.84px. Subhead in Antarctica 400 16px white at 90% opacity. Filled CTA below: #200e0e background, white text in Antarctica 500 14px, 2.23px radius, 12px 20px padding, right-arrow icon after label.

3. *Category Navigation Bar*: Centered single row of 7 text links, Antarctica 500 16px #200e0e, 40px horizontal gap between links, 64px vertical padding. No background, no borders, no active state styling. Ghost 'Help Me Choose' button centered below: 1px #200e0e border, 2.23px radius, transparent fill, label in Antarctica 500 14px #200e0e with right-arrow icon.

4. *Top Seller Badge*: Small rectangle in top-left corner of a product image. White background, 2.23px radius, no border. Label 'Top Seller' in Antarctica 500 12px #200e0e. Padding 5px 10px.

5. *Advice Section Card*: Full-width image (portrait photograph or coral line-art illustration on #fde3d6 background). Below image: title in Antarctica 600 18px #200e0e, body paragraph in Antarctica 400 14px #200e0e at 1.5 line-height. No card border, no background - the image is the container.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
