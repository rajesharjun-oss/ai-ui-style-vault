# Applied Labs

Source: [Refero Style](https://styles.refero.design/style/e68d2972-4344-4954-b00c-56fdf97d9de4) 
Reference site: [https://appliedlabs.ai](https://appliedlabs.ai) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:19:03.191Z 
Refero modified: 2026-06-03T19:12:30.913Z 
Theme: light 
Category: AI

## Style Summary

Explore Applied Labs's light AI design system: White #ffffff, Cream #f7f7f4 colors, Geist typography, and DESIGN.md for AI agents.

North star: Sunlit cream paper with cobalt punctuation and floating conversation cards

## What To Borrow

- White `#ffffff` for Page canvas, base card surface, nav background
- Cream `#f7f7f4` for Warm off-white section background, soft card fill - the secondary surface layer that gives the page its paper-like warmth
- Fog `#f5f5f5` for Elevated card surfaces and subtle section bands
- Ash `#e4e4e7` for Hairline borders, dividers, input underlines - the structural skeleton of the layout
- Stone `#8c8c8c` for Tertiary text, placeholder copy, disabled states
- Steel `#737373` for Secondary body text, helper copy, muted descriptions
- Graphite `#666666` for Secondary body text on cream surfaces
- Charcoal `#4d4d4d` for Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color
- Warm Gray `#7d7c78` for SVG icon fills, subtle warm-toned decorative elements
- Espresso `#26251e` for Primary text on cream surfaces, dark card accents, outlined action borders - the warm alternative to pure black
- Midnight `#09090b` for Primary body and heading text on white, the dominant ink color
- Pure Black `#000000` for Primary headings, body text, and icon fills on light surfaces. Do not promote it to the primary CTA color
- Deep Ink `#111111` for Footer and nav text, dark surface accents
- Slate Blue `#5c7aa1` for Muted blue-gray for section backgrounds, subdued text accents, and image overlay washes - adds cool depth without competing with the cobalt accent
- Warm Sand `#b39987` for Warm tan card surfaces, trust/social-proof section backgrounds - a near-gray with just enough warmth to echo the photography
- Cobalt Spark `#0051ff` for Violet text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Emerald `#00cb39` for Green text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color

- Geist `--font-geist` for Sole typeface - used for everything from display headlines down to 10px micro-copy. Geist's geometric neutrality and tall x-height make it read as editorial without being cold.

## Avoid

- Do not fill buttons with Cobalt Spark (#0051ff) - that color is reserved for inline text accents and links, never for filled button backgrounds
- Do not use shadows on cards unless they represent a floating overlay or modal; the system relies on borders and surface color shifts, not elevation
- Do not use illustrations, 3D renders, or icon-heavy compositions as primary visuals - real warm-toned photography carries the brand
- Do not use a second typeface; Geist handles everything from 10px caption to 48px display
- Do not use the warm tan (#b39987) or slate blue (#5c7aa1) for more than 10-15% of the visible surface - they are accent surfaces, not the canvas
- Do not set headline weight above 500; weight 300 is the signature, weight 500 is for emphasis, never 600-700
- Do not use border-radius above 24px on standard cards; the 8px default is the system's defining softness

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
