# AI Implementation Prompt

Build a Laura Monin-inspired interface using this source-derived style bundle.

Reference site: https://lauramonin.com
Theme: light
Category: Agency
North star: editorial gallery wall, white marble, ink stamp

Use these palette anchors:

- Paper White `#ffffff` for Page canvas, card surfaces, image borders, nav backgrounds - the only surface tone in the system
- Ink Black `#000000` for Primary text, all border outlines on images and nav, list markers - the sole chromatic anchor

Use these typography anchors:

- title `--font-title` for Display serif used exclusively for the brand title and hero headlines. The custom serif - with its high contrast strokes and slightly condensed forms - carries all brand identity. Letter-spacing of -0.018em tightens the large caps just enough to feel deliberate without becoming stiff. A close substitute would be a transitional or didone-style serif like 'GT Sectra Display' or free options 'Playfair Display' / 'DM Serif Display'
- neue-haas-grotesk-display `--font-neue-haas-grotesk-display` for All UI, navigation, captions, metadata, and body-adjacent text. Geometric grotesque at a single weight (400) - the system deliberately avoids bold/light contrast, using size and placement to create hierarchy instead. Use 'Inter' or 'Neue Haas Grotesk' itself (free via Adobe) as substitutes

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: .
- Card padding: 0px.
- Element gap: 7-12px.

Build these component patterns where relevant:

- Image Tile: Scattered photography containers - the primary content unit
- Image Overlay Caption: Label text positioned over or adjacent to image tiles
- Display Title: Hero brand title - the dominant visual element of the page
- Navigation Link: Top-bar navigation items (INDEX, INFOS, ARCHIVES)
- Wordmark/Brand Mark: Site identity in the top-left
- Section Label: Small text used for project names and collection titles overlaid on images

Do:

- Use only #ffffff and #000000 for all surfaces, text, and borders - never introduce a third color
- Set the hero display title at 58-158px in the custom serif with letter-spacing -0.018em; this scale is non-negotiable for the editorial feel
- Use neue-haas-grotesk-display at weight 400 only - never bold, never light - for all UI text at 12/14/18/22px
- Maintain 200-300px vertical spacing between major page sections to preserve the gallery-wall breathing room
- Keep all border-radius at 0px - every container, image, and button is perfectly rectangular
- Place image tiles in an asymmetric scatter, not a uniform grid - irregular positioning is the layout signature
- Use generous negative space (60%+ of the viewport) rather than packing content into the available area

Avoid:

- Do not add drop shadows, glows, or any box-shadow to any element - the design is intentionally flat
- Do not use rounded corners (border-radius > 0) on any image, card, or button
- Do not introduce accent colors, gradients, or background fills - the system is strictly black on white
- Do not use bold or semibold weights for UI text - weight 400 at all sizes is the rule
- Do not align images to a uniform grid with equal gutters - the asymmetric scatter is the layout identity
- Do not add hover animations, transitions, or micro-interactions to navigation or links
- Do not use sans-serif or grotesque fonts for headlines or display text - the serif carries all brand weight

Source prompt cues:

**Quick Color Reference**
- background: #ffffff
- text: #000000
- border: #000000
- image border: #000000 (1px hairline)
- primary action: no distinct CTA color
- accent: none - system is strictly monochrome

**Example Component Prompts**

1. **Hero Display Title**: Center the text 'La Croisette' on a #ffffff canvas. Font: custom serif (substitute Playfair Display), weight 400, size 158px, line-height 1.20, letter-spacing -0.018em, color #000000. No background, no border, no decoration. The title alone should occupy ~50% of the viewport width.

2. **Image Tile with Overlay Caption**: Place a rectangular photograph (4:5 or 3:4 aspect ratio) on the #ffffff canvas. Wrap with a 1px #000000 border, 0px border-radius. Overlay the caption text (e.g. 'FLEXHIBITION SS24') in neue-haas-grotesk-display weight 400, 12px, uppercase, #000000, positioned at 9px from the top-left corner of the image.

3. **Minimal Navigation Bar**: Top bar spanning full viewport width on #ffffff. Left: brand mark 'LAURA MONIN' in neue-haas-grotesk-display 14px weight 400 uppercase #000000, 16px from left edge. Center: secondary nav links ('FLEXHIBITION SS24', 'LA CROISETTE', 'PISCINE MOLITOR', 'INSTAGRAM') at 12-14px weight 400 #000000 with 16px gaps. Right: nav links ('INDEX', 'INFOS', 'ARCHIVES') at 14px weight 400 #000000. No underlines, no hover effects, no borders.

4. **Asymmetric Photo Scatter Section**: Place 5-6 rectangular photograph tiles in irregular positions across a #ffffff canvas - for example, one in the top-left quadrant (~250px wide), one centered-top (~200px), one top-right (~300px), and a larger one centered below the display title (~400px). Each tile: 0px border-radius, 1px #000000 hairline border, full-bleed image, 0px padding. Maintain 80-120px of irregular negative space between tiles. No grid alignment.

5. **Empty Section Gap**: Insert a vertical breathing zone of 250-300px (padding-bottom) with zero content, zero decoration, pure #ffffff. This is a design element, not wasted space - it creates the gallery-walk cadence between content clusters.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
