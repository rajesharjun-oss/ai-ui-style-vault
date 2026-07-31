# Electronic Materials Office(R)

Source: [Refero Style](https://styles.refero.design/style/297f65f7-0fbd-4521-ab91-a5f6e17175d9)
Reference site: [https://electronicmaterialsoffice.com](https://electronicmaterialsoffice.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:28:50.412Z
Refero modified: 2026-06-05T10:29:02.082Z
Theme: dark
Category: E-commerce

## Style Summary

Explore Electronic Materials Office(R)'s dark E-commerce design system: Studio Charcoal #202020, Bone White #ffffff colors, GT-Flexa, Tobias-light typography,...

North star: Incandescent ember in a charcoal gallery

## What To Borrow

- Studio Charcoal `#202020` for Page canvas and card surfaces - the floor of the dark gallery, never pure black so the eye can rest on edge softness
- Bone White `#ffffff` for Primary text, hairline borders on images, and the rare inverted surface. Carries all type hierarchy on its own
- Ash Gray `#9d9d9d` for Muted text, subtle card borders, inactive labels - the only middle gray in the scale, used when white is too loud
- Mid Felt `#eaeaea` for Light surface wash for inverted panels or modal scrims - the off-white that sits between bone and the dark canvas
- Carbon `#000000` for Deepest accent for icon strokes and contrast borders where the charcoal canvas is too light to hold an edge
- Ember Orange `#f45500` for Filled primary action button - the only chromatic surface in the UI, always paired with a 30px orange halo so it glows like a filament; 30px outer glow on the primary CTA - duplicates the Ember Orange hex but exists as a box-shadow, not a fill, so the button appears lit from within
- Lavender Link `#9e9eff` for Inline link color and the outlined secondary action border - a desaturated cool counterpoint to the warm orange ember, keeping actions readable against charcoal

- GT-Flexa `--font-gt-flexa` for Display and heading workhorse. Weight 200 carries every headline above 24px - the 200 weight is the signature: at 68px and 86px the letterforms dissolve into atmosphere rather than shout. Weight 400 steps in for sub-headings and card captions where a whisper isn't enough. Line-heights collapse toward 1.0 at the largest sizes so display type stacks like a column of breath.
- Tobias-light `--font-tobias-light` for Secondary display voice for section headers and the footer wordmark. Used at a step below GT-Flexa 200 to create tonal contrast - Tobias feels more architectural, more labeled, while GT-Flexa feels ambient. Negative letter-spacing tightens the wide proportions of the Tobias Light cut.
- Times `--font-times` for Body text and hero paragraph copy - a deliberate serif counterpoint to the geometric display fonts. The serif adds warmth and editorial gravity to product descriptions without ever growing larger than body size.

## Avoid

- Do not use Times or any serif for headings, labels, or UI chrome - it is body copy only
- Do not apply the Ember Orange glow to anything other than the primary CTA
- Do not introduce additional saturated brand colors - the system is orange + violet on charcoal
- Do not use weight 400 or above for display headlines above 42px - the 200 weight is non-negotiable
- Do not add box-shadows to cards, images, or navigation - shadows are reserved for the two button variants
- Do not center body copy or paragraph text - left alignment only, matching the hero headline
- Do not round anything below 16px - the system commits to soft, large radii

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
