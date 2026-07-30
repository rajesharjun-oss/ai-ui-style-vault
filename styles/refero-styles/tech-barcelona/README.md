# Tech Barcelona

Source: [Refero Style](https://styles.refero.design/style/271172f7-9f6d-4d6f-9baa-91a41648d8be)
Reference site: [https://techbarcelona.com/en](https://techbarcelona.com/en)
Captured: 2026-07-30
Refero published: 2026-04-30T02:29:49.606Z
Refero modified: 2026-07-03T11:47:11.897Z
Theme: mixed
Category: Other

## Style Summary

Explore Tech Barcelona's mixed Other design system: Cobalt Action #0075ff, Ink Black #090707 colors, FavoritPro-Light typography, and DESIGN.md for AI agents.

North star: Editorial tech manifesto on white marble

## What To Borrow

- Cobalt Action `#0075ff` for Primary CTA buttons, the only chromatic accent in the entire interface - one vivid blue against monochrome neutrals, used sparingly so it signals action without competing with content
- Ink Black `#090707` for Headline color, image borders, large display text - near-black with the slightest warmth, chosen over pure black to feel printed rather than digital
- Graphite `#212529` for Body text, nav links, icon strokes, card borders - the working neutral for interface chrome and readable paragraph copy
- Pure White `#ffffff` for Page canvas, card surfaces, text on dark hero and dark logo backgrounds - establishes the light-mode base and all content surfaces
- Hairline Gray `#cccccc` for Subtle dividers and secondary borders - thin separator lines on light surfaces where #212529 would be too heavy
- Pure Black `#000000` for Dark borders and separators for elevated surfaces and inverted UI.
- Shadow Whisper `#eeeeee` for Near-invisible ambient shadow tint for button states - a 1px 1px wash so faint it barely registers, used instead of full drop-shadows

- FavoritPro-Light `--font-favoritpro-light` for Single-family type system used for every interface element - nav, body, buttons, headlines, and 80px display. Weight 400 throughout is a signature choice: the system relies on scale jumps (14px body 50px subhead 80px display) rather than bold weights to establish hierarchy, giving the entire site an understated, editorial cadence

## Avoid

- Do not use shadows or elevation effects - the system is intentionally flat with hairline borders only
- Do not introduce additional chromatic colors - the blue/cobalt is the sole accent and its power depends on singularity
- Do not use bold (600+) or semibold weights - the entire interface speaks at weight 400 and louder weights would break the voice
- Do not apply rounded corners (border-radius) to any element - the squared-off geometry is load-bearing
- Do not add gradients, textures, or background patterns to any surface - every surface is a flat solid color
- Do not use #ffffff as a filled button background for actions - the only filled action color is #0075ff; everything else is ghost or text-link
- Do not compress line-height below 1.0 on display sizes - the tight tracking combined with the geometric letterforms already create visual density

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
