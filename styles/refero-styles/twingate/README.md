# Twingate

Source: [Refero Style](https://styles.refero.design/style/0acef011-07da-4416-b874-ccdd675140f6) 
Reference site: [https://twingate.com](https://twingate.com) 
Captured: 2026-07-29 
Refero published: 2026-03-02T14:05:05.000Z 
Refero modified: 2026-06-03T18:04:16.926Z 
Theme: dark 
Category: Dev Tools

## Style Summary

Explore Twingate's dark Dev Tools design system: Void Black #000000, Obsidian #0e0f11 colors, sans-serif, TT Hoves Light typography, and DESIGN.md for AI...

North star: Midnight control room with violet and chartreuse signal lights. The whole interface sits on a near-black void, with two accent colors pulsing like status LEDs across instrument-panel components - restrained, engineered, and slightly futuristic without being showy.

## What To Borrow

- Void Black `#000000` for Page canvas, hero backgrounds, full-bleed sections
- Obsidian `#0e0f11` for Card surfaces, elevated panels, content containers above the page
- Carbon `#141617` for Secondary surface layer, input fields, nested containers
- Graphite `#1d2023` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Slate `#21223a` for Subtle violet-tinted surface for spotlight/featured cards
- Ash `#303438` for Hairline borders and dividers, very low-contrast separation
- Steel `#3a3d40` for Slightly stronger borders, subtle outer shadow tint
- Fog `#61626b` for Muted helper text, disabled labels, low-priority metadata
- Smoke `#8d8d96` for Secondary icons, inactive navigation items, tertiary text
- Cloud `#a1a1aa` for Body text secondary, link text in resting state, icon strokes
- Silver `#cfcfd3` for Body text default, paragraph copy, description text
- Bone `#999999` for Captions, fine print, decorative text
- Paper White `#ffffff` for Primary headings, button text on dark fills, high-emphasis text
- Signal Violet `#b6abff` for Brand accent - highlighted phrases, feature body text, link emphasis, inline brand moments
- Live Wire `#eef35f` for Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Circuit Teal `#00cbaa` for Decorative icon and illustration accent - network node strokes, lock/connection diagrams, graphic highlights

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- TT Hoves Light `--font-tt-hoves-light` for Display and headline - all large hero/section headlines (48-68px) use weight 300 with tight negative tracking (-0.018em to -0.007em). The whisper-weight at huge sizes is the brand's signature: confidence through restraint, not volume.
- TT Hoves Medium `--font-tt-hoves-medium` for Subheadings, feature card titles, navigation, button labels - the workhorse of the system. 32px appears as a mid-tier section heading, 20px as card titles.
- TT Hoves Regular `--font-tt-hoves-regular` for Body text and long-form copy - paragraph text at 16px with generous 1.5-1.7 line-height, smaller annotations at 11-14px
- Basis Grotesque Mono Pro `--font-basis-grotesque-mono-pro` for Code snippets, terminal-style text, and technical labels - used sparingly as a technical accent, never for body copy
- Inter `--font-inter` for Secondary body text and supporting UI labels (appears as a fallback/supplement to TT Hoves Regular in some contexts)

## Avoid

- Never use drop shadows for elevation - the system communicates depth through inset hairline highlights and stacked dark surfaces
- Never use more than one filled chartreuse CTA per viewport - it is a single-action accent
- Never set body text below 14px or use weight 300 for body - light weights are reserved for large displays
- Never add decorative gradients - the system is flat dark with chromatic accents, not glossy
- Never use pure black (#000000) text on dark surfaces - text on dark should always be white or a silver tone (#cfcfd3 minimum)
- Never break the 50px pill convention for buttons - outlined or ghost variants must also use the full pill radius
- Never introduce photography with a warm or colorful treatment - all imagery is monochrome, vector, or UI-screenshot

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
