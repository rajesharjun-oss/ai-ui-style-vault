# (dot)connect - Style Reference

(dot)connect is a warm paper, near-monochrome engineering system with one ember-orange pulse. The layout is text-first, sparse, and architectural: huge tightly tracked headlines, quiet borders, generous whitespace, and rounded-but-not-cute controls. It should feel designed by a Swiss technical studio, not by a generic SaaS template.

## Theme

- Theme mode: light.
- Visual temperature: warm off-white with charcoal and one orange spark.
- Surface logic: bone canvas, ash cards, hairline borders, charcoal actions.
- Energy: precise, calm, networked, premium, technically literate.

## Core Principles

1. Let typography and whitespace carry the brand.
2. Use Ember orange only once per viewport.
3. Use Signal Blue only as an outline color, never as a filled surface.
4. Prefer charcoal filled arrow-pill CTAs for inline movement.
5. Use borders and tonal shifts instead of shadows.
6. Keep all major surfaces warm and flat.
7. Use abstract 3D renders as occasional interludes, never as text backgrounds.

## Color System

| Name | Value | Role |
| --- | --- | --- |
| Bone Canvas | `#fcfbf8` | Page background, card surface, light text on dark controls |
| Charcoal Ink | `#001011` | Primary text, headings, borders, dark CTA fill |
| Smoke Veil | `#0f1e1f` | Secondary text, quieter borders, dark surface moments |
| Ash Layer | `#ededea` | Elevated flat surface, hover fill, subtle card background |
| Mist Border | `#c1c4c2` | Hairline borders, dividers, section separators |
| Ember | `#fd5321` | Rare brand punctuation, header CTA, high-intent conversion accent |
| Signal Blue | `#007aff` | Ghost-outline secondary action stroke and text only |

## Typography

Primary type is AeonikPro. Fallbacks: Inter, Satoshi, General Sans, Arial, sans-serif. Enable `dlig`, `ss02`, and `ss08` OpenType features where supported.

DotConnect is a branded display variant used sparingly for brand moments and special headings. If it is unavailable, use AeonikPro with the same tracking rules.

Recommended scale:

| Token | Size | Weight | Line Height | Letter Spacing |
| --- | ---: | ---: | ---: | ---: |
| Caption | 16px | 400 | 1.5 | 0.16px |
| Body | 18px | 400 | 1.4 | 0.18px |
| Body Dense | 19px | 500 | 1.67 | 0.19px |
| Subheading | 24px | 500 | 1.4 | -0.29px |
| Heading Small | 32px | 500 | 1.1 | -0.38px |
| Heading | 36px | 500 | 1.1 | -0.72px |
| Heading Large | 72px | 500 | 0.9 | -1.8px |
| Display | 101px | 500 | 0.8 | -2.53px |

Rules:

- Use weights 400 and 500 only.
- Use `-0.025em` tracking at 72px and above.
- Use about `-0.012em` tracking around 32px to 36px.
- Use about `+0.010em` tracking at 16px to 19px.
- Do not set body below 16px or above 21px.
- Body text is left aligned. Display headlines may be centered.

## Spacing And Shape

- Density: comfortable.
- Base unit: 8px.
- Max content width: 1200px.
- Section gap: 96px.
- Card padding: 24px to 32px.
- Element gap: 24px.
- Spacing values: 8, 16, 24, 32, 48, 64, 72, 80, 96, 160.

Radius:

- Badges: 8px.
- Cards and images: 20px.
- Buttons: 24px.
- Links and arrow-pill controls: 44px.
- Full pill elements: 48px.
- Do not mix tiny 8px corners into the card/button family.

## Elevation

(dot)connect is border-driven.

- No box shadows.
- No drop shadows.
- No glow effects.
- No decorative gradients.
- Use 1px `#c1c4c2` borders for structure.
- Use `#ededea` and `#fcfbf8` surface changes for depth.

## Layout

- Use full-width sections on Bone Canvas.
- Center content inside a 1200px max-width container.
- Hero is text-only: large centered headline, compact supporting copy, and one arrow-pill action.
- Page rhythm alternates text sections and sparse 3D visual interludes.
- Section headers use split labels: left label plus arrow icon, right parenthetical number.
- Offer cards use a two-column grid.
- Story/case cards use a three-column carousel or row.
- Top navigation is thin and calm: logo left, nav links center, Ember CTA right.
- Vertical spacing around sections should feel generous and deliberate.

## Imagery

Preferred imagery:

- Abstract 3D renders.
- Chrome, glass, or metallic object studies.
- Brain, network, geometric, or sculptural forms.
- One small Ember accent inside an otherwise monochrome render.
- Case study thumbnails with the same abstract-object language.

Avoid:

- Photography.
- People.
- Lifestyle scenes.
- Images behind text.
- Decorative icon packs.
- Dense illustration systems.

## Motion

Motion should be minimal and architectural.

- Use simple color, border, and opacity transitions.
- Avoid hover lift and animated depth.
- Avoid glow and blur transitions.
- Arrow icon buttons can shift subtly, but should not bounce.

