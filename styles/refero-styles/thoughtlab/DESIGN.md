# ThoughtLab Design Reference

## Essence

ThoughtLab feels like an executive research terminal built from black space and typographic force. It does not rely on rich illustration, gradients, or decorative UI. The page earns attention through pure contrast, huge uppercase text, crimson action points, and strict rectangular structure.

## Color System

Black Void is the page ground and primary surface. White is the dominant text color. Crimson Signal is the only real accent and should be used for primary actions, active states, and small emphasis marks. White Mist supports secondary text, while White Hairline and Glass Edge create subtle borders. Deep Gray and Mid Gray are low-emphasis structural tones. Do not add extra hues.

## Typography

Use Sui as the only type family when available. Use Inter, Helvetica Neue, or Arial as fallbacks. The system uses weight for structure but stays within one family. Display type is extremely large, uppercase, and tightly set. Body and UI text stay small and clean. Do not introduce a serif, mono, condensed sports face, or soft rounded family.

## Shape And Space

The geometry is hard-edged. Buttons, cards, inputs, images, and sections all use 0px radius. There are no shadows. Separation comes from hairlines, contrast, and negative space. Spacing is spacious: wide section gaps, large display areas, and sparse card grids.

## Layout Rhythm

Use black full-bleed sections with large left-aligned or edge-aware display text. Keep navigation minimal. Use transparent content cards with hairline borders rather than filled panels. Email capture fields and CTA rows are square and thin. Article grids can be dense, but they should still feel editorial and severe.

## Components

- Minimal header with black surface, white nav links, and a crimson action.
- Hero text stack with huge uppercase Sui display type.
- Crimson action button with square corners and white or black text depending on state.
- Transparent topic card with hairline border, no fill, and compact metadata.
- Hairline email input with black fill, white text, square corners, and crimson focus state.
- Editorial article grid with black surface, white titles, muted descriptions, and hairline separators.
- Large section number or label, used as an editorial marker.
- Footer link block with thin dividers and compact white or mist text.
- White hairline divider for structure.
- Filter or nav link row with active crimson text or underline.

## Implementation Direction

Start with a pure black canvas. Add a minimal header, one enormous display message, and one crimson CTA. Build content as transparent or near-black panels with hairline borders. Keep everything square. Avoid rounded cards, gradients, colorful illustrations, glowing effects, shadows, decorative data visuals, and soft SaaS styling.
