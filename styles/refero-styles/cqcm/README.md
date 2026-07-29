# CQCM

Source: [Refero Style](https://styles.refero.design/style/12db22d6-7738-4aee-ab6b-6d6731c7e1e0) 
Reference site: [https://cqcm.coop](https://cqcm.coop) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:40:48.837Z 
Refero modified: 2026-06-03T19:59:10.805Z 
Theme: light 
Category: Other

## Style Summary

Explore CQCM's light Other design system: Cooperative Green #44d991, Civic Blue #4c92e9 colors, Athletics, Manrope typography, and DESIGN.md for AI agents.

North star: Verdant cooperative megaphone. A vivid green slab screams a civic message across a white grid while black pill buttons ground the chromatic energy.

## What To Borrow

- Cooperative Green `#44d991` for Hero panel fill, primary stat block, decorative dot overlays - the loudest brand voice; the color that makes the page feel activated
- Civic Blue `#4c92e9` for News card surfaces, secondary stat blocks - chromatic but cooler, reserved for media/content contexts rather than primary brand expression
- Sunset Coral `#ff6a51` for Accent stat block only - appears once as data emphasis, treated as a single-note punctuation rather than a system color
- Mint Whisper `#eaf9f2` for Card and nav surface tint - a barely-there green echo of the hero green, softens white space without breaking the light theme
- Ink Black `#000000` for Primary text, pill button fill, all borders and dividers - does the structural work of the system, the only color used for controls
- Paper White `#ffffff` for Page canvas, text on filled buttons, image surfaces
- Steel Gray `#666666` for Muted helper text, secondary nav borders - the only mid-gray in the system, used sparingly for de-emphasis

- Athletics `--font-athletics` for Display and badge type - used for hero headlines (48-78px), card labels, and uppercase tags. The wide letter-spacing (0.04em) is a French institutional signature that turns every headline into a civic declaration. Custom face; substitute with Archivo Black, Anton, or Druk for similar uppercase weight and tracking, or with a wide-tracked geometric like Bebas Neue for closer feel.
- Manrope `--font-manrope` for Body, navigation, button labels, and small text - the working font. Slightly opened tracking (0.01-0.011em) is a subtle departure from default; it keeps dense French text feeling breathable without becoming display-like. Pairs cleanly with Athletics because both share geometric, humanist proportions.

## Avoid

- Do not use any chromatic color as a button fill - buttons are always #000000 or outlined; color is for surfaces and decoration only
- Do not add shadows to cards, buttons, or content - the system is flat by design; the only shadow is the nav bar's soft halo
- Do not mix Athletics into body copy or Manrope into hero headlines - the font split is strict: Athletics displays, Manrope reads
- Do not use letter-spacing tighter than 0.01em on Manrope or 0.04em on Athletics - the opened tracking is part of the brand's breathable French-institutional feel
- Do not use coral (#ff6a51) more than once per surface - it is a single-note punctuation, not a system color
- Do not use square corners on buttons - pill shape (100px) is the only button geometry; cards get 8px, small elements get 4px
- Do not introduce gradients, blurs, or glass effects - the system is unapologetically flat, saturated, and solid

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
