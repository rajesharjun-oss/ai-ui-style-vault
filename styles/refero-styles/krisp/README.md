# Krisp

Source: [Refero Style](https://styles.refero.design/style/3b3fa99e-cee4-41f3-ac26-777b4b6a8b12)
Reference site: [https://krisp.ai](https://krisp.ai)
Captured: 2026-07-31
Refero published: 2026-04-10T18:18:42.000Z
Refero modified: 2026-06-05T11:13:04.963Z
Theme: light
Category: AI

## Style Summary

Explore Krisp's light AI design system: Midnight Iris #131032, Iris Spark #614efa colors, Plus Jakarta Sans typography, and DESIGN.md for AI agents.

North star: Warm cream paper, inked in indigo, lit by a violet spark - a confident editorial-tech feel.

## What To Borrow

- Midnight Iris `#131032` for Primary text, headings, and dark section backgrounds - the deepest near-black with a violet undertone carries the same identity across both light copy and immersive dark bands
- Iris Spark `#614efa` for Filled buttons, link emphasis, active states, gradient stops - the only vivid saturated color in the palette, used as a small functional spark against the cream canvas
- Violet Mist `#dfdcfe` for Soft accent washes, tag backgrounds, decorative highlights - a near-white violet tint that echoes Iris Spark at very low intensity
- Cyan Glow `#98c8ff` for Supporting palette color for small decorative accents when the core palette needs contrast.
- Mint Whisper `#eafdfa` for Pill badge and announcement tag backgrounds - a barely-there cool tint to differentiate informational chips from the warm cream canvas
- Iris Halo `#8374fb` for Soft highlight overlays and secondary gradient midtones - a lighter violet used in multi-stop gradients
- Fog `#918f9f` for Muted body copy, helper text, secondary labels - the primary low-emphasis text color against cream and white surfaces
- Shadow `#5b5971` for Stronger secondary text, metadata - deeper than Fog for labels that need more presence without reaching Midnight Iris
- Ash `#a1a1aa` for Disabled text, placeholder content, very low-emphasis UI elements
- Slate `#1a1a22` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Charcoal `#24232d` for Secondary dark text, very dark UI elements
- Hairline `#e7e7ea` for Borders, dividers, card outlines - a cool light gray that separates surfaces on the warm cream canvas
- Silver `#cccccc` for Shadows, very subtle borders, disabled surface tones
- Snow `#ffffff` for Card surfaces, button text, dark-section text - pure white for maximum contrast on dark backgrounds
- Cloud `#f7f7f8` for Secondary surface, footer background - a cool off-white that sits one step below Snow
- Warm Paper `#f2ece2` for Dominant page canvas - a warm beige that replaces the typical cold white SaaS background, giving the entire site a tactile, editorial feel

- Plus Jakarta Sans `--font-plus-jakarta-sans` for Single-family geometric humanist sans used for every text role from 10px badges to 58px display headlines

## Avoid

- Don't introduce new saturated colors - Iris Spark is the only vivid hue, and it should appear at most 1-2 times per viewport
- Don't apply drop shadows to cards or panels - surface shifts on the Warm Paper canvas are the elevation system
- Don't use pure #000000 for text - Midnight Iris (#131032) carries the brand undertone
- Don't place white cards on white backgrounds; always layer Snow (#ffffff) on Warm Paper (#f2ece2) or Cloud (#f7f7f8) for separation
- Don't use gradients on body, heading, or subheading text - the gradient treatment is reserved for display headlines only
- Don't use border-radius larger than 8px on buttons - the 8px radius is the button signature, not pills
- Don't show customer logos in full color - they must be muted to grayscale/gray to maintain the quiet editorial feel

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
