# AI Implementation Prompt

Build a Channel Studio-inspired interface using this source-derived style bundle.

Reference site: https://channel.studio
Theme: dark
Category: Agency
North star: Studio darkroom with a single coral flare

Use these palette anchors:

- Bone Gray `#cacaca` for Primary text on dark surfaces, hairline borders on images and links, divider strokes - a desaturated near-white that reads softer than pure #fff against black
- Carbon Black `#0a0a0a` for Page background, section canvas, project card surface - the entire design lives here
- Iron Gray `#727272` for Muted secondary text, low-emphasis borders, caption-level metadata
- Coral Flare `#ff7777` for Accent for project titles, signature heading borders, and occasional decorative strokes - the only chromatic element in the system, used sparingly for editorial emphasis

Use these typography anchors:

- Lausanne `--font-lausanne` for Sole typeface across all roles - navigation, body, subheadings, and display headlines. Weight stays at 400 throughout; visual hierarchy is built entirely through size and tracking, not weight. Display at 75px uses line-height 0.90-0.95, creating a compressed poetry-staircase effect unique to this system.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 40px.
- Card padding: 0px.
- Element gap: 10px.

Build these component patterns where relevant:

- Top Navigation: Primary site navigation
- Hero Display Headline: Hero section typography
- Full-Bleed Hero Background: Atmospheric hero surface
- Section Display Headline: Large editorial text on black panels
- Client Logo Strip: Social proof / client listing
- Project Card: Portfolio entry / case study preview
- Arrow Link: Text link with directional indicator
- Decorative Coral Border: Signature accent stroke
- Footer: Site footer
- Inline 3D Render: Decorative/artistic element

Do:

- Use #cacaca for all text and borders on black surfaces - never pure #fff, the slight desaturation is the signature
- Set display headlines at 75px with line-height 0.90 and letter-spacing -0.03em for the compressed staircase effect
- Reserve #ff7777 exclusively for project titles and signature borders - never use it for body text, navigation, or UI controls
- Keep all radii at 0px - sharp edges are non-negotiable for this editorial aesthetic
- Use full-bleed imagery (viewport-width) for all project cards and hero sections; never constrain images to card-sized containers
- Maintain generous vertical spacing: 40px between sections, 192px above the footer
- Set all type in Lausanne weight 400 - build hierarchy through size and tracking, never through bold weights

Avoid:

- Never use shadows, gradients, or any elevation effects - the design is deliberately flat
- Never add border-radius to cards, buttons, images, or any element - 0px everywhere
- Never use color other than #ff7777 for accents - no blues, greens, or other hues; the system is monochromatic plus one coral
- Never set body or heading text in pure #fff - always use #cacaca for the softened-light quality
- Never use multiple font weights - the system is weight 400 only across all roles
- Never use centered text alignment for body content - everything is left-aligned with the viewport edge
- Never add background colors to cards, buttons, or interactive elements - they sit directly on the black canvas

Source prompt cues:

**Quick Color Reference**
- text: #cacaca
- background: #0a0a0a
- border: #cacaca (1px hairlines)
- accent: #ff7777 (project titles, signature borders only)
- muted text: #727272
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. **Project Card**: Full-bleed image filling 100vw width. Above the image on a black #0a0a0a panel: small uppercase label in 13px Lausanne weight 400, letter-spacing -0.26px, color #cacaca. Project title at 45px Lausanne weight 400, line-height 1.19, letter-spacing -1.35px, color #ff7777. Right-aligned 'See Project ' link in 13px #cacaca. Zero border-radius on everything.

2. **Hero Section**: Full-bleed grayscale photographic background (soft studio lighting texture). Top-left: 'C:S' logo at 18px Lausanne weight 400, color #cacaca. Below: nav links (Home, Projects, About, Careers) at 13px #cacaca with 9px vertical gap. Display headline at 75px Lausanne weight 400, line-height 0.90, letter-spacing -2.25px, color #cacaca, left-aligned.

3. **Client Logo Row**: Small label 'Select Clients:' in 13px Lausanne weight 400, color #cacaca. Below: horizontal row of grayscale client logos, each rendered in #cacaca, evenly spaced with 19px gaps. No borders, no backgrounds.

4. **Type-Only Section**: Black #0a0a0a background. Display text at 75px Lausanne weight 400, line-height 0.95, letter-spacing -2.25px, color #cacaca, left-aligned. Optional 3D render or abstract visual element positioned to the right of or below the text block.

5. **Arrow Link**: Plain text in 15px Lausanne weight 400, color #cacaca, followed by a thin arrow character. No underline, no background, no border. Padded with 10px margins from surrounding elements.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
