# AI Implementation Prompt

Build a 247Studio-inspired branding-agency UI. Use it as a style reference, not as a clone of the source site.

## Required Feel

The interface must feel like a monochrome editorial portfolio for a serious branding studio: white canvas, black ink typography, gray supporting copy, large left-aligned display type, rounded flat cards, and no decorative color. Make typography, spacing, and alignment carry the whole experience.

## Core Rules

- Use only black, white, and neutral grays.
- Do not add a colored primary CTA.
- Use a custom display-like grotesk for the hero and labels. Prefer `247 grotesk`; fall back to Inter, Neue Haas Grotesk, Sohne, or system sans.
- Use a quiet sans body face. Prefer `Ntbau`; fall back to Inter, Untitled Sans, Sohne, or system sans.
- Enable `font-feature-settings: "ss01";` on display/logo text when supported.
- Use 73px desktop display text with line-height 1.
- Make the second hero line muted gray and italic.
- Keep body copy narrow, around 350px.
- Use large whitespace and sparse content.
- Use 1px gray borders and tonal surfaces instead of shadows.
- Use 33.76px card/image radius and 42.96px button radius.

## Suggested Page Structure

1. Minimal header with a black wordmark and sparse nav labels.
2. Hero with a two-line flush-left display statement.
3. Narrow body paragraph below the hero.
4. Client logo grid with small numbered cells and grayscale logos.
5. Case-study or service cards with rounded white surfaces and hairline borders.
6. Office/contact card with image placeholder, label, address, and underlined email.
7. Optional dark footer section using `#1f1f1f` and white text.

## Component Recipes

Hero:

- Container max width 1440px.
- Left rail starts around 120px on desktop.
- Display line 1: black, `247 grotesk`, 73px, line-height 1, weight 400.
- Display line 2: `#999999`, italic, same size and line-height.
- Body copy: `Ntbau`, 14px, line-height about 1.89, max width 350px.

Client logo cell:

- Height 80px.
- White background.
- Bottom border `1px solid #e6e6e6`.
- Tiny number at top-left in 10px `#999999`.
- Center grayscale logo at 60% opacity.

Office card:

- Width around 280px.
- Border `1px solid #cccccc`.
- Radius 33.76px.
- Padding 24px.
- Image placeholder with ash fill.
- 11px uppercase label in display face.
- 11px address lines in body face.

Buttons:

- Black text on white or white text on black.
- Border black or pale gray.
- Radius 42.96px.
- No color fill beyond black/white/gray.

## Do Not

- Do not use gradients, glows, blobs, glass effects, or colored accent systems.
- Do not add heavy shadows.
- Do not center all content just to fill space.
- Do not make body text wide.
- Do not use multiple accent colors.
- Do not turn the style into a corporate SaaS landing page.

