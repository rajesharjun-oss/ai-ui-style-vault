# AI Implementation Prompt

Build a Aptos Network-inspired interface using this source-derived style bundle.

Reference site: https://aptosnetwork.com
Theme: light
Category: Crypto
North star: Earth-toned code atelier - a sage-walled observatory where terracotta, sand, and powder-blue panels hold monospaced code beside serif prose, framed by 1px ink hairlines.

Use these palette anchors:

- Ink `#0f0e0b` for Primary text, hairline borders, icon strokes, nav outlines - the near-black that carries 90% of all foreground weight. Not pure black: a warm brown-black that feels printed, not screened
- Bone `#f9f9f0` for Page canvas, card surfaces, nav-pill fill, button text on dark - a warm off-white with the faintest yellow-green cast that matches the sage and sand sections without competing
- Ash `#6d6c67` for Secondary text, subtle borders, muted metadata - a mid neutral that sits between Ink and the page; used when primary text would be too heavy
- Charcoal `#21201c` for Filled CTA buttons, active markers - slightly warmer than Ink; the button fill that reads as a dense matte stamp rather than a flat black
- Graphite `#555450` for Tertiary text, low-emphasis borders - for labels and helper text that should recede further than Ash
- Mist `#84837d` for Heading borders, de-emphasized dividers - the lightest neutral that still registers as a line on Bone
- Deep Earth `#3d3b34` for Alternate surface for code-adjacent panels and inset blocks - a warm dark that bridges Ink and the mid neutrals
- Soft Sand `#ccc5a3` for Secondary section background, 1px sand-colored hairline dividers, striped-pattern accent - the warm neutral that lives between the chromatic sections and true gray
- Warm Stone `#9d937c` for Khaki section background, tonal counterpoint to Sage - the muted olive-khaki that fills body-text sections and grounds the palette's middle register
- Sage `#d5fad3` for Hero section background, signature accent - a desaturated mint that signals freshness without being loud; the only color bold enough to hold a 120px headline
- Powder Blue `#badbee` for Code-panel background, striped-pattern accent, 1px blue hairlines - the cool counterweight to all the warm earth tones; appears wherever monospace code or technical data lives

Use these typography anchors:

- Season Serif `--font-season-serif` for Sole typeface - display, headings, body, nav, buttons, footer, code labels. Custom variable serif with fractional weights (no standard 300/400/700 scale) that allow whisper-light display at 335-340 and confident body at 420-444.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 90-150px.
- Card padding: 30px.
- Element gap: 15-30px.

Build these component patterns where relevant:

- Floating Nav Pill: Primary site navigation container
- Filled Pill CTA: Primary action button
- Ghost Text Link: Secondary inline action or nav item
- Full-Bleed Color Section: Page section with solid muted-color background
- Section Hairline Divider: Horizontal divider between sections or within sections
- Display Headline: Hero and section-opening title
- Body Copy Block: Editorial prose section content
- Code Panel: Monospace code display
- Striped Geometric Panel: Decorative right-side pattern
- Nav Dropdown Item: Submenu item within nav pill
- Section Opening Label: Small caption above headlines or between sections

Do:

- Use Season Serif for all text - there is no secondary typeface. Weight 335-340 for display 55px+, weight 400-420 for body and UI, weight 420-444 for emphasis.
- Apply -0.030em letter-spacing to any type 90px or larger. Positive tracking (+0.01em) only at 9px caption size. Body text uses normal tracking.
- Use full-bleed color section backgrounds (Sage, Warm Stone, Soft Sand, Powder Blue) at 90-150px vertical padding. Never constrain sections to a max-width background.
- Draw all dividers as `inset 0 0 0 1px {color}` box-shadows, not as border properties. Rotate colors: Ink, Soft Sand, Powder Blue.
- Use 9999px radius for all buttons, nav container, and tags. Use 0px radius for all other surfaces (cards, code panels, inputs).
- Enable `font-feature-settings: "calt"` on all Season Serif text - contextual alternates are part of the brand voice.
- Split every section into left text / right decoration at roughly 55/45. Text left-aligns; decorative striped panel occupies the right.

Avoid:

- Do not use any sans-serif typeface. Season Serif carries everything, including buttons, nav, and code labels.
- Do not use drop shadows. The system is flat by design - all line work is 1px inset.
- Do not use border-radius on cards, panels, code blocks, or images. Only buttons and the nav pill are rounded (9999px).
- Do not use bright or saturated colors. Every chromatic value is muted: sage, khaki, sand, powder blue. Saturation above 40% breaks the system.
- Do not use smooth gradients. The decorative right-side panels are hard-edge striped patterns implemented with sharp linear-gradient color stops.
- Do not use standard font weights (300, 400, 700). Season Serif uses fractional weights (335, 340, 420, 444) - pick from the available scale.
- Do not place text on both halves of a split section. The right side is always decorative (striped pattern or code panel), never text.

Source prompt cues:

**Quick Color Reference**
- Text (primary): #0f0e0b
- Background (canvas): #f9f9f0
- Border (hairline): #0f0e0b
- Accent (hero/section): #d5fad3
- Accent (code panel): #badbee
- primary action: #21201c (filled action)

**3-5 Example Component Prompts**

1. *Create a hero section:* Sage (#d5fad3) full-bleed background, 150px vertical padding. Headline in Season Serif weight 335, 120px, #0f0e0b, letter-spacing -3.6px, line-height 1.0, left-aligned. A 10pxx20px Charcoal (#21201c) filled pill button with Bone (#f9f9f0) text, weight 420, 16px, 9999px radius, positioned below the headline. Right side: a curved striped panel with alternating 44px bands of #0f0e0b and #badbee.

2. *Create a body-copy section:* Warm Stone (#9d937c) full-bleed background, 90px vertical padding. Top headline: Season Serif weight 340, 90px, #0f0e0b, letter-spacing -2.7px. Below a 1px Ink hairline divider (`box-shadow: inset 0 0 0 1px #0f0e0b`), a narrow ~400px right-aligned text column in Season Serif weight 400, 18px, #0f0e0b, line-height 1.4, 30px row-gap between paragraphs.

3. *Create a code-display section:* Soft Sand (#ccc5a3) left half, Powder Blue (#badbee) right half. Left: headline Season Serif weight 340, 55px, #0f0e0b, letter-spacing -1.1px. Right: monospace code in Season Serif weight 420, 14px, #0f0e0b on #badbee, 1px Ink inset border on the panel edges.

4. Create a Primary Action Button: #21201c background, #f9f9f0 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

5. *Create a section divider:* Full-width 1px line using `box-shadow: inset 0 -1px 0 0 #ccc5a3`. No actual border, no margin, no padding. Sits between two full-bleed color sections.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
