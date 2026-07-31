# AI Implementation Prompt

Build a jun.works-inspired interface using this source-derived style bundle.

Reference site: https://jun.works
Theme: light
Category: Design
North star: printed editorial zine with sticker labels - black ink on bright white, nothing else

Use these palette anchors:

- Press Black `#000000` for Body text, all borders, pill outlines, button strokes - the sole ink color, used at full opacity for every foreground element
- Bone White `#ffffff` for Page canvas, card surfaces, pill fills - the only surface color, creating maximum contrast against Press Black
- Smoke Gray `#cccccc` for Hairline dividers, muted outlines, secondary borders where a softer separation is needed

Use these typography anchors:

- Standard `--font-standard` for Display and heading type only - a custom geometric sans used at two large sizes with extreme negative tracking (-0.045em to -0.054em). Also sets link and button text. The single weight (400) and tight tracking create a compressed, poster-like presence that dominates the page. No bold variant exists; hierarchy is achieved through size and tracking alone.
- Times `--font-times` for Body and micro-copy type - the system serif at 13px, used in editorial contexts (footnotes, annotations, fine print). The serif/sans collision with Standard is deliberate: the sans shouts, the serif footnotes.

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: .
- Section gap: 52px.
- Card padding: 19px.
- Element gap: 13px.

Build these component patterns where relevant:

- Pill Button: All clickable actions - nav toggles, social links, CTAs
- Pill Section Label: Category headers like 'Service', 'Clients', 'Recognition'
- Display Heading: Page-level statements and paragraph introductions
- Body Paragraph: Primary prose content - bio text, descriptions
- Dashed List Item: Service offerings, client names, recognition entries
- Footnote Link: Superscript annotations referencing email, social, etc.
- Social Pill Row: External profile links (LinkedIn, Instagram, Soot, Behance)
- Logo Lockup: Brand mark at top-left of page
- Hamburger Toggle: Menu trigger at top-right
- Two-Column Content Grid: Service/Clients/Recognition layout

Do:

- Use 129.6px border-radius on every interactive element - no rectangles, no modest rounding
- Set all display text in Standard at 45-54px with -0.045em to -0.054em letter-spacing
- Render body text in Times serif with ~1.70 line-height for editorial breathing room
- Anchor all content to the left edge - no centering, no max-width containers
- Prefix list items with an em-dash (-) instead of bullets or numbers
- Use #000000 for all borders, text, and outlines - never introduce color
- Maintain #ffffff backgrounds everywhere; let the 1px black border define shape, not fill

Avoid:

- Never add color - no accent, no semantic green/red/yellow, no brand color
- Never use box-shadow or elevation - depth comes from border definition, not shadow
- Never use border-radius below 129.6px on any element
- Never bold the display type - Standard ships in one weight (400) and that restraint is the system
- Never use a sans-serif for body text - the serif/sans split is structural, not optional
- Never center-align headings or body paragraphs
- Never add imagery, photography, or illustration - the page is pure typography and label geometry

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #ffffff
- border: #000000
- muted border: #cccccc
- accent: none
- primary action: no distinct CTA color

3-5 Example Component Prompts:
1. Create a display heading: 'Selected Work' in Standard font, 54px, weight 400, #000000, letter-spacing -2.916px (or -0.054em). Line-height 1.12. Left-aligned, no margin.

2. Create a pill-shaped navigation button: 1px solid #000000 border, #ffffff fill, 129.6px border-radius, padding 5px 18px 3px 19px. Label text in Standard font, #000000. No shadow, no gradient.

3. Create a two-column service list: Left column headed by an inverted pill label ('Service' - #000000 fill, #ffffff text, 129.6px radius), followed by lines prefixed with em-dash (-) in Standard font at 45px. Right column mirrors with 'Clients' label and client names. 26px horizontal padding per column, 13px vertical gap between items.

4. Create a body paragraph: Times serif, ~1.70 line-height, #000000, left-aligned, running edge-to-edge with no max-width. Use normal letter-spacing.

5. Create a social link pill row: horizontal flex of 4 pills, each with 129.6px radius, 1px #000000 border, white fill. Labels: 'LinkedIn', 'Instagram', 'Soot', 'Behance' in Standard font. 13px gap between pills.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
