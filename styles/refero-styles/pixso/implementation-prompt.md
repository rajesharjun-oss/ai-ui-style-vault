# AI Implementation Prompt

Build a Pixso-inspired interface using this source-derived style bundle.

Reference site: https://pixso.net
Theme: light
Category: Design
North star: pristine designer's canvas flooded with morning light

Use these palette anchors:

- Obsidian `#000000` for Primary text, heading type, dark icons, and the strongest foreground layer
- Carbon `#121212` for Filled primary buttons, active nav state, dark surface fill
- Graphite `#333333` for Secondary headings, button labels on light surfaces, heavy icon strokes
- Slate `#666666` for Body secondary text, helper copy, muted metadata
- Ash `#808080` for Tertiary text, disabled states, placeholder copy, subtle borders
- Fog `#999999` for Inactive icons, low-emphasis dividers, shadow tinting
- Pebble `#8b8c8f` for Icon strokes on neutral surfaces, muted glyph color
- Smoke `#4d4d4d` for Heavy body text where Obsidian feels too sharp, small caption emphasis
- Charcoal Veil `#3d3d3d` for Navigation bar text and borders - the dark nav strip registers as a separate layer
- Dusk `#292929` for Deep surface fill for elevated dark blocks and image overlays
- Paper `#faf8fd` for Page canvas - barely-there warm/lavender tint that separates the site from pure white
- Bone `#f9f9fa` for Card surfaces, secondary panels, subtle raised containers
- Mist `#eaebee` for Hairline borders, divider rules, button outlines, input borders
- Ice Wash `#cfe7ed` for Pale cool-blue background tint for highlighted cards and feature panels
- Iris Sweep `#ee7cff` for Brand logo gradient midpoint - the wordmark's signature purple-to-blue sweep
- Orchid Edge `#ee7cff` for Brand logo gradient start - warm violet anchor of the wordmark sweep
- Sky Drift `#559cff` for Brand logo gradient end - cool blue terminus of the wordmark sweep

Use these typography anchors:

- Figtree `--font-figtree` for Single-family system: 700 carries the hero and section headlines at 48-60px with tight tracking, 600 handles subheadings and prominent labels at 24-34px, 500 covers button labels and emphasized body at 16-18px, 400 runs body and caption copy at 13-16px. The geometric, low-contrast character of Figtree keeps the all-black type from feeling oppressive.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Filled Primary Button: Main conversion action - the loudest UI element on the page
- Outlined Secondary Button: Companion action - same row, lower weight
- Ghost Nav Link: Top navigation items and in-content links
- Design Kit Card: Gallery tile in the design kit grid (4-column layout)
- Product Showcase Frame: Large framed mockup in the product section
- Floating Feature Card: Callout card floating over hero or product imagery
- Top Navigation Bar: Persistent site header
- Section Divider: Vertical separation between content sections
- Decorative Icon Scatter: Atmospheric floating icons in the hero margins

Do:

- Use Figtree for everything - no secondary font family, no system fallbacks in production output
- Let the page background be #faf8fd, never pure #ffffff, so cards visibly lift
- Pair a Filled Primary Button (Carbon #121212) with an Outlined Secondary Button (Mist border) in the same action row
- Reserve 8px radius for cards and nav, 12px for buttons, 18px only for prominent product frames
- Keep shadows to the signature two-layer stack: 1px hairline dark + 2-4px soft blur
- Use the Iris Sweep gradient only on the wordmark and brand-identity surfaces - never on buttons or functional UI
- Let product mockups and design kit thumbnails carry all the color; keep chrome grayscale

Avoid:

- Don't introduce a chromatic CTA color - the primary action is always Carbon #121212
- Don't use heavy drop shadows or colored shadows; elevation must stay hairline
- Don't set body type below 13px or use Figtree below weight 400
- Don't add gradient backgrounds to UI surfaces; gradients belong to the logo and decorative imagery
- Don't center-align body paragraphs - the system uses left-aligned running text below the hero
- Don't use #0000ee or browser-default link blue for any interactive element
- Don't round buttons to pill (9999px); the system uses 8/12/18px radii only

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
