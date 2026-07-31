# clau.as.kee

Source: [Refero Style](https://styles.refero.design/style/9aad4722-413d-4b32-bda7-6f94bbd9938c)
Reference site: [https://clauaskee.com](https://clauaskee.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:47:15.558Z
Refero modified: 2026-06-05T10:21:07.953Z
Theme: light
Category: Agency

## Style Summary

Explore clau.as.kee's light Agency design system: Periwinkle Field #8e93ff, Carbon Ink #1a1a1a colors, Beastly clauworks, Suisse Intl clauworks typography,...

North star: lavender poster wall, monumental type. A flat periwinkle field with a single black-letter sculpture filling the viewport and a thin line of small nav text floating above it.

## What To Borrow

- Periwinkle Field `#8e93ff` for Page canvas, hero background, full-bleed section fills - the single defining brand color, a mid-saturation lavender that swallows the viewport and against which all type is set in black ink
- Carbon Ink `#1a1a1a` for Primary text, display type, hairline borders, dark panels, nav links - near-black rather than pure black, keeps the lavender from vibrating too hard
- Paper White `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces.
- Signal Green `#47f654` for Green action color for filled buttons, selected navigation states, and focused conversion moments.

- Beastly clauworks `--font-beastly-clauworks` for Display / wordmark - the proprietary display face, used only at monumental scale (288-504px) for the brand wordmark and hero sculpture. Chunky, almost stencil-cut geometric forms that read as a graphic object rather than readable text. Single weight, no italic. Substitute: a heavy display grotesque like Druk Wide or a custom commission. Do not use at small sizes - this face is architecture, not communication.
- Suisse Intl clauworks `--font-suisse-intl-clauworks` for Headlines, subheads, and long-form body - a custom-cut Suisse International (Swiss grotesque) in a single weight. Used at three distinct scales: 20px for body and nav, 30px for section subheads, 144px for editorial display headings like 'Art direction - Dig...'. The absence of bold/medium weights is the signature: everything is the same quiet weight, hierarchy comes from size alone. Substitute: Suisse Int'l, Inter, or Neue Haas Grotesk.
- Times `--font-times` for Smallest body fallback / metadata - appears as system Times at 16px, likely the serif default for tiny labels and captions. Single weight, system face. Substitute: any system serif.

## Avoid

- Do not add a fifth color, a tinted neutral, or a soft shadow to soften the lavender - the flatness is the design
- Do not use rounded corners on panels, cards, or images; 0px radius everywhere except the green badge
- Do not introduce a bold or medium weight of Suisse Intl - hierarchy is size-driven only
- Do not use Beastly at small sizes (under 200px) - it loses its character and becomes a bad display grotesque
- Do not center body copy or set it in narrow columns; body text is left-aligned, full-width-feeling, generous
- Do not add a sticky header, breadcrumb, or secondary navigation; the three-link top bar is the entire nav system
- Do not use gradients, blur, glow, or any CSS filter on the lavender background - it must read as a flat printed field

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
