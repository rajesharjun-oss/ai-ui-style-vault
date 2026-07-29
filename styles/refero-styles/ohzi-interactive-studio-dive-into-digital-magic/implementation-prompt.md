# AI Implementation Prompt

Build a OHZI Interactive Studio / Dive into digital magic.-inspired interface using this source-derived style bundle.

Reference site: https://ohzi.io
Theme: dark
Category: Agency
North star: A glowing cube suspended in a dark gallery

Use these palette anchors:

- Pure White `#ffffff` for Primary text, icon strokes, hairline borders, outlined button frame - the only foreground color on the dark canvas, used at full opacity for headlines and at 1px hairline weight for UI structure
- Void Black `#000000` for Deep background fill, SVG icon bases - the absolute floor of the visual hierarchy, used for full-bleed canvas and asset fills
- Carbon `#111111` for Heading text on light sections, deep surface layer - near-black with a whisper of warmth, used where #000000 would feel too flat
- Fog `#f5f5f7` for Secondary text, subtle panel surfaces, light-section borders - cool-tinted off-white that softens transitions on inverted sections
- Ash `#cfcfcf` for Muted helper text, disabled states, tertiary borders - the mid-gray for elements that should recede

Use these typography anchors:

- Unbounded `--font-unbounded` for Sole typeface for everything - headlines, body, buttons, nav. Its geometric, slightly squared character with wide-aperture letterforms reads as digital-native and architectural. Weight 100 for display text creates a near-wireframe quality that feels holographic against the dark background.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 80-120px.
- Card padding: 24-40px.
- Element gap: 20px.

Build these component patterns where relevant:

- Ghost CTA Button: Primary action trigger
- Brand Lockup: Top-left identity mark
- Hamburger Menu Trigger: Navigation toggle
- Hero Headline: Page title
- Hero Subtext: Supporting description
- 3D Hero Object: Central visual anchor
- Cookie Consent Banner: Compliance overlay

Do:

- Use Unbounded exclusively - never substitute a secondary typeface, the single-family discipline is the identity
- Apply positive letter-spacing to all text; never collapse tracking below 0.067em even at display sizes
- Keep all UI elements at 0px border-radius - sharp corners are non-negotiable and echo the 3D geometry
- Let the 3D scene be the sole source of color and light; UI stays pure grayscale (#ffffff, #f5f5f7, #cfcfcf, #111111, #000000)
- Use 1px hairline borders for all structural elements - buttons, dividers, card frames
- Center-align hero content and maintain generous vertical breathing room (80-120px between sections)
- Pair weight 600-700 for headlines with weight 100-400 for body to create a weight-contrast hierarchy that replaces color contrast

Avoid:

- Never introduce accent colors, gradients, or chromatic buttons - the system is deliberately achromatic
- Never use border-radius on buttons, cards, inputs, or images - the sharp geometry is load-bearing
- Never apply shadows, glows, or blur effects to UI elements - depth belongs to the 3D scene only
- Never use negative letter-spacing or tight tracking - the wide-open spacing is the typographic signature
- Never fill buttons with solid color - always use the transparent ghost-button treatment with a 1px stroke frame
- Never use more than one typeface or mix serif/sans - Unbounded is the sole voice
- Never crowd the central viewport with UI - the 3D object needs negative space to breathe

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
