# Mews

Source: [Refero Style](https://styles.refero.design/style/6b2777fd-7021-4a96-add3-ec4a32374214)
Reference site: [https://www.mews.com/en](https://www.mews.com/en)
Captured: 2026-07-31
Refero published: 2026-04-30T00:14:32.679Z
Refero modified: 2026-06-05T07:49:51.469Z
Theme: light
Category: SaaS

## Style Summary

Explore Mews's light SaaS design system: Canvas White #ffffff, Warm Cream #fffcf6 colors, Soehne typography, and DESIGN.md for AI agents.

North star: Hospitality command center at pink dawn. A white-walled, sunlit workspace where bold black type, warm cream cards, and a single candy-pink action button define every screen - playful confidence over enterprise restraint.

## What To Borrow

- Canvas White `#ffffff` for Primary page background, top of surface stack
- Warm Cream `#fffcf6` for Card and elevated surface backgrounds, gentle warmth against pure white
- Ink Black `#000000` for Primary text, icons, borders, and dark hero panels - the dominant structural color
- Charcoal `#333333` for Secondary text and softer borders where pure black would feel too heavy
- Deep Panel `#161616` for Dark feature cards, inverse surface for hero blocks, and high-contrast panels
- Fog Gray `#8c8c8c` for Muted helper text, disabled button fills, and tertiary borders
- Mist Gray `#cccccc` for Hairline dividers, nav separators, subtle structural borders
- Lilac Mist `#c4c9dd` for Cool-toned decorative borders, illustration fills, and subtle chrome highlights
- Bubblegum `#ff83da` for Primary brand accent - pill-shaped CTAs, announcement bar background, active highlights; vivid pink against white is the visual signature
- Cotton Pink `#ffc5ee` for Softer pink surface for secondary buttons and pastel card variants
- Blush Mist `#f7e1f7` for Lightest pink wash for category tile backgrounds and quiet brand surfaces
- Ice Blue `#d2f4ff` for Cool supporting accent for product UI screenshots, informational tiles, and category surface variation
- Voltage Lime `#e8ff5b` for High-energy accent for spotlight highlights, image overlays, and surprise moments - used sparingly for visual punctuation

- Soehne `--font-soehne` for Single typeface across all UI. Body and UI copy at 400-500, navigation and labels at 500-600, subheads at 700, and display headlines at 900 - the extreme weight contrast between 400 body and 900 display is the signature typographic move. Aggressive negative tracking (-0.025em at display sizes) tightens headlines into bold block-like forms that feel architectural rather than airy.

## Avoid

- Don't use the pink CTA fill for anything other than the primary conversion - ghost, outline, and text-link alternatives exist for secondary actions.
- Don't set headlines in weights below 700; the 900/400 contrast between display and body is the brand's voice - flattening to 600 kills the energy.
- Don't add drop shadows to cards; the design relies on flat warm-cream surfaces and hairline borders for separation - shadows would feel corporate and wrong.
- Don't use the lime #e8ff5b or ice blue #d2f4ff on body text or large surfaces; they're accent and supporting-tile colors only.
- Don't introduce new rounded radii (12px, 16px, 24px) - stick to the 4px / 8px / 9999px scale or the visual rhythm collapses.
- Don't use cool grays (#94a3b8, #64748b) for text or borders; the system runs warm with #333333, #8c8c8c, and #cccccc.
- Don't add decorative gradients; the design is flat, photographic, or product-screenshot-driven - gradients would clash with the editorial flatness.

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
