# LogoArchive

Source: [Refero Style](https://styles.refero.design/style/b63cc4ca-52c6-4b70-9a5a-cb04bae15edb)
Reference site: [https://www.logo-archive.org](https://www.logo-archive.org)
Captured: 2026-07-30
Refero published: 2026-04-30T02:04:19.064Z
Refero modified: 2026-06-05T12:53:09.282Z
Theme: dark
Category: Design

## Style Summary

Explore LogoArchive's dark Design design system: Canvas Charcoal #27272a, Elevated Ink #18181b colors, Suisse International, Suisse Works Book typography,...

North star: midnight gallery of iconic marks

## What To Borrow

- Canvas Charcoal `#27272a` for Page background, primary canvas surface
- Elevated Ink `#18181b` for Card surfaces, product window backgrounds, logo tiles - one step deeper than canvas for contrast
- Slate Surface `#343538` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Deep Void `#000000` for Nav fills, deepest surface tone, pure black accents
- Near Black `#0c0c0e` for List borders, hairline dividers, subtle structural edges
- Pure White `#ffffff` for Primary text, icons, borders, high-contrast elements - the dominant interface color
- Fog Gray `#a8afb7` for Muted body text, secondary headings, subtle borders - readable but recessive
- Mist Gray `#dadee4` for Light borders, disabled-state text, very subtle dividers
- Dim Stone `#8c8c8d` for Placeholder/disabled surfaces, inactive list backgrounds
- Signal Yellow `#fde533` for Yellow outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color

- Suisse International `--font-suisse-international` for Primary typeface for all UI text, body, navigation, buttons, and most headings
- Suisse Works Book `--font-suisse-works-book` for Italic display emphasis in hero and section headlines

## Avoid

- Don't introduce a second accent color - the system is monochromatic with one yellow signal
- Don't use box-shadow for elevation - rely on tonal surface contrast only
- Don't use display sizes below 65px for headlines - the scale jumps from 28px to 65px intentionally
- Don't use system fonts or non-Swiss grotesques - the typographic identity is precise and mechanical
- Don't add gradients - the system is fully flat
- Don't use light-theme colors or white backgrounds - the system is dark-first
- Don't use borders thicker than 1px or with high contrast - borders are always hairline and subtle

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
