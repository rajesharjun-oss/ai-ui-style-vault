# Arthursimonini

Source: [Refero Style](https://styles.refero.design/style/6778ff21-44eb-40f3-ba85-2ee7de935f8f)
Reference site: [https://arthursimonini.com](https://arthursimonini.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:27:50.539Z
Refero modified: 2026-06-05T12:01:03.652Z
Theme: dark
Category: Media

## Style Summary

Explore Arthursimonini's dark Media design system: Obsidian #000000, Bone #ffffff colors, RomieLigatures-Regular, LifeLTStd-Roman typography, and DESIGN.md...

North star: printed film programme in black ink

## What To Borrow

- Obsidian `#000000` for Page canvas, nav background, poster grid ground
- Bone `#ffffff` for All text, hairline section borders, image borders, icon strokes

- RomieLigatures-Regular `--font-romieligatures-regular` for Display headlines, section titles, marquee text. The signature choice: this didone carries discretionary ligatures (dlig) that fuse letters into ornamental shapes - the oversized wordmarks and repeated marquee bands rely on these ligatures for their distinctive character. Line-height collapses to 0.73 at the 167px size so stacked display lines almost touch, creating a dense editorial block. Reserved exclusively for type-as-art moments; never used for body copy or UI labels.
- LifeLTStd-Roman `--font-lifeltstd-roman` for Navigation links, metadata, body copy, timestamps, section category labels. A single weight at a single size - the system does not modulate emphasis through weight. Tracking is normal. This is the functional typeface that scaffolds the UI while the display face performs. Its quietness is the point: LifeLTStd is a transitional serif that reads cleanly at 18px without competing with the display type.

## Avoid

- Never introduce color - not for hover states, not for active nav, not for error messages, not for decorative accents.
- Never use border-radius - all corners are square (0px). This includes buttons, images, and tags.
- Never apply box-shadow or drop-shadow - elevation is expressed through white hairlines and negative space, not depth.
- Never use bold or semibold weights - both typefaces operate at 400 only. Emphasis comes from size contrast, not weight.
- Never use RomieLigatures for body copy, labels, timestamps, or anything below 65px - the decorative ligatures become illegible at small sizes.
- Never add background fills, gradients, or colored overlays to poster images - keep them raw grayscale with only a white border.
- Never center-align body text or metadata - left-align for content, right-align only for timestamps and durations.

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
