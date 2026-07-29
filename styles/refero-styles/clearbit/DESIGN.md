# Clearbit Style Reference

## Summary

Clearbit is a room-bright B2B data interface style. It feels like a data blueprint printed on white linen: clean white canvas, pale lavender product zones, deep navy ink, and a single blue current for active moments.

The product interface is the main visual signal. Use UI cards, enrichment tables, company records, score chips, customer logos, and data rows as hero material. Avoid stock photography, decorative 3D scenes, and abstract backgrounds.

## Theme

Light.

## Personality

- Restrained
- Product-led
- Analytical
- Quietly technical
- High-trust
- Thin-bordered
- Almost monochrome

## Color System

The chromatic budget is extremely small. Midnight Ink should dominate all reading surfaces. Electric Blue and Cobalt Surface are used only for focus, checks, links, and one clear action. Lavender Wash creates content zones without feeling decorative.

| Name | Value | Token | Use |
| --- | --- | --- | --- |
| Midnight Ink | `#091135` | `--color-midnight-ink` | Primary text, headings, nav, links, and main UI labels |
| Electric Blue | `#0f77ff` | `--color-electric-blue` | Focus rings, checkmarks, outlines, and small active edges |
| Cobalt Surface | `#127ee3` | `--color-cobalt-surface` | Filled primary action and rare blue surface emphasis |
| Slate | `#36394a` | `--color-slate` | Secondary text, labels, metadata, helper copy |
| Mist | `#b1bbcd` | `--color-mist` | Soft neutral, focus glow support, deeper separators |
| Frost Border | `#e1e9f0` | `--color-frost-border` | Hairline borders, inputs, card edges, table structure |
| Lavender Wash | `#f5f3ff` | `--color-lavender-wash` | Full-bleed section tint and soft product backdrop |
| Paper | `#ffffff` | `--color-paper` | Page canvas and card surfaces |
| Graphite | `#000000` | `--color-graphite` | Sparse icon fills only, not body text |

## Typography

Use InterVar everywhere. The signature is positive letter spacing that gets wider as the type gets larger. Do not tighten display type.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Display | 64px | 600 | 1.25 | 1.152px |
| Heading | 56px | 600 | 1.25 | 1.008px |
| Heading Small | 32px | 600 | 1.25 | 0.512px |
| Subheading | 18px | 400 | 1.5 | 0.252px |
| Body | 16px | 400 | 1.5 | 0.128px |
| Caption | 14px | 400 | 1.43 | 0.056px |

## Spacing And Shape

- Base unit: 4px
- Max width: 1200px
- Section gap: 64px
- Card padding: 24px
- Element gap: 8px to 20px
- Buttons and inputs: 8px radius
- Cards: 12px radius
- Tags: 9999px radius

Keep the radius scale strict. Buttons and inputs are softly squared, cards are slightly softer, and tags are fully pill-shaped.

## Surfaces

| Level | Surface | Value | Role |
| --- | --- | --- | --- |
| 0 | Paper | `#ffffff` | Default page canvas |
| 1 | Lavender Wash | `#f5f3ff` | Product showcase sections |
| 2 | Card | `#ffffff` | Cards floating over lavender zones |
| 3 | Cobalt Surface | `#127ee3` | Primary action fill |

## Elevation

Do not add resting drop shadows to cards. Use this only for focused or active elements:

```css
box-shadow: rgb(15, 119, 255) 0 0 0 1px,
  rgba(12, 43, 100, 0.32) 0 1px 2px 0,
  rgba(12, 43, 100, 0.32) 0 6px 16px 0;
```

## Components

### Top Navigation Bar

White full-width header with logo at left and one Cobalt Surface action at right. Keep padding low, around 8px vertical. Avoid a visible heavy bottom border.

### Filled Primary Button

Cobalt Surface fill, white text, 8px radius, InterVar 500 at 16px, 12px vertical padding, 20px horizontal padding. On focus, use the Electric Blue ring and blue glow.

### Outlined Ghost Button

Transparent background, 1px Frost Border, Midnight Ink text, 8px radius, same size as the filled button. It should stay quiet beside the blue action.

### Hero Headline Block

Centered display or heading text in Midnight Ink with positive tracking. Pair with an 18px Slate subhead. Keep the hero white and do not put the text in a card.

### Product Showcase Card

White card over Lavender Wash, 12px radius, 1px Frost Border, 24px padding, no resting shadow. The content should be the product: attribute tables, records, score badges, logos, or enrichment rows.

### Data Record Row

Use Slate labels and Midnight Ink values in a two-column layout. Add Electric Blue checkmarks sparingly in the leading column. Keep rows separated by whitespace rather than heavy dividers.

### Section Eyebrow

Small 14px InterVar text, weight 500, Midnight Ink. Often plain text, not always a pill.

### Lavender Pill Badge

Lavender Wash fill, Midnight Ink text, 9999px radius, 8px vertical and 16px horizontal padding.

### Score Badge

Small white circle, around 40px diameter, 1px Frost Border, Electric Blue number at 18px weight 600. Use as a small anchor on a product card.

### Brand Data Card

White surface with a real brand mark, a short attribute grid, and product-specific data. Brand colors are allowed only inside these product mockups.

## Layout

Use a centered 1200px container inside full-bleed white and Lavender Wash bands. The hero starts as a centered text stack, then the page shifts into alternating product sections. Common rhythm:

- Minimal nav.
- Centered headline and subhead.
- Logo or customer row.
- Lavender product section.
- Two-column feature sections with text on one side and product cards on the other.

## Imagery

Imagery should be product screenshots and realistic UI mockups. Show data tables, enrichment records, account cards, scoring chips, Slack-style records, and company profile widgets. Do not use lifestyle photos or decorative renderings.

## Do

- Use Midnight Ink for nearly all text and headings.
- Use Electric Blue only for the most important active signals.
- Separate sections with Lavender Wash and Frost Border, not shadows.
- Use InterVar with positive tracking on larger headings.
- Keep cards at 12px radius and buttons or inputs at 8px.
- Put real product UI in hero and feature visuals.
- Keep major vertical rhythm around 64px.

## Do Not

- Do not add resting drop shadows to cards.
- Do not introduce a second accent color.
- Do not use negative tracking on display text.
- Do not set body text below 14px.
- Do not use pure black for long-form body text.
- Do not break the radius scale.
- Do not use heavy gradients or decorative backgrounds.
