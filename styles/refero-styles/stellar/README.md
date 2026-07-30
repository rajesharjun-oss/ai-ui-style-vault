# Stellar

Source: [Refero Style](https://styles.refero.design/style/98a1ad40-90e2-4665-b49f-e5ffd4d4b90b)
Reference site: [https://www.stellar.work](https://www.stellar.work)
Captured: 2026-07-30
Refero published: 2026-04-30T01:23:35.661Z
Refero modified: 2026-06-05T12:23:02.416Z
Theme: dark
Category: Agency

## Style Summary

Explore Stellar's dark Agency design system: Void Black #000000, Obsidian #171718 colors, Neue Montreal typography, and DESIGN.md for AI agents.

North star: Gallery wall at midnight

## What To Borrow

- Void Black `#000000` for Page background, primary canvas - absolute black eliminates surface depth, making images and white type feel like they float
- Obsidian `#171718` for Card surfaces, elevated panels, designer profile containers - one shade above void to separate without illuminating
- Graphite `#2c2c2e` for Borders on inputs, buttons, and nav dividers - the thinnest readable outline on near-black
- Ash `#888888` for Muted body text, secondary labels, inactive borders - the only gray with enough chroma to carry information
- Smoke `#e9e9e9` for Helper text, subtle text accents on dark surfaces
- Bone `#f3f3f3` for Headings, high-emphasis text - slightly off-white to avoid harshness against pure black
- Paper `#ffffff` for Primary headings, logo text, pure-contrast display copy
- Platinum `#dddddd` for Nav text at rest - sits one step below pure white to create a de-emphasized nav hierarchy

- Neue Montreal `--font-neue-montreal` for Single-family type system. Weight 400 carries the entire display scale up to 104px - the deliberate refusal of a bold weight is the signature. Weight 500 activates only on small uppercase labels and button text. Negative letter-spacing tightens display sizes (-0.02em at 70-104px) while small uppercase eyebrow labels open to +0.035-0.040em. The 104px display at weight 400 is anti-conventional - most systems would set this at 700-800; here it whispers, letting the void around it carry the weight.

## Avoid

- Do not introduce a second chromatic accent - Sprint Violet is the only color, and adding another dilutes the system
- Do not use bold (weight 600+) on any headline - weight 400 at large sizes is the signature; bold would break the hushed tone
- Do not add box-shadows to cards or buttons - depth comes from the #000000 #171718 surface contrast, not elevation shadows
- Do not use light gray (#f3f3f3, #e9e9e9) as a page background - the entire system depends on pure void black as the canvas
- Do not use 8px or 12px border-radius on cards or buttons - the system only uses 6px (inputs/nav), 10px (cards), and 50px (buttons/links)
- Do not set body text below 15px - the type scale starts at 14px for captions only; 15-16px is the readable minimum
- Do not place white or violet text directly on a #6a48f2 background without testing contrast - use white-on-violet for the CTA text only, never decorative

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
