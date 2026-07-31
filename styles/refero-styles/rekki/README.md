# REKKI

Source: [Refero Style](https://styles.refero.design/style/65b8df27-36a3-47a6-be53-735d1f6a485d)
Reference site: [https://rekki.com](https://rekki.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:49:13.198Z
Refero modified: 2026-06-05T09:12:30.728Z
Theme: dark
Category: SaaS

## Style Summary

Explore REKKI's dark SaaS design system: Signal Blue #0063e1, Obsidian #000000 colors, sans-serif, Diatype REKKI typography, and DESIGN.md for AI agents.

North star: Mission control dashboard in a darkroom

## What To Borrow

- Signal Blue `#0063e1` for Primary CTA fill, active nav indicator, brand accent dots, link highlights - the single chromatic voice in an otherwise silent monochrome system
- Obsidian `#000000` for Page canvas, dominant background, hairline divider color, icon fill - the floor of the entire system
- Carbon `#040910` for Card surface base, deep panel backgrounds - first step above the page canvas
- Graphite `#0d0d0d` for Elevated card surfaces, section backgrounds, border fills - the mid-surface layer
- Iron `#1f1f1f` for Input field backgrounds, form controls, tertiary surfaces
- Steel `#2b2c2e` for Highest card elevation, modal surfaces, hover-state surfaces - the ceiling of the surface stack
- Ash `#858585` for Body text, muted labels, secondary borders, link underlines - the workhorse neutral for non-heading text
- Smoke `#979797` for Icon strokes, tertiary button borders, low-priority text
- Fog `#8c8c8c` for Link text, subdued navigation labels
- Paper `#ffffff` for Light neutral action fill for buttons on dark surfaces.

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Diatype REKKI `--font-diatype-rekki` for Primary brand typeface - body text at 16-20px weight 400, large headlines at 56-86px weight 400 with aggressive negative tracking (as tight as -0.064em at 86px). The whisper-weight headlines are signature: no bold shouting, just precise geometric calm. Subheadings/nav at 16-20px weight 400-600.
- Diatype REKKI Bolder Rounded `--font-diatype-rekki-bolder-rounded` for Display variant for the most prominent brand moments - heavier geometric terminals, used sparingly at 72px for hero declarations and at 12-20px weight 700 for emphasis labels in nav/inputs.
- OCD-GARRI `--font-ocd-garri` for Secondary utility face - likely for product UI labels, status indicators, or monospaced-feeling tabular data within the embedded product screenshots. Carries slight positive letter-spacing (0.033-0.038em) giving it a structured, instrument-label quality.
- Diatype REKKI Regular `--font-diatype-rekki-regular` for Diatype REKKI Regular - detected in extracted data but not described by AI
- Inter `--font-inter` for Inter - detected in extracted data but not described by AI

## Avoid

- Never use multiple chromatic accent colors - the system is monochromatic + one blue; introducing green, red, or purple breaks the entire visual language
- Never apply drop shadows to cards or panels; the inset white border IS the elevation system
- Never set body text below #858585 contrast against the black canvas; use Paper #ffffff for any text that needs to be read at a glance
- Never use bold (700) weights for headlines; Diatype REKKI weight 400 at large sizes with tight tracking is the signature - bolding destroys it
- Never use letter-spacing greater than 0em on display type; the negative tracking is what makes the headlines feel architectural
- Never place white or light-colored cards on the dark canvas; all surfaces must stay in the black-to-charcoal range
- Never use rounded images or organic shapes for the logo or brand mark - the geometry is angular and precise

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
