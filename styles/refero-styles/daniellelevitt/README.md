# Daniellelevitt

Source: [Refero Style](https://styles.refero.design/style/1a8d2d66-bb84-4929-acbe-2685fc9ab6e7)
Reference site: [https://www.daniellelevitt.com](https://www.daniellelevitt.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:30:53.290Z
Refero modified: 2026-06-05T11:23:17.548Z
Theme: mixed
Category: Agency

## Style Summary

Explore Daniellelevitt's mixed Agency design system: Vermillion #d15022, Acid Mint #75dfb5 colors, Helvetica Now Display, Helvetica Now Display Condensed...

North star: Punk broadsheet at billboard scale - a flat acid-mint field cracked open by a slab of vermillion condensed type the size of a car door.

## What To Borrow

- Vermillion `#d15022` for Display type, navigation, outlined action borders, section headings - burnt orange against white and mint creates the system's only chromatic voice; it carries every heading, every link, and the massive name lockup
- Acid Mint `#75dfb5` for Green action color for filled buttons, selected navigation states, and focused conversion moments
- Pure Black `#000000` for Image borders, hairline dividers, secondary borders, and body-text outlines where Vermillion isn't used - the structural ink that frames every photograph
- Paper White `#ffffff` for Primary canvas behind image collages and the opening viewport - flat, untextured, the gallery wall on which the photographs are pinned

- Helvetica Now Display `--font-helvetica-now-display` for Body emphasis, navigation labels, sub-headings, image captions, link text - the non-display workhorse at 29px bold for the bio statement and 18px for running text. The 800 weight everywhere (no medium, no regular) is a signature choice: the system never steps down from maximum volume.
- Helvetica Now Display Condensed `--font-helvetica-now-display-condensed` for Display name lockup and section-spanning hero type - the ultra-condensed bold at 72px+ fills viewports and overlaps photography. The condensation is the brand's signature: standard Helvetica at 800 wouldn't create the same monolithic, poster-scale letters that define the site's identity.

## Avoid

- Don't introduce a second body weight below 800 - medium and regular have no place in this system
- Don't add drop shadows, gradients, or any elevation - the system is completely flat
- Don't use rounded corners on images, buttons, or containers - 0px radius is non-negotiable
- Don't constrain the layout to a max-width container - the editorial poster aesthetic requires full-bleed
- Don't add a third color - the palette is strictly Vermillion, Acid Mint, Black, and White
- Don't separate type and photography into stacked rows - they should overlap and share the same plane
- Don't use a standard sans-serif at body sizes - even 18px and 29px text must be 800 weight to match the system's volume

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
