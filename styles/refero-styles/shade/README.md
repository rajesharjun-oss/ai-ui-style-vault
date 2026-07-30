# Shade

Source: [Refero Style](https://styles.refero.design/style/e549766e-b8b1-48a2-bd72-8cc04e9e4e9d)
Reference site: [https://shade.inc](https://shade.inc)
Captured: 2026-07-30
Refero published: 2026-04-30T00:18:31.730Z
Refero modified: 2026-07-03T15:50:45.320Z
Theme: light
Category: SaaS

## Style Summary

Explore Shade's light SaaS design system: Charcoal Ink #131315, Pure White #ffffff colors, sans-serif, Inter Display typography, and DESIGN.md for AI agents.

North star: Editorial paper cutouts on white

## What To Borrow

- Charcoal Ink `#131315` for Primary text, dark pill button fill, heading borders - warm near-black, the only filled button color in the system
- Pure White `#ffffff` for Page canvas, card surfaces, button text, ghost button background
- Bone `#f7f5ff` for Secondary canvas, subtle violet-tinted off-white for alternating sections
- Cutout Gray `#f1f1f1` for Solid offset shadow color under primary buttons and secondary surfaces
- Slate Mid `#717173` for Muted body text, secondary metadata, helper copy
- Hairline `#d0d0d0` for Subtle borders, dividers, inactive tab indicators
- Deep Charcoal `#444444` for Input borders, slightly heavier dividers than Hairline
- Logo Violet `#855cf7` for Brand mark gradient terminus, logo cube fill - the only saturated color in the system
- Lavender Trace `#dacefd` for Selected tab underline, violet hairline accents, announcement pill border - violet at whisper volume

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Inter Display `--font-inter-display` for Primary typeface for all UI text, body and headings alike. Single weight 400 carries the entire hierarchy through size and tracking alone - no bold, no light. The custom stylistic sets (ss01, ss07, ss08) reshape the g, a, and l terminals into a more geometric, editorial silhouette that distinguishes it from stock Inter.
- Aux Mono `--font-aux-mono` for Monospaced label font for section eyebrows (e.g. 'DAY 1', 'LET'S CHAT', nav items, badge text). Sets at 14px with -0.04em tracking gives timestamps and labels a technical, archival feel against the editorial display type.
- Inter `--font-inter` for Secondary fallback / system-level utility text where the custom display features aren't required

## Avoid

- Do not introduce additional brand colors or saturated fills - the system is 99% achromatic by design
- Do not use soft blurred shadows on buttons; the signature is hard, solid, paper-cutout offsets
- Do not bold headlines or use weight 500+ in Inter Display - the single-weight hierarchy is intentional
- Do not round the active tab into a pill background; the 2px violet underline is the only acceptable indicator
- Do not add gradient backgrounds to sections or cards - gradients are reserved for the brand mark
- Do not use border-radius values outside the defined scale (35/20/14/9/2px)
- Do not center-align body paragraphs longer than two lines - the system is left-aligned with a centered display headline only

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
