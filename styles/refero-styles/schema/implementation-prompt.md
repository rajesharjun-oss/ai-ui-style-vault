# AI Implementation Prompt

Build a Schema-inspired interface using this source-derived style bundle.

Reference site: https://schema.figma.com
Theme: mixed
Category: Design
North star: Ink-black keynote stage with confetti-bright murals

Use these palette anchors:

- Obsidian `#000000` for Hero canvas, heavy structural borders, icon strokes - sets the high-contrast keynote-stage mood for the opening fold
- Ink `#0f0f0f` for Body and heading text on light surfaces, dark section borders
- Paper `#ffffff` for Page background, speaker card surfaces, light-section text on dark hero
- Ash `#e2e2e2` for Hairline borders, subtle icon fills, structural dividers between UI regions
- Mint Wash `#c7f8fb` for Teal wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Emerald Band `#24cb71` for Full-bleed accent section background - a bright green horizontal band that closes the hero composition

Use these typography anchors:

- Source Sans Pro `--font-source-sans-pro` for Source Sans Pro - detected in extracted data but not described by AI
- Figma Sans Display `--font-figma-sans-display` for Headlines and display copy - used at 56-86px for hero ('Schema by Figma', 'Meet our speakers!') with tight leading (0.90-1.10) and -0.02em tracking that makes type feel carved from a block. Weight 400 carries the design; 700 is reserved for emphasis.
- Figma Sans Text `--font-figma-sans-text` for Body, nav, button labels, supporting text. The companion text face at modest sizes (13-18px) with weight 400 as default and 600 for buttons/labels. -0.02em at 13px prevents the small type from feeling loose; 0.03em at 18px gives labels air.
- Figma Mono `--font-figma-mono` for Code or metadata snippets - used sparingly at 16px with 0.03em tracking for an architectural, monospaced accent in a world of proportional text
- Figma VF-normal-700-75 `--font-figma-vf-normal-700-75` for Figma VF-normal-700-75 - detected in extracted data but not described by AI
- Figma VF-normal-400-100 `--font-figma-vf-normal-400-100` for Figma VF-normal-400-100 - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 60px.
- Card padding: 16px.
- Element gap: 24px.

Build these component patterns where relevant:

- Top Navigation Bar: Persistent header across all sections
- Hero Outlined Register Button: Primary action on the dark hero
- Eyebrow Label: Section pre-heading (VIRTUAL, SPEAKERS, REGISTER)
- Display Headline: Section hero titles ('Schema by Figma', 'Meet our speakers!', 'Join us virtually!')
- Geometric Mural Banner: Decorative full-bleed section divider between hero and content
- Speaker Portrait Card: Speaker in the grid
- Event Status Notice: Inline status banner ('Event ended')
- Full-Bleed Color Section: Horizontal content band with colored background
- Date/Time Metadata Block: Event date and time under hero headline
- Grid Section Header: Section title block above card grid (e.g., "Meet our speakers!")

Do:

- Use 0px border-radius on all cards, buttons, images, and tags - sharp corners are non-negotiable
- Pair the dark hero with a large outlined button (1px Paper border, no fill); fill it on hover
- Apply Figma Sans Display at 56-86px with -0.02em tracking and 0.90-1.00 line-height for any headline that needs to feel carved
- Reach 0.03em tracking on small labels (13-18px) to give uppercase eyebrows and nav links air
- Alternate full-bleed colored bands (Mint Wash #c7f8fb, Emerald Band #24cb71) between dark and light sections to create visual rhythm
- Use Ash (#e2e2e2) 1px borders for hairline separation; reserve Ink (#0f0f0f) borders for emphasis on light sections
- Keep the UI monochrome - let color appear only in decorative murals and speaker portrait backgrounds, never in controls

Avoid:

- Don't add border-radius to any element - sharp corners define the system's poster-like character
- Don't use shadows, glows, or blur effects - flat is the only elevation language here
- Don't introduce a chromatic CTA color - the system is intentionally monochrome, actions are outlined or text-only
- Don't set body text below 16px; captions can go to 13px but never smaller
- Don't let display headlines exceed 0.90-1.00 line-height - tight leading is what makes them feel architectural
- Don't color-fill buttons with brand hues; outlined Paper-on-Obsidian is the only button pattern in the system
- Don't separate light sections with gray bands - use either full-bleed color or seamless Paper-to-Paper flow

Source prompt cues:

**Quick Color Reference**
- text on light: #0f0f0f (Ink)
- text on dark hero: #ffffff (Paper)
- page background: #ffffff (Paper)
- hero background: #000000 (Obsidian)
- hairline borders: #e2e2e2 (Ash)
- accent section band 1: #c7f8fb (Mint Wash)
- accent section band 2: #24cb71 (Emerald Band)
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Dark hero with outlined Register button**: Full-bleed Obsidian (#000000) background, left-aligned content with 60px horizontal padding. Eyebrow 'VIRTUAL' at 13px Figma Sans Text weight 400, uppercase, tracking 0.03em, Paper color. Headline 'Schema by Figma' at 72px Figma Sans Display weight 400, line-height 0.90, letter-spacing -1.44px, Paper. Date/time block at 18px Figma Sans Text, Paper, 16px gap between lines. Register button: full-width within content column, 64px tall, 1px Paper border, 0px radius, no fill, 'Register' at 24px Figma Sans Text weight 400 centered, Paper text.

2. **Speaker card in a 4-column grid**: 0px radius portrait image, 1:1 aspect ratio, placed on a solid lavender (#b8b3ff) background. 24px gap below portrait, then name 'Loredana Crisan' at 18px Figma Sans Text weight 600 in Ink, title 'Chief Design Officer / Figma' at 16px weight 400 in Ink with 4px line gap. Cards separated by 48px vertical and 24px horizontal gaps; grid sits inside a 1200px max-width container with 60px section padding above.

3. **Geometric mural divider**: Full-bleed, 250px tall, no padding. Layer flat shapes: 200px indigo (#4a4afc) circle bottom-left, 120px lavender (#b8b3ff) rectangle top-center, 80px maroon (#7a2e2e) hexagon right-center on a 120px mint (#c7f8fb) square, 60px orange (#ff6b2c) circle far right, 180px emerald (#24cb71) rectangle bottom-right. No gradients, no shadows, no border-radius.

4. **Light section header**: Paper background. Eyebrow 'SPEAKERS' at 13px Figma Sans Text weight 600, uppercase, tracking 0.03em, Ink color. 16px gap to headline 'Meet our speakers!' at 56px Figma Sans Display weight 400, line-height 1.00, letter-spacing -1.12px, Ink. 60px gap below to grid.

5. **Event status notice on colored band**: Mint Wash (#c7f8fb) full-bleed section, 60px vertical padding, right-aligned content block. 24px Ink triangular warning icon, 16px gap, label 'Event ended' at 18px Figma Sans Text weight 600 Ink, subtext 'This event has already ended.' at 16px weight 400 Ink.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
