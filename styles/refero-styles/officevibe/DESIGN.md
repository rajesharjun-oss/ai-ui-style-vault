# Officevibe Style Reference

## Summary

Officevibe feels like a thoughtful HR essay rendered as a product page. It uses warm cream paper, literary serif italics, modern compressed sans headings, deep navy editorial panels, and a vivid cobalt action color. The result is humane and calm, but still clearly SaaS.

The signature move is an italic serif phrase inside a modern headline. That italic phrase should feel personal, like an editor underlined the emotional part of the sentence.

## Theme

Light.

## Personality

- Editorial
- Humane
- Calm
- Warm
- People-ops focused
- Magazine-like
- Softly rounded
- Conversational

## Color System

The palette pivots around two blues and warm neutrals. Electric Cobalt is rare and functional. Ink Navy is the serious editorial color.

| Name | Value | Token | Use |
| --- | --- | --- | --- |
| Ink Navy | `#0c1754` | `--color-ink-navy` | Display headings, dark feature cards, footer background, body text on light canvas |
| Electric Cobalt | `#2545ff` | `--color-electric-cobalt` | Filled action buttons, active links, strongest icon, accent border |
| Lavender Mist | `#eaebf8` | `--color-lavender-mist` | Tinted badge backgrounds and soft cobalt highlight washes |
| Charcoal | `#171417` | `--color-charcoal` | Primary body and heading text, nav text, icon strokes |
| Graphite | `#222222` | `--color-graphite` | Secondary text, ghost button text, inactive nav labels |
| Stone | `#969696` | `--color-stone` | Muted helper text, placeholder content, metadata |
| Smoke | `#cccccc` | `--color-smoke` | Input borders, disabled states, neutral dividers on white |
| Cream Border | `#f0e9e1` | `--color-cream-border` | Hairline dividers, card borders, warm section separators |
| Warm Canvas | `#f9f8f6` | `--color-warm-canvas` | Page background, soft card fills, input backgrounds |
| Paper White | `#ffffff` | `--color-paper-white` | Elevated cards, button text, nav background, fields |

## Typography

Officevibe is a three-font system. The serif makes the product feel editorial. The compressed sans makes it feel modern. Inter keeps controls and body text neutral.

| Role | Font | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- | --- |
| Display Large | Martinaplantijn | 64px | 400 | 1 | normal |
| Display | Martinaplantijn | 48px | 400 | 1.1 | normal |
| Heading Large | Abcfavoritvariable | 40px | 400 | 1.2 | -0.8px |
| Heading | Abcfavoritvariable | 32px | 400 | 1.4 | -0.64px |
| Heading Small | Abcfavoritvariable | 24px | 400 | 1.4 | -0.48px |
| Subheading | Inter | 20px | 400 | 1.4 | normal |
| Body | Inter | 16px | 400 | 1.6 | normal |
| Body Small | Inter | 14px | 400 | 1.6 | normal |
| Caption | Inter | 12px | 400 | 1.4 | normal |

## Font Rules

- Use Martinaplantijn for 48px to 64px hero and section headlines.
- Italicize one meaningful phrase inside the serif headline.
- Use Abcfavoritvariable for section subheads, steps, and large modern labels.
- Use negative tracking on Abcfavorit at 24px and above.
- Use Inter for body, nav, buttons, inputs, captions, and footer text.
- Use OpenType features `ss01` and `ss04` where available.

## Spacing And Shape

- Base unit: 8px
- Density: comfortable
- Max width: 1200px
- Section gap: 80px
- Card padding: 32px
- Element gap: 24px
- Cards: 16px radius
- Badges: 16px radius
- Inputs: 16px radius
- Images: 24px radius
- Buttons: 100px radius

## Shadows

Most structure uses borders, but product screenshots and the chat widget can lift softly:

```css
--shadow-dashboard: rgba(12, 23, 84, 0.08) 0 4px 24px 0;
--shadow-chat: rgba(12, 23, 84, 0.12) 0 12px 32px 0;
```

Do not use heavy black shadows.

## Surfaces

