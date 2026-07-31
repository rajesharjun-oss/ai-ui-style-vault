# AI Implementation Prompt

Build a KeepGrading-inspired interface using this source-derived style bundle.

Reference site: https://www.keepgrading.com
Theme: dark
Category: Agency
North star: Polaroids scattered in a darkroom

Use these palette anchors:

- Studio White `#f8f8f8` for Primary text, ghost-button borders, image-frame outlines, nav icon strokes - the single light voice in a dark room
- Void Black `#080808` for Page canvas, behind-everything background, image frame fills between photographs
- Pure Black `#000000` for SVG icon fills, deepest surface layer for inline graphics and decorative marks
- Bone White `#f0f0f0` for Soft secondary text and supporting hairline strokes when pure white feels too clinical
- Pewter Border `#2a2a2a` for Low-contrast dividers and inactive frame edges that recede against the void

Use these typography anchors:

- Cabinet Grotesk `--font-cabinet-grotesk` for Brand display and logo wordmark - the 96px headline weight 400 is anti-convention; no bold, no display tricks, just a single weight carried to monumental size that feels confident through restraint. Also used at 24px for short subheadings and 16px for nav labels. This custom typeface carries the entire brand identity.
- Inter `--font-inter` for Body text and supporting copy at 16px and 20px, both at weight 400 - no bold variant in use, the system keeps a single weight even for emphasis, letting size and color do the hierarchy work

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: .
- Section gap: 48px.
- Card padding: 24px.
- Element gap: 15px.

Build these component patterns where relevant:

- Ghost Pill Button: Primary navigation/action control
- Circular Nav Toggle: Menu trigger in top-right corner
- Wordmark Logo: Brand identity in top-left
- Floating Image Frame: Photo card scattered across the canvas
- Canvas Layer: Base surface for the entire page
- Section Spacer: Vertical rhythm between content bands
- Nav Label: Secondary navigation text

Do:

- Use #f8f8f8 for all text, borders, and icon strokes on the #080808 canvas - never introduce a chromatic accent for emphasis.
- Set display headlines in Cabinet Grotesk 96px weight 400, line-height 1.0; the single weight at monumental size is the signature.
- Use 9999px border-radius for all buttons, tags, and the nav toggle to maintain the pill/circle-only shape vocabulary.
- Use 160px border-radius for image frames to keep corners soft but distinct from the fully pill-shaped controls.
- Maintain 48px minimum vertical gap between content bands; let whitespace separate sections rather than dividers or shadows.
- Keep all UI chrome at weight 400 across both Cabinet Grotesk and Inter; hierarchy comes from size, not weight.
- Position image frames as scattered floating elements with varying offsets and sizes rather than aligning them to a strict grid.

Avoid:

- Do not introduce any chromatic brand color, accent, or gradient - the monochrome void is the brand.
- Do not add drop shadows, glows, or any elevation effects - depth comes from layering and contrast alone.
- Do not use bold (600+) or semibold weights for emphasis; switch size or color instead.
- Do not use sharp corners (0-8px radius) on any visible element - all surfaces must be pill-rounded or softly curved.
- Do not apply background fills to buttons; the ghost outlined style is the only button treatment.
- Do not constrain the page to a max-width column; the full-bleed black canvas is essential to the darkroom feel.
- Do not add icons, badges, or decorative graphics to the UI chrome - type, borders, and photographs are the only visual elements.

Source prompt cues:

Quick Color Reference:
- text: #f8f8f8
- background: #080808
- border: #f8f8f8 (1px)
- muted border: #2a2a2a
- accent: none (monochrome system)
- primary action: no distinct CTA color

Example Component Prompts:
1. Create a hero section: full-bleed #080808 canvas. Top-left wordmark 'KEEPGRADING' in Cabinet Grotesk 96px weight 400, #f8f8f8, line-height 1.0, allowed to crop at viewport edge. Top-right circular nav button: 160px diameter, 1px solid #f8f8f8 border, transparent fill, centered hamburger glyph in #f8f8f8 1px stroke.
2. Create a floating image card: photograph with 1px solid #f8f8f8 border, border-radius 160px, no fill, no shadow, no padding - image fills the frame edge to edge. Position at non-grid offset on the canvas.
3. Create a ghost pill button: transparent background, 1px solid #f8f8f8 border, 9999px border-radius, padding 12px 24px. Label in Inter 16px weight 400 #f8f8f8, followed by a right-arrow stroke icon in #f8f8f8 1px.
4. Create a scattered photo grid: 3-5 image frames at varying sizes (300px-600px wide), positioned with editorial offsets (not aligned to a grid), separated by at least 48px vertical gap, each with 160px corner radius and 1px #f8f8f8 border, on #080808 canvas.
5. Create a section spacer: 48px tall empty #080808 band between content clusters, no visible divider line, no shadow.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
