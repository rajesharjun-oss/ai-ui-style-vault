# Sprig

Source: [Refero Style](https://styles.refero.design/style/cbd8a058-6ecb-4f1b-9b5a-2bf2597826ee)
Reference site: [https://sprig.com](https://sprig.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:02:04.534Z
Refero modified: 2026-06-05T10:31:13.037Z
Theme: light
Category: SaaS

## Style Summary

Explore Sprig's light SaaS design system: Abyssal Ink #0b2330, Bone #faf9f8 colors, TT Commons Pro, ABC Diatype typography, and DESIGN.md for AI agents.

North star: editorial research notebook on warm paper - quiet, almost inkless, with warm light leaking in at the edges

## What To Borrow

- Abyssal Ink `#0b2330` for Primary text, nav links, borders, icon strokes - the workhorse near-black with a whisper of navy. Carries every reading surface in the system
- Bone `#faf9f8` for Page canvas, card surfaces, button text on dark fills - a warm off-white, never pure #fff
- Obsidian `#141312` for Headings, display text, strong UI fills - slightly warmer than Abyssal, used where headings need a touch more warmth
- Espresso `#272420` for Filled button background (primary action), dark surface sections - the primary CTA color, a warm near-black
- Carbon `#000000` for Absolute dark for SVG fills and the strictest contrast moments - used sparingly where true black is needed
- Ash `#f3f3f3` for Card surfaces, badge backgrounds, subtle elevated panels - the first step up from the canvas
- Mist `#e8e7e6` for Borders, dividers, secondary surface fills - a warm gray that defines edges without drawing attention
- Vapor `#dddcd9` for Lightest visible border, ghost button outlines - the quietest edge in the system
- Pebble `#c4c4bc` for Muted body text, subdued metadata, tertiary information
- Fog `#9a9a91` for Disabled text, placeholder text, very subdued heading accents
- Smoke `#8f8d8b` for Mid-tone surface fills, pressed button states
- Graphite `#6e6d6a` for Tertiary text, subtle borders, icon strokes in secondary contexts
- Slate `#575653` for Body text, nav borders, link underlines - the mid-neutral for readable secondary information
- Coffee `#322e2a` for Deep dark surface, image borders, the second-darkest fill - used in footer-adjacent surfaces and image frames
- Ember `#eba370` for Gradient mid-stop - coral-orange transition in the signature sunset gradient
- Twilight `#7d7a8f` for Gradient end - muted purple-gray closing the sunset gradient

- TT Commons Pro `--font-tt-commons-pro` for Functional UI typeface - nav links, button labels, badge text, small labels. Single weight 400 is a deliberate choice: the interface whispers instead of shouts. Used at 16-18px for UI chrome and at 40px for one rare editorial moment.
- ABC Diatype `--font-abc-diatype` for Editorial typeface - display headings at 40px weight 500, section headings at 32px weight 500, subheadings at 24px weight 400, body at 16px. The geometric construction gives the system its quiet authority; the weight 500 (not 600-700) for headings is the anti-convention choice that defines Sprig's restraint.

## Avoid

- Do not add drop shadows to any component - use surface tone shifts and curvature instead
- Do not introduce a secondary brand color - the system is monochrome plus warm gradient, and adding blue, green, or red breaks the editorial register
- Do not center body text or feature descriptions - left-alignment is structural, not stylistic
- Do not use border-radius below 4px on any visible element - the system commits to soft, never sharp
- Do not apply the warm gradient to text, icons, or UI controls - it is reserved for image backdrops and large decorative cards
- Do not use bold (weight 700) anywhere - ABC Diatype 500 is the maximum, TT Commons Pro is weight 400 only
- Do not alternate between light and dark section backgrounds to create rhythm - use hairline dividers and generous spacing instead

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
