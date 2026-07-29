# Typography

## Fonts

- Primary: system UI stack
- Fallback: `system-ui`, `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `sans-serif`

## Behavior

Use no custom webfonts. The interface should render natively and quietly. Typography is utilitarian: 16px body, 14px captions, and a modest 24px heading tier.

```css
font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
```

## Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Caption | 14px | 1.43 | 400 | normal |
| Body | 16px | 1.5 | 400 | normal |
| Heading | 24px | 1.33 | 600 | normal |

## Rules

- Do not load custom fonts.
- Do not use text larger than 24px in the UI.
- Use weight 500 for row titles and compact emphasis.
- Use weight 600 only for welcome headings or compact page headings.
- Keep letter spacing normal.
