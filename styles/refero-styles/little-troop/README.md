# Little Troop

Source: [Refero Style](https://styles.refero.design/style/bd62b51f-e1be-4e4f-b3d9-e9b91f817625)
Reference site: [https://littletroop.com](https://littletroop.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:51:24.395Z
Refero modified: 2026-06-05T10:48:45.529Z
Theme: light
Category: Agency

## Style Summary

Explore Little Troop's light Agency design system: Pure Black #000000, Pure White #ffffff colors, Arial Narrow, Times Now typography, and DESIGN.md for AI...

North star: Monochrome gallery with chromatic artworks. A black pearl floating in white void.

## What To Borrow

- Pure Black `#000000` for All text, all borders, the nav mark, section dividers, filter indicators. The structural ink of the entire system - every line, frame, and glyph is black on white
- Pure White `#ffffff` for Page canvas and inverse text. The only surface; cards do not introduce a separate fill - they borrow the page and let imagery do the work

- Arial Narrow `--font-arial-narrow` for The functional voice of the entire interface - navigation, body, metadata, project captions, filter labels, footer copy. Narrow letterforms in a generous white field create a typesetter's galley feel; everything reads as a running label rather than as UI chrome.
- Times Now `--font-times-now` for The single display voice, reserved for the hero headline curved around the orb. Weight 250 is anti-convention - most studios reach for 600-800 bold serifs. This whisper-weight, paired with a sculptural -0.066em tracking and 0.79 line-height, makes the text feel like a ribbon on the surface rather than a title above it. When the system needs authority, it gets it through restraint, not volume.

## Avoid

- Do not introduce a third color, a shadow, a gradient, or any surface tint. The two-color discipline is the brand.
- Do not use a bold display weight for headlines. Times Now weight 250 is the only display voice; if you need more presence, increase size, never weight.
- Do not use rectangular corners anywhere. Even small chips, tags, and buttons get 50px radius.
- Do not add borders, outlines, or focus rings that aren't pure 1px black. No colored states, no tinted hovers.
- Do not break the white canvas with a panel, sidebar, or container surface. The page is the only surface.
- Do not center-align body or metadata text. The footer credit and project captions are left- or right-aligned to specific edges.
- Do not use a sans-serif system font for display. The serif at ultra-light weight is what separates this system from every other minimalist agency portfolio.

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
