# Kinfolk

Source: [Refero Style](https://styles.refero.design/style/ac9b040e-36aa-4881-ada5-72d4744947a4)
Reference site: [https://www.kinfolk.com](https://www.kinfolk.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:42:17.813Z
Refero modified: 2026-06-05T09:36:11.012Z
Theme: light
Category: Media

## Style Summary

Explore Kinfolk's light Media design system: Ink Black #000000, Bone White #ffffff colors, Kinfolk-Serif-Text, Kinfolk-Serif-Display typography, and...

North star: Editorial broadsheet on bone-white linen - generous margins, ink-black serif, and a single warm-paper accent for section breaks.

## What To Borrow

- Ink Black `#000000` for Primary type, borders, icon strokes, and all hairline rules. The only foreground color in the system
- Bone White `#ffffff` for Primary canvas, card surfaces, and reverse text on dark photo overlays
- Paper Mist `#f4f4f4` for Soft surface elevation for insets, input fields, and section backgrounds that need to step down from pure white without introducing a hue
- Sage Paper `#dbded5` for Warm greenish-gray paper tint used as a section-break wash and full-bleed band. Provides the only chromatic moment in the system without becoming a brand color

- Kinfolk-Serif-Text `--font-kinfolk-serif-text` for Long-form body copy, captions, and article decks at 20px (lead paragraphs) and 15px (body). Normal letter-spacing lets the text breathe at reading size; the elevated line-height (1.5 at 15px) gives prose an airier, more literary rhythm than typical web body text.
- Kinfolk-Serif-Display `--font-kinfolk-serif-display` for Hero and feature headlines (60px, lh 1.0, tracking -0.025em / -1.5px). The tight tracking on a single 400 weight produces compressed, almost carved letterforms - authority through restraint, not volume. Used sparingly for the largest editorial moments.
- Kinfolk-Serif-Deck `--font-kinfolk-serif-deck` for Section titles, article headlines, and deck/sub-deck lines at 50/32/25px. Same 400-only discipline as the display face but at intermediate optical sizes. Tracking is still negative at the top end (-0.5px at 50px) for that dense editorial feel.
- Kinfolk-Sans `--font-kinfolk-sans` for UI chrome, metadata, category labels, navigation, button text, and small functional text. Tracking opens up dramatically at the small end (0.06em / ~0.78px at 13px) - a common editorial convention that makes all-caps metadata read as labels rather than body. One weight only, with scale doing all the differentiation.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

## Avoid

- Do not introduce any chromatic color beyond #dbded5 - the 0% colorfulness is the brand.
- Do not use filled buttons; every action is a text link with a 1px hairline border at most.
- Do not add shadows or elevation to cards - the surface hierarchy is purely typographic and positional.
- Do not use sans-serif for headlines, deck lines, or pull quotes; serif carries the entire editorial voice.
- Do not bold or italicize any of the Kinfolk type families; weight 400 is the only registered weight.
- Do not mix the #f4f4f4 mist and #dbded5 sage in adjacent surfaces - they read as conflicting neutrals.
- Do not use tracking above 0.06em on any text size; wide tracking is a 13px-and-below convention only.

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
