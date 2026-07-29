# Incommonwith

Source: [Refero Style](https://styles.refero.design/style/1f9089e1-4170-482f-b988-afe1124a70a9) 
Reference site: [https://www.incommonwith.com](https://www.incommonwith.com) 
Captured: 2026-07-29 
Refero published: 2026-04-30T00:26:33.269Z 
Refero modified: 2026-06-03T19:06:51.716Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore Incommonwith's light E-commerce design system: Oxblood Ink #4a0a05, Cream Paper #fafaf9 colors, Mier A, Caslon Ionic typography, and DESIGN.md for...

North star: Editorial atelier in oxblood ink - warm cream pages, sunlit interior photography, and a single deep burgundy ink that carries every word, border, and link like fine letterpress.

## What To Borrow

- Oxblood Ink `#4a0a05` for All body text, headings, links, borders, outlined actions, and footer type - the singular chromatic voice; warmth and gravity without aggression
- Cream Paper `#fafaf9` for Primary page background; the warm off-white that gives the site its paper-stock feel
- Aged Linen `#f8f7f1` for Secondary surface, subtle card backgrounds, and pill-tag fills - slightly greener/warmer than the page, used for soft differentiation
- Warm Stone `#bcb6a6` for Muted background wash and tertiary surface - the only mid-tone neutral, used sparingly for section backgrounds
- Dusty Clay `#a2827f` for Muted captions, helper text, and de-emphasized UI labels. Do not promote it to the primary CTA color

- Mier A `--font-mier-a` for Primary UI and body sans - used for navigation, body copy, captions, dates, links, and all functional text. Weight 400 only; the system trusts size and color contrast to carry hierarchy, never weight. Substitute: Inter or Untitled Sans (free: Inter).
- Caslon Ionic `--font-caslon-ionic` for Sole serif - reserved exclusively for category names, journal headlines, and brand wordmark at 24px. The single appearance of a classical letterform creates a literary counterpoint to the neo-grotesque UI. Substitute: Cormorant Garamond or Libre Caslon Text.

## Avoid

- Don't use filled colored buttons - the system is entirely text-link driven; an outlined/underlined text link in #4a0a05 is the only action style
- Don't apply border-radius to images, cards, or panels - only pill tags at 9999px may be rounded; everything else is sharp
- Don't use drop shadows for elevation - depth comes from photography and warm color temperature, never from box-shadow
- Don't use pure white (#ffffff) backgrounds - always use #fafaf9 or #f8f7f1; the warmth is the brand
- Don't introduce accent colors beyond oxblood - the palette is intentionally narrow; adding blue, green, or other hues breaks the editorial coherence
- Don't use system fonts or substitute the Caslon/Mier pairing - the serif-sans tension is the brand's typographic identity
- Don't center-align body text or use large display headlines - the system is left-aligned and restrained; headlines are 24px, not 48px+

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
