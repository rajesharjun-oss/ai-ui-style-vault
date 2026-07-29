# Typography

## Family

| Role | Preferred Font | Fallbacks | Notes |
|---|---|---|---|
| Whole system | Calibre | Inter, Satoshi, General Sans, Arial | One family for captions, body, nav, labels, and display |

## Scale

| Token | Size | Line Height | Weight | Tracking |
|---|---:|---:|---:|---:|
| `--text-caption` | 10px | 1.5 | 400-500 | 0 to -0.08px |
| `--text-body` | 14px | 1.5 | 400 | 0 |
| `--text-heading-sm` | 18px | 1.32 | 600 | 0 |
| `--text-heading` | 24px | 1.25 | 700 | -1.27px |
| `--text-heading-lg` | 26px | 1.2 | 700 | -1.38px |
| `--text-display` | 48px | 1.1 | 700 | -3.84px |
| `--text-display-lg` | 54px | 1.0 | 700 | -4.32px |

## Rules

- Use Calibre everywhere.
- Use weight 400 for body and most UI.
- Use 500-600 for nav, labels, and buttons.
- Use 700 for display headlines and large values.
- Apply `tnum` for financial values.
- Keep display tracking tight at about -0.08em.
