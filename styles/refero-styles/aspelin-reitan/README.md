# Aspelin Reitan

Source: [Refero Style](https://styles.refero.design/style/3a331157-f5a5-4640-ada8-8a3ad262ee6a) 
Reference site: [https://www.aspelineiendom.no](https://www.aspelineiendom.no) 
Captured: 2026-07-29 
Refero published: 2026-05-11T00:08:46.760Z 
Refero modified: 2026-06-03T21:33:24.660Z 
Theme: light 
Category: Other

## Style Summary

Explore Aspelin Reitan's light Other design system: Warm Parchment #ffebd0, Candlelight #fff8e9 colors, ModernEra typography, and DESIGN.md for AI agents.

North star: Candlelit architectural archive - the page reads like a portfolio of built places pinned to a warm cream wall, with a single line of white type floating over each full-bleed image.

## What To Borrow

- Warm Parchment `#ffebd0` for Gray accent for outlined action borders, linked labels, and lightweight interactive emphasis.
- Candlelight `#fff8e9` for Lighter cream for elevated surfaces and secondary text on dark - a half-step above Parchment for subtle layering
- Obsidian `#000000` for Structural borders, section dividers, image edge treatments - used as a hairline, never as a fill
- Walnut Shell `#2f2116` for Dark canvas behind full-bleed photographs, footer backgrounds, and dark editorial sections - the deep brown that makes white type glow warm
- Aged Bronze `#4f3622` for Secondary dark surface and border on dark sections - a half-step lighter than Walnut for subtle layering on dark
- Amber Glow `#fee197` for Navigation borders, active state accents, warning/attention states, and the single chromatic punctuation in an otherwise warm-neutral system
- Muted Gold `#987f61` for Link borders and heading underlines on dark sections - a desaturated brass for typographic detail without breaking the monochrome feel

- ModernEra `--font-modernera` for Sole typeface for body, navigation, buttons, links, headings, and overlay captions - a custom humanist sans that sits at 400 for body and 500 for emphasis. The entire type scale tops out at 40px, which is anti-SaaS: no 56px or 72px display sizes, no dramatic weight jumps. Authority comes from restraint, not volume.

## Avoid

- Do not introduce filled CTA buttons, drop shadows, or gradient backgrounds - the system is flat and outlined by design.
- Do not add chromatic colors beyond Amber Glow (#fee197) and Muted Gold (#987f61). The palette is warm-neutral only.
- Do not use display sizes above 40px or bold weights above 500. The system whispers; it does not shout.
- Do not apply border-radius to images or cards. Only buttons and links get 8px. Images and cards are sharp-cornered.
- Do not place white text on Warm Parchment backgrounds - contrast is reserved for Walnut Shell dark sections.
- Do not add icons, illustrations, or decorative graphics over photographs. The photograph is the only visual layer.
- Do not use multiple typefaces. ModernEra is the sole family - no serifs, no display fonts, no mono.

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
