# Midjourney

Source: [Refero Style](https://styles.refero.design/style/225059ac-0450-49d3-b2b7-d0e98b7ae938) 
Reference site: [https://midjourney.com](https://midjourney.com) 
Captured: 2026-07-29 
Refero published: 2026-03-12T13:16:36.000Z 
Refero modified: 2026-06-05T01:26:17.330Z 
Theme: dark 
Category: AI

## Style Summary

Explore Midjourney's dark AI design system: Cosmic Void #06051d, Abyssal Blue #0f1c36 colors, JetBrains Mono, DM Sans typography, and DESIGN.md for AI agents.

North star: Deep-ocean bioluminescent terminal. A pressurized darkness where intelligence visibly generates itself in ASCII streams, and controls appear as faintly glowing specimens.

## What To Borrow

- Abyssal Blue `#0f1c36` for Secondary surface backgrounds, button background variant - a step lighter than Cosmic Void for subtle depth layering
- Steel Navy `#1d293d` for Card surfaces, nav background, interactive container backgrounds
- Deep Slate `#314062` for Elevated card or hover state backgrounds
- Mist `#cad5e2` for Primary body text, general UI text - slightly blue-gray rather than pure white, reducing harshness against the dark void backgrounds
- Fog `#e5e7eb` for Borders, dividers, icon strokes throughout the UI
- Ash `#2e3038` for Secondary text, subdued labels
- Ghost White `#ffffff` for Heading text at maximum contrast
- Ice Blue `#ebf8ff` for High-brightness text on dark surfaces, link contrast text
- Portal Blue `#63b3ed` for Hyperlinks, inline text links - the single fully saturated accent visible in body content, connecting to Midjourney's Discord/community ecosystem
- Bioluminescent Green `#004f3b` for Sign Up pill button background (20% opacity tint) - deep green specimen glow against void
- Terminal Amber `#733e0a` for Explore pill button background (20% opacity tint) - amber specimen variant
- Crimson Depth `#8b0836` for Log In pill button background (20% opacity tint) - deep red specimen variant
- Specimen Green `#00bc7d` for Icon strokes and decorative SVG fills - vivid but used sparingly in iconography only
- Warning Amber `#f0b100` for Icon and UI accent strokes - section heading icons (Projects , About )
- Fault Red `#ff2056` for Icon strokes, error-adjacent SVG fills

- JetBrains Mono `--font-jetbrains-mono` for Every typographic role on this site - navigation labels, body copy, headings, buttons, links. Using a monospace font as the universal typeface (not just for code) makes the entire interface read as an active terminal output. 30px at lineHeight 1.25 serves section headings; 16px at 1.50 serves body and UI labels; 14px at 1.63 serves captions and metadata.
- DM Sans `--font-dm-sans` for Secondary UI copy and body text in prose sections - appears at 16px only. Weight 500 for emphasis within body blocks. Provides a subtle humanist contrast against the monospace primary, used sparingly so the terminal character of JetBrains Mono dominates.

## Avoid

- Do not use any sans-serif or serif font as a heading font - DM Sans is for body prose only; JetBrains Mono must dominate the typographic hierarchy.
- Do not create solid-fill opaque buttons - the translucent 20% opacity tinted backgrounds on pills are the system; solid fills break the bioluminescent specimen aesthetic.
- Do not introduce light backgrounds (#ffffff, light grays) into page sections - the design has no light mode; all surfaces must remain within the #06051d to #314062 dark range.
- Do not use more than three accent tint colors for buttons - the red/green/amber specimen triad is a closed system; adding new button colors dilutes the precision.
- Do not bold section headings or use font-weight above 500 anywhere in the UI - weight 400 at display sizes is the deliberate anti-convention choice that defines the visual voice.
- Do not add decorative imagery or photography - the only permitted visuals are AI-generated monochromatic renders and the ASCII/generative text hero.
- Do not apply colored backgrounds to body text sections - prose content must sit directly on #06051d Cosmic Void with #cad5e2 Mist text, no content cards with contrasting backgrounds.

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
