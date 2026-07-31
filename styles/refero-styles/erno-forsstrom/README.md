# Erno Forsstrom

Source: [Refero Style](https://styles.refero.design/style/cffa5959-4283-41d2-ad11-bada2d731419)
Reference site: [https://erno.works](https://erno.works)
Captured: 2026-07-31
Refero published: 2026-04-30T03:35:48.728Z
Refero modified: 2026-06-05T12:07:06.239Z
Theme: light
Category: Agency

## Style Summary

Explore Erno Forsstrom's light Agency design system: Ink #202020, Bone #dfdcdc colors, NB Akademie Pro typography, and DESIGN.md for AI agents.

North star: editorial gallery on warm paper

## What To Borrow

- Ink `#202020` for Body text, headings, project titles, hairline borders, and the bottom edge of links - a soft near-black that reads as flat black at body sizes but never goes dead 000
- Bone `#dfdcdc` for Page canvas and the implicit surface for every project card - a warm off-white with just enough gray to feel like paper, not a screen
- Ash `#cdcecf` for Hairline divider tone that sits one step darker than the canvas to register as a visible rule without becoming a hard line

- NB Akademie Pro `--font-nb-akademie-pro` for The only font in the system, used at a single weight across every role. 58px at 0.93 line-height carries the hero - lines overlap slightly, creating editorial density. 43px at 1.10 serves medium section heads. 21px at 1.33 is the body, nav, labels, and project metadata - a single typographic voice at conversational size. The 'tnum' feature is active sitewide, forcing tabular figures in any year label or date.

## Avoid

- Don't add a CTA button, a colored accent, or a filled background - this system has no primary action surface
- Don't round image corners, add drop shadows, or apply any elevation to project cards
- Don't introduce a second typeface, a serif companion, or a different weight of NB Akademie Pro
- Don't use white (#ffffff) as the canvas - #dfdcdc is the signature warm paper tone
- Don't break the three-size type scale (21 / 43 / 58) with intermediate steps; the gap between sizes is the hierarchy
- Don't underline links by default - use the bottom border in #202020 only on hover/active to signal interaction
- Don't add gradients, colored badges, tags, or status pills - the system is strictly two-color

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
