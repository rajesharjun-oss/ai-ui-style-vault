# Fey - Style Reference

Fey feels like a nocturnal finance terminal refined into a premium consumer product: matte black surfaces, luminous white type, floating product cards, pill-shaped controls, and color that appears only when it carries market meaning or navigational focus.

**Theme:** dark

## Summary

Build this style around the product UI. The page should feel like a dark showroom for the Fey application: portfolio dashboards, ticker cards, news recaps, insider transactions, stock pages, and dock controls floating in space. Avoid decorative color. Status, accent, and navigation color should each have a job.

## Tokens - Colors

| Name | Value | Token | Role |
|---|---:|---|---|
| Fey White | `#ffffff` | `--color-fey-white` | Primary text, decorative borders, hairlines |
| Fey Ink | `#0b0b0b` | `--color-fey-ink` | Primary canvas and core dark surface |
| Fey Charcoal | `#191919` | `--color-fey-charcoal` | Product mockup cards and secondary panels |
| Fey Obsidian | `#131313` | `--color-fey-obsidian` | Nested cards, input wells, subtle elevated containers |
| Fey Graphite | `#868f97` | `--color-fey-graphite` | Muted text, subdued borders, disabled labels |
| Fey Mist | `#cccccc` | `--color-fey-mist` | Icon strokes, subtle links, tertiary borders |
| Fey Smoke | `#525252` | `--color-fey-smoke` | Deep dividers and low-emphasis strokes |
| Fey Pale | `#e6e6e6` | `--color-fey-pale` | Light ghost outlines and subtle borders |
| Fey Ash | `#999999` | `--color-fey-ash` | Low-emphasis borders and secondary text |
| Fey Ember | `#ffa16c` | `--color-fey-ember` | Warm highlighted words and warm showcase gradients |
| Fey Signal | `#479ffa` | `--color-fey-signal` | Active navigation underline and cool trust accent |
| Fey Growth | `#4ebe96` | `--color-fey-growth` | Positive market movement, buy pills, finance signals |
| Fey Abyss | `#000000` | `--color-fey-abyss` | Shadow base and deepest background |
| Fey Frost | `#b6d6ff` | `--color-fey-frost` | Cool gradient accent |
| Fey Volt | `#d6fe51` | `--color-fey-volt` | Electric highlight gradient accent |

## Typography

Use `Calibre` for every role. No second family. Body and most UI use weight 400. Nav and labels use 500-600. Display headlines use weight 700 with compressed tracking.

| Role | Size | Weight | Line Height | Tracking |
|---|---:|---:|---:|---:|
| Caption | 10px | 400-500 | 1.5 | 0 to -0.08px |
| Body | 14px | 400 | 1.5 | 0 |
| Heading small | 18px | 600 | 1.32 | 0 |
| Heading | 24px | 700 | 1.25 | -1.27px |
| Heading large | 26px | 700 | 1.2 | -1.38px |
| Display | 48px | 700 | 1.1 | -3.84px |
| Display large | 54px | 700 | 1.0 | -4.32px |

## Spacing And Shape

- Page max width: 1200px
- Section gap: 64px
- Element gap: 10-16px
- Card padding: 18-24px
- Card radius: 16px
- Icon radius: 6px
- Small radius: 10px
- Button/nav/badge radius: 99px
- Featured card radius: 275px

## Components

**Pill Navigation Button**

Fully rounded 99px radius. Transparent background. Text is 12-14px Calibre 500. Inactive text uses Fey Graphite; active state becomes Fey White with a 1px Fey Signal underline. No fill and no shadow.

**Primary Action Button**

99px radius, transparent or Fey Ink background, white text at 12-14px Calibre 500, and a subtle white halo. It is ghost-like; shape and light define it rather than a chromatic fill.

**Product Showcase Card**

16px radius, Fey Charcoal background, heavy Fey Abyss halo shadow. Contains miniature dashboard UI: charts, tickers, news feeds, portfolio values, and insider transaction cards.

**Insider Transaction Card**

16px radius with Fey Ink or Fey Charcoal surface. Left avatar, center name in white and company in Fey Graphite, right-side Buy/Sell pill. Buy uses Fey Growth with white text.

**Feature Section Card**

Outer featured card can use the extreme 275px radius. Inner content uses Fey Ink, Fey Mist body copy, and a label below in Fey Graphite 12px.

**Dock Navigation Bar**

99px pill container with Fey Charcoal background, 1px Fey Mist border, 7-8 monoline icons, and a separated search button. It floats over a product image with dotted leader lines to annotation text.

**Status Badge**

Small 99px pill. Fey Growth for Buy or positive movement; a muted warm/red tone for Sell or negative movement. Text is 10-11px Calibre 500 uppercase.

**Ticker Display**

Large 48px Calibre 700 white numeric value with tight tracking. Use Fey Growth for positive change and muted red for negative change. Use tabular numerals where possible.

**Section Headline**

48-54px Calibre 700, white, tracking around -0.08em, line height 1.0-1.1. One word may use Fey Ember or Fey Signal. Keep the sentence short and confident.

**Highlighted Word**

A single colored word inside a white headline. Use one accent word maximum per headline.

**News Recap Card**

Fey Charcoal surface, 10px radius, ticker badge, 14px white headline, 12px Fey Mist summary, and 10px Fey Graphite timestamp.

**Carousel Navigation Arrow**

Circular ghost control about 40px diameter. Fey Ink background, 1px Fey Mist border, centered white chevron.

## Layout And Imagery

- Center main content inside an approximately 1200px max-width rail.
- Hero is a full-width product showcase with floating dashboard mockup and a two-line headline below.
- Use a minimal top nav with logo, five nav links, a contextual pill, and a Learn more action.
- Sections alternate dark rooms with generous 64px gaps.
- Highlights use a headline/description block, carousel arrows, and horizontal 3-card product rows.
- Feature showcases are usually 3-up grids.
- Product mockups are the main imagery; avoid stock photography.
- A secondary motif can be a rough 3D stone/sculpture behind the dock section, dramatically lit on black.
- Use monoline 1.5-2px icons in Fey White or Fey Mist.

## Implementation Rules

Use color as meaning, not decoration. Fey Ember highlights language, Fey Signal marks navigation, and Fey Growth signals financial movement. Keep surfaces in the `#0b0b0b` to `#191919` range, then use shadows and card radius to create depth.
