# AI Implementation Prompt

Build a Morphic-inspired interface using this source-derived style bundle.

Reference site: https://morphic.com
Theme: dark
Category: AI
North star: Dark cinema canvas for AI storytelling. Pure black absorbs everything except the blue pulse of a single accent and the glow of generated imagery.

Use these palette anchors:

- Pure Black `#000000` for Page canvas, hero backgrounds, full-bleed sections - the void that makes all imagery and accent color read as luminous
- Surface One `#212121` for Primary card surface, elevated panels, and section backgrounds one level above the canvas
- Surface Two `#292929` for Secondary button background (ghost/outlined), nested cards, and hover surfaces one step lighter than Surface One
- Surface Three `#333333` for Tertiary button background, highest elevation layer, and active-state surface tints
- Paper White `#ffffff` for Primary headings, button text, logo, and high-emphasis copy on dark surfaces
- Fog `#e5e7eb` for Hairline borders and dividers - applied at very low opacity so cards have edge definition without visual weight
- Mist `#f5f5f5` for Soft highlight washes, secondary text on light surfaces, and subtle icon fills
- Mid Gray `#999999` for Muted body text, inactive labels, and disabled-state copy
- Steel `#737373` for Link text in resting state, secondary annotations, and icon strokes at low contrast
- Graphite `#666666` for Tertiary headings, caption text, and supporting metadata
- Slate `#525252` for Lowest-emphasis body text, helper copy, and subdued annotations
- Charcoal `#404040` for Icon strokes and outlines at medium contrast, secondary borders
- Electric Blue `#0075ff` for Blue action color for filled buttons, selected navigation states, and focused conversion moments.

Use these typography anchors:

- Inter `--font-inter` for Sole typeface across all UI, headings, and body. The complete weight range (400-700) allows a single family to carry the full hierarchy: 700 for display headlines, 600 for section headers, 500 for buttons and nav, 400 for body and captions. Inter's geometric neutrality and tall x-height make it ideal for a dark canvas where character width and spacing carry more visual weight than personality.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1280px.
- Section gap: 96px.
- Card padding: 12px.
- Element gap: 8px.

Build these component patterns where relevant:

- Primary CTA Button: The only filled chromatic action in the system
- Secondary Button: Non-primary action button on dark surfaces
- Outline Button: Tertiary or navigation-adjacent action
- Pill Tag: Category or filter label in card grids
- New Badge: Announcement indicator for new features
- Image Showcase Card: Display container for AI-generated images in the gallery grid
- Workflow Card: Horizontally-scrolling content card with title and description
- Tab Control: Product mode switcher in the Canvas product UI
- Navigation Bar: Top-level site navigation
- Hero Headline Block: Two-line display headline in the hero section
- Section Header: Repeating section title pattern (e.g., 'Workflows / Built for speed')
- Avatar Stack: Social proof element (e.g., review author avatars)

Do:

- Use #0075ff exclusively for primary actions and the 'New' badge - never as a decorative accent, background tint, or text color outside of a clickable element
- Apply the two-tone headline pattern (white line 1, #999999 line 2) for all section headers and the hero - this is the site's signature typographic device
- Use the surface stack #000000 #212121 #292929 #333333 for hierarchy; never introduce a new shade between steps
- Apply -0.0620em letter-spacing at 52px and -0.0480em at 40px for display text - the tight tracking is what makes the headlines feel cinematic
- Use 10px radius for image/showcase cards and 7px radius for buttons - these are the only two radii that should appear in the main content flow
- Keep all borders at 1px #e5e7eb at very low opacity (10-20%) - borders should be felt, not seen
- Use Inter at weight 500 for all buttons, 700 for display, 400 for body - never mix more than two weights on a single screen

Avoid:

- Never use a second chromatic color - the system is deliberately monochromatic with one blue accent; adding any other hue breaks the cinema-canvas concept
- Never apply drop shadows to UI components - shadows are reserved for image cards in the showcase grid only
- Never use #ffffff text for body copy - body text should be #999999 or lower contrast; white is reserved for headings, buttons, and high-emphasis labels
- Never center-align body paragraphs - only headlines, CTAs, and the hero text block are centered; body copy is left-aligned
- Never use border-radius values outside the defined scale (7px, 10px, 16px, 24px, 32px, 100px) - ad-hoc radii will break the system's geometric consistency
- Never place a colored background behind text blocks - the canvas must remain pure black; cards float on the void, they don't fill it
- Never use gradient backgrounds - the system is strictly flat; depth comes from the surface stack, not color transitions

Source prompt cues:

**Quick Color Reference**
- text (primary): #ffffff
- text (secondary/muted): #999999
- background (canvas): #000000
- border: #e5e7eb
- accent: #0075ff
- primary action: #0075ff (filled action)

**3-5 Example Component Prompts**

1. **Hero headline block**: Render a two-line headline on #000000 canvas. Line 1: 'Smart storytelling' at 52px Inter weight 700, #ffffff, letter-spacing -3.2px, line-height 1.15. Line 2: 'For every creative' at 52px Inter weight 700, #999999, letter-spacing -3.2px, line-height 1.15. No margin between lines. The gray echo on line 2 is the signature device.

2. **Primary CTA button**: Create a filled button with #0075ff background, #ffffff text at 14px Inter weight 500, 7px border-radius, 8px vertical padding, 16px horizontal padding. Text reads 'Start for free'. No border, no shadow. This is the only filled chromatic element in the system.

3. **New badge**: Create an inline badge with #0075ff background, #ffffff text 'New' at 12px Inter weight 500, 7px border-radius, 4px vertical padding, 8px horizontal padding. Sits inline with body text: 'Seedance 2.0 on all paid plans' at 12px Inter weight 400 #999999.

4. **Image showcase card**: Render a rectangular card with 10px border-radius, no border, no background - the AI-generated image fills the entire card area. Place on #000000 canvas. Optional soft shadow: rgba(0,0,0,0.1) 0px 20px 25px -5px, rgba(0,0,0,0.1) 0px 8px 10px -6px.

5. **Workflow card with caption**: Create a card with #212121 background, 10px border-radius, 1px #e5e7eb border at 15% opacity, 12px internal padding. Top 60% is an image at 10px top-corner radius. Below: title 'Time-freeze effect' at 14px Inter weight 600 #ffffff, description at 12px Inter weight 400 #999999.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
