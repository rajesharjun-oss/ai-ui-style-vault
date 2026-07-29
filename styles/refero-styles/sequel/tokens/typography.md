# Typography

## Fonts

- Primary: `VisueltPro`
- Primary fallback: `Inter`, `Satoshi`, `General Sans`, `ui-sans-serif`, `system-ui`
- Accent serif: `Bradford`
- Accent fallback: `Canela`, `Tiempos Headline`, `GT Super`, `Georgia`, `serif`

## Primary Behavior

VisueltPro carries almost everything: navigation, labels, body copy, buttons, hero headlines, and section headings. Use weights 300, 400, and 500 only. Avoid bold weights.

Use Bradford only for a single italic emotional word inside a headline. Do not use it for full headings, body text, navigation, or buttons.

## OpenType

```css
font-feature-settings: "ss01" 1, "cv11" 1;
```

## Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Label Small | 11px | 1.5 | 500 | 0.55px |
| Body | 16px | 1.5 | 400 | 0 |
| Body Large | 20px | 1.5 | 400 | 0 |
| Subheading | 30px | 1.2 | 500 | -0.75px |
| Heading | 54px | 1.2 | 300 | 0 |
| Heading Large | 57px | 1 | 500 | -2.85px |
| Display | 128px | 1 | 500 | -3.2px |

## Rules

- Use 54px weight 300 for elegant narrative headings.
- Use 57px to 128px weight 500 for dramatic display moments.
- Use positive tracking for uppercase labels, badges, and captions.
- Use negative tracking at large display sizes.
- Keep body text comfortable at 16px to 20px with 1.5 line-height.
