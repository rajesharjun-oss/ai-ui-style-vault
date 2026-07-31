# Paragraph

Source: [Refero Style](https://styles.refero.design/style/37dd9612-4df0-4cdd-b942-bd97dd0efbd2)
Reference site: [https://mirror.xyz](https://mirror.xyz)
Captured: 2026-07-31
Refero published: 2026-04-30T02:14:58.812Z
Refero modified: 2026-06-05T09:51:29.596Z
Theme: light
Category: Crypto

## Style Summary

Explore Paragraph's light Crypto design system: Page Parchment #dbd5d2, Ink Black #271f1b colors, IvyOra, Google Sans Flex typography, and DESIGN.md for AI...

North star: Editorial letterpress on warm parchment - a literary journal where the only color is ink-blue and every border is a page edge

## What To Borrow

- Page Parchment `#dbd5d2` for Primary border color for all containers, cards, nav, body, and links - warm taupe that reads as paper edge, not digital gray
- Ink Black `#271f1b` for All text, icons, and heading strokes - warm near-black with brown undertone, never pure #000
- Sheet White `#ffffff` for Primary page canvas and white card surfaces. Do not promote it to the primary CTA color
- Felt Gray `#ededed` for Secondary surface for badges, subtle panel backgrounds, and inactive card states
- Margin Gray `#888786` for Muted helper text, secondary metadata, and inactive nav items
- Periwinkle Action `#4a83f5` for Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Cornflower Wash `#b1cafb` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Dusk Periwinkle `#cedaf3` for Inset border and subtle blue-tinted edge on elevated or focused elements

- IvyOra `--font-ivyora` for Display and heading serif - used at 64px for hero headlines, 24px for section titles, and 18px for card titles. Weight stays at 400 across all sizes: the serif's contrast and tight tracking (-0.03em at display) do the visual work, not boldness.
- Google Sans Flex `--font-google-sans-flex` for Body, navigation, buttons, and utility text. Stays compact (14-18px) and invisible - its job is legibility, not personality. Weight 500 for nav active states, 400 for body, 600 reserved for button labels.

## Avoid

- Do not introduce gradients anywhere - the system is flat by design
- Do not use bold (600+) weights in the serif - IvyOra stays at 400 always
- Do not use pure black (#000000) for text - always #271f1b for warmth
- Do not place chromatic color on non-action elements; blue is reserved for buttons
- Do not use cold grays (#e5e7eb, #d1d5db) for borders - always the warm #dbd5d2
- Do not add box-shadows to content cards - the 1px border is the only elevation
- Do not set hero or section headlines above 64px; restraint is the editorial voice

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
