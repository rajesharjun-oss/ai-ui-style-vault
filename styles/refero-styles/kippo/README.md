# Kippo

Source: [Refero Style](https://styles.refero.design/style/917048a3-53b3-44e6-ab33-faefc4dcc9df)
Reference site: [https://kippo.com](https://kippo.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:40:54.453Z
Refero modified: 2026-06-05T10:34:40.210Z
Theme: dark
Category: Other

## Style Summary

Explore Kippo's dark Other design system: Kippo Pink #ee1f66, Void Black #000000 colors, Source Code Pro typography, and DESIGN.md for AI agents.

North star: Pixel arcade boot screen in a black void. Monospace glyphs traced in white neon against a pure black void, with a single hot-pink power-up color that should feel rare and electric when it appears.

## What To Borrow

- Kippo Pink `#ee1f66` for Primary action background, accent headings, active badges - the only chromatic voice in the system, rationed to feel like a power-up rather than a brand wash
- Void Black `#000000` for Page canvas, card backgrounds, image fills - the infinite dark that everything else floats on
- Carbon `#29292a` for Elevated card surfaces and secondary panels - barely-distinguishable dark gray for cards that need to step forward from the black canvas
- Ash `#333333` for Subtle borders and dividers where white is too loud - a near-black separator for nested or secondary content
- Ghost White `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces.
- Sunset Gradient `#ffc400` for Gradient start stop - used only on the warm-to-cool decorative band behind the phone mockup and small accent elements
- Terminal Cyan `#33beff` for Gradient start for cool accents - used sparingly in decorative gradient bands

- Source Code Pro `--font-source-code-pro` for Sole typeface - used for every text element from nav links to body copy to display headlines. Monospace at 42px/weight 700 with 0.3-0.5em tracking in all-caps creates a retro arcade marquee feel; at 16px/weight 400 it reads as clean monospace body. The slashed-zero feature is enabled, reinforcing the terminal/CRT aesthetic.

## Avoid

- Don't introduce a second typeface (no Inter, no Helvetica, no sans-serif fallback for body). Monospace-only is the identity.
- Don't fill cards with color, gradient, or image. Cards are transparent panels - the border is the card.
- Don't use drop shadows for elevation. Depth comes from overlapping layers and outline contrast, never from blur.
- Don't dilute #ee1f66 by using it for body text, borders on non-action elements, or large background areas. It must remain rare.
- Don't use border-radius larger than 15px on rectangular surfaces, and never use fully-rounded pill shapes on buttons (10px max).
- Don't mix light and dark themes - this is a dark-only system. No white-background sections, no theme toggle.
- Don't use red, green, or yellow for semantic states (success/error/warning) - those colors are decorative only in this system, and the dark canvas + white text + single pink accent is the entire signal vocabulary.

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
