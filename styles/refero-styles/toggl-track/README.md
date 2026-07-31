# Toggl Track

Source: [Refero Style](https://styles.refero.design/style/813be405-c2b9-41be-9864-7b53d66483dc)
Reference site: [https://toggl.com](https://toggl.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:58:09.944Z
Refero modified: 2026-06-05T09:29:31.713Z
Theme: mixed
Category: Productivity

## Style Summary

Explore Toggl Track's mixed Productivity design system: Plum #2c1338, Heather #412a4c colors, Inter, GT Haptik typography, and DESIGN.md for AI agents.

North star: Plum theater marquee - a deep aubergine stage where a single magenta spotlight word illuminates each headline.

## What To Borrow

- Plum `#2c1338` for Hero, header, and footer canvases; brand mark background. Near-black aubergine that reads as the brand's signature dark
- Heather `#412a4c` for Primary headings and UI text on light surfaces; secondary dark surface when Plum is too heavy. The workhorse purple
- Magenta `#e57cd8` for Filled CTA buttons, emphasis words inside headlines, selected nav state, star ratings, and decorative dots. The only vivid hue - rationed to one word or one control per screen
- Lavender Smoke `#564260` for Body copy and link text on warm-white surfaces where Heather would feel too heavy. Carries the brand tint into running text
- Dusty Mauve `#6b5a74` for Secondary body text, descriptions, helper text, and muted icon strokes on light surfaces. Desaturated enough to recede behind headings
- Stone Violet `#817187` for Borders and dividers on light surfaces; button borders for outlined variants; disabled or placeholder text
- Ink `#000000` for Primary text and high-contrast borders on light surfaces; footer text on dark Plum
- Bone `#fefbfa` for Page background for all content sections, card surfaces, and text color on dark Plum headers
- Silver `#d5d0d7` for Hairline borders, list separators, and input outlines across cards and tables. The structural neutral grid
- Fog `#c0b8c3` for Subtle borders and dividers where Silver reads too dark; secondary placeholder text on inputs
- Blush `#fdeae2` for Soft warm wash for icon fills, decorative card backgrounds, and nav hover states. The warmest surface tint
- Petal `#fcf1f8` for Elevated card and modal surfaces above Bone. Carries a pink whisper without competing with Magenta
- Orchid Mist `#fae5f7` for Highlighted card background for featured or selected content blocks
- Bubblegum Wash `#f7d8f3` for Pale pink surface for secondary buttons, tag backgrounds, and the softest brand-tinted fill
- Amber `#ffde91` for Yellow action color for filled buttons, selected navigation states, and focused conversion moments.

- Inter `--font-inter` for All body copy, navigation links, UI labels, table data, and secondary headings. Inter's neutrality keeps the content calm while GT Haptik performs on the headlines. Weight 500 for nav and buttons, 700 for subheadings, 800 for compact stat callouts.
- GT Haptik `--font-gt-haptik` for Display headlines and large section titles. GT Haptik's geometric warmth with rounded terminals gives the brand a friendly, non-corporate voice; weight 700 at 43-69px with tight 1.1 line-height creates dense, confident heroes. Substitute: Inter Tight, Manrope, or Outfit.
- GT Haptik Rotalic `--font-gt-haptik-rotalic` for The single highlighted word inside every hero and section headline - rendered in Magenta (#e57cd8) with a right-leaning italic slant. This is the brand's theatrical signature: one word per headline gets the spotlight. Substitute: Inter Tight Italic with manual skew, or Manrope Italic.
- GT Haptik Medium Rotalic `--font-gt-haptik-medium-rotalic` for GT Haptik Medium Rotalic - detected in extracted data but not described by AI

## Avoid

- Don't use drop shadows on cards, buttons, or modals - the design language is flat with surface tint contrast instead.
- Don't set the pink emphasis word in upright GT Haptik - it must be in the Rotalic variant to carry the theatrical meaning.
- Don't use Magenta as a background wash, gradient, or large surface fill. It only appears on filled buttons, emphasis words, and small dots.
- Don't introduce a second accent hue. The system is monochromatic purple with one spotlight pink - adding teal, green, or orange breaks the duotone.
- Don't use pure white (#ffffff) for backgrounds - Bone (#fefbfa) is the canvas. Pure white reads as cold and unbranded against the warm tints.
- Don't apply corner radii smaller than 10px or larger than 200px. The system has three: 10px (cards/inputs), 26px (buttons), 200px (pills).
- Don't set display headlines above 1.25 line-height - loose leading makes GT Haptik feel airy and undermines the dense, confident voice.

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
