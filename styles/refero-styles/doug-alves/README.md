# Doug-Alves

Source: [Refero Style](https://styles.refero.design/style/24c54bfb-959d-4ca3-b274-e76ba823f3c0)
Reference site: [https://dougalves.work](https://dougalves.work)
Captured: 2026-07-31
Refero published: 2026-04-30T03:54:44.268Z
Refero modified: 2026-06-05T10:01:32.630Z
Theme: mixed
Category: Design

## Style Summary

Explore Doug-Alves's mixed Design design system: Espresso #1d1610, Graphite #282828 colors, Inter, wtqc typography, and DESIGN.md for AI agents.

North star: Oversized typographic monolith on warm charcoal

## What To Borrow

- Espresso `#1d1610` for Hero and dark section background - warm-tinted near-black reads as architectural, not as raw #000, giving the oversized display type a gallery-wall feel
- Graphite `#282828` for Primary body text, structural borders, section dividers - the workhorse neutral that draws the hairline rules and most interface lines
- Slate `#333333` for Secondary body and heading text - slightly lighter than Graphite, used for headings and emphasized body copy where Graphite is reserved for borders
- Obsidian `#000000` for Display headings on light sections and pure-black accents - used sparingly for maximum impact on the white About and Latest sections
- Paper `#ffffff` for Content section surfaces and inverted text on dark hero - the bright surface that the warm espresso sections cut against
- Bone `#fff5f2` for Warm off-white page canvas - subtle pink-ivory tint replaces plain white as the base, keeping the entire palette on the warm side of neutral

- Inter `--font-inter` for Primary body and UI text. The 18px body size with 1.78 line-height creates a generous, editorial reading rhythm that contrasts the compact, tight display type. The 0.89 line-height variant handles single-line labels and metadata where vertical density matters.
- wtqc `--font-wtqc` for Signature display and heading face. The massive 197px/72px/28px scale at weight 300 with tight tracking (-0.033em -0.014em) creates the poster-art identity. At 300 weight, headlines whisper rather than shout - authority through scale and restraint, not boldness. The lighter weight prevents the enormous letterforms from feeling heavy or aggressive.
- System UI (-apple-system) `--font-system-ui-apple-system` for Tertiary fallback for cards, metadata blocks, and system-level UI that doesn't carry brand typographic weight
- -apple-system `--font-apple-system` for -apple-system - detected in extracted data but not described by AI
- Roboto `--font-roboto` for Roboto - detected in extracted data but not described by AI

## Avoid

- Don't add a brand accent color. The system is monochrome by design - introducing a blue or red CTA breaks the editorial identity.
- Don't use border-radius above 0px on UI elements (buttons, cards, dividers, tags). The single 20px radius applies only to image containers. Sharp corners are the rule.
- Don't set display type above weight 400. The 300 weight whispers - bolding it turns a poster into a billboard.
- Don't use drop shadows, glows, or blur effects. Elevation is communicated through contrast (dark on light, light on dark) and the hairline border system, never through shadow.
- Don't add decorative gradients. The palette is flat - gradients introduce a visual register the system doesn't support.
- Don't set body text below 16px. The 18px body is paired with massive display type; shrinking body to 12-14px breaks the hierarchy rhythm.
- Don't add icons to body content, navigation, or section headers. The refresh icon in the hero is the only icon in the system - all other structure is pure typography.

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
