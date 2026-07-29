# Athletics - Style Reference

## North Star

Build the interface like a well-typeset creative monograph on black velvet: enormous thin serif headlines, small quiet labels, generous dark space, and almost no component chrome. The page should feel confident because it does less.

## Theme

Dark only. Obsidian is the base canvas. Charcoal is the elevated section surface. Paper White is all readable text. Ash is for hairline dividers and structural borders. Interface color is strictly monochrome.

## Color Tokens

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Obsidian | `#000000` | `--color-obsidian` | Base page canvas, deepest section backgrounds, footer, hero |
| Charcoal | `#1d1d1d` | `--color-charcoal` | Elevated section surfaces, card backgrounds, input fields |
| Ash | `#d6d5d0` | `--color-ash` | Hairline borders, dividers, input outlines, card edges |
| Paper White | `#ffffff` | `--color-paper-white` | Display text, body text, icon strokes, form controls on dark surfaces |

## Typography

Use Feature Deck for display and section headlines only. Use Sohne for all body, navigation, links, forms, buttons, labels, and footer.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Body Small | 16px | 400 | 1.5 | 0 |
| Functional | 17px | 300 | 1.3 | 0 |
| Subheading | 22px | 300 | 1.3 | 0 |
| Heading | 72px | 300 | 1.1 | -0.009em |
| Heading Large | 82px | 300 | 1.05 | -0.009em |
| Display | 116px | 300 | 1.05 | -0.018em |

Font roles:

- Feature Deck: display type only, 72px to 116px, weight 300, tight negative tracking. Fallbacks: GT Sectra Display Light, Canela, Domaine Display Thin.
- Sohne: all functional and body type, 16px to 22px, weights 300 and 400. Fallbacks: Inter, Neue Haas Grotesk, Untitled Sans.

Rules:

- Never use Feature Deck for body, navigation, or functional UI.
- Never set Feature Deck at 400 weight or above.
- Pair small uppercase Sohne labels above large Feature Deck headlines.
- Use scale contrast as the main hierarchy signal.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | Comfortable |
| Base unit | 8px |
| Max width | 1440px |
| Section gap | 128px to 144px |
| Card padding | 24px |
| Element gap | 24px to 32px |

Spacing scale: 16, 24, 32, 48, 64, 128, 144.

Radius scale:

- Cards and image containers: 8px.
- Tags, buttons, and chips: 9999px.

Elevation:

- No shadows.
- No glows.
- No gradients behind text.
- Use flat color shifts from Obsidian to Charcoal and occasional 1px Ash hairlines.

## Components

### Top Navigation Bar

Use transparent or black background with no visible border or shadow. Place the wordmark on the left in 16px Sohne 400 Paper White. Place right-aligned links such as Work, About, Approach, Careers, and Contact in 16px Sohne 400 Paper White with about 16px gaps. No underlines, no fills, no hover color.

### Hero Mark And Display Headline

Use a centered stack on Obsidian. Place a large editorial mark above a 116px Feature Deck 300 Paper White headline with -0.018em tracking. The mark may be filled with editorial photography and is the only place saturated color can appear.

### Two-Column Section Opener

Use Charcoal background. Left column: small uppercase Sohne 400 Paper White label above a 72px Feature Deck 300 headline. Right column: 17px Sohne 400 Paper White body copy, max width around 480px, line-height 1.5. Use 128px to 144px vertical padding.

### Specialty Tag

Use a Paper White pill with Obsidian text, 9999px radius, about 8px vertical and 16px horizontal padding, and 16px Sohne 400. No border and no shadow.

### Service Index List

Use stacked service names in 82px Feature Deck 300 Paper White, line-height 1.05. Add one uppercase letter such as A, B, C, or D in 16px Sohne 400 Paper White flush-left and aligned to each entry. No dividers and no bullets.

### Hairline Divider

Use 1px solid Ash. Use sparingly between major zones. Do not use Ash for readable text.

### Pill Button

Use Paper White background, Obsidian text, 9999px radius, 12px vertical padding, 24px horizontal padding, 16px Sohne 400, no border, no shadow, and no color hover.

### Form Input

Use transparent or Charcoal background, bottom border only, 1px Ash, Paper White text and placeholder, 16px Sohne 400. Do not use a full input box or glow focus state.

## Layout And Imagery

- Use a full-bleed dark layout with no visible page container.
- Hero is a centered stack: mark above oversized headline.
- Alternate two editorial patterns: two-column section openers and full-width single-column displays.
- Give major sections the full viewport or more.
- Keep content density very low.
- Use A/B/C/D letter annotations for service or capability indexes.
- Imagery is photography-led but restrained: dark, moody, editorial, tightly cropped.
- Saturated color belongs only inside the brand mark or editorial photography.
- Avoid decorative illustration, abstract graphics, and icons beyond minimal text markers.

## Do

- Use Obsidian as the base canvas and Charcoal for elevated section bands.
- Keep the theme dark at all times.
- Set display headlines at 72px to 116px in Feature Deck 300.
- Use -0.009em to -0.018em tracking on display serif.
- Use 9999px radius only for tags and buttons.
- Use 8px radius only for cards and image containers.
- Apply 128px to 144px vertical padding for major sections.
- Annotate index lists with uppercase single letters.
- Restrict all chromatic color to imagery and the brand mark.

## Do Not

- Do not introduce chromatic UI colors.
- Do not use Feature Deck for body, navigation, or functional text.
- Do not apply shadows or drop shadows.
- Do not use display serif at 400 weight or above.
- Do not use gradients, glows, or colored backgrounds behind text blocks.
- Do not use Ash for readable text.
- Do not add background fills to navigation or header areas.
