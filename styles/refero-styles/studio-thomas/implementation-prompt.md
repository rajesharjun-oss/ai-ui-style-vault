# AI Implementation Prompt

Build a Studio Thomas-inspired interface using this source-derived style bundle.

Reference site: https://studiothomas.co.uk
Theme: mixed
Category: Agency
North star: Alarm-orange broadcast panel on raw linen

Use these palette anchors:

- Signal Orange `#ff4f00` for Hero blocks, brand statement panels, full-bleed feature sections - the single chromatic commitment, used in large committed areas rather than small accents
- Ink Black `#000000` for Primary text, logo, hairline borders, dark UI elements, and display type on light surfaces
- Paper White `#ffffff` for Display headings overlaid on photography and colored panels, input fields, light surface level, inverse text on dark hero blocks
- Raw Linen `#ebe9e3` for Page canvas, footer background, secondary surface - warm off-white that softens the contrast between stark white and pure black
- Faint Stone `#767676` for Input field borders, low-emphasis form chrome - the only mid-tone in the system

Use these typography anchors:

- Moderat `--font-moderat` for Sole typeface - geometric sans-serif used at weight 300 for display and project names (120px) and weight 400 for body copy (16px). The light weight at display scale is a deliberate anti-shout: headlines whisper authority rather than declaring it, letting the orange blocks and editorial photography carry visual volume instead.

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: .
- Section gap: 100px.
- Card padding: 40px.
- Element gap: 20-30px.

Build these component patterns where relevant:

- Signal Orange Hero Block: Full-bleed brand statement panel
- Project Showcase Panel: Full-bleed editorial project card
- Wordmark Header: Minimal site identity
- Linen Footer: Closing section
- Hairline-Bordered Link: Text link with border treatment
- Text Input Field: Form input
- Category Caption: Project descriptor label
- View Project Link: Project CTA - text-only

Do:

- Use Signal Orange (#ff4f00) only in full, committed blocks - hero panels, section dividers, or accent rectangles. Never as a small dot, icon tint, or text color.
- Set display type at 120px weight 300 with line-height 1.0 and letter-spacing -0.004em. This is the signature scale - anything smaller undermines the editorial register.
- Use Raw Linen (#ebe9e3) as the page canvas, not pure white. The warm off-white is what separates this system from generic white-page SaaS layouts.
- Keep the header to a wordmark plus hamburger. Do not add nav links, search bars, or secondary actions to the top bar.
- Use weight 300 for all large-scale and display type. Reserve weight 400 for body copy (16px) and functional UI text.
- Let photography fill the entire viewport edge-to-edge for project showcases. Do not constrain to a max-width container or add margins.
- Space sections with 100px vertical gaps (footer token) and use 40px padding for contained content blocks.

Avoid:

- Do not introduce a secondary accent color. The system is monochromatic-plus-orange - adding blue, green, or any other hue dilutes the commitment.
- Do not use border-radius on any element. The system is edgeless - buttons, cards, inputs, and tags are all sharp-cornered (0px radius).
- Do not use bold or black weights (600-900). Moderat is loaded at 300 and 400 only; using heavier weights breaks the restrained voice.
- Do not add drop shadows, glows, or elevation effects. Surfaces are flat - separation comes from color blocks and full-bleed edges, not depth.
- Do not create a filled CTA button. The system has no ACTION_BACKGROUND evidence - interactions are text links and border-bordered text, not filled buttons.
- Do not wrap project photography in cards with borders, backgrounds, or padding. The image IS the container.
- Do not use gradients. The system is entirely flat color - no detected gradient usage anywhere.

Source prompt cues:

**Quick Color Reference**
- text: #000000 (Ink Black)
- background: #ebe9e3 (Raw Linen)
- border: #767676 (Faint Stone) for inputs, #000000 for hairlines
- accent: #ff4f00 (Signal Orange)
- inverse text: #ffffff (Paper White)
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Signal Orange Hero Block**: Full-bleed rectangle with #ff4f00 background. Centered headline at 120px, Moderat weight 300, #000000, line-height 1.0, letter-spacing -0.004em. Page canvas is #ebe9e3 with the wordmark 'Studio Thomas' at 16px weight 400, #000000, top-left, and a hamburger icon top-right.

2. **Full-Bleed Project Showcase**: Edge-to-edge photographic background. Project name in #ffffff at 120px, weight 300, line-height 1.0, positioned left-center. Category caption at 16px weight 400, #ffffff, bottom-left. 'View project' text link at 16px weight 400, #ffffff with a white border, bottom-right. No card, no border, no padding around the image.

3. **Wordmark Header**: Sticky top bar on #ebe9e3. Left: brand name in 16px weight 400, #000000. Right: three-line hamburger icon, #000000. No nav links, no buttons.

4. **Linen Footer**: Full-width section with #ebe9e3 background, 100px top padding, 50px bottom padding. Footer text at 16px weight 400, #000000.

5. **Text Input Field**: White (#ffffff) background, 1px border in #767676, text at 16px weight 400 in #000000. No border-radius, no shadow, no fill button beside it - submit is a text link or border-bordered text.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
