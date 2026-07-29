# Typography

## Families

| Token | Family | Fallback | Role |
| --- | --- | --- | --- |
| `--font-d-din` | D-DIN | Barlow, DIN Next Condensed | Navigation, body, labels, buttons |
| `--font-d-din-bold` | D-DIN-Bold | Barlow Bold, DIN Next LT Pro Bold | 48px section headlines |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- | --- |
| Caption | 10px | 400 | 0.94 to 1.5 | 0.09em | `--text-caption` |
| Body small | 12px | 400 | 1 to 1.5 | 0.10em | `--text-body-sm` |
| Body | 13px | 400 or 700 | 0.94 to 1.7 | 0.10em | `--text-body` |
| Body large | 16px | 400 | 1.5 | 0.10em | `--text-body-lg` |
| Section headline | 48px | 700 | 1 to 1.25 | 0.02em | `--text-section-headline` |

## OpenType

When available, use tabular and alternate industrial forms:

```css
font-feature-settings: "tnum" 1, "ss01" 1;
```

## Rules

- Small text should feel like instrument readouts.
- Navigation, labels, and buttons should use uppercase tracked text.
- Body copy can remain sentence case if content requires it, but keep the wide tracking.
- Headlines are uppercase at 48px with tighter tracking.
- Avoid humanist sans, warm serif, handwritten, or editorial fonts.
