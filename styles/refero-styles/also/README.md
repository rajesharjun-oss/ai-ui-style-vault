# ALSO

Source: [Refero Style](https://styles.refero.design/style/d04a3970-45f0-4030-8375-d0d26c083c0f) 
Reference site: [https://ridealso.com](https://ridealso.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T22:35:03.443Z 
Refero modified: 2026-06-03T21:02:20.560Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore ALSO's light E-commerce design system: Cream Paper #fcf7fa, Pure Card #ffffff colors, ABCCameraPlainVariable, SerialC-Heavy typography, and...

North star: Bicycle zine on cream paper

## What To Borrow

- Cream Paper `#fcf7fa` for Page canvas, soft section background - warm off-white with a barely-there pink cast, never pure white
- Pure Card `#ffffff` for Card surfaces, elevated panels, button text on violet fills
- Ash Mist `#f1f1f1` for Tertiary surface, muted dividers, subtle background washes
- Carbon Black `#000000` for Primary text, default borders, icon strokes - the structural ink of the system
- Graphite Input `#212121` for Input field borders, secondary dark surfaces
- Obsidian Pill `#1a1a1a` for Dark CTA fill - the secondary action button (e.g. Reserve), pairs with white text and violet shadow
- Electric Violet `#ac74fc` for Primary accent - link borders, active states, icon highlights, section accent borders. The brand's signal color
- Lilac Pill `#c181ff` for Primary CTA button fill - the dominant call-to-action, sits on violet hard shadow with black text
- Deep Plum `#381b5e` for Dark violet text variant, deep accent borders, section-level emphasis when Electric Violet feels too bright
- Shadow Plum `#48316a` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Acid Lime `#b1ff8f` for Sparingly used highlight wash or accent surface for urgency moments (limited drops, reservation states)
- Signal Blue `#1276a9` for Outlined action border - secondary ghost button or informational outline accent

- ABCCameraPlainVariable `--font-abccameraplainvariable` for Primary UI and display typeface - handles body, headings, navigation, and product copy
- SerialC-Heavy `--font-serialc-heavy` for Uppercase eyebrows, button text, section labels, mono-influenced captions
- SerialC `--font-serialc` for SerialC - detected in extracted data but not described by AI

## Avoid

- Never use soft drop shadows with blur - the 2px solid hard shadow is the only shadow in the system.
- Never use Pure White (#ffffff) as page canvas - always start from Cream Paper (#fcf7fa); white is reserved for cards and elevated surfaces.
- Never set ABCCameraPlainVariable with positive letter-spacing on body or heading text - the system compresses at scale, it does not expand.
- Never use rounded corners on product images, story cards, or hero photography - these are sharp-edged; only buttons, inputs, and feature cards get radius.
- Never add a second chromatic accent - Electric Violet is the system; Acid Lime and Signal Blue are rare utility colors for specific states only.
- Never use a different shadow color - Shadow Plum (#48316a) stays constant even on dark or green buttons, keeping the brand cohesive across all CTA variants.
- Never set SerialC-Heavy in lowercase or sentence case - it is an uppercase-only typeface in this system; using it otherwise breaks the typographic rhythm.

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
