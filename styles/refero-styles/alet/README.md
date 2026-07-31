# alet

Source: [Refero Style](https://styles.refero.design/style/9b5203a8-07c8-4987-94c5-6411970896d2)
Reference site: [https://aletagency.com](https://aletagency.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:35:08.031Z
Refero modified: 2026-06-05T08:00:07.475Z
Theme: light
Category: Agency

## Style Summary

Explore alet's light Agency design system: Taupe Paper #ada59b, Ink Black #000000 colors, WorkSans, SilkSerif typography, and DESIGN.md for AI agents.

North star: Vintage editorial contact sheet on warm taupe paper.

## What To Borrow

- Taupe Paper `#ada59b` for Full-page canvas, the single dominant surface - every section and component sits on this warm gray, never on white or near-black. The warm undertone (vs cool slate) is what makes the whole site feel like printed stock rather than a digital UI
- Ink Black `#000000` for Primary text, all borders, all hairlines, all SVG strokes. Used at full opacity - no softened text grays, no 80% black. The crispness against warm taupe creates the magazine-printed feel
- Charcoal `#252525` for Navigation text and the nav underline borders. Slightly softer than pure ink for the persistent top-of-page chrome so the nav recedes behind the work
- Graphite `#101010` for Secondary text and supporting borders where Charcoal reads too soft but pure Ink is too loud. The single mid-step between nav and body
- Stone `#454545` for Occasional inset surface for body-level containers - the only tonal step above the canvas, used sparingly for any small frame or block that needs to separate from the page without introducing color
- Press Black `#060506` for Fine SVG illustration stroke - near-identical to Ink Black but kept distinct in the source. Use for line-art icons and decorative vector marks

- WorkSans `--font-worksans` for All UI chrome: navigation, category labels, body copy, metadata, toggle text. Deliberately tiny - 11-13px forces an editorial intimacy and keeps the page from feeling like a product interface. Set in Work Sans Regular at default tracking; the small size is what makes it feel like print captions rather than web UI.
- SilkSerif `--font-silkserif` for The ALET wordmark and any other serif display moment. Light weight at 23px with tight leading (0.94) and extremely wide letter-spacing - the letters almost float apart. The serif is the only non-sans on the site, which is what makes the brand mark readable as a masthead rather than a wordmark.

## Avoid

- Do not introduce any chromatic color - no accent, no CTA fill, no status greens/reds/blues
- Do not use white, off-white, or near-black as a section background - the taupe canvas is the only surface
- Do not add box-shadows, elevation, or gradient fills to any component
- Do not use a sans-serif for the wordmark or any display moment - Silk Serif is the only serif and the only size above 13px
- Do not round image corners or wrap photographs in cards with fills or borders
- Do not center body text in narrow columns - the studio statement is the only centered block, and it spans a wide measure
- Do not use large display weights (600-700) - the system runs entirely on Regular and Light

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
