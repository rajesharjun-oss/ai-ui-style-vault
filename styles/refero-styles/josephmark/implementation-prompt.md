# AI Implementation Prompt

Build a Josephmark-inspired interface using this source-derived style bundle.

Reference site: https://josephmark.studio
Theme: dark
Category: Agency
North star: Midnight editorial gallery. Monochrome walls, warm spotlights, oversized grotesque typography floating in negative space.

Use these palette anchors:

- Carbon Black `#000000` for Primary dark canvas - hero backgrounds, full-bleed section stages, base for the editorial atmosphere
- Pure White `#ffffff` for Inverse text on dark canvases, form field backgrounds, button text on filled dark elements
- Stone Taupe `#a9a498` for The system's sole warm chromatic note - muted link states, secondary surface tints, paper-like card backgrounds that soften the black-to-gray transitions
- Bone Cream `#f4f5ef` for Warm off-white surface - secondary card and panel backgrounds, breaks the clinical feel of pure white and echoes the studio's paper-based brand collateral
- Mist Gray `#e5e7eb` for Hairline borders, dividers, list separators, subtle structural lines - the 999-occurrence border color that defines spatial relationships without visual weight
- Graphite `#666666` for Mid-tone text - secondary headings, supporting copy, metadata that needs presence without competing with primary type
- Forest Ink `#4e5449` for Body text on light surfaces - a desaturated dark olive that reads warmer than pure black, the only hue-leaning neutral in the system

Use these typography anchors:

- Scto Grotesk A `--font-scto-grotesk-a` for The sole typeface - a custom neo-grotesque used for everything from 70px display headlines down to 12px captions. Weight 300 carries display and large headings (a deliberate anti-convention choice - most agency sites use bold for impact; Josephmark whispers with light). Weight 400 for body, 500 reserved for emphasis and interactive elements. The consistent aggressive negative tracking (-0.019em to -0.035em) tightens the grotesque's natural apertures, creating a compressed, editorial density even at body sizes.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: .
- Section gap: 64-96px.
- Card padding: 16-24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Editorial Hero: Full-bleed dark opening section with oversized headline
- Minimal Nav Bar: Transparent top navigation
- Pill Text Button: Primary interactive element
- Project Showcase Card: Case study entry in grid
- Cream Content Insert: Warm light section breaking the dark rhythm
- Arrow Link: Directional text link with chevron icon
- Section Heading: Editorial sub-section title
- Body Text Block: Paragraph and supporting copy
- Horizontal Divider: Structural separator between content blocks
- Menu Toggle: Full-screen navigation overlay

Do:

- Use Scto Grotesk A at weight 300 for all display and heading sizes - the light weight is the signature, not a fallback
- Apply negative letter-spacing consistently: -0.035em at display (70px), scaling proportionally to -0.019em at caption (12px)
- Build with full-bleed sections, not contained max-width layouts - let the dark canvas extend to the viewport edges
- Use #000000 and #f4f5ef as the two primary canvas colors, alternating between them for section rhythm
- Define interactive elements with 1px borders and 9999px radius - the pill shape is the only button form
- Set body text at 16px/1.38 with #ffffff on dark and #4e5449 on light surfaces
- Separate content blocks with 1px #e5e7eb hairlines, never with shadows or background fills

Avoid:

- Do not introduce color beyond the single warm taupe (#a9a498) - the system's power comes from its 1% colorfulness
- Do not add shadows, glows, or any drop effects - this system is rigorously flat
- Do not use rounded corners on cards, images, or containers - only buttons are rounded (to 9999px)
- Do not center text - everything is left-aligned, following editorial column logic
- Do not use bold weights (600+) for emphasis - the scale goes 300 400 500, and contrast comes from size and color, not weight
- Do not add icon systems or decorative graphics - typography and photography are the only visual elements
- Do not use #ffffff as a section background - it appears only as surface within forms and as text color on dark

Source prompt cues:

**Quick Color Reference**
- text (on dark): #ffffff
- text (on light): #4e5449
- text (secondary): #666666
- background (primary dark): #000000
- background (warm light): #f4f5ef
- border: #e5e7eb
- accent: #a9a498
- primary action: no distinct CTA color

**Example Component Prompts**

1. Create a full-bleed hero section: #000000 background, padding-top 96px, padding-bottom 64px. Display headline at 70px, Scto Grotesk weight 300, #ffffff, letter-spacing -2.45px, line-height 1.10. Left-aligned, no max-width.

2. Create a project showcase card: no border, no radius, no shadow. Full-bleed image fills the card on #000000 background. Project title at 20px weight 400, #ffffff, letter-spacing -0.5px, positioned below the image with 16px gap.

3. Create a cream content insert: #f4f5ef background, 0px radius, padding 64px. Section heading at 36px weight 300, #000000, letter-spacing -1.08px. Body text at 16px weight 400, #4e5449, line-height 1.38. Product image right-aligned with no border.

4. Create a pill text button: 9999px border-radius, 1px solid #e5e7eb border, transparent fill, padding 8px 20px. Text at 14px weight 500, #ffffff, letter-spacing -0.28px. On dark backgrounds only.

5. Create a full-screen menu overlay: covers viewport with #000000. Nav links stacked vertically at 70px weight 300, #ffffff, letter-spacing -2.45px, with 40px vertical gap between items. Left-aligned with 28px padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
