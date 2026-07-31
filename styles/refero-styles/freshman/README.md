# Freshman

Source: [Refero Style](https://styles.refero.design/style/a6284fcd-fa69-4469-ac40-4239e5b84a39)
Reference site: [https://freshman.tv](https://freshman.tv)
Captured: 2026-07-31
Refero published: 2026-04-30T00:20:59.021Z
Refero modified: 2026-06-05T08:13:24.569Z
Theme: dark
Category: Media

## Style Summary

Explore Freshman's dark Media design system: Pure White #ffffff, Carbon Black #000000 colors, Editorial New, TT Firs Neue typography, and DESIGN.md for AI...

North star: cinema title card on black velvet

## What To Borrow

- Pure White `#ffffff` for Primary text, logotype fill, border strokes, and the dominant foreground on the dark canvas - carries 92% of all color instances
- Carbon Black `#000000` for Base canvas and primary background - the default surface for every page
- Charcoal Shale `#101010` for Secondary surface for icon wells, sub-panels, and slight tonal lift above the pure-black canvas
- Signal Red `#ff2936` for Sparingly-applied accent for active states, marquee highlights, and high-emphasis punctuation - used as a single saturated note against the monochrome system

- Editorial New `--font-editorial-new` for Hero and headline display - the ultralight weight 200 is anti-convention; combined with the 20px breakpoint it reads as editorial print rather than web UI
- TT Firs Neue `--font-tt-firs-neue` for Workhorse UI and body sans - the only geometric grotesque in the system, anchors the project ticker labels, menu trigger, and utility text
- Altform `--font-altform` for Compact meta and condensed labels - tight 0.86-0.88 line-height and -0.03em tracking make it read like a festival credit roll
- Wasted Year `--font-wasted-year` for Signature editorial flourishes - bracket-wrapped taglines and small accent phrases; its hand-set quality is used for personality, not information density

## Avoid

- Do not introduce shadows, gradients, or elevation of any kind - flatness is the system
- Do not add card backgrounds or rounded corners; all surfaces are 0px radius on the black canvas
- Do not use bold or semibold weights for headlines - the weight 200 Editorial New is the anti-convention that defines the brand
- Do not use #ff2936 as a button fill or large background block - it loses all impact if used at scale
- Do not add a secondary navigation, breadcrumbs, or page tabs - the MENU trigger and the reel are the entire IA
- Do not set body copy above 16px or below 14px - the type scale is deliberately tight
- Do not alternate between light and dark sections; the page is uniformly dark, depth comes from type scale not surface color

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
