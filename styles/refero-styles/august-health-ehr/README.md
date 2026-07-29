# August Health EHR

Source: [Refero Style](https://styles.refero.design/style/81bd6ad6-b02b-4fb3-a600-91ecf8324171)  
Reference site: [https://www.augusthealth.com](https://www.augusthealth.com)  
Captured: 2026-07-29  
Refero published: 2026-05-11T00:39:08.258Z  
Refero modified: 2026-06-03T17:18:13.440Z  
Theme: light  
Category: SaaS

## Style Summary

Explore August Health EHR's light SaaS design system: Primary Indigo #4865ff, Deep Ink #080331 colors, Reckless Neue, Saans typography, and DESIGN.md for AI...

North star: Warm cream pharmacy with violet ink a humanist clinical surface that softens healthcare's typical sterility.

## What To Borrow

- Primary Indigo `#4865ff` as Primary action buttons, active nav state, icon accents the single saturated focal color that makes CTAs unmistakably interactive
- Deep Ink `#080331` as Headlines, body text, primary borders near-black violet that pairs warmth with the serif typeface
- Midnight Violet `#1b1463` as Navigation borders, secondary surfaces, gradient terminus darker sibling to Primary Indigo for layered depth
- Forest `#328a3b` as Green action color for filled buttons, selected navigation states, and focused conversion moments
- Ember `#ff6d39` as Tinted card surfaces, portrait frame backgrounds warm orange that signals energy and human warmth
- Blossom `#f098d7` as Tinted feature card backgrounds, hero photo frame mid-pink for category-coded surfaces
- Reckless Neue All headings and display text. A contemporary editorial serif used exclusively at weight 400 (regular) no bold. This is anti-convention: most healthtech brands use sans-serif or bold serifs; the regular-weight serif at large sizes creates a literary, trustworthy quality without shouting. Largest sizes (48-64px) anchor section headlines, while 24-32px serves subheadings. `--font-reckless-neue` for the source typography voice
- Saans Body text, UI controls, navigation, buttons, cards, labels, and everything non-headline. Weight 400 for body and descriptions, weight 500 for buttons and nav links where slight emphasis is needed. The geometric humanist sans provides clarity and warmth at small sizes, contrasting the editorial serif headings. `--font-saans` for the source typography voice
- 8px base spacing with comfortable density
- Source radius system: nav 100px, cards 16px, links 24px, badges 1600px

## Avoid

- Do not use bold (600+) weights with Reckless Neue the serif's power is in its regular weight restraint
- Do not apply cool gray shadows (rgba(0,0,0,...)) warm brown shadows are part of the visual identity
- Do not use pure white (#ffffff) as the page background cream is the base, white is for surfaces on top
- Do not use the accent colors (Forest, Ember, Blossom) for primary CTAs reserve Primary Indigo for that role
- Do not add more than two weights to any text element the system is intentionally restrained (400/500 for sans, 400 for serif)
- Do not use sharp corners (0px radius) on cards or buttons the minimum card radius is 16px, buttons are always pills
- Do not break the cream/white/tinted surface hierarchy by placing a colored accent directly on cream without a white card container
- Do not use green for success states or red for error states unless explicitly required the accent colors are decorative, not semantic

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
