# Hugo

Source: [Refero Style](https://styles.refero.design/style/58a36cba-3fc4-48fa-a7d9-7f14592b7857)
Reference site: [https://www.hugoandmarie.com](https://www.hugoandmarie.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:58:00.853Z
Refero modified: 2026-06-05T10:59:04.450Z
Theme: light
Category: Agency

## Style Summary

Explore Hugo

North star: Monochrome gallery catalog - editorial photography mounted on infinite white, framed by whisper-thin serif.

## What To Borrow

- Paper White `#ffffff` for Page background, card surfaces, badge fills, nav dividers, input fields - the dominant surface that recedes to let imagery speak
- Ink Black `#000000` for Primary text, dense border structure, dark image overlays - the structural anchor for rules and headings
- Soft Ink `#0a0a0a` for Dark borders and separators for elevated surfaces and inverted UI.
- Graphite `#767676` for Input field borders - the only place a mid-gray border appears, marking form-field edges without competing with imagery
- Smoke `#b3b3b3` for Muted icon strokes, separators, and secondary graphic details. Do not promote it to the primary CTA color
- Ash `#cccccc` for Neutral form states, badge text, and quiet UI feedback where color should stay understated.

- saol-display `--font-saol-display` for Ceremonial headlines and editorial titles - ultralight serif at 100px with 0.95 line-height creates near-touching baselines that feel like fashion-magazine coverlines. This is the only place dramatic typography appears; everything else defers to sans-serif.
- soehne `--font-soehne` for All interface text - nav links at 16px weight 300, section headings at 20-22px weight 300, body at 16px weight 400 with comfortable 1.64 leading, supporting copy at 14px. The weight-300 default for nav and headings is a signature choice: it makes the UI feel editorial and unpressured rather than assertive.
- soehne-mono `--font-soehne-mono` for Badge labels and small metadata - monospace at 13px marks categorically different content (tags, IDs, status) from the proportional body text

## Avoid

- Never introduce a chromatic accent color, brand color, or decorative gradient - the system is strictly achromatic and adding color breaks the editorial contract
- Never apply box-shadow, drop-shadow, or any elevation effect - depth is communicated through image bleed and hairline rules, not shadows
- Never use soehne-mono for body copy or navigation - reserve it exclusively for badge labels and small metadata
- Never use saol-display at body sizes (14-22px) - it is a display face only; body work belongs to soehne
- Never add border-radius to cards, images, or inputs - 0px radius is the system default for all non-badge elements
- Never use filled background colors for buttons or interactive elements - text links and hairline buttons are the only interactive pattern
- Never use a font weight above 400 in soehne for UI text - heavier weights break the restrained editorial tone

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
