# Typography

## Display Family

```css
font-family: "Rhymes Display", "Playfair Display", "Cormorant Garamond", serif;
font-weight: 300;
font-feature-settings: "blwf", "cv03", "cv04", "cv09", "cv11";
```

Use Rhymes Display 300 for hero and section-opening display copy. Playfair or Cormorant are prototype fallbacks only.

## Body Family

```css
font-family: "Suisse Intl", "Suisse Intl Book", Inter, Sohne, sans-serif;
font-feature-settings: "blwf", "cv03", "cv04", "cv09", "cv11";
```

Use Suisse-style humanist sans for body and UI. Use Aktiv Grotesk only for longer neutral paragraphs when needed.

## Scale

| Token | Family | Size | Weight | Line Height | Letter Spacing |
| --- | --- | ---: | ---: | ---: | ---: |
| `caption` | Suisse Intl | 11px | 450 | 0.8 | 0.1px |
| `ui-small` | Suisse Intl | 13px | 500 | 1.0 | -0.01em |
| `body-sm` | Suisse Intl | 14px | 450 | 1.3 | -0.01em |
| `body` | Suisse Intl | 16px | 450 | 1.25 | -0.01em |
| `body-long` | Aktiv Grotesk | 15px | 400 | 1.3 | 0 |
| `heading-sm` | Aktiv Grotesk | 20px | 400 | 1.3 | 0 |
| `heading` | Rhymes Display | 32px | 300 | 1.1 | -0.32px |
| `display` | Rhymes Display | 88px | 300 | 0.95 | -1.76px |

## Rules

- Do not use bold or semibold display weights.
- Use Rhymes Display 300 at 88px for major openings.
- Use Suisse Intl 450 for body copy.
- Body copy should sit at 14px to 16px.
- Display headlines should not exceed two lines.

