# Gleap

Source: [Refero Style](https://styles.refero.design/style/2eab438d-32cd-40c2-b160-1e4127dac569)
Reference site: [https://gleap.io](https://gleap.io)
Captured: 2026-07-30
Refero published: 2026-04-30T02:31:49.866Z
Refero modified: 2026-07-03T10:28:39.082Z
Theme: light
Category: SaaS

## Style Summary

Explore Gleap's light SaaS design system: Linen Canvas #edede8, Frosted White #ffffff colors, Switzer, system-ui typography, and DESIGN.md for AI agents.

North star: warm cream-paper workspace with graphite accents - a studio where matte-black ink dots float over linen architecture.

## What To Borrow

- Linen Canvas `#edede8` for Page background, section surfaces - warm off-white that pushes the whole system toward paper rather than screen
- Frosted White `#ffffff` for Card surfaces, elevated panels, glass overlays - clean white floats above the linen canvas for primary content
- Warm Stone `#dbdbd2` for Secondary card fills, secondary button backgrounds, accent surface - sage-tinted beige gives neutral elements warmth without becoming chromatic
- Pebble `#c0c0c0` for Circular accent tiles, muted card backgrounds - cool gray that sits one step back from stone for de-emphasized surfaces
- Graphite Ink `#141414` for Primary action button background, dark text on light surfaces - near-black with a hair of warmth, anchors every CTA
- Charcoal Body `#292929` for Primary body and heading text - readable but softer than pure black, keeps long-form copy from feeling harsh
- Slate Caption `#6f6f6e` for Secondary body, helper text, descriptive copy - carries the most volume of any text color
- Ash Subheading `#8f8f8e` for Subtle labels, muted headings, decorative type - sits between caption and hairline
- Iron Nav `#353535` for Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color
- Onyx Border `#000000` for Hairline borders, strong dividers, selected-state outlines - used at 1-2px to outline cards, buttons, and focus rings
- Quartz `#d0d0c8` for Quietest surface tint, reserved for low-contrast dividers and hover-state hints
- Lime Pulse `#4cc02b` for Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color

- Switzer `--font-switzer` for Primary typeface for all UI, body, headings, and buttons. Weight 400 dominates even at display sizes - headlines whisper rather than shout, which gives the brand authority through restraint. The Minor Third scale (1.2) is unusually compressed for a SaaS site, so sizes cluster more tightly than a Major Third or Perfect Fourth system would produce.
- system-ui `--font-system-ui` for Icon-internal text and OS-native labels - minimal usage, mostly decorative
- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI

## Avoid

- Don't introduce a brand-colored CTA - the system is intentionally chromatic-free; colored buttons would break the architectural language
- Don't use bold (600+) on headlines - weight 400 at display sizes is the signature; heavier weights belong in buttons and badges only
- Don't stack more than three surface tones in one screen (canvas white stone); the palette is rationed to preserve warmth
- Don't use drop shadows as decoration - if depth is needed, shift surface tone from white to stone to graphite instead
- Don't apply sharp corners to feature cards or panels - 12px is the floor for content surfaces; only consent dialogs may use 3.75px
- Don't add gradients to UI elements - the gradient zone is reserved for the hero product screenshot backdrop only
- Don't use letter-spacing wider than -0.01em on body copy; positive tracking breaks the tight architectural feel

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
