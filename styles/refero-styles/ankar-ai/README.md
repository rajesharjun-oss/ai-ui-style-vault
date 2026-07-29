# Ankar AI

Source: [Refero Style](https://styles.refero.design/style/478c8660-f1a0-4339-ac8c-4cf7ca4cf738) 
Reference site: [https://ankar.ai](https://ankar.ai) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:16:45.641Z 
Refero modified: 2026-06-03T15:45:45.704Z 
Theme: light 
Category: AI

## Style Summary

Explore Ankar AI's light AI design system: Obsidian #000000, Paper White #ffffff colors, Switzer Variable, Kibitz Pro Light typography, and DESIGN.md for AI...

North star: Patent vault opening into white atelier - a darkroom hero with a single illuminated manuscript, dissolving into generous editorial whitespace.

## What To Borrow

- Obsidian `#000000` for Primary text, hairline borders, icon strokes
- Paper White `#ffffff` for Page canvas, card surfaces, text on dark
- Ink `#171717` for Filled button background, dark card surfaces, hero base
- Charcoal `#1f1f1f` for Dark feature card surfaces, elevated dark panels
- Graphite `#515151` for Secondary text, muted labels
- Slate `#979797` for Muted helper text, disabled labels, logo grayscale
- Ash `#b9b9b9` for Soft surface tint, placeholder backgrounds
- Fog `#cfcfcf` for Dividers, input borders, ghost button fills
- Mist `#c5c5c5` for Light borders on muted backgrounds

- Switzer Variable `--font-switzer-variable` for Switzer Variable - detected in extracted data but not described by AI
- Kibitz Pro Light `--font-kibitz-pro-light` for Display and heading serif - used at all H1-H4 sizes. Weight 300 is anti-convention: most SaaS uses 600-700 for authority, this whisper-weight conveys authority through restraint. Tight line-heights (0.98-1.06) let large sizes feel carved from a single block rather than stacked lines.
- Switzer `--font-switzer` for Primary UI and body sans-serif. Weight 400 for body and 500 for nav labels and emphasis. Geometric humanist construction keeps it neutral so the serif can lead.
- Space Mono `--font-space-mono` for Monospace for labels, tags, metadata, and code-adjacent micro-copy. Adds technical credibility to the editorial voice.
- System sans-serif `--font-system-sans-serif` for Fallback utility text - secondary nav micro-copy and fallbacks. Lowest in the hierarchy; should not appear on hero or feature content.

## Avoid

- Don't introduce chromatic accent colors - the system is strictly monochrome and any color breaks the editorial voice
- Don't use bold (600+) weights for the serif - the whisper-weight is the signature; going heavier flattens the hierarchy
- Don't apply line-height above 1.10 on display sizes - the carved, tight leading is what makes 48-64px feel architectural
- Don't add drop shadows to cards, buttons, or nav - the design is intentionally flat and shadow kills the editorial feel
- Don't use pill-shaped (fully rounded) buttons - 4px corners read as precise and professional, pills would feel consumer/playful
- Don't use the system sans-serif fallback for any user-facing content beyond utility micro-copy
- Don't center-align body paragraphs or long-form descriptions - left-align with a max-width column

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
