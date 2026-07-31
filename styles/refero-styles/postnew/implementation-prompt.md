# AI Implementation Prompt

Build a PostNew-inspired interface using this source-derived style bundle.

Reference site: https://www.postnew.xyz
Theme: dark
Category: Design
North star: After-hours gallery with daylight spreads

Use these palette anchors:

- Canvas Black `#1a1a1a` for Page background, gallery vitrine, frame around content - a near-black not-quite-pure-black that lets imagery breathe without the harshness of #000
- Bone White `#fafafa` for Primary text, nav labels, icon strokes, light surface fill - the only light token, reserved for foreground against Canvas Black
- Slate Surface `#242424` for Elevated cards, button backgrounds, secondary surface panels - one step lighter than canvas to create depth without contrast drama
- Ash `#5d5d5d` for Muted UI elements, inactive dots, decorative fills - the 6.3:1 ratio against white keeps it legible but clearly secondary
- Absolute Black `#000000` for Hairline borders, high-contrast text, deepest shadow line - used sparingly where maximum definition is needed against the canvas

Use these typography anchors:

- ABC Diatype Medium `--font-abc-diatype-medium` for Editorial display and body - the only display face, used at just two sizes (18px / 22px) with -0.025em tracking. The single weight (500) is deliberate: no bold, no light. The OpenType features (blwf, cv03-cv11, ss09-ss10) activate specific character alternates that give it a subtly editorial personality. Substitute with Inter Tight Medium or Sohne Medium if ABC Diatype is unavailable.
- System Sans-Serif `--font-system-sans-serif` for UI chrome only - nav labels (Index, Feed, Profile), view toggle icons, scroll dots. At 12px it is intentionally small and quiet, the typographic equivalent of architectural labeling. Do not promote to editorial content.

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: .
- Section gap: 50px.
- Card padding: 12px.
- Element gap: 10px.

Build these component patterns where relevant:

- Top Nav Bar: Minimalist site navigation - three labels centered on a dark canvas
- Scroll Position Indicator: Vertical dot column tracking scroll progress
- View Toggle: Switch between grid and list layout modes for content
- Vitrine Frame: Dark container that presents a single work or art object in isolation
- Editorial Spread: Full-bleed two-page-style layout combining imagery and bold type
- Abstract Shape Decoration: Sculptural 3D blob/bead elements that punctuate editorial spreads
- Ghost Button: Secondary interactive element - minimal, no fill
- Brand Mark Lockup: Logo + product name combination for sponsored or featured content

Do:

- Keep the canvas at #1a1a1a - do not shift to pure #000 or lighter grays; the near-black is the gallery floor.
- Use ABC Diatype Medium at 18px or 22px only - these are the only two editorial sizes. Never scale beyond or interpolate.
- Set letter-spacing to -0.025em on all ABC Diatype text - tighter tracking at this weight is signature.
- Keep all UI radius at 0px - sharp corners are non-negotiable; this is a gallery, not a friendly SaaS app.
- Reserve #fafafa for text and light surface elements against the dark canvas - never use it as a page background.
- Let imagery carry all color - the five neutrals are the entire UI palette; do not introduce brand color tokens.
- Maintain 10px element gaps and 50px section gaps - the compact gallery rhythm depends on tight clustering with deliberate breathing room.

Avoid:

- Do not introduce saturated brand colors, accent hues, or semantic states (success/error/warning) - they break the achromatic gallery frame.
- Do not round corners on cards, buttons, images, or frames - 0px radius is structural to the system.
- Do not add shadows or elevation effects - depth comes from #1a1a1a #242424 #5d5d5d surface steps, not from box-shadows.
- Do not use more than two type sizes from ABC Diatype - 18px and 22px are the complete editorial scale.
- Do not use the system sans above 12px - it is chrome-only typography, not editorial.
- Do not center-align editorial body text - the design uses flush-left or full-bleed compositions, not centered paragraphs.
- Do not add gradients - the system is flat; any gradient breaks the gallery wall metaphor.

Source prompt cues:

**Quick Color Reference**
- text: #fafafa
- background: #1a1a1a
- border: #000000
- muted: #5d5d5d
- surface: #242424
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Create a top nav bar:* Three centered text links (Index, Feed, Profile) on #1a1a1a canvas. System sans-serif 12px, weight 400, color #fafafa, letter-spacing normal. 10px gap between items. No background, no border, no shadow.

2. *Create a gallery vitrine:* Centered dark panel, full-viewport height, #1a1a1a background. A single hero object (rendered as an img) centered horizontally, occupying ~400px wide. No border, no radius, no shadow. The object floats in the dark with no frame or label.

3. *Create an editorial spread:* Full-bleed split layout. Left half: product photograph bleeding to left and bottom edges. Right half: oversized headline in ABC Diatype Medium, 22px, color #000000, letter-spacing -0.55px, set tight and overlapping the left image. 3D blob decorations in saturated colors layered on top. No padding from viewport edges.

4. *Create a view toggle:* Bottom-center floating control. Two ghost icon buttons side by side. Background #242424, 12px horizontal padding, 8px vertical padding, 0px radius. Icons in #fafafa at 12px. 13px gap between buttons. No border, no shadow.

5. *Create a scroll indicator:* Left edge of viewport, vertically centered. Column of 10 small dots, 4px diameter each, 5px row-gap. Filled dots in #5d5d5d, one active dot in #fafafa. No background container.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
