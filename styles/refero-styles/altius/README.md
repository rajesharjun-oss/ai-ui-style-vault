# Altius

Source: [Refero Style](https://styles.refero.design/style/227ff379-9b46-44fc-8ff1-37e0472239a6) 
Reference site: [https://www.altiuslabs.xyz](https://www.altiuslabs.xyz) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:13:58.887Z 
Refero modified: 2026-06-03T21:39:22.702Z 
Theme: dark 
Category: Crypto

## Style Summary

Explore Altius's dark Crypto design system: Obsidian Ember #190501, Dark Cocoa #340a01 colors, Matter, Fabrikatmono typography, and DESIGN.md for AI agents.

North star: Molten embers on obsidian. A blockchain command center lit from within by coral fire, where dark surfaces breathe warm light through hairline gaps and inset glows.

## What To Borrow

- Obsidian Ember `#190501` for Primary dark canvas - page background in dark sections, card surface, deepest borders. The black-with-warmth that defines the brand atmosphere
- Dark Cocoa `#340a01` for Secondary dark surface, deep link borders, icon outlines - one step lifted from obsidian for layering depth
- Molten Core `#631303` for Inset glow shadow source, deep red-brown accents - the pressed-ember tone that gives buttons their internal fire
- Signal Red `#951c04` for Outlined/ghost action border, nav borders, icon strokes, interactive outlines - the chromatic action color used for outlined buttons and active control edges
- Flare Orange `#fa5838` for Primary brand accent - links, decorative borders, the hero gradient spectrum, highlight washes. The single hottest color in the system; used sparingly as functional punctuation
- Warm Blush `#fcac9c` for Soft surface wash, secondary peach background, decorative highlight fields - the diffused ember tone for breathing sections
- Vapor Peach `#feeae6` for Light section background, light-mode card surface, body text on dark, ghost button text - the warm off-white that breaks the dark rhythm
- Linen `#f7f6ff` for Primary text on dark, crisp borders on dark sections, inverse text. The near-white that carries most typography on dark surfaces
- Warm Ash `#baadab` for Muted button borders on light sections, tertiary text, subtle dividers - a warm gray that softens edges without going cold
- Pure Black `#000000` for Decorative SVG fills, icon line art, graphical accents - high-contrast details that read as deep-ink on the warm canvas
- Mist `#cccccc` for Input field borders on light backgrounds - the only cool-neutral in the system, used minimally for form controls

- Matter `--font-matter` for Primary typeface - body, display, headings, buttons, navigation, icons. Weight 700 carries display headlines; 500 for emphasis in body; 400 for regular text. Tight tracking across all sizes creates a compressed, confident read.
- Fabrikatmono `--font-fabrikatmono` for Monospace accent - section labels, tags, technical metadata, trust signals. Used in uppercase for eyebrow labels like 'THE PROBLEM' and 'SOLUTIONS'. The technical-utility voice that contrasts Matter's editorial confidence.

## Avoid

- Don't add drop shadows to cards or panels - the system uses hairline borders and surface differentiation only
- Don't use blue or cool tones - the entire palette is warm, from Vapor Peach through Molten Core
- Don't create filled buttons with Flare Orange (#fa5838) background - Flare Orange is for accents, not button fills
- Don't use display sizes below 48px or above 60px - the type scale is compressed and confident
- Don't let dark sections run more than 2-3 before introducing a Vapor Peach break - the thermal alternation is structural
- Don't use generic sans-serif fallbacks as the primary face - Matter's tight tracking is part of the voice
- Don't apply color to body text - keep body text in Linen (#f7f6ff) on dark or Obsidian Ember (#190501) on light

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
