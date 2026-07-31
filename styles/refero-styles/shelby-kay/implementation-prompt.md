# AI Implementation Prompt

Build a Shelby Kay-inspired interface using this source-derived style bundle.

Reference site: https://shelbykay.dev
Theme: light
Category: Agency
North star: botanical editorial spread on warm linen - two-color ink system on aged paper, with display type that bleeds past the page edge and metadata that whispers from the margins.

Use these palette anchors:

- Olive Ink `#393c2a` for Primary text, borders, and structural strokes - all type from body to display headings, all card and image borders, all interactive outlines
- Sage Type `#737955` for Display headings and brand voice - used for the monumental SHELBY wordmark, section anchors, and selective heading accents that carry the brand's botanical identity
- Linen `#efe6d9` for Primary canvas and card surfaces - page background, card fills, the base warm tone the entire system sits on
- Sienna `#d6b292` for Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Driftwood `#afa199` for Tertiary surface and muted helpers - profile-section backdrop, desaturated metadata, low-emphasis UI text and dividers
- Riverstone `#7b8785` for Cool-toned neutral for subtle contrast shifts - secondary surface, hover or muted state for UI elements needing visual separation from the warm base

Use these typography anchors:

- Ranade `--font-ranade` for Display and editorial headlines. Used at extreme scale (83-265px) for the wordmark and section anchors, and at 24px for the CONTACT callout. The geometric, slightly condensed forms give the brand its monumental-but-restrained voice - the type fills the frame without shouting. Substitute: Boldonse or Bold Neue for display, Space Grotesk for smaller uses.
- Switzer `--font-switzer` for Everything else: body copy, nav, labels, metadata, card titles, list items. The compact grotesque reads as editorial running text. Weight 500-600 is the workhorse range; 700 is reserved for section headers and emphasized nav. Substitute: Inter, Untitled Sans, or Suisse Int'l for full weight coverage.

Use these layout rules:

- Base spacing: 8px.
- Density: compact.
- Page max-width: .
- Section gap: 36-56px.
- Card padding: 20px.
- Element gap: 12px.

Build these component patterns where relevant:

- Wordmark Display: Brand-defining type element
- Section Anchor: Section transition label
- Rotated Side Label: Vertical decorative element
- Minimal Nav: Text-only site navigation
- Project Card: Work grid item
- Date Stamp: Editorial metadata
- Client List Column: Sidebar content list
- Portrait Image Card: Profile photo with duotone treatment
- Recognition / Award List: Right-aligned metadata column
- Full-Bleed Botanical Background: Hero atmosphere layer
- Hero Subtitle: Opening statement below the wordmark

Do:

- Use Ranade at 83px or larger for any brand or section-defining headline - it is the only type with permission to fill the frame.
- Set body and metadata in Switzer weight 500-600 at 10-16px - the compact grotesque is the workhorse and should handle 90% of the interface.
- Build the palette from exactly two brand colors: Olive Ink (#393c2a) for structure, Sage Type (#737955) for brand voice. Use Sage sparingly - one display element per section maximum.
- Let the canvas shift through warm tonal layers (Linen Sienna Driftwood) to define sections instead of hard borders or color blocks.
- Use 0px border-radius everywhere - cards, images, tags. The printed-page metaphor demands sharp corners.
- Use 7-8px padding for tight metadata containers and 20px for card padding - the 8px base unit governs all spacing.
- Use Olive Ink (#393c2a) for all text and borders. The 9.2:1 contrast ratio on Linen makes it readable at 10px and monumental at 265px.

Avoid:

- Don't add drop shadows, glows, or any CSS elevation - the system is deliberately flat and print-like.
- Don't introduce rounded corners (border-radius > 0) on any element - it breaks the editorial metaphor.
- Don't use Sage Type (#737955) for body text - its 3.7:1 contrast on Linen fails readability standards. Reserve it for display headings only.
- Don't create filled button backgrounds in any color - this system has no CTA buttons. Navigation is text-only, contact is a typographic anchor.
- Don't use gradients, brand illustrations, or icon sets - the visual language is photography, type, and tonal layering only.
- Don't use any cool or neutral gray outside the Riverstone (#7b8785) token - all neutrals must stay warm to maintain the botanical atmosphere.
- Don't center body text. Left-align everything except section anchors, which are the only elements that get centered treatment.

Source prompt cues:

**Quick Color Reference**
- text: #393c2a (Olive Ink)
- background: #efe6d9 (Linen)
- border: #393c2a (Olive Ink)
- accent: #737955 (Sage Type)
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. **Build the wordmark hero**: Full-bleed #efe6d9 canvas with a large botanical photograph at ~12% opacity filling the background. Centered display heading 'SHELBY' in Ranade weight 400, size 265px, line-height 0.90, color #737955, stretching edge-to-edge. A hero subtitle below in Switzer weight 500, 14px, line-height 1.30, color #393c2a, left-aligned, two short lines maximum.

2. **Build a project card for the work grid**: On a #d6b292 section background, render a full-bleed image with 0px border-radius as the card body. Overlay a date stamp in the top-left corner using Switzer weight 500, 10px, color #393c2a, rotated 90 . Below the card, center a two-letter label in Switzer weight 600, 11px, color #393c2a. No border, no shadow, 20px gap between cards.

3. **Build the minimal nav bar**: Fixed or bottom-aligned, 7px vertical padding. Left side: three text links ('WORK', 'PROFILE', 'CONTACT') in Switzer weight 500, 11px, uppercase, color #393c2a, separated by 20px gap. Right side: a year label ('2026') in the same style, right-aligned. No backgrounds, no borders, no dividers - whitespace defines the items.

4. **Build the profile section**: On a #afa199 background, place a square portrait image on the left (0px radius, no border). In the center, a label 'RECOGNITION' in Switzer weight 700, 14px, color #393c2a, followed by a vertical list of names in Switzer weight 500, 11px. On the right, a right-aligned column of award entries in Switzer weight 500, 11px, with project names on one line and details below. 36px gap between sections.

5. **Build the rotated side label**: Pin a 'KAY' text element to the right edge of the viewport, rotated 90 counter-clockwise. Ranade weight 400, 158px, color #393c2a, line-height 0.90. Positioned vertically centered in the hero. Functions as a running header - the type touches the frame edge with no padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
