# Dot Inc.

Source: [Refero Style](https://styles.refero.design/style/4bcd0728-0d28-4835-ba9f-d61554f797b1)
Reference site: [https://pad.dotincorp.com](https://pad.dotincorp.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:24:50.940Z
Refero modified: 2026-06-05T09:19:14.588Z
Theme: light
Category: Productivity

## Style Summary

Explore Dot Inc.'s light Productivity design system: Ember Orange #ff5a2f, Ember Orange (link variant) #f15b2b colors, Plus Jakarta Sans typography, and...

North star: white laboratory with a single orange spark

## What To Borrow

- Ember Orange `#ff5a2f` for Primary action buttons, active badges, accent borders - the system's only chromatic voice, used to signal interactivity and emphasis
- Ember Orange (link variant) `#f15b2b` for Orange text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Carbon Black `#000000` for Primary text, icons, image overlays, card headings - maximum contrast against white canvas
- Graphite `#1f1f1f` for Headings, body emphasis, dark surface alternative - slightly softened black for large display text
- Slate Dark `#333333` for List items, secondary body text, card content
- Stone `#555555` for Navigation labels, subdued body text
- Pewter `#707070` for Muted descriptions, inactive list items, heading borders
- Steel `#a5a5a5` for Disabled or decorative text
- Mist `#b7bfc1` for Card borders, subtle button shadows - cool-tinted gray that defines container edges
- Cloud `#cbcbcb` for Alternate card backgrounds, disabled surfaces
- Fog `#dddddd` for Neutral secondary button fill, placeholder surfaces
- Paper `#e5e7eb` for Hairline dividers, borders across all contexts - the structural neutral that separates sections
- Pearl `#f5f5f5` for Card surfaces, subtle backgrounds, alternate section bands
- Canvas White `#ffffff` for Page background, nav surface, card fill, button text - the dominant canvas

- Plus Jakarta Sans `--font-plus-jakarta-sans` for Sole typeface for all text - body, headings, nav, buttons, badges, icons. The wide weight range (300-800) carries the entire visual hierarchy; display sizes reach 80px at weight 300 for a light, expansive headline, while UI text sits at 14-16px weight 400-500

## Avoid

- Do not introduce additional chromatic colors - the system's identity depends on the 2% colorfulness ceiling.
- Do not use border-radius below 8px for any interactive element; the soft, rounded geometry is a core brand trait.
- Do not apply shadows to cards, images, or navigation - only the primary CTA may have elevation.
- Do not use #000000 for body text at sizes above 20px; switch to #1f1f1f for large headings to avoid harshness.
- Do not use bold (weight 700-800) for body or heading text - reserve weights 700-800 for short labels or tags only.
- Do not create flat hard-edged rectangular blocks; every container needs 20-30px radius.
- Do not use gradients - the system is entirely flat with single solid color fills.

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
