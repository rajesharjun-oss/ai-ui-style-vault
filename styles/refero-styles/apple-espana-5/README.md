# Apple (Espana)

Source: [Refero Style](https://styles.refero.design/style/a4f123f2-cd4b-4d26-998f-a3d3ee158024)
Reference site: [https://apple.com](https://apple.com)
Captured: 2026-07-30
Refero published: 2026-03-06T10:42:58.000Z
Refero modified: 2026-07-03T10:08:37.091Z
Theme: light
Category: E-commerce

## Style Summary

Explore Apple (Espana)'s light E-commerce design system: Fog White #f5f5f7, Pure White #ffffff colors, SF Pro Display, SF Pro Text typography, and DESIGN.md...

North star: Museum gallery in soft daylight - the gallery is a single, immersive, weightless white room where each product is spotlit against a faintly tinted wall.

## What To Borrow

- Fog White `#f5f5f7` for Dominant page canvas, section backgrounds, footer
- Pure White `#ffffff` for Nav background, button text, elevated surface
- Obsidian `#1d1d1f` for Primary headline and body text - the only true dark for editorial content
- Carbon `#000000` for Nav glyphs, link underlines, dark text on light surfaces
- Pewter `#707070` for Secondary body text, footer copy, muted helper text
- Slate `#505050` for Tertiary body text and subdued link states
- Graphite `#474747` for Nav and link text at rest - sits between body text and pure black
- Iron `#333333` for Nav icons (fill) and button text - the dominant dark accent in chrome
- Silver `#858585` for Icon strokes, tertiary glyphs, muted UI controls
- Pale Mist `#d6d6d6` for Hairline dividers, subtle borders between content blocks
- Ash Veil `#e2e2e5` for Button backgrounds for secondary filled actions (dark mode variant)
- Iris Blue `#0071e3` for Filled primary action buttons - the sole chromatic CTA, signals the only commitment the page asks of you
- Sapphire `#0066cc` for Outlined action buttons, body and link text - darker blue for outlined variants and inline links
- Sky Signal `#2997ff` for Outlined action buttons on dark sections, secondary CTAs - lighter blue for ghost buttons against dark hero bands
- Cornflower `#509be7` for Hover state for inline links, decorative link accent
- Ice Wash `#aad0f6` for Gradient section background wash - the pale blue tint behind iPad Air / MacBook Air hero bands

- SF Pro Display `--font-sf-pro-display` for Product headlines, large editorial display text. Used at 56px/600 for hero titles like 'MacBook Air' and 40px/600 for section subheads. The tighter 1.07 line height at 56px is signature - it lets the headline sit as a single visual block without breathing room between lines.
- SF Pro Text `--font-sf-pro-text` for Navigation, body copy, buttons, footer, subheads below display. The 17px/400/1.47 body setting appears 221 times - this is the workhorse. The 12px/400/1.33 setting handles everything in the footer and micro-copy. 44px/400/1.00 is the nav logo wordmark.

## Avoid

- Don't add box-shadows to buttons, cards, or sections - elevation comes from color contrast, not shadows.
- Don't use the brand blue (#0071e3) for anything other than filled primary action buttons; links and outlines use #0066cc.
- Don't left-align product headlines; the system is always centered.
- Don't use border-radius values below 980px on buttons - no square buttons, no 4px or 8px pill variants.
- Don't place horizontal rules or border lines between sections; use background color shifts instead.
- Don't use SF Pro Display at sizes below 21px; that family is reserved for headlines and large body. Use SF Pro Text for everything under 21px.
- Don't introduce secondary accent colors, gradients, or decorative backgrounds within the product hero areas - the product render is the only visual interest.

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
