# Quizlet - Style Reference

Quizlet feels like a quiet study desk: cool gray page canvas, crisp white cards, one saturated indigo highlighter, and a small set of pastel learning cards that carry the friendly color.

**Theme:** light

## Summary

Build this style around compact, highly legible product UI. The base is near-monochrome: Ink Charcoal text, Slate Veil secondary copy, Paper White surfaces, and Mist Border hairlines. Iris Bolt is the only saturated interactive color, used for links, filled pills, active states, and brand marks. Pastels are allowed, but only as controlled feature-card backgrounds.

## Tokens - Colors

| Name | Value | Token | Role |
|---|---:|---|---|
| Iris Bolt | `#4255ff` | `--color-iris-bolt` | Links, filled buttons, active states, low-frequency brand emphasis |
| Ink Charcoal | `#282e3e` | `--color-ink-charcoal` | Primary text, headings, body copy, icons |
| Deep Indigo | `#2e3856` | `--color-deep-indigo` | Secondary body text and support copy |
| Slate Veil | `#586380` | `--color-slate-veil` | Muted metadata, helper text, tertiary nav items |
| Fog Mist | `#939bb4` | `--color-fog-mist` | Placeholders, disabled states, low-emphasis strokes |
| Pure Black | `#000000` | `--color-pure-black` | App store badges and occasional icon detail only |
| Chalk Canvas | `#f6f7fb` | `--color-chalk-canvas` | Page-level canvas behind content |
| Paper White | `#ffffff` | `--color-paper-white` | Cards, inputs, modals, raised panels |
| Lilac Wash | `#edefff` | `--color-lilac-wash` | Tinted sections and promotional panels |
| Mist Border | `#d9dde8` | `--color-mist-border` | Card borders, separators, input edges |
| Feature Pastel | `#dbdfff` | `--color-feature-pastel` | Feature-card tint and category surfaces |

## Typography

Use `hurme_no2-webfont` or `Hurme Geometric Sans` as the whole system. If unavailable, use Inter. The type should feel open, geometric, and textbook-friendly.

| Role | Size | Weight | Line Height | Notes |
|---|---:|---:|---:|---|
| Caption | 12px | 400 | 18px | Metadata and small labels |
| Body small | 14px | 400 | 20px | Nav, helper text, secondary copy |
| Body | 16px | 400 | 24px | Main body and links |
| Subheading | 20px | 600-700 | 28px | Feature/card labels |
| Heading small | 24px | 600-700 | 32px | Compact headings |
| Heading | 32px | 600-700 | 41px | Section headings |
| Display | 44px | 700 | 55px | Hero headline |

## Spacing And Shape

- Page max width: 1200px
- Section gap: 80px
- Card padding: 24px for larger sections, 16px for study-set cards
- Element gap: 8px
- Primary button radius: 200px
- Search bar radius: 200px
- Content card radius: 8px
- Feature category card radius: 24px
- Utility/store badge radius: 4px
- Carousel arrow size: 40px

## Components

**Filled Pill Button**

Iris Bolt background, white text, 14-16px Hurme-style type, weight 600, 10px 20px or 10px 24px padding, 200px radius, no border, and a subtle 2px/4px shadow.

**Ghost Text Link**

No box styling. Use Iris Bolt text at 16px weight 400 and add underline only on hover.

**Ghost Outlined Button**

Transparent background, 1px Iris Bolt border, Iris Bolt text, 200px radius, 10px 24px padding, and 600 weight.

**Store Badge**

Pure Black background, white text, 4px radius, 8px 16px padding. Keep it visually distinct from native Quizlet pills.

**Study Set Card**

Paper White background, 1px Mist Border, 8px radius, 16px padding. Use 16px weight 600 title, 12px Slate Veil metadata, and an avatar/creator row.

**Feature Category Card**

Large 24px-radius pastel card with an 8px-radius white inset panel. Use 20-24px weight 700 labels and 14-16px body content. Use for learning modes and product feature previews.

**Top Navigation Bar**

Paper White full-width header with a 1200px inner rail, about 56px height, logo on the left, two dropdown menus, centered pill search bar, and right-aligned Create plus Log in actions. Use the 4px/16px shadow token.

**Search Bar**

Chalk Canvas fill, 200px radius, 8px 16px padding, Fog Mist placeholder, search icon at left, no visible border.

**Promotional Section Panel**

Full-width Lilac Wash section with a 1200px inner container and two-column layout: product mockup on one side, heading/body/button on the other.

**Carousel Navigation Arrow**

40px circle, Paper White background, 1px Mist Border, centered chevron in Ink Charcoal.

**Footer Link Column**

Multi-column footer on Chalk Canvas. Use 14px weight 600 headings in Ink Charcoal and 14px links in Slate Veil with 8px vertical gaps.

## Layout And Imagery

- Use a centered 1200px content rail on full-bleed Chalk Canvas.
- Hero is a centered text stack: headline, subhead, filled pill, ghost link.
- Follow hero with a horizontal feature-card carousel.
- Alternate white and Lilac Wash sections for product explanations.
- Use two-column product sections with mockup left and copy/actions right.
- Footer is a 5-column link grid.
- Imagery is product-first: flashcards, study guides, diagrams, practice tests, score screens, and flat illustrated UI cards. Avoid lifestyle photography.

## Implementation Rules

Keep color disciplined. Use Iris Bolt as the only saturated interactive color. Pastel panels should identify feature categories, not become random decoration. Let cards sit on Chalk Canvas or Paper White with simple borders and one small shadow token.
