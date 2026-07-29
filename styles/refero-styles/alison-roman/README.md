# Alison Roman

Source: [Refero Style](https://styles.refero.design/style/b2ace2c1-d6ee-4d57-915e-901224cded11) 
Reference site: [https://www.alisoneroman.com](https://www.alisoneroman.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T22:33:49.199Z 
Refero modified: 2026-06-05T10:32:44.319Z 
Theme: light 
Category: Other

## Style Summary

Explore Alison Roman's light Other design system: Aubergine Ink #290a08, Vintage Burgundy #810c00 colors, Jannon Neo, Modale Antique typography, and...

North star: cookbook pages on warm cream paper - a printed spread from an artisan food memoir, translated to screen with zero loss of tactility

## What To Borrow

- Aubergine Ink `#290a08` for Primary text, headings, filled action buttons, footer text - the warm near-black that anchors every screen; it is the only chromatic dark in the system and the only acceptable fill for primary actions
- Vintage Burgundy `#810c00` for Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Buttery Highlight `#fff3cc` for Link text and selected heading accent - a pale custard yellow used sparingly to mark hyperlinks and tiny editorial highlights, sitting at AAA contrast on the ink
- Parchment Canvas `#f6f0e1` for Page background - the dominant warm cream that defines the entire site mood; every screen sits on this surface
- Linen Card `#fffaec` for Card surfaces, list-item backgrounds, subtle elevated zones - a step lighter than the canvas, the only card treatment in the system
- Hairline Mist `#e5e7eb` for All borders and dividers throughout the system; used on cards, body blocks, links, and structural dividers - the single hairline color of the site
- Paper White `#ffffff` for Button borders, reverse text on dark fills, and the lightest possible surface lift; the only true white in the palette

- Jannon Neo `--font-jannon-neo` for Display and heading serif - carries every headline, section title, and large editorial moment from 20px through a dramatic 120px. The custom transitional serif with weight 300 for the largest sizes is the signature choice: the 'Books by Alison Roman' hero and book titles sit at whisper-light weight, giving the page a printed-book authority rather than a SaaS-bold shout. Substitute with Cormorant Garamond or EB Garamond at light weights.
- Modale Antique `--font-modale-antique` for Body, button, card, and UI serif - a slightly more grounded old-style serif for all running text, button labels, card descriptions, and footer lines. The workhorse that lets Jannon Neo's headlines breathe. Substitute with Lora or Source Serif Pro.
- -apple-system `--font-apple-system` for System fallback for legacy card content blocks; only present at 29px with normal tracking - used as a safety net rather than a deliberate voice

## Avoid

- Do not introduce drop shadows, glows, or blurred elevations anywhere - the system is intentionally flat.
- Do not use a border-radius on any element; the 0px geometry is the design's signature.
- Do not use blue for links, buttons, or accents - Buttery Highlight is the only accent color for hyperlinks.
- Do not use Vintage Burgundy (#810c00) for UI chrome, text, or buttons; it is reserved for book-cover backgrounds only.
- Do not use system sans-serifs (Inter, Helvetica) for headlines - the Jannon Neo serif is the identity.
- Do not fill more than 15% of any page with a non-cream, non-ink color; the system is overwhelmingly two-tone.
- Do not stack sections on alternating background colors; the cream canvas is continuous from top to bottom.

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
