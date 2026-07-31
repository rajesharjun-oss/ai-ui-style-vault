# Zoox

Source: [Refero Style](https://styles.refero.design/style/e85a82b1-c70e-42de-8c42-4bd95dd5e047)
Reference site: [https://zoox.com](https://zoox.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:38:40.979Z
Refero modified: 2026-06-05T10:29:53.131Z
Theme: light
Category: Other

## Style Summary

Explore Zoox's light Other design system: Sage Canvas #d3e4df, Pure White #ffffff colors, GT Standard S, GT Standard L typography, and DESIGN.md for AI agents.

North star: serene sage showroom. A pale mint gallery space where one vivid teal accent and one dark forest panel interrupt the quiet - spacious, premium, and forward-looking.

## What To Borrow

- Sage Canvas `#d3e4df` for Page background, hero bands, section dividers - the dominant ambient color that gives the system its calming gallery atmosphere
- Pure White `#ffffff` for Card surfaces, image masks, icon fills, high-contrast text on dark sections
- Mint Frost `#edf4f2` for Badge backgrounds, subtle highlight washes, secondary card surfaces - a quieter sibling of the sage canvas
- Carbon `#0d1212` for Primary text, dark section backgrounds, heavy borders - the deepest near-black, slightly cooler than true black
- Graphite `#34484a` for Navigation borders, secondary headings, muted icon strokes - a dark desaturated teal that bridges neutrals and the accent; Dark borders and separators for elevated surfaces and inverted UI.
- Slate `#565959` for Body text secondary level, list dividers, footers, muted borders
- Fog `#9aa3a5` for Tertiary text, placeholder labels, disabled icon strokes
- Mist `#7b8889` for Eyebrow text and label color, small caps headers
- Vivid Teal `#64d5b3` for Primary action button fills, accent surfaces, interactive highlights - the single chromatic color in the system, used sparingly to signal action
- Eucalyptus `#5b8279` for Gray outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color

- GT Standard S `--font-gt-standard-s` for Primary UI and body typeface - used for navigation, buttons, body copy, badges, inputs, and headings up to 50px. The 'kern' 0 feature setting deliberately disables kerning for a monospaced-mechanical feel. The 0.0500em tracking on 12-13px text gives small labels a spacious, typeset quality.
- GT Standard L `--font-gt-standard-l` for Display-only typeface reserved for hero headlines and large section titles. Used at a single weight (400) to keep the voice calm and confident - no bold shouting. The 120px size with normal letter-spacing creates wide, architectural headlines that sit centered on the sage canvas.

## Avoid

- Do not introduce additional chromatic colors - the system is sage, white, carbon, and one teal accent
- Do not use bold weights for display headlines - GT Standard L is always weight 400
- Do not apply box-shadow to cards, buttons, or navigation - the system relies on radius and borders
- Do not use #34484a (Deep Forest) as a text color or border on light backgrounds - it is reserved for the dark section background
- Do not set body text below 13px or use letter-spacing tighter than -0.002em on UI text
- Do not use the Vivid Teal on text - it is a surface color only, paired with #0d1212 or #ffffff text
- Do not break the section rhythm with narrow max-width containers - let the sage canvas flow full-bleed

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
