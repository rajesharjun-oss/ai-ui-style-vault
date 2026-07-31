# Vectary

Source: [Refero Style](https://styles.refero.design/style/dfe5faa4-a108-45a8-a68c-ed19be2db766)
Reference site: [https://vectary.com](https://vectary.com)
Captured: 2026-07-31
Refero published: 2026-03-18T10:36:25.000Z
Refero modified: 2026-06-05T10:43:32.645Z
Theme: light
Category: Design

## Style Summary

Explore Vectary's light Design design system: Graphite #252525, Charcoal #313131 colors, Inter typography, and DESIGN.md for AI agents.

North star: Graphite blueprint with violet signal

## What To Borrow

- Graphite `#252525` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Charcoal `#313131` for Secondary dark surface, nav panel background
- Slate `#595959` for Body text, secondary headings - the readable gray for paragraph copy
- Fog `#949494` for Muted helper text, captions, links at rest
- Paper `#ffffff` for Page background, text on dark fills
- Electric Violet `#6100ff` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Soft Violet `#9d50ff` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color

- Inter `--font-inter` for Single-family system: weight 400 for body and UI labels, weight 700 for section headings and button text, weight 900 reserved for display headlines (83px). The dramatic jump from 26px to 83px creates a two-tier hierarchy - page-heading-class copy lives at 22-26px, and only true hero moments reach 83px. Negative letter-spacing tightens with size: -0.012em at 14px scaling linearly to -0.039em at 83px, so display text optically squares up while small text stays crisp.

## Avoid

- Do not introduce a second chromatic accent - the system is monochromatic plus one violet, and adding red/green/blue/yellow breaks the drafting-tool identity
- Do not use weight 900 for body, labels, or section headings; it is loud and will flatten the hierarchy
- Do not add drop shadows, glows, or blur effects - the design language is flat; elevation comes from background tone, not shadow
- Do not use #6100ff on decorative icons, tags, illustrations, or non-action UI - the violet earns its place by being scarce
- Do not use #313131 as a page or card background; it is a nav-level surface only
- Do not set letter-spacing to 0 or positive values - the system always tightens, even at 14px body size
- Do not place violet text on a violet gradient background; the gradient already carries the brand and needs white text for contrast

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
