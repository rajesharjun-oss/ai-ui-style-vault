# AI Implementation Prompt

Build a Alt-Border-inspired interface using this source-derived style bundle.

Reference site: https://www.alt-border.com
Theme: light
Category: Agency
North star: Monochrome editorial gallery - broadsheet headline on gallery white.

Use these palette anchors:

- Ink `#000000` for Primary type, body text, hairline rules, link borders, and the structural color of the entire page - used at high frequency for borders and text alike, creating a printed-ink quality against the white canvas
- Gallery White `#ffffff` for Page canvas, card and image backgrounds, the negative space that lets type and photography breathe
- Graphite `#333333` for Secondary text, muted borders, image strokes - a slightly softened black for elements that should not compete with primary ink
- Ash `#808080` for Section divider rules, link borders, faint hairlines where a true black stroke would be too assertive

Use these typography anchors:

- Neuehaasdisplay `--font-neuehaasdisplay` for Hero display - used only for the massive opening headline and section-statement lines that fill the viewport. The 0.85 line-height is a deliberate choice: lines nearly touch, producing the compressed broadsheet effect. Substitute: Neue Haas Grotesk Display Pro 35 Thin, or Inter at extreme sizes.
- Inferi `--font-inferi` for Multi-purpose face - medium-weight paragraphs (21px), oversized secondary statements (34px, 120px), and small UI labels (14px). The negative tracking (-0.0270em) tightens the rhythm at every size. Substitute: Sohne, Inter, or Untitled Sans.
- Suisseintl `--font-suisseintl` for Body and supporting copy - quiet, legible, never decorative. Same negative tracking as Inferi keeps the family consistent. Substitute: Suisse Int'l Light, or Inter Light.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: .
- Section gap: .
- Card padding: 0px.
- Element gap: 9px.

Build these component patterns where relevant:

- Top Navigation Bar: Minimal global navigation - three items distributed across the full viewport width.
- Hero Display Headline: Opening statement that defines the studio's identity.
- Section Label Row: Identifies the section and provides a navigation cue to related content.
- Image Feed Grid: Three-column photography showcase for project work and social feed.
- Image Card with Caption: Individual portfolio thumbnail with title underneath.
- Statement Section: Mid-page manifesto block - the second editorial moment after the hero.
- Link with Arrow: Inline navigation cue used in section label rows.
- Inline Thumbnail: Small photographic element embedded within a hero headline.
- Section Divider Rule: Hairline separator between editorial sections.

Do:

- Set display headlines in Neuehaasdisplay 300 at 105px with line-height 0.85 - the compressed vertical rhythm is the signature, not a default.
- Use #000000 for all primary type, borders, and rules; #808080 only for soft dividers.
- Keep all radii at 0px - the design is anti-rounded, it reads as print, not product UI.
- Separate sections with a single 1px #808080 hairline and 7-9px vertical padding, never with background color changes or cards.
- Let photographs carry all color and texture; the type and chrome stay strictly achromatic.
- Set body and supporting type at 21px with letter-spacing -0.0270em - the negative tracking is consistent across the Inferi and Suisseintl families.
- Place small square thumbnails inline within hero text as if they were characters on the baseline.

Avoid:

- Do not introduce any chromatic color - the palette is achromatic by design, not by omission.
- Do not add drop shadows, blurs, or any elevation - separation comes from rules and whitespace alone.
- Do not round corners on images, buttons, or cards - 0px radius is the system.
- Do not use a CTA button style - there is no primary action color; navigation is text-only with arrow links.
- Do not exceed 0.92 line-height on the 105px display - looser tracking destroys the broadsheet compression.
- Do not set body type below 14px or above 34px - the scale jumps are deliberate: 14, 21, 34, 105.
- Do not add background fills to sections, cards, or navigation - the page is a single white sheet.

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #ffffff
- border / hairline: #808080
- muted border: #333333
- accent: none (no chromatic accent in the system)
- primary action: no distinct CTA color

Example Component Prompts:

1. Create the hero headline band: white background, full viewport width. Type 'A multidisciplinary art direction studio working across fashion, beauty, and luxury.' set in Neuehaasdisplay 300 weight at 105px, color #000000, line-height 0.85, letter-spacing normal. 7-9px top padding. A 1px #808080 hairline below.

2. Create a section label row: full-width, white background. Left side reads 'Feed' in 14px Inferi 400 weight #000000. Right side reads ' Instagram' in the same type. 1px #808080 hairline below with 7-9px vertical padding.

3. Create a 3-column image grid: full viewport width, white background, 9px gap between columns and rows. Images are object-fit cover, 0px border-radius, no captions inside the grid. Below one image, place a title in 14px Inferi 400 weight #000000 with 9px top margin.

4. Create a statement section: white background, full-width, 19px top margin. Type 'We create concept-driven imagery and identities through CGI, photography, and design.' in Neuehaasdisplay 300 at 105px, line-height 0.92, color #000000. 7-9px top padding. No border, no background.

5. Create a text-link with arrow: 14px Inferi 400 weight #000000, preceded by a glyph, 5px padding-bottom. No underline, no hover color change, no border.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