| Level | Surface | Value | Role |
| --- | --- | --- | --- |
| 0 | Warm Canvas | `#f9f8f6` | Page background and soft section field |
| 1 | Paper White | `#ffffff` | Cards, nav, fields, chat widget |
| 2 | Ink Navy | `#0c1754` | Dark feature cards and footer |
| 3 | Lavender Mist | `#eaebf8` | Badges and soft accent chips |

## Components

### Filled Pill Button

Electric Cobalt fill, Paper White text, Inter 16px weight 500, 100px radius, 12px vertical and 24px horizontal padding. Use for Request a demo and the hero CTA. No shadow; color does the work.

### Ghost Nav Button

Transparent background, Graphite text, Inter 14px weight 500, no border, 16px to 24px horizontal padding. Keep it quiet inside the nav.

### Eyebrow Label

All-caps Inter 12px weight 700 or Abcfavorit 12px weight 500, Charcoal text, 0.12em letter spacing, 16px to 24px above the section heading.

### Display Headline With Italic Accent

Martinaplantijn 48px to 64px, weight 400, line-height 1.0 to 1.1, Charcoal on cream or Paper White on Ink Navy. One phrase is italicized to create the editorial signature.

### Step Card Dark

Ink Navy background, 16px radius, 24px to 32px padding. Use numbered badge in Electric Cobalt, Abcfavorit heading in Paper White, and supporting text in Lavender Mist or translucent white.

### Step Card Light

Paper White background, 16px radius, 1px Cream Border, 24px to 32px padding. This is the neutral card in a step row.

### Step Card Bordered Accent

Paper White background, 1.5px Electric Cobalt border, 16px radius, 24px to 32px padding. Use for the differentiated or most important capability.

### Chat Widget

Fixed bottom-center. Paper White background, 16px radius, 1px Smoke border, soft shadow, about 360px wide. Header includes a small Electric Cobalt circular avatar, Inter 14px question text, input row, and three pill suggestion chips.

### FAQ Accordion Row

Paper White background, 1px Cream Border bottom edge, 24px vertical padding, Inter 16px weight 500 question in Charcoal, chevron in Graphite. Expanded copy uses Inter 16px weight 400.

### Product Dashboard Card

Paper White background, 16px radius, soft navy-tinted shadow. Contains product screenshots, chart areas, score gauges, metric rows, and sentiment dots. Avoid making this feel like a generic analytics dashboard; keep it warm and editorial.

### Top Navigation Bar

Warm Canvas background, Workleap wordmark at left, Inter 14px weight 500 nav links in Graphite, Login as a ghost link, and Request a demo as the filled pill on the right. Height around 64px to 72px.

### Metric Pill Badge

Lavender Mist background, Ink Navy text, Inter 12px weight 500, 16px radius, 4px by 10px padding.

## Layout

Use a centered 1200px max-width layout on a full Warm Canvas page. Sections breathe with 80px gaps. The hero can use a large editorial headline and product dashboard visual. Step sections work well as three cards: dark card, light card, bordered accent card.

Dark Ink Navy sections should feel editorial and deliberate, not like dark mode. Footer may use Ink Navy as a full-width band.

## Imagery

Use product screenshots, dashboards, survey widgets, coaching cards, chat UI, score gauges, and illustrated people-ops moments. Screenshots sit in Paper White cards with warm borders or subtle navy-tinted shadows.

Avoid stock photography, cold gray dashboards, neon gradients, and generic abstract shapes.

## Do

- Use Martinaplantijn for the largest 48px to 64px headlines.
- Italicize one phrase inside major headlines.
- Use Electric Cobalt only for filled actions, active links, and one key icon per view.
- Pair Ink Navy with Paper White for dark feature cards and footer.
- Use 100px radius for approachable interactive pills.
- Use 16px radius for cards, images, and the chat widget.
- Keep the canvas Warm Canvas and borders Cream Border.
- Use Abcfavorit tight tracking at 40px and above.
- Include the bottom chat widget in product pages.

## Do Not

- Do not set display headlines in Inter or Abcfavorit.
- Do not use Electric Cobalt for body text, ordinary borders, or large backgrounds.
- Do not introduce cool gray borders.
- Do not use sharp button corners.
- Do not use cards without either Paper White surface, warm border, or Ink Navy fill.
- Do not use heavy black shadows.
- Do not center long body copy.
