# AI Implementation Prompt

Build a Lovable-inspired interface using this source-derived style bundle.

Reference site: https://lovable.dev
Theme: light
Category: AI
North star: Warm parchment canvas behind a single prismatic horizon

Use these palette anchors:

- Parchment `#fcfbf8` for Page canvas, primary background, card surfaces when on darker parents
- Warm Sand `#f7f4ed` for Card backgrounds, elevated surface panels, secondary containers
- Linen Border `#eceae4` for All borders - nav dividers, card outlines, input strokes, section separators. Warm beige rather than cool gray gives the entire UI its distinctive non-tech softness
- Stone `#d4d3d0` for Subtle box-shadow tints, disabled borders, secondary dividers
- Dim Gray `#5f5f5d` for Secondary text, placeholder text, muted nav labels, subheadings
- Charcoal `#1c1c1c` for Primary text, nav labels, icon fills, inverse button background. Near-black rather than pure black keeps the warm tone consistent
- Ink `#030303` for Highest-emphasis text (hero headline, button labels in chat input), icon fills
- Indigo Accent `#3451b2` for Reserved accent from CSS tokens (--bg-accent). Inline text links, focus rings, accent highlights when needed

Use these typography anchors:

- Camera Plain Variable `--font-camera-plain-variable` for The only typeface on the entire site. A custom variable-weight sans-serif that carries both body text and display headlines. The 480 weight is unusual - heavier than normal but not semi-bold, giving headlines a confident but non-aggressive stance. Ligatures are explicitly disabled ("liga" 0), keeping the letterforms mechanical and preventing decorative swashes.

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1280px.
- Section gap: 64-80px.
- Card padding: 20-24px.
- Element gap: 6-8px.

Build these component patterns where relevant:

- Ghost Nav Button: Top navigation items
- Outlined Pill Button: Secondary actions like 'Log in'
- Dark Pill Button: Primary action ('Get started')
- Frosted Pill Button: Overlay actions on the hero gradient
- Chat Input Card: Hero prompt area where users type their app idea
- Template Preview Card: Template gallery items in the 'Discover templates' grid
- Warm Surface Card: Feature explanation panels, content containers
- Logo Bar: Social proof strip showing company logos
- Section Heading: Major content section titles like 'Meet Lovable', 'Discover templates'
- Feature Step: Numbered feature explanations ('Start with an idea', 'Watch it come to life')
- View All Link: Secondary navigation to full listings
- Sticky Navigation Bar: Top-of-page persistent navigation

Do:

- Use 9999px border-radius for all buttons, badges, and pill-shaped controls - the full-pill shape is the signature interactive affordance
- Keep the palette almost entirely achromatic; reserve chromatic color exclusively for the hero gradient and semantic states - never for buttons, links, or UI accents
- Apply -0.025em letter-spacing globally across all text sizes; this tight tracking is a defining characteristic of the type system
- Use #f7f4ed (Warm Sand) for card surfaces and #fcfbf8 (Parchment) for the page canvas - the two warm whites create the surface hierarchy
- Use weight 480 for headings and weight 400 for body text - this subtle weight contrast (not bold vs regular) defines the typographic hierarchy
- Set 'liga' 0 in font-feature-settings on all text to disable ligatures, matching the original type rendering
- Use 1px solid #eceae4 for all borders - dividers, card outlines, input strokes, nav separators - one warm beige border color everywhere

Avoid:

- Never use cool grays (#e5e7eb, #6b7280) - all neutrals skew warm with a yellow undertone; cool grays would break the parchment atmosphere
- Never apply colored backgrounds to buttons; the primary action is near-black (rgba(0,0,0,0.88)) and secondary is transparent - there is no colored CTA
- Never use drop shadows for elevation except on the chat input card; most cards and surfaces are flat with no shadow at all
- Never use more than one font family - Camera Plain Variable (or its substitute) handles everything from 14px captions to 60px display headlines
- Never use sharp corners (0px radius) on interactive elements; even image thumbnails get 12px radius
- Never use the hero gradient colors on individual UI components like buttons, badges, or icons - the gradient exists only as a full-bleed atmospheric background
- Never add visual weight to feature sections with icons, colored badges, or decorative elements - this system communicates through type weight and scale alone

Source prompt cues:

**Quick Color Reference**
- text (primary): #1c1c1c
- text (high emphasis): #030303
- text (secondary): #5f5f5d
- background (canvas): #fcfbf8
- background (card): #f7f4ed
- border: #eceae4
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Hero Section**: Full-bleed gradient background using linear-gradient(90deg, #1c1c1c 0%, #1c1c1c 33%, #82bcff 40%, #2483ff 45%, #ff66f4 50%, #ff3029 55%, #fe7b02 60%, transparent 67%). Center a headline at 60px weight 480, #1c1c1c, letter-spacing -1.5px, line-height 1.0. Below it, subtitle at 18px weight 400, #5f5f5d. Below that, a floating chat input card: #f7f4ed background, 24px radius, 24px padding, shadow oklab(0 0 0 / 0.08) 0px 0px 0px 1px, rgba(0,0,0,0.1) 0px 20px 25px -5px, rgba(0,0,0,0.1) 0px 8px 10px -6px.

2. **Navigation Bar**: Sticky, backdrop-filter blur(4px), rgba(255,255,255,0.8) background. Logo left. Center: text links at 15px weight 400 #1c1c1c, no underline, 6px horizontal gaps. Right: 'Log in' as outlined pill (transparent bg, 1px solid #eceae4, 9999px radius, 6px 10px padding, #1c1c1c text) and 'Get started' as dark pill (rgba(0,0,0,0.88) bg, #fcfbf8 text, 9999px radius, 6px 10px padding).

3. **Template Card Grid**: 4-column grid on #fcfbf8 canvas. Each card: no background, no border, no shadow. Screenshot image with 12px radius at top. Title at 16px weight 480 #1c1c1c below image (8px gap). Description at 14px weight 400 #5f5f5d (4px gap below title). All text letter-spacing -0.025em, font-feature-settings "liga" 0.

4. **Feature Section (2-column)**: Left column: warm surface card (#f7f4ed, 24px radius, 24px 20px padding) containing a UI mockup. Right column: stack of 3 feature blocks, each with heading at 36px weight 480 #1c1c1c (line-height 1.1, letter-spacing -0.9px) and body at 16px weight 400 #5f5f5d. 32px gap between blocks.

5. **Section Header**: Left-aligned heading at 48px weight 480 #1c1c1c, letter-spacing -1.2px, line-height 1.1. Subtitle at 16px weight 400 #5f5f5d, 8px below. Optional 'View all' pill link aligned right: 15px weight 400 #030303, 1px solid #eceae4 border, 9999px radius, 6px 10px padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
