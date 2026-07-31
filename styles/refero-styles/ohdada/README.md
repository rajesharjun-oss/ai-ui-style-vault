# OhDada

Source: [Refero Style](https://styles.refero.design/style/d69af89b-cb31-426d-b9aa-c21d127b8947)
Reference site: [https://ohdada.de](https://ohdada.de)
Captured: 2026-07-31
Refero published: 2026-04-30T03:28:43.924Z
Refero modified: 2026-06-05T11:34:11.080Z
Theme: light
Category: E-commerce

## Style Summary

Explore OhDada's light E-commerce design system: Chalk Cream #e6e0d9, Lavender Stone #b7b3be colors, GrandSlang-Roman, Neue Haas Grotesk Display typography,...

North star: Editorial gallery wall

## What To Borrow

- Chalk Cream `#e6e0d9` for Primary page canvas and secondary section background; the warm off-white that makes brown type and sculpture photography feel curated rather than clinical
- Lavender Stone `#b7b3be` for Alternate section background and hero canvas; introduces a cool, chalky counterpoint to the warm cream without breaking the achromatic discipline
- Saddle Brown `#5d3a19` for All headings, body copy, link text, and hairline borders - the only chromatic voice in the system, used as a drawn-with-ink accent against the pale neutrals; Outlined and ghost interactive borders; links and navigation controls carry a 1px brown stroke rather than a filled background, keeping the surface quiet
- Ink Black `#000000` for Decorative SVG fills only; never used for UI text or surface elements

- GrandSlang-Roman `--font-grandslang-roman` for Brand mark and large display headings only - used at 58px+ for the wordmark and section titles. Weight 100 is the entire signature: hairline serif strokes that read as drawn rather than typeset. Substitute: Cormorant Garamond Ultralight or Italiana, which approximate the extreme thinness and high-contrast serif construction.
- Neue Haas Grotesk Display `--font-neue-haas-grotesk-display` for All body copy, navigation, secondary headings, and product labels. Weights 400 for body, 500 for emphasis. The neo-grotesque geometry acts as a neutral ground for the expressive display serif - a deliberate Swiss-type baseline that lets GrandSlang perform. Substitute: Inter, Neue Haas Unica, or Helvetica Neue.

## Avoid

- Do not introduce gradients, drop shadows, or elevation effects - the system is flat by design
- Do not use rounded corners on any element; 0px radius is structural to the editorial feel
- Do not add a fourth color to the palette - Saddle Brown, Chalk Cream, and Lavender Stone are the complete chromatic vocabulary
- Do not set GrandSlang-Roman below 58px or in any weight other than 100; it loses its character at small sizes
- Do not use filled button backgrounds for primary actions; use the outlined-link treatment with a brown border instead
- Do not center body text - the layout is left-aligned throughout, even in the hero
- Do not add hover animations, color transitions, or motion; the interface reads as a printed catalog

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
