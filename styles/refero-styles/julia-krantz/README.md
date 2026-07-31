# Julia Krantz

Source: [Refero Style](https://styles.refero.design/style/92857b05-1c01-4c7a-b196-beb4e4871998)
Reference site: [https://juliakrantz.com](https://juliakrantz.com)
Captured: 2026-07-31
Refero published: 2026-04-28T21:33:22.049Z
Refero modified: 2026-06-05T12:02:38.260Z
Theme: dark
Category: Agency

## Style Summary

Explore Julia Krantz's dark Agency design system: Void #000000, Salt #f8f8f8 colors, DM Sans, ClashDisplay typography, and DESIGN.md for AI agents.

North star: Darkroom contact sheet - a grid of photographic tiles on pure black, identity spelled in barely-visible weight-300 letterforms.

## What To Borrow

- Void `#000000` for Page canvas, all section backgrounds - the true floor of the UI; every element floats above absolute black
- Salt `#f8f8f8` for All text, links, nav labels, borders, icons - the single foreground tone serving every text and UI edge function against black
- Ash `#707070` for Secondary labels, muted nav text, subdued body copy - mid-tone for visual hierarchy without introducing any hue

- DM Sans `--font-dm-sans` for All body copy, navigation labels, press list items, links, captions. Weight 300 across every size - the site refuses to bold anything in this family, keeping the text layer visually quiet against photography.
- ClashDisplay `--font-clashdisplay` for Project initials on tiles (44px weight 300, tracking -0.04em), section codes and labels (12-14px weight 300, tracking +0.05em to +0.14em), name logotype. The 44px weight-300 display setting - a nearly invisible letterform over a photograph - is the signature visual move of the portfolio.

## Avoid

- Never add any color to the UI chrome - buttons, links, labels, borders must remain in the #f8f8f8 / #707070 / rgba opacity system only
- Never round corners - no border-radius on tiles, containers, or any interactive element; 0px is non-negotiable
- Never use font weight above 500 - ClashDisplay 500 is the ceiling and used only for the name logotype; DM Sans stays at 300
- Never add box-shadows or elevation - the design has zero shadow tokens; depth comes from contrast with the black canvas only
- Never add hover backgrounds or button fills - interactive states change text opacity or image brightness only, never add a background color
- Never introduce gradients, overlays, or tinted backgrounds - the CSS tokens confirm no gradient system exists; #000 is the only background
- Never separate the category label from its tile project code with more than 4px margin - the tight stacking (4px marginBottom between elements) is the spatial rhythm

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
