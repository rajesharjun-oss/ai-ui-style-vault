# AI Implementation Prompt

Build a Enter GmbH-inspired interface using this source-derived style bundle.

Reference site: https://enter-support.de
Theme: mixed
Category: Dev Tools
North star: Bauhaus poster workshop, midday sun

Use these palette anchors:

- Signal Orange `#ff5000` for Full-bleed section surfaces, geometric illustration caps, partner section canvas - carries warmth and authority across an otherwise achromatic text system
- Seafoam Panel `#a5d3d4` for Hero canvas and alternating section ground - a cool counterweight to the warm orange, used as full-bleed background, never as a text highlight
- Cream Stock `#f9f8ea` for Soft band surfaces between content sections - a paper-like off-white warmer than pure #ffffff, signals a transition zone
- Charcoal `#282828` for Filled button background, dark illustration blocks, heading accents - the loaded weight of the palette, softer than pure black
- Ink `#000000` for Primary body and heading text, hairline borders, icon strokes, link underlines - the dominant typographic color
- Pebble `#6a6a6a` for Muted border and separator color for subtle structural lines that shouldn't compete with text
- Paper `#ffffff` for Default page canvas, text on dark filled buttons, surface for content sections between color bands

Use these typography anchors:

- Maax Mono `--font-maax-mono` for Primary text and body - monospaced at body size gives the whole site a code-readout, technical-manual cadence. This is the signature choice: a service company writing like a terminal
- Sofia-Regular `--font-sofia-regular` for Display headings - a softer humanist sans used sparingly for larger section titles, providing the only non-monospaced typographic moment in the system
- Helvetica `--font-helvetica` for Micro UI text - marquee strips, tiny labels, and small interface markers; falls back to system monospaced where available

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 24px.
- Card padding: 20px.
- Element gap: 24px.

Build these component patterns where relevant:

- Filled Pill Button: Primary action control (Support, Submit)
- Icon Pill Button: Compact utility control (the + button)
- Text Link with Arrow: Inline navigation to subpages
- Marquee Strip: Top-of-page announcement ticker
- Header Bar: Top navigation
- Hero Illustration Block: Abstract visual identity asset
- Two-Column Text Layout: Narrative + link list pair
- Section Divider Band: Color-block transition between content zones
- Partner Section (Orange Field): Full-bleed spectacle band
- Footer Label: Bottom-of-section identification

Do:

- Use Maax Mono (or a monospaced substitute) for all body, nav, link, and button text - the monospaced cadence is the site's identity
- Set border-radius to 25px on all buttons, tags, marquee containers, and link pills
- Stack sections as full-bleed color bands (#ffffff #f9f8ea #a5d3d4 #ff5000) with hard seams and no gradients between them
- Use #282828 as the filled button background and #ffffff as the button text - no other filled-button color
- Anchor headings in Sofia-Regular 28px line-height 1.3; everything else stays in the mono family
- Use 24px as the default element gap and 20px as the default link/heading padding token
- Keep links typographic: underlined #000000 Maax Mono with a arrow prefix, never styled as buttons or chips

Avoid:

- Do not introduce a sans-serif body font - replacing the mono face destroys the technical-manual personality
- Do not use orange (#ff5000) as a button or link color - it's an architectural surface, not an interactive accent
- Do not add shadows, glows, or elevation effects to cards or buttons - the system is flat and hard-edged
- Do not use teal (#a5d3d4) for text or borders - it only works as a full-bleed surface
- Do not use border-radius values other than 25px on interactive elements - partial rounding breaks the pill vocabulary
- Do not place photography or product screenshots - the site is text-and-illustration only
- Do not add gradient transitions between color bands - every section boundary must be a hard seam

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #ffffff
- border: #000000 (hairline) or #6a6a6a (muted)
- accent: #ff5000 (Signal Orange - surfaces only, not interactive)
- primary action: #282828 (filled action)
- section surface: #a5d3d4 (Seafoam), #f9f8ea (Cream Stock), #ff5000 (Signal Orange)

3-5 Example Component Prompts:

1. Build a Support pill button: background #282828, text #ffffff, border-radius 25px, padding 13px 25px, font Maax Mono 16px weight 400. Place on a seafoam (#a5d3d4) hero canvas.

2. Build a hero section with full-bleed background #a5d3d4. Center an abstract geometric illustration of three vertical posts in cream (#f9f8ea) and charcoal (#282828) with three charcoal cubes and three orange (#ff5000) caps at varying heights. No shadows. No gradients.

3. Build a two-column content section: left column contains Maax Mono 16px weight 400 body text in #000000 describing IT services; right column contains three text links stacked vertically, each prefixed with and underlined. Background #ffffff, max-width 1200px centered, 24px gap between columns.

4. Build a marquee announcement strip: pill-shaped container (border-radius 25px) with background #ffffff, Maax Mono text in #000000 at 10-16px, padding ~6px 20px. Position it in the header between the logo and the action buttons.

5. Build a partner section: full-bleed #ff5000 background spanning the full viewport width, minimal content, no buttons or CTAs. Below it, a cream (#f9f8ea) band with a centered small label 'Unsere Partner' in Maax Mono.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
