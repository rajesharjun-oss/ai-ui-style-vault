# Arc

Source: [Refero Style](https://styles.refero.design/style/acfb6fa1-3aed-4e64-8522-7f332a796de8) 
Reference site: [https://arcboats.com](https://arcboats.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:41:30.025Z 
Refero modified: 2026-06-03T18:21:23.128Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore Arc's light E-commerce design system: Bone #e5e7eb, Charcoal #0a0a0a colors, Soehne typography, and DESIGN.md for AI agents.

North star: industrial white gallery above midnight water

## What To Borrow

- Bone `#e5e7eb` for Page canvas, card surfaces, hairline dividers between sections, ghost-button borders - the lightest structural gray carries borders, surface, and the dominant background in a near-white mode
- Charcoal `#0a0a0a` for Primary body and heading text, nav links, footer text, filled button text - near-black for maximum legibility without the harshness of pure black
- Paper `#ffffff` for Card surfaces, filled button backgrounds, image overlays, reverse text on dark sections - the brightest structural white
- Obsidian `#000000` for Headings on light canvas where maximum contrast is required, nav background accents - used sparingly only where absolute black is needed
- Deep Current `#031e25` for Dark feature section backgrounds (alternating bands), large image containers - the navy-black that recedes like deep ocean water
- Slate Depth `#1d1d1e` for Secondary dark section background, elevated panels over Deep Current - one step lighter to layer depth within dark bands

- Soehne `--font-soehne` for All interface type: weight 300 reserved for display headings (48-140px) to create a quiet engineering voice, 400 for body and subheadings, 500 for nav and meta, 600 for button labels. Soehne's geometric neutrality with the extreme -0.043em tracking on display sizes is the signature - it makes headlines feel architectural rather than editorial. Substitute: Inter (closest free analog with matching weights and tracking) or Untitled Sans.

## Avoid

- Never introduce a chromatic accent color - the system is deliberately monochromatic plus dark teal-navy
- Never use weight 700 or higher - the heaviest weight in the system is 600, and display text stays at 300
- Never add drop shadows, glows, or blur effects to elements beyond the single detected hero shadow
- Never use a border-radius between 6px and 31px - controls stay at 5px, images at 32px, nothing in between
- Never place text directly on a photograph without a darkening overlay or contained card surface
- Never use centered body copy longer than two lines; long-form content goes left-aligned in contained columns
- Never use illustrations, icons-as-decoration, or 3D renders - photography and type are the only visual vocabulary
- Never set body text above 18px or below 14px - the 14-18px range is the readable band

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
