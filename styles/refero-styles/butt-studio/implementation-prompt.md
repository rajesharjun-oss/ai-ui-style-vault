# AI Implementation Prompt

Build a BUTT STUDIO-inspired interface using this source-derived style bundle.

Reference site: https://www.butt-studio.com
Theme: light
Category: Agency
North star: gallery wall with one massive serif wordmark

Use these palette anchors:

- Ink Black `#000000` for Primary text, borders, button outlines, structural strokes - the only color that ever carries information
- Paper `#ffffff` for Card surfaces, thumbnail covers, inverted text on dark blocks
- Carbon `#131313` for Dark project tile backgrounds, near-black surface for video panels
- Bone Gray `#e0e0e0` for Page canvas, neutral button fills - the warm gray the whole composition sits on
- Studio Indigo `#31338e` for Sole chromatic accent - STUDIO pill badge, and any deep brand punctuation. The only saturated color in the system

Use these typography anchors:

- helvetica `--font-helvetica` for Every utility, body, list, button, and link on the site. Stays at one weight - no bold, no medium. The decision to use weight 400 Helvetica at 20px for body (not 16px) is deliberate: text is meant to feel like printed matter, not a UI. Tighter letter-spacing on larger sizes (-0.03em) prevents the 40px from feeling airy.
- Caslon `--font-caslon` for The hero wordmark and any serif accent. A single weight of a custom display serif - chosen because its high contrast strokes and ball terminals read as editorial print, not web type. This font IS the brand; everything else is scaffolding.
- Sometimes Times `--font-sometimes-times` for Sometimes Times - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: .
- Card padding: 20px.
- Element gap: 20px.

Build these component patterns where relevant:

- Wordmark Hero: The site identity block
- STUDIO Pill Badge: Brand stamp overlapping the wordmark
- Three-Column Info Ledger: Primary navigation and metadata block beneath the hero
- Project Tile (Light): Standard project entry with video thumbnail
- Project Tile (Dark): Inverted project entry for visual rhythm
- Download Button: Neutral pill action
- Video Thumbnail: Clickable preview for project media
- Page Divider: Visual break between project entries

Do:

- Set the hero wordmark oversized in Caslon at weight 400, tight tracking (-0.02em), so one word fills the full viewport width
- Use #e0e0e0 as the page canvas - never pure white at the page level; reserve #ffffff for card surfaces only
- Use Studio Indigo #31338 exactly once per surface as the only chromatic accent
- Set body text at 20px Helvetica weight 400 with -0.03em letter-spacing - bigger and tighter than web convention
- Give buttons and the STUDIO badge a 50px pill radius for the only rounded elements in the system
- Separate project tiles with a 1px black hairline and 180px vertical space to read as a printed catalog
- Let interactive illustrations physically break through or weave between the serif letterforms in the hero

Avoid:

- Do not introduce any color other than the four neutrals and Studio Indigo - no gradients, no tints, no hover-state color shifts
- Do not use shadows, glows, or elevation - the design is flat like print, with no synthetic depth
- Do not add border-radius to cards, tiles, or thumbnails - they must stay sharp like cut paper
- Do not set body text below 20px or add bold/medium weights to Helvetica - weight 400 is the only weight that exists
- Do not use Caslon for anything below the hero - reserve it for the wordmark and project titles to preserve its weight
- Do not add underlines, color, or icons to links in the client/feature lists - they read as plain text on purpose
- Do not center body text or list items - the ledger columns are left-aligned like a contact page

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
