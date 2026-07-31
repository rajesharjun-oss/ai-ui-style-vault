# Pentagram

Source: [Refero Style](https://styles.refero.design/style/86b56f02-57da-48a1-a647-fda9bbdf2c97)
Reference site: [https://pentagram.com](https://pentagram.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:32:42.082Z
Refero modified: 2026-06-05T10:04:43.672Z
Theme: light
Category: Agency

## Style Summary

Explore Pentagram's light Agency design system: Paper White #ffffff, Ink #1a1a1a colors, Plain typography, and DESIGN.md for AI agents.

North star: Gallery wall of compressed restraint

## What To Borrow

- Paper White `#ffffff` for Page canvas, card surfaces, text on dark bands
- Ink `#1a1a1a` for Primary body text, heading text, hairline borders, link color - the near-black that carries 90% of all strokes
- True Black `#000000` for Solid surface fills for dark bands, inverted text backgrounds, inverted footer
- Graphite `#222222` for Elevated dark surface, input field fills on dark contexts
- Carbon `#333333` for Card border on light surfaces, subtle structural dividers
- Ash `#767676` for Muted body text, secondary metadata, less-prominent captions
- Fog `#8c8c8c` for Light borders, low-emphasis dividers, placeholder text
- Mist `#ededed` for Tinted light surface between pure white and true black bands
- Haze `#e3e4e5` for Subtle alt-row surface, hover wash, low-contrast card fill

- Plain `--font-plain` for All roles - display, headings, body, caption, nav, button. The single typeface carries the entire site. Weight contrast is limited (400 vs 500) so hierarchy comes from size and tracking, not boldness. The 52px display at -0.02em tracking is anti-display: it whispers instead of shouts. Line-heights under 1.1 on 32-52px create stacked, compressed blocks where headings read as solid slabs. Open features 'kern' and 'case' hint at a typeface with carefully spaced uppercase alternates - the 'case' feature likely gives access to stylistic capital forms.

## Avoid

- Don't add any color to navigation, buttons, or backgrounds. The interface is 100% achromatic - color only appears inside project thumbnails.
- Don't use border-radius above 8px on cards or 4px on buttons. Sharp corners read as editorial plates; rounding undermines the gallery-catalog feel.
- Don't introduce filled buttons, outlined buttons, or ghost buttons. There is no button component - every affordance is a text link, an image, or a dot.
- Don't use weight 600+ or italic. The typeface's weight range stops at 500; anything heavier breaks the compressed-restraint language.
- Don't add icons inside body content. The only icon on the entire site is the search affordance in the nav.
- Don't use background colors on text or dividers for emphasis. Emphasis comes from size, tracking, and the Paper White / Ink contrast pair - never from color fill or tint.
- Don't use shadows, gradients, or glow effects. Elevation is communicated purely through band alternation (white black white), not through drop shadows.

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
