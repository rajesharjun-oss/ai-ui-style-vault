# The1

Source: [Refero Style](https://styles.refero.design/style/04d2e256-61b0-4184-a834-e36c15d09ea5) 
Reference site: [https://the1.amsterdam](https://the1.amsterdam) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:54:35.309Z 
Refero modified: 2026-06-03T19:28:42.225Z 
Theme: light 
Category: Other

## Style Summary

Explore The1's light Other design system: The Green #027b49, The Pink #f19ec8 colors, KH Teka, System sans-serif typography, and DESIGN.md for AI agents.

North star: building-scale typography on painted concrete

## What To Borrow

- The Green `#027b49` for Full-bleed identity block for The Green property and any place or section it owns - deep forest green reads as architectural paint, not decoration
- The Pink `#f19ec8` for Red wash for highlight backgrounds, decorative bands, and soft emphasis behind content
- The Red `#fa4d43` for Full-bleed identity block and dramatic section background - vermillion red carries the most visual weight and anchors expanded menu states and signature moments
- The Yellow `#fbb833` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content
- Concrete `#d9d9d9` for Page canvas and primary surface - the light gray ground every screen sits on, treated as a material (concrete, drywall) rather than a neutral
- Iron `#1f1f1f` for Primary text, pill button fills, and most structural borders - near-black rather than pure black, softer on the concrete canvas while keeping max contrast
- Carbon `#000000` for Hairline borders, icon strokes, and occasional deep accents where maximum bite is needed against the colored blocks

- KH Teka `--font-kh-teka` for Primary display and heading face - the entire brand voice. Custom condensed sans set at 215px for the hero with letter-spacing -0.06em and line-height 0.70 so descenders kiss the next line and the word reads as a single architectural mass. Same family drops to 60px and 26px for sub-moments and 15-18px for in-line labels, always retaining negative tracking. This single family does every visible word on the site.
- System sans-serif `--font-system-sans-serif` for Utility micro-copy only - availability text, small annotations, fine print. Used sparingly so KH Teka remains the brand voice.

## Avoid

- Do not assign the four chromatic colors to statuses (success/error/warning/info) - they are a fixed identity set, not a semantic palette
- Do not add box-shadows, gradients, or any elevation to cards, buttons, or images - the system is ruthlessly flat
- Do not introduce a second display typeface; KH Teka is the only voice and must own every visible word
- Do not round card corners - properties and sections are full-bleed rectangles; rounding is reserved exclusively for pills (100px) and the hamburger circle
- Do not use a line-height above 1.20 anywhere; display type must be crushed to 0.70-0.80, never relaxed to 1.4-1.6 'for readability'
- Do not use #027b49, #f19ec8, #fa4d43, or #fbb833 for body text, fine print, or button fills - they are surface colors, not content colors
- Do not wrap the hero display type in a max-width container that breaks it across lines naturally; let the headline run full-bleed and break on its own terms

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
