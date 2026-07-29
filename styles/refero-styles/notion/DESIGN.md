# Notion Design Notes

Notion reads as a warm productivity notebook rather than a cold SaaS dashboard. The surface hierarchy starts with a warm paper canvas, then pure white cards, then selective accent panels. The overall effect is calm, tactile, and editorial, with enough playful punctuation to avoid feeling sterile.

## Visual Principles

- The page canvas is warm off-white, never pure white.
- White cards sit on the canvas with 1px hairline borders and 12px corners.
- The primary blue is reserved for the most important action.
- Accent colors belong in feature panels, status tags, highlights, and playful marks.
- Typography is confident and compact at display sizes through negative tracking.
- Motion is light and quick; playful bounce is reserved for decorative marks.

## Color System

Use `#0075de` as the single committed action blue. Build the rest of the UI through warm neutrals, black alpha hierarchy, and feature-card accents. Avoid adding many button colors. Let card backgrounds carry the color variety instead.

## Typography

The primary sans is NotionInter, with Inter as a practical substitute. Use 400 for body, 500 for UI/nav, and 600 to 700 for large display moments. Apply tighter letter spacing at 54px, 72px, and 96px.

Lyon Text is an editorial accent, not a UI font. Use it sparingly for intros, pull-quote-like paragraphs, or literary body copy.

## Layout

Use a centered page with max width around `1440px`. Hero structure should stack character marks, large headline with inline highlight pill, subhead, CTA row, and product UI mockup. Below the hero, alternate white card grids with colored feature panels and product mockups.

## Elevation

Most cards have no shadow. They rely on warm-canvas contrast plus a `1px rgba(0,0,0,0.08)` border. Shadows are allowed mainly for sticky nav and large product UI mockups.
