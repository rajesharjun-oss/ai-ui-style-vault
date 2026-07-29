# Relate - Style Reference

Relate is a cool-white SaaS system for CRM and pipeline workflows. It combines a bright canvas, near-black text, a vivid royal-blue brand signal, soft lavender washes, pill controls, and large rounded product UI cards. The page should feel focused, optimistic, and operational: sales pipeline software shown with enough polish to feel modern, but not decorative.

## Theme

- Theme mode: light.
- Visual temperature: cool white with blue/lavender tinting.
- Surface logic: snow canvas, lavender wash bands, white product cards, subtle dividers, and soft shadows.
- Energy: friendly CRM clarity, compact product density, rounded and smooth.

## Core Principles

1. Use `#145aff` as the main saturated brand color.
2. Keep the page bright: `#fcfcfc`, `#ffffff`, and `#f0f4fe` carry most surfaces.
3. Make interactive controls pill-shaped.
4. Use large rounded containers around product sections.
5. Let product screenshots and CRM cards act as the main visual proof.
6. Use tight Inter display typography with generous line-height for body copy.
7. Keep extra status colors small and dot-sized.

## Color System

| Name | Value | Role |
| --- | --- | --- |
| Royal Signal | `#145aff` | Main brand accent, hero highlight word, links, logo mark, active dots |
| Cobalt Glow | `#3b82f6` | Soft blue highlights, decorative blue wash, product emphasis |
| Mint Win | `#16ca2e` | Small green accent for positive micro-status or short emphasis |
| Coral Lost | `#f26052` | Small red/orange trust badge cue or negative micro-status |
| Amber Pending | `#ffa64d` | Small pending status dot or short emphasis |
| Azure Focus | `#0099ff` | Form focus glow and active input state |
| Midnight Ink | `#020520` | Hero and section headings |
| Graphite Body | `#14141e` | Body text, UI labels, secondary headings |
| Slate Caption | `#374151` | Muted body copy, nav labels, lists |
| Ash Helper | `#6b7280` | Helper text, metadata, timestamps |
| Stone Divider | `#e2e8f0` | Borders, card edges, hairline dividers |
| Lavender Wash | `#f0f4fe` | Hero and feature band tint |
| Fog Surface | `#f1f5f9` | Inputs, disabled surfaces, grouping backgrounds |
| Snow Canvas | `#fcfcfc` | Page background, nav surface, neutral card surface |
| White Card | `#ffffff` | Product cards and inner UI cards |

## Typography

Primary type is Inter. Use it for headings, body, nav, buttons, and most UI text. Fallbacks: DM Sans, Geist, Manrope, Arial, sans-serif.

Secondary type is Pretendard for localized Korean UI labels when needed. Roboto Mono can appear for code-adjacent numerical labels, but should not become the main product voice.

Recommended scale:

| Token | Size | Weight | Line Height | Letter Spacing |
| --- | ---: | ---: | ---: | ---: |
| Caption | 12px | 400 | 1.2 | 0 |
| Body Small | 14px | 400 | 1.43 | 0 |
| Body | 16px | 400 | 1.63 | 0 |
| Subheading | 20px | 400 | 1.4 | -0.16px |
| Heading Small | 22px | 500 | 1.4 | -0.2px |
| Heading | 40px | 600 | 1.05 | -1.48px |
| Heading Large | 56px | 600 | 1.05 | -1.51px |
| Display | 80px | 600 | 1.05 | -1.52px |

Rules:

- Use 400, 500, and 600 only.
- Do not use weights above 600.
- Body copy usually sits at 14px to 16px.
- Display and hero headings use tight negative tracking.
- Use one colored word in the hero headline when helpful.

## Spacing And Shape

- Density: compact.
- Max width: 1200px.
- Section gap: about 80px.
- Card padding: often 12px inside product cards.
- Element gap: 8px to 12px.
- Spacing values: 4, 6, 8, 9, 10, 11, 12, 16, 20, 24, 28, 32, 36, 40, 52, 72.

Radius:

- Inner cards: 8px.
- Inputs: 12px.
- Pipeline cards: 16px.
- Outer containers: 16px to 40px.
- Glassy containers: 28px to 48px.
- Buttons, tags, and nav items: pill radius, usually 100px or 9999px.
- Minimum visible radius: 4px.

## Elevation

Relate uses soft floating elevation.

- Deal cards use a tiny black shadow.
- Feature containers use a multi-layer soft black shadow.
- Blue glow accents can appear behind hero or CTA areas.
- Use shadow lightly and softly. Avoid harsh raised-card effects.

Common shadow values:

- Small card: `rgba(0, 0, 0, 0.1) 0px 0px 4px -2px`
- Feature card: `rgba(0, 0, 0, 0.082) 0px 0.36px 1.8px -1.4px, rgba(0, 0, 0, 0.07) 0px 1.37px 6.87px -2.8px, rgba(0, 0, 0, 0.016) 0px 6px 30px -4.25px`
- Blue glow: `rgba(20, 90, 255, 0.1) 0px 0px 100px -28px`

## Layout

- Use full-width light sections with centered content capped at 1200px.
- Hero is centered and single-column: badge, large headline, compact body copy, pill CTA.
- A pale blue/lavender gradient or wash can sit behind the hero product area.
- Product UI screenshots appear as large floating CRM boards below the hero.
- Feature sections use centered headings and descriptions above large rounded product mockups.
- Logo strip is a centered 4-by-2 monochrome grid.
- Footer can shift to a dark navy surface.
- Navigation is horizontal: logo left, links centered, login and CTAs right.

## Imagery

Preferred imagery:

- Kanban-style CRM pipeline boards.
- Deal cards, company avatars, timestamps, assignees, and activity notes.
- Prospect/contact list UI, email thread panels, contact detail panels.
- Monochrome customer logos.
- Small flat trust badges.

Avoid:

- Lifestyle photography.
- 3D renders.
- Heavy illustrations.
- Decorative graphic systems.
- Busy multi-color art.

## Motion

Motion is restrained.

- Use simple ease transitions.
- Animate color shifts, opacity, and small shadow changes.
- Avoid spring, bounce, parallax, and entrance choreography.
- Product UI should remain still and immediately readable.

