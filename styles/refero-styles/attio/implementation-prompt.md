# AI Implementation Prompt

Build a Attio-inspired interface using this source-derived style bundle.

Reference site: https://attio.com
Theme: light
Category: SaaS
North star: Architectural editorial on white marble

Use these palette anchors:

- Page Canvas `#ffffff` for Primary page background, card surfaces, button backgrounds
- Ink Black `#1c1d1f` for Primary heading and body text, logo mark
- Graphite `#232529` for Dark surface text, dark filled button background
- Obsidian `#101113` for Deepest text and dark surface fills
- Carbon `#2e3238` for Secondary dark text, nav states, button text on light fills
- Slate 500 `#505967` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Slate 600 `#6f7988` for Muted body text, secondary descriptions
- Slate 700 `#8f99a8` for Tertiary headings, captions, low-emphasis text
- Fog 400 `#9fa1a7` for Placeholder text, disabled states, subtle icons
- Mist 300 `#b5bdc9` for Muted body text, secondary copy
- Cloud 200 `#cad0d9` for Hairline borders on cards, input borders, dividers
- Cloud 100 `#d3d8df` for Card borders, surface boundaries
- Mist 50 `#e4e7ec` for Primary border color, dividers, subtle backgrounds, button borders
- Haze `#eeeff1` for Subtle background fills, section bands, inset borders
- Paper `#f4f5f6` for Alternate surface background, subtle elevated panels
- Cobalt Core `#266df0` for Primary brand accent - link text, focus rings, active states, highlighted icons, gradient midtone
- Cobalt Bright `#407ff2` for Secondary accent, hover states, decorative strokes in illustrations
- Cobalt Soft `#538bf3` for Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Periwinkle `#bad0fa` for Decorative card borders, subtle blue-tinted surface outlines
- Ice Wash `#e4edff` for Soft blue-tinted background, highlight washes, button box-shadow tints
- Onyx Footer `#000000` for Footer background, dark section backgrounds, high-contrast text on light

Use these typography anchors:

- Inter `--font-inter` for UI body - used for all body text, buttons, nav, links, card content, footers, icons. Weight 500 is the default for nearly all UI text (buttons, nav, body), giving Attio a slightly heavier, more confident UI voice than typical 400-only systems. Activated 'ss03' alternates give the text a distinctive geometric character.
- InterDisplay `--font-interdisplay` for Marketing headlines and display copy - weight 600 exclusively for large hero and section headings, with tight tracking (-0.015em to -0.02em) and near-1.0 line-heights creating dramatic, compact display blocks. The 56px size with -0.015em tracking is the signature hero voice. Activates 'ss03' and 'calt' for the same alternate character as Inter body.
- TiemposText `--font-tiempostext` for Editorial pull-quote and testimonial headings - a humanist serif that breaks the sans-serif system to create warmth and editorial weight. Used sparingly for quoted customer voices. This serif/sans contrast is the single most distinctive typographic choice in the system.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1440px.
- Section gap: 80-120px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Primary Filled Button: Main conversion action
- Secondary Outline Button: Companion action beside primary
- Ghost Text Button: Tertiary inline action
- Dark Inverted Button: Action on dark surfaces
- Tab Bar: Section navigation
- Product Screenshot Card: Product visual showcase
- Feature Card: Content card with description
- Logo Strip: Social proof / customer logos
- Eyebrow Pill / Tag: Section category label
- New Badge: Status indicator
- Promo Banner: Top-of-page announcement
- Chat Input Field: AI query input

Do:

- Use #266df0 (Cobalt Core) as the single accent for all interactive highlights, active states, and link text - never introduce additional saturated colors
- Set display headlines in InterDisplay weight 600 at 40-64px with tracking -0.015em to -0.02em and line-height 1.0-1.1
- Use 10px border-radius for all buttons and inputs, 7px for tags and badges, 11-14px for cards
- Apply blue-tinted shadows at very low opacity (rgba(28, 40, 64, 0.04) to rgba(28, 40, 64, 0.1)) - never use warm-gray or pure-black shadows
- Use Inter weight 500 as the default UI weight, not 400 - the slightly heavier weight is the system's default voice
- Activate 'ss03' on all Inter and InterDisplay text for the alternate geometric character
- Keep the max-width at 1440px and maintain 80-120px vertical gaps between major sections

Avoid:

- Don't use rounded buttons with radius above 12px - the 10px radius is part of the system identity
- Don't introduce secondary accent colors, gradients on buttons, or decorative color - one blue accent is the rule
- Don't use TiemposText for anything other than testimonial pull-quote headings - the serif/sans contrast is earned by rarity
- Don't use Inter weight 400 as a default - weight 500 carries the UI voice
- Don't apply shadows warmer than rgba(28, 40, 64, ...) - the blue-tinted shadow is deliberate, not neutral
- Don't use letter-spacing wider than 0 for body or heading text - the system is consistently tight-tracked
- Don't place the cobalt accent on filled backgrounds in body copy - it belongs to links, icons, and small interactive moments

Source prompt cues:

Quick Color Reference:
- text primary: #1c1d1f (Ink Black)
- text muted: #6f7988 (Slate 600)
- background: #ffffff (Page Canvas)
- border: #e4e7ec (Mist 50)
- accent: #266df0 (Cobalt Core)
- primary action: #232529 (filled action)

Example Component Prompts:

1. Create a Primary Action Button: #232529 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Create a product screenshot card: white background, 14px border-radius, shadow rgba(0,0,0,0.04) 0px 12px 30px 0px, zero internal padding, product UI image fills the card edge-to-edge.

3. Create a section with eyebrow pill + heading + body: Eyebrow pill (7px radius, 1px border #e4e7ec, Inter 12px weight 500, #6f7988 text, 8px 12px padding). Heading at 40px InterDisplay 600, #1c1d1f, tracking -0.4px. Body at 16px Inter weight 500, #6f7988, line-height 1.38.

4. Create a chat input field: white background, 1px border #e4e7ec, 12px radius, shadow rgba(28,40,64,0.06) 0px 2px 6px 0px. Placeholder in #9fa1a7 (Fog 400) Inter 15px weight 500. Send button: 28px square, #266df0 background, 7px radius, white arrow icon.

5. Create a footer: full-bleed #000000 background, 4-column grid with column titles (Inter 15px weight 500, #b5bdc9) and links below (Inter 14px weight 500, #ffffff). Logo + wordmark in white at top-left, 80-120px vertical padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
