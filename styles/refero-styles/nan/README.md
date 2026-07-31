# NaN

Source: [Refero Style](https://styles.refero.design/style/71db2a51-118e-42b1-879d-29872d52142f)
Reference site: [https://www.nan.xyz](https://www.nan.xyz)
Captured: 2026-07-31
Refero published: 2026-04-30T02:58:47.536Z
Refero modified: 2026-06-05T10:58:38.149Z
Theme: light
Category: Design

## Style Summary

Explore NaN's light Design design system: Mint Canvas #b7ffb4, Lime Spark #00ff00 colors, NaN Holo Mono, NaN Holo typography, and DESIGN.md for AI agents.

North star: mint greenhouse of living letters - a pastel type lab where every headline is the product itself

## What To Borrow

- Mint Canvas `#b7ffb4` for Page background, card surfaces - the signature pastel that makes dark type appear sunlit rather than printed
- Lime Spark `#00ff00` for Decorative typographic flourishes and SVG scribble overlays - a raw signal-green that contrasts the pastel canvas without warming it
- Carbon Ink `#262626` for Primary text, borders, icon strokes, button outlines - softer than pure black, sits on mint without vibrating
- Obsidian `#000000` for Display-type fills at the largest sizes, pure-black SVG fills for the heaviest display specimens
- Fog `#999999` for Muted helper text, inactive borders, disabled controls - the quietest readable neutral on the mint canvas
- Smoke `#767676` for Input field borders in resting state - darker than fog to signal interactivity without competing with the canvas
- Bone `#efefef` for Light surface for elevated UI bits (button hover, inverted controls) - provides a near-white counterpoint when the canvas needs to recede
- Paper `#ffffff` for Input field interior, pure-white text on dark inverted moments

- NaN Holo Mono `--font-nan-holo-mono` for All interface chrome - navigation, labels, buttons, form controls, metadata, keyboard hints. Set uppercase with +0.075em tracking, the letter-spacing is the signature that makes mono read as a deliberate UI system rather than terminal output. The weight range lets it flex from thin nav links to heavy button text without leaving the family.
- NaN Holo `--font-nan-holo` for Prose body and large secondary headlines that need to sit beside display specimens without competing. The 86px weight-300 size is a typographic statement - a humanist counterweight to the blocky display faces above it.
- NaN Archy On ExtraBlack `--font-nan-archy-on-extrablack` for Hero display headline - the signature specimen face, shown at its native 228px with tight 0.90 leading so the letterforms stack into a near-monolithic mass. This is the typeface the homepage exists to sell.
- NaN SuperX Sans Display Black `--font-nan-superx-sans-display-black` for Secondary display face - ultra-tight 0.85 leading creates a dense typographic slab, the contrast to Archy's rounded forms. Used in alternate hero rotations.
- NaN SuperX Serif Text Thin Italic `--font-nan-superx-serif-text-thin-italic` for Editorial italic display - the serif counterpoint that proves the practice spans humanist letterforms, not just geometric sans. Thin weight at 216px is a tension device: fragile strokes at monumental size.
- NaN Holo Gigawide Ultra1 `--font-nan-holo-gigawide-ultra1` for Ultra-condensed display at 336px - the widest single-character scale on the site, used sparingly as a one-word exclamation.
- NaN Rage family (Zipp, Soft, Beau, Sans Narrow) `--font-nan-rage-family-zipp-soft-beau-sans-narrow` for Card specimen headlines in the 'You Might Have Missed' grid - each card shows the family name rendered in that exact family at 86px, making the grid self-documenting.
- NaNRageZippNarrowThin `--font-nanragezippnarrowthin` for NaNRageZippNarrowThin - detected in extracted data but not described by AI
- NaNRageSoftXCondensedRegular `--font-nanragesoftxcondensedregular` for NaNRageSoftXCondensedRegular - detected in extracted data but not described by AI
- NaNRageBeauStandardSemibold `--font-nanragebeaustandardsemibold` for NaNRageBeauStandardSemibold - detected in extracted data but not described by AI
- NaNRageSansNarrowMedium `--font-nanragesansnarrowmedium` for NaNRageSansNarrowMedium - detected in extracted data but not described by AI
- NaNSerfATextLightItalic `--font-nanserfatextlightitalic` for NaNSerfATextLightItalic - detected in extracted data but not described by AI
- NaNSerfSansLightItalic `--font-nanserfsanslightitalic` for NaNSerfSansLightItalic - detected in extracted data but not described by AI

## Avoid

- Don't use #ffffff as a page surface - it kills the mint canvas identity
- Don't use #000000 for body text or UI borders - it fights the pastel canvas
- Don't set the Holo Mono tracking below 0.05em - the letter-spacing is what makes the mono read as deliberate UI
- Don't introduce additional accent colors - the palette is mint, lime, carbon, and the aurora gradient, nothing else
- Don't add drop shadows to cards or buttons - the site defines depth through borders and whitespace only
- Don't use a 4px or 8px radius on cards - the 18px card radius is the signature soft-corner language
- Don't wrap display specimens in centered containers; full-bleed is what makes the type feel architectural

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
