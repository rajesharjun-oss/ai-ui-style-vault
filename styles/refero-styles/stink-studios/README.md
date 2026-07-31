# Stink Studios

Source: [Refero Style](https://styles.refero.design/style/e287e026-3433-4a1d-9b23-9a65f8b9c138)
Reference site: [https://www.stinkstudios.com](https://www.stinkstudios.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:11:06.973Z
Refero modified: 2026-06-05T11:45:17.346Z
Theme: dark
Category: Agency

## Style Summary

Explore Stink Studios's dark Agency design system: Void #000000, Bone #ffffff colors, Helvetica, Times New Roman typography, and DESIGN.md for AI agents.

North star: cinema studio at midnight - the projector hums, the room is black, only the reel glows.

## What To Borrow

- Void `#000000` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Bone `#ffffff` for Primary text, heading strokes, nav links, icon strokes, badge fills, logo type - the only high-contrast value in the system
- Soot `#050505` for Subtle tonal break from pure black for nested surfaces and hairline borders that need to feel present without breaking the dark mode
- Ember Coral `#e1695e` for Accent warmth for marquee display moments, logo gradient highlight, and select project card color treatments - borrowed from the work, never applied to UI chrome
- Burnt Sienna `#573332` for Deep warm surface for warm-toned project cards and content imagery containers - the shadow side of the coral accent

- Helvetica `--font-helvetica` for Primary workhorse - body copy at 16px/400, secondary headings at 23px/400, nav and links at 16px/400, and the massive 52px/300 hero logo treatment. Weight 300 is the default for large display: whisper-thin against the heavy black canvas creates a neon-on-velvet tension.
- Times New Roman `--font-times-new-roman` for Display serif for editorial pull-quotes and manifesto text - the 60px size with -0.05em tracking creates a fashion-magazine weight that contrasts Helvetica's geometric neutrality. Used sparingly for sentences that need gravitas.
- Courier New `--font-courier-new` for Monospace for tags, badges, index numbers, and micro-labels - the 0.10em positive tracking turns utility text into graphic texture, like film slate markings

## Avoid

- Do not introduce colored buttons, colored backgrounds, or gradient UI elements - the accent palette belongs to the work, not the chrome
- Do not use box-shadow or elevation on cards, buttons, or navigation - this system is deliberately flat; depth comes from imagery, not stacking
- Do not use rounded corners on cards or work tiles - 0px radius is the signature; rounded containers would break the cinematic frame
- Do not combine the serif display (Times New Roman) with the monospace (Courier New) on the same line or within the same component
- Do not add light-mode toggle, theme switcher UI, or alternate color schemes - dark is the only mode
- Do not use font-weight above 700 for Helvetica - the system lives in the 300-700 range; black weight would break the whisper-thin display logic
- Do not pad work cards with internal whitespace - imagery bleeds to the cell edges, and titles overlay the image directly

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
