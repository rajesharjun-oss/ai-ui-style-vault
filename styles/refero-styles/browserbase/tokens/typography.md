# Typography

## Families

| Token | Family | Fallback | Role |
| --- | --- | --- | --- |
| `--font-plain` | plain | Inter, Geist | Body copy, nav, UI labels, buttons |
| `--font-gtplanar` | gtPlanar | GT America, Inter Tight | Display headlines and section headings |
| `--font-gtstandardmono` | gtStandardMono | JetBrains Mono, IBM Plex Mono | Metadata, captions, eyebrows, stat labels |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- | --- |
| Caption | 14px | 400 | 1.2 | 0.6px | `--text-caption` |
| Body | 16px | 400 | 1.5 | 0.11px | `--text-body` |
| Subheading | 24px | 500 | 1.3 | -0.12px | `--text-subheading` |
| Heading | 34px | 400 or 500 | 1.15 | -0.68px | `--text-heading` |
| Heading large | 45px | 500 | 1.1 | -0.9px | `--text-heading-lg` |
| Display | 189px | 500 | 1 | -9.45px | `--text-display` |

## OpenType

When using gtPlanar, enable:

```css
font-feature-settings: "ss05" 1;
```

Use this on display and heading text only.

## Rules

- Display headings should feel dense, geometric, and editorial.
- Body copy should stay plain and readable.
- Mono labels should be uppercase, small, and positively tracked.
- Do not use display type for long paragraphs.
- Do not use mono type for body copy.
