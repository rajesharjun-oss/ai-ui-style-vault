# ORYZO AI

Source: [Refero Style](https://styles.refero.design/style/1f204e95-454a-437e-845b-c1b169d35607) 
Reference site: [https://oryzo.ai](https://oryzo.ai) 
Captured: 2026-07-29 
Refero published: 2026-04-30T00:11:38.351Z 
Refero modified: 2026-07-03T09:53:54.161Z 
Theme: dark 
Category: Design

## Style Summary

Explore ORYZO AI's dark Design design system: Warm Cream #ffedd7, Walnut Shadow #100904 colors, halyard-display-variable, Arial typography, and DESIGN.md...

North star: Darkroom product editorial. A lone object floating in warm darkness, cream typography the only decoration.

## What To Borrow

- Warm Cream `#ffedd7` for Light text on dark surfaces, inverse labels, and high-contrast captions.
- Walnut Shadow `#100904` for Page canvas and deepest background - warm near-black, not pure black. The void behind every product reveal
- Bark Brown `#382416` for Elevated surface and filled button background - the one chromatic step above the canvas, used for the single solid CTA
- Cork Border `#40372e` for Hairline dividers, dashed section separators, subtle container borders - warmer than the canvas by one step
- Driftwood `#6c5f51` for Mid-tone warm gray for secondary dividers and muted structural elements - the bridge between Bark and Cream
- Ember Accent `#dc5000` for Orange text accent for links, tags, and emphasized short phrases.
- Pure Black `#000000` for SVG icon fills and decorative vector elements only - never used as a background or text color

- halyard-display-variable `--font-halyard-display-variable` for The only typeface. Weight 500 at 51px drives display headlines with extreme uppercase confidence; the same family at weight 400 / 29px becomes the system's sole mixed-case body voice. Letter-spacing stays normal - the geometric forms do the work without tightening. Substitute: 'Inter', 'Sohne', or 'Neue Haas Grotesk' for close structural match.
- Arial `--font-arial` for System fallback for micro-legal labels (8px uppercase credits like "* ADOBE ILLUSTRATOR"). Not a design choice - a necessity for system-rendered disclaimers.

## Avoid

- Never use pure #fff for text or #000 for backgrounds - the warm cream and walnut shadow are the system; purity reads as wrong here.
- Never apply #dc5000 to buttons, CTAs, or interactive surfaces - the orange is editorial credit only.
- Never use lowercase or sentence-case for headings, nav, or labels; the only mixed-case text is the 29px body description.
- Never add drop shadows to cards, buttons, or sections - depth comes from the two-step surface stack (#100904 #382416), not from blur.
- Never use border-radius below 12px on containers - the geometry is deliberately chunky, not sharp.
- Never use more than one filled button per section; restraint is the design language.
- Never center-align body copy - headings and body text are always left-aligned, even when flanking a centered image.

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
