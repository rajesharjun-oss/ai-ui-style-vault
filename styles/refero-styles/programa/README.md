# Programa

Source: [Refero Style](https://styles.refero.design/style/41af8353-6a8f-416d-947b-57932f591497)  
Reference site: [https://programa.design](https://programa.design)  
Captured: 2026-07-29  
Refero published: 2026-04-30T00:43:24.577Z  
Refero modified: 2026-06-05T08:01:42.145Z  
Theme: light  
Category: Design

## Style Summary

Explore Programa's light Design design system: Ink Black #1a1a1a, Paper White #ffffff colors, Neue Haas Grotesk Text, neue-haas-grotesk-text typography, and...

North star: Swiss design studio at high noon. A white gallery wall lit by a single yellow desk lamp everything is grayscale until a button, badge, or highlight demands attention, and then that one yellow note carries the whole room.

## What To Borrow

- Ink Black `#1a1a1a` as Primary text, all borders, icon strokes, logo, divider lines, button outlines the structural ink that defines every shape on the page
- Paper White `#ffffff` as Page canvas, card surfaces, text on dark fills, input fields
- Fog Gray `#f4f4f4` as Soft section background, alternate surface, and quiet card fill
- Ash Gray `#a3a3a3` as Muted secondary text, inactive links, placeholder copy, tertiary metadata
- Highlighter Yellow `#fbff2b` as Primary action background, focus highlights, tag fills the single chromatic accent that makes interactive elements feel switched on against the monochrome system
- Neue Haas Grotesk Text The single typeface carries every voice on the site nav, body, headings, buttons, inputs. Weight 400 is the default for body and nav; weight 500 is reserved for emphasized inline labels (e.g. 'Last Updated:') and section opens. The choice of a neo-grotesque with consistent -0.03em tracking at every size creates optical tightness even at 42px, avoiding the airy looseness most sans-serifs default to. This is a Swiss-tool typeface, not a personality typeface restraint is the signature. `--font-neue-haas-grotesk-text` for the source typography voice
- neue-haas-grotesk-text neue-haas-grotesk-text detected in extracted data but not described by AI `--font-neue-haas-grotesk-text` for the source typography voice
- 6px base spacing with comfortable density
- Source radius system: nav 10px, cards 16px, inputs 10px, buttons 10px

## Avoid

- Don't introduce drop shadows, glow effects, or blur elevation is flat and border-defined.
- Don't use #fbff2b on more than one element per viewport its power comes from scarcity.
- Don't add a second accent color; the palette is monochrome + one yellow-green signal.
- Don't use Ash Gray (#a3a3a3) for body copy it's a 2.5:1 contrast fail on white; reserve it for placeholders and inactive metadata only.
- Don't increase border-radius above 16px the slightly squared geometry is part of the identity.
- Don't break the 6px spacing grid with arbitrary pixel values; every gap should be a multiple of 6.
- Don't add a subtitle or eyebrow text above page headings the 42px heading stands alone.

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
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
