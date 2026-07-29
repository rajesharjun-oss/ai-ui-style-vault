# Apollo

Source: [Refero Style](https://styles.refero.design/style/5fbdad0a-d102-41c2-8253-f201ad6a6673) 
Reference site: [https://apolloworkspace.com](https://apolloworkspace.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:17:25.659Z 
Refero modified: 2026-06-03T17:48:32.675Z 
Theme: light 
Category: Other

## Style Summary

Explore Apollo's light Other design system: Espresso Bark #3c261c, Terracotta Ember #e97451 colors, MonaSans, paradigm-pro typography, and DESIGN.md for AI...

North star: Warm brick atelier at golden hour

## What To Borrow

- Espresso Bark `#3c261c` for Primary text, navigation background, structural borders - a warm near-black that anchors every screen without the harshness of pure #000000
- Terracotta Ember `#e97451` for Primary action borders, active nav state, decorative accents - rationed to moments of intent, never used as a large surface fill
- Iris Ink `#4a43dd` for Decorative display headings, logo monogram stroke - a vivid violet that breaks the warm palette for brand-voice headlines only
- Honey Parchment `#f7efc5` for Subtle highlight washes, eyebrow label backgrounds, warm text tint - a muted yellow that warms the cream canvas without competing with terracotta
- Warm Linen `#f9f8f0` for Page canvas, content section backgrounds - the dominant surface, never pure white, always slightly cream
- Ash Mist `#dddedf` for Hairline borders, dividers, card edges - the most-used color on the site (1,300+ occurrences), creates the cool rule-lines that structure every layout
- Blush Cream `#fcede8` for Warm tinted surface for hover states and soft callout blocks - a peach wash that warms the cream canvas
- Lilac Mist `#e4e3f2` for Cool surface accent for secondary panels - a lavender-tinted gray that introduces gentle contrast against the warm cream
- Carbon `#000000` for True black used sparingly for image fills and footer text - Espresso Bark handles all structural dark needs

- MonaSans `--font-monasans` for Body text, navigation, buttons, section headings, UI labels - the workhorse sans-serif. Uppercase instances at 0.07-0.1em tracking are signature; the wide tracking on 12-14px labels reads like a museum placard, not a UI label.
- paradigm-pro `--font-paradigm-pro` for Display headings and hero text only - a whisper-thin custom serif at weight 300. The ultra-light weight is anti-convention: most editorial sites use 400-500 serifs for headlines, but this 300 creates authority through restraint. Tight line-height (0.95) lets the letters interlock like a logotype.

## Avoid

- Do not use border-radius larger than 3px - no pill buttons, no rounded cards, no soft corners anywhere
- Do not use #ffffff as a background - always use Warm Linen (#f9f8f0) to maintain the cream canvas warmth
- Do not use drop shadows or box-shadow elevation - separation comes from hairline borders and tonal surface shifts only
- Do not use Terracotta Ember as a large fill color - it is an accent, rationed to borders, active states, and the logo only
- Do not use Iris Ink (#4a43dd) for body text or navigation - it is reserved for decorative display headings and the logo monogram stroke
- Do not use font-weight above 300 for the paradigm-pro display serif - the whisper-thin weight is the entire point
- Do not mix multiple accent colors in a single view - terracotta speaks alone; adding iris or honey to the same component creates noise

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
