# Franco Maria Ricci Editore

Source: [Refero Style](https://styles.refero.design/style/6120469b-a1c8-46d3-b7fd-8aa6dc22c0d9)
Reference site: [https://www.francomariaricci.com/en](https://www.francomariaricci.com/en)
Captured: 2026-07-31
Refero published: 2026-04-30T02:49:19.178Z
Refero modified: 2026-06-05T10:37:08.420Z
Theme: light
Category: E-commerce

## Style Summary

Explore Franco Maria Ricci Editore's light E-commerce design system: Vellum White #f6f6f6, Paper #ffffff colors, BodoniSvntytwoITCStd-Book,...

North star: Art Deco gallery catalogue - burnished gold hairlines on bone-white vellum

## What To Borrow

- Vellum White `#f6f6f6` for Page canvas - the warm off-white that grounds every section, never pure #ffffff so type never feels clinical
- Paper `#ffffff` for Card and section surfaces - book spreads, product panels, inset blocks sitting one shade above the vellum canvas
- Gallery Ink `#0a0a0a` for Dark sections (FMR Magazine block, footer band) and deepest typographic emphasis - reads as letterpress black, not screen black
- Letterpress Black `#000000` for Body copy, navigation text, icons, all hairlines and borders, pagination marks - the structural ink of the system
- Silver Wash `#b3b3b3` for Muted surface for secondary hero panels and quiet tonal breaks - used sparingly as a gallery-shadow gray
- Burnished Gold `#bc9c5c` for Section header underlines, link hover rules, decorative title borders - the only chromatic voice in the system, applied as 1px strokes and inline rules, never as fill

- BodoniSvntytwoITCStd-Book `--font-bodonisvntytwoitcstd-book` for Primary voice - every editorial moment. 42px with line-height 0.95 for the cinematic display headline (the tight leading lets the tall Bodoni capitals lock together as a single typographic object). 22px for section openers. 18px and 16px for body and book metadata. 14px and 12px for navigation, captions, and the monogrammed fine print. Substitute: Bodoni Moda, Bodoni 72, or Playfair Display when the ITC cut is unavailable.
- BodoniSvntytwoITCStd-BookIt `--font-bodonisvntytwoitcstd-bookit` for Editorial italics for the signature flourish - "Editore" wordmark, italic section titles like OUR SELECTION, and the quiet poetic asides. The italic is used as ornament, not emphasis: a single italic line beside a roman headline changes the register of the whole spread. Substitute: Bodoni Moda Italic, Playfair Display Italic.
- Arial `--font-arial` for System utility for pagination counters (2/5), shipping notices, form labels, and the rare inline metadata. Arial sits beside Bodoni as a quiet functional label - the contrast between high-contrast serif and neutral sans is the only typographic tension the system permits. No tracking adjustments; letterspacing inherits from the browser default.

## Avoid

- Do not introduce drop-shadows, blurs, or glow effects. The system is flat; elevation is tonal.
- Do not use Burnished Gold (#bc9c5c) as a background fill on buttons, badges, or surfaces. It is a stroke color only.
- Do not round any corner. Buttons, cards, inputs, images all keep 0px radius.
- Do not use any secondary accent color. The palette is monochrome + one gold; introducing red, blue, or green would destroy the letterpress discipline.
- Do not use Arial for headlines or editorial copy. Arial is reserved for pagination counters, form labels, and utility metadata.
- Do not set line-height above 0.95 on the 42px display headline - the tight leading is signature, not an oversight.
- Do not add hover animations, transitions, or micro-interactions. The page reads as a printed catalogue; movement would break the metaphor.

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
