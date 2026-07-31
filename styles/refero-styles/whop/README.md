# Whop

Source: [Refero Style](https://styles.refero.design/style/9eeab5f0-eece-4898-a1d2-2db48ac2bc7d)
Reference site: [https://whop.com](https://whop.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:52:13.446Z
Refero modified: 2026-06-05T11:02:10.359Z
Theme: light
Category: SaaS

## Style Summary

Explore Whop's light SaaS design system: Ember Orange #fa4616, Ember Shadow #b62600 colors, acidGrotesk, Inter typography, and DESIGN.md for AI agents.

North star: Bold sticker on cream paper - a minimal light canvas with a single orange button that casts a hard burnt-orange shadow.

## What To Borrow

- Ember Orange `#fa4616` for Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Ember Shadow `#b62600` for Hard 3px offset shadow beneath Ember Orange buttons - a deeper burnt orange instead of a soft drop shadow
- Carbon `#202020` for Primary text, heading strokes, heavy borders, icon fills
- Snow `#ffffff` for Card surfaces, button text on dark fills, the elevated layer above the page canvas
- Mist `#f9f9f9` for Page canvas - the near-white background that all sections sit on
- Silver `#e1e4e8` for Hairline dividers, card borders, subtle structural separators
- Slate `#646464` for Muted body text, secondary links, inactive nav items, mid-weight borders
- Ash `#838383` for Tertiary text, placeholder text, disabled labels
- Pearl `#bbbbbb` for Light borders, icon outlines, low-emphasis strokes
- Obsidian `#0a0a0a` for Dark surface variant for inverted cards or code-editor panels

- acidGrotesk `--font-acidgrotesk` for Display and section headlines - used at near-mega sizes (128px) for hero, 56px for section titles. Line-height locked to 1.00, tracking at -0.03em creates a compressed, poster-like quality. This is a custom geometric face; no system font replicates its personality.
- Inter `--font-inter` for All functional UI: body copy, links, buttons, nav, footer, card text, labels. Weight 400 for body, 500 for buttons and emphasized text, 600-700 for subheadings and strong labels. Tracking tightens as size increases (-0.016em at 20px down to -0.006em at 13px).
- Geist Mono `--font-geist-mono` for Code snippets, terminal prompts, technical metadata, version labels. Generous line-height (1.70) for multi-line code blocks. Normal letter-spacing - mono fonts don't need optical tightening.

## Avoid

- Don't use Ember Orange for any element that isn't the primary action button on that screen
- Don't apply soft drop shadows, blur, or opacity-based shadows to any element - the system is flat
- Don't use display sizes (56px+) in Inter - Inter is for 13-20px functional UI only
- Don't add gradients - the system is entirely flat color
- Don't use neutral grays for decorative accents or illustrations - the palette is near-black to near-white with one orange
- Don't set border-radius values outside the four tokens: 4px, 8px, 12px, 16px, 24px
- Don't place multiple orange buttons on the same screen - one primary action per view

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
