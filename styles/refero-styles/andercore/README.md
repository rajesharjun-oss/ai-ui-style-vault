# Andercore

Source: [Refero Style](https://styles.refero.design/style/2d4ced28-e579-4fa0-84bc-836dd008034f) 
Reference site: [https://www.andercore.com](https://www.andercore.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:16:14.919Z 
Refero modified: 2026-06-03T19:50:37.310Z 
Theme: dark 
Category: SaaS

## Style Summary

Explore Andercore's dark SaaS design system: Signal Red #e32735, Carbon #0b0405 colors, Archivo, Space Mono typography, and DESIGN.md for AI agents.

North star: Steel blueprint at midnight

## What To Borrow

- Signal Red `#e32735` for Red action color for filled buttons, selected navigation states, and focused conversion moments
- Carbon `#0b0405` for Primary section background, full-bleed dark canvases, secondary button fill
- Graphite `#150e0f` for Alternate near-black surface for cards and elevated panels on dark sections
- Steel `#382e30` for Hairline borders on dark surfaces, card edges, table dividers, UI mockup outlines
- Slate `#858182` for Secondary text, badge borders, badge labels, muted helper copy
- Chalk `#ffffff` for Primary text on dark, nav and hero overlay type, inverted button text, light section backgrounds
- Foil `#000000` for SVG icon fills, decorative vector detail

- Archivo `--font-archivo` for All interface type - headlines (40/56px, weight 500), subheads (24px, weight 500), body and UI (14/16px, weight 400), nav links (12/14px). The geometric grotesque with tight -0.02em tracking gives industrial precision; weight 500 (not 700) for display type keeps the system restrained rather than shouty.
- Space Mono `--font-space-mono` for Badge labels, step counters ('01', '02', '03'), industrial tag stamps - the monospace face signals instrumentation and serial-number precision, contrasting Archivo's proportional geometry

## Avoid

- Don't introduce drop shadows, glows, or blur-based elevation - structure is line-based only
- Don't use #e32735 for body text, icons, or secondary UI - it's an action color, rationed
- Don't round corners beyond 4px - no 8px, 12px, 16px, or pill radii anywhere
- Don't set headings in bold (700+); weight 500 Archivo at 40-56px is the maximum voice
- Don't alternate between light and dark sections within a single content flow - the page is dark-dominant after the hero
- Don't use Archivo for numeric step counters, product codes, or instrumentation labels - those are Space Mono territory
- Don't add gradient fills to buttons or cards - the one gradient in the system (white red) is reserved for the hero-to-content transition

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
