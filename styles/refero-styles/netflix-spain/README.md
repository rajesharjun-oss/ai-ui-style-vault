# Netflix Spain

Source: [Refero Style](https://styles.refero.design/style/0e4d933c-aa07-4787-9884-40a0e6c338e4)
Reference site: [https://www.netflix.com](https://www.netflix.com)
Captured: 2026-07-30
Refero published: 2026-04-29T00:47:24.716Z
Refero modified: 2026-06-05T12:54:37.146Z
Theme: dark
Category: Media

## Style Summary

Explore Netflix Spain's dark Media design system: Netflix Red #e50914, Pure Black #000000 colors, Netflix Sans typography, and DESIGN.md for AI agents.

North star: A black cinema lobby with one red exit sign.

## What To Borrow

- Netflix Red `#e50914` for Primary CTAs, brand logo, active states, and the single chromatic accent in the entire system - the only warm color allowed to break the black void
- Pure Black `#000000` for Dominant page canvas and deepest surface - the cinematic background that swallows everything non-essential
- Obsidian `#0f0f0f` for Elevated surface tone, barely distinguishable from black - used for subtle layering and section dividers
- Carbon `#232323` for Card and button surface background - the primary elevated layer above pure black
- Charcoal `#2d2d2d` for Deeper card surface and input field background - secondary surface level for nested elements
- Graphite `#323232` for Rounded card backgrounds and tertiary surface treatment
- Slate `#393939` for Hover states and pressed button backgrounds - a step lighter than carbon for interaction feedback
- Ash `#5a5a5a` for Hairline borders and subtle dividers on dark surfaces
- Steel `#808080` for Muted body text and inactive helper copy
- Fog `#b3b3b3` for Secondary body text, metadata, footer links, and de-emphasized descriptions
- Pure White `#ffffff` for Primary headings, body text, input text, and icon fills - the sole text color that carries information weight
- Cinema Indigo `#192247` for Feature card gradient origin - deep blue-violet used as the cool terminus in card background gradients
- Bordeaux Glow `#461518` for Radial highlight origin on feature cards - a warm deep red that adds atmospheric luminosity to card edges
- Ember Arc `#6f181d` for Horizontal light beam across card midlines - a thin warm glow that bisects feature cards with a soft red line

- Netflix Sans `--font-netflix-sans` for Netflix Sans is a custom geometric sans optimized for on-screen readability across devices. The wide weight range (400-900) creates a dramatic hierarchy where 900-weight headlines at 56-100px feel like movie marquee titles. Body text stays at 400/500 with tight tracking. The extreme size jump from 24px to 56px signals a sharp two-tier heading system: section titles, then hero displays.

## Avoid

- Do not introduce any chromatic color other than #e50914 into the system - no blues, greens, or purples as UI accents (gradients on feature cards are the sole exception and are decorative only)
- Do not use drop shadows or box-shadows for elevation - depth comes from surface tone shifts only
- Do not add borders to cards - use tonal contrast between the card surface (#232323) and the page (#000000) instead
- Do not use rounded corners above 16px - the system is rectilinear with subtle softening, never pill-shaped except for tag/badge contexts
- Do not use Netflix Sans weight 400 for headings - reserve it for body copy; headings should be 700 or 900
- Do not place UI text directly on poster artwork without a dark scrim overlay - always protect legibility
- Do not introduce additional accent colors for states (hover, focus) - use #393939 (hover surface) and keep the red button as the only action signal

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
