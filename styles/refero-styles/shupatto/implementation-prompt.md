# AI Implementation Prompt

Build a Shupatto-inspired interface using this source-derived style bundle.

Reference site: https://www.shupatto.com/en
Theme: light
Category: E-commerce
North star: Museum vitrine on white marble

Use these palette anchors:

- Graphite `#2d2d2d` for Primary text, hairline borders, structural lines - the dominant neutral carrying all interface weight
- Ink `#000000` for Strongest text and most emphatic borders, logo dots, footer marks
- Paper `#ffffff` for Page canvas, card surfaces, nav backgrounds - the unbroken white field everything floats on
- Fog `#878887` for Muted helper text, secondary borders, dimmed metadata
- Periwinkle `#738ae5` for Sole chromatic accent - selected nav state, badge fills, a rare pressure point in an otherwise colorless system

Use these typography anchors:

- GillSansNova-Book `--font-gillsansnova-book` for Primary typeface for body, headings, nav, links, and icon-adjacent text - carries the entire English typographic system at a medium weight with wide tracking
- GillSansNova-SemiBold `--font-gillsansnova-semibold` for Emphasis and key headings - the bolder weight creates hierarchy without size inflation; the 8px variant carries micro-labels and badge text
- (Yu Gothic) `--font-yu-gothic` for Japanese text rendering - sits at the same metric scale as the English system, ensuring bilingual visual parity
- CezannePro-DB `--font-cezannepro-db` for Micro-decorative and brand-specific marks - a secondary display face for labels that need a different visual texture from the main Gill system
- GillSansNova-Medium `--font-gillsansnova-medium` for GillSansNova-Medium - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Hairline-Bordered Card: Universal content container
- Text-Nav Link: Navigation item
- Selected Nav Dot: Active state indicator
- Editorial Display Heading: Page title and section headers
- Micro-Label Badge: Category tags and product marks
- Product Grid Cell: Catalog item
- Hairline Divider: Section separator
- Ghost Body Link: Inline text link
- Sparse Footer Mark: Footer brand and meta
- Image Caption Label: Photo or product caption

Do:

- Use uppercase with letter-spacing 0.07em for all interface text - this tracking is the typographic signature, not the weight or size
- Separate content containers with 1px #2d2d2d or #000000 hairline borders, never with background fills or shadows
- Keep the 3px border-radius for every rounded element - a sharper, more architectural system than the common 8-16px
- Limit color to the neutrals plus periwinkle #738ae5; let the periwinkle appear on at most 1-2 elements per view as a quiet accent
- Set body text at 16-18px with 1.22-1.33 line-height and 0.07-0.1em letter-spacing for an editorial gallery feel
- Use GillSansNova-SemiBold (weight 800) at 8px with 0.119em tracking for all micro-labels, badges, and category stamps
- Apply the "palt" font-feature setting globally - it optimizes proportional alternates and is non-negotiable for the brand's typographic identity

Avoid:

- Do not introduce shadows, gradients, or any form of elevation - the design system is flat by philosophy
- Do not add bright or saturated colors beyond #738ae5; even secondary accents should stay neutral
- Do not use border-radius above 3px; avoid pill shapes and large rounded corners
- Do not set type in mixed case or normal letter-spacing; everything reads as editorial display via tracking
- Do not fill cards or sections with tinted backgrounds; rely on hairline borders to create structure on the white canvas
- Do not use large display type below 28px or above 32px - the scale is deliberately compressed and quiet
- Do not add icons with weight above 1px stroke; icons are absent or drawn as the thinnest possible lines

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
