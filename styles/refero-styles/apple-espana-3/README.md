# Apple (Espana)

Source: [Refero Style](https://styles.refero.design/style/96eae189-95ad-4a38-83d1-840497e5daf3) 
Reference site: [https://www.apple.com/apple-watch-series-11](https://www.apple.com/apple-watch-series-11) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:17:24.680Z 
Refero modified: 2026-06-03T19:26:49.392Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore Apple (Espana)'s light E-commerce design system: Apple Blue #0071e3, Link Blue #0066cc colors, SF Pro Display, SF Pro Text typography, and DESIGN.md...

North star: cinematic gallery on poured concrete - every product its own still life, every headline a wall label

## What To Borrow

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

- SF Pro Display `--font-sf-pro-display` for Headlines and display. The 48-64px range carries section titles like 'Lo principal.' and 'Mas de cerca.' with aggressively tight letter-spacing (-0.015em to -0.003em) that lets words lock into a single visual block. Weight 600 is the workhorse; 700 appears on the most emphatic display sizes. 260px is the extreme hero-numeral scale. Substitute: Inter, system-ui.
- SF Pro Text `--font-sf-pro-text` for Body, nav, buttons, legal copy, and supporting UI. 17px is the canonical body size; 14px carries secondary descriptions and footnote text; 12px is reserved for micro-labels and legal fine print. Weight 400 for body, 600 for nav items, button labels, and emphasis. Tight tracking throughout (-0.022em at 12px down to -0.003em at 44px) keeps even long paragraphs visually dense. Substitute: Inter, -apple-system.

## Avoid

- Never use #0066cc as a button fill - it is a link/underline color only; buttons use #0071e3
- Never apply a drop shadow to a card or button - tonal contrast against #f5f5f7 is the only depth signal
- Never set body type below 14px or above 21px - the 17px body / 14px secondary split is fixed
- Never use #000000 for body text - use #1d1d1f; reserve pure black for hero overlays and icon fills on white
- Never introduce a chromatic accent outside the activity-ring palette (green/orange/violet/teal) - these are decorative only, never CTA
- Never end a headline without a period or use a question mark - the system is declarative, not interrogative
- Never use a border-radius below 10px or above 28px for any container - the 28px radius is the lower bound for everything

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
