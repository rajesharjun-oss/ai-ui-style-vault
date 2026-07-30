# OPX Studio

Source: [Refero Style](https://styles.refero.design/style/bd395e2e-58a8-4626-acfa-9be8d6cdf604)
Reference site: [https://opx.studio](https://opx.studio)
Captured: 2026-07-30
Refero published: 2026-04-30T03:13:32.279Z
Refero modified: 2026-06-05T12:30:10.805Z
Theme: dark
Category: Agency

## Style Summary

Explore OPX Studio's dark Agency design system: Void Black #020202, Surface Black #000000 colors, OPX-Medium, Open Sans typography, and DESIGN.md for AI agents.

North star: Dark gallery monolith - a near-black exhibition hall where monumental white type and full-bleed photography do all the talking, and borders whisper at #292a2c.

## What To Borrow

- Void Black `#020202` for Page canvas - the base background across all sections
- Surface Black `#000000` for Section surfaces and image containment backgrounds, barely distinguishable from canvas to keep elevation flat
- Charcoal Hairline `#292a2c` for Structural dividers and borders - the only mid-tone in the system, carrying 900 occurrences as the skeleton between sections and elements
- Bone White `#ffffff` for Primary text, nav labels, project titles, and 1px pill-button borders - the sole signal of interactivity
- Ash Gray `#9b9b9b` for Muted helper text and secondary metadata in footer and supporting copy - recedes against the void

- OPX-Medium `--font-opx-medium` for Primary brand display and text face - a single weight (400) scaling across body, nav, subheadings, and monumental display. Custom face with a humanist-geometric tension; the anti-convention of using weight 400 (not bold) at 111px display size lets the headline dominate through scale alone rather than visual weight
- Open Sans `--font-open-sans` for Secondary supporting copy - used in hero subtext and longer descriptive passages where a more relaxed, open-licensed humanist is desired
- Untitled `--font-untitled` for Small label text for pill buttons and tag-like links (e.g. "View case study") - the only weight-500 usage in the system, giving micro-UI slightly more presence
- Helvetica `--font-helvetica` for System fallback for incidental body text and metadata

## Avoid

- Do not introduce a brand color, accent, or gradient - the system is monochrome by design
- Do not use box-shadows, glows, or any drop-shadow elevation
- Do not bold the display type - authority comes from size (80-111px), not weight
- Do not round the project imagery or apply a card background - images sit on the void directly
- Do not use #9b9b9b on a #ffffff surface - it fails contrast (2.8:1); it's only valid on the dark canvas
- Do not add icons, bullets, or decorative glyphs to the nav or links - type is the only ornament
- Do not tighten body line-height below 1.67 - the relaxed leading is the only counterpoint to the display text's compression

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
