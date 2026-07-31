# AI Implementation Prompt

Build a Limitless-inspired interface using this source-derived style bundle.

Reference site: https://limitless.ai
Theme: light
Category: AI
North star: monochrome editorial on plaster white. A single weight-contrast typeface, no accent color, and one violet spark - the system achieves identity through restraint, not decoration.

Use these palette anchors:

- Plaster `#f2f3f5` for Page background, full-bleed canvas
- Mist `#e5e7eb` for Card surfaces, placeholder image wells, subtle inset zones
- Chalk `#ffffff` for Elevated card surfaces when differentiation from Plaster is needed
- Hairline `#d1d5db` for Stronger dividers, disabled icon strokes, secondary borders
- Inkstone `#0f172a` for Primary heading text, high-emphasis body copy, nav logo wordmark
- Slate `#334155` for Secondary headings, medium-emphasis text, icon strokes
- Graphite `#475569` for Body text, nav links, button labels - the everyday workhorse neutral
- Pewter `#64748b` for Muted helper text, secondary links, metadata
- Fog `#939eae` for Disabled state text, tertiary captions, low-emphasis labels
- Obsidian `#000000` for Maximum-contrast text where #0f172a still feels too soft (rare)
- Spark Violet `#6d4aff` for Wordmark icon and the sole chromatic accent in the entire system - used at the smallest possible size to mark the brand without coloring the interface

Use these typography anchors:

- Greycliff `--font-greycliff` for Single-family system. Weight 300 carries display (60px) and large headings (36px) for a quiet, editorial whisper. Weight 400-500 handles body (16-18px) and UI labels. Weight 600-700 reserved for emphasis and the wordmark. Because there is no secondary face, the system creates rhythm purely through weight and size contrast inside one typeface.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 48px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Display Heading: Hero and page-level titles
- Section Heading: H2-level headings
- Body Paragraph: Long-form content
- Pill Button: Primary and secondary actions
- Nav Link: Top navigation items
- Brand Mark / Wordmark: Logo in nav
- Hero Image Well: Large media placeholder on the landing surface
- Content Card: General-purpose surface for grouped content
- Article / Message Block: Long-form communication (CEO message, legal text)
- Inset Placeholder: Empty-state or media slot inside a content area
- Footer: Page-bottom utility links

Do:

- Use Greycliff weight 300 for any text 30px and above - the light weight is the brand's voice, not a fallback
- Maintain letter-spacing of -0.025em on display and heading sizes; let it relax to normal at body sizes
- Keep the palette monochromatic on the page surface - introduce the violet spark (#6d4aff) only in the wordmark icon, never as a button fill, border, or background
- Use 16px border-radius for all cards and image wells; use 9999px (full pill) for all buttons, tags, and avatars
- Apply the single shadow (rgba(30, 41, 59, 0.15) 0px 25px 50px -12px) only to the hero media well - do not propagate it to cards or modals
- Set body text to #334155 and nav/UI text to #475569 - reserve #0f172a for headings and the wordmark
- Use 8px and 16px for inline element gaps; jump to 48px or 64px between sections; never use 24px as a section gap

Avoid:

- Do not introduce a second typeface - the system is single-family by design
- Do not use weight 700 on headings; weight 300 is the display treatment and weight 500-600 is the UI treatment
- Do not use a chromatic color as a button background, link color, or badge fill - the interface is intentionally colorless
- Do not add borders to cards that sit on #f2f3f5; let the white-on-plaster contrast do the work
- Do not center display headings - they are always left-aligned with the content column
- Do not use sharp corners (0-4px radius) on any surface - the system reads rounded or pill, never squared
- Do not stack multiple shadow layers or add glow effects - one shadow, used once, is the rule

Source prompt cues:

**Quick Color Reference**
- text (heading): #0f172a
- text (body): #334155
- text (muted): #64748b
- background (page): #f2f3f5
- background (card): #ffffff
- border / divider: #e5e7eb
- accent: #6d4aff (wordmark icon only)
- primary action: no distinct CTA color

**Example Component Prompts**
1. Hero section: #f2f3f5 page background. Headline at 60px Greycliff weight 300, #0f172a, letter-spacing -1.5px, line-height 1.0, left-aligned. Below it, a #e5e7eb image well at 16px radius, minimum 360px tall, with the shadow rgba(30, 41, 59, 0.15) 0px 25px 50px -12px and a centered #939eae line-icon.
2. Section heading block: 36px Greycliff weight 300, #0f172a, letter-spacing -0.9px, line-height 1.11. 48px of space above.
3. Body paragraph: 16px Greycliff weight 400, #334155, line-height 1.63, max-width 680px. Inline links in #475569 with underline.
4. Ghost nav button: transparent background, 1px #e5e7eb border, 9999px radius, 8px 16px padding, 16px Greycliff weight 500, #475569 text. Hover shifts text to #0f172a.
5. Content card: #ffffff background, 16px radius, 24px padding, no border, no shadow. Sits on the #f2f3f5 canvas with tone-on-tone contrast.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
