# North Kingdom

Source: [Refero Style](https://styles.refero.design/style/145e70b3-e0a4-4fbd-8d9e-23bd93dd0021)
Reference site: [https://www.northkingdom.com](https://www.northkingdom.com)
Captured: 2026-07-30
Refero published: 2026-04-30T02:55:31.086Z
Refero modified: 2026-06-05T12:30:35.196Z
Theme: dark
Category: Agency

## Style Summary

Explore North Kingdom's dark Agency design system: Void Ink #050311, Pure White #ffffff colors, FKGroteskNeue, Arial typography, and DESIGN.md for AI agents.

North star: cinematic void with luminous type - a black film-studio soundstage where a single wordmark glows

## What To Borrow

- Void Ink `#050311` for Page canvas, section backgrounds, dark surface base - the near-black stage on which all content sits, carrying a barely-perceptible cool-violet undertone that keeps it from feeling clinical
- Pure White `#ffffff` for Primary text, headline color, hairline borders, icon strokes, button outlines - the only high-contrast voice in the system; when something needs to be seen, it is white
- Carbon Black `#000000` for Monochrome icon fills, brand marks, and high-contrast graphic details. Do not promote it to the primary CTA color
- Ash Gray `#9b9aa0` for Muted body text, secondary headings, subtle borders, disabled states - carries all secondary information without competing with the white voice
- Graphite `#44424d` for Dividers, low-emphasis borders, hairline separators between sections - quiet structural lines that organize the dark canvas without drawing attention

- FKGroteskNeue `--font-fkgroteskneue` for Universal type family - used for navigation, body, headings, badges, buttons, cards, and the massive hero wordmark. A neo-grotesque sans with tabular numerals as a deliberate feature. The single weight (400) is the system's signature: the hero 'North Kingdom' wordmark achieves its cinematic weight through sheer size, not font weight. Substitute: Space Grotesk or Inter at matching weight.
- Arial `--font-arial` for System fallback for button labels, icons, and input fields - used where the custom font license or loading constraints prevent the primary face from rendering

## Avoid

- Never introduce a chromatic brand color - the system is monochrome; color appears only inside the 3D emblem artwork
- Never use drop shadows, glows, or blur effects - depth comes from value contrast, not elevation
- Never use border-radius above 8px on cards or images - the 26px and 100px values are reserved for inputs and pills only
- Never use more than one font weight - the system speaks in a single 400 voice at varying sizes
- Never place white text on white surfaces or dark text on the void without testing contrast - the system depends on absolute clarity between two values
- Never use gradients on backgrounds - the canvas is a solid void; gradients were not detected in the system
- Never add decorative borders or ornamental elements - the aesthetic is architectural minimalism, not illustration

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
