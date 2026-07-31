# Nathan Riley

Source: [Refero Style](https://styles.refero.design/style/1c516bc6-278b-4cf6-bfe8-c5a39118e730)
Reference site: [https://www.nrly.co](https://www.nrly.co)
Captured: 2026-07-31
Refero published: 2026-04-30T02:13:38.914Z
Refero modified: 2026-06-05T09:00:03.849Z
Theme: light
Category: Design

## Style Summary

Explore Nathan Riley's light Design design system: Pure Black #000000, Paper White #ffffff colors, font1, Custom Display Serif typography, and DESIGN.md for...

North star: Gallery wall in a black void. A monochrome portfolio where the grid of atmospheric renders is the only color, and a single oversized serif name card anchors the center like a magazine cover floating over the work.

## What To Borrow

- Pure Black `#000000` for Text, image grid gutter borders, hairline dividers, nav chip outlines - the structural ink that defines the grid structure and typography
- Paper White `#ffffff` for Page canvas, nav chip backgrounds, card surface - the gallery wall behind everything
- Warm Charcoal `#393939` for Central name card surface, secondary text, soft borders - the mid-tone that makes the pale-rose card read as a distinct layer without breaking the monochrome
- Blush Card `#e8c4c0` for Background of the central name card - the only chromatic accent, a dusty rose that warms the otherwise pure black-and-white system

- font1 `--font-font1` for font1 - detected in extracted data but not described by AI
- Custom Display Serif `--font-custom-display-serif` for Hero name display and small print. The 238px size with line-height 0.80 and -0.04em tracking creates a tightly cropped masthead that feels printed, not rendered. Weight 300 at display size is the signature - it whispers rather than shouts, giving the name editorial weight through restraint rather than boldness. The italic treatment in the screenshot adds a calligraphic warmth that contrasts the rigid grid around it.
- Custom Body Serif `--font-custom-body-serif` for Body copy, bio description, nav chip text, and link labels. Tight line-height 1.10 at small sizes creates a dense, catalog-like feel. The -0.025em tracking tightens the letterforms for compact, refined small text that reads as label or caption rather than prose.
- font2 `--font-font2` for font2 - detected in extracted data but not described by AI
- ui-sans-serif `--font-ui-sans-serif` for ui-sans-serif - detected in extracted data but not described by AI

## Avoid

- Do not add any new color - no blues, greens, or warm tones beyond the single blush card background
- Do not use border-radius on cards, images, or content containers - only pill nav chips get radius
- Do not apply shadows or elevation effects to any component - the system is flat, relying on color contrast and grid structure for depth
- Do not add gradients of any kind - the palette is solid only
- Do not use sans-serif for headlines or display text - the custom serif at extreme sizes is the signature element
- Do not constrain the image grid with a max-width container - the grid must be full-bleed edge-to-edge
- Do not add header navigation, footers, or sidebar chrome - the floating name card and bottom pill row are the entire navigation system

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
