# AI Implementation Prompt

Build a Perk-inspired interface using this source-derived style bundle.

Reference site: https://travelperk.com
Theme: light
Category: SaaS
North star: electric lime on warm parchment paper

Use these palette anchors:

- Electric Lime `#beff50` for Primary action background, hero surface fills, accent panels - the singular chromatic charge against an otherwise achromatic system, creating brand presence through contrast not decoration
- Off-Black Ink `#14140f` for Body text, headings, icon fills, link borders, button text - warm-tinted near-black that feels less clinical than pure black against parchment
- Off-White Canvas `#f5f5eb` for Card surfaces, secondary page background - warm parchment replacing cold white as the resting surface for the lime accent
- Pure White `#ffffff` for Highest surface level, card fills, input fields - used where clean white needs to lift above the parchment
- Ash `#d2d2c8` for Borders, dividers, subtle structural lines, inactive backgrounds - the warm gray that separates surfaces without harshness
- Graphite `#6e6e64` for Muted body text, secondary copy, card text - warm gray for de-emphasized information
- Deep Charcoal `#30302a` for Dark card surfaces, inverted blocks - for rare moments when the page flips to a dark island
- Stone `#919183` for Faint borders, decorative strokes - only visible at fine stroke widths
- Smoke `#b9b9b7` for Placeholder backgrounds, subtle wash zones

Use these typography anchors:

- OTSono `--font-otsono` for Single-family system covering everything from 90px display headlines (weight 500, line-height 0.89, tracking -0.03em) through 16px body (weight 400, line-height 1.5) to 10px micro-labels. Weight 500 is the emphasis voice used on headings, labels, and CTAs; weight 400 handles body, icons, and supporting text. The 0.1em tracking on small caps is reserved for eyebrow labels and category tags.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80-120px.
- Card padding: 32-48px.
- Element gap: 16-24px.

Build these component patterns where relevant:

- Primary Action Button (Lime Pill): Filled CTA on warm-white backgrounds
- Ghost Text Button: Inline navigation and secondary actions
- Underline Link: In-content navigation and emphasis links
- Parallax Card: Product feature card on parchment surface
- White Surface Card: Elevated content card or form container
- Dark Island Card: Inverted feature block
- Lime Accent Block: Hero band or feature highlight surface
- Inline Label Tag: Category eyebrow or status pill
- Input Field: Form text input
- Section Divider: Horizontal structural separator
- Icon Container: Feature icon or category indicator
- Logo Mark: Brand identity lockup

Do:

- Use #beff50 as the ONLY filled button color - never introduce a second chromatic action color
- Set border-radius to 28px on all cards and primary buttons, 9999px on pills and tags
- Use OTSono weight 500 for all headings, labels, and CTAs; weight 400 for body and supporting text
- Apply letter-spacing -0.03em to any text at 28px and above; let body text use default tracking
- Build the surface stack as white parchment (#f5f5eb) lime (#beff50) - never use shadows to separate layers
- Use 0.1em tracking with uppercase for category eyebrows at 10-12px
- Let the off-black #14140f carry all text - never use pure #000000 except in input fields
- Keep section gaps between 80-120px to maintain the editorial breathing rhythm

Avoid:

- Do not add box-shadows to cards - the system relies on tonal contrast, not elevation
- Do not use #000000 for body text - #14140f is warmer and more on-brand
- Do not introduce blue, red, or any secondary accent color - the lime is the only chromatic voice
- Do not mix border-radius values within the same component type (all buttons are 28px, all pills are 9999px)
- Do not use system fonts as fallback for display sizes - OTSono at 60px+ with -0.03em tracking is signature
- Do not place lime buttons on white surfaces without sufficient padding - the contrast is loud, give it room
- Do not use 600 or 700 weights - the system operates on 400 and 500 only
- Do not add gradients - the lime is already saturated; gradients would muddy it

Source prompt cues:

Quick Color Reference:
- Text: #14140f
- Background (canvas): #ffffff
- Background (card/surface): #f5f5eb
- Border/divider: #d2d2c8
- Accent surface: #beff50
- primary action: #beff50 (filled action)

Example Component Prompts:

1. Create a Primary Action Button: #beff50 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Create a feature card grid: 3 columns on white canvas. Each card: background #ffffff, border-radius 28px, padding 40px, no shadow. Category eyebrow label at 12px OTSono weight 500, uppercase, letter-spacing 0.1em, color #6e6e64. Card title at 28px OTSono weight 500, color #14140f, letter-spacing -0.02em. Body text at 16px OTSono weight 400, color #6e6e64.

3. Create a lime accent panel: full-bleed #beff50 background, generous padding (80px vertical). Centered display text at 80px OTSono weight 500, color #14140f, letter-spacing -0.03em, line-height 0.9. Below: ghost text button (transparent background, #14140f text, 1px underline border).


5. Create a dark footer section: background #14140f, padding 80px. Multi-column layout with link lists. All text in #f5f5eb at 14px OTSono weight 400. Section headers at 12px uppercase, letter-spacing 0.1em, weight 500, color #d2d2c8.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
