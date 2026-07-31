# Pastel

Source: [Refero Style](https://styles.refero.design/style/409d92b9-00a8-4e21-a430-ab95ea48204f)
Reference site: [https://usepastel.com](https://usepastel.com)
Captured: 2026-07-31
Refero published: 2026-02-27T09:29:23.000Z
Refero modified: 2026-06-05T07:34:18.584Z
Theme: light
Category: SaaS

## Style Summary

Explore Pastel's light SaaS design system: Paper Stone #f5f5f4, Chalk #e6e3e2 colors, Figtree, Inter typography, and DESIGN.md for AI agents.

North star: Quiet paper notebook with one vivid ink stamp

## What To Borrow

- Paper Stone `#f5f5f4` for Light supporting surface for subtle backgrounds and section separation.
- Chalk `#e6e3e2` for Secondary card surface, subtle section bands one step above canvas
- Ink Black `#111111` for Primary headings, body text, icon strokes - the dominant text and graphic color across all contexts
- Graphite `#222222` for Secondary headings, card titles, slightly softer than Ink Black for hierarchical depth
- Fog Gray `#78716b` for Muted helper text, icon hints, tertiary metadata - warm gray that sits naturally on Paper Stone
- Smoke `#646464` for Secondary icon color, disabled-adjacent UI elements
- Ice Line `#d1dee8` for Hairline borders, card outlines, structural dividers - cool blue-tinted gray that distinguishes borders from text
- Ash `#d7d3d1` for Subtle link underlines, very light decorative borders
- Charcoal Block `#45403c` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Pure White `#ffffff` for Button text on dark or accent surfaces, inverse text on dark blocks
- Cobalt Stamp `#165dfb` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color

- Figtree `--font-figtree` for Sole display and text family. 58px/45px/35px carry weight 500-600 for headlines with -0.016em tracking that pulls characters tight; 18-21px at weight 400-500 is the body and subheading range; 14-16px at weight 400-500 is caption and small UI. Negative letter-spacing scales with size - tighter at display, near-zero at body. The geometric humanist shapes of Figtree (rounded but not soft) match the 8.8px corner radius system.
- Inter `--font-inter` for Secondary micro-copy context only (appears in 6 instances at 14px) - treat as fallback/utility, not a display voice. Figtree handles all visible brand communication.

## Avoid

- Don't introduce additional accent colors - the system is 1% colorful by design; a second chromatic hue breaks the 'one stamp' identity
- Don't use pure #000000 - Ink Black is #111111, Graphite is #222222, Charcoal Block is #45403c; always retain the warm undertone
- Don't add box-shadows to cards or buttons - the design uses flat surfaces with hairline borders as its elevation language
- Don't round corners to 12px, 16px, or 9999px for cards or buttons - 8.8px is a deliberate, non-standard value that defines the system
- Don't use letter-spacing 0 or positive values on headlines - negative tracking at 35px and above is a signature of this system
- Don't use Cobalt Stamp for large text blocks, section backgrounds, or illustration fills - it loses urgency when used at scale
- Don't use Inter for display or body copy - Figtree is the only visible brand voice; Inter is a utility fallback

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
