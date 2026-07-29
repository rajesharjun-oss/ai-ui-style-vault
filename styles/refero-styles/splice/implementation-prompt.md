# AI Implementation Prompt

Build a Splice-inspired interface using this source-derived style bundle.

Reference site: https://splice.com
Theme: dark
Category: Media
North star: midnight recording studio - a dark, weightless space where the only thing that ever gets loud is the music.

Use these palette anchors:

- Signal Blue `#528fff` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Button Blue `#1253ff` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Voltage Yellow `#f1f607` for Rare text accent - highlight punctuation, featured labels, emphasis. Used sparingly, only when a word needs to flash against the dark canvas. Never on backgrounds
- Carbon `#121214` for Primary page canvas, card surfaces, input fields, footer. The dominant working surface at 425 occurrences across every context
- Obsidian `#000000` for Deepest dark - image containers, nav surface, full-bleed backgrounds. Creates the bottom of the surface stack
- Platinum `#ffffff` for Primary text, inverted button text, icon fills. The only true white in the system; appears 1506 times across every text context
- Graphite `#232426` for Dominant canvas background, secondary button surface. Sits one step lighter than Carbon, used when a surface needs to feel like a different plane without using shadow
- Fog `#a6a8ad` for Muted text, nav items, secondary labels, inactive links. The first step down from white in the type hierarchy
- Ash `#c8c9cc` for Button borders, icon strokes, hairline dividers, ghost control outlines. The border that doesn't feel like a border
- Slate `#63656d` for Borders, dividers, inactive controls. Darker than Ash for when a divider needs to recede further
- Iron `#45464d` for Elevated surfaces, button borders, nav separators. The highest dark in the stack - used for the 1px inset stroke that replaces shadows

Use these typography anchors:

- InterVariable (custom) `--font-intervariable-custom` for Workhorse for all UI text - body, nav, buttons, inputs, cards, footer. The variable axis allows weight shifts (400 500 600 700) within a single family. Universal -0.015em tracking creates a compact, efficient reading rhythm across every size.
- SoehneBreit (custom) `--font-soehnebreit-custom` for Editorial display headlines. The wider, geometric cut of SoehneBreit at weight 400 creates a distinctive voice - headlines don't shout, they announce with quiet authority. The 0.071em tracking (applied at 14px) appears on uppercase eyebrow labels, creating the system's only wide-tracked text. Weight 400 only - bold is never used.
- Soehne (custom) `--font-soehne-custom` for Subheadings - bridges the gap between SoehneBreit display and Inter body. Used at 20px for secondary headings that need editorial weight without display scale.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 80px.
- Card padding: 20-32px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Promotional Banner: Top-of-page announcement strip
- Navigation Bar: Primary site navigation
- Filled Button (Primary): Interactive action trigger
- Ghost Button: Secondary interactive trigger
- Pill Button: Rounded utility button
- Hero Section: Full-bleed landing visual
- Content Card: Grouped content surface
- Input Field: Text input control
- Inline Link: Text-level navigation
- Footer: Site-bottom content

Do:

- Use #528fff Signal Blue for all links and interactive text - it is the system's only persistent color voice
- Apply -0.015em letter-spacing to all text at all sizes for the compact reading rhythm
- Use SoehneBreit weight 400 for headlines - never bold, the whisper-weight is the voice
- Separate surfaces with 1px borders in #45464d or #232426, never with drop shadows
- Use 8px radius for standard buttons and 60px for pill-shaped interactive elements
- Apply 0.071em tracking to uppercase SoehneBreit labels at 14px for the editorial eyebrow pattern
- Let photography provide all visual elevation - full-bleed images carry the weight that shadows would

Avoid:

- Never use #f1f607 Voltage Yellow on backgrounds - it is text-only punctuation
- Don't add drop shadows to cards or panels - the system is intentionally flat
- Never set SoehneBreit to bold weight - it only exists at 400 in this system
- Don't introduce new accent colors - the palette is grayscale plus two signals (blue, yellow-green)
- Avoid pure white backgrounds - the canvas is always Carbon #121214 or Graphite #232426
- Don't center-align body text - left-align for editorial reading rhythm
- Never use more than one chromatic color per component - the system rations color

Source prompt cues:

primary action: no distinct CTA color
**Quick Color Reference**
- text: #ffffff
- background: #121214
- border: #45464d
- accent: #528fff
- button fill: #1253ff
- highlight: #f1f607

**Example Component Prompts**

1. Create a full-bleed hero section: a large dark-toned photograph filling the entire viewport with no border-radius. Overlaid in the lower-left, a headline at 54px SoehneBreit weight 400, #ffffff, letter-spacing -0.81px. Below it, a filled blue button (#1253ff background, #ffffff text, 8px radius, 16px 20px padding, Inter weight 500 at 14px).

2. Create a content card: #121214 background, 4px border-radius, 1px #45464d border, 24px padding. Headline at 28px SoehneBreit weight 400 in #ffffff, body text at 16px Inter weight 400 in Fog #a6a8ad. No drop shadow.

3. Create a ghost button: transparent background, 1px #c8c9cc border, #ffffff text, 8px radius, 8px 20px padding, Inter weight 400 at 14px. Include a small play icon ( ) in white to the left of the text.

4. Create a navigation bar: #000000 background, 60px height, sticky to top. Logo (wordmark in #ffffff, Inter weight 700 at 16px) on the left, nav links (#a6a8ad, Inter weight 400 at 14px, 20px horizontal gap) in the center, and a filled blue button (#1253ff, 8px radius, Inter 14px weight 500) on the right.

5. Create an input field: #121214 background, 1px #45464d border, 4px border-radius, 12px 16px padding. Placeholder text 'Search samples...' in #a6a8ad, Inter weight 400 at 14px. On focus, border shifts to #528fff.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
