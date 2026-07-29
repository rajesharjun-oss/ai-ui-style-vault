# AI Implementation Prompt

Build a cord.com-inspired recruiting marketplace UI. Use it as a style reference, not as a clone of the source site.

## Required Feel

The interface must feel airy, trustworthy, and human: white canvas, deep navy text, one signal-blue action color, Figtree typography, rounded search controls, photo-heavy company cards, and soft blue-tinted shadows.

## Core Rules

- Use `#0b3658` for primary text and headings.
- Do not use pure black for text.
- Use `#4e9ad9` only for logo, primary filled buttons, and active states.
- Use `#486984` for secondary text and muted icons.
- Use `#dde7ee` for borders and hairlines.
- Use `#e6f1fa` for hover washes, toggle fill, and badge backgrounds.
- Use `#42b3b1` only for presence or response status.
- Use Figtree as the single type family.
- Use 700-800 weights for hero and display headings.
- Use 20px radius for cards and images.
- Use 24px radius for buttons and inputs.
- Use blue-tinted shadows based on `#0b3658`.

## Suggested Page Structure

1. Minimal sticky nav with blue wordmark, text links, CTA, and mode toggle.
2. Centered hero with two-option toggle pill.
3. Large 100px headline, subtitle, and pill search field.
4. Horizontal filter chip row.
5. 3-column company card grid.
6. Full-bleed dark navy CTA banner.
7. Footer with link columns.

## Component Recipes

Primary CTA:

- Background: `#4e9ad9`.
- Text: `#ffffff`.
- Font: Figtree, 16px, weight 600.
- Padding: 12px 20px.
- Radius: 24px.
- No border.
- Optional hover shadow: `0px 4px 12px rgba(11, 54, 88, 0.04)`.

Hero search input:

- Background: `#ffffff`.
- Border: `1px solid #dde7ee`.
- Radius: 24px.
- Padding: 16px 20px.
- Text: Figtree 16px, weight 400, `#0b3658`.
- Icon: `#486984`.
- Keyboard hint chip: `#e6f1fa`, 5px radius.
- Focus shadow: `0px 4px 32px rgba(11, 54, 88, 0.08)`.

Company card:

- Background: `#ffffff`.
- Radius: 20px.
- Shadow: `0px 12px 48px rgba(11, 54, 88, 0.08)`.
- Padding: 20px.
- Top image: full width, 20px radius.
- Logo: 40px square.
- Name: Figtree 16px, weight 700, `#0b3658`.
- Meta: Figtree 14px, weight 400, `#486984`.
- Status badge: `#e6f1fa` fill, `#4e9ad9` text, 5px radius.
- Response text: `#42b3b1`, weight 600.

Dark CTA banner:

- Full-bleed background: `#0b3658`.
- Headline: 48-56px, Figtree 800, white.
- Subtext: 18px, `#dde7ee`.
- CTA button: `#4e9ad9` fill, white text, 24px radius.
- Avatar stack: circular 24-32px avatars with overlap.

Filter chip:

- Background: white.
- Border: `1px solid #dde7ee`.
- Radius: 8px.
- Padding: 8px 16px.
- Font: Figtree 14px, weight 600, `#0b3658`.
- Optional icon prefix: `#486984`.

## Do Not

- Do not add a second accent color.
- Do not use pure black for text.
- Do not use sharp cards or buttons.
- Do not add gray shadows.
- Do not use light display weights.
- Do not use Signal Blue for body text or large headings.
- Do not repeat the dark CTA banner as a regular section style.

