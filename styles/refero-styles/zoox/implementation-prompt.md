# AI Implementation Prompt

Build a Zoox-inspired interface using this source-derived style bundle.

Reference site: https://zoox.com
Theme: light
Category: Other
North star: serene sage showroom. A pale mint gallery space where one vivid teal accent and one dark forest panel interrupt the quiet - spacious, premium, and forward-looking.

Use these palette anchors:

- Sage Canvas `#d3e4df` for Page background, hero bands, section dividers - the dominant ambient color that gives the system its calming gallery atmosphere
- Pure White `#ffffff` for Card surfaces, image masks, icon fills, high-contrast text on dark sections
- Mint Frost `#edf4f2` for Badge backgrounds, subtle highlight washes, secondary card surfaces - a quieter sibling of the sage canvas
- Carbon `#0d1212` for Primary text, dark section backgrounds, heavy borders - the deepest near-black, slightly cooler than true black
- Graphite `#34484a` for Navigation borders, secondary headings, muted icon strokes - a dark desaturated teal that bridges neutrals and the accent; Dark borders and separators for elevated surfaces and inverted UI.
- Slate `#565959` for Body text secondary level, list dividers, footers, muted borders
- Fog `#9aa3a5` for Tertiary text, placeholder labels, disabled icon strokes
- Mist `#7b8889` for Eyebrow text and label color, small caps headers
- Vivid Teal `#64d5b3` for Primary action button fills, accent surfaces, interactive highlights - the single chromatic color in the system, used sparingly to signal action
- Eucalyptus `#5b8279` for Gray outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color

Use these typography anchors:

- GT Standard S `--font-gt-standard-s` for Primary UI and body typeface - used for navigation, buttons, body copy, badges, inputs, and headings up to 50px. The 'kern' 0 feature setting deliberately disables kerning for a monospaced-mechanical feel. The 0.0500em tracking on 12-13px text gives small labels a spacious, typeset quality.
- GT Standard L `--font-gt-standard-l` for Display-only typeface reserved for hero headlines and large section titles. Used at a single weight (400) to keep the voice calm and confident - no bold shouting. The 120px size with normal letter-spacing creates wide, architectural headlines that sit centered on the sage canvas.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 12px.

Build these component patterns where relevant:

- Sage Hero Section: Full-bleed hero band on the sage canvas
- Filled Teal CTA Button: Primary action - only filled chromatic button in the system
- Ghost Navigation Button: In-text or link-style action
- Dark Pill CTA: Secondary action button in the header
- Image Card (Rounded): Photo or illustration container
- Eyebrow Label: Small caps section pre-title
- Mint Badge: Status or category tag
- Cookie Consent Dialog: Fixed-bottom privacy notice
- Navigation Bar: Top-level site navigation
- Dark Forest Feature Section: Dramatic contrast section
- Play/Pause Toggle Button: Media control
- Text Input Field: Form input

Do:

- Use #d3e4df (Sage Canvas) as the dominant page background across all full-bleed sections
- Reserve #64d5b3 (Vivid Teal) exclusively for filled CTA buttons and single accent surfaces - never as text color or decorative fill
- Set display headlines at 56px or 120px in GT Standard L weight 400 only - never bold, never at intermediate sizes
- Apply 36px border-radius to all image cards and feature containers
- Use 1px #565959 or #34484a hairline borders for separators and card edges, never thick rules
- Set font-feature-settings to "kern" 0 on all GT Standard text to maintain the mechanical spacing identity
- Space sections with 80-120px vertical padding to preserve the gallery-like breathing room

Avoid:

- Do not introduce additional chromatic colors - the system is sage, white, carbon, and one teal accent
- Do not use bold weights for display headlines - GT Standard L is always weight 400
- Do not apply box-shadow to cards, buttons, or navigation - the system relies on radius and borders
- Do not use #34484a (Deep Forest) as a text color or border on light backgrounds - it is reserved for the dark section background
- Do not set body text below 13px or use letter-spacing tighter than -0.002em on UI text
- Do not use the Vivid Teal on text - it is a surface color only, paired with #0d1212 or #ffffff text
- Do not break the section rhythm with narrow max-width containers - let the sage canvas flow full-bleed

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
