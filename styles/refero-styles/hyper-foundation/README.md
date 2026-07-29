# Hyper Foundation

Source: [Refero Style](https://styles.refero.design/style/369ac603-c1e9-4231-9369-a198493f8e47)  
Reference site: [https://hyperliquid.xyz](https://hyperliquid.xyz)  
Captured: 2026-07-29  
Refero published: 2026-05-07T12:16:40.461Z  
Refero modified: 2026-06-03T19:20:38.028Z  
Theme: dark  
Category: Crypto

## Style Summary

Explore Hyper Foundation's dark Crypto design system: Forest Depths #072724, Midnight Tide #0f3933 colors, Teodor, Inter typography, and DESIGN.md for AI...

North star: Living emerald sanctuary a deep forest vault where a single luminous mint glow breathes through organic, shadowed forms.

## What To Borrow

- Forest Depths `#072724` as Page canvas, hero background, deep surface layer the dominant dark field that everything else floats on
- Midnight Tide `#0f3933` as Primary text on canvas, strong borders, secondary surface tint readable white-space-equivalent for dark mode
- Shadow Teal `#23524c` as Elevated surface, card fills, subtle borders one step lighter than the canvas for layer separation
- Charcoal Hairline `#2c2e33` as Subtle dividers and default 1px borders across cards, images, and icons almost invisible on the dark canvas, used for structural quietness
- Abyss Green `#122d28` as Decorative background blob deepest atmospheric tint behind organic hero shapes
- Deep Lagoon `#1c3f38` as Decorative mid-tone blob in the hero atmosphere, sits between canvas and surface
- Teodor Display and editorial headlines, brand statements, section titles. Custom serif with sharp contrast between thick and thin strokes; at 90px with 0.75 leading it creates a magazine-cover authority that is the signature typographic gesture of the site. Subheading scale at 24px carries the same character into smaller contexts. `--font-teodor` for the source typography voice
- Inter Body copy, UI labels, navigation, buttons, captions. The weight 300 default across most sizes keeps the interface quiet against the display serif the contrast between Teodor's editorial presence and Inter's whisper-light functional text is a defining rhythm of the system. `--font-inter` for the source typography voice
- source-defined base spacing with comfortable density
- Source radius system: tags 60px, cards 12px, buttons 60px, largePills 37px

## Avoid

- Do not introduce any new saturated hue the entire chromatic vocabulary is mint; adding red, blue, or yellow breaks the rarified atmosphere.
- Do not use box-shadow with gray or black tones; the only allowed shadow color is the mint glow rgba(151,252,215,0.4).
- Do not set Teodor below 24px its editorial detail collapses at small sizes and Inter should take over.
- Do not use square or 4px corner radii on interactive elements; the system is defined by 60px pill geometry.
- Do not place mint text directly on the Forest Depths canvas at small sizes without enough weight mint on dark needs at least 16px / 400 weight to read.
- Do not use the Charcoal Hairline (#2c2e33) as a visible decorative border it is for near-invisible structural hairlines only.
- Do not center-align body paragraphs; keep body text left-aligned to maintain the editorial reading rhythm.

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
