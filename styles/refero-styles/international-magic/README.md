# International Magic

Source: [Refero Style](https://styles.refero.design/style/c406697b-677f-40c7-a3a2-10ea545278f1)
Reference site: [https://intmagic.com](https://intmagic.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:24:53.568Z
Refero modified: 2026-06-05T11:20:26.934Z
Theme: dark
Category: Agency

## Style Summary

Explore International Magic's dark Agency design system: Void #0a0a0a, Chalk #f7f7f7 colors, Wand UI Pro typography, and DESIGN.md for AI agents.

North star: midnight gallery wall - a single spotlight, a piece of work, and a wall of black velvet

## What To Borrow

- Void `#0a0a0a` for Page background, primary canvas - the dark field that holds every piece of work
- Chalk `#f7f7f7` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Ivory `#ebebeb` for Button labels and button borders - marginally warmer than Chalk, used on neutral pill buttons to feel pressed but not clinical
- Ash `#7c7c7c` for Secondary link and body text, subdued dividers - mid-gray for de-emphasized type that still needs to read
- Graphite `#4d4d4d` for Heading borders and low-emphasis heading text - darker mid-gray that recedes behind primary Chalk type
- Smoke `#707070` for Badge text - sits between Ash and Charcoal, calm and unreadable as ornament
- Steel `#616161` for Badge borders - paired with Smoke text for outlined tag affordance
- Charcoal `#585858` for Elevated surface for the single neutral filled button - barely lighter than Void so the button whispers rather than shouts

- Wand UI Pro `--font-wand-ui-pro` for Sole typeface - used for everything from 96px display headlines down to 10px badge labels. The 475 and 550 weights are the workhorses; 650 is reserved for emphasis. The font is custom but has the personality of a contemporary geometric grotesk with subtle humanist warmth, tight apertures, and a tall x-height.

## Avoid

- Don't introduce any hue - no blue, no red, no warm grays with chroma. The page is 0% colorful by design.
- Don't add a filled primary-color CTA. Actions stay ghost (outlined Ivory) or neutral-charcoal.
- Don't use sharp 0-4px corners on device or card surfaces - the 24px radius is what makes the dark canvas feel soft.
- Don't crowd sections. If vertical space between blocks drops below 80px, the void stops working.
- Don't use weights above 650 in Wand UI Pro; the type system caps there and going heavier breaks the quiet voice.
- Don't add secondary shadows, colored shadows, or border-glow effects to lift work - the 64/72/25% ambient shadow is the only elevation.
- Don't left-align hero content. Every headline, subtitle, badge, and CTA in the main column is centered.

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
