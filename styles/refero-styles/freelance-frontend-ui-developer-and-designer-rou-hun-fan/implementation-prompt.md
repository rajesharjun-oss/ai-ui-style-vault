# AI Implementation Prompt

Build a Freelance frontend UI developer and designer, Rou Hun Fan-inspired interface using this source-derived style bundle.

Reference site: https://flowen.me
Theme: dark
Category: Agency
North star: Riso-printed zine on black construction paper

Use these palette anchors:

- Carbon `#0a0a0a` for Page canvas and section backgrounds - near-true-black maximizes the contrast pop of white type and saturated accent blocks
- Bone `#ffffff` for Primary text, display headlines, borders, and link strokes - the only voice for the majority of the page
- Voltage Cyan `#1ef0e4` for Accent card backgrounds, highlight panels - flat saturated cyan that screams against the dark canvas, reserved for project cards and editorial callout blocks
- Plasma Magenta `#e91e8c` for Display text on cyan cards, decorative script flourishes - hot pink/magenta used only as ink-on-cyan contrast or as editorial accent
- Ember `#ff3a1a` for Supporting palette color for small decorative accents when the core palette needs contrast.

Use these typography anchors:

- Azeret Mono `--font-azeret-mono` for Monospace system voice - navigation, metadata, UI labels, footer text. Brings a developer-terminal identity that matches the frontend-developer positioning
- AzeretMono (display variant) `--font-azeretmono-display-variant` for Oversized condensed display headlines (ROU HUN FAN, UI DEV, DESIGN, MOTION & FRONTEND). The extreme scale and bold weight turn the page into a typographic poster - type IS the design
- Ephidona `--font-ephidona` for Calligraphic editorial script for section labels (PROJECTS). Counter-typography that breaks the geometric/mono discipline with human handwriting - the anti-machine flourish that signals personal craft over automated output

Use these layout rules:

- Base spacing: 8px.
- Density: compact.
- Page max-width: 1400px.
- Section gap: 80-120px.
- Card padding: 32-48px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Display Headline: Primary typographic element - sets the poster/magazine tone
- Editorial Script Label: Section divider and humanizing accent
- Voltage Project Card: Featured project showcase block
- Monospace Navigation: Top-of-page nav and section links
- Photo Plate: Personal photography and project imagery
- Metadata Tag: Small labels for project categories, years, skills
- Footer: Contact and social links
- Decorative Organic Shape: Graphic accent on Voltage cards

Do:

- Use AzeretMono 700/900 at 72-100px for all primary headlines - type scale should feel oversized, never comfortable
- Apply Voltage Cyan (#1ef0e4) as flat panel backgrounds only - never as gradients, never as semi-transparent overlays
- Keep all border-radius at 0px - cards, buttons, images, tags are all hard rectangles
- Use Ephidona script sparingly (1-2 instances per page) as editorial flourishes on Voltage cards, not for functional text
- Set elementGap to 8-16px and use whitespace as structural division between content blocks
- Let display text break across columns naturally - asymmetric, magazine-grid layout is intentional
- Pair Plasma Magenta text exclusively with Voltage Cyan backgrounds - never use magenta on dark or magenta as body text

Avoid:

- Don't add box-shadows, drop-shadows, or any form of depth simulation - the design is ruthlessly flat
- Don't round corners on any element - hard edges define the brutalist editorial language
- Don't use the brand accent colors for buttons or CTAs - there are no traditional CTAs; navigation is text-only
- Don't introduce a third display weight between 56px and 100px - the scale jumps from readable to poster-sized, no comfortable middle ground
- Don't apply gradients to any surface - the palette is 100% flat fills
- Don't use the Ephidona script for body copy, navigation, or functional labels - it is decorative only
- Don't soften the white text with opacity below 80% for body content - if hierarchy is needed, drop the size and weight instead

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
