# Typography

## Fonts

- Primary: `Gill Sans`
- Primary fallback: `Gill Sans MT Pro`, `Avenir`, `Proxima Nova`, `Museo Sans`, `ui-sans-serif`, `system-ui`
- Label mono: `Fira Mono`
- Label fallback: `JetBrains Mono`, `IBM Plex Mono`, `ui-monospace`, `monospace`

## Primary Behavior

Gill Sans carries headings, body copy, wordmarks, property names, section text, and links. Use weight 400 for most text and weight 500 for property titles, subheadings, and the wordmark.

## Mono Behavior

Fira Mono carries labels, badges, navigation, categories, prices, and metadata. Use uppercase text, wide tracking, and small sizes so the labels read like printed museum tags.

```css
font-feature-settings: "tnum" 1, "ss01" 1;
```

## Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Label | 10px | 1.5 | 500 | 0.183em |
| Caption | 12px | 1.43 | 400 | 0.167em |
| Body Small | 15px | 1.43 | 400 | 0 |
| Body | 16px | 1.25 | 400 | 0 |
| Subheading | 21px | 1.25 | 500 | 0 |
| Heading Small | 24px | 1.25 | 500 | 0 |
| Heading Large | 33px | 1.2 | 400 | 0 |
| Display Wordmark | 64px | 1 | 500 | 0 |

## Rules

- Do not introduce a third typeface.
- Do not use heavy weights above 500.
- Do not set labels without tracking.
- Use Fira Mono for every nav, label, badge, price, and metadata element.
- Use Gill Sans for all editorial copy.
