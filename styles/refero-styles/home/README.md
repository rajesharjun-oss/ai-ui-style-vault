# Home

Source: [Refero Style](https://styles.refero.design/style/2230ba53-445e-411d-b483-16410a072639) 
Reference site: [https://www.useparallel.com](https://www.useparallel.com) 
Captured: 2026-07-29 
Refero published: 2026-05-07T18:04:46.669Z 
Refero modified: 2026-06-03T15:53:28.462Z 
Theme: light 
Category: SaaS

## Style Summary

Explore Home's light SaaS design system: Cream Paper #e4dfd9, Pure White #ffffff colors, Rules Font, ui-sans-serif typography, and DESIGN.md for AI agents.

North star: Warm editorial atelier. Cream paper, charcoal ink, and one ember-orange period of emphasis - a job platform that feels like an art-book spread photographed under amber light.

## What To Borrow

- Cream Paper `#e4dfd9` for Page background canvas, hero overlays, editorial section backdrops - the warm off-white that sets the entire system apart from generic SaaS grays
- Pure White `#ffffff` for Card surfaces, product UI mockups, input fields, text on dark photography
- Charcoal Ink `#000000` for Primary text, strong borders, icon strokes, logo wordmark - the maximum-contrast voice
- Near Black `#050505` for Body text and heading color for subtle warmth below pure black
- Pressed Graphite `#171717` for Filled button backgrounds, dark UI surfaces, photo overlay scrims
- Slate `#737373` for Secondary text, subtle heading borders, metadata - the 60% voice
- Iron `#4b4b4b` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Stone `#999694` for Muted body text, caption-level copy, placeholder text
- Pewter `#666666` for Hairline borders on low-emphasis elements, dividers
- Fog `#c7c7c7` for Hairline borders, subtle dividers, ghost outlines - the most frequent border color in the system

- Rules Font `--font-rules-font` for Editorial display face for all headings - the weight-500 medium is deliberately non-bold, creating a literary, hand-set quality rather than a SaaS marketing shout. Tight -0.02em letter-spacing at 69px tightens the large headline to a single confident line. Substitute: 'Sohne Breit', 'GT America', or 'Inter' at weight 500
- ui-sans-serif `--font-ui-sans-serif` for System sans-serif for all functional text - body copy at 400/16px, UI labels and button text at 500, emphasized sub-labels at 600. The neutral system face keeps the interface quiet so the Rules Font headlines carry all the personality. Substitute: 'Inter', 'Sohne', or 'Geist'

## Avoid

- Don't introduce additional chromatic colors - the system is intentionally monochrome with one ember accent; adding blues, greens, or other hues breaks the editorial discipline
- Don't use bold (700+) or heavy weights for headlines - the Rules Font at weight 500 is the signature restraint
- Don't apply drop shadows beyond the single soft pattern rgba(0,0,0,0.07) 0px 6px 27px - avoid colored, multi-layer, or hard shadows
- Don't use pure black (#000000) as a filled button background when Pressed Graphite (#171717) is available - the slight warmth matters
- Don't set border-radius to 4px or 0px on cards or buttons - the 8-20px range is the system's tactile signature
- Don't use more than one chromatic element per viewport - the Ember Dot should feel like punctuation, not decoration
- Don't apply the 69px display size to subheadings or body text - reserve it for hero-level headlines only

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
