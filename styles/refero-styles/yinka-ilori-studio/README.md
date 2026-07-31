# Yinka Ilori Studio

Source: [Refero Style](https://styles.refero.design/style/deccaba1-8d53-4a82-b4c7-e2b99a3dc326)
Reference site: [https://yinkailori.com](https://yinkailori.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:37:32.390Z
Refero modified: 2026-06-05T09:36:13.426Z
Theme: light
Category: Design

## Style Summary

Explore Yinka Ilori Studio's light Design design system: Blush Paper #f5e5e5, Ink #000000 colors, Haas Grotesk Display R Web, Yinka Sans Ultra typography,...

North star: West African textile gallery on blush paper

## What To Borrow

- Blush Paper `#f5e5e5` for Page canvas, breathing space between pattern sections, card surfaces on quiet pages
- Ink `#000000` for Body text, navigation links, hairline borders, structural grid lines, icon strokes
- Rose `#d9698c` for Wavy stripe fill in hero/pattern compositions, deeper pink surface variant

- Haas Grotesk Display R Web `--font-haas-grotesk-display-r-web` for All UI text: navigation links, body copy, footer, labels. The 14px weight 400 is the default for everything clickable; 20px weight 500 for subheadings and journal titles. This is the working typeface - small, neutral, Swiss-grid functional.
- Yinka Sans Ultra `--font-yinka-sans-ultra` for Exclusive to the studio wordmark and oversized display moments. The +0.04em tracking at 120px is critical - it gives the dense letterforms air without losing the custom geometric character. Custom face only used at this display scale; never below 80px.

## Avoid

- Never add box-shadows, gradients, or border-radius to any component - the system is strictly flat and sharp-cornered
- Never introduce blue, green, or cool tones as UI colors - the palette is warm pink/orange/green within patterns, neutral outside
- Never use a type size between 20px and 120px - the scale is intentionally binary: small functional type or massive display type
- Never apply background colors to cards, buttons, or links - all UI chrome is transparent on the #f5e5e5 canvas
- Never decorate navigation with icons, buttons, or containers - it must remain plain uppercase text links
- Never compress section gaps below 175px between pattern and quiet sections - the rhythm requires dramatic vertical distance
- Never use Yinka Sans Ultra for navigation, body text, or anything below display scale - it is a wordmark face only

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
