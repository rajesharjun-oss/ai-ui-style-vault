# INK

Source: [Refero Style](https://styles.refero.design/style/6262b0bb-ea6f-481b-b706-65df29507b6c)
Reference site: [https://weareink.co.uk](https://weareink.co.uk)
Captured: 2026-07-31
Refero published: 2026-03-07T09:18:39.000Z
Refero modified: 2026-06-05T07:58:00.985Z
Theme: light
Category: Agency

## Style Summary

Explore INK's light Agency design system: Ink Carbon #2e2a2b, Paper White #ffffff colors, Good Sans typography, and DESIGN.md for AI agents.

North star: Editorial spread on warm paper. A single humanist voice, monochrome with a whisper of taupe, interrupted only by full-bleed photography and a slim band of warm orange.

## What To Borrow

- Ink Carbon `#2e2a2b` for Primary text, logo mark, dark surface inversions, footer text on cream - a near-black with a barely-warm undertone that keeps the page from feeling clinical
- Paper White `#ffffff` for Page canvas and nav surface - the warm-white background that everything floats on
- Whisper Taupe `#afa697` for Supporting neutral for secondary UI, dividers, and muted labels.
- Bone Cream `#e6dcd4` for Alternate panel background and footer band - a warm cream that signals a quieter section without leaving the monochrome family
- Lampblack `#212121` for Deep surface for inversions and image overlays - slightly cooler than Ink Carbon, used where absolute darkness is needed without color cast
- Signal Orange `#fe5431` for Decorative illustration accent - appears inside graphic bands and artwork, never as a UI control fill
- Amber Pulse `#ff8000` for Decorative illustration accent - companion to Signal Orange inside warm gradient bands and visual punctuation

- Good Sans `--font-good-sans` for Single voice across the entire interface - body, nav, buttons, headings, and display all share weight 400. The absence of bold is the signature: hierarchy comes from size and color, not weight.

## Avoid

- Don't add drop-shadows to any element - depth comes from fill, not blur
- Don't use Signal Orange #fe5431 or Amber Pulse #ff8000 as button backgrounds or link colors - they are decoration only
- Don't introduce a max-width container on text blocks - the left-edge 64px padding is the only gutter
- Don't use a second typeface, even for captions - Good Sans 400 covers the entire voice
- Don't add borders, dividers, or rules between sections - let whitespace do the work
- Don't crop project images with rounded corners or contain them in cards
- Don't bold or italicize any text for emphasis - use the taupe-to-carbon color shift instead

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
