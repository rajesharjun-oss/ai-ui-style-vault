# AI Implementation Prompt

Build a Doug-Alves-inspired interface using this source-derived style bundle.

Reference site: https://dougalves.work
Theme: mixed
Category: Design
North star: Oversized typographic monolith on warm charcoal

Use these palette anchors:

- Espresso `#1d1610` for Hero and dark section background - warm-tinted near-black reads as architectural, not as raw #000, giving the oversized display type a gallery-wall feel
- Graphite `#282828` for Primary body text, structural borders, section dividers - the workhorse neutral that draws the hairline rules and most interface lines
- Slate `#333333` for Secondary body and heading text - slightly lighter than Graphite, used for headings and emphasized body copy where Graphite is reserved for borders
- Obsidian `#000000` for Display headings on light sections and pure-black accents - used sparingly for maximum impact on the white About and Latest sections
- Paper `#ffffff` for Content section surfaces and inverted text on dark hero - the bright surface that the warm espresso sections cut against
- Bone `#fff5f2` for Warm off-white page canvas - subtle pink-ivory tint replaces plain white as the base, keeping the entire palette on the warm side of neutral

Use these typography anchors:

- Inter `--font-inter` for Primary body and UI text. The 18px body size with 1.78 line-height creates a generous, editorial reading rhythm that contrasts the compact, tight display type. The 0.89 line-height variant handles single-line labels and metadata where vertical density matters.
- wtqc `--font-wtqc` for Signature display and heading face. The massive 197px/72px/28px scale at weight 300 with tight tracking (-0.033em -0.014em) creates the poster-art identity. At 300 weight, headlines whisper rather than shout - authority through scale and restraint, not boldness. The lighter weight prevents the enormous letterforms from feeling heavy or aggressive.
- System UI (-apple-system) `--font-system-ui-apple-system` for Tertiary fallback for cards, metadata blocks, and system-level UI that doesn't carry brand typographic weight
- -apple-system `--font-apple-system` for -apple-system - detected in extracted data but not described by AI
- Roboto `--font-roboto` for Roboto - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 8px.
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80-120px.
- Card padding: 24-32px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Hero Display Block: Full-bleed opening section carrying the signature oversized type
- Section Mega-Header: Section opener that repeats the poster-scale type on white
- Project Image Card: Showcase tiles for case studies and design work
- Info Grid Row: Multi-column structured data display (footer, contact, experience)
- Bio Statement Block: Long-form introductory text on white sections
- Experience Entry: Compact career timeline item within the Info Grid
- Hairline Divider: Section separator and row delimiter
- External Link: Outbound links to Instagram, LinkedIn, email, etc.
- Refresh Icon Button: Top-right utility icon on the dark hero

Do:

- Use weight 300 at display sizes (72px+). The light weight on massive type is the identity - using 600+ kills the gallery-wall feel.
- Set letter-spacing at -0.033em or tighter for any text above 48px. Tight tracking is what makes the display type look like one continuous mark.
- Alternate between Espresso (#1d1610) full-bleed sections and Paper/Bone sections with no gradient transitions. Hard cuts only.
- Use 1px Graphite (#282828) rules as the primary structural element between rows and sections.
- Keep the palette strictly achromatic. No brand color, no accent, no hover tint - color in the work itself is the only chromatic element.
- Set body copy at 18px with 1.78 line-height. The generous reading rhythm balances the compressed display type.
- Maintain a 4-column grid for all structured information (contact, experience, portfolio meta). Consistency of grid is the layout signature.

Avoid:

- Don't add a brand accent color. The system is monochrome by design - introducing a blue or red CTA breaks the editorial identity.
- Don't use border-radius above 0px on UI elements (buttons, cards, dividers, tags). The single 20px radius applies only to image containers. Sharp corners are the rule.
- Don't set display type above weight 400. The 300 weight whispers - bolding it turns a poster into a billboard.
- Don't use drop shadows, glows, or blur effects. Elevation is communicated through contrast (dark on light, light on dark) and the hairline border system, never through shadow.
- Don't add decorative gradients. The palette is flat - gradients introduce a visual register the system doesn't support.
- Don't set body text below 16px. The 18px body is paired with massive display type; shrinking body to 12-14px breaks the hierarchy rhythm.
- Don't add icons to body content, navigation, or section headers. The refresh icon in the hero is the only icon in the system - all other structure is pure typography.

Source prompt cues:

**Quick Color Reference**
- text: #282828 (Graphite)
- background: #fff5f2 (Bone canvas) or #1d1610 (Espresso dark)
- border: #282828 (Graphite, 1px)
- display heading: #000000 (Obsidian) on light, #fff5f2 (Bone) on dark
- primary action: no distinct CTA color

**Example Component Prompts**
1. *Create a full-bleed dark hero section:* Background #1d1610, no max-width. Display text 'P-2026.DA' at 197px, font-family 'wtqc' (substitute: Inter Tight), weight 300, line-height 1.0, letter-spacing -6.5px, color #fff5f2. The first and last fragments ('P-' and '.DA') in #282828 for internal contrast. A 12px monochrome refresh icon in #fff5f2 sits at top-right with a 1px #fff5f2 border, 0px radius.

2. *Create a section mega-header:* Background #ffffff, left-aligned text 'LATEST' at 120px, weight 300, letter-spacing -4px, color #000000. No underline, no border, no padding above - sits flush at section top.

3. *Create a 4-column info grid row:* Background #fff5f2, 4 equal columns with 32px gutters. Each column: header label in Inter 12px weight 400 #333333, body text in Inter 16px weight 400 #282828. Rows separated by 1px #282828 horizontal rules at 60% opacity. 24px vertical padding per row.

4. *Create a project image card:* Image fills container, 20px border-radius, no border, no shadow. Caption below: Inter 14px #333333, 12px gap between image edge and text.

5. *Create a bio statement block:* Max-width 900px, left-aligned, Inter 18px weight 400 line-height 1.78 #282828 on #ffffff background. Arrow glyphs ( ) between clauses. No border, no padding beyond the text block itself.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
