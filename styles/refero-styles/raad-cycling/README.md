# Raad Cycling

Source: [Refero Style](https://styles.refero.design/style/a59e7f31-1fca-46c1-a6b0-8d1294b33a7c)
Reference site: [https://www.raad.cc](https://www.raad.cc)
Captured: 2026-07-31
Refero published: 2026-04-30T03:01:38.694Z
Refero modified: 2026-06-05T11:19:15.779Z
Theme: light
Category: E-commerce

## Style Summary

Explore Raad Cycling's light E-commerce design system: Ink Black #000000, Ivory White #ffffff colors, Arial, Raad Display (custom geometric sans-serif)...

North star: Ink and ivory gallery runway

## What To Borrow

- Ink Black `#000000` for Primary canvas for dark sections, product photography backgrounds, all body text on light surfaces, divider lines, and the dominant border color throughout the system
- Ivory White `#ffffff` for Primary canvas for light sections, text on dark backgrounds, ghost-button fills and borders, the base surface against which all product photography is staged
- Charcoal Edge `#181818` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Graphite `#333333` for Secondary border tone for subtle UI structure, divider lines between content blocks, and depth separation on otherwise flat surfaces
- Stone Gray `#666666` for Muted helper text, secondary metadata, and the only step down in the type hierarchy where pure black would feel too heavy - the softest voice in the system

- Arial `--font-arial` for Fallback system font for micro-text and edge-case rendering - appears so rarely it functions as a safety net rather than a design choice
- Raad Display (custom geometric sans-serif) `--font-raad-display-custom-geometric-sans-serif` for The sole brand typeface used for everything from uppercase product category labels to the massive hero display 'LIQUID LOVE'. The custom face is a clean geometric sans with tall x-height and wide letterforms that hold up at extreme scale. It is used at weight 400 only - no bold, no light variations. The 0.1em positive letter-spacing is applied uniformly across all sizes, creating a slightly aired-out feel even at body text. This single-font, single-weight discipline is the most opinionated choice in the system: Raad removes the typographic hierarchy tools (weight contrast, family contrast) that most sites rely on, forcing scale and letter-spacing to do all the structural work instead.
- wfont_8b8bfe_cd7287b5071a4785a78bba57128a74e2 `--font-wfont8b8bfecd7287b5071a4785a78bba57128a74e2` for wfont_8b8bfe_cd7287b5071a4785a78bba57128a74e2 - detected in extracted data but not described by AI

## Avoid

- Never introduce a chromatic color, gradient, or accent - the system is 0% colorful by design, and any hue would break the gallery aesthetic
- Never use a filled or solid-background button - ghost outlines are the only button pattern permitted
- Never apply box-shadow, drop-shadow, or blur to any element - depth comes from black/white alternation, not elevation
- Never use border-radius on images or cards - the only rounded element is the pill button at 100px
- Never use bold or semibold weights - the custom font exists at weight 400 only, and introducing weight contrast would destroy the system
- Never set body text tighter than 1.4 line-height - the generous leading is what keeps small white-on-black text legible
- Never add decorative UI elements (badges, tags, pills, chips, tooltips) - the system is intentionally stripped to typography, photography, and hairline borders

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
