# Typography

## Display Family

```css
font-family: "Plus Jakarta Sans", Inter, "General Sans", Arial, sans-serif;
font-feature-settings: "calt" 0;
```

Use Plus Jakarta Sans for display headings, hero claims, major section titles, and CTA labels.

## Body Family

```css
font-family: Inter, system-ui, Arial, sans-serif;
font-feature-settings: "calt" 0, "clig" 0, "liga" 0;
```

Use Inter for supporting copy, dense product UI, captions, cards, and micro labels.

## Mono Family

```css
font-family: "Sometype Mono", "JetBrains Mono", "IBM Plex Mono", monospace;
```

Use Sometype Mono for uppercase status labels, feature tags, code-like labels, and tracked metadata.

## Scale

| Token | Family | Size | Weight | Line Height | Letter Spacing |
| --- | --- | ---: | ---: | ---: | ---: |
| `body-sm` | Inter | 14px | 400 | 1.5 | -0.01px |
| `body` | Inter | 16px | 400 | 1.5 | -0.01px |
| `subheading` | Plus Jakarta Sans | 20px | 500 | 1.5 | -0.02px |
| `heading-sm` | Plus Jakarta Sans | 34px | 650 | 1.2 | -0.04em |
| `heading` | Plus Jakarta Sans | 48px | 650 | 1.25 | -0.035em |
| `heading-lg` | Plus Jakarta Sans | 60px | 700 | 1.1 | -0.035em |
| `display` | Plus Jakarta Sans | 80px | 700 | 1.2 | -0.04em |
| `mono-label` | Sometype Mono | 10px to 12px | 400 | 1.2 to 2.0 | 0.06em to 0.08em |

## Rules

- Use weights 650 to 800 for display text above 34px.
- Use around `-0.04em` tracking for display text 48px and larger.
- Do not use Plus Jakarta Sans below 14px.
- Do not use Inter as display text.
- Do not apply positive tracking to body text.

