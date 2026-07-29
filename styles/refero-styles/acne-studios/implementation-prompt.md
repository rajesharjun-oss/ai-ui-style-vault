# AI Implementation Prompt

Build a Acne Studios-inspired interface using this source-derived style bundle.

Reference site: https://acnestudios.com
Theme: light
Category: E-commerce
North star: Minimalist gallery white space with bold photographic moments - a fashion magazine laid flat on marble.

Use these palette anchors:

- Electric Cobalt `#0018a8` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Ink Black `#000000` for Primary text, logo wordmark, icon strokes, nav labels, and footer copy. Used at 21:1 contrast on white for absolute legibility
- Graphite `#6b6b6b` for Supporting neutral for secondary UI, dividers, and muted labels.
- Paper White `#ffffff` for Page canvas, product card backgrounds, and nav bar surface. The dominant ground that lets editorial photography breathe
- Bone `#f2f2f2` for Subtle box-shadow tint and hairline border for elevated overlays. Used minimally - the system prefers whitespace to tinted surfaces

Use these typography anchors:

- Helvetica Monospaced Pro `--font-helvetica-monospaced-pro` for Helvetica Monospaced Pro - detected in extracted data but not described by AI
- Acne Studios (custom wordmark) `--font-acne-studios-custom-wordmark` for Oversized brand wordmark overlaid on hero photography. The custom face has geometric construction with humanist terminals; no system font replicates it, but its character is closest to a wide-aperture geometric sans.
- Helvetica Neue / system sans `--font-helvetica-neue-system-sans` for All functional UI text: nav links, section labels, product captions, footer. Always rendered uppercase with generous tracking - this typographic treatment is the single most recognizable non-photographic element on the site.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: .
- Section gap: 60px.
- Card padding: 0px.
- Element gap: 10px.

Build these component patterns where relevant:

- Top Navigation Bar: Minimal text-only site header
- Section Label: Category indicator above editorial splits
- Full-Bleed Split Hero: Primary landing visual
- Product Grid Cell: Individual product listing in the category grid
- Editorial Tile Row: Brand storytelling content beneath product grid
- Text Link: Interactive inline link in body copy and nav
- Icon Button: Search, help, account, and cart triggers

Do:

- Use #0018a8 only for text links, active nav states, and icon strokes - never as a filled button background
- Set body and nav text to 10-11px uppercase with 0.0330em letter-spacing for the signature editorial voice
- Let product and editorial images span full viewport width with 0px gap between adjacent cells
- Default page background to #ffffff and avoid any tinted surface unless absolutely necessary
- Keep card and image radius at 0px - the system uses hard edges to read as printed magazine spreads
- Use #000000 at 21:1 contrast for all primary text on white; reserve #6b6b6b for genuinely secondary copy
- Maintain 60px vertical section gaps and 30px nav padding as the structural rhythm

Avoid:

- Do not introduce filled CTA buttons, pill shapes, or rounded containers - they break the editorial-flat aesthetic
- Do not apply box-shadow to product cards, nav, or content tiles; separation comes from whitespace alone
- Do not use colors outside the five-token palette for interface chrome - photography supplies all chromatic richness
- Do not set type below 9px or render body text in anything other than uppercase with tracking for nav-adjacent labels
- Do not center body content or constrain to a max-width - layouts should be full-bleed to feel like a magazine spread
- Do not add borders, dividers, or background fills to product cells - they must bleed into each other
- Do not use #0018a8 as decorative illustration color; it is reserved for functional interactive states

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
