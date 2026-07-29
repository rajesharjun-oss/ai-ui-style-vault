# Playful - Style Reference

> Sunlit paper notebook with a hot-pink highlighter: warm cream surfaces, one vivid magenta accent, heavy italic Inter display type, pill CTAs, and soft lifted cards.

## Theme

Light. The page background is warm cream rather than clinical white. The style should feel friendly, tactile, and editorial, like a product interface printed on soft notebook paper.

## Design Story

Build around one bold type moment per section. The main visual voice is oversized italic Inter, usually 70px to 79px, set in black or near-black. Everything else should give that type room: centered hero stacks, quiet body copy, warm whitespace, a single magenta CTA, and playful app tiles.

Color is deliberately disciplined. Hot Magenta does all chromatic work: logo, primary action, link accents, and occasional highlight wash. Do not add blue, green, orange, purple, or rainbow UI color.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Hot Magenta | `#ff2e95` | `--color-hot-magenta` | Primary CTA fill, logo mark, links, accent strokes |
| Ink Black | `#000000` | `--color-ink-black` | Main heading text, button text, heavy borders, dark nav band |
| Oat Canvas | `#f6f2ee` | `--color-oat-canvas` | Page background and warm cream surface |
| Soft Ink | `#111111` | `--color-soft-ink` | Body text, headings, dark card surface |
| Slate | `#0f172a` | `--color-slate` | Secondary copy and muted body text |
| Charcoal | `#414040` | `--color-charcoal` | Neutral form states, badge text, quiet UI feedback |
| Stone | `#848383` | `--color-stone` | Icon strokes, helper text, subtle dividers |
| Paper White | `#ffffff` | `--color-paper-white` | Card surfaces and elevated panels |
| Warm Mist | `#e8e5e0` | `--color-warm-mist` | Hairline borders and dividers |
| Sand | `#e2dcd6` | `--color-sand` | Secondary borders on warm surfaces |
| Driftwood | `#c3c1bf` | `--color-driftwood` | Muted fills and shadow-adjacent tones |
| Midnight | `#202126` | `--color-midnight` | Deep heading variant with subtle cool cast |

## Typography

Primary typeface: Inter.

- Use Inter for everything: display, body, nav, inputs, labels, buttons, FAQ cards, and captions.
- Display headlines use Inter 700 or 900 italic at 70px to 79px.
- Body uses Inter 400 at 16px to 18px.
- Captions use Inter 500 at about 13px to 14px.
- Use barely tightened letter spacing around `-0.002em`.
- Enable `"ss01"` and `"cv11"` when the font pipeline supports it.

Fallback: Arial is acceptable only as degradation for some input or button contexts. Prefer Inter whenever possible.

## Type Scale

| Role | Size | Weight | Line height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 13px | 500 | 1.4 | -0.026px |
| Body | 16px | 400 | 1.5 | -0.032px |
| Body Large | 18px | 400 | 1.5 | -0.036px |
| Subheading | 26px | 600 or 700 | 1.23 | -0.052px |
| Heading Small | 30px | 600 or 700 italic | 1.2 | -0.06px |
| Display | 79px | 700 or 900 italic | 1 | -0.158px |

## Spacing And Shape

- Density: spacious.
- Page max width: 1200px.
- Section gap: 113px.
- Card padding: 24px.
- Element gap: 10px to 16px.
- Tags: 999px radius.
- Cards: 44px radius.
- Images: 16px radius.
- Inputs: 99px radius.
- Buttons: 99px pill radius.

## Elevation

Use exactly one card-level shadow stack:

`0 32px 80px rgba(0, 0, 0, 0.22), 0 2px 8px rgba(0, 0, 0, 0.08)`

Apply it to cards, FAQ rows, and app tiles only. Do not apply shadows to text, buttons, icons, inputs, or navigation.

## Components

### Primary Pill CTA

Hot Magenta fill, white or black text depending contrast context, Inter 600 at 16px, 99px radius, and 14px 24px padding. This is the main action treatment and should appear sparingly.

### Email Capture Composite

Use one white pill container with 99px radius that holds an Oat Canvas input and a Hot Magenta CTA. The input uses a 1px Charcoal border, 16px Inter placeholder text, and muted gray copy. Input and button should read as one combined control.

### Editorial Display Headline

Inter 700 or 900 italic, 70px to 79px, line-height 1, color Ink Black or Soft Ink. Center it and keep it to one or two lines. This is the signature move.

### App Tile Card

Paper White surface, 44px radius, deep diffused shadow, roughly 140px to 180px square. Place a centered soft 3D illustration inside. Tiles can be slightly tilted and overlapped to feel like a hand of cards.

### FAQ Accordion Card

Paper White surface, 44px radius, optional warm border, same shadow stack, and 12px to 16px vertical gaps. Question text uses Inter 600 italic at 16px to 18px. Chevron icon uses Stone.

### Category Navigation Bar

Full-width black band, white Inter 500 labels at 14px to 16px, horizontal scroll, and 24px to 32px item spacing. It is the only dark band on the page.

### Logo Wordmark

Hot Magenta italic wordmark with a small rounded-square geometric mark. Use it as both brand identity and navigation.

### Gradient Highlight Section

Soft large gradient from Hot Magenta through lavender-pink into Oat Canvas. Keep it atmospheric, without hard edges. Use one centered 30px italic headline.

## Layout

Use a centered 1200px container and spacious 113px vertical section rhythm. The hero stack is centered: display headline, subtext, email and CTA pill composite, then a tilted row of app tiles. Later sections alternate warm cream, a magenta gradient wash, a full-width black category nav band, two-column FAQ layout, and a centered final CTA.

## Imagery

Use illustration, not photography. The image language is soft 3D app icons and playful character-like forms with rounded, candy-like surfaces. Keep UI icons minimal line icons in muted gray. Avoid lifestyle photography, realistic people, screenshots as the primary hero, and generic SaaS device mockups.

## Rules

Do:

- Use Oat Canvas for full-page backgrounds.
- Use Hot Magenta only for CTA, logo, links, and small accent strokes.
- Use Inter 700 or 900 italic for large display headlines.
- Use 44px rounded cards and 99px pill controls.
- Apply the two-layer shadow only to cards and tiles.
- Center hero compositions with generous section gaps.
- Keep icons stroke-based in Stone.

Do not:

- Do not use upright bold display headlines.
- Do not add extra accent colors.
- Do not switch full-page surfaces to pure white.
- Do not use sharp 0px to 4px radii on cards or buttons.
- Do not stack more than two type weights on a screen.
- Do not place Paper White cards directly on a white background.
- Do not use shadows on text, buttons, icons, or inputs.
