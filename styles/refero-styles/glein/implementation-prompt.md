# AI Implementation Prompt

Build a Glein-inspired interface using this source-derived style bundle.

Reference site: https://glein.wien
Theme: light
Category: E-commerce
North star: Atelier lookbook on warm linen - full-bleed photography, hairline rules, one whisper-weight voice.

Use these palette anchors:

- Midnight Ink `#000000` for Primary text, nav hairline borders, footer dividers, section rules, button text. Dominant structural color - defines the graphic skeleton against the warm canvas
- Bone White `#ffffff` for Page canvas, card surfaces, overlay text on dark imagery, cookie dialog background. The breathing space
- Warm Sand `#ebe6dc` for Secondary surface and section bands - the warm beige that gives the atelier its linen-like tactility. Section dividers, footer wash, category card backgrounds
- Concrete Gray `#8c8c8c` for Muted secondary text, tertiary borders, subdued image overlays. The recede color - present but never competing
- Ash Gray `#b3b3b3` for Subtle dividers, inactive nav borders, low-emphasis rules. The quietest member of the scale

Use these typography anchors:

- F-Grotesk `--font-f-grotesk` for Primary grotesque - used for everything from body to display. The entire type system runs at weight 400 only; hierarchy is pure scale.
- Maison-Neue-Mono `--font-maison-neue-mono` for Monospace companion - navigation, category labels, button text, footer meta, promotional strip. The 'labelling' voice that contrasts the editorial grotesque.

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: .
- Section gap: 42px.
- Card padding: 13px.
- Element gap: 13px.

Build these component patterns where relevant:

- Category Image Tile: Primary navigation and discovery surface - large editorial image with overlaid white category title
- Editorial Section Block: Scrolling content band that mixes imagery with body text
- Top Promo Strip: Persistent thin announcement bar above the navigation
- Primary Navigation: Top-level site navigation with brand wordmark center
- Hairline CTA Button: Micro interactive element - 'Alle akzeptieren' and 'Auswahlen' in the cookie dialog
- Monospace Text Link: Inline navigational link - 'mehr anzeigen' below category titles, footer links
- Cookie Consent Dialog: GDPR consent overlay
- Image Grid Container: The layout chassis for category and product imagery
- Brand Wordmark: Centered logo lockup in the primary navigation

Do:

- Keep every element at weight 400 - F-Grotesk and Maison-Neue-Mono both run single-weight. Build hierarchy through size and space, never through bold.
- Let photography fill the viewport edge to edge. No internal gutters in image grids, no rounded corners, no borders around photos.
- Overlay white F-Grotesk category titles directly on imagery. Use 30px for category names, 13px monospace for 'mehr anzeigen' sub-links.
- Separate sections with warm sand (#ebe6dc) bands or 1px #000000 hairlines - never with shadows or card elevation.
- Use Maison-Neue-Mono for all functional labels: nav items, buttons, tags, footer meta. The mono face is the system's 'utility voice'.
- Let the display type breathe: 111px F-Grotesk at line-height 1.0 with generous surrounding whitespace. No letter-spacing tightening - the natural mono-influenced rhythm of F-Grotesk carries it.
- Use the 2px/6px micro-padding for all interactive elements. Buttons are stamp-sized by design, not 'small by accident'.

Avoid:

- Don't introduce any chromatic color. The system is 0% colorful - adding even one accent breaks the entire monochrome contract.
- Don't use bold, semibold, or light weights. The font files are loaded at 400 only; attempting 500/600/700 will fall back or look wrong.
- Don't add shadows, glows, or blur effects. The surface model is flat - elevation is communicated by warm-band transitions, not z-axis depth.
- Don't round corners. Every radius in the system is 0px. Adding border-radius introduces a 'card' or 'button' feel that contradicts the editorial-paper aesthetic.
- Don't use sans-serif for functional labels. Monospace is reserved for nav, buttons, and meta - mixing it with F-Grotesk here dilutes the atelier voice.
- Don't crowd the 111px display with surrounding UI. Display type needs air - no buttons, links, or images in its immediate margin zone.
- Don't use colored hover states on links. Underline-on-hover in the same color is the only state change the system supports.

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- secondary surface: #ebe6dc (Warm Sand)
- border: #000000 (1px hairline)
- muted text: #8c8c8c
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Category Image Tile*: Full-bleed 3-column grid cell containing a fashion photograph. No padding, no border, no radius. White F-Grotesk 30px category title ('Leinen') overlaid at bottom-left, with 13px Maison-Neue-Mono 'mehr anzeigen' link directly beneath in #ffffff.

2. *Top Navigation*: Full-width bar with 1px #000000 bottom border. Left: 'SHOP' and 'NACHHALTIGE MATERIALIEN' in 13px Maison-Neue-Mono #000000. Center: 'Glein' wordmark in F-Grotesk 20px #000000. Right: 'STUDIO', 'DE | EN', 'Warenkorb' in 13px Maison-Neue-Mono. 18px top padding, 11px bottom padding. Background: #ffffff.

3. *Ghost Outlined Button*: White background, 1px #000000 border, zero radius. Text 'Auswahlen' in F-Grotesk 13px #000000. Padding 2px vertical, 6px horizontal. No hover state change beyond a background-color shift to #ebe6dc.

4. *Editorial Text Block*: Centered narrow column (~400px max-width) on #ebe6dc warm sand background. Body text in F-Grotesk 20px weight 400, line-height 1.3, color #000000. No headings, no decorations - just generous typographic space.

5. *Promo Strip*: Full-width 1px #000000 bottom border, 11px top/bottom padding. Text 'GRATIS VERSAND AB EUR 150,-' repeated 3x in 13px Maison-Neue-Mono #000000, separated by whitespace, on #ffffff background.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
