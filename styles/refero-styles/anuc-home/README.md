# Anuc Home

Source: [Refero Style](https://styles.refero.design/style/5e9409c4-d130-42f3-b224-5bd66cdfbe28) 
Reference site: [https://www.anuchome.com](https://www.anuchome.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:16:46.617Z 
Refero modified: 2026-06-03T20:31:22.395Z 
Theme: light 
Category: Agency

## Style Summary

Explore Anuc Home's light Agency design system: Ink #1a1a1e, Canvas #f3f3f2 colors, Instrument Sans, Instrument Serif typography, and DESIGN.md for AI agents.

North star: editorial gallery in warm white - a quiet, magazine-like space where oversized serif headlines and monumental rounded geometric letterforms frame intimate interior photography

## What To Borrow

- Ink `#1a1a1e` for Primary text, all borders, logo forms, icon strokes - the structural near-black that defines every contour across the system
- Canvas `#f3f3f2` for Page background - warm off-white that gives the entire system its gallery-wall warmth rather than clinical white
- Paper `#ffffff` for Card surfaces, article blocks, elevated panels - pure white sits on top of Canvas to create subtle layering without shadows
- Ash `#d1d1d2` for Hairline borders, divider lines, subtle structural rules - the thinnest visible grid
- Stone `#c1c2bd` for Secondary borders, muted fills, icon strokes at lower emphasis
- Linen `#e7e6e4` for Muted surface for category tags, soft chips, low-emphasis backgrounds - warm-tinted neutral that steps between Paper and Canvas
- Graphite `#4d4942` for Muted body text, secondary copy - warm dark gray for hierarchy below Ink
- Mist `#8d8d8f` for Tertiary text, timestamps, metadata - the lightest readable gray
- Bronze `#9a682c` for Sparingly used warm accent - appears as small punctuation dots or category indicators, never as fills; adds a whisper of warmth to the achromatic system
- Slate `#4a626f` for Secondary accent - cool counterpoint to Bronze, used in equally restrained dot/tag contexts to create subtle color rhythm

- Instrument Sans `--font-instrument-sans` for All UI, navigation, body copy, button labels, and small headlines. Weight 500 carries nav and button emphasis; weight 400 is the default reading voice. Free substitute: Inter, DM Sans.
- Instrument Serif `--font-instrument-serif` for All display and editorial headlines - the 52px and 74px sizes carry the brand's magazine-portfolio voice. The contrast between this high-contrast serif and the neutral sans is the system's signature typographic gesture. Free substitute: Playfair Display, Cormorant Garamond.

## Avoid

- Do not introduce shadows, glows, or blur effects - the system communicates elevation through background color steps (Canvas Paper Linen), never through box-shadow
- Do not use border-radius greater than 0px on any UI element - rounded buttons or cards would break the architectural language; the only rounded forms are the monumental logo shapes
- Do not add chromatic fills to buttons, backgrounds, or large UI surfaces - Bronze and Slate are reserved for dot punctuation only
- Do not use Instrument Sans for display headlines - the serif/sans contrast is the system's signature; flattening both to sans destroys the editorial voice
- Do not place body copy at sizes below 15px - the system is generous with reading size, not compact
- Do not stack dense information without the 96px section gap - the gallery-walk rhythm requires breathing room between content blocks
- Do not use decorative gradients, textures, or background imagery behind text - every text surface must sit on a flat, untextured neutral

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
