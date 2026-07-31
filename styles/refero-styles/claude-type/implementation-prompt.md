# AI Implementation Prompt

Build a Claude Type-inspired interface using this source-derived style bundle.

Reference site: https://claudetype.com
Theme: light
Category: Design
North star: curated gallery on warm parchment

Use these palette anchors:

- Parchment Cream `#fcfbf7` for Primary page canvas and hero section background - warm off-white that flatters display serifs the way museum walls flatter paintings
- Pure Linen `#ffffff` for Card surfaces, button fills, icon strokes - the cleanest white sits one step above the cream canvas to separate cards from page
- Warm Linen `#e7e4e0` for Secondary surface and frosted nav background - a muted stone tone that softens the nav bar against the cream canvas
- Ink Black `#0d0d0f` for Primary text and button borders - near-black with a cool undertone, used for all body copy and the outlined button strokes
- Espresso `#2b1b1b` for Secondary text and hairline borders - a warm dark brown that acts as the dominant border color across cards, nav, and dividers
- Carbon `#000000` for SVG fills, logo marks, and icon strokes - pure black for the highest-contrast graphic elements
- Bitter Brown `#100401` for Dark showcase card background - nearly black with warm brown undertone, used for display type specimen cards to make white serifs glow
- Acid Lime `#99ff66` for Accent badge fill for metadata tags - the only chromatic color in the UI, used sparingly to mark type specs, style counts, and new releases

Use these typography anchors:

- MagicUIPro `--font-magicuipro` for Sole UI typeface - all navigation, body copy, buttons, labels, and section headings use this family at 11-18px; the custom font includes discretionary ligatures ("dlig") that add character to small text

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1400px.
- Section gap: 64-96px.
- Card padding: 16px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Frosted Glass Navigation Bar: Primary site navigation
- Pill Nav Link: Navigation item
- Arched Image Card: Product/editorial showcase card
- Dark Display Specimen Card: Typeface showcase on dark background
- Outlined Pill Button: Primary action button on dark cards
- Filled Dark Pill Button: Primary action on light backgrounds
- Acid Lime Badge: Metadata tag for type specimens
- Standard Card: Content card with border
- Section Title: Page section heading
- Hero Display Serif: Typeface specimen headline
- Gradient Feature Section: Promotional band between content blocks
- Footer: Site footer

Do:

- Use 100px border-radius for all interactive elements: nav bar, buttons, badges, and tags
- Use 900px border-radius for full-bleed image cards and dark specimen cards to create the signature arched/tombstone shape
- Set all body text in MagicUIPro weight 400 - never use bold weights in UI copy; the system stays visually quiet so display serifs can speak
- Reserve #99ff66 (Acid Lime) exclusively for metadata badges; never apply it to backgrounds, borders, or body text
- Use #2b1b1b (Espresso) for all hairline borders at 1px; this warm brown is the structural line color across the system
- Maintain generous spacing: 64px minimum between major sections, 14-16px within component groups
- Activate "dlig" font-feature-settings on all MagicUIPro text to enable the custom discretionary ligatures

Avoid:

- Do not add drop shadows, glows, or blur effects to cards or buttons - the system is shadow-free by design
- Do not introduce additional accent colors beyond #99ff66; the 3% colorfulness is intentional
- Do not use border-radius values below 10px for cards or 100px for interactive elements - the pill/arch vocabulary is binary
- Do not set body text above 18px or use MagicUIPro for display headlines; display serifs are product content, not UI
- Do not use pure white (#ffffff) as a page background - always use #fcfbf7 cream as the canvas
- Do not apply bold (600+) or semibold weights to MagicUIPro; the family exists at 400 only and any synthetic bolding breaks the system
- Do not center-align body paragraphs or create dense text blocks; the layout is gallery-sparse with generous line-height (1.6-2.0)

Source prompt cues:

**Quick Color Reference**
- text: #0d0d0f
- background: #fcfbf7
- card surface: #ffffff
- border: #2b1b1b
- accent badge: #99ff66
- dark card: #100401
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. **Frosted Glass Nav Bar**: Floating pill navigation with 100px border-radius, semi-transparent #e7e4e0 background, 1px #2b1b1b border, 14px vertical padding, 16px horizontal padding. Center the CLAUDE wordmark in MagicUIPro 14px weight 400. Place 'Typefaces' and 'Studio' links to the left, 'Trials' and 'Cart' to the right, all in #0d0d0f at 12px.

2. **Arched Image Card**: Full-bleed editorial photograph with 900px border-radius creating a tombstone arch shape. No padding, no border, no shadow. The image fills the entire card edge to edge. Use for fashion, portrait, or product photography in showcase rows.

3. **Acid Lime Metadata Badge**: Small pill badge with 100px border-radius, #99ff66 background, #0d0d0f text in MagicUIPro 12px weight 400. Padding 3px vertical, 10px horizontal. Place inline next to typeface names or metadata. This is the only chromatic element - use sparingly.

4. **Dark Display Specimen Card**: Full-bleed card with 900px border-radius, #100401 background. Center a large white display serif at 80-120px as the showcase headline. Below the text, place two outlined pill buttons side by side: 100px radius, 1px white border, transparent fill, white 14px MagicUIPro text, 14px vertical and 20px horizontal padding.

5. **Standard Content Card**: White (#ffffff) background, 16-32px border-radius, 1px #2b1b1b border, 16px internal padding. No shadow. Contains MagicUIPro body text at 14px in #0d0d0f with 1.6 line-height. Use for type listings, descriptions, and secondary content blocks.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
