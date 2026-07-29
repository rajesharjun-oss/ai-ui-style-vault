# Goodnotes

Source: [Refero Style](https://styles.refero.design/style/c7fe6b78-9ce3-4d69-a3f0-b8310c779e7a) 
Reference site: [https://www.goodnotes.com](https://www.goodnotes.com) 
Captured: 2026-07-29 
Refero published: 2026-05-11T13:17:05.983Z 
Refero modified: 2026-06-05T08:17:03.049Z 
Theme: light 
Category: Productivity

## Style Summary

Explore Goodnotes's light Productivity design system: Pure Canvas #ffffff, Midnight Ink #000000 colors, Roobert, Font Awesome 6 Brands typography, and...

North star: Paper-white command canvas - a blank notebook page where every tool snap into place without decoration.

## What To Borrow

- Pure Canvas `#ffffff` for Page background, card backgrounds, button text on cyan CTA
- Midnight Ink `#000000` for Primary headlines, body text, borders on UI chrome
- Deep Charcoal `#1e1e1e` for Ghost button text and borders, secondary headings, icon strokes
- Graphite `#111213` for Dark nav backgrounds, dark section surfaces, link text in dark contexts
- Slate `#565656` for Body copy on cards, secondary descriptive text
- Fog `#888889` for Muted helper text, captions, de-emphasised labels
- Ash `#666666` for Tertiary text, subtle UI labels
- Steel `#333333` for Badge text, mid-weight secondary content
- Border Medium `#e8e8e8` for Tab underlines, nav separators, light hairline dividers
- Border Soft `#bebebe` for Card outlines, modal borders, container edges
- Aqua Spark `#57d2ee` for Blue action color for filled buttons, selected navigation states, and focused conversion moments.
- Teal Deep `#45bfdb` for Brand surface wash, teal background sections
- Cyan Mist `#bcedf8` for Outlined button borders, soft teal ring accents
- Cyan Text `#6dd9f2` for Blue outline accent for tags, dividers, and focused UI edges.
- Sky Link `#0299e0` for Hyperlinks and underline accents in body copy
- Highlighter Yellow `#f2e6b3` for Text highlight wash - mimics physical highlighter pen on note-taking UI screenshots

- Roobert `--font-roobert` for Single-font system - every piece of UI copy, from 10px captions to 48px hero headlines, is Roobert. The rounded geometric forms mirror the tablet/handwriting brand; weight 700 at 48px with -0.05em tracking creates dense, close-set display text that reads like a confident pencil stroke rather than a digital shout.
- Font Awesome 6 Brands `--font-font-awesome-6-brands` for Social/brand icon glyph set used in badges and footer; monochromatic, no resizing

## Avoid

- Never add box-shadow to cards, modals, or buttons - all surface separation must come from borders, not elevation.
- Never use a second chromatic fill color for buttons; ghost (#1e1e1 border) and tinted-teal (rgba(87,210,238,0.1)) variants must stay visually subordinate to the cyan CTA.
- Never set headline letter-spacing to 0 or positive values at sizes above 24px - the negative tracking is the signature of the display voice.
- Never substitute a different typeface for Roobert; if the custom font fails to load, fall back to Plus Jakarta Sans or DM Sans - not Inter or system-ui.
- Never use #0299e0 (Sky Link) as a button fill or a section color - it is reserved for inline hyperlinks and "Learn more" text in white-background contexts only.
- Never apply the teal tinted button (rgba(87,210,238,0.1)) with a border-radius - it is a 0px radius tab control, not a pill or rounded button.
- Never center-align body copy paragraphs beyond 600px width - long centered text breaks readability; left-align body text in two-column feature sections.

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
