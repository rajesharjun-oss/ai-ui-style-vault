# Symbolic.ai

Source: [Refero Style](https://styles.refero.design/style/694723e9-0df7-4b9f-ba07-83fc598532d6)
Reference site: [https://symbolic.ai](https://symbolic.ai)
Captured: 2026-07-30
Refero published: 2026-04-30T00:18:51.694Z
Refero modified: 2026-07-03T15:42:55.000Z
Theme: light
Category: AI

## Style Summary

Explore Symbolic.ai's light AI design system: Canvas Cream #fdfcf5, Ink Black #000000 colors, sans-serif, Suisse Works typography, and DESIGN.md for AI agents.

North star: editorial newsroom on cream paper. A broadsheet masthead in serif type, floating on warm off-white stock, with soft tan shadows that make every card feel like it was set in letterpress - not rendered.

## What To Borrow

- Canvas Cream `#fdfcf5` for Primary page canvas and white card surfaces.
- Ink Black `#000000` for Primary text, hairline borders, icon strokes, and the single CTA fill - black-on-cream is the system's only action color, no chromatic buttons
- Paper White `#ffffff` for Card surfaces, elevated content layers, input fills - the brighter sheet the cream canvas holds
- Charcoal `#4c4c4a` for Secondary borders, muted body text, link underline tones
- Slate Black `#333231` for Strong secondary borders and slightly softer heading text - separates structural dividers from Ink Black
- Warm Gray `#7f7e7b` for Captions, helper text, disabled states, tertiary borders
- Mid Stone `#656562` for Muted body copy and secondary dividers
- Soft Sand `#f5f3e9` for Subtle section bands, recessed surfaces, and the lighter shadow base
- Khaki Shadow `#edeadd` for The warm shadow tint used across all card elevations - replaces standard cool gray
- Sandstone `#e5e2d0` for Faint horizontal rules and gentle background tints
- Lavender Mist `#e2e0e4` for Cool-leaning hairline borders, subtle separation lines
- Editorial Teal `#10756a` for Teal wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- AI Violet `#6938ef` for Violet outline accent for tags, dividers, and focused UI edges.
- Deep Violet `#6a27d9` for Dark-mode variant of AI Violet for borders and stronger emphasis on processing states
- Stamp Red `#f42c2b` for Red wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Suisse Works `--font-suisse-works` for Editorial serif for all headlines and display type - Book (450) carries the masthead voice at 28-58px, Medium (500) for sub-headings at 20px. Suisse Works' high contrast and sharp serifs give the interface a printed-broadsheet authority that no sans could replicate.
- Open Runde `--font-open-runde` for Humanist sans for body, navigation, links, and most UI labels. Open Runde's slightly rounded geometric forms soften the editorial serif above - Regular (400) for body, Semibold (600) for nav emphasis, Bold (700) for inline labels. The wide x-height at 16px with 1.63 line-height creates comfortable reading density.
- Geist Mono `--font-geist-mono` for Monospaced labels for product state indicators ('Rewriting...', 'Transcribing...') and technical metadata. Geist Mono at 14px is intentionally small - it's a whisper of machinery inside the editorial voice, not a visual block.
- Grenze Gotisch `--font-grenze-gotisch` for Decorative blackletter for stamp-style elements like 'For Immediate Release'. Used once or twice per screen as accent texture, never for body. The gothic contrast against Suisse Works' modern serif is the system's signature historical flourish.
- Inter `--font-inter` for Minor fallback for non-primary UI labels where Open Runde is unavailable

## Avoid

- Don't introduce chromatic CTA buttons - black-on-cream is the system's only action language
- Don't use pure white (#ffffff) as a page background - the cream canvas (#fdfcf5) is the entire atmosphere
- Don't apply cool gray shadows (rgba(0,0,0,...)) - all elevation must use the warm khaki base
- Don't mix sans-serif into headlines above 20px - the serif/sans split is structural, not decorative
- Don't use Stamp Red (#f42c2b) for buttons, errors, or destructive actions - red is reserved for editorial stamp accents only
- Don't flatten the type scale - Suisse Works Book (450) is the headline weight; don't promote to Bold (700) for emphasis, use size and line-height instead
- Don't add drop shadows stronger than 0.4 opacity - the system never goes beyond a soft printed-paper lift, never a hovering UI panel

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
