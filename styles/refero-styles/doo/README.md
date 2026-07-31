# Doo

Source: [Refero Style](https://styles.refero.design/style/d486c348-fc1b-4b01-9064-1213e4dbcb1b)
Reference site: [https://getdooapp.com](https://getdooapp.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:39:09.936Z
Refero modified: 2026-06-05T11:33:28.931Z
Theme: light
Category: Productivity

## Style Summary

Explore Doo's light Productivity design system: Indigo Pulse #3b3996, Slate #6e6d7a colors, Avenir Next typography, and DESIGN.md for AI agents.

North star: pastel sticky notes drifting on white linen

## What To Borrow

- Indigo Pulse `#3b3996` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color
- Slate `#6e6d7a` for Hairline borders, dividers, secondary text, list separators - the structural gray that quietly defines the page grid
- Graphite `#383938` for Navigation text, heading text, dark UI elements - the primary readable dark on white
- Ink `#111111` for Headline color, strongest body emphasis, near-black for maximum contrast on light surfaces
- Paper `#ffffff` for Page background, card surfaces, text on dark/indigo fills - the dominant canvas
- Mist `#edeef3` for Elevated panels, subtle background washes, light borders - the cool-tinted off-white that lifts content above the page
- Cloud `#f7f7f7` for Secondary card surfaces, quiet content panels
- Mint Whisper `#c3f5dd` for Task category tag accent (product UI), logo green dot - pastel annotation, not interface chrome
- Lavender Drift `#d1cafa` for Task category tag accent (product UI), logo blue dot - pastel annotation

- Avenir Next `--font-avenir-next` for Sole typeface across the entire system - nav, body, headings, display. Avenir Next's geometric humanism gives the page a calm, friendly, Apple-adjacent feel. Weight 400 carries everything; weight 600 is reserved for navigation and small emphases. Display headlines at 65px with negative tracking create a compressed, confident presence rather than shouting.

## Avoid

- Don't introduce additional chromatic UI colors on the marketing page - Indigo Pulse is the only saturated fill permitted
- Don't use drop shadows, gradients, or glow effects - the design is deliberately flat and paper-like
- Don't use any border-radius value other than 30px (cards) or 39px (buttons/links/pills)
- Don't use weight 700 or 800 - Avenir Next caps at 600 in this system, and the whisper-weight 400 headlines are the signature
- Don't add background colors to content sections - the page stays Paper white; use Mist (#edeef3) only for specific elevated panels
- Don't use icons or decorative graphics on the marketing page - product photography and the tri-dot logo are the only visual elements
- Don't use tight column grids; the layout is centered and spacious, not information-dense

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
