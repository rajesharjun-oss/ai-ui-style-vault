# Pangram Pangram Foundry

Source: [Refero Style](https://styles.refero.design/style/6d64a4da-ef40-453e-86f7-4bfabc0c9051)
Reference site: [https://pangrampangram.com](https://pangrampangram.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:33:11.444Z
Refero modified: 2026-06-05T11:30:46.711Z
Theme: light
Category: Design

## Style Summary

Explore Pangram Pangram Foundry's light Design design system: Ember Orange #ff2f00, Marble White #fafafa colors, Neue Montreal, Neue Montreal Semibold...

North star: Museum vitrine on white marble. A gallery-style type foundry where the canvas is bare stone, the lighting is flat daylight, and the only vivid color is a single orange-red label used by a curator to flag what is new.

## What To Borrow

- Ember Orange `#ff2f00` for Orange action color for filled buttons, selected navigation states, and focused conversion moments.
- Marble White `#fafafa` for Page canvas, card surfaces, input fields, default panel backgrounds. The dominant surface tone, barely off-white for warmth
- Stone Gray `#ededed` for Secondary surface for filled buttons, muted card backgrounds, image placeholder fills. One step deeper than Marble White to create gentle separation without contrast
- Graphite `#666666` for Secondary text, link color, subdued metadata, helper text. Reads as muted black - never used for primary text or headings
- Ink Black `#000000` for Primary text, all headings, hairline borders (cards, lists, badges, inputs), icons, navigation. The structural backbone - 1px borders everywhere define the system
- Signal Yellow `#ffb700` for Yellow state accent for badges, validation surfaces, and short status labels.
- Ice Blue `#bfe0ff` for Blue state accent for badges, validation surfaces, and short status labels.

- Neue Montreal `--font-neue-montreal` for The workhorse and display face. Weight 400 for body, weight 530 for subheads and medium emphasis, weight 600 for headings and display overlays. Used at 145px for hero type, 48px for section headlines, 18-20px for body, 14px for navigation, 12px for badges. The type IS the product - this single family carries the entire brand voice.
- Neue Montreal Semibold `--font-neue-montreal-semibold` for Heavy display variant used for the largest typographic moments in specimen cards. Tighter, more compressed than standard weight 600.
- Neue York `--font-neue-york` for Companion serif/contrast face shown in specimen contexts. The 700 weight provides a sharp counterpoint to the geometric Montreal.
- Frama Semibold `--font-frama-semibold` for Specimen showcase weight - displayed at exact 103px in the grid to demonstrate each family's character at scale.
- Kyoto Semibold `--font-kyoto-semibold` for Specimen showcase - fixed 103px display size in the font grid.
- Neue Gstaad Bold `--font-neue-gstaad-bold` for Specimen showcase - fixed 103px display size in the font grid.
- Palma Fizzy Heavy `--font-palma-fizzy-heavy` for Specimen showcase - fixed 103px display size in the font grid.
- Mori Bold `--font-mori-bold` for Specimen showcase - fixed 103px display size in the font grid.
- Museum Light `--font-museum-light` for Specimen showcase - the 300 weight in the grid is deliberately whisper-light, making weight 300 headlines read as anti-convention: authority through restraint rather than volume.
- Neue Corp Semibold `--font-neue-corp-semibold` for Specimen showcase - fixed 103px display size in the font grid.
- Watch Medium `--font-watch-medium` for Specimen showcase - fixed 103px display size in the font grid.
- Monument Narrow Medium `--font-monument-narrow-medium` for Specimen showcase - fixed 103px display size in the font grid.
- Model Plastic Regular `--font-model-plastic-regular` for Specimen showcase - fixed 103px display size in the font grid.
- neue-gstaad-normal-bold `--font-neue-gstaad-normal-bold` for neue-gstaad-normal-bold - detected in extracted data but not described by AI
- neue-corp-normal-semibold `--font-neue-corp-normal-semibold` for neue-corp-normal-semibold - detected in extracted data but not described by AI
- neue-york-normal-normal-bold `--font-neue-york-normal-normal-bold` for neue-york-normal-normal-bold - detected in extracted data but not described by AI

## Avoid

- Do not use #ff2f00 for body text, headings, or large surfaces - its role is badge/punctuation only
- Do not apply box-shadow or heavy elevation - the system relies on 1px borders and whitespace, not depth
- Do not use radius values other than 20px (cards/buttons/inputs) and 999px (badges) - the rounded softness is signature
- Do not use colors other than the defined palette - no decorative blues, greens, or purples for UI chrome
- Do not use multiple type families in the same view - Neue Montreal carries everything except specimen showcases
- Do not set line-height above 1.30 for any size - the tight leading is essential to the editorial feel
- Do not center body text or metadata - only headlines and hero type use center alignment

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
