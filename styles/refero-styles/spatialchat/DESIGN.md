# SpatialChat Style Reference

## Summary

SpatialChat is a clean light SaaS marketing style built on off-white surfaces, white cards, Satoshi typography, and a single sharp violet accent. It feels modern, confident, and approachable. It should not feel dark, noisy, or playful.

The page structure is familiar but polished: announcement bar, sticky-friendly nav, centered hero stack, CTA pair, trust row, logo strip, centered section headings, and alternating feature sections with product screenshot cards.

## Theme

Light.

## Personality

- Airy
- Confident
- Friendly
- Modern SaaS
- Violet-accented
- Product-led
- Spacious
- Grayscale-first

## Color System

Violet is the only chromatic accent. Everything else is grayscale. Use Cloud as the canvas and Paper as the top surface so white cards stay visible without needing heavy borders.

| Name | Value | Token | Use |
| --- | --- | --- | --- |
| Brand Violet | `#5727e7` | `--color-brand-violet` | Filled primary CTAs, announcement bar, New badge text, active states, bullets |
| Tinted Highlight | `#f2f2ff` | `--color-tinted-highlight` | Soft violet highlight badges and subtle section accents |
| Ink Black | `#030712` | `--color-ink-black` | Headlines, primary text, ghost button borders |
| Graphite | `#222222` | `--color-graphite` | Button labels on light or dark UI chrome |
| Slate | `#4b5563` | `--color-slate` | Body text, paragraphs, subheads |
| Mid Gray | `#5c5c5c` | `--color-mid-gray` | Icon strokes, list markers, muted metadata |
| Steel | `#6b7280` | `--color-steel` | Placeholders, helper text, disabled states |
| Mist | `#d1d5db` | `--color-mist` | Input borders and stronger divider lines |
| Fog | `#e5e7eb` | `--color-fog` | Hairline borders, card outlines, table dividers |
| Cloud | `#f9fafb` | `--color-cloud` | Page canvas and section background |
| Paper | `#ffffff` | `--color-paper` | Cards, nav bar, inputs, text on violet |

## Typography

Use Satoshi or a close substitute like Inter or General Sans. Satoshi should cover all sizes from helper text to hero headlines. Use weight, size, and space for hierarchy.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Display | 60px | 700 | 1.3 | normal |
| Heading Large | 40px | 700 | 1.3 | normal |
| Heading | 32px | 600 | 1.38 | normal |
| Heading Small | 24px | 600 | 1.4 | normal |
| Subheading | 20px | 600 | 1.5 | normal |
| Body | 18px | 400 | 1.56 | normal |
| Body Small | 16px | 400 | 1.5 | normal |
| Caption | 14px | 400 | 1.43 | normal |

## Font Rules

- Weight 700 owns the hero and section headlines.
- Weight 600 handles subheadings and emphasized feature titles.
- Weight 500 is for buttons, badges, and nav labels.
- Weight 400 is for paragraphs and UI labels.
- Do not use Satoshi below 400 or above 700.

## Spacing And Shape

- Base unit: 4px
- Density: comfortable
- Max width: 1200px
- Section gap: 64px
- Card padding: 24px
- Element gap: 12px
- Feature column gap: 48px
- Buttons: 12px radius
- Inputs: 12px radius
- Cards: 16px radius
- Badges: 8px radius
- Logos: 50px radius
- Announcement bar: 0px radius

## Shadows

All shadows use 6 percent black. Do not use colored shadows or darker elevation.

```css
--shadow-subtle: rgba(0, 0, 0, 0.06) 0 1px 2px 0;
--shadow-md: rgba(0, 0, 0, 0.06) 0 4px 16px 0;
--shadow-xl: rgba(0, 0, 0, 0.06) 0 4px 28px 0;
```

## Surfaces

