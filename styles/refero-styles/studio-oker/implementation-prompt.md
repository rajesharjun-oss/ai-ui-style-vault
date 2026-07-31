# AI Implementation Prompt

Build a Studio Oker-inspired interface using this source-derived style bundle.

Reference site: https://oker.com
Theme: dark
Category: Agency
North star: darkened gallery with scarlet punctuation - a black-walled portfolio room where white type floats and one red whisper cuts through the silence.

Use these palette anchors:

- Pure Black `#000000` for Page canvas, section backgrounds, project card fills - the void everything else floats on
- Soft Black `#101010` for Subtle surface elevation over the pure black canvas, card backgrounds in tight stacks
- Bone White `#ffffff` for Primary text, headings, hairline borders, nav text - the only light in the room
- Fog Gray `#a0a0a0` for Secondary text, metadata, captions, image borders, inactive labels
- Graphite `#484848` for Footer borders, section dividers, rare structural lines that recede into the dark
- Scarlet Signal `#e4002b` for Supporting palette color for small decorative accents when the core palette needs contrast.
- Rose Brand Spectrum `#f5a5a5` for Brand color exploration panel - a pink-to-black swatch that walks from #f5a5a5 #e85a5a #d42020 #7a0a0a #2a0606 #000000 as a literal brand-color system reveal

Use these typography anchors:

- NextBook `--font-nextbook` for The studio's own custom display and text face. Weight 300 whispers in section headings and 80px display; weight 400 carries body, labels, and nav. Used across every context - hero, body, heading, link, list, icon, footer.
- Circular Std `--font-circular-std` for Referenced inside project case studies (the 'AaBbCc 1234' specimen tile) as a client font example - not part of Studio Oker's own UI system

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: .
- Section gap: 120px.
- Card padding: 16px.
- Element gap: 16px.

Build these component patterns where relevant:

- Top Navigation Bar: Site-wide persistent header
- Project Tile Card: Grid cell in the work showcase
- Full-Bleed Red Panel: Hero-scale statement tile (e.g. 'Think Big.')
- Brand Color Swatch Panel: A literal brand-system reveal inside a project tile
- Typography Specimen Tile: A client's font system displayed inside a project card
- Section Heading: Top-of-section title for Feed, Studio, etc.
- Studio Stat Block: Compact label/value pairs in the About/Studio section
- Services List: Vertical list of service offerings
- Project Showcase Card (Feed): Large format work card with image + caption
- Link with Red Dot: Standalone call-to-action / read-more affordance
- Footer: Page-bottom site info

Do:

- Use Pure Black (#000000) as the universal background - never introduce gray surfaces, tints, or off-white panels
- Set all radii to 0px - cards, buttons, images, and tags all share sharp corners
- Use NextBook weight 300 at 80px for section headings, with -0.02em letter-spacing (-1.6px) - the whisper-weight is the signature, not the size
- Reserve Scarlet Signal (#e4002b) for exactly one use per screen - a single red dot, a single red panel, or a single red link - never as a fill color across multiple elements
- Honor the 120px section gap and 240-264px breathing-room margins as the page's structural rhythm; collapse these only inside dense tile grids
- Use #a0a0a0 for ALL secondary text, metadata, and image borders - never invent intermediate grays
- Treat photographs as edge-to-edge artwork with no inner padding, no rounded corners, and no overlay treatments

Avoid:

- Don't add drop shadows, inner shadows, or glow effects - the system uses void, not elevation, to separate elements
- Don't introduce a second accent color - the scarlet is the only chromatic signal in the entire system
- Don't use bullet points, numbered lists, or icon prefixes in body copy - the Services list and Studio stat block prove that raw stacked text carries more weight than decorated lists
- Don't center-align body paragraphs - every long-form block is left-aligned and reads as a typographic column, not a display statement
- Don't use buttons with backgrounds - actions are dots, links, or text; the red dot IS the button
- Don't add gradients to UI elements (the rose panel is a single brand artifact, not a pattern to replicate on cards, buttons, or backgrounds)
- Don't use NextBook weight 600+ - the system only operates at 300 and 400; bolder weights would break the whisper-confident voice

Source prompt cues:

**Quick Color Reference**\n- text: #ffffff\n- secondary text: #a0a0a0\n- background: #000000\n- border / divider: #a0a0a0 or #484848\n- accent (scarce): #e4002b\n- primary action: no distinct CTA color

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
