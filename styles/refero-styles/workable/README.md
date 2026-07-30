# Workable

Source: [Refero Style](https://styles.refero.design/style/0ab4c544-6147-4998-8365-3a0f6191e54f)
Reference site: [https://www.workable.com](https://www.workable.com)
Captured: 2026-07-30
Refero published: 2026-04-30T00:53:19.366Z
Refero modified: 2026-07-03T11:20:35.628Z
Theme: light
Category: SaaS

## Style Summary

Explore Workable's light SaaS design system: Workable Ink #0f161e, Page Canvas #fbfaf8 colors, Proxima Nova typography, and DESIGN.md for AI agents.

North star: warm newsroom with teal ink

## What To Borrow

- Workable Ink `#0f161e` for Headlines, body copy, icon fills, dark UI surfaces - near-black with a blue-ink undertone, softer than pure black
- Page Canvas `#fbfaf8` for Default page background and warm card surface - slightly cream-tinted off-white that gives the whole site a paper-like warmth
- Pure White `#ffffff` for Elevated card surfaces on warm canvas, nav background - true white used sparingly for crisp product panels against the cream page
- Body Graphite `#3d3e45` for Body paragraph text, secondary link color - softened dark gray for readable prose without the weight of ink-black
- Muted Slate `#6f7073` for Eyebrow labels, helper text, metadata - medium gray for de-emphasized copy like section kickers and timestamps
- Hairline Gray `#efefef` for Disabled button background, subtle dividers - the lightest neutral surface
- Forest Teal `#004038` for Teal text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Midnight Violet `#1d0953` for Secondary action (Check it out pill), stat callout headings - deep indigo-violet used sparingly for the announcement bar and number highlights
- Lavender Wash `#e5d3f7` for Soft feature card background - pastel lavender for the most prominent colored card surface, gives sections a calm purple identity
- Peach Cream `#fef1e1` for Section background wash, hero-adjacent panels - warm peach-cream used as a large surface band, the dominant chromatic neutral
- Butter Yellow `#fde8ce` for Card background for warm-themed feature panels - muted butter for secondary colored cards
- Periwinkle `#c6c4f4` for Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Sky Tint `#bee9f4` for Cool-tone card background - pale sky blue for variety in the pastel card rotation

- Proxima Nova `--font-proxima-nova` for Single sans family carries all UI - bold 700 at 56-72px with tight 1.14 line-height creates editorial display weight, while 400 at 18-20px with 1.56-1.67 line-height keeps body comfortable. The Minor Third scale (1.2 ratio, 16px base) produces a restrained 8-step hierarchy.

## Avoid

- Don't add drop shadows to cards or buttons - the system is intentionally flat, depth comes from surface color contrast only
- Don't use #1d0953 Midnight Violet as a general CTA - it's reserved for the announcement bar pill and number callouts, not buttons
- Don't apply the teal lime violet gradient to buttons, backgrounds, or text - it's only for the Workable 'w' app icon and AI-agent visuals
- Don't use #0f161 ink for body paragraphs - reserve it for headlines, icons, and UI chrome; use #3d3e45 for readable prose
- Don't introduce additional saturated accent colors - the system is built on teal + pastel rotation; adding a new hue breaks the restrained palette
- Don't use sharp 0px or 4px radius on cards - the 16px softness is a signature, all elevated surfaces should feel rounded
- Don't set body line-height below 1.5 - the generous 1.56 line-height at 18px is what makes the dense type feel airy

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
