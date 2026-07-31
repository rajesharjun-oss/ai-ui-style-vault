# Duolingo

Source: [Refero Style](https://styles.refero.design/style/95b472c5-fc07-46a8-a11f-c5432e290fcd)
Reference site: [https://www.duolingo.com](https://www.duolingo.com)
Captured: 2026-07-31
Refero published: 2026-04-29T00:46:37.746Z
Refero modified: 2026-06-05T11:37:59.917Z
Theme: light
Category: SaaS

## Style Summary

Explore Duolingo's light SaaS design system: Ecto Green #58cc02, Lingot Lime #a5ed6e colors, din-round, feather typography, and DESIGN.md for AI agents.

North star: Green playground with thick marker outlines

## What To Borrow

- Ecto Green `#58cc02` for Green outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color
- Lingot Lime `#a5ed6e` for Outlined-action border and link accent - used as the chromatic border on link and button elements in 256+ instances. The lighter green outline gives interactive elements a glowing, highlighter-pen quality against white backgrounds
- Eel Light `#d7ffb8` for Soft highlight and pale border - lightest green used for card outlines, soft surface washes, and the bottom shadow border on filled green buttons to create a 3D pressable effect
- Macaw Blue `#1cb0f6` for Secondary action accent - body borders, link text, and outlined button borders for secondary actions like language-specific CTAs. The cyan-blue sibling to the green system, signaling alternative or complementary actions
- Eel Dark Blue `#042c60` for Deep heading text and border - navy blue used for emphasis headings and key border treatments, providing weight and contrast without competing with the green primary
- Midnight `#000437` for Dark surface and button text - near-black violet used for dark-surface sections and as button label text on green fills
- Graphite `#3c3c3c` for Dominant neutral border - the workhorse gray used for hundreds of list and card borders throughout navigation, lists, and structural dividers. Not a background, a border system
- Ash `#777777` for Secondary text and nav borders - medium gray for navigation chrome, secondary text labels, and subtle structural borders
- Charcoal `#4b4b4b` for Body text and icon borders - darker gray for body copy and icon outlines, sitting between the lighter Ash and the darker structural Graphite
- Paper `#ffffff` for Page and card surface - the white canvas on which all content sits. Also used as text on dark surfaces and as border color for ghost buttons
- Ink `#000000` for Pure black for SVG illustration fills and maximum-contrast text where needed

- din-round `--font-din-round` for Primary UI typeface - used for body text, navigation, buttons, links, lists, and smaller headings. The rounded terminals and friendly weight create an approachable, educational tone. Weight 500 for body, weight 700 for emphasis and button labels. The +0.053em letter-spacing is wider than typical, giving text a breezy, open feel.
- feather `--font-feather` for Display face for large feature headlines - bold, heavy, and tight (letter-spacing: -0.02em). Reserved exclusively for oversized section headlines. The extreme weight contrast against the lighter din-round body creates a shout/whisper rhythm: feather headlines announce, din-round explains.

## Avoid

- Do not use drop shadows on any element - depth comes from solid borders, never from blurred shadow stacks
- Do not use gradients - the system is strictly flat solid colors with no gradient transitions
- Do not use card containers with background fills or box-shadows - sections are separated by white space alone
- Do not set body radius below or above 12px - the system has exactly one radius value and it should be used uniformly
- Do not use feather for body text or anything under 32px - it is exclusively a display face for oversized headlines
- Do not introduce new accent colors outside the established palette of green, blue, dark blue, and midnight
- Do not use the light green #a5ed6 as a filled background - it is exclusively a border/outline color

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
