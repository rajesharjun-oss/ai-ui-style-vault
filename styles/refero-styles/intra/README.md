# Intra

Source: [Refero Style](https://styles.refero.design/style/16a8de02-a4c6-4077-9d3a-ef6b5c10db12) 
Reference site: [https://intracbr.com.au](https://intracbr.com.au) 
Captured: 2026-07-29 
Refero published: 2026-04-30T02:43:09.852Z 
Refero modified: 2026-06-05T07:15:35.207Z 
Theme: light 
Category: Other

## Style Summary

Explore Intra's light Other design system: Paper White #ffffff, Ink Black #212529 colors, Whyte, -apple-system typography, and DESIGN.md for AI agents.

North star: white-walled gallery placard with one giant black eye

## What To Borrow

- Paper White `#ffffff` for Page canvas, card surfaces, type knocked out of black panels
- Ink Black `#212529` for Primary text, bold panels, the dominant non-white surface - carries a barely-perceptible cool tint that softens it from pure #000
- Pure Black `#000000` for Button strokes, logo fill, and the heaviest typographic moments where absolute zero contrast is required
- Hairline Gray `#e4e4e4` for Dividers, card borders, image outlines, table rules - the only mid-tone in the system

- Whyte `--font-whyte` for Single-weight type system. 95px display headlines for the wordmark and section titles carry the brand's editorial weight; 18-20px reads as body and meta; 16px as captions and link lists. The single weight (400) at all sizes is a signature choice - no bold, no light, the hierarchy is built through SIZE, not stroke. Substitute with Inter, Sohne, or Neue Haas Grotesk.
- -apple-system `--font-apple-system` for System fallback for environments where Whyte is unavailable; inherits macOS/iOS native rhythm. Use only as the last-resort stack, not the primary voice.

## Avoid

- Don't introduce a chromatic accent color for buttons, links, badges, or icons - there is no brand color in this system, the packaging supplies the only saturation.
- Don't use drop shadows, gradients, or blur effects - surfaces are flat, defined only by hairline borders.
- Don't use rounded corners anywhere, even on tags or avatars - everything is a sharp rectangle.
- Don't use bold (weight 600+) or light (weight 300) cuts of Whyte - weight 400 is the only voice, all hierarchy is typographic scale.
- Don't add icons, emojis, or decorative glyphs to the UI - the eye mark and the wordmark are the only marks.
- Don't split the giant wordmark into multiple lines or hyphenate it - "CAFE", "HOURS", "INTRA" each occupy one line at 95px.
- Don't apply a hover color change to links - the underline is the affordance, not a color shift.

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
