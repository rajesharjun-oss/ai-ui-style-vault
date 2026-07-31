# Daylit

Source: [Refero Style](https://styles.refero.design/style/5076959f-f849-4b50-8f8a-2040d4756f98)
Reference site: [https://www.daylit.com](https://www.daylit.com)
Captured: 2026-07-31
Refero published: 2026-05-10T22:04:14.397Z
Refero modified: 2026-06-05T11:22:24.686Z
Theme: light
Category: Fintech

## Style Summary

Explore Daylit's light Fintech design system: Wine Ink #4d1520, Midnight Wine #360912 colors, Tt Commons Pro Variable, Geist Mono typography, and DESIGN.md...

North star: Burgundy ink on cream parchment - a modern ledger rewritten for the AI era.

## What To Borrow

- Wine Ink `#4d1520` for Primary text, primary filled button background, active states, heading color, card borders, and dominant brand stroke - the single chromatic anchor of the entire system
- Midnight Wine `#360912` for Darkest surface for footer bands and inverted panels
- Lemon Whisper `#faffa7` for Decorative accent fill and border - used in illustration blocks, testimonial card outlines, icon highlights, and soft highlight washes
- Blush Rust `#662f3d` for Softened brand fill for secondary surfaces and SVG illustration shading
- Citrine Pop `#e6b800` for Rare saturated accent for micro-detail and decorative strokes
- Mauve Ash `#825b63` for Muted body text and subtle borders when full brand ink would be too loud
- Parchment `#fbf9f6` for Primary page canvas - the warm ivory that replaces cold white throughout
- Pure White `#ffffff` for Card surfaces, input fields, elevated panels - the brightest neutral layer above the parchment canvas
- Linen Beige `#f2eee7` for Hairline borders, dividers, ghost button outlines, and subtle UI separators
- Sandstone `#d3cac3` for Muted borders and secondary divider lines on cards and links
- Driftwood `#aaa49f` for Lowest-contrast neutral for decorative borders and inactive link text
- Slate Smoke `#717182` for Body secondary text, icon strokes, and helper copy - the only cool-leaning neutral
- Charcoal Ink `#101828` for Occasional dark text and info-toned badge borders when Wine Ink would be too warm
- Butter Cream `#feffe1` for Ultra-soft warm fill for highlight zones and subtle surface washes
- Dawn Glow `#e9e3d8` for Warm card background tint used sparingly for warm-on-warm contrast
- Rose Whisper `#d7a0a0` for Soft card border accent for warm-toned testimonial and content cards
- Plum Echo `#906c7b` for Badge and pill background for muted tag variants

- Tt Commons Pro Variable `--font-tt-commons-pro-variable` for Primary typeface across all contexts - headings, body, nav, buttons, cards. The variable weight axis (400-600) and extreme size range (9px micro-labels to 85px display) make it the sole workhorse. Display sizes use aggressive negative tracking (-0.04em at 76-85px) for a sculptural editorial feel; body sizes stay near normal tracking. The 600 weight carries emphasis without ever feeling bold-shouty.
- Geist Mono `--font-geist-mono` for Monospace accent for badge labels, inline code, and small caps-style tags like '+ AI AGENTS FOR ACCOUNTS RECEIVABLE'. Normal letter-spacing - not tracked like the primary face.
- Open Sans `--font-open-sans` for Open Sans - detected in extracted data but not described by AI

## Avoid

- Do not introduce cold grays (#e5e7eb, #f3f4f6, #6b7280) - the entire system is warm-toned and cool neutrals will clash
- Do not use 8px or 12px border-radius on cards or buttons - the 6px radius is part of the system's distinctive geometry
- Do not set body or heading text to weight 600 or 700 - the system maxes out at 600 for emphasis and prefers 400-500
- Do not use pure black (#000000) for text - use #4d1520 wine ink instead, even for body copy
- Do not add drop shadows to buttons, nav items, or small interactive elements - shadows are reserved for hero-scale elevation
- Do not use blue, green, or standard semantic colors for status - the system communicates state through opacity, position, and the single brand hue
- Do not center-align body paragraphs longer than two lines - left-align for readability; center only for headlines and short CTAs

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
