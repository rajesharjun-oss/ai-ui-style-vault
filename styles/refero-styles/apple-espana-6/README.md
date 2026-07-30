# Apple (Espana)

Source: [Refero Style](https://styles.refero.design/style/764b6a64-c233-4e0f-b8e1-bc01e2f8aa16)
Reference site: [https://www.apple.com/macbook-pro](https://www.apple.com/macbook-pro)
Captured: 2026-07-30
Refero published: 2026-03-25T11:46:13.000Z
Refero modified: 2026-07-03T03:37:17.050Z
Theme: dark
Category: E-commerce

## Style Summary

Explore Apple (Espana)'s dark E-commerce design system: True Black #000000, Charcoal #1d1d1f colors, SF Pro Display, SF Pro Display typography, and...

North star: black theater with luminous hardware

## What To Borrow

- True Black `#000000` for Primary canvas, hero background, nav backdrop, full-page surface
- Charcoal `#1d1d1f` for Elevated card surfaces on dark mode, section dividers, body text on light surfaces
- Smoke `#333336` for Nav segment bar, secondary button fills, subtle tonal contrast on dark backgrounds
- Graphite `#424245` for Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color
- Ash Gray `#86868b` for Muted body text, meta labels, input borders, helper copy
- Platinum `#cccccc` for Icon fills, nav glyphs, decorative outlines at low contrast
- Silk `#f5f5f7` for Primary heading and body text on dark backgrounds, light surface fills, badge backgrounds
- Pure White `#ffffff` for Maximum contrast text, icon fills, light card surfaces, button text
- Apple Blue `#0071e3` for Primary purchase CTA fill - the single chromatic action button, Buy button, focus ring
- Link Blue `#2997ff` for Blue text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Deep Link `#0066cc` for Standard body link color, secondary anchor text
- Ember `#b64400` for New badge accent - small warm punctuation for freshness markers

- SF Pro Display `--font-sf-pro-display` for Display and headline typography - hero h1, section openers, product names. Weight 600 with aggressive negative tracking (-0.015em at 80px down to -0.003em) gives the type a compressed, architectural presence. The whisper-thin tracking on the largest sizes is signature: 80px headlines feel monolithic rather than decorative.
- SF Pro Display `--font-sf-pro-display` for Subheadings, card titles, eyebrow labels - transitions from display to functional type. Tracking shifts to slightly positive values (+0.007em at 28px, +0.012em at 19px) as size decreases, compensating for optical tightness in shorter strings.
- SF Pro Text `--font-sf-pro-text` for Body copy and primary paragraph text - the 17px/1.47 combination with -0.022em tracking is the workhorse of the system. Used everywhere from hero subtext to footer disclaimers.
- SF Pro Text `--font-sf-pro-text` for Small UI text - nav links, footnotes, legal copy, micro-labels. Tracking goes more negative (-0.037em at 10px) at the smallest sizes to maintain readability despite size.
- SF Pro Text `--font-sf-pro-text` for Logo and brand mark rendering size in the global nav - weight 400 not 600, because the wordmark itself carries the form. Line-height 1.00 keeps it visually compact.

## Avoid

- Never use a second accent color beyond #0071e3 for actions - the blue is rationed, do not dilute it with green, orange, or purple CTAs
- Never add box-shadows to cards or buttons - the system defines elevation through color and radius alone, shadows would feel cheap
- Never use font-weight 700 anywhere - the system maxes at 600 because 700 reads as desperate on the negative tracking
- Never set headings below 28px - the scale starts at subheading 28px and goes up; small bold text is not in the vocabulary
- Never introduce a new radius below 10px for interactive elements - pills (9999px), cards (28px), and links (10px) are the only curves
- Never use color #0066cc as a button fill - it is link-text only; filling a button with it would confuse the action hierarchy
- Never add background gradients to text blocks or content sections - gradients are reserved for chip badges and decorative product imagery

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
