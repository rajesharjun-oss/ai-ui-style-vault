# Evernote

Source: [Refero Style](https://styles.refero.design/style/0c0b6140-2b6c-44f8-8bba-4ecfcadba420) 
Reference site: [https://evernote.com](https://evernote.com) 
Captured: 2026-07-29 
Refero published: 2026-04-30T00:53:00.105Z 
Refero modified: 2026-06-05T06:14:55.638Z 
Theme: light 
Category: Productivity

## Style Summary

Explore Evernote's light Productivity design system: Lime Sprout #94e130, Paper Cream #f9f6f2 colors, Figtree, Inter typography, and DESIGN.md for AI agents.

North star: Afternoon sun on cream paper - a warm, lived-in notebook where white cards float on beige, dark text breathes, and one lime-green highlighter marks the important things.

## What To Borrow

- Lime Sprout `#94e130` for Primary action button, icon highlights, accent tags - the singular chromatic punctuation that makes actions feel switched on against the cream canvas
- Paper Cream `#f9f6f2` for Page canvas, hero background, section backgrounds - warm off-white that replaces standard white with a paper-like quality
- Ivory Card `#f4eee5` for Alternate card surface, warm-toned elevated panels that sit one step deeper than the cream canvas
- Pure White `#ffffff` for Elevated card surfaces, product screenshot containers, button text on dark fills
- Slate Border `#e7e7e7` for Card borders, hairline dividers between content sections and list items
- Smoke `#a1a1a1` for Muted link borders, nav underlines, subtle structural dividers
- Stone `#737373` for Helper text, tertiary body content, subdued annotations
- Graphite `#4e4d4c` for Secondary text, icon strokes, subdued UI labels
- Iron `#262626` for Dark surface elements, body borders on inverted sections
- Charcoal `#141414` for Primary text, dark filled buttons, heading color - the near-black that carries all weight in the type system
- Onyx `#000000` for Maximum-contrast borders, footer rules, SVG fills where absolute black is needed

- Figtree `--font-figtree` for Primary typeface across all UI - display, headings, body, nav, buttons. Weight 300 at 72px hero is a signature choice: whisper-light headlines that feel editorial and confident rather than bold-and-shouting. The geometric humanist forms of Figtree at 300 weight give the warm cream canvas a modern editorial feel.
- Inter `--font-inter` for Secondary body text at 16-20px, likely fallback or supplementary paragraph copy. Used sparingly alongside Figtree for longer-form descriptive text.

## Avoid

- Don't use pure white #ffffff as a page background - it breaks the warm paper system
- Don't apply weight 600 or above to display headlines - weight 300 is the signature, heavier weights feel corporate
- Don't use Lime Sprout for large background fills, gradients, or decorative bands - it loses its energy when used at scale
- Don't add drop shadows to cards - the system relies on flat hairline borders (#e7e7e7) for separation, not elevation
- Don't use fully rounded (9999px) buttons - 5px is the intentional subtle rounding, not pill-shaped
- Don't introduce more than one additional accent color per screen - the cream + charcoal + lime triad is the system
- Don't use letter-spacing looser than -0.03em on headings - the tight tracking is what makes the large type feel modern rather than textbook

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
