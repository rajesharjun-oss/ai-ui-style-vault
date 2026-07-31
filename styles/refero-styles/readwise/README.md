# Readwise

Source: [Refero Style](https://styles.refero.design/style/34c8dbee-f5d9-4495-a0e0-a25c6ca4b95b)
Reference site: [https://readwise.io](https://readwise.io)
Captured: 2026-07-31
Refero published: 2026-02-22T09:37:09.000Z
Refero modified: 2026-06-05T09:45:01.261Z
Theme: light
Category: Productivity

## Style Summary

Explore Readwise's light Productivity design system: Pen Blue #478cd0, Highlighter Yellow #fff7ca colors, Charter, Mulish typography, and DESIGN.md for AI...

North star: A reader's annotated journal - quiet paper-white, serif headlines, and one blue pen.

## What To Borrow

- Pen Blue `#478cd0` for Blue supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Highlighter Yellow `#fff7ca` for Yellow supporting accent for decorative details and low-frequency emphasis.
- Reader Orange `#fb9100` for Orange supporting accent for decorative details and low-frequency emphasis
- Paper White `#ffffff` for Card surfaces, product screenshot backgrounds, button text on filled buttons, and the nav background. The topmost surface tier
- Ink `#1f1f1f` for Primary heading and body text. Near-black rather than pure black - softer on the eye, reads as printed ink rather than digital display
- Page Mist `#f1f5f8` for Page canvas background. A cool, very-light blue-gray that reads as off-white paper rather than a flat gray, giving the entire page a subtle blue cast
- Deep Slate `#2d2f33` for Secondary text and dark surface details. Used in nav and component borders where a slightly different tone from Ink is needed
- True Black `#000000` for Dark supporting neutral for text, icons, and strong contrast.

- Charter `--font-charter` for Editorial serif used exclusively for headlines and large display text. The choice of a transitional serif in a productivity SaaS is the site's signature move - it signals 'reading' and 'books' before any copy is read. Weight 400 at 50px with lineHeight 1.00 creates tight, book-title-style display; weight 600 at 29px handles section headlines. Substitute: Source Serif Pro or Lora if Charter is unavailable.
- Mulish `--font-mulish` for Humanist sans for everything non-display: nav, body, buttons, labels, icons. The weight range is wide - 400 for body, 600 for buttons, 700/800 for bold tags and emphasis. Tighter lineHeight (1.09) at 11px keeps captions compact; 1.50 at 16-18px gives body copy room to breathe. Consistent -0.02em tracking across all sizes tightens the sans into a clean utility voice.

## Avoid

- Don't use Charter for body copy, nav, or buttons - it's reserved for headlines 22px and above.
- Don't apply #fff7ca to full card surfaces, section backgrounds, or large areas - it loses its meaning as a highlighter if it covers more than a line of text.
- Don't introduce additional accent colors beyond Pen Blue, Highlighter Yellow, and Reader Orange - the system is deliberately near-monochromatic.
- Don't use heavy drop shadows on cards or buttons; if elevation is needed, keep it soft (spread 20px) and tinted with Ink rather than pure black.
- Don't set display headlines in all-caps or with positive letter-spacing - Charter at 50px works because of its tight 1.00 leading and natural tracking.
- Don't use a filled colored button for secondary actions; use the Ghost Sign In style (white fill, 1px border) or a plain text link in Pen Blue.
- Don't set the page background to pure white #ffffff - Page Mist #f1f5f8 is what makes the white cards and product mockups read as elevated surfaces.

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
