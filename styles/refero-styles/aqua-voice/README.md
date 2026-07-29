# Aqua Voice

Source: [Refero Style](https://styles.refero.design/style/6734fe92-6a02-45d5-8d72-0c55b37ace82) 
Reference site: [https://withaqua.com](https://withaqua.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:41:36.421Z 
Refero modified: 2026-06-03T18:59:19.483Z 
Theme: light 
Category: SaaS

## Style Summary

Explore Aqua Voice's light SaaS design system: Sky Signal #67beff, Electric Iris #4288ff colors, sans-serif, PP Neue Montreal typography, and DESIGN.md for...

North star: Whisper on paper - ultra-light type resting on near-white with a single blue drop of color

## What To Borrow

- Sky Signal `#67beff` for Blue action color for filled buttons, selected navigation states, and focused conversion moments
- Electric Iris `#4288ff` for Outlined/ghost action border, inline link accent, focus rings - cooler and slightly deeper than Sky Signal
- Paper White `#fafbfc` for Page canvas, primary surface, inverted text on dark bars
- Mist `#f3f7fa` for Subtle band backgrounds, section alternation, elevated surface tint
- Fog `#f2f6fa` for Card surface, soft fill behind product screenshots
- Linen `#e5e8ec` for Hairline dividers, faint borders, disabled surfaces
- Ash `#efefef` for Ghost button background, subtle hover fill
- Inkstone `#292c3d` for Primary text, strongest contrast - carries the 200-weight headlines
- Slate `#3e4150` for Body text, secondary headings, dense body copy
- Pewter `#686a76` for Muted body text, helper text, inactive nav
- Graphite `#7d7e7e` for Tertiary text, footer links, faint labels
- Silver `#c2c3c8` for Placeholder text, very faint borders, decorative strokes
- Obsidian `#171719` for Top announcement bar background, dark surface, inverted text fill
- Midnight `#1e1e20` for Dark card surface, secondary dark fill

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- PP Neue Montreal `--font-pp-neue-montreal` for Primary typeface - weight 200 for display and headlines (anti-convention; most sites use 600-700, this whisper-weight gains authority through restraint), weight 400 for body and subheadings. Custom Pangram Pangram face with Polish alternates and character variants.
- PP Neue Montreal `--font-pp-neue-montreal` for Medium cut for UI controls, buttons, nav links, and small labels where the Book weight feels too quiet to anchor interaction
- Inter `--font-inter` for System-level fallback and small UI text - nav micro-labels, metadata, the smallest body sizes
- Geist Mono `--font-geist-mono` for Monospaced face for keyboard hints (the Hold/Space key chips), code, and technical micro-labels
- IBM Plex Mono `--font-ibm-plex-mono` for IBM Plex Mono - detected in extracted data but not described by AI

## Avoid

- Do not use weights above 500 for PP Neue Montreal - the Medium 500 is already the upper bound; 600+ destroys the whisper character of the system.
- Do not add color to body copy, headings, or backgrounds beyond the Inkstone/Slate/Pewter neutral scale - chromatic text breaks the monochrome contract.
- Do not apply large or saturated shadows; the system intentionally operates at rgba(0,0,0,0.02) to rgba(0,0,0,0.1) depth only.
- Do not use pill shapes (9999px radius) for primary buttons - 8px is the button radius; pill shapes are reserved for tags and status chips.
- Do not introduce gradients, glassmorphism, or heavy blur effects - the design language is flat, matte, and paper-like.
- Do not set headline letter-spacing to negative values - PP Neue Montreal is already optically balanced; additional tracking adjustment creates inconsistency with the font's native rhythm.
- Do not use Electric Iris (#4288ff) as a fill - it is an outline/link/ghost action color only; Sky Signal owns the filled action role.

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
