# AI Implementation Prompt

Build a Rains INT-inspired interface using this source-derived style bundle.

Reference site: https://www.rains.com
Theme: light
Category: E-commerce
North star: Nordic rain catalog on fog-gray paper.

Use these palette anchors:

- Fog `#efefef` for Page canvas, card surfaces, divider hairlines - the warm light gray that IS the page background
- Ink `#10100f` for Primary text, nav links, body copy, icon strokes - near-black with a barely-warm bias (never pure #000)
- Paper `#ffffff` for Card surfaces over the gray canvas, text on dark buttons, product image backgrounds
- Charcoal `#26292a` for Filled button background, active states, inverted UI surfaces - warm-tinted dark, never pure black
- Graphite `#40403f` for Secondary button fill, subtle dark UI accents
- Ash `#b3b3b2` for Muted helper text, tertiary metadata, inactive nav items
- Black `#000000` for Pure black for SVG icon fills and the occasional hard edge - functional, not brand
- Butter Cream `#fffb85` for Hero display text accent - the single chromatic voice on the page, used only on oversized seasonal headlines over photography

Use these typography anchors:

- EuropaGroNr2SH `--font-europagronr2sh` for Headings, display statements, nav items, body emphasis - the hero font. Used at 232-245px with weight 400 and line-height 0.90 for the signature oversized editorial type. The ultra-tight leading locks massive letters into a single visual band. Subheads drop to 32-48px at weight 600-700.
- EuropaGroNr2SB `--font-europagronr2sb` for Small UI text, nav labels, button copy, captions, footer micro-copy. The functional sans - quiet, compact, only at 12-14px. The deliberate size gap between this and EuropaGroNr2SH creates a clear voice split: small = system, large = editorial.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 48-56px.
- Card padding: 16px.
- Element gap: 16px.

Build these component patterns where relevant:

- Pill Button (Filled Dark): Primary action button on light backgrounds
- Pill Button (Outlined): Secondary action on light backgrounds
- Pill Button (On Image): Hero or category card CTA
- Category Split Card: Men/Women category entry on homepage
- Product Card: Individual product listing in grid
- Product Grid: 3-column product showcase
- Hero Section: Seasonal campaign entry with oversized editorial type
- Top Navigation: Primary site navigation
- Footer: Site footer with link columns
- Search Trigger: Search button in nav
- Cart Trigger: Cart button in nav

Do:

- Use EuropaGroNr2SH for all display and heading text - never substitute a different display face; the 232-245px scale with 0.90 line-height is the signature
- Set border-radius to 9999px on every button, tag, and pill-shaped control - sharp corners are not in this system
- Keep the palette to fog, ink, paper, and charcoal for all UI chrome - let photography provide the only visual richness
- Use #fffb85 exclusively for oversized hero display text over photography - never for buttons, links, or small UI text
- Let product images fill their containers edge-to-edge with no card borders, no padding, and no shadows
- Space sections at 48-56px and let the gray canvas carry the rhythm between content blocks
- Use weight 400 for display headlines at maximum scale - the whisper-weight at 245px creates authority through restraint, not volume

Avoid:

- Do not introduce saturated accent colors (reds, blues, greens) into the UI - the 1% colorfulness is deliberate
- Do not apply box-shadows, drop-shadows, or gradient fills to any component - the system is completely flat
- Do not use sharp or moderately rounded corners on buttons or interactive elements - only 9999px or 0px exist
- Do not use pure #000000 for text - use #10100f; the near-black warmth is a design choice, not a compromise
- Do not place body text directly over product photography without sufficient contrast or a dark scrim
- Do not break the two-font split: EuropaGroNr2SB for 12-14px system text, EuropaGroNr2SH for 16px and above - mixing sizes across fonts fragments the voice
- Do not add decorative borders, dividers, or background tints to card components - the photograph and gray canvas define all visual structure

Source prompt cues:

**Quick Color Reference**
- text: #10100f
- background: #efefef
- surface/card: #ffffff
- border: #efefef
- primary action: #26292a (filled action)
- hero accent: #fffb85

**3-5 Example Component Prompts**

1. *Hero Section*: Full-viewport-height product photograph as background. Display headline at 245px EuropaGroNr2SH weight 400, color #fffb85, line-height 0.90, positioned center-left. Subtext at 20px weight 400, #ffffff, below headline. Two pill CTAs at bottom-left: first filled #26292a with white text 14px, second outlined 1px #ffffff border with white text 14px. Both buttons at 9999px radius, 12px vertical / 32px horizontal padding.

2. *Category Split Card (50/50)*: Full-bleed product photograph filling left or right half of viewport, edge-to-edge, no border or padding. Overlay text 'Shop Women' or 'Shop Men' at bottom-left in EuropaGroNr2SH 40px weight 600, color #ffffff, with 20px left and bottom margin from image edge.

3. *Product Card in 3-Column Grid*: Product image filling full column width, edge-to-edge, no padding, no border, no shadow. Below image: product name at 14px EuropaGroNr2SB weight 400, #10100f, and price on the same line right-aligned at 14px. No card background color - the #efefef canvas shows through.

4. *Pill Button (Filled)*: Background #26292a, text at 14px EuropaGroNr2SB weight 400, color #ffffff, padding 12px vertical / 32px horizontal, border-radius 9999px, no border, no shadow, no hover transition beyond color shift to #40403f.

5. *Top Navigation*: Single row, #efefef or transparent background, no bottom border. Brand mark 'RAINS' at far left in EuropaGroNr2SB 14px. Nav links NEWIN, WOMEN, MEN, BAGS, ACCESSORIES, HOME AWAY, RAINS WORLD left-aligned with 32px left padding each, 14px uppercase #10100f. Search and Cart pill buttons at far right, 9999px radius, transparent fill, #10100f icon and label, 14px.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
