# AI Implementation Prompt

Build a Outsource Consultants-inspired interface using this source-derived style bundle.

Reference site: https://oci.madebybuzzworthy.com
Theme: light
Category: Agency
North star: Architectural broadsheet on bone paper. A monograph aesthetic where one violent indigo section interrupts an otherwise warm, typographically maximalist grid.

Use these palette anchors:

- Indigo Strike `#1925aa` for Brand mark, full-bleed section backgrounds, large headlines, icon strokes, nav borders - the singular chromatic voice of the system, used as a sudden tonal shift rather than a decorative accent
- Bone `#e8e6e0` for Page canvas and card surface - a warm off-white that reads as paper rather than screen, providing the neutral ground against which indigo gains force
- Ink `#000000` for Body copy, small labels, standard text - used for dense information layers that must stay recessive against the bone canvas
- Paper `#ffffff` for Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color
- Deep Indigo `#0d1355` for Logo and brand-mark fill - a near-black violet that grounds the wordmark against the brighter Indigo Strike used in UI contexts

Use these typography anchors:

- GT America Mono `--font-gt-america-mono` for Micro-metadata and technical labels - nav identifiers, menu button text, accordion descriptions, footer tags. The mono face signals 'technical / regulatory / specification' and is kept under 14px so it reads as annotation rather than content. Negative tracking at 10px tightens the monospace grid; the slight positive tracking at 14px opens it for legibility. This pairing of editorial sans + technical mono is the system's core typographic gesture.
- PP Neue Montreal `--font-pp-neue-montreal` for Display and editorial type - carries the massive hero headline at 160px (line-height 0.94, so letters nearly touch), subheadings at 36-46px, and body at 18px. The grotesque geometry and tight line-height at scale create a poster-like voice; the same family steps down to 12-16px for nav links and service titles. Using one sans family from 12px to 160px (an extreme ratio) is a signature choice - it means hierarchy is built by size alone, not by weight or family switching.
- ui-sans-serif `--font-ui-sans-serif` for ui-sans-serif - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 15px.

Build these component patterns where relevant:

- Brand Header Bar: Sticky top navigation
- Menu Toggle Button: Navigation trigger
- Hero Display Headline: Section anchor / brand statement
- Vertical Side Label: Section annotation
- Full-Bleed Indigo Section: Alternating tonal band
- Service Accordion Item - Collapsed: Expandable list row
- Service Accordion Item - Expanded: Open accordion panel
- Section Heading Pair: Two-part section title
- Centered Body Caption: Editorial block

Do:

- Let PP Neue Montreal do the work - push display sizes to 46-160px and use line-height 0.94-1.10 at those scales; do not add weight to compensate for small size.
- Use GT America Mono exclusively for labels, captions, nav items, and accordion descriptions; keep it at 10-14px with tracking -0.05em (tight) at 10px and +0.02em (open) at 14px.
- Alternate between the bone canvas and the Indigo Strike full-bleed to create section rhythm - do not stack multiple bone sections without an indigo interruption.
- Treat borders as hairlines: 1px Ink at low opacity for dividers between accordion rows and section bisectors; never use borders for cards or containers.
- Use vertical rotated text in the right margin (18px PP Neue Montreal) as a section annotation device.
- Anchor every section with a flush-left display headline in the body color (Ink on bone, Bone on indigo); keep headlines full-width and uncontained.
- Keep all corners sharp - 0px radius on every element including buttons, cards, and tags.

Avoid:

- Do not introduce shadows, glows, blurs, or any form of drop elevation - the system is deliberately flat.
- Do not use indigo as a button background fill - the Menu button is white with an indigo icon square; indigo is a surface, not an action color.
- Do not add a second accent color - the system is bone + ink + a single indigo; any new chromatic role will dilute the editorial tension.
- Do not use PP Neue Montreal below 12px - the grotesque loses character at small sizes; switch to GT America Mono for anything sub-14px.
- Do not center headlines or wrap them - display type stays flush-left and bleeds toward the page edge.
- Do not use cards with backgrounds, padding, or radius - content sits directly on the bone canvas divided only by hairlines.
- Do not use a system font fallback for hero type - if PP Neue Montreal is unavailable, substitute with a grotesque (Inter or Sohne), not a humanist sans.

Source prompt cues:

Quick Color Reference:
- text: #000000 (Ink) on bone, #e8e6e0 (Bone) on indigo
- background: #e8e6e0 (Bone canvas)
- border: 1px Ink at ~10% opacity for hairlines
- accent: #1925aa (Indigo Strike) - used for headlines, icons, and full-bleed section backgrounds, not for button fills
- primary action: no distinct CTA color

Example Component Prompts:

1. Service Accordion Row (collapsed): Full-width row on Bone canvas (#e8e6e0). Title in PP Neue Montreal 24px weight 500, color #1925aa, flush-left. '+' glyph in PP Neue Montreal 24px weight 400, color #1925aa, flush-right. 1px hairline border-bottom in #000000 at 10% opacity. Zero padding-radius. No background fill.

2. Hero Display Headline: PP Neue Montreal 160px weight 400, line-height 0.94, color #000000 (on bone) or #e8e6e0 (on indigo), flush-left, bleeding to the left page edge. Paired with a rotated 18px PP Neue Montreal caption in #e8e6e0 positioned in the right margin.

3. Menu Toggle Button: Square button, 40x40px, background #ffffff, containing 'MENU' in GT America Mono 10px tracking +0.02em in #000000, with a flush-right 40x40px #1925aa square containing a white '/' glyph. Zero radius, no border.

4. Full-Bleed Indigo Section: Background #1925aa spanning full viewport width. Headline in PP Neue Montreal 46px weight 400 line-height 1.05, color #e8e6e0, flush-left. Body copy in PP Neue Montreal 18px weight 400, color #e8e6e0.

5. Section Heading Pair: Two words (e.g. 'Our' and 'Services') in PP Neue Montreal 160px weight 400 color #1925aa, placed at opposite horizontal edges of the section (one flush-left, one flush-right). A 1px vertical hairline in #000000 at 10% opacity bisects the section between them.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
