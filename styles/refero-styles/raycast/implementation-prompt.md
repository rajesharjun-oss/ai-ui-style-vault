# Implementation Prompt

Build the UI in the Raycast Refero style.

Create a dark productivity power-tool interface on a near-black canvas. Use Inter typography, neutral light-gray CTAs, a floating glass nav, tactile keyboard-key card treatments, compact extension tiles, and a restrained coral brand accent. The style should feel Mac-native, fast, technical, and premium without becoming colorful SaaS.

Color rules:

- Page background: `#040506`.
- Card surface: `#07080a`.
- Recessed fields: `#111214`.
- Badge fill: `#1b1c1e`.
- Primary text: `#ffffff`.
- Secondary text: `#9c9c9d`.
- Muted text: `#6a6b6c`.
- Neutral action fill: `#e6e6e6`.
- Neutral action text: `#454647`.
- Coral accent: `#ff6363`, only for brand mark, hero art, AI badge, or tiny selected states.
- Hero-only blue tones: `#63a1ff`, `#143ca3`, `#02193b`.

Typography rules:

- Use Inter for the page, nav, body, cards, headings, and buttons.
- Use Geist Mono for version strings, install commands, terminal hints, and technical micro-labels.
- Use SF Pro Text or system glyph fonts only for numeric/icon callouts.
- Hero headline: 56px, Inter 400, line-height 1.17, letter-spacing 0.22px.
- Body: 16px, Inter 400.
- Feature heading: 20px, Inter 500.
- Nav/button labels: 13-14px, Inter 500.

Component rules:

- Primary actions are Mist filled buttons, not coral/blue/green buttons.
- Floating nav uses 8px radius, 1px `#363739` border, and backdrop blur around 48px.
- Cards use 16px radius, 24px padding, and the key-shadow stack:

```css
box-shadow:
  rgba(255, 255, 255, 0.05) 0 1px 0 0 inset,
  rgba(255, 255, 255, 0.25) 0 0 0 1px,
  rgba(0, 0, 0, 0.2) 0 -1px 0 0 inset;
```

- Inputs use 8px radius, subtle white-tinted fill, white text, and Ash placeholder text.
- Badges use Graphite fill, white text, 6px radius, and compact padding.
- Icon containers are full circles with dark fill and 20px padding.

Layout rules:

- Keep the whole page dark.
- Hero can be full-bleed with dramatic red/blue abstract gradient geometry.
- Below the hero, return to restrained 1200px centered dark sections.
- Use 80-120px section gaps.
- Use 3-column compact grids and 2-column feature grids.
- Snap spacing to the 8px grid.

Avoid light sections, chromatic CTA buttons, coral body links, generic multicolor accents, outer drop shadows, glass everywhere, dense dashboards, and stock photography.

