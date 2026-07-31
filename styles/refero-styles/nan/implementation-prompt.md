# AI Implementation Prompt

Build a NaN-inspired interface using this source-derived style bundle.

Reference site: https://www.nan.xyz
Theme: light
Category: Design
North star: mint greenhouse of living letters - a pastel type lab where every headline is the product itself

Use these palette anchors:

- Mint Canvas `#b7ffb4` for Page background, card surfaces - the signature pastel that makes dark type appear sunlit rather than printed
- Lime Spark `#00ff00` for Decorative typographic flourishes and SVG scribble overlays - a raw signal-green that contrasts the pastel canvas without warming it
- Carbon Ink `#262626` for Primary text, borders, icon strokes, button outlines - softer than pure black, sits on mint without vibrating
- Obsidian `#000000` for Display-type fills at the largest sizes, pure-black SVG fills for the heaviest display specimens
- Fog `#999999` for Muted helper text, inactive borders, disabled controls - the quietest readable neutral on the mint canvas
- Smoke `#767676` for Input field borders in resting state - darker than fog to signal interactivity without competing with the canvas
- Bone `#efefef` for Light surface for elevated UI bits (button hover, inverted controls) - provides a near-white counterpoint when the canvas needs to recede
- Paper `#ffffff` for Input field interior, pure-white text on dark inverted moments

Use these typography anchors:

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

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1440px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site navigation
- Hero Statement Block: Opening brand description
- Live Font Tester: Interactive type specimen controller
- Aurora CTA Button: Sole chromatic primary action
- Display Headline (Specimen): Full-bleed type demonstration
- Font Specimen Card: Library entry in the 'You Might Have Missed' grid
- Section Label: Subsection heading
- Select Dropdown: Form control within the font tester
- Range Slider: Numeric control for size/leading
- Keyboard Hint Chip: Reveals power-user shortcuts

Do:

- Set all interface text in NaN Holo Mono with 0.075em tracking - the monospace + tracking combo is what reads as 'NaN UI' versus generic mono
- Use #262626 for text and borders, never #000000 for UI chrome - pure black is reserved for the heaviest display specimens
- Let display specimens bleed to viewport edges without a max-width clamp; the type defines the lateral scale
- Use the aurora gradient button (29.4px radius) exactly once per page - the gradient is rationed because it's the only warm element
- Mark every new section with a hollow circle bullet ( ) in 14px NaN Holo Mono, followed by 60-80px vertical space
- Make specimen cards self-documenting: render the card's font name IN that font, not as a label
- Keep all elevation to 1-2px hairline borders in #262626 - never introduce drop shadows

Avoid:

- Don't use #ffffff as a page surface - it kills the mint canvas identity
- Don't use #000000 for body text or UI borders - it fights the pastel canvas
- Don't set the Holo Mono tracking below 0.05em - the letter-spacing is what makes the mono read as deliberate UI
- Don't introduce additional accent colors - the palette is mint, lime, carbon, and the aurora gradient, nothing else
- Don't add drop shadows to cards or buttons - the site defines depth through borders and whitespace only
- Don't use a 4px or 8px radius on cards - the 18px card radius is the signature soft-corner language
- Don't wrap display specimens in centered containers; full-bleed is what makes the type feel architectural

Source prompt cues:

**Quick Color Reference**
- Page background: #b7ffb4 (Mint Canvas)
- Primary text & borders: #262626 (Carbon Ink)
- Muted text & disabled borders: #999999 (Fog)
- Decorative accent: #00ff00 (Lime Spark)
- Inverted / elevated surface: #efefef (Bone)
- primary action: #b7ffb4 (filled action)

**Example Component Prompts**
1. *Hero statement*: full-width #b7ffb4 background, left-aligned paragraph in NaN Holo Mono 26px weight 400, #262626, line-height 2.25, letter-spacing 0.075em, occupying ~75% viewport width. Overlay a lime (#00ff00) SVG scribble at the right edge.
2. *Display specimen*: full-bleed headline in NaN Archy On ExtraBlack 228px, weight 400, #000000, line-height 0.90, bleeding past the right viewport edge. No background, no border, no max-width.
3. Create a Primary Action Button: #b7ffb4 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
4. *Font specimen card*: 1px #262626 border, 18px radius, transparent fill (shows #b7ffb4 through), 20px padding. The card's own title rendered in its native family at 86px weight 400 #262626 line-height 1.0. Three-column grid.
5. *Section label*: left-aligned ' Section Name' in NaN Holo Mono 14px weight 400, #262626, 0.075em tracking, followed by 80px vertical space before content begins.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
