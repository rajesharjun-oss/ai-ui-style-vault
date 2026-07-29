# Alpine Bio

Source: [Refero Style](https://styles.refero.design/style/1995b916-d3f1-4b13-8eb0-c1317ab63ccb) 
Reference site: [https://alpbio.com](https://alpbio.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T22:34:41.324Z 
Refero modified: 2026-06-03T22:08:59.611Z 
Theme: light 
Category: Other

## Style Summary

Explore Alpine Bio's light Other design system: Parchment #f5f5f5, Warm Cream #f8f4e6 colors, Switzer, Geist typography, and DESIGN.md for AI agents.

North star: Sun-drenched botanical apothecary on cream parchment

## What To Borrow

- Parchment `#f5f5f5` for Page canvas and base background - the neutral ground everything sits on
- Warm Cream `#f8f4e6` for Section backgrounds, footer surface, and warm page rhythm - gives the system its apothecary warmth
- Paper White `#ffffff` for Text on dark imagery, elevated card surfaces, and bright contrast moments
- Mist Gray `#e9e9e9` for Subtle surface fills - nav background, button hover rests, and quiet UI layers
- Ink `#1e1e1f` for Primary body text and structural borders - softer than pure black, warmer against the cream
- Carbon `#000000` for Heading text, heavy borders, icon strokes - the highest-contrast neutral in the system
- Sky Blue `#8ec7e2` for Blue wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Pollen Yellow `#f7ca50` for Highlight labels, breadcrumb tags, scroll-indicator text - rare warm punctuation against the cream

- Switzer `--font-switzer` for Display and heading type - geometric sans with consistent tight tracking, carries the editorial voice from 20px subheads up to 76px hero headlines
- Geist `--font-geist` for Body and intermediate type - comfortable reading at 15-18px, scales up to 42px for feature sub-heads
- PT Mono `--font-pt-mono` for Nav items, category labels, and small uppercase tags - the only monospace, used to signal nav/system elements distinct from editorial body
- system sans-serif `--font-system-sans-serif` for Micro-copy and fallback - only appears at 12px in utility positions

## Avoid

- Don't add drop shadows to cards, buttons, or modals - the system is intentionally flat, depth comes from surface color only
- Don't introduce new chromatic colors - the palette is sky blue + pollen yellow + warm neutrals, nothing else
- Don't use the pollen yellow as a CTA or button background - it's a typographic accent only
- Don't center content in a max-width container for body sections - the editorial feel depends on left-aligned, edge-to-edge composition
- Don't use type weights above 500 - Switzer and Geist at 400-500 carry the whole system, bolder weights would break the quiet tone
- Don't apply borders to the Primary Pill Button - it relies on the sky-blue fill alone for its identity
- Don't use dark mode - the entire system is calibrated around the cream canvas; inverting it would destroy the apothecary warmth

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
