# Altitude Beverages

Source: [Refero Style](https://styles.refero.design/style/243a3dde-80a8-47a9-87f8-c549726ec6f3) 
Reference site: [https://altitudebev.com](https://altitudebev.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:13:55.585Z 
Refero modified: 2026-06-03T20:48:52.020Z 
Theme: mixed 
Category: E-commerce

## Style Summary

Explore Altitude Beverages's mixed E-commerce design system: Canvas White #fafafa, Warm Ash #d9d9d9 colors, HelveticaNowDisplay, EditorialNew typography,...

North star: Monochrome editorial spread. Imagine a fashion magazine spread stripped of all color except the product photography - the type and whitespace do all the storytelling.

## What To Borrow

- Canvas White `#fafafa` for Page background, card surfaces, primary canvas - the dominant near-white that lets photography and type carry all visual weight
- Warm Ash `#d9d9d9` for Elevated surface backgrounds for cards, buttons, and nav pill container - a warm gray one step darker than canvas for subtle layering without shadows
- Mid Gray `#cdcdce` for Hairline borders, link underlines, and divider lines - sits between canvas and text to create structure without weight
- Ink Black `#07060b` for Primary text, button labels, heading copy - a near-pure black with a faint blue undertone for maximum contrast against the warm canvas
- Pure Black `#000000` for Navigation borders and secondary text accents - used sparingly where a slightly harder edge is needed
- Glacial Mist `#ddfcff` for Faint cool-tinted accent on borders and fills - a barely-perceptible icy wash that adds micro-contrast without breaking the monochrome discipline

- HelveticaNowDisplay `--font-helveticanowdisplay` for Display and hero headlines - weight 800 at 160px with -0.05em tracking is the signature: massively compressed, ultra-bold statement type that dominates the viewport. Also used at 18px/500 for emphasized inline labels and 11px for caption-level brand marks
- EditorialNew `--font-editorialnew` for Editorial body and subheadings - the light-weight serif (weight 200) at 40-60px creates the 'fashion magazine pull-quote' feeling. The extreme thinness against the massive Helvetica display generates typographic tension. Also flows at 14-16px for editorial paragraph text
- DepartureMono `--font-departuremono` for Monospaced utility face for navigation labels, button text, form inputs, and small data - uppercase tracked monospace signals 'technical/informational' against the display serif and sans
- ui-sans-serif `--font-ui-sans-serif` for Fallback body text and generic UI copy - system sans at 16px handles the long tail of small interface labels that don't warrant the custom faces

## Avoid

- Do not add shadows to any component - use surface color steps (#fafafa #d9d9d9) and gradient transitions for all depth
- Do not use rounded corners below 44px for cards or 100px for buttons - the system is defined by its pill/lozenge geometry
- Do not set body text in HelveticaNowDisplay - reserve that face for display headlines at 60px+ only
- Do not use color for buttons, badges, or interactive elements - all actions are black text on warm gray or white surfaces
- Do not break the light/dark alternation with a chromatic section - the dark gradient is the only non-monochrome surface
- Do not use line-heights above 1.06 for headlines - the tight leading is part of the compressed, editorial feel
- Do not add icons or illustrations to the UI - the system relies on photography, monogram marks, and pure typography

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
