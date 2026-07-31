# Sackville

Source: [Refero Style](https://styles.refero.design/style/8a3d3f72-9ef0-466d-adde-77189ddff797)
Reference site: [https://sackville.co](https://sackville.co)
Captured: 2026-07-31
Refero published: 2026-04-30T02:21:06.772Z
Refero modified: 2026-06-05T08:51:42.721Z
Theme: light
Category: E-commerce

## Style Summary

Explore Sackville

North star: Cobalt zine pressed onto cream - a hand-inked editorial spread where the illustration is the hero and the UI is just typeset text on warm paper.

## What To Borrow

- Cream Paper `#f3f4ee` for Page canvas, card surfaces - the warm off-white that makes every ink color feel like print
- Bone White `#f8f8f8` for Alternate surface wash, subtle section differentiation from the cream canvas
- Press Black `#231f20` for Primary text, borders, dividers, icon strokes - the near-black ink that anchors every screen
- Charcoal Headline `#383435` for Display heading text - slightly lifted from press black for softer masthead weight
- Mid Gray `#9a9a9a` for Muted helper text, hairline borders, secondary metadata
- Pure Black `#000000` for Icon fills, maximum-contrast borders, nav accent
- Cobalt Ink `#245dc5` for Primary brand color - illustrated duotone wash, outlined action borders, interactive text - saturated blue against cream creates the risograph-print signature
- Peach Wash `#ffc6a6` for Secondary illustration accent, decorative borders, warm tonal fill - the cheek-pink of risograph layering
- Fire Red `#f04736` for Outlined action borders, emphasis strokes, error-like accent - used as editorial red rather than as a functional error state
- Vermillion `#f52302` for Deep red-orange accent for borders and fills - the warmest ink in the riso palette
- Crimson `#d42121` for Deep red accent - used sparingly in illustration washes and emphasis borders
- Marigold `#feee71` for Yellow accent fill, spot-color highlights, decorative emphasis - the third riso plate
- Terracotta `#b45e42` for Warm brown accent for body and heading borders - the earthiest ink in the editorial palette

- FoundersGrotesk `--font-foundersgrotesk` for Workhorse type for everything from body to display - single weight 400 with no bold variants means hierarchy is created purely through size, line-height, and letter-spacing, not weight contrast. The aggressive negative line-heights (0.80 at 130px) create magazine-cover masthead pressure. Substitute: Neue Haas Grotesk, Inter, Sohne.
- TimesNow SemiLight `--font-timesnow-semilight` for Editorial serif contrast for select headings and navigation - a humanist serif breaks the grotesque monotony at key moments, creating the magazine-section-divider effect. Substitute: Times Now, Tiempos, Source Serif.
- Sackville Script (hand-drawn wordmark) `--font-sackville-script-hand-drawn-wordmark` for Custom hand-inked cursive used only for the brand wordmark - overlaid on illustrations and hero compositions. Not a UI font. No substitute; this is the signature mark.

## Avoid

- Do not fill any button with Cobalt Ink, Fire Red, or any chromatic color - the system is outlined-action only; filled buttons would break the zine aesthetic
- Do not introduce box-shadows, drop-shadows, or any elevation effects - the design is flat by principle; depth comes from color contrast and illustration density, not from blur or offset
- Do not use a white (#ffffff) canvas - the cream (#f3f4ee) is warmer and is the reason the ink colors read as print rather than screen
- Do not set body text in the serif TimesNow SemiLight - it is a display contrast font only; body copy stays in FoundersGrotesk 400
- Do not apply bold or semibold weights - the type system is single-weight (400) by design; hierarchy is size and line-height, never weight
- Do not round cards or images beyond 10px - the 50px and 81px radii are reserved for buttons and the oval action; everything else stays close to sharp
- Do not add gradients, blurs, or glow effects to any element - the palette is risograph-flat; any smooth tonal transition breaks the print illusion

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
