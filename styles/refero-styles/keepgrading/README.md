# KeepGrading

Source: [Refero Style](https://styles.refero.design/style/2f0a053b-0596-4212-a4f4-8a7b580acb90)
Reference site: [https://www.keepgrading.com](https://www.keepgrading.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:09:47.925Z
Refero modified: 2026-06-05T10:11:06.590Z
Theme: dark
Category: Agency

## Style Summary

Explore KeepGrading's dark Agency design system: Studio White #f8f8f8, Void Black #080808 colors, Cabinet Grotesk, Inter typography, and DESIGN.md for AI...

North star: Polaroids scattered in a darkroom

## What To Borrow

- Studio White `#f8f8f8` for Primary text, ghost-button borders, image-frame outlines, nav icon strokes - the single light voice in a dark room
- Void Black `#080808` for Page canvas, behind-everything background, image frame fills between photographs
- Pure Black `#000000` for SVG icon fills, deepest surface layer for inline graphics and decorative marks
- Bone White `#f0f0f0` for Soft secondary text and supporting hairline strokes when pure white feels too clinical
- Pewter Border `#2a2a2a` for Low-contrast dividers and inactive frame edges that recede against the void

- Cabinet Grotesk `--font-cabinet-grotesk` for Brand display and logo wordmark - the 96px headline weight 400 is anti-convention; no bold, no display tricks, just a single weight carried to monumental size that feels confident through restraint. Also used at 24px for short subheadings and 16px for nav labels. This custom typeface carries the entire brand identity.
- Inter `--font-inter` for Body text and supporting copy at 16px and 20px, both at weight 400 - no bold variant in use, the system keeps a single weight even for emphasis, letting size and color do the hierarchy work

## Avoid

- Do not introduce any chromatic brand color, accent, or gradient - the monochrome void is the brand.
- Do not add drop shadows, glows, or any elevation effects - depth comes from layering and contrast alone.
- Do not use bold (600+) or semibold weights for emphasis; switch size or color instead.
- Do not use sharp corners (0-8px radius) on any visible element - all surfaces must be pill-rounded or softly curved.
- Do not apply background fills to buttons; the ghost outlined style is the only button treatment.
- Do not constrain the page to a max-width column; the full-bleed black canvas is essential to the darkroom feel.
- Do not add icons, badges, or decorative graphics to the UI chrome - type, borders, and photographs are the only visual elements.

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
