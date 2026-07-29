# Analogue aF-1

Source: [Refero Style](https://styles.refero.design/style/6607e4ff-2de6-4a6a-a7ed-53a9e4b550b9) 
Reference site: [https://af1.analogueshop.com](https://af1.analogueshop.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:16:11.553Z 
Refero modified: 2026-06-03T21:18:03.331Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore Analogue aF-1's light E-commerce design system: Cobalt Signal #002fff, Pure White #ffffff colors, ITC Garamond Std Light Narrow, Graphik Medium...

North star: Vogue spread meets Bauhaus blueprint

## What To Borrow

- Cobalt Signal `#002fff` for Violet action color for filled buttons, selected navigation states, and focused conversion moments.
- Pure White `#ffffff` for Page canvas, card surfaces, button text on cobalt fill, heading text on dark sections
- Graphite `#171717` for Primary body text, heading text, hairline borders, icon strokes - the workhorse near-black that carries UI structure
- Carbon `#070707` for Deepest text, dark gradient anchor points, near-black accents where maximum contrast is needed
- Ink `#000000` for Absolute black for borders, icons, and the film-strip frame effect - appears most in structural borders rather than type
- Fog `#ededed` for Soft card surface lift, input fields, subtle background differentiation from pure white canvas
- Mist `#b9b9b9` for Light surface wash, disabled or decorative backgrounds
- Dove `#c3c3c3` for Mid-neutral border for tertiary dividers
- Iron `#696969` for Muted body copy, secondary borders, placeholder text - the dominant mid-gray carrying prose-level hierarchy

- ITC Garamond Std Light Narrow `--font-itc-garamond-std-light-narrow` for Editorial serif - deployed for the brand-defining typographic moments: the 'Analogue aF-1' wordmark, the nostalgic pull-quote ('Remember when every shot was a moment to cherish?'), and section-level statements. Light weight at large sizes is deliberately anti-luxury-tech; a Garamond at 64px weight 400 whispers where most product pages shout with bold sans. Narrow variant tightens the serif into modern proportions.
- Graphik Medium `--font-graphik-medium` for Geometric sans for all functional UI: navigation, buttons, input fields, captions, body labels, and the massive 150px display headline. Single weight (400) at every size creates a remarkably consistent voice - no bold/light toggle. The 150px instance is the 'af-1' hero display. Extremely tight tracking (-0.067em at the largest size) pushes the geometric forms into near-architectural density.
- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI

## Avoid

- Never apply #002fff to backgrounds, icons, or text - it is a button fill only. Decorative blue dilutes its power as the system's one action color.
- Do not introduce drop shadows. The system uses flat surfaces and hairline borders. The only shadow permitted is the inset white glow on inputs.
- Do not use bold weights on Garamond. The light weight is the point - bold Garamond breaks the editorial whisper into a shout.
- Never use corner radii below 10px for interactive elements. The rounded geometry is non-negotiable for the premium feel.
- Do not add gradients to UI components. Gradients appear only as atmospheric washes on full-bleed sections, never on buttons, cards, or inputs.
- Do not use warm colors, greens, oranges, or reds for any state. The system is achromatic + cobalt. If you need a success/error state, use the neutral scale (#171717, #696969).
- Do not use Garamond for functional UI text (buttons, labels, inputs). It is reserved for editorial moments. Graphik handles everything functional.

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
