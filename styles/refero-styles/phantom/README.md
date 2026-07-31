# Phantom

Source: [Refero Style](https://styles.refero.design/style/6144c3ae-fc57-4efe-b6ed-2b5eab2dc108)
Reference site: [https://phantom.com](https://phantom.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:42:02.869Z
Refero modified: 2026-06-05T07:46:32.660Z
Theme: mixed
Category: Crypto

## Style Summary

Explore Phantom's mixed Crypto design system: Aubergine #3c315b, Ghost Lavender #e2dffe colors, Phantom typography, and DESIGN.md for AI agents.

North star: lavender candy shop at dusk. A monochromatic violet world where everything is a soft pill on a near-white plane, interrupted by a mischievous ghost and pastel highlights.

## What To Borrow

- Aubergine `#3c315b` for Primary brand - navigation borders, nav text, heading text, card surfaces in dark sections, icon strokes. The structural spine of the entire system
- Ghost Lavender `#e2dffe` for Primary action - filled CTA button background, violet glow shadow on buttons. The light-on-light button that only reveals its presence through a soft 4px halo
- Periwinkle `#ab9ff2` for Secondary action - brighter lavender for secondary CTAs, decorative fills, icon accents. Adds saturation to the pale-violet world
- Cornflower Pop `#4a87f2` for Accent button - occasional vivid blue button for emphasis or differentiation. Use sparingly as a high-energy interruption
- Buttercream `#ffffc4` for Accent button - pale yellow button fill for variety in multi-action contexts. Pastel punctuation in the candy palette
- Blush Mist `#ffdadc` for Accent button - near-gray pink button for warmth and tonal range. The softest of the pastel set
- Mint Signal `#2ec08b` for Success badge - vivid green for status indicators, positive confirmations, live signals
- Paper White `#fdfcfe` for Canvas - page background, card surfaces, button borders, text on dark backgrounds. Near-white with the faintest cool tint
- Obsidian `#1c1c1c` for Body text, heading text on light backgrounds, button borders, card borders. The near-black ink for all foreground content
- Fog `#86848d` for Muted text, icon strokes, secondary nav borders. The quiet gray for non-emphasized elements
- Ash `#e9e8ea` for Button background, subtle surface fill. The neutral pale surface beneath lavender hero panels
- Bone `#f4f2f4` for Surface background - light section panels, button fills. The warmest of the near-white neutrals

- Phantom `--font-phantom` for Custom typeface used for everything. Weight 350 is the default body and display weight - unconventional lightness creates an airy, anti-bold personality. Weight 400 reserved for body copy that needs slightly more presence. Sizes scale dramatically from 13px caption to 96px display. Tight -0.025em letter-spacing at all sizes creates compressed, high-density headlines. Line-height collapses to 1.0-1.1 at display sizes for sculptural headline forms.

## Avoid

- Don't use drop shadows beyond the single 4px violet glow on primary CTAs - the system stays flat
- Don't set text at weight 600+ - the 350 whisper-weight is the brand's voice, not a choice for emphasis
- Don't use sharp corners under 16px - the world is pills and soft capsules
- Don't introduce saturated colors outside the pastel accent set (#4a87f2, #ffffc4, #ffdadc) - the palette is intentionally narrow
- Don't set body text larger than 16px weight 400 or use line-height above 1.4 - readability rules apply but stay restrained
- Don't use high-contrast decorative elements like gradients, patterns, or backgrounds images - surface is always flat color
- Don't add border-radius values below 24px on cards or 16px on smaller elements - every container should feel soft

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
