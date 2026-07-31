# Adanola

Source: [Refero Style](https://styles.refero.design/style/a54e5114-bfb1-44ce-ab07-a133a1226117)
Reference site: [https://adanola.com](https://adanola.com)
Captured: 2026-07-31
Refero published: 2026-05-10T22:01:39.628Z
Refero modified: 2026-06-05T07:50:36.730Z
Theme: light
Category: E-commerce

## Style Summary

Explore Adanola's light E-commerce design system: Carbon Ink #000000, Paper White #ffffff colors, Favorit, Nunito Sans typography, and DESIGN.md for AI agents.

North star: Editorial lookbook on white paper. A fashion editorial spread where typography and photography breathe across clean white surfaces, with black ink for type and a whisper-thin custom sans-serif (Favorit) carrying the entire brand voice.

## What To Borrow

- Carbon Ink `#000000` for Primary text, filled action buttons, icon strokes, hairlines - the dominant ink across the entire interface
- Paper White `#ffffff` for Page canvas, card surfaces, text on dark fills, image backgrounds
- Soft Mist `#e5e7eb` for Subtle surface alternation, disabled states, skeleton backgrounds, light dividers
- Warm Fog `#f0efe7` for Off-white surface variant for subtle banding between product rows and editorial sections
- Blush Sand `#f5ebd5` for Warm cream surface for editorial highlight sections and seasonal accents
- Smoke Charcoal `#333333` for Secondary text, input borders, subdued UI chrome
- Onyx `#1d1d1d` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Stone Gray `#cccccc` for Placeholder backgrounds, image placeholder fills, neutral swatch defaults
- Slate `#2f3440` for Cool charcoal for product photography backgrounds and muted editorial surfaces
- Olive Drab `#636355` for Warm muted surface for product photography contexts
- Maroon Clay `#523037` for Warm muted surface for product photography contexts
- Deep Iris `#222845` for Cool muted surface for product photography contexts
- Pewter `#677284` for Cool gray for product photography contexts
- Driftwood `#dfccbe` for Warm beige for product photography contexts
- Pale Tide `#badce4` for Cool pastel surface for editorial accent sections

- Favorit `--font-favorit` for Brand and UI typeface - used across all navigation, headings, body, buttons, inputs, and product cards. Custom monoline sans-serif with tight tracking (0.025em). Substitutes: Inter, Sohne, or Neue Haas Grotesk. The whisper-weight 400 at 30px for hero headlines is a signature choice - most fashion sites use display serifs or bold weights, but Adanola's regular-weight headlines in a clean sans feel like editorial captions rather than advertising slogans.
- Nunito Sans `--font-nunito-sans` for Secondary fallback for form inputs and minor chrome elements
- Arial `--font-arial` for System fallback for legacy email and content blocks
- swym-font `--font-swym-font` for swym-font - detected in extracted data but not described by AI
- Source Sans Pro `--font-source-sans-pro` for Source Sans Pro - detected in extracted data but not described by AI

## Avoid

- Do not introduce drop shadows or box-shadow elevation on any component - the design system is deliberately flat and relies on whitespace and hairlines for separation
- Do not use saturated brand colors for buttons, links, or interactive states - keep the action palette strictly black/white/outline
- Do not round product card images or product card containers - the sharp rectangular edges are signature to the lookbook treatment
- Do not use display serifs, script fonts, or decorative typefaces for headings - the whisper-weight regular Favorit at 30px is the hero voice
- Do not add gradient backgrounds, colored section bands, or decorative patterns to page sections - alternation should be subtle (#e5e7eb, #f0efe7, #f5ebd5) at most
- Do not add icon containers, badges, or pill shapes around UI elements - tags and labels should be plain text with optional hairline underlines
- Do not use large border-radius values (8px+) on any element - the entire system is anchored to 0px and 4px radii only

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
