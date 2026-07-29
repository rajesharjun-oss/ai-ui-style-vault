# ClickUp - Style Reference

ClickUp is a light productivity-dashboard system. It uses white canvas, oversized confident headlines, black pill CTAs, grayscale product structure, dense screenshots, status pills, avatars, award badges, and a single controlled rainbow-gradient animation. It should feel hard-working and product-rich, not airy or decorative.

## Theme

- Theme mode: light.
- Visual temperature: crisp white and neutral grayscale, with targeted violet, blue, green, and gradient accents.
- Surface logic: white canvas, off-white cards, pale gray section bands, dark panels for contrast.
- Energy: busy, productive, high-contrast, dashboard-native, SaaS confident.

## Core Principles

1. Show the product UI as the hero evidence.
2. Use oversized heavy headlines and tight tracking.
3. Use full-pill buttons, chips, tags, and badges.
4. Use `#202020` for primary filled actions and large text, not pure black.
5. Keep brand violet away from primary CTA fills.
6. Reserve blue for links, outline actions, checkmarks, and active tags.
7. Use the conic rainbow border only once per section at most.
8. Keep product density high inside sections and spacing generous between sections.

## Color System

| Name | Value | Role |
| --- | --- | --- |
| Signal White | `#ffffff` | Page canvas, cards, light button fills |
| Ink Black | `#202020` | Primary CTA fill, heading text, main UI copy |
| Onyx | `#090c1d` | Maximum-scale display text and stat numbers |
| Carbon | `#2a2a2a` | Borders, dark text on light fills, section dividers |
| Slate | `#646464` | Secondary body text, nav labels, icon fills |
| Ash | `#838383` | Tertiary text, muted labels, disabled states |
| Fog | `#b3b3b3` | Subtle card borders, dividers, placeholders |
| Cloud | `#d4d4d4` | Hairline borders, dashed dividers, input outlines |
| Bone | `#e8e8e8` | Default border color and button outlines |
| Plaster | `#e9ebf0` | Large neutral section band |
| Mercury | `#eeeeee` | Neutral chips, soft badge surfaces |
| Mist | `#f8f9fa` | Light action fill and secondary card surface |
| Brand Violet | `#6647f0` | Brand badges, product identity marks, short status labels |
| Signal Blue | `#0091ff` | Links, outline action border, checkmarks, active tag text |
| Mint | `#6ee7b7` | Green text accent and done-state surfaces |
| Emerald | `#00c07a` | Green outlines, focused edges, positive dividers |
| Teal Tag | `#16c0a4` | Teal state badge accent |

Gradient roles:

- Rainbow conic: animated border around one hero CTA or premium element.
- Primary gradient: cyan-to-magenta text or premium brand mark treatment.
- Dark fade: dark feature panel background from charcoal into black.

## Typography

Primary display type is Plus Jakarta Sans. Use it for headings, major claims, buttons, and brand-forward UI. Fallback: Inter or General Sans.

Inter is the secondary workhorse for body text in cards, captions, dense product UI, and micro labels.

Sometype Mono is used for uppercase status labels, technical tags, and tiny tracking-wide metadata. Fallback: JetBrains Mono or IBM Plex Mono.

Recommended scale:

| Token | Family | Size | Weight | Line Height | Letter Spacing |
| --- | --- | ---: | ---: | ---: | ---: |
| Body Small | Inter | 14px | 400 | 1.5 | -0.01px |
| Body | Inter | 16px | 400 | 1.5 | -0.01px |
| Subheading | Plus Jakarta Sans | 20px | 500 | 1.5 | -0.02px |
| Heading Small | Plus Jakarta Sans | 34px | 650 | 1.2 | -0.04em |
| Heading | Plus Jakarta Sans | 48px | 650 | 1.25 | -0.035em |
| Heading Large | Plus Jakarta Sans | 60px | 700 | 1.1 | -0.035em |
| Display | Plus Jakarta Sans | 80px | 700 | 1.2 | -0.04em |
| Mono Label | Sometype Mono | 10px to 12px | 400 | 1.2 to 2.0 | 0.06em to 0.08em |

Rules:

- Use Plus Jakarta Sans at 650 to 800 for display text 34px and larger.
- Apply around `-0.04em` tracking on display text 48px and above.
- Do not use Inter as the display face.
- Do not use positive body tracking.
- Use Inter for small body text and captions.

## Spacing And Shape

- Density: compact.
- Base unit: 4px.
- Max content width: 1200px.
- Section gap: 80px.
- Card padding: 28px.
- Element gap: 12px.
- Spacing values: 4, 8, 12, 16, 20, 24, 28, 32, 40, 48, 52, 56, 72, 80, 100.

Radius:

- Inputs: 9px.
- Cards: 12px.
- Images: 16px.
- Large cards: 20px.
- Tags: 100px.
- Buttons and badges: 9999px.
- Avatar clusters: 9999px circular geometry.

## Elevation

The default system is flat.

- Most cards use borders and off-white surfaces rather than shadows.
- Default border: `1px solid #e8e8e8`.
- Product screenshot cards may use a soft directional shadow as an exception.
- Do not stack many shadow levels inside one section.
- Gradients are not regular card backgrounds; they are brand effects.

## Layout

- Use max-width 1200px centered content.
- Hero is a two-column split: left side text, benefits, CTA, and tags; right side a large product screenshot.
- Use announcement bar, top nav, hero, logo strip, illustration section, awards grid, stats, and footer.
- Section gaps are large, around 80px.
- Internal section spacing is compact, around 8px to 12px.
- Use product UI screenshots with sidebar, tasks, inbox, statuses, avatars, and dense lists.
- Use social proof logos as grayscale flat rows.
- Use award badges in a 3-column grid when relevant.

## Imagery

Preferred imagery:

- Real product UI screenshots.
- Task boards, inbox panels, docs, chats, and dashboard lists.
- Status pills and avatar clusters inside product screenshots.
- G2 award badges or similar award cards.
- Grayscale trusted-by logo rows.
- Abstract gray line-art only as a secondary illustration.

Avoid:

- Lifestyle photography.
- Stock people photos.
- Purely abstract gradient hero art.
- Decorative illustrations that replace product UI.
- Hero video.

## Motion

Motion is expressive but constrained.

- Dominant state duration: around 0.45s.
- Fast hover feedback: around 0.15s.
- Use cubic-bezier(0.33, 1, 0.68, 1) for soft settling.
- Conic rainbow border can rotate linearly.
- Use one continuous rainbow animation per viewport at most.
- Avoid making every component animated.

