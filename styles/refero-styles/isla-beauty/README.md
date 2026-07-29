# Isla Beauty

Source: [Refero Style](https://styles.refero.design/style/0b9da6ef-bec5-4073-90af-66c67e72f2a4) 
Reference site: [https://isla-beauty.com](https://isla-beauty.com) 
Captured: 2026-07-29 
Refero published: 2026-04-30T03:59:35.437Z 
Refero modified: 2026-06-03T19:33:49.439Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore Isla Beauty's light E-commerce design system: Crimson Seal #e4263d, Vermillion Mark #e4002b colors, Soehne Buch, Nimbus Sans typography, and...

North star: Cream apothecary with surgical red accents - think warm parchment walls, amber bottles, and a single red seal on every label.

## What To Borrow

- Crimson Seal `#e4263d` for Primary action - filled add-to-cart buttons, CTA borders, section eyebrows, price accents, link underlines, and all brand punctuation against the cream canvas. The red carries the entire chromatic load; it must read as deliberate and small, never as decoration
- Vermillion Mark `#e4002b` for Secondary red accent - link borders, icon strokes, and outline-only controls. Slightly deeper than Crimson Seal; use when a quieter red moment is needed alongside the primary
- Ink Black `#000000` for Primary text, primary borders, navigation rules, body hairlines. The structural anchor of the entire interface
- Soft Coal `#1a1a1a` for Badge borders, heading text, list markers, card text on cream - a near-black used where pure black would feel clinical against the warm canvas
- Slate Drift `#2e2e2e` for Navigation borders, secondary structural lines - sits between Ink Black and the warm cream as a third depth
- Graphite `#3a3a3a` for Body text and borders for muted but still-readable paragraphs
- Pewter `#6f6f6f` for Badge borders, helper text, muted body copy - the first true mid-gray in the scale
- Stone `#8a8580` for Warm-leaning gray for tags, secondary body text, and quiet fills where neutrality needs to harmonize with the cream
- Sand Border `#e4dfd9` for Warm button borders, subtle section dividers - the border color that ties the warm palette together instead of fighting it with cool gray
- Cream Paper `#f8f6f3` for Page canvas, badge fills, soft card surfaces - the dominant background. Slightly warm to harmonize with product photography of amber liquids
- Pure Linen `#ffffff` for Card surfaces, button text on red, elevated product panels - the brightest surface that sits one step above the cream canvas
- Blush Wash `#f5e7df` for Soft accent badge fills, warm callout backgrounds - a desaturated peach that gives badge states a skin-like warmth

- Soehne Buch `--font-soehne-buch` for Primary body face at comfortable reading sizes (13-16px). Cleaner, more humanist than Nimbus; used for longer paragraphs and form input text.
- Nimbus Sans `--font-nimbus-sans` for Workhorse sans for UI: button labels, body copy, price text, nav links, and all utility surfaces. Carries lnum/tnum features for tabular alignment of prices.
- Soehne Kraftig `--font-soehne-kraftig` for Display and small-bold sans for headlines (60px), navigation, and tracked uppercase labels (11-12px with 0.07-0.10em tracking). The Kraftig cut adds authority without geometric coldness.
- AGaramondPro `--font-agaramondpro` for Editorial serif for major section headlines (54px) and subheadings (17-26px). The Garamond weight gives the brand its apothecary/editorial voice; pairs with italic for emotional accents.
- Garamond Italic `--font-garamond-italic` for Signature italic for emotional phrases, pull quotes, and editorial interjections mid-paragraph. Used sparingly - it is a whisper, not a shout.
- EB Garamond `--font-eb-garamond` for EB Garamond - detected in extracted data but not described by AI

## Avoid

- Don't introduce drop shadows, glow effects, or elevation layers - the design is intentionally flat.
- Don't use cool grays (blue-tinted). All neutrals should sit in the warm spectrum (#6f6f6f, #8a8580, #e4dfd9).
- Don't round corners beyond 3px on rectangular components; the system is sharp with intentional restraint.
- Don't mix more than one serif in the same paragraph. Garamond Italic is punctuation, not body type.
- Don't use red as a fill area larger than a button - red is a seal, not a field.
- Don't set body copy below 13px or above 17px. The 13-17px range is the system's comfort zone.
- Don't use #000000 for anything other than primary text and primary borders. For surfaces and secondary text, move to #1a1a1a or #3a3a3a.

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
