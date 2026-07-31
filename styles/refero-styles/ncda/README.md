# NCDA

Source: [Refero Style](https://styles.refero.design/style/f654d52c-42de-4f3b-a377-9287b1536ad0)
Reference site: [https://ncda.biz](https://ncda.biz)
Captured: 2026-07-31
Refero published: 2026-04-30T01:58:41.015Z
Refero modified: 2026-06-05T08:22:05.598Z
Theme: mixed
Category: Agency

## Style Summary

Explore NCDA's mixed Agency design system: Onyx #191919, Pure Black #000000 colors, TWK Everett, TWK Everett Mono typography, and DESIGN.md for AI agents.

North star: Architectural monograph in negative space. The NCDA wordmark at 62px is cropped by the viewport edge, turning a logo into a wall.

## What To Borrow

- Onyx `#191919` for Primary text, hairline borders, full-bleed dark surface bands - the near-black ink of the system
- Pure Black `#000000` for Secondary text fills, deepest borders, and image overlays where maximum contrast against white is required
- Paper `#ffffff` for Page canvas, surface backgrounds, inverse text on dark bands
- Concrete `#808080` for Secondary descriptive text, muted link borders, subdued meta-information - the gray of footnotes and captions

- TWK Everett `--font-twk-everett` for All interface and display type - a neo-grotesque with tall x-height and geometric openness. The sole weight (400) across the entire range from 11px captions to 62px display creates a monolithic typographic voice. At 62px it receives aggressive negative tracking (-0.05em) that pulls the letterforms into a continuous architectural band; at 11px it switches to slight positive tracking (+0.04em) for utilitarian legibility in timestamps and labels.
- TWK Everett Mono `--font-twk-everett-mono` for Monospaced companion for data and technical annotations - used sparingly in body contexts where tabular alignment or code-like precision is needed. Single size at 21px with -0.01em tracking.

## Avoid

- Do not introduce any chromatic color - the system is 0% colorfulness by design, any hue breaks the monograph language
- Do not add border-radius to any element - all corners are sharp 0px, rounded shapes would undermine the architectural print language
- Do not use drop shadows or elevation effects - depth comes from scale and negative space, not from shadow stacks
- Do not set body or paragraph type at 62px - that size is reserved for the wordmark and display headlines that function as layout architecture
- Do not use more than two type sizes on a single screen - the system relies on extreme size contrast (15px body vs 62px display), intermediate sizes dilute the rhythm
- Do not add icons, arrows, or decorative glyphs to the Menu trigger or any navigation - the plain text label is the entire affordance
- Do not center-align body text - left-align everything; centering is reserved for the wordmark, everything else hangs from a left edge

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
