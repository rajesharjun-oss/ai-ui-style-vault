# AI Implementation Prompt

Build a ARTWORLD-inspired interface using this source-derived style bundle.

Reference site: https://artworld.agency
Theme: light
Category: Agency
North star: fashion masthead on white linen

Use these palette anchors:

- Ink Black `#000000` for All text, the ARTWORLD wordmark, hairline structural borders, link strokes - the only mark-making color in the entire system
- Paper White `#ffffff` for Page canvas, negative space between type, reverse text on the wordmark bar

Use these typography anchors:

- Graphik Light `--font-graphik-light` for The invisible support system - body text, captions, metadata, role tags, the legend, the info link. Weight 300 is deliberately thin: it recedes so the Cardinal Fruit can dominate. This is the typographic equivalent of using whisper voice in a conversation where someone else is speaking. The consistent -0.065em letter-spacing tightens the already-light forms, giving the sans-serif an editorial density that prevents it from feeling like default UI text.
- Cardinal Fruit (and Italic / Classic Italic variants) `--font-cardinal-fruit-and-italic-classic-italic-variants` for The editorial display voice - used for talent names, artist credits, and any moment of typographic expression. The italic variant carries the romantic, fashion-magazine feeling while the upright version provides structural headlines. Custom serif with high contrast strokes, used at extreme sizes (65-75px) to dominate the page. The whisper weight (300) on such a large serif is anti-convention: most editorial serifs use 400-700 here, but the light cuts create airier letterforms that feel more printed than digital.
- Cardinal Fruit Italic `--font-cardinal-fruit-italic` for Cardinal Fruit Italic - detected in extracted data but not described by AI
- Cardinal Classic Italic `--font-cardinal-classic-italic` for Cardinal Classic Italic - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: .
- Section gap: 76-95px.
- Card padding: 30px.
- Element gap: 20px.

Build these component patterns where relevant:

- Talent Name Cell: Primary unit of the talent grid - individual artist/creator name in the credits section
- Role Legend: Key explaining the superscript role tags in the talent grid
- ARTWORLD Wordmark: Brand identifier and visual anchor - the page's only large-scale graphic element
- Info Link: Persistent utility link, likely to contact or about details
- Credits Grid: The main content surface - a multi-row, multi-column layout of talent name cells

Do:

- Use only #000000 and #ffffff. Any introduction of grey, tint, or color breaks the monochrome contract.
- Set all display type in Cardinal Fruit (upright or italic) at 65-75px with weight 300. The whisper weight is non-negotiable - it creates the airiness that makes the type feel printed, not digital.
- Set all body and supporting type in Graphik Light at weight 300. Do not promote to Regular or Medium; the thinness is the point.
- Use the two type families as a system of contrast: Cardinal Fruit speaks, Graphik Light stays quiet. Never let Graphik Light appear at sizes that compete with Cardinal Fruit.
- Maintain tight letter-spacing: -0.065em for Graphik Light, -0.010 to -0.031em for Cardinal Fruit. This tracking is what gives the type its editorial density.
- Keep all spacing generous - 76-95px between major sections, 20-30px between elements. This is a spacious design that breathes.
- Left-align everything. Center-alignment would break the ragged editorial grid that gives the page its fashion-magazine rhythm.

Avoid:

- Do not add any color beyond black and white. No accent colors, no state colors, no hover tints. Monochrome is the brand.
- Do not use rounded corners. Every edge is sharp, every surface is flat. The system has no curves.
- Do not add shadows, gradients, or elevation effects. The design is completely flat - depth comes from type size contrast, not from visual effects.
- Do not use bold or semibold weights for body or display type. The system lives at 300. Heavier weights break the whisper voice.
- Do not use system sans-serifs (Arial, Helvetica, Roboto) as substitutes for Graphik Light. The lightness and tight tracking of Graphik are what make it disappear correctly.
- Do not center-align body text or grid items. The ragged left edge is a design feature, not a limitation.
- Do not add icons, illustrations, photography, or decorative graphics. This is a typography-only system. The wordmark is the only visual element that isn't running text.

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border: #000000 (1px hairline)
- accent: no distinct accent color
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. Create a talent name cell: white background. Name in Cardinal Fruit Italic, 18px, weight 300, color #000000, letter-spacing -0.198px. Immediately after the name, a superscript role tag in the same font at 12px, raised 4px. No border, no background, no padding - just type sitting on the page.

2. Create a section legend: horizontal row at the bottom of a credits grid, set in Graphik Light 12px weight 300, color #000000, letter-spacing -0.78px. Items separated by 29px horizontal padding. Format each item as a parenthetical letter followed by a lowercase label, e.g. '(P) Photographer'.

3. Create the ARTWORLD wordmark: set 'ARTWORLD' in a heavy bold sans-serif (Neue Haas Grotesk Display or Inter at weight 900) at 120-150px, line-height 1.00, letter-spacing -0.02em, color #000000, left-aligned, spanning the full viewport width. No margin above - it should sit directly against the preceding content with the page's standard 76-95px section gap.

4. Create a credits grid container: white background, no border, no padding. 3-column grid with 95px column gap and 20px row gap. Each grid cell is a talent name cell (see component 1). Grid is left-aligned within the page - no centering, no max-width constraint.

5. Create an info link: Cardinal Fruit Italic 12px, weight 300, color #000000, no underline, positioned bottom-right of the page with 30px padding from the viewport edge. The italic serif itself signals clickability - no hover treatment needed beyond the existing #000000 color.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
