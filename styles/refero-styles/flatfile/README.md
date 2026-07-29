# Flatfile

Source: [Refero Style](https://styles.refero.design/style/1ded7f89-3df0-4e7c-9cac-28218d038575) 
Reference site: [https://flatfile.com](https://flatfile.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T22:04:47.619Z 
Refero modified: 2026-06-05T09:46:55.334Z 
Theme: light 
Category: Dev Tools

## Style Summary

Explore Flatfile's light Dev Tools design system: Midnight Ink #090b2b, Obsidian #151515 colors, FlatfileDiatypeVariable, Flatfile Diatype (Variable)...

North star: Quiet data journal on warm parchment

## What To Borrow

- Midnight Ink `#090b2b` for Primary brand color for headings, logo, emphasized text, nav labels, and icon strokes - a near-black with a faint violet cast that reads as ink rather than pure black against the cream canvas
- Obsidian `#151515` for Dark elevated surface for cards, headers, and contained panels. Do not promote it to the primary CTA color
- Graphite `#1b1b1e` for Primary body and heading text, dark card fills, and icon fills - the workhorse near-black with the faintest cool cast
- Charcoal `#262626` for Secondary dark surfaces and muted borders for inverted panels
- Steel `#808080` for Mid-gray for supporting UI marks, icon fills, and medium borders
- Silver `#aaaaaa` for Lighter mid-gray for tertiary text, placeholder copy, and decorative fills
- Fog `#d7d7d7` for Subtle border tone for ghost controls and quiet dividers
- Mist `#e5e7eb` for The system's structural hairline - dominant border, divider, and table-rule color across every layout context
- Parchment `#e5ebd3` for Warm sage-cream wash used as the hero background and as the secondary button fill - gives the page its printed-paper atmosphere
- Linen `#f8f8f8` for Card and elevated surface background - one step off the page to create depth without shadows
- Paper `#ffffff` for Pure white reserved for inverted buttons, tag chips, and high-contrast list items where Mist would be too muted
- Slate Link `#8c8c8c` for Default link and breadcrumb text color, distinct from body text gray

- FlatfileDiatypeVariable `--font-flatfilediatypevariable` for FlatfileDiatypeVariable - detected in extracted data but not described by AI
- Flatfile Diatype (Variable) `--font-flatfile-diatype-variable` for Primary UI and body sans - nav links, buttons, body copy, small labels, and card content. The variable axis lets the system shift between neutral body weight and slightly heavier button weight without changing family.
- Flatfile Diatype (Static) `--font-flatfile-diatype-static` for Display and section heading sizes. Uses tighter tracking as size grows - the 60px display sits at -0.0320em, pulling letters into a compact editorial block.
- Source Serif 4 `--font-source-serif-4` for Reserved exclusively for customer-quote hero text in testimonial cards. The serif italic-leaning humanist voice creates a print-publication contrast against the otherwise sans-only system.
- Sharp Grotesk `--font-sharp-grotesk` for Secondary display face for product-feature subheadings where a more condensed, technical voice is needed - used sparingly to break up the Diatype rhythm.
- Booton `--font-booton` for Booton - detected in extracted data but not described by AI

## Avoid

- Do not introduce a secondary chromatic brand color - Midnight Ink (#090b2b) is the only one.
- Do not use box-shadows to separate cards; shift the surface color one step instead.
- Do not set body text in anything other than Graphite (#1b1b1e) or #090b2b - no chromatic body copy.
- Do not use rectangular (non-pill) buttons; the 99px radius is a signature.
- Do not pair a chromatic icon color with chromatic background - keep the surface white and the icon the only color.
- Do not apply letter-spacing looser than -0.0050em - the system is built on tight, compact tracking at every size.
- Do not use the Parchment (#e5ebd3) wash outside the hero - it is a hero-only atmosphere, not a general surface.

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
