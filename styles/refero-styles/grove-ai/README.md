# Grove AI

Source: [Refero Style](https://styles.refero.design/style/7f7d3ff7-7a74-40f1-9098-a946ce53d4d4)  
Reference site: [https://www.grovetrials.com](https://www.grovetrials.com)  
Captured: 2026-07-29  
Refero published: 2026-05-10T22:04:52.495Z  
Refero modified: 2026-06-03T20:09:22.337Z  
Theme: light  
Category: AI

## Style Summary

Explore Grove AI's light AI design system: Forest Grove #0b835c, Pine Shadow #1c2b27 colors, sans-serif, Libre Caslon Text typography, and DESIGN.md for AI...

North star: clinical journal in morning light a single green word anchors a page of measured prose

## What To Borrow

- Forest Grove `#0b835c` as Primary brand color used for the logo mark, the signature word in serif headlines, accent borders on tags and announcement pills, and small icon highlights. A deep, slightly desaturated green that reads as clinical and t...
- Pine Shadow `#1c2b27` as Secondary dark surface a near-black green-tinted shade for inverted buttons and dark surface moments where #000 would feel too harsh against the green accent
- Ink Black `#1c1c1e` as Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Graphite `#303033` as Secondary text and dividers a mid-dark gray for body copy de-emphasis, subtle borders, and metadata
- Slate Mid `#676768` as Muted helper text, inactive labels, and tertiary metadata sits at a comfortable AA contrast against white
- Mist Gray `#eff1f6` as Card surface and the only neutral fill color in the system. Creates a single elevated tier above the white canvas without introducing a new hue
- sans-serif sans-serif detected in extracted data but not described by AI `--font-sans-serif` for the source typography voice
- Libre Caslon Text Display serif used exclusively for hero-level headlines and the signature brand word. The italic-leaning contrast strokes give "Grace" and "Meet" a humanized, editorial voice that contrasts with the precise Geist below. The choice is anti-SaaS: most clinical-tech sites use a geometric sans for the hero; this serif makes the brand feel like a respected medical publication. `--font-libre-caslon-text` for the source typography voice
- 4px base spacing with comfortable density
- Source radius system: tags 9999px, cards 20px, icons 12px, inputs 8px

## Avoid

- Do not use Geist or any sans-serif for the hero headline the serif Libre Caslon Text is the brand's signature and must stay in the display slot.
- Do not apply drop shadows greater than 12px of blur; the system rejects heavy elevation in favor of hairline halos.
- Do not introduce new accent colors; the palette is monochrome plus one green, and adding blue/red/purple would dilute the clinical authority.
- Do not use #0b835c for filled buttons the dark filled button is always #1c1c1, and green is reserved for accent and small-caps labels.
- Do not center-align body paragraphs; the system reads as an editorial layout and left-alignment is non-negotiable below the hero.
- Do not use radii between 14px and 18px the system commits to either 8/12px (tight elements), 20/24px (cards), or 9999px (pills), with nothing in between.
- Do not pair the serif with bright or saturated colors other than #0b835c; any other chromatic color on the serif text breaks the signature.

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
