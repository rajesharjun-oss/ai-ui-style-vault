# Arsenijs Fabrica

Source: [Refero Style](https://styles.refero.design/style/eb3bf6c1-a18f-4d72-801e-50c2cdbbaa21) 
Reference site: [https://www.arsenijsfabrica.com](https://www.arsenijsfabrica.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:54:42.130Z 
Refero modified: 2026-06-03T19:14:40.459Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore Arsenijs Fabrica's light E-commerce design system: Ember Orange #f15730, Tangerine Blaze #f7651a colors, Onest, Times typography, and DESIGN.md for...

North star: Editorial beauty spread under gallery lights. Pure-white gallery walls, a single warm strobe pulsing orange against the monochrome, type set thin as glass and hung with generous negative space.

## What To Borrow

- Ember Orange `#f15730` for Filled CTA buttons, primary action backgrounds - deep saturated orange that reads as confident rather than playful, the only color with enough chroma to anchor a click target against the white field
- Tangerine Blaze `#f7651a` for Promotional surface fills (email capture modal, featured product cards, stat callout backgrounds) - slightly brighter and more luminous than Ember, used where orange must own an entire region of the layout
- Apricot Whisper `#ff8562` for Borders on outlined cards, link underlines, icon strokes, accent hairlines - the lightest orange, functioning as a warm-tinted structural color rather than a fill
- Graphite Black `#111111` for Body text, default borders, the dominant structural color - a true near-black, not warm, used for the bulk of hairline rules and paragraph copy
- Inkwell `#0d1717` for Heading text, navigation text, primary headings - a deep black with the faintest cool-green undertone that gives headlines a quiet cast against pure white
- Pure White `#ffffff` for Page canvas, card surfaces, text on dark/orange surfaces - the unchanging ground tone across every section
- Mist Gray `#eeeeee` for Soft card borders, hairline dividers on white surfaces where Graphite would feel too heavy
- Smoke `#818181` for Secondary captions, muted helper text, subdued icon strokes - the only mid-gray in the palette, used sparingly to fade metadata without going fully light

- Onest `--font-onest` for Sole brand typeface. The 200-300 weights at display sizes (48-152px) define the editorial couture voice - thin strokes hung on a white wall with aggressive negative letter-spacing. Weights 400-500 handle body and UI; 600-800 reserved for occasional emphasis. Substantial negative letter-spacing contracts large text to the width of small, producing the 'cut from a single line' effect. Substitute with Inter or General Sans if Onest is unavailable.
- Times `--font-times` for Times - detected in extracted data but not described by AI
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

## Avoid

- Don't apply box-shadows to cards, buttons, or modals - the system communicates depth with borders and color alone
- Don't use Orange for body text - its contrast on white fails accessibility, keep it for fills, borders, and large display numbers only
- Don't use weights 600-800 for body text or UI labels - reserve them for the rare emphasis moment
- Don't introduce a second accent color or hue - the orange must remain the single chromatic note
- Don't use 0px or 4px border-radius on cards or images - the 10px/15px minimum is part of the soft editorial feel
- Don't center product card text - left-align all UI copy; centering is reserved for the hero overlay and modal content
- Don't apply gradients to surface fills - the only observed gradient is a single progress-bar indicator on a dark surface

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
