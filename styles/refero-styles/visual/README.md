# Visual

Source: [Refero Style](https://styles.refero.design/style/d2c0ed7b-c649-4d77-91de-1bd69dd10a9e)  
Reference site: [https://designstripe.com](https://designstripe.com)  
Captured: 2026-07-29  
Refero published: 2026-04-30T02:23:31.042Z  
Refero modified: 2026-06-05T01:35:37.983Z  
Theme: light  
Category: AI

## Style Summary

Explore Visual's light AI design system: Vellum #f6f6f4, Paper #ffffff colors, Serif (custom resembles a high-contrast modern editorial serif like...

North star: Warm editorial zine. Cream paper, serif posters, mono marginalia, a single yellow highlighter mark.

## What To Borrow

- Vellum `#f6f6f4` as Page background the warm off-white that defines the entire canvas tone
- Paper `#ffffff` as Card surfaces, elevated panels, product mockup backgrounds
- Ink `#000000` as Primary text, heavy structural borders, nav bar outlines
- Carbon `#2c2c26` as Warm near-black for dark panels, footer background, and neutral filled button fill the only filled button in the system
- Ash `#d0d0c8` as Light hairline borders, card outlines, subtle dividers
- Olive Char `#57584b` as Mid-dark structural borders, heavier dividers between sections
- Serif (custom resembles a high-contrast modern editorial serif like Reckless Neue, GT Sectra, or PP Editorial New) All display and heading copy. Used at poster sizes (6496px) for hero headlines and product section titles. The weight 300 at 96px is the signature move whisper-thin strokes at near-poster scale create authority through restraint, not volume. Tight tracking (-0.05em) at all sizes; line-heights under 1.1 let letterspacing do the vertical work `--font-serif-custom-resembles-a-high-contrast-modern-editorial-serif-like-reckless-neue-gt-sectra-or-pp-editorial-new` for the source typography voice
- Mono (custom clean geometric monospace) All UI text: navigation, buttons, labels, body copy, metadata, footer links. The mono choice is deliberate it makes every UI element feel like terminal output or code annotation, contrasting the serif's editorial softness. Weight 400 dominates; 500 for button text; 300 reserved for large mono headings (2848px range) `--font-mono-custom-clean-geometric-monospace` for the source typography voice
- 4px base spacing with comfortable density
- Source radius system: nav 3px, tags 3px, cards 8px, buttons 3px

## Avoid

- Don't use pure #ffffff as the page background always #f6f6f4 for the warm cream canvas
- Don't add drop shadows to cards or buttons the system is intentionally flat, separation comes from 1px borders and color contrast
- Don't use the serif at body sizes (16px or below) it is a display-only face; body copy must be mono
- Don't apply #fff347 to text, large backgrounds, or filled buttons it is a decorative accent only, not an action color
- Don't use cool grays (blues or true neutrals) the entire palette runs warm: olive-sage tones, warm blacks (#2c2c26 not #000000 for surfaces), and cream whites
- Don't use gradients the system is flat color only, with the one exception of the 3D hero render which contains its own internal gradients
- Don't exceed 4 instances of #fff347 per screen the accent loses impact if it appears more than 34 times on a single page

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
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
