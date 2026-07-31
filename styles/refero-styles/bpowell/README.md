# Bpowell

Source: [Refero Style](https://styles.refero.design/style/7afd842e-44d4-4f01-9ef5-683c31d820c9)
Reference site: [https://www.bpowell.co](https://www.bpowell.co)
Captured: 2026-07-31
Refero published: 2026-04-30T01:39:54.380Z
Refero modified: 2026-06-05T09:40:55.961Z
Theme: mixed
Category: Design

## Style Summary

Explore Bpowell's mixed Design design system: Plaster White #ffffff, Carbon #111111 colors, Teg, Beatrice Display typography, and DESIGN.md for AI agents.

North star: type as architecture on white plaster

## What To Borrow

- Plaster White `#ffffff` for Primary canvas for the light sections; text color on the dark sections; hairline dividers on the dark sections
- Carbon `#111111` for Page background for the dark/film section; primary body text on light sections; structural fill for project name typography
- Ink Black `#000000` for Secondary text and fill on light sections; used where maximum contrast is needed against the white canvas
- Graphite `#2b2b2b` for Subtle darker border for low-emphasis rules on light surfaces

- Teg `--font-teg` for Display - reserved for the largest project names and the hero text. The aggressive -0.033em tracking at 86px tightens the letters into a near-monolithic block; this is the font that creates the 'stacked concrete' reading. Substitute: Migra, Editorial New, or Canela Display.
- Beatrice Display `--font-beatrice-display` for Mid-scale editorial type - appears as secondary project list text alongside the larger Teg names, providing typographic counterpoint at a calmer scale. Substitute: Tiempos Headline, Canela, or Reckless.
- Beatrice `--font-beatrice` for Body-weight Beatrice variant for the same 26px role but with the text-figure character set. Substitute: same as Beatrice Display.
- Diatype `--font-diatype` for Workhorse sans for body copy, nav items, and supporting text. Weight 500 is the default; 700 is reserved for the nav name 'Ben Powell' to give it anchor weight in the distributed nav. Substitute: Sohne, Inter, or ABC Diatype.
- New Grotesk `--font-new-grotesk` for Wide-tracked all-caps label face for section markers ('Design', 'Film'). The extreme +0.069em tracking turns short words into spaced-out type-art - this is the system's only 'decorative' choice. Substitute: ABC Diatype Mono Upper, Space Grotesk, or Neue Haas Grotesk Display.

## Avoid

- Do not introduce any color beyond #ffffff, #111111, #000000, and #2b2b2b - the system is monochrome by design
- Do not add images, thumbnails, or preview artwork to project list items; the name alone is the entry
- Do not center project names or align them to a grid - they are pinned to the left margin and let their own length determine the column
- Do not use card containers, rounded corners, or drop shadows; the system has zero elevation and zero radius
- Do not set body or nav text larger than 26px; the scale jumps directly to 58px for sub-headings and 86px for display, and bridging that gap destroys the contrast
- Do not add hover color changes, underlines, or button styles to project names - they read as a list, not as links
- Do not use more than one typeface per text block; mixing Teg with Beatricedisplay inside the same line breaks the typographic system

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
