# AI Implementation Prompt

Build a Altius-inspired interface using this source-derived style bundle.

Reference site: https://www.altiuslabs.xyz
Theme: dark
Category: Crypto
North star: Molten embers on obsidian. A blockchain command center lit from within by coral fire, where dark surfaces breathe warm light through hairline gaps and inset glows.

Use these palette anchors:

- Obsidian Ember `#190501` for Primary dark canvas - page background in dark sections, card surface, deepest borders. The black-with-warmth that defines the brand atmosphere
- Dark Cocoa `#340a01` for Secondary dark surface, deep link borders, icon outlines - one step lifted from obsidian for layering depth
- Molten Core `#631303` for Inset glow shadow source, deep red-brown accents - the pressed-ember tone that gives buttons their internal fire
- Signal Red `#951c04` for Outlined/ghost action border, nav borders, icon strokes, interactive outlines - the chromatic action color used for outlined buttons and active control edges
- Flare Orange `#fa5838` for Primary brand accent - links, decorative borders, the hero gradient spectrum, highlight washes. The single hottest color in the system; used sparingly as functional punctuation
- Warm Blush `#fcac9c` for Soft surface wash, secondary peach background, decorative highlight fields - the diffused ember tone for breathing sections
- Vapor Peach `#feeae6` for Light section background, light-mode card surface, body text on dark, ghost button text - the warm off-white that breaks the dark rhythm
- Linen `#f7f6ff` for Primary text on dark, crisp borders on dark sections, inverse text. The near-white that carries most typography on dark surfaces
- Warm Ash `#baadab` for Muted button borders on light sections, tertiary text, subtle dividers - a warm gray that softens edges without going cold
- Pure Black `#000000` for Decorative SVG fills, icon line art, graphical accents - high-contrast details that read as deep-ink on the warm canvas
- Mist `#cccccc` for Input field borders on light backgrounds - the only cool-neutral in the system, used minimally for form controls

Use these typography anchors:

- Matter `--font-matter` for Primary typeface - body, display, headings, buttons, navigation, icons. Weight 700 carries display headlines; 500 for emphasis in body; 400 for regular text. Tight tracking across all sizes creates a compressed, confident read.
- Fabrikatmono `--font-fabrikatmono` for Monospace accent - section labels, tags, technical metadata, trust signals. Used in uppercase for eyebrow labels like 'THE PROBLEM' and 'SOLUTIONS'. The technical-utility voice that contrasts Matter's editorial confidence.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 32px.
- Element gap: 10px.

Build these component patterns where relevant:

- Top Navigation Bar: Site-wide header
- Hero Section: Landing page hero
- Filled Primary Button: Primary action
- Outlined Ghost Button: Secondary action
- Investor Logo Grid: Social proof band
- Section Header (Tag + Heading): Section introduction
- Problem Statement Card: Light-section content card
- Solutions Feature Card: Feature highlight (dark variant)
- Input Field: Form control
- Footer: Site footer
- Hero Gradient Bar: Decorative hero element
- Eyebrow Tag Label: Section category indicator

Do:

- Use Obsidian Ember (#190501) as the default canvas for all primary content sections
- Apply 60px Matter weight 700 with -2.58px letter-spacing for display headlines
- Use the Flare Orange (#fa5838) sparingly as functional punctuation - links, accents, single highlight elements per section
- Include the 20px inset ember-glow shadow (rgb(99,19,3)) on all filled primary buttons
- Alternate between dark and Vapor Peach (#feeae6) sections to create thermal rhythm across the page
- Set all buttons to 4px radius and cards to 8px radius - sharp enough to feel technical, soft enough to feel crafted
- Use Fabrikatmono 14px uppercase in Flare Orange for all section tags and technical labels

Avoid:

- Don't add drop shadows to cards or panels - the system uses hairline borders and surface differentiation only
- Don't use blue or cool tones - the entire palette is warm, from Vapor Peach through Molten Core
- Don't create filled buttons with Flare Orange (#fa5838) background - Flare Orange is for accents, not button fills
- Don't use display sizes below 48px or above 60px - the type scale is compressed and confident
- Don't let dark sections run more than 2-3 before introducing a Vapor Peach break - the thermal alternation is structural
- Don't use generic sans-serif fallbacks as the primary face - Matter's tight tracking is part of the voice
- Don't apply color to body text - keep body text in Linen (#f7f6ff) on dark or Obsidian Ember (#190501) on light

Source prompt cues:

primary action: #951c04 (outlined action border)
Create an Outlined Primary Action: Transparent background, #951c04 border and text, 9999px radius, compact pill padding. Use it for the main CTA instead of a filled button.
Quick Color Reference:
- text: #f7f6ff (on dark) / #190501 (on light)
- background: #190501 (dark sections) / #feeae6 (light sections)
- border: #190501 (hairline on dark) / #baadab (on light)
- accent: #fa5838 (links, highlights, single-color punctuation)
- outlined action: #951c04 (ghost/outlined button border)

Example Component Prompts:

1. Create a hero section: Obsidian Ember (#190501) full-width background. Centered 60px Matter weight 700 headline in Linen (#f7f6ff), letter-spacing -2.58px. 16px subtext in Linen at 70% opacity. Two CTAs: filled button with Dark Cocoa (#340a01) background, Linen text, 4px radius, 8px 20px padding, inset shadow rgb(99,19,3) 0px 0px 20px; outlined button with 1px Linen border, transparent fill, Linen text, same radius and padding. Below text, 12 vertical Flare Orange (#fa5838) bars (40-80px wide, 240px tall) with center-to-edge opacity fade.

2. Create a solutions feature card: Dark Cocoa (#340a01) background, 8px radius, 32px padding, 1px border in Signal Red (#951c04). Top-left: '01' in Fabrikatmono 14px Flare Orange (#fa5838). Top-right: small line-art icon in Flare Orange. Center: 24px Matter weight 700 heading in Linen (#f7f6ff), letter-spacing -0.8px. Body: 16px Matter weight 400 Linen at 80% opacity.

3. Create a section header: Fabrikatmono 14px uppercase tag in Flare Orange (#fa5838) with letter-spacing -0.05em, preceded by a 12x12px outlined square icon. 16px gap. Followed by 48px Matter weight 700 headline in Linen (#f7f6ff), letter-spacing -1.92px.

4. Create a light problem-statement card: Linen (#f7f6ff) background on Vapor Peach (#feeae6) section. 40px padding, 8px radius, 1px Warm Ash (#baadab) border. Contains a coral wireframe illustration on the left half and 16px body text in Obsidian Ember (#190501) on the right half.

5. Create a footer: Obsidian Ember (#190501) background, 64px vertical padding. Two 32x32px outlined social icons (X, LinkedIn) with 1px Flare Orange (#fa5838) border, 4px radius, Flare Orange line-art icons centered inside.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
