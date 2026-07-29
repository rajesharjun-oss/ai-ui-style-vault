# WHOOP - Style Reference

> Performance laboratory at midnight: clinical white lab benches beneath a black theatrical void, with one violet pulse of electricity.

**Theme:** mixed

WHOOP uses a high-contrast split-canvas system. Black sections create drama and effort; white sections create recovery and analysis. The design feels premium, clinical, athletic, and data-led. It avoids decorative SaaS illustration and relies on oversized typography, rounded photographic cards, pill actions, and full-bleed section rhythm.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Pulse Violet | `#4a53ff` | `--color-pulse-violet` | Announcement bar, brand action moments, low-frequency emphasis |
| Obsidian | `#000000` | `--color-obsidian` | Dark hero sections, primary text on light, filled neutral buttons |
| Carbon | `#191919` | `--color-carbon` | Secondary dark bands, footer sections, dark text on light |
| Fog Gray | `#808080` | `--color-fog-gray` | Muted body copy, descriptions, placeholder text |
| Ash | `#999999` | `--color-ash` | Tertiary metadata, inactive labels, disabled strokes |
| Hairline | `#e5e7eb` | `--color-hairline` | Borders, dividers, outlined buttons, input frames |
| Lab Mist | `#f3f5f9` | `--color-lab-mist` | Light feature cards and flat elevated panels |
| Paper White | `#ffffff` | `--color-paper-white` | Light page canvas, text on dark, white pill buttons |

## Tokens - Typography

- Font family: `Proxima Nova`.
- Fallback: Montserrat, Nunito Sans, or DM Sans.
- Display behavior: 120px, weight 400, line-height around 0.71, letter-spacing -4.8px.
- Heading behavior: 32px to 50px, weight 600, tight line height.
- Body behavior: 19px to 20px for confident running copy, tight tracking.
- Label behavior: 14px to 15px uppercase with 0.1em tracking.

| Role | Size | Weight | Line height | Letter spacing | Use |
|------|------|--------|-------------|----------------|-----|
| Caption | 14px | 400-500 | 1.59 | 0 | Small text and labels |
| Body Small | 16px | 400 | 1.33 | -0.48px | Short body copy |
| Body Large | 20px | 600 | 1.29 | -0.6px | Confident body and metrics |
| Subheading | 24px | 500 | 1.13 | -0.72px | Section subheads |
| Heading Small | 32px | 600 | 1.09 | -0.96px | Small feature headings |
| Heading | 35px | 600 | 1 | -1.05px | Main feature headings |
| Heading Large | 50px | 600 | 0.8 | -2px | Large section headings |
| Display | 120px | 400 | 0.71 | -4.8px | Hero display |

## Tokens - Spacing And Shape

| Purpose | Value |
|---------|-------|
| Density | comfortable |
| Max width | 1200px |
| Section gap | 80px to 120px |
| Card padding | 24px to 32px |
| Element gap | 15px to 24px |
| Spacing scale | 5, 8, 10, 12, 15, 16, 20, 24, 25, 30, 33, 36, 38, 40, 50, 92px |
| Small elements | 8px radius |
| Cards | 24px radius |
| Images | 24px radius |
| Medium rounded | 30px radius |
| Pills | 300px radius |
| Buttons | 300px radius |

## Components

- Announcement bar: full-width Pulse Violet strip, compact white text, flush above nav.
- Primary navigation: black background, white wordmark, tracked nav labels, violet pill action on the right.
- Full-bleed dark hero: black 100vh stage, huge 120px display type, tight leading, athlete-performance tone.
- Pulse Violet pill button: violet fill, white uppercase label, 300px radius, used sparingly for brand action.
- White pill button: white fill, black uppercase label, 300px radius, used on dark hero sections.
- Outlined pill button: transparent fill, Hairline border, black text, 300px radius, for tertiary actions on light sections.
- Lab Mist feature card: `#f3f5f9` background, 24px radius, no shadow, image plus copy plus pill action.
- Carousel story card: full-bleed photography inside 24px radius card with white text overlay.
- Dark CTA band: full-width black section with huge white display type.
- Membership pricing card: white card, Hairline border, 24px radius, large price type, violet selected-tier action.
- Metric overlay stat: white number and uppercase label over photography.

## Layout And Imagery

Use alternating full-bleed black and white sections. Do not soften the transition with gray. Use dramatic athlete photography as the main visual asset: running, swimming, sleep, recovery, body data, and lifestyle motion. Cards can be photographic and tall. Avoid abstract illustrations and 3D assets.

## Do

- Use 300px border radius for all buttons.
- Set display headlines at 120px with very tight line height and -4.8px tracking.
- Alternate black and white full-bleed sections with 80px to 120px gaps.
- Use Pulse Violet only for announcement bars and key brand action moments.
- Render cards at 24px radius with no drop shadow.
- Apply uppercase 0.1em tracking to nav, button, and metric labels.
- Keep body text large, around 19px to 20px.

## Do Not

- Do not add drop shadows to cards or buttons.
- Do not introduce a second accent color.
- Do not use loose line-height on large display text.
- Do not center-align long body paragraphs.
- Do not use square or tiny-radius buttons.
- Do not put colored gradients on UI surfaces.
- Do not set running prose below 16px.
