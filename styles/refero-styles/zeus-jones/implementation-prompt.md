# AI Implementation Prompt

Build a Zeus Jones-inspired interface using this source-derived style bundle.

Reference site: https://zeusjones.com
Theme: light
Category: Agency
North star: risograph broadsheet on warm cream - a page that prints like a zine and loads like a gallery.

Use these palette anchors:

- Midnight Ink `#1a1c2c` for Primary text, filled pill buttons, hairline borders, dark surfaces - the only chromatic color in the system; near-black with a barely-perceptible cool navy cast that softens the contrast against warm cream without losing the gravitas of pure black
- Warm Parchment `#fcfaf3` for Page canvas and light surface base - a creamy off-white that replaces the default SaaS pure-white with paper warmth, making the page feel printed rather than rendered
- Soft Linen `#ebe9e4` for Elevated card and panel surface - one step darker than the canvas, used sparingly to lift a card or a section band without introducing a new color
- Obsidian `#000000` for SVG icon fills and decorative monochrome marks - reserved for vector assets where true black reads cleaner than the navy-tinted Midnight Ink
- Blush Coral `#fd9494` for Sporadic warm accent - emerges from the hero aurora and may surface in tag dots or decorative washes; the only warm hue that earns a place in an otherwise cool-neutral system

Use these typography anchors:

- ZJSansDisplay `--font-zjsansdisplay` for Primary typeface for body, navigation, subheadings, and the 40-48px heading range. The 12px eyebrow and tag text carries +0.05em tracking (letter-spacing: 0.6px at 12px) to read as a small caps eyebrow; everything at 16px and above sits at -0.02em (-0.32px at 16px) for tight, editorial density. This is the working sans that does 95% of the page's communicative labor.
- FeatureDeckLight `--font-featuredecklight` for Hero display face used at 60-90px with line-height compressed to 1.07-1.11. Weight 100 is the anti-convention signature: while every agency site uses 600-800 for display, this hairline weight makes the largest text the lightest on the page - authority through restraint, not volume. The italic cut is used for poetic emphasis words inside the headline (e.g. 'the world').

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 40px.
- Card padding: 16px.
- Element gap: 16px.

Build these component patterns where relevant:

- Filled Pill Button (Primary Action): Primary call-to-action, used sparingly - contact, next-step, conversion.
- Outlined Pill Tag (Project Label): Labels on project cards and section eyebrows.
- Project Card: Portfolio grid item under the 'recent work' section.
- Hero Display Headline: Opening statement on the landing page.
- Announcement Bar: Thin strip below the hero promoting a publication or event.
- Sticky Top Navigation: Persistent brand and menu bar.
- Section Eyebrow with Dash: Small label introducing a content section, paired with a counter.
- Section Heading (Serif Display): Headings for content sections below the hero.
- Next/Previous Step Link: Pagination between sequential content steps.
- Underlined Emphasis Text: Inline emphasis within body and headline copy.
- Footer: Site footer (inferred from context frequency).

Do:

- Use #1a1c2c (Midnight Ink) for every filled button, heading, body paragraph, and hairline border - it is the system's only working color and the only legitimate action background.
- Set display headlines at 60-90px in FeatureDeckLight weight 100 with -0.02em tracking and line-height 1.07 - the hairline weight is the brand's signature, never substitute with 600+.
- Use 9999px radius for every button, tag, and nav element; use 20px for every card, image, and panel - these are the only two radii in the system.
- Apply 1px solid #1a1c2c underlines to emphasized words inside headlines and links - this is the editorial emphasis device, not bold or color.
- Keep the body of the page in Warm Parchment #fcfaf3 and reserve Soft Linen #ebe9e4 for the occasional elevated card or section band.
- Use 12px ZJSansDisplay weight 500 with +0.05em tracking (0.6px) for all eyebrows, tags, and small labels - this is the only uppercase-tracked text style.
- Maintain section gaps of 40px and element gaps of 16px; the page reads in 8px increments, never break the grid with arbitrary spacing.

Avoid:

- Never use box-shadows or drop-shadows - the system is flat by design; use 1px borders and surface tonal steps for separation instead.
- Never use a bold or 600+ weight for display headlines - weight 100 at 60-90px is the signature; a bold version would erase the brand voice.
- Never introduce a new accent color for buttons, links, or interactive elements - the action is always filled Midnight Ink on Warm Parchment.
- Never use pure white (#ffffff) as a background - the canvas is Warm Parchment #fcfaf3; pure white would break the printed-paper quality.
- Never add a gradient to UI components, buttons, or cards - the system is solid-fill only; color gradients are reserved for the single full-bleed hero image.
- Never use sharp corners (0-4px radius) on cards or buttons - the system is either 20px rounded or fully pill-shaped; no in-between.
- Never use decorative dividers, background patterns, or ornamental graphics below the hero - the body of the site is typographic and photographic only.

Source prompt cues:

Quick Color Reference:
- text: #1a1c2c (Midnight Ink)
- background: #fcfaf3 (Warm Parchment)
- card surface: #ebe9e4 (Soft Linen)
- border: #1a1c2c 1px
- accent: #fd9494 (Blush Coral - decorative only)
- primary action: #1a1c2c (filled action)

Example Component Prompts:

1. Hero Display Headline - 'Zeus Jones: risograph on warm cream'. Set a 90px FeatureDeckLight weight 100 headline at #1a1c2c, line-height 1.07, letter-spacing -1.8px, over a full-bleed colorful aurora background. Underline the words 'risograph' and 'warm'. End the headline with 'cream.' in serif italic. No max-width; pad 80px left.

2. Filled Pill Button - 'Interested? let's talk'. 9999px radius. Background #1a1c2c. Text #fcfaf3, ZJSansDisplay 16px weight 400, tracking -0.32px. Padding 16px vertical x 24px horizontal. No border, no shadow.

3. Project Card - four cards in a horizontal row, each with a 20px-radius image filling the top, a pill tag below (1px #1a1c2c border, radius 9999px, 12px ZJSansDisplay weight 500 +0.6px tracking, #1a1c2c text, padding 8px x 16px), then a 24px ZJSansDisplay weight 400 title, then an 18px body descriptor. Background Warm Parchment #fcfaf3; cards separated by 16px gap.

4. Section Heading + Eyebrow - eyebrow row: 'How we partner -' left-aligned, '1 of 7' right-aligned, ZJSansDisplay 16px weight 400 #1a1c2c, tracking -0.32px, 1px solid #1a1c2c bottom border across the row. Below, 24px gap, then a 48px FeatureDeckLight weight 100 heading at #1a1c2c, tracking -0.96px.

5. Announcement Bar - full-width strip, 1px solid #1a1c2c bottom border, 16px vertical padding. Left content: 8px filled dot in #fd9494, then ZJSansDisplay 16px weight 400 #1a1c2c text, ending with an underlined 'Learn more' link. Background #fcfaf3.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
