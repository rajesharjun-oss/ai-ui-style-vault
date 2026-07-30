# Scheduling

Source: [Refero Style](https://styles.refero.design/style/7ad5549e-9baa-4fda-ac43-79d568a86b98)
Reference site: [https://glossgenius.com](https://glossgenius.com)
Captured: 2026-07-30
Refero published: 2026-03-18T16:21:18.000Z
Refero modified: 2026-07-03T10:54:44.982Z
Theme: light
Category: SaaS

## Style Summary

Explore Scheduling's light SaaS design system: Gloss Black #17150e, Gloss White #f0f7f6 colors, Basel Grotesk Book, Basel Classic Book typography, and...

North star: Editorial ink on cream paper

## What To Borrow

- Gloss Black `#17150e` for Primary text, dark card surfaces, footer background, pill button fill - a warm near-black that reads softer than pure #000 and makes the large display type feel printed rather than digital; 1.5px borders and dividers - uses the same warm-black as text to keep all structural lines tonally unified
- Gloss White `#f0f7f6` for Page tint sections, card surfaces, badge fills, button text on dark - a barely-green-tinted off-white that warms the interface and creates gentle contrast bands against pure white
- Pure White `#ffffff` for Primary page canvas, card surface, dark-button text, nav link color - used wherever maximum contrast is needed without any color temperature
- Solar Yellow `#cccc25` for Yellow action color for filled buttons, selected navigation states, and focused conversion moments; Soft yellow-to-pale-yellow gradient used as decorative wash behind hero copy and section transitions
- Soft Charcoal `#272b30` for Secondary dark surface, deep section backgrounds - cooler alternative to Gloss Black for variant cards and panels
- Mid Grey `#949494` for Muted helper text, secondary labels - reserved for non-essential copy where readability is still required
- Light Coral `#ff7780` for Accent tint for decorative illustrations and marketing gradient washes - never used for UI states
- Apricot `#ffe5d6` for Soft accent fill for illustration blocks and feature card backgrounds in the marketing surface
- Apricot Glow `#ffb36a` for Warm illustration accent - pairs with Light Coral in editorial gradient compositions
- Lavender Mist `#c0c8f6` for Cool illustration accent balancing the warm Coral/Apricot pair in product showcase gradients
- Periwinkle Fade `#9fa6ff` for Periwinkle-to-lavender gradient used in product feature illustrations and decorative dividers

- Basel Grotesk Book `--font-basel-grotesk-book` for Workhorse for all UI: nav, body, buttons, badges, card copy, h2-h6 headings, and the 72px section headlines. Weight 500 is the default (heavier than typical body text) which gives the interface a confident, almost magazine-pull-quote density. The slight geometric warmth keeps it from feeling clinical.
- Basel Classic Book `--font-basel-classic-book` for Reserved exclusively for display/editorial statements at 96px+ and the 40px h1 variant. Its sharper, slightly more serifed terminals distinguish hero-level copy from section headlines - a deliberate two-voice system that signals "this is the big idea" vs "this is the next thought." Weight stays at 400 even at 144px because the tight 0.8 line-height and -0.03em tracking already create visual mass.

## Avoid

- Don't introduce drop shadows on standard cards; the system is flat by design and shadows undermine the editorial feel
- Don't use #000000 for text or fills - always warm it to #17150 to preserve the printed-ink quality
- Don't pair Basel Classic with anything below 96px; the contrast in voice collapses at smaller sizes
- Don't place yellow buttons on yellow gradient backgrounds - the CTA loses all emphasis
- Don't add a third display weight (e.g. 600) to either font; the system only uses 400 and 500
- Don't use the decorative illustration colors (Coral, Apricot, Lavender) for UI states, text, or borders - they are gradient art only
- Don't add hover shadows to buttons; use background-color or border-color transitions exclusively

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
