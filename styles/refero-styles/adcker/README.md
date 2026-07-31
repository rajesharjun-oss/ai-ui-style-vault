# Adcker

Source: [Refero Style](https://styles.refero.design/style/e48b2dd0-328a-42ab-ad0f-ed24901bac4c)
Reference site: [https://adcker.com](https://adcker.com)
Captured: 2026-07-31
Refero published: 2026-05-10T22:02:11.645Z
Refero modified: 2026-06-05T08:08:18.732Z
Theme: light
Category: Agency

## Style Summary

Explore Adcker's light Agency design system: Ink Black #191919, Bone Canvas #efedea colors, nhm, psl typography, and DESIGN.md for AI agents.

North star: Giant brutalist poster on warm museum paper

## What To Borrow

- Ink Black `#191919` for All text, headlines, borders, link colors - the sole foreground color in the entire system. Near-black rather than pure black adds warmth that harmonizes with the cream canvas
- Bone Canvas `#efedea` for Page background, card surfaces, nav bar - the warm off-white ground that makes the near-black ink read with high contrast (15.1:1 AAA) without feeling harsh or clinical
- Stone Veil `#e3e1de` for Subtle surface variation against Bone Canvas - used sparingly for secondary panels or section backgrounds to create depth without introducing color

- nhm `--font-nhm` for Primary type system spanning body (16-21px) to extreme display (173-185px). Weight 400 carries both the whisper-quiet metadata and the 185px display headlines - the system trusts the scale to create hierarchy rather than reaching for bold weights. Letter-spacing tightens aggressively to -0.05em at display sizes to prevent the large counters from feeling airy.
- psl `--font-psl` for Mid-scale display for subheadings and section titles. Sits between body text and the extreme display tier, carrying -0.015em tracking for controlled density at smaller display sizes.
- psr `--font-psr` for Body text alternative at 21px with normal tracking - used for longer-form passages where the tighter nhm spacing would feel constrained.
- Kumbh Sans `--font-kumbh-sans` for Alternate display family at extreme sizes, sharing the same -0.05em tracking and tight 0.78-0.80 line-height as nhm. Provides a geometric counterpoint to nhm's neo-grotesque character for typographic variation within display lockups.

## Avoid

- Never introduce chromatic colors, brand accents, or semantic state colors - the 0% colorfulness is the system
- Never apply border-radius to any element - all corners are sharp (0px) to preserve the brutalist editorial feel
- Never use shadows, glows, or elevation effects - the system is completely flat
- Never use body text larger than 21px or smaller than 16px - the gap between body and display is intentional and vast
- Never use a centered CTA button with a colored fill - interactive elements are text links with underlines, not buttons
- Never set display type at line-height above 0.85 - the tight leading is what makes 185px text feel like a single sculptural object
- Never overlay text on dark backgrounds to create contrast - invert by using Ink Black (#191919) as a full surface, not as a treatment

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
