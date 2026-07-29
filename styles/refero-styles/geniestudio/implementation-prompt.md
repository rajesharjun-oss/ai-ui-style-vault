# AI Implementation Prompt

Build a Geniestudio-inspired interface using this source-derived style bundle.

Reference site: https://geniestudio.app
Theme: light
Category: AI
North star: soft daylight notebook - the kind with generous margins and a single bold pen stroke

Use these palette anchors:

- Sky Tint `#ebf5ff` for Page canvas and soft background washes - the defining ambient color that sets the daylight atmosphere
- Paper White `#ffffff` for Pure card surfaces, button text, and icon fills on dark controls
- Bone White `#fafdff` for Primary card surface and elevated panel backgrounds - a barely-blue white that feels paper-like
- Mist Gray `#f6f7f8` for Subtle secondary surfaces and section dividers
- Ink `#0a0d12` for All heading text, primary display type, and deep emphasis copy
- Charcoal `#181d27` for Filled button backgrounds and the dense visual anchor against the airy canvas
- Graphite `#535862` for Secondary body text and supporting copy
- Fog `#93979f` for Muted helper text, FAQ answers, and low-emphasis body
- Slate Shadow `#3b3d41` for Dark shadow tone behind buttons and elevated controls
- Sky Blue `#0099ff` for Inline highlight text and emphasis spans within body copy
- Lavender Wash `#f1e6ff` for Pastel card surface for feature tiles and category blocks
- Mint Wash `#d3f6e3` for Pastel card surface for feature tiles and category blocks
- Powder Blue `#cce7ff` for Gray wash for highlight backgrounds, decorative bands, and soft emphasis behind content

Use these typography anchors:

- Aeonik `--font-aeonik` for Display and heading face for all editorial moments - 148px hero headlines, 72px section openers, 48px card titles, 32px subheadings. Fixed at weight 500; the brand never goes bolder. Tracking pulls tight at -0.02em which gives the geometric forms a sculpted, almost engraved quality at large sizes. Substitute: 'Sohne', 'Inter', or 'General Sans'.
- Geist `--font-geist` for UI and body face for everything below the headline tier - body copy, buttons, labels, captions, card descriptions, nav links. Weight 500 is the workhorse; 600 only for tiny 10px micro-labels. The 18px / 20px sizes with -0.01em tracking carry the interface's conversational voice. Substitute: 'Geist', 'Inter', or 'Sohne'.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 40px.
- Element gap: 24px.

Build these component patterns where relevant:

- Primary CTA Button: Filled dark pill - the only dense visual element on the page
- Secondary CTA Button: Smaller filled pill for inline actions
- Ghost Nav Link: Header navigation text
- Feature Card (32px radius): Primary content card - FAQ, testimonial, feature block
- Pastel Category Tile: Colored feature block - style library, category cards
- Testimonial Card: Masonry-style horizontal card in the social-proof section
- FAQ Accordion Row: Expandable question/answer block
- Pill Tag / Chip: Category labels and status indicators
- Marquee Logo Strip: Endlessly scrolling brand logo wall
- Hero Gradient Banner: Decorative border/frame around hero artwork
- 3D Illustration Asset: Whimsical floating objects - clouds, crayons, envelopes, smiley faces, flowers
- Section Header: Centered display headline + supporting subhead

Do:

- Use weight 500 (not 600 or 700) for all display and heading type - the system is intentionally mid-weight, never bold
- Apply 32px border-radius to all content cards and 9999px to all interactive pills and tags
- Set the page canvas to #ebf5ff and card surfaces to #fafdff - the pale blue-to-bone-white shift is the primary depth mechanism
- Use the dark fill #181d27 for all filled buttons; reserve #0069e0 for accent borders and inline highlight text only
- Pull heading tracking to -0.02em and body tracking to -0.01em; never set type with default or positive letter-spacing
- Let 3D illustrations float in the canvas without cards, borders, or backgrounds - they are the brand voice, not decoration
- Use the iris gradient (71,157,255 0,105,224) only for thin 3px accent borders; never as a button fill or large surface

Avoid:

- Do not use bold weights (600+) for display headlines - Aeonik 500 is the ceiling
- Do not use 90 sharp corners on cards or buttons - minimum 16px, default 32px, pill 9999px
- Do not place saturated blue (#0069e0) as a button fill - it is an outline/accent color, not a CTA color
- Do not add box-shadows to content cards - depth comes from the canvas/surface color shift, not elevation
- Do not use body-weight black (#000000) for text - use #0a0d12, which has a hint of blue that ties to the canvas
- Do not mix more than two pastel washes in a single section - the pastel palette is for tile variety, not visual noise
- Do not set display type below 48px or use display sizes for body content - the scale has a hard floor for editorial moments

Source prompt cues:

Quick Color Reference:
- text: #0a0d12 (headings), #535862 (body), #93979f (muted)
- background: #ebf5ff (canvas), #fafdff (card), #ffffff (elevated)
- border: transparent default; #0069e0 for accent outlines
- accent: #0069e0 (iris blue - borders, highlights)
- primary action: #181d27 (filled action)

Example Component Prompts:
1. Create a hero section: #ebf5ff canvas, centered Aeonik 148px weight 500 headline in #0a0d12 with -0.02em tracking, a single 3D-rendered illustration floating below on transparent background, and one filled CTA button (#181d27, #ffffff text, 32px radius, 12px 32px padding, Geist 16px weight 500).
2. Build a feature card: #fafdff background, 32px border-radius, 40px padding all sides, Aeonik 48px weight 500 title in #0a0d12 with -0.96px tracking, Geist 18px body in #535862. No border, no shadow.
3. Create a pastel category tile: solid #f1e6ff (or #d3f6e3 / #cce7ff / #fff2be) background, 32px radius, 40px padding, Aeonik 32px weight 500 label in #0a0d12 centered, with a small 3D illustration inset.
4. Build a testimonial card: #fafdff background, 32px radius, 40px padding, Geist 18px quote in #535862, Geist 16px name in #0a0d12, Geist 14px role in #93979f, brand logo at the right.
5. Create a dark filled button: #181d27 background, #ffffff text, 32px radius, 12px 32px padding, Geist 16px weight 500, tight shadow ring (0 1px 2px rgba(10,13,18,0.8), 0 0 0 1px #0a0d12).

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
