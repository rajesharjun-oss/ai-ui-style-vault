# Nofilter.space - Style Reference

Nofilter.space feels like an uncompromising editorial index: white paper, black-gray ink, square media, strict 3-column grids, tiny filter controls, and no decorative interface effects.

**Theme:** light

## Summary

Build this style as a printed page, not a software surface. There is no z-axis, no card elevation, no brand color, and no rounded image treatment. The system relies on Pragmatica type, shared baselines, square edges, 1px rules, and austere white space.

## Tokens - Colors

| Name | Value | Token | Role |
|---|---:|---|---|
| Paper | `#ffffff` | `--color-paper` | Full page background and card surface |
| Ink | `#333333` | `--color-ink` | Primary text, hairlines, borders, checkbox strokes |
| Carbon | `#000000` | `--color-carbon` | Emphasis stroke, rare strongest text, image contrast |

## Typography

Use `Pragmatica` as the entire system voice. It should feel plain, editorial, and unsentimental. Fallback to Helvetica Neue or Arial.

| Role | Size | Weight | Line Height | Usage |
|---|---:|---:|---:|---|
| Nav/filter label | 12px | 400 | 1.2 | FEED, ABOUT, WORDS, PROJECTS, REPORTAGE |
| Meta/byline/date | 12px | 400 | 1.2 | Author, date, category labels |
| Body/list copy | 14px | 400 | 1.4 | Short summaries and index text |
| Headline | 24px | 400 | 1.14 | Editorial image-card headlines |
| Featured headline | 30px | 400 | 1.14 | Bordered featured card headline |
| Wordmark | 35px | 400 | 1.14 | NOFILTER. SPACE header |

## Spacing And Shape

- Page background: white.
- Grid: 3 columns for editorial cards.
- Grid gutter: 30px row and column gap.
- Outer/grid side padding: about 35px.
- Featured card padding: 35px.
- Wordmark bottom margin: 40px.
- Content group top margin: 40-60px.
- Card radius: 0px.
- Image radius: 0px.
- Checkbox size: about 12px.
- Border width: 1px.

## Components

**Top Nav Bar**

White background, no border, no shadow. Left side: `FEED` and `ABOUT` in 12px Pragmatica with 20px gap. Right side: checkbox-and-label filter pairs for `WORDS`, `PROJECTS`, and `REPORTAGE`. Each checkbox is a 1px Ink square around 12px.

**Wordmark Header**

Full-width row reading `NOFILTER. SPACE`. Use 35px Pragmatica weight 400, Ink, 1.14 line height, left aligned. Keep a 40px bottom margin.

**Editorial Image Card**

No border, no radius, no shadow. Image fills its column at native aspect ratio. Below it: 24px headline, then 12px byline, then 12px date. Keep about 35px of grid gutter breathing room.

**Bordered Featured Card**

White surface, 1px Ink border, 0px radius, 35px padding. Headline at 30px, 1.14 line height, then byline/date stacked below in 12px text.

**Section Row**

Use 40-60px margin-top between content groups. Inside the 3-column grid, use 30px row and column gaps. Cards should align to a shared baseline.

**Checkbox Filter**

1px Ink square plus uppercase label. No colored active state. If active, mark with a plain check or filled square in Ink.

## Layout And Imagery

- White full-page canvas.
- No shadows, no panels, no rounded wrappers.
- Use a rigid 3-column editorial grid.
- Align cards to a shared baseline.
- Use full-column editorial photography and image-forward cards.
- Images should appear at native aspect ratio and square corners.
- Avoid illustrations, gradients, and decorative chrome.

## Implementation Rules

The design deliberately uses zero elevation. Elevation is communicated only with 1px borders, whitespace, and typographic hierarchy. Treat the page as a printed surface, not an app.
