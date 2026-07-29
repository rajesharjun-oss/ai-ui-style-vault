# Giga

Source: [Refero Style](https://styles.refero.design/style/607e0dbf-e2fc-45c9-b939-946b8981c156)  
Reference site: [https://giga.ai](https://giga.ai)  
Captured: 2026-07-29  
Refero published: 2026-04-30T00:22:31.071Z  
Refero modified: 2026-07-03T10:50:25.966Z  
Theme: dark  
Category: AI

## Style Summary

Explore Giga's dark AI design system: Obsidian #000000, Onyx #0f0d0d colors, gigaSansText, emilioDisplay typography, and DESIGN.md for AI agents.

North star: Midnight horizon above matte obsidian

## What To Borrow

- Obsidian `#000000` as Deepest background, hero image overlay, footer canvas, shadow base pure black creates cinematic depth behind atmospheric photography
- Onyx `#0f0d0d` as Primary page canvas (--bg), card surface, default button fill the warm-tinted near-black that grounds the entire interface
- Charcoal `#171615` as Raised surface, dark button background (--button-dark-bg), elevated cards one step lighter than the canvas to signal depth without drawing attention
- Graphite `#262828` as Stepped feature panels, image containers, secondary surface layer visible in side-by-side comparison modules
- Void `#050404` as Near-black used in box-shadow tints and image depth effects effectively black but with a barely-warm undertone matching Onyx
- Paper `#ffffff` as Primary text, icons, light button text, filled button surface (--primary) pure white on near-black achieves 19:1 contrast, the highest readable tier
- gigaSansText Body text, buttons, navigation, links the workhorse. Weight 400 for paragraphs, 500 for button labels and emphasis. 16px at 1.5 line-height is the readable default; 14px at 1.43 handles dense UI chrome. `--font-gigasanstext` for the source typography voice
- emilioDisplay Display headlines the signature voice. Ultra-light weight at 48-66px with tight -0.02em to -0.03em tracking creates a film-title-card feel. Most enterprise brands shout with 700-weight headlines; Giga whispers with 300, which is the entire personality in one choice. `--font-emiliodisplay` for the source typography voice
- 4px base spacing with comfortable density
- Source radius system: cards 16px, chips 6px, input 6px, badges 9999px

## Avoid

- Don't use weight 600+ for headlines the system whispers at 300, shouting breaks the entire atmosphere
- Don't add drop shadows to cards depth comes from surface color stepping (#0f0d0d #171615 #262828), not elevation
- Don't use rectangular buttons or sharp corners on any interactive element all controls are pills
- Don't apply the Ember Red accent to more than one element per section overuse destroys its impact
- Don't use #000000 as page background use #0f0d0d; pure black is reserved for photographic backdrops
- Don't use chromatic colors for text white and grays only for typography; color is surface-only
- Don't mix serif and sans at the same hierarchy level emilioDisplay is for display, gigaSansText for everything else, never both at body size

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
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
