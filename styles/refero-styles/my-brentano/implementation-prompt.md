# AI Implementation Prompt

Build a My Brentano-inspired interface using this source-derived style bundle.

Reference site: https://mybrentano.ch
Theme: light
Category: E-commerce
North star: Pharmacy broadsheet on cream paper. A Swiss editorial layout where one typewriter voice does all the speaking and warm-toned product photography supplies the only color.

Use these palette anchors:

- Charcoal Ink `#212529` for Body text, headings, nav text, footer text, most borders - the dominant text and structural color, slightly softer than pure black for warmth
- Pure Press `#000000` for Secondary text, button borders, link borders, input outlines, nav separators - true black for maximum contrast on outlined elements
- Bone White `#ffffff` for Page canvas, card surfaces, button fills, input backgrounds - the ground that all ink sits on

Use these typography anchors:

- Studio Feixen Sans Writer Book Regular `--font-studio-feixen-sans-writer-book-regular` for Studio Feixen Sans Writer Book Regular - detected in extracted data but not described by AI
- Studio Feixen Sans Writer `--font-studio-feixen-sans-writer` for Primary typeface for all text - body, headings, nav, links, buttons, lists. The Writer variant carries a typewriter/letterpress quality with subtle ink-trapped details that a geometric sans cannot replicate. Weight 700 is used sparingly only on the 60px display; everything else stays at 400, making the single bold moment feel intentional and declarative.
- Studio Feixen Sans `--font-studio-feixen-sans` for Secondary sans variant for select body passages and inputs where the typewriter serifs would be too loud. The same family, stripped of the Writer details, creates a quiet alternation within the same typographic world.

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: .
- Section gap: 40-60px.
- Card padding: .
- Element gap: 10px.

Build these component patterns where relevant:

- Circular Nav Arrow Button: Navigation link with directional affordance
- Language Selector Pill: Locale switcher
- Editorial Display Headline: Hero and section H1
- Section Heading: H2/H3 within content blocks
- Body Paragraph: Long-form description text
- Offset Image Stack: Product/editorial imagery placement
- Text Link: Inline navigation and reference
- Outlined Action Button: Interactive controls (implied from nav pattern)
- Shopping Bag Icon: Cart access in top-right
- Top Navigation Bar: Primary site navigation

Do:

- Use Studio Feixen Sans Writer at 60px weight 700 for the single most important headline on any page
- Set body text at 15-18px with line-height between 1.67 and 2.08 - never tighter than 1.5
- Use 0px border-radius on all images, inputs, and rectangular elements; reserve 9999px exclusively for circular nav controls
- Separate the top nav from page content with a single 1px #000000 hairline - no background fill, no shadow
- Let product imagery supply all color; keep UI strictly in Charcoal Ink (#212529), Pure Press (#000000), and Bone White (#ffffff)
- Break the grid by rotating overlapping product images 2-5 rather than aligning them perfectly
- Use 10px gaps for inline element spacing, 40-60px for vertical section rhythm

Avoid:

- Never introduce an accent or brand color - the system is intentionally near-monochrome, and color belongs only to photography
- Never apply shadows, glows, or any form of elevation - surfaces must remain flat like printed paper
- Never use bold weight (700) for anything smaller than 30px - the single bold moment must remain monumental
- Never round corners on cards, images, or input fields - 0px radius is non-negotiable
- Never use more than two typefaces per view; alternate between Writer and Sans within the same family only
- Never center-align body paragraphs or set them narrower than 50% of the viewport - the grid is left-aligned and generous
- Never apply a colored background to the page - the cream warmth comes from the paper-tone canvas and the imagery, not from a tint

Source prompt cues:

**Quick Color Reference**
- text: #212529 (Charcoal Ink)
- background: #ffffff (Bone White)
- border: #000000 (Pure Press)
- accent: none - color exists only in product photography
- primary action: no distinct CTA color

**3 Example Component Prompts**

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. *Body text block with offset images*: Above the text, place two rectangular product photographs (0px radius) overlapping at a 3 clockwise rotation on the right side of the layout, with the leftmost image slightly larger and the right image cropped to show a warm mustard-yellow cream swirl. Below, two paragraphs of body text at 18px Writer weight 400, line-height 2.08, color #212529, left-aligned, occupying roughly 45% of the viewport width. No background, no border around the text.

3. *Outlined nav button*: A 40px circle with 1px #000000 border, transparent fill. Inside, a right-arrow glyph ( ) in #212529 at 15px Writer weight 400, vertically and horizontally centered. No hover fill, no shadow - on hover, optionally invert to a #000000 fill with a white arrow, but the default state is strictly outlined.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
