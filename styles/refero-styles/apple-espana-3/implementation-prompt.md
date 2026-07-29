# AI Implementation Prompt

Build a Apple (Espana)-inspired interface using this source-derived style bundle.

Reference site: https://www.apple.com/apple-watch-series-11
Theme: light
Category: E-commerce
North star: cinematic gallery on poured concrete - every product its own still life, every headline a wall label

Use these palette anchors:

- Apple Blue `#0071e3` for Primary CTA fill - the single saturated button on the page (Comprar, Learn more). Vivid mid-blue that reads as a switch-on moment against matte neutrals
- Link Blue `#0066cc` for Inline text links, footnote references, and underlined link borders. Slightly deeper and cooler than the CTA blue so links and buttons read as distinct actions
- Signal Green `#03aa49` for Accent stroke for positive health/sleep metric visualizations and decorative data highlights on product UI
- Ember Orange `#ed6300` for Orange outline accent for tags, dividers, and focused UI edges
- Iris Violet `#8668ff` for Tertiary accent for multicolor data rings, decorative product UI, and illustration strokes
- Deep Teal `#00a1b3` for Quaternary accent completing the Apple Watch activity ring palette
- Space Black `#1d1d1f` for Primary text, heading fills, icon strokes, and card borders. Apple's near-black - softer than #000, reads warm against white
- Sterling `#707070` for Secondary/muted text, nav borders, list dividers, and subdued UI labels
- Graphite `#474747` for Nav border-bottom, link muted state, and mid-contrast UI text
- Slate `#333336` for Nav-specific dark text and borders in the top utility bar
- Smoke `#777779` for Disabled or de-emphasized button/link background fill
- Pebble `#d6d6d6` for Hairline borders, inactive dividers, and subdued list separators
- Concrete `#e2e2e5` for Light surface tone for secondary buttons and list-item fills sitting on white
- Fog `#f5f5f7` for Page canvas and section background - the dominant pale-gray that separates content bands from pure white card surfaces
- Pure White `#ffffff` for Card surfaces, button text on dark fills, nav backgrounds, and badge interiors
- Absolute `#000000` for True black for hero image overlays, icon fills, and high-contrast heading strokes

Use these typography anchors:

- SF Pro Display `--font-sf-pro-display` for Headlines and display. The 48-64px range carries section titles like 'Lo principal.' and 'Mas de cerca.' with aggressively tight letter-spacing (-0.015em to -0.003em) that lets words lock into a single visual block. Weight 600 is the workhorse; 700 appears on the most emphatic display sizes. 260px is the extreme hero-numeral scale. Substitute: Inter, system-ui.
- SF Pro Text `--font-sf-pro-text` for Body, nav, buttons, legal copy, and supporting UI. 17px is the canonical body size; 14px carries secondary descriptions and footnote text; 12px is reserved for micro-labels and legal fine print. Weight 400 for body, 600 for nav items, button labels, and emphasis. Tight tracking throughout (-0.022em at 12px down to -0.003em at 44px) keeps even long paragraphs visually dense. Substitute: Inter, -apple-system.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 80px.
- Card padding: 28px.
- Element gap: 10px.

Build these component patterns where relevant:

- Pill CTA Button (Primary): The single saturated blue action - 'Comprar', 'Buy', primary download.
- Pricing Chip: Adjacent price display next to a primary CTA - 'Desde 449 '.
- Outline Ghost Link: Secondary action - 'Learn more', 'Compare', section deep-links.
- Eyebrow Label: Category tag above a hero headline - 'WATCH SERIES 11'.
- Section Headline: Opening line of each content band - 'Lo principal.', 'Mas de cerca.'.
- Feature Accordion Row: Expandable feature list item in product deep-dive sections.
- Product Feature Card: White surface card pairing a product image with a short feature description.
- Global Nav Bar: Sticky top utility bar with product category links.
- Promo Banner: Thin announcement strip above the nav - education pricing, trade-in.
- Hero Section: Full-bleed cinematic opener with overlaid editorial text.
- Split Feature Block: Two-column section: short text on one side, product image on the other.
- List Separator: Horizontal divider within stacked content rows.

Do:

- Set every section background to #f5f5f7 and every card surface to #ffffff - this is the only elevation system in use
- End every section headline with a period: 'Lo principal.', 'Mas de cerca.' - the full stop is a signature editorial move
- Use SF Pro Display at 48-56px weight 600 for section openers, with letter-spacing -0.005em
- Use the 28px radius for every card, accordion pill, and chip; reserve 980px only for true pill-shaped buttons
- Pair every CTA blue (#0071e3) with a white pricing chip (#333336 60%) when the price is part of the call to action
- Place the eyebrow label as 'PRODUCT ICON + ALL-CAPS 12px/600' directly above the hero headline at 3px gap
- Keep body paragraphs to a single 17px sentence per line - the system edits for visual silence, not information density

Avoid:

- Never use #0066cc as a button fill - it is a link/underline color only; buttons use #0071e3
- Never apply a drop shadow to a card or button - tonal contrast against #f5f5f7 is the only depth signal
- Never set body type below 14px or above 21px - the 17px body / 14px secondary split is fixed
- Never use #000000 for body text - use #1d1d1f; reserve pure black for hero overlays and icon fills on white
- Never introduce a chromatic accent outside the activity-ring palette (green/orange/violet/teal) - these are decorative only, never CTA
- Never end a headline without a period or use a question mark - the system is declarative, not interrogative
- Never use a border-radius below 10px or above 28px for any container - the 28px radius is the lower bound for everything

Source prompt cues:

**Quick Color Reference**
- text: #1d1d1f
- background: #f5f5f7
- card surface: #ffffff
- border: #d6d6d6
- link: #0066cc
- primary action: #0071e3 (filled action)

**3-5 Example Component Prompts**

1. Create a Primary Action Button: #0071e3 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Section opener**: Background #f5f5f7, max-width 1440px centered, 80px top/bottom padding. Headline left-aligned in SF Pro Display 48px/600 #1d1d1f, letter-spacing -0.005em, ending with a period. No body text, no button - the headline alone opens the section.

3. **Split feature block**: Background #f5f5f7, two-column at max-width 1440px. Left column (40%): headline at 40px SF Pro Display/600 #1d1d1f, followed by 17px SF Pro Text/400 #1d1d1f body paragraph with line-height 1.47. Right column (60%): product render on pure white with 28px radius, no border, no shadow.

4. **Feature accordion list**: Vertical stack of 28px-radius pills on #f5f5f7 canvas. Each row: 8px vertical padding, 16px horizontal padding, background #f5f5f7, 24px circular icon on the left in #1d1d1f, label in SF Pro Text 14px/400 #1d1d1f. 6px gap between rows. Active row: background #1d1d1f, text and icon flip to #ffffff.

5. **Outlined/ghost link row**: Single line of 17px SF Pro Text/400 #0066cc text with trailing glyph, 8px gap to the right of preceding content. No background, no border, no padding. On hover: underline appears via 1px #0066cc border-bottom.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
