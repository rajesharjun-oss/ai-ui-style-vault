# AI Implementation Prompt

Build a Kalstore(R)-inspired interface using this source-derived style bundle.

Reference site: https://kal-store.com
Theme: light
Category: E-commerce
North star: Paper atelier on a quiet morning. The interface is warm off-white, sparsely set, and lets one mustard accent and oversized editorial type do the talking.

Use these palette anchors:

- Paper White `#faf9f7` for Page canvas - warm off-white that mimics uncoated paper stock; the default surface behind everything
- Ink `#242424` for Primary text, icon strokes, and dominant border color. Slightly softened from pure black to sit comfortably on the warm canvas
- Felt Gray `#d3d3d3` for Hairline dividers, card borders, list separators - the structural neutral that holds the layout together without drawing attention
- Linen `#edecea` for Subtle surface elevation for nav backgrounds and hover states; slightly cooler than Paper White to create depth without contrast
- Parchment `#e0ddd7` for Warm-toned surface for body sections and secondary cards; introduces a faint paper-fiber warmth against the cooler Linen
- Slate `#727272` for Muted secondary text and subdued borders for de-emphasized content like timestamps and helper labels
- Ash `#8d9090` for Tertiary text and disabled-state borders; sits between Slate and Felt Gray in the neutral ladder
- Charcoal `#585a5a` for Navigation borders and medium-emphasis UI structure; a bridge between the near-black Ink and the mid-grays
- Pure White `#ffffff` for Badge fills, icon backgrounds, and the highest surface elevation - used sparingly to lift elements above Linen and Parchment
- Mustard `#f1ba35` for Primary action color - CTA buttons, nav accents, and badge highlights. A warm sunlit yellow that reads as a sticky-note moment against the monochrome layout
- Espresso `#30250b` for Dark accent paired with Mustard on badges and nav - provides a near-black complement that makes the yellow pop without using pure black
- Terracotta `#d26c46` for Editorial accent - appears in the typographic art palette and decorative product imagery. Rust-orange warmth that belongs in illustrations, not buttons
- Sage `#458e71` for Editorial accent - a muted forest green used in the typographic art palette. Decorative, not functional
- Cobalt `#3b59a3` for Editorial accent - deep ultramarine from the typographic art palette. The strongest chromatic statement in the decorative system
- Rust `#6c3c3c` for Editorial accent - dark brick red from the typographic art palette, echoing the warmth of Terracotta but grounded
- Sky Dust `#90abc8` for Editorial accent - a washed, chalky blue used in the typographic art palette. The lightest chromatic in the decorative system

Use these typography anchors:

- ABCDiatype `--font-abcdiatype` for The only typeface. A neo-grotesque editorial sans used at every register - 19px body copy, 25px section headings, and dramatic 71-140px display treatments with tight tracking. The wide weight range (400-500) keeps the system monovariational; hierarchy comes from size, not weight contrast.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 12px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary CTA Button (Mustard): Filled action button for purchases, subscriptions, and key conversions
- Ghost Navigation Button: Secondary navigation and text-style links
- Product Card: Individual product display in grids and featured sections
- Sold Out Badge: Status indicator for unavailable products
- Typographic Art Block: Full-bleed decorative section using stacked chromatic letterforms
- Newsletter Popup: Email capture overlay triggered after page interaction
- Sticky Navigation Bar: Top-level site navigation that persists on scroll
- Price Display: Product pricing with optional original/sale price strikethrough
- Hero Lifestyle Image: Full-bleed editorial photography in the primary hero section
- Sale Banner Section: Promotional call-to-action band with headline and CTA
- Product Detail Card (Calendar): Featured product showcase with large image and metadata
- Email Input Field: Single-line text input for newsletter and form capture

Do:

- Use #f1ba35 Mustard exclusively for filled action buttons - it is the only chromatic that functions as a CTA in this system.
- Set display type at 71-140px ABCDiatype with -0.04em to -0.02em letter-spacing for editorial impact; the tight tracking is what makes the oversized type feel intentional rather than bloated.
- Use 8px border-radius for cards, buttons, and inputs; reserve 4px for badges and icon containers.
- Use 1px #d3d3d3 Felt Gray borders for structural definition; avoid using box-shadow as the primary separator.
- Set body text at 19px ABCDiatype weight 400 with 1.30 line-height - the 19px body size is larger than typical e-commerce (usually 14-16px) and signals editorial intent.
- Use the chromatic accent palette (#d26c46, #458e71, #3b59a3, #6c3c3c, #90abc8) only in editorial art blocks and illustrations - never in functional UI elements like buttons, links, or status indicators.
- Maintain 64px minimum section gaps to preserve the spacious, magazine-like reading rhythm.

Avoid:

- Don't use chromatic colors for functional UI - no green for success, no red for error, no blue for info. The system is monochrome with one warm accent.
- Don't apply box-shadows with opacity above 10% - the elevation philosophy is paper-lift, not digital pop.
- Don't use bold weights (600+) - the system maxes out at weight 500; hierarchy comes from size, not weight contrast.
- Don't use pure black (#000000) for text or backgrounds - use #242424 Ink to maintain warmth on the paper-tone canvas.
- Don't add gradients - the raw data shows zero gradient usage; the system is entirely flat surfaces.
- Don't use button padding larger than 8px vertical - the compact 6x8px button size is a signature; larger padding would break the restrained feel.
- Don't place Mustard (#f1ba35) on large filled surfaces - it works as a button fill or badge, not as a section background.

Source prompt cues:

**Quick Color Reference**
- Canvas: #faf9f7 (Paper White)
- Text/Border: #242424 (Ink)
- Hairline: #d3d3d3 (Felt Gray)
- Surface: #edecea (Linen)
- primary action: #f1ba35 (filled action)
- Dark surface: #30250b (Espresso)

**Example Component Prompts**
1. Create a product card: #faf9f7 background, 1px #d3d3d3 border, 8px radius, 12px padding. Product image fills top. Title in ABCDiatype 16px weight 400 #242424. Price in ABCDiatype 14px #727272. Optional Mustard (#f1ba35) sold-out badge top-left with 4px radius and 12px text.
2. Create a hero section: full-bleed lifestyle photograph left (60% width), dark typographic art block right (40% width) with stacked chromatic letterforms in #d26c46, #458e71, #3b59a3, #6c3c3c, #90abc8. No overlay text - the image is the content.
3. Create a Primary Action Button: #f1ba35 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
4. Create a newsletter popup: #30250b dark surface, #ffffff text, 19px ABCDiatype headline, 14px body copy, 12px fine print. Email input with #faf9f7 background and 8px radius. Mustard (#f1ba35) subscribe button. Fixed bottom-right with x close in top-right.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
