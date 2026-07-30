# AI Implementation Prompt

Build a Waka Waka-inspired interface using this source-derived style bundle.

Reference site: https://wakawaka.world
Theme: light
Category: Design
North star: museum poster in bone and ink - monumental black grotesk type printed on warm off-white paper, everything else recedes

Use these palette anchors:

- Bone Paper `#edeae4` for Page background, all canvas surfaces - warm off-white that reads as unbleached paper rather than digital white
- Stone Gray `#c9c7c4` for Secondary surface and muted contextual neutral - appears in contrast pairings as a slightly deeper layer below the canvas
- Ink Black `#28282a` for Primary text, all borders, hairline rules, icon strokes, and the only chromatic anchor in the system - near-black with a hint of warmth so it sits comfortably on the bone background instead of vibrating

Use these typography anchors:

- Waka Sans `--font-waka-sans` for Single custom grotesk used for everything from 10px captions to 560px display - tight tracking scales with size (-0.09em at display, -0.02em at body) so the enormous type locks into a dense block while body text stays readable. The 0.80-0.83 line-height at display size is the signature: letterforms stack into an almost solid mass of ink

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Monumental Display Headline: Hero wordmark and section dividers
- Editorial Section Heading: Mid-scale titles and category labels
- Product Image Plate: Photography containers in grid layouts
- Hairline Divider: Section and content separators
- Nav Link: Top navigation items
- Footer Text: Bottom page information
- Outlined Action Border: The only interactive element treatment available
- Icon Stroke: All iconography
- Full-Bleed Poster Page: Landing and index pages

Do:

- Use Waka Sans weight 700 at 560px with line-height 0.80 and letter-spacing -0.09em for any monumental display element - this is the system's single most recognizable choice
- Set all backgrounds to #edeae4 and all text, borders, and icons to #28282a - never introduce a second color
- Use 0px border-radius on every component including cards, buttons, and image containers
- Use hairline 1px #28282a dividers and borders instead of background-color contrast to separate content
- Set tight letter-spacing at scale: -0.09em at display, -0.03em at subheading, -0.02em at body
- Keep spacing compact: 10px element gaps, 20px container padding, 80px section gaps
- Let product photography sit directly on the bone background with no frame, shadow, or radius

Avoid:

- Do not introduce any chromatic color, gradient, or accent hue - the system is strictly two-tone
- Do not use filled buttons, colored backgrounds, or background-fill hover states on interactive elements
- Do not apply border-radius greater than 0px to any element
- Do not use box-shadow or any elevation effect - surfaces are flat
- Do not set type below 10px or above 560px - the scale is deliberate and extreme
- Do not use light line-heights (1.5+) on display or heading sizes - 0.80-1.00 is required to maintain density
- Do not separate sections with colored bands or background fills - use whitespace and hairline rules only

Source prompt cues:

**Quick Color Reference**
- background: #edeae4
- text: #28282a
- border: #28282a
- accent: no accent color
- primary action: no distinct CTA color

**3-5 Example Component Prompts**
1. *Create a hero poster section:* Full-viewport on #edeae4 background. Headline at 560px Waka Sans weight 700, color #28282a, line-height 0.80, letter-spacing -50.4px (-0.09em). Subtitle at 18px weight 400, color #28282a, letter-spacing -0.36px. No buttons, no decoration - the type is the hero.

2. *Create a product image grid:* 2-column grid with 10px gap on #edeae4 background. Each cell is a product photograph filling the cell edge-to-edge with 0px radius, no border, no padding, no shadow. Caption below each image at 10px Waka Sans weight 400, color #28282a, 6px margin-top.

3. *Create a minimal top navigation:* Full-width on #edeae4 background, 20px horizontal padding. Nav items in Waka Sans weight 500 at 14px, color #28282a, 10px horizontal gap between items. No background, no border, no underline on hover - just a quiet list of words.

4. *Create a section divider:* Full-width 1px solid #28282a hairline rule, no padding, no margin decoration. This is the only structural separator in the system.

5. *Create a footer colophon:* 3-column text block at the bottom of the page on #edeae4 background, 20px horizontal padding, separated from content above by a 1px #28282a hairline. Text in Waka Sans weight 400 at 10-14px, line-height 1.6, color #28282a.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