| Level | Surface | Value | Role |
| --- | --- | --- | --- |
| 0 | Canvas | `#f9fafb` | Page background and section bands |
| 1 | Surface | `#ffffff` | Nav, cards, inputs, elevated blocks |
| 2 | Tinted Surface | `#f2f2ff` | Violet badges and soft highlight chips |

## Components

### Announcement Bar

Full-width Brand Violet strip with centered white Satoshi 16px/500 text and about 12px vertical padding. This is the only full-bleed colored band.

### Primary CTA Button

Filled Brand Violet, white text, Satoshi 16px/500, 12px radius, 12px vertical and 20px horizontal padding, subtle 0 1px 2px shadow. Do not add an arrow inside the filled button.

### Ghost CTA Button

Transparent fill, 1px Ink Black border, Ink Black Satoshi 16px/500 text, 12px radius, same sizing as primary. Often paired with a trailing arrow icon.

### Navigation Link

Satoshi 16px/500 in Ink Black, no underline, 8px horizontal padding, small chevron for dropdowns.

### New Badge

Tinted Highlight background, Brand Violet text, Satoshi 12px/500, 8px radius, 4px vertical and 10px horizontal padding.

### Login Link

Quiet ghost-style text button. Transparent fill, Satoshi 15px/500, Ink Black, 12px radius, 12px vertical and 20px horizontal padding.

### Hero Headline

Centered Satoshi 60px/700 in Ink Black with 1.30 line height. Pair with an 18px Slate subhead and the primary plus ghost CTA pair.

### Social Proof Row

Inline trust strip under hero CTAs. Use white surface, 14px to 16px Satoshi, 16px gutters, ratings, review badges, and short trust labels.

### Logo Strip Card

Full-width Paper band with 40px vertical padding and evenly spaced client logos inside a 1200px container. Native logo colors are allowed only here.

### Section Heading

Centered Satoshi 40px/700 headline with an 18px Slate paragraph. Use this before major feature blocks.

### Feature Section

Two-column grid with 48px gap. Text side includes a small tag pill, 32px Satoshi 600 heading, violet bullet list, stat grid, and CTA. Visual side includes a 16px-radius product screenshot card with 0 4px 28px 6-percent black shadow.

### Feature List Item

8px Brand Violet disc, 12px gap, Satoshi 16px/600 title in Ink Black, and Satoshi 14px/400 description in Slate.

### Stat Block

No border and no background. Use 24px/700 Ink Black number with 14px/400 Slate label.

### Product Screenshot Card

Paper surface, 16px radius, `0 4px 28px rgba(0, 0, 0, 0.06)` shadow. The product image fills the card edge-to-edge inside the radius.

## Layout

Use full-width announcement and nav bars, then constrain main content to 1200px. The hero is centered:

1. 60px headline.
2. 18px subhead.
3. Filled violet CTA plus ghost CTA.
4. Social proof row.

Below the hero, use a full-width logo strip, then alternate centered narrow text blocks and two-column feature sections. Keep 64px vertical gaps and 48px between feature columns.

## Imagery

Product screenshots are the visual language. Show the live UI: video thumbnails, avatar bubbles, chat panels, polls, and collaboration surfaces. Logo rows can preserve native brand colors. Avoid lifestyle photography, stock images, and abstract illustration.

## Do

- Use Brand Violet only for CTAs, the announcement bar, New badges, active states, and bullets.
- Keep buttons at 12px radius and cards at 16px radius.
- Use Satoshi 700 at 40px to 60px for display and section headings.
- Pair a filled violet CTA with a ghost-bordered CTA in hero sections.
- Keep shadows at 6 percent black.
- Use Fog for structural borders and Mist for input borders.
- Set the page canvas to Cloud and cards to Paper.

## Do Not

- Do not introduce a second accent color.
- Do not use button radii below 10px or above 14px.
- Do not use shadows darker than 6 percent black.
- Do not use Satoshi below 400 or above 700.
- Do not center-align long body paragraphs.
- Do not put violet controls on Tinted Highlight backgrounds.
- Do not make dark mode sections with large Ink Black fills.
