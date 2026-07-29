# Implementation Prompt

Build a polished editorial financial-broadsheet interface inspired by the New Form Refero style system.

Use a warm Bone White page canvas, oversized serif and grotesque display typography, tiny uppercase micro-labels, grayscale-green photo inserts, and one saturated Highlighter Green accent. The page should feel like a printed capital markets broadsheet, not a normal SaaS landing page.

## Required Style Decisions

- Canvas: Bone White `#fafffa`, never pure white.
- Dark surface and footer: Press Black `#121613`.
- Main text: Typesetter Ink `#000000` or Press Black.
- Muted editorial text: Newsprint Gray `#516254`.
- Inverse text: Muted Sage `#c8d2c8` or Bone White.
- Accent: Highlighter Green `#2bee4b`.
- Button shadow: green-tinted Shadow Moss, not gray.
- Primary button radius: 5px, not fully pill-shaped.
- Image radius: 14px.
- Ghost blocks: 10px radius.
- Max width: 1400px.
- Section gap: 80px.

## Typography Direction

Use PP Mondwest for hero-scale serif display type at 165px to 295px, weight 400, line-height 0.9, and -0.04em tracking. Use TWK Lausanne for micro-labels, navigation, grotesque headings, body, and buttons. Use Editorial New for lighter editorial display passages. Use Times only for old-school underlined inline links.

## Layout Direction

Create:

- A wide broadsheet-style page.
- Oversized editorial headline blocks.
- Small grayscale-green photo inserts floating inline between display text lines.
- Micro-label navigation and section metadata.
- A green action button with green shadow.
- Press Black editorial sections with Bone White type.
- A full-bleed Highlighter Green band before the footer.

## Photo Treatment

Apply the grayscale-green filter to every photographic asset:

```css
filter: grayscale(1) saturate(1) invert(0.27) sepia(0.07) saturate(10.67) hue-rotate(80deg) brightness(1.02) contrast(0.83);
```

## Avoid

- A second saturated accent color.
- Full-color photography.
- Gray card shadows.
- 9999px radius CTA buttons.
- Body copy larger than 18px.
- Standard SaaS card grids.
- Sans-serif-only display headlines.
- Pure white page backgrounds.
- Decorative gradients.
