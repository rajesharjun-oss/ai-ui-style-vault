# Mother Design

Source: [Refero Style](https://styles.refero.design/style/f40e6a6c-1704-407a-b21b-6141fb90adfe)
Reference site: [https://www.motherdesign.com](https://www.motherdesign.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:37:49.539Z
Refero modified: 2026-06-05T10:57:13.354Z
Theme: light
Category: Agency

## Style Summary

Explore Mother Design's light Agency design system: Newsprint #f4f4f4, Bone White #ffffff colors, Basis, Basis Mono typography, and DESIGN.md for AI agents.

North star: broadsheet manifesto in black ink

## What To Borrow

- Newsprint `#f4f4f4` for Soft section background, alternate surface, and quiet card fill.
- Bone White `#ffffff` for Navigation background, card surfaces, button fills, inverted text - pushes forward off the gray canvas
- Press Black `#000000` for Neutral form states, badge text, and quiet UI feedback where color should stay understated.
- Foil Gray `#808080` for Secondary text, subdued link borders, metadata - sits behind Press Black as quiet annotation
- Ink Green `#306f09` for Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content

- Basis `--font-basis` for Primary typeface across all UI. Weight 400 for body, links, and most running text; weight 600 used sparingly for the small uppercase-ish labels and the navigation tabs. The 226px size at 1.0 line-height is the signature - display type behaves like a poster headline, not a web heading. Negative tracking tightens as size grows: -0.04em at display, -0.02em at mid, -0.01em at body.
- Basis Mono `--font-basis-mono` for Used for technical labels, metadata, timestamps, and small annotations. The +0.06em letter-spacing gives it the feel of a printed caption set in a typewriter face - a deliberate counterpoint to Basis's tight grotesque.
- Times `--font-times` for System serif used as a rare editorial accent - appears in icon and small body contexts where a note of 'newspaper' or 'footnotes' is wanted. Its presence is felt more than seen; the choice signals print lineage rather than decoration.

## Avoid

- Do not introduce additional colors. Any new hue, even a desaturated one, will dilute the broadsheet identity. The green is a printer's mark, not a palette swatch.
- Do not add box-shadows, blurs, or any form of elevation. The system has no z-axis - depth is typographic.
- Do not round corners. Every border, button, and cell stays at 0px radius. Curvature would betray the printed-page metaphor.
- Do not cap display type at conventional web sizes (48-72px). The 226px / 110px scale is the point - shrinking it to 'feel more modern' removes the signature.
- Do not use weight 700 or 800. Basis 600 is the heaviest weight in the system; 400 does the work at display sizes because the size itself provides weight.
- Do not add icons inside buttons or cards. Icons live only in the theme toggle cluster and the brand mark cell.
- Do not center body copy or set paragraphs to a narrow max-width. The manifesto reads full-bleed; column width is controlled by the grid, not by a content container.

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
