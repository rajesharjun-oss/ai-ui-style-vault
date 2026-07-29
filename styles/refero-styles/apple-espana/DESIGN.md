# Apple Espana Design Notes

Apple Espana is a bright retail product system. It makes devices feel close, thin, and desirable through white staging, huge product imagery, precise SF Pro type, and very small commerce actions. The UI is quiet because the product imagery does the selling.

## Visual Principles

- Use white and frost surfaces as the stage.
- Let product imagery dominate every major section.
- Use blue only for purchase actions, active links, and commerce navigation.
- Keep text hierarchy centered, spare, and confident.
- Use pill buttons for buying and rounded frost tiles for product groupings.
- Use almost no shadows; use product lighting and negative space instead.

## Color System

The palette is Apple Blue, deep ink, graphites, frost neutrals, white, and restrained state colors. Blue should not become a decorative fill. It is for buy buttons, links, and selected commerce states.

## Typography

Use SF Pro Display for large headings and SF Pro Text for body, nav, links, captions, and product UI. If native SF fonts are unavailable, use system fonts with `-apple-system`, BlinkMacSystemFont, and Inter fallback.

## Layout

Use a content max width around `980px` for text-heavy content and `1440px` for hero imagery. Sections breathe with 96px to 160px vertical spacing. Major pages often use centered hero stacks: eyebrow, headline, subhead, CTA row, and large product image.

## Elevation

Avoid normal SaaS shadows. Frosted nav can use backdrop blur. Product images can carry their own rendered lighting; cards and tiles should remain flat with hairline borders or subtle frost backgrounds.
