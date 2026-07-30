# Framer

Source: [Refero Style](https://styles.refero.design/style/242db326-a6f3-482a-b12e-5e7f8af94981)
Reference site: [https://www.framer.com](https://www.framer.com)
Captured: 2026-07-30
Refero published: 2026-04-29T00:26:17.096Z
Refero modified: 2026-06-05T12:41:45.479Z
Theme: dark
Category: Design

## Style Summary

Explore Framer's dark Design design system: Void #000000, Carbon #080808 colors, sans-serif, GT Walsheim typography, and DESIGN.md for AI agents.

North star: cinematic black gallery. Pure black canvases cradle white editorial type and one electric blue accent that traces edges rather than filling space.

## What To Borrow

- Void `#000000` for Page background, primary canvas - the void that everything else sits on. Also used for filled primary buttons, nav background, card borders, and the vast majority of interface borders
- Carbon `#080808` for Card surface layer, elevated panels, secondary background - barely lifted from the void to suggest depth without leaving the dark family
- Obsidian `#111111` for Higher elevation cards and modal surfaces - the second step up from the page
- Graphite `#171717` for Top-tier surface for popovers, tooltips, and deeply nested panels
- Slate `#242424` for Mid-tone fills, hover states, subtle panel backgrounds
- Fog `#333333` for Button hover, pressed states, and darker UI fills
- Ash `#666666` for Muted text, secondary labels, disabled states, subtle borders
- Smoke `#8c8c8c` for Helper text, tertiary metadata, thin dividers
- Silver `#999999` for Secondary text, body copy at lower emphasis, border dividers
- Bone `#cccccc` for Light borders, subtle dividers on dark surfaces
- Paper `#ffffff` for Primary text, headings, filled button backgrounds, light-on-dark iconography - the dominant foreground against the void
- Deep Harbor `#021f33` for Deep blue-black for box-shadows and subtle tinted surface washes - carries the brand's cool undertone into elevation
- Electric Cyan `#0099ff` for Brand accent: link underlines, active nav state, focus rings, outlined button borders, decorative card borders, and text selection - appears only on edges and micro-states, never as a fill

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- GT Walsheim `--font-gt-walsheim` for Display and hero headlines. The ultra-condensed geometric character with aggressive negative tracking at 85-110px creates the editorial, almost cinematic weight that defines Framer's voice. At 110px the line-height compresses to 0.85, letting the headline feel like a single block of mass. Substitute: Inter Tight or Mona Sans as a free alternative.
- Inter Variable `--font-inter-variable` for Primary UI and body font. The extensive character variant alternates (cv01-cv11, ss02-ss07) tune individual glyphs - switching between straight and curved tails, alternate g shapes, and stylistic sets depending on context. Body text uses subtle negative tracking (-0.01em to -0.02em); uppercase labels use positive tracking (0.03em). Substitute: Inter (Google Fonts) with matching feature settings.
- Inter `--font-inter` for Secondary text, nav items, links, form labels, and button text. Weights 500-700 for emphasized UI elements. Tracking tightens dramatically at larger sizes (22px at -0.05em). Substitute: Inter from Google Fonts.
- Mona Sans `--font-mona-sans` for Secondary display and text accents. Used at 62px for section headers, with extremely tight tracking (-0.05em) giving it a dense, graphic feel. Substitute: Mona Sans (GitHub).
- Open Runde `--font-open-runde` for Micro-labels and oversized tagline micro-text. Substitute: Inter at 600 weight.
- GT Walsheim Framer Medium `--font-gt-walsheim-framer-medium` for GT Walsheim Framer Medium - detected in extracted data but not described by AI

## Avoid

- Don't introduce any background color other than the black-to-charcoal surface stack - no grays, no tinted backgrounds, no warm tones
- Don't use Electric Cyan (#0099ff) as a filled button background - it is an edge accent only
- Don't use box shadows with offset greater than 10px on regular cards - the design is flat-by-default
- Don't set border-radius below 8px on any container - the minimum visual softness is 8px
- Don't use font-weight above 500 for display type - GT Walsheim at 500 is already commanding; going heavier breaks the voice
- Don't add decorative gradients, glows, or colored backgrounds to sections - sections transition through pure black
- Don't use color for body text - keep all text in #ffffff, #999999, or #666666 only

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
