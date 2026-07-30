# Flutterwave Design

Source: [Refero Style](https://styles.refero.design/style/97bbc1bd-873f-4048-b4cc-b20ea2e70097)
Reference site: [https://www.flutterwave.design](https://www.flutterwave.design)
Captured: 2026-07-30
Refero published: 2026-04-30T03:38:09.589Z
Refero modified: 2026-06-05T12:57:24.001Z
Theme: light
Category: Design

## Style Summary

Explore Flutterwave Design's light Design design system: Cream Paper #fff9f1, Ink Black #171717 colors, Millik, Moderat typography, and DESIGN.md for AI agents.

North star: warm editorial magazine on cream paper

## What To Borrow

- Cream Paper `#fff9f1` for Primary page canvas, card surfaces, nav background - the warm ground tone every screen sits on
- Ink Black `#171717` for Primary text, body copy, icon strokes, hairline borders - the dominant ink across the system
- Steel Gray `#b5b5b5` for Muted card backgrounds, disabled surfaces, secondary fills
- Graphite `#8b8b8b` for Tertiary surface, subtle background blocks, inactive dividers
- True Black `#000000` for Hard borders on icons, nav emphasis, button outlines where maximum contrast is needed
- Midnight Indigo `#12122c` for Display headings, link text, heading borders - deep violet-black replacing pure black for warmth and brand character
- Golden Amber `#f5a623` for Primary action fill, logo heart mark, highlighter accents - the single warm punctuation color in an otherwise cool monochrome system
- Peach Blush `#fcd2ba` for Accent section band backgrounds (Vibes, features) - warm wash that breaks cream monotony without introducing a new hue

- Millik `--font-millik` for Display and heading font - used only for the hero headline and section titles. Heavy weight (700-800) with -0.025em tracking at 60px creates a poster-like authority. Custom serif-adjacent display cut gives the site its editorial magazine voice; substitute with Recoleta or Tiempos Headline if Millik is unavailable.
- Moderat `--font-moderat` for Primary UI and body font - covers everything from 12px captions to 22px subheads. Geometrical sans with uniformly tight -0.036em tracking that keeps even small text compact and editorial. 400 for body, 500 for nav/links, 600 for labels, 700 for emphasis. Substitute with Inter or General Sans for closest match.
- Flutterwave `--font-flutterwave` for Reserved for the Flutterwave wordmark and icon glyphs - not a general-purpose text face. Limited to brand marks and the small heart logo.

## Avoid

- Do not introduce drop shadows, glows, or blurs to cards or buttons - elevation comes from color contrast alone.
- Do not use Golden Amber for backgrounds, panels, or large fills - it loses its punch as a accent if it covers more than button-sized areas.
- Do not use pure white (#ffffff) as a surface - cream (#fff9f1) is the canvas, white breaks the warm system.
- Do not set headings in pure black (#000000) - Midnight Indigo (#12122c) is the heading color, it carries the brand character.
- Do not use border-radius values other than 5px - no pills, no 0px sharp corners, no 8-12px rounded cards.
- Do not add gradients, patterns, or decorative backgrounds to UI chrome - illustrations on cards are where visual interest lives.
- Do not set body text above 20px in Moderat - for larger sizes, switch to Millik to maintain the type hierarchy.

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
