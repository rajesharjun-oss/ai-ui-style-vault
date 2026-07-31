# AI Implementation Prompt

Build a Iad-lab-inspired interface using this source-derived style bundle.

Reference site: https://iad-lab.ch
Theme: dark
Category: Design
North star: art-school exhibition on charcoal

Use these palette anchors:

- Charcoal Canvas `#222222` for Page background, the dominant surface across all sections and the base layer behind full-bleed photography
- Bone `#f8f8f8` for All body text, meta labels, navigation dots, and the dominant hairline border color - serves as the single foreground tone in this near-monochrome system
- Graphite `#2a2b2d` for Secondary icon strokes, subtle list dividers, and muted fill details - sits one step darker than the canvas for low-contrast decoration
- Ash `#757577` for Inactive or resting state for navigation dots and quiet UI affordances

Use these typography anchors:

- Neue Haas Unica `--font-neue-haas-unica` for The sole text family for all UI copy: meta labels at 16px, body at 18px, list/links at 24px, subheadings at 27px, section headings at 36px. Weight 400 is default; 700 is reserved for emphasis in the meta block and active labels. The 1.10 lineHeight on 36px headings creates tight, architectural vertical rhythm.
- Display (custom or system fallback) `--font-display-custom-or-system-fallback` for Reserved exclusively for the two program words ('IMAGINE', 'PROGRAM') that span the full viewport width and bleed past both edges. This face is wide, heavy, with rounded terminals - it is the visual signature of the entire site and carries the brand's identity more than any other element. When recreating, use a heavy extended grotesque (e.g. Obviously Wide Black, Neue Machina Black) at a size that forces letter cropping at the viewport edges.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 40px.
- Card padding: 24px.
- Element gap: 24px.

Build these component patterns where relevant:

- Full-Bleed Program Word: Brand-defining display heading
- Meta Label Block: Contextual site identity
- Section Navigation Dots: Sole navigation control
- Full-Bleed Photographic Panel: Visual content section
- List Item with Hairline Border: Content links or project entries
- Rounded Interactive Surface: Buttons, tags, or clickable chips
- Quiet Text Section: Interstitial content between visual panels

Do:

- Use #f8f8f8 for all text and borders; #222222 is the only background. This binary is the system.
- Apply 20px border-radius to any rounded element - buttons, tags, chips, containers. Never use sharp corners on interactive surfaces.
- Set the display heading to overflow the viewport. The wordmark must bleed past both left and right edges - if all letters are fully visible, it is too small.
- Use Neue Haas Unica weight 400 as default; reserve weight 700 for active or emphasized labels only. Do not mix intermediate weights.
- Separate list items with 1px solid #f8f8f8 bottom borders. This hairline divider is the primary structural separator in the system.
- Use 24px as the default element gap and 16px as the tight gap. Maintain the 4px base unit for all spacing decisions.
- Let photography fill 100vw with zero padding or border-radius. Full-bleed is non-negotiable for visual panels.

Avoid:

- Do not introduce any color beyond the four neutrals (#222222, #f8f8f8, #2a2b2d, #757577). Chromatic accents are forbidden.
- Do not add drop shadows, gradients, or glow effects. Elevation is communicated through photography scale, not CSS shadows.
- Do not add a traditional navigation bar, header, or footer chrome. The meta label and dot navigation are the entire structural frame.
- Do not center text in narrow columns. Text should be short, left-aligned, and surrounded by generous negative space.
- Do not use border-radius values other than 15px or 20px. Avoid 4px, 8px, or fully rounded (9999px) - neither matches the system's geometric language.
- Do not set the display heading at a size where all letters fit within the viewport. The cropping is intentional and defines the visual identity.
- Do not use line-height above 1.35 for body text or below 1.10 for headings. The tight heading leading creates the architectural feel.

Source prompt cues:

**Quick Color Reference**
- text: #f8f8f8
- background: #222222
- border: #f8f8f8 (1px hairline)
- muted: #2a2b2d
- inactive: #757577
- primary action: no distinct CTA color

**Example Component Prompts**

1. Create a full-bleed display wordmark: a single word at 200px+ in a heavy, wide, rounded display face (weight 900), color #f8f8f8, positioned flush to the viewport top, intentionally overflowing left and right edges. No padding, no background. On a #222222 canvas.

2. Create a meta label block: four stacked lines of text at 16px Neue Haas Unica weight 400, line-height 1.30, color #f8f8f8, positioned 16px from the top-left corner. No container, no border. Reads as floating text on the dark canvas.

3. Create a section navigation indicator: three 8px circles vertically stacked at 24px from the right viewport edge, vertically centered. First circle filled #f8f8f8 (active state), remaining two are 1px outlined #f8f8f8 with transparent fill.

4. Create a full-bleed photographic panel: a single image filling 100vw and ~80vh with zero padding, zero border-radius, and no border. The image is abstract, high-saturation, large-scale material subject (petal, paper, 3D form). Edges are hard - no gradient fade to canvas.

5. Create a list of linked items: each item is a single line of text in Neue Haas Unica 24px weight 400, color #f8f8f8, separated by a 1px solid #f8f8f8 bottom border. No padding between items beyond 24px vertical gap. No background on items. Full-bleed width - items span edge to edge.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
