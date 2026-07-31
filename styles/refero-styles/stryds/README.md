# Stryds

Source: [Refero Style](https://styles.refero.design/style/6b4e6620-5c06-4dc1-931b-82265116f6f2)
Reference site: [https://stryds.com](https://stryds.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:21:27.601Z
Refero modified: 2026-06-05T07:39:05.657Z
Theme: dark
Category: Other

## Style Summary

Explore Stryds's dark Other design system: Electric Lime #a6ff00, Deep Violet #040126 colors, SF Pro Display, Arial typography, and DESIGN.md for AI agents.

North star: Aurora ringed midnight void

## What To Borrow

- Electric Lime `#a6ff00` for Green action color for filled buttons, selected navigation states, and focused conversion moments.
- Deep Violet `#040126` for Outlined action borders, subtle decorative borders - a near-black indigo that adds tonal depth to dark borders without breaking the monochrome canvas
- Obsidian `#101010` for Page canvas, outermost background, shadow tokens - the base void that every surface floats on
- Carbon `#171717` for Card surfaces, elevated content panels - the only step above Obsidian in the surface stack
- Slate `#333333` for Hairline borders, card borders, subtle dividers - the structural border color, used more than any other in the system
- Steel `#3d3d3d` for Strokes, secondary card borders - a half-step lighter than Slate for layering borders on borders
- Fog `#6f6f6f` for Dark borders and separators for elevated surfaces and inverted UI.
- Paper `#fdfdfd` for Primary text, heading borders, illustration highlights - the only text color that reads as active
- Void `#000000` for SVG fills, spectrum ring backing - pure black for graphic elements where absolute darkness is needed

- SF Pro Display `--font-sf-pro-display` for Display and heading typography - the choice of SF Pro Display signals a premium, iOS-adjacent system voice. Weights 500-600 (never 700+) keep headings from feeling heavy; the brand's authority comes from size, not weight. Display sizes escalate to 184px, creating poster-scale type that dominates every section. Line-height tightens to 0.95 at the largest sizes, making individual letters feel monumental and architectural.
- Arial `--font-arial` for Body, links, card text, button labels - deliberately a system fallback so it stays invisible. While SF Pro Display headlines shout at 184px, Arial whispers at 14px in the background. This split (premium display + neutral body) is a deliberate hierarchy choice: the display type does all the emotional work, the body text just delivers information.

## Avoid

- Do not use box-shadows for elevation - Stryds is flat against the void, separated by borders not depth
- Do not introduce additional accent colors beyond Electric Lime; the monochrome discipline is what makes the lime feel urgent
- Do not set body text below 14px or use font-weight below 400; the brand speaks with confidence, not subtlety
- Do not use sharp corners or radii under 16px; every element is either pill-shaped (100px) or softly rounded (40px)
- Do not center content in narrow columns or constrain to a max-width under 1000px; let display type and the ring fill the viewport
- Do not use color to establish text hierarchy - use size, weight, and the #fdfdfd/#6f6f6f contrast pair instead
- Do not add gradients to UI components, buttons, or cards; gradients are reserved exclusively for the spectrum ring system

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
