# AI Implementation Prompt

Build a Applied Labs-inspired interface using this source-derived style bundle.

Reference site: https://appliedlabs.ai
Theme: light
Category: AI
North star: Sunlit cream paper with cobalt punctuation and floating conversation cards

Use these palette anchors:

- White `#ffffff` for Page canvas, base card surface, nav background
- Cream `#f7f7f4` for Warm off-white section background, soft card fill - the secondary surface layer that gives the page its paper-like warmth
- Fog `#f5f5f5` for Elevated card surfaces and subtle section bands
- Ash `#e4e4e7` for Hairline borders, dividers, input underlines - the structural skeleton of the layout
- Stone `#8c8c8c` for Tertiary text, placeholder copy, disabled states
- Steel `#737373` for Secondary body text, helper copy, muted descriptions
- Graphite `#666666` for Secondary body text on cream surfaces
- Charcoal `#4d4d4d` for Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color
- Warm Gray `#7d7c78` for SVG icon fills, subtle warm-toned decorative elements
- Espresso `#26251e` for Primary text on cream surfaces, dark card accents, outlined action borders - the warm alternative to pure black
- Midnight `#09090b` for Primary body and heading text on white, the dominant ink color
- Pure Black `#000000` for Primary headings, body text, and icon fills on light surfaces. Do not promote it to the primary CTA color
- Deep Ink `#111111` for Footer and nav text, dark surface accents
- Slate Blue `#5c7aa1` for Muted blue-gray for section backgrounds, subdued text accents, and image overlay washes - adds cool depth without competing with the cobalt accent
- Warm Sand `#b39987` for Warm tan card surfaces, trust/social-proof section backgrounds - a near-gray with just enough warmth to echo the photography
- Cobalt Spark `#0051ff` for Violet text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Emerald `#00cb39` for Green text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color

Use these typography anchors:

- Geist `--font-geist` for Sole typeface - used for everything from display headlines down to 10px micro-copy. Geist's geometric neutrality and tall x-height make it read as editorial without being cold.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80-120px.
- Card padding: 12-16px.
- Element gap: 12px.

Build these component patterns where relevant:

- Sticky Navigation Bar: Top-level site navigation, persistent across scroll
- Primary CTA Button (Dark Filled): Main action - Get Demo, Book demo, Submit
- Pill CTA Button: Compact action in nav or tight spaces
- Ghost Text Link: Secondary navigation, inline links
- Cobalt Inline Link: Highlighted link within body text - the system's only colored link
- Hero Section with Photo + Chat Overlay: Above-the-fold brand impression
- Chat Message Bubble (User): Visualization of customer message in product context
- Chat Message Bubble (Agent): Visualization of AI agent reply in product context
- Trust Logo Strip: Social proof - brands that use the product
- Section Heading Block: Section introduction - text-only or text + subhead
- Feature Card: Product capability or benefit block
- Form Section: Lead capture with visual context

Do:

- Use #f7f7f4 cream for section backgrounds that need warmth; reserve #ffffff for the page canvas and elevated cards
- Apply 8px border-radius consistently to cards, buttons, and inputs - this is the system's signature softness, not pill-rounded, not sharp
- Set headline letter-spacing to -0.02em at 48px and -0.012em at 24px; use positive tracking (0.005-0.010em) only on 12-14px body and micro-copy
- Use Cobalt Spark (#0051ff) for at most one inline link or accent per section - it marks the singular important action, not decoration
- Fill primary action buttons with #000000 or #26251e; let white text carry the contrast
- Use #e4e4e7 for all structural borders, dividers, and input underlines at 1px
- Layer chat-message visuals over warm photography to communicate the product's conversational nature without explaining it

Avoid:

- Do not fill buttons with Cobalt Spark (#0051ff) - that color is reserved for inline text accents and links, never for filled button backgrounds
- Do not use shadows on cards unless they represent a floating overlay or modal; the system relies on borders and surface color shifts, not elevation
- Do not use illustrations, 3D renders, or icon-heavy compositions as primary visuals - real warm-toned photography carries the brand
- Do not use a second typeface; Geist handles everything from 10px caption to 48px display
- Do not use the warm tan (#b39987) or slate blue (#5c7aa1) for more than 10-15% of the visible surface - they are accent surfaces, not the canvas
- Do not set headline weight above 500; weight 300 is the signature, weight 500 is for emphasis, never 600-700
- Do not use border-radius above 24px on standard cards; the 8px default is the system's defining softness

Source prompt cues:

**Quick Color Reference**
- text: #09090b (primary), #737373 (secondary), #8c8c8c (tertiary)
- background: #ffffff (canvas), #f7f7f4 (cream sections), #f5f5f5 (card surfaces)
- border: #e4e4e7 (hairline, 1px)
- accent: #0051ff (Cobalt Spark - links and inline emphasis only)
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. **Hero Section**: White (#ffffff) background, max-width 1200px. Headline 'Every customer, better served' at 48px Geist weight 300, color #09090b, letter-spacing -0.96px, line-height 1.08. Subhead at 16px Geist 400, #737373. Dark filled button: #000000 background, white text, 8px radius, 14px 24px padding, Geist 500 14px. Right side: full-bleed warm-toned photograph with 3-4 translucent chat message bubbles overlaid, each with 12px radius and rgba(255,255,255,0.85) fill.

2. **Feature Card**: 8px border-radius, 1px #e4e4e7 border, 16px padding, #ffffff background. 24px icon in #09090b. Heading 'Capability name' at 16px Geist 500 #09090b. Body at 14px Geist 400 #737373, 12px margin-top. No shadow.

3. **Form Input (Underline)**: No background, no top or side borders, 1px #e4e4e7 bottom border only, 12px vertical padding. Label at 12px Geist 500 #737373 above the field. Input text at 14px Geist 400 #09090b. Placeholder #8c8c8c. On focus, bottom border becomes #09090b.

4. **Trust Logo Strip**: Full-width band, background #b39987 (Warm Sand) or #f7f7f4 (Cream). Centered caption 'Trusted by millions of customers' at 13px Geist 400 #737373, 24px bottom margin. Row of 6-8 monochrome logos (each in #09090b or #4d4d4d), spaced 48px apart, optically aligned to the same height.

5. **Section Heading Block**: 120px top padding, max-width 720px. Headline at 36px Geist 300 #09090b, letter-spacing -0.72px, line-height 1.17. Optional subhead at 18px Geist 400 #737373, 16px top margin.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
