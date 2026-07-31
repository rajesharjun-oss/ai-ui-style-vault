# AI Implementation Prompt

Build a Co Projects-inspired interface using this source-derived style bundle.

Reference site: https://co-projects.xyz
Theme: light
Category: Agency
North star: black geometric sculpture on white void. Massive circular forms carved from a pure white gallery wall, where the only type is whisper-weight 400 and the only accent is the void between things.

Use these palette anchors:

- Paper White `#ffffff` for Page canvas, background of all surfaces, inner counter of the ring forms - the negative space that gives the black marks their mass
- Graphite Ink `#000000` for Primary mark fill, text, and the large circular ring forms. The sole chromatic-payload element in the system
- Fog Hairline `#e5e7eb` for Hairline borders, structural dividers, and subtle separator rules at 1px. The only gray in the palette and it never fills - it only divides

Use these typography anchors:

- Alpha `--font-alpha` for Primary face for nav, body, and display. Used at 16px for navigation labels and links (lineHeight 1.50), 29px for mid-scale headings, and 60px for the display headline (lineHeight 1.00 - headline sits tight on its baseline). The signature move is running 60px display text at weight 400, which reads as architectural line-drawing rather than shouted headline
- Takt `--font-takt` for Secondary face for body copy and 36px subheadings. Tight lineHeight (1.10-1.11) at all sizes gives it a compact, editorial-block feel - runs in long stacked paragraphs where Alpha would feel too austere. Weight 400 is the ONLY weight in the entire system

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: .
- Section gap: .
- Card padding: 32px.
- Element gap: 8px.

Build these component patterns where relevant:

- Sparse Top Navigation: Primary site navigation
- Geometric Ring Hero: Brand-defining visual composition
- Display Headline Block: Primary text statement on hero
- Subhead Text Block: Secondary descriptive copy
- Hairline Divider: Structural section separator
- Text-Link Nav Item: Inline navigation element
- Body Paragraph: Long-form descriptive text
- Image Placeholder Counter: Visual break / negative space element

Do:

- Use only the three palette colors: #ffffff for canvas, #000000 for ink and geometric fills, #e5e7eb exclusively for 1px hairline dividers
- Set all type to weight 400 - never bold, never medium, never light. The system has exactly one weight and that constraint is the brand
- Apply 139-208px vertical margins between major sections to maintain gallery-scale breathing room
- Let geometric ring/circle forms occupy 50-70% of the viewport to create the architectural scale contrast with 16px nav text
- Use Alpha at 60px / lineHeight 1.00 for display headlines and Takt at 36px / lineHeight 1.11 for subhead blocks
- Position navigation as three sparse text labels at the top corners - no bar, no background, no border
- Set border-radius to 0 on all rectangular elements; reserve all rounding for intentional circular geometry

Avoid:

- Never add a shadow, blur, or elevation effect - the system is completely flat and any depth cue breaks the figure/ground purity
- Never introduce a color outside the three achromatic tokens - no accent hues, no tinted grays, no hover-state colors beyond opacity shifts
- Never use a font weight other than 400 - no 500, 600, 700, or 800 under any circumstance
- Never apply border-radius to buttons, cards, tags, or inputs - rectangular means sharp corners, always
- Never constrain the hero composition to a max-width container - let the geometric forms run full-bleed and crop at viewport edges
- Never add icons, illustrations, photography, or decorative graphics - the circle/ring IS the imagery
- Never use letter-spacing adjustment - all type sits at default tracking, the custom typefaces are already tuned

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #ffffff
- border: #e5e7eb (1px hairline only)
- accent: #000000 (black is the accent in a monochrome system)
- primary action: no distinct CTA color

Example Component Prompts:

1. Create a full-bleed hero section: #ffffff background, no max-width constraint. A massive black ring (#000000 fill, outer diameter ~70% viewport height, inner counter ~40% diameter revealing #ffffff) positioned to crop at both left and right viewport edges. Display headline in Alpha at 60px / weight 400 / lineHeight 1.00, color #000000, positioned 139px from top edge.

2. Create a sparse top navigation: three text links in Alpha at 16px / weight 400 / lineHeight 1.50, color #000000. First link at top-left (0px, 0px), second at top-center, third at top-right. No background, no border, no padding, no underline. Sits as floating text on bare white canvas.

3. Create a subhead text block: Takt font at 36px / weight 400 / lineHeight 1.11, color #000000. Left-aligned paragraph block, no max-width constraint beyond natural reading flow, 32px gap above and below to neighboring elements.

4. Create a section divider: a single 1px solid #e5e7eb rule spanning the full viewport width, with 96-139px vertical margin above and below. No other styling - the hairline is the entire component.

5. Create a body paragraph: Takt at 16px / weight 400 / lineHeight 1.50, color #000000. Single-column block, left-aligned, 32px column-gap between successive paragraphs. No border, no background, no indent.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
