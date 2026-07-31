# OFFFICE :

Source: [Refero Style](https://styles.refero.design/style/190d4a0b-0353-4fc8-be09-affa6e977146)
Reference site: [https://offficestud.io](https://offficestud.io)
Captured: 2026-07-31
Refero published: 2026-02-22T17:15:07.000Z
Refero modified: 2026-06-05T08:39:30.625Z
Theme: dark
Category: Design

## Style Summary

Explore OFFFICE :'s dark Design design system: Onyx #0e0e00, Paper White #fefefe colors, ak, gs typography, and DESIGN.md for AI agents.

North star: noir gallery swallowed by monolithic type

## What To Borrow

- Onyx `#0e0e00` for Full-bleed page background, navigation surface, product staging void - the entire canvas is one continuous dark field
- Paper White `#fefefe` for Display headlines, body text, navigation labels, archive list entries, locale switcher - the sole ink color across all UI layers
- Faint White `#2a2a2a` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color

- ak `--font-ak` for Primary workhorse - nav, body, display headlines, archive list, labels, links. The extreme range from 12px to 216px in a single family, with weights 400 for quiet copy and 700 only for emphasis, defines the system's voice. Tight 0.80 line-height at 216px creates stacked text-blocks that read as architectural walls rather than sentences.
- gs `--font-gs` for Editorial serif accent - used exclusively in the project archive list for project titles. At 72px it provides a high-contrast counterpoint to ak's geometric sans; at 12px it renders archive metadata with classical warmth. The two-font system is deliberately minimal: one sans does everything, one serif appears only where editorial gravitas is needed.

## Avoid

- Do not introduce any accent color, brand color, or chromatic hue - the system is 100% achromatic by design
- Do not add borders, dividers, or background fills to separate sections - use space and type scale instead
- Do not use border-radius on any element - all corners are sharp (0px)
- Do not use shadows, glows, or blur effects for elevation - the design is flat by philosophy
- Do not use the serif (gs) for body copy, navigation, or anything outside the archive project titles
- Do not add gradients, textures, or background patterns to the Onyx canvas
- Do not constrain display headlines with max-width or text-overflow:hidden styling - overflow is the point

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
