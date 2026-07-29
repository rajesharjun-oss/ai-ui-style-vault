# Typography

## Fonts

- Primary: `Poppins`
- Primary fallback: `Inter`, `DM Sans`, `Manrope`, `ui-sans-serif`, `system-ui`
- Serif accent: `CanelaDeck`
- Serif fallback: `Playfair Display`, `DM Serif Display`, `Lora`, `serif`

## Primary Behavior

Poppins handles display headlines, headings, UI, navigation, labels, buttons, and most body copy. Use weight 500 for display and headings, 400 for normal body, and 600 to 700 for buttons or emphasis.

```css
font-feature-settings: "clig" 0, "liga" 0;
```

## Serif Accent Behavior

CanelaDeck is a body-size editorial accent. Use it sparingly around 16px to add a premium newsroom tone. Do not use it as the main heading system.

## Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Caption | 11px | 1.5 | 500 | 0.143px |
| Body Small | 14px | 1.55 | 600 | 0 |
| Body | 16px | 1.5 | 400 | 0 |
| Subheading | 20px | 1.4 | 600 | -0.2px |
| Heading Small | 25px | 1.25 | 500 | -0.4px |
| Heading | 40px | 1.2 | 500 | -0.8px |
| Heading Large | 44px | 1.15 | 500 | -0.88px |
| Display | 64px | 1 | 500 | -1.98px |

## Rules

- Use Poppins 64px weight 500 with -1.98px tracking for display headlines.
- Use wide positive tracking only on 11px to 12px uppercase labels.
- Keep body text between 14px and 18px.
- Use CanelaDeck only as a sparse body accent.
- Do not use letter spacing above 0.05em on text larger than 14px.
