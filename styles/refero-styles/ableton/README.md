# Ableton

Source: [Refero Style](https://styles.refero.design/style/e5081033-bd79-479a-aef6-8b002df6086a)
Reference site: [https://ableton.com](https://ableton.com)
Captured: 2026-07-31
Refero published: 2026-01-27T16:17:02.000Z
Refero modified: 2026-06-05T08:29:40.986Z
Theme: light
Category: Productivity

## Style Summary

Explore Ableton's light Productivity design system: Ink #000000, Paper #ffffff colors, futura-pt typography, and DESIGN.md for AI agents.

North star: Editorial workshop on stark white. White paper, black Futura, one blue pen mark for interactivity, photography clipped flush to the edges like magazine spreads.

## What To Borrow

- Ink `#000000` for Primary text, nav labels, logo, icon strokes, and every text-level heading - sets the full information hierarchy
- Paper `#ffffff` for Page canvas, card surface, and hero overlay text - the default background for almost every screen
- Fog `#eeeeee` for Subtle form inputs, tag surfaces, and quiet secondary panel backgrounds - barely-there neutral
- Signal Blue `#0000ff` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Coral `#ff8389` for Category tag fills (Downloads, News) - flat rectangular badges that classify content without padding the layout
- Teal `#00d2be` for Category tag fills (Tutorials, Videos) - flat rectangular badges paired with coral to split content taxonomy visually

- futura-pt `--font-futura-pt` for The single typeface powering everything from body copy to 90px display headlines. Futura PT's geometric precision mirrors Ableton's grid-based music software - the type and the product share a visual logic. Weight 700 carries headlines, 400 carries body. No serif, no monospace secondary face - the system stays mono-typographic.

## Avoid

- Do not add box-shadows or elevation to any component - the system is deliberately flat
- Do not round corners on cards, tags, buttons, or inputs - keep 0px everywhere
- Do not use coral or teal for buttons, CTAs, or interactive text - they are taxonomy-only
- Do not call #0000ff a 'CTA color' - it is a link color used for interactive text, not filled buttons
- Do not introduce gradient backgrounds - the system is solid color and photography only
- Do not add icons, illustrations, or decorative graphics - photography and type carry the visual load
- Do not set body text below 14px or use a weight other than 400 for body copy

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
