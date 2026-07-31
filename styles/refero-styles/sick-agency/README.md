# SICK AGENCY

Source: [Refero Style](https://styles.refero.design/style/9ff03bd9-2ce0-474c-8c73-1905dbacc23b)
Reference site: [https://sick.agency](https://sick.agency)
Captured: 2026-07-31
Refero published: 2026-04-30T03:01:07.011Z
Refero modified: 2026-06-05T08:26:17.033Z
Theme: mixed
Category: Agency

## Style Summary

Explore SICK AGENCY's mixed Agency design system: Voltage Yellow #ffc700, Radioactive Orange #ff4e27 colors, Morganite, Thunder typography, and DESIGN.md...

North star: Loud printed broadside on a brick wall - a maximalist zine spread screaming from a screen.

## What To Borrow

- Voltage Yellow `#ffc700` for Primary section background and dominant display text color. Headings, borders, and full-bleed canvas bands. Carries the highest visual weight on the page
- Radioactive Orange `#ff4e27` for Secondary section background and accent border color. Outlined action borders, dividers, icon strokes, and full-bleed canvas bands that create contrast with the yellow
- Electric Cobalt `#0029ff` for Primary action background and tertiary section background. The only filled button color in the system; also used for full-bleed canvas bands and decorative sticker badges
- Burnt Sienna `#4d170c` for Error and warning state. Input border in invalid state. Reads as a deep brick-red against the lighter orange, preserving the system's warm-color vocabulary
- Ink Black `#000000` for Body text on light/yellow backgrounds, and the dominant border color across all surface bands. Functions as a hairline outline and text color wherever contrast is needed against yellow or white
- Bone White `#ffffff` for Body text and button text on cobalt and orange surfaces. The inverse of Ink Black - the two together carry all foreground-to-background contrast in the system

- Morganite `--font-morganite` for Hero display face for the single largest typographic statement per page. The extreme 0.70 line-height stacks letterforms with no air between lines - type is treated as a solid block, not a paragraph. This face defines the agency's shock-value identity.
- Thunder `--font-thunder` for Secondary display face used at near-hero scale. The light weight is anti-convention for a 122px headline - most agencies use 700-900 here. Thunder's 300 whispers while still occupying monumental space, creating tension between volume and restraint. Substituted by ITC Avant Garde Gothic, Futura, or any geometric humanist sans.
- Sentient `--font-sentient` for Workhorse text face for body copy, buttons, inputs, links, and small labels. Carries tight negative tracking (-0.0100em to -0.0200em) even at body sizes, which is a serif's signature in a sans-dominated layout. Substituted by any transitional serif.
- Times `--font-times` for Fine-print and micro-label face for legal text, tiny annotations, and icon-adjacent micro-copy. Its system-serif feel is a deliberate contrast to the custom display faces, creating a visual fossil-record effect.

## Avoid

- Do not introduce grays, off-whites, beige, or any desaturated color into the system - neutrals are only #000000 and #ffffff, used for text and borders.
- Do not add box-shadow, drop-shadow, or blur to any element - depth comes from color contrast between full-bleed bands, never from elevation.
- Do not use rounded corners (4px, 8px, 16px) on cards, sections, or containers - sharp 0px corners and 999px pills are the only two radii allowed.
- Do not set display type below 80px or set body type above 24px - the gap between body and display is what creates the broadside scale, and closing it destroys the system.
- Do not use Morganite 900 with line-height above 0.80 - its identity depends on near-touching stacked lines; looser leading would turn it into a generic display face.
- Do not place a primary action button on a white or near-white background - the system has no white surface; buttons live on yellow, orange, or cobalt fields.
- Do not use photographic backgrounds, gradients, or textures - surfaces are always flat solid color.

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
