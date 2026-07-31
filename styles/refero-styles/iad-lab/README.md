# Iad-lab

Source: [Refero Style](https://styles.refero.design/style/7d66c966-6cee-4c82-b2e4-2bf1ca7b2ccd)
Reference site: [https://iad-lab.ch](https://iad-lab.ch)
Captured: 2026-07-31
Refero published: 2026-04-30T02:42:58.965Z
Refero modified: 2026-06-05T10:49:46.645Z
Theme: dark
Category: Design

## Style Summary

Explore Iad-lab's dark Design design system: Charcoal Canvas #222222, Bone #f8f8f8 colors, Neue Haas Unica, Display (custom or system fallback) typography,...

North star: art-school exhibition on charcoal

## What To Borrow

- Charcoal Canvas `#222222` for Page background, the dominant surface across all sections and the base layer behind full-bleed photography
- Bone `#f8f8f8` for All body text, meta labels, navigation dots, and the dominant hairline border color - serves as the single foreground tone in this near-monochrome system
- Graphite `#2a2b2d` for Secondary icon strokes, subtle list dividers, and muted fill details - sits one step darker than the canvas for low-contrast decoration
- Ash `#757577` for Inactive or resting state for navigation dots and quiet UI affordances

- Neue Haas Unica `--font-neue-haas-unica` for The sole text family for all UI copy: meta labels at 16px, body at 18px, list/links at 24px, subheadings at 27px, section headings at 36px. Weight 400 is default; 700 is reserved for emphasis in the meta block and active labels. The 1.10 lineHeight on 36px headings creates tight, architectural vertical rhythm.
- Display (custom or system fallback) `--font-display-custom-or-system-fallback` for Reserved exclusively for the two program words ('IMAGINE', 'PROGRAM') that span the full viewport width and bleed past both edges. This face is wide, heavy, with rounded terminals - it is the visual signature of the entire site and carries the brand's identity more than any other element. When recreating, use a heavy extended grotesque (e.g. Obviously Wide Black, Neue Machina Black) at a size that forces letter cropping at the viewport edges.

## Avoid

- Do not introduce any color beyond the four neutrals (#222222, #f8f8f8, #2a2b2d, #757577). Chromatic accents are forbidden.
- Do not add drop shadows, gradients, or glow effects. Elevation is communicated through photography scale, not CSS shadows.
- Do not add a traditional navigation bar, header, or footer chrome. The meta label and dot navigation are the entire structural frame.
- Do not center text in narrow columns. Text should be short, left-aligned, and surrounded by generous negative space.
- Do not use border-radius values other than 15px or 20px. Avoid 4px, 8px, or fully rounded (9999px) - neither matches the system's geometric language.
- Do not set the display heading at a size where all letters fit within the viewport. The cropping is intentional and defines the visual identity.
- Do not use line-height above 1.35 for body text or below 1.10 for headings. The tight heading leading creates the architectural feel.

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
