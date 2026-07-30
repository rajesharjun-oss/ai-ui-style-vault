# Dia Browser

Source: [Refero Style](https://styles.refero.design/style/b458ca1a-70f0-4f85-b745-f879a4d08457)
Reference site: [https://diabrowser.com](https://diabrowser.com)
Captured: 2026-07-30
Refero published: 2026-03-11T12:14:50.000Z
Refero modified: 2026-07-03T10:07:38.458Z
Theme: mixed
Category: Productivity

## Style Summary

Explore Dia Browser's mixed Productivity design system: Void Black #020204, Pure Black #000000 colors, Exposure Variable, Exposure VAR typography, and...

North star: blackroom gallery meets editorial broadsheet. A pitch-dark stage opens onto a sunlit paper spread where a single serif headline anchors each section.

## What To Borrow

- Void Black `#020204` for Hero background, dramatic dark sections - the opening stage of the experience
- Pure Black `#000000` for Primary text, button text, icon fills - the dominant ink across all surfaces
- Carbon `#636363` for Secondary text, muted nav, helper labels - softer than pure black for hierarchy
- Slate `#888888` for Tertiary text, inactive nav items, disabled states
- Silver `#c6c6c6` for Placeholder text, very subtle UI dividers
- Soft Graphite `#575757` for Dark button backgrounds on light surfaces - secondary action fill
- Paper White `#ffffff` for Primary page canvas and white card surfaces. Do not promote it to the primary CTA color
- Bone `#f8f8f8` for Page canvas, nav backgrounds, base surface beneath cards
- Linen `#efefef` for Button fills, pill backgrounds, header wash - slightly warmer than Bone, the dominant secondary surface
- Lime Wash `#f2fcb3` for Accent background wash, highlight zones, editorial color punctuation
- Saffron `#ffdc5c` for Secondary accent wash, warm highlight zones
- Spectrum Marquee `#fd02f5` for Sweeping rainbow gradient - the brand's signature motion element, traveling across hero and section dividers

- Exposure Variable `--font-exposure-variable` for Display headlines - the 112px whisper-weight serif that anchors hero and section titles. Its 0.85 line-height vertically compresses letters, making headlines feel carved and monumental rather than airy. Signature choice: anti-convention weight (300, not 700) and negative letter-spacing (-0.03em) create authority through restraint. Substitute: Playfair Display or DM Serif Display at weight 400 with tight tracking.
- Exposure VAR `--font-exposure-var` for Section headings and large nav - the bold companion to Exposure Variable. Used for 'Dia reads between the tabs' and feature titles. Tighter tracking at -0.05em at 48px gives headline density. Substitute: Inter Tight or a condensed grotesque.
- ABC Oracle `--font-abc-oracle` for Body text, UI labels, subheadings, and large feature headlines (54px at weight 300). The workhorse font - its humanist sans quality keeps long-form copy legible at generous line-heights (2.19 for body). Weight 500 used sparingly for emphasis. The 54px weight 300 headline is the secondary display voice, lighter than Exposure VAR but in the same serif-adjacent register. Substitute: Sohne or Inter at matching weights.
- ABC Oracle Triple `--font-abc-oracle-triple` for Button text, inline labels, UI microcopy - a narrower variant of Oracle designed for button and tag contexts. The wide line-height (2.19) suggests single-line button use with internal padding breathing. Substitute: Inter at 16px weight 400.
- ABC Favorit Mono `--font-abc-favorit-mono` for Eyebrow labels, step numbers (01, 02, 03), navigation metadata - all-caps at 13px with 0.1em tracking creates the editorial chapter-marker effect. The mono face contrasts with Oracle's humanist sans, creating typographic tension.

## Avoid

- Do not use bright saturated colors as background fills - the system is 96% achromatic; the only permitted color washes are lime (#f2fcb3) and saffron (#ffdc5c) in small editorial zones
- Do not set headlines at weight 600-700 - Dia speaks at weight 300 for display and 650 for subheadings; bold weights break the whisper-tone voice
- Do not use border-radius values outside the defined set (12, 16, 20, 24, 9999px) - improvised radii destroy the visual coherence
- Do not use multi-layer drop-shadow stacks on cards - the 3-layer filter is reserved for product screenshot windows only; regular cards use 1px borders
- Do not place colored buttons on colored backgrounds - the system uses black text on white/linen or white text on black, never chromatic fills
- Do not use line-height below 1.25 for any text - even the compressed 112px display keeps 0.85 only because the font is custom-designed for tight vertical fit; do not replicate this with system fonts
- Do not add hover transforms (scale, translate) to buttons - the system transitions only color, border, and opacity at 0.2s ease

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
