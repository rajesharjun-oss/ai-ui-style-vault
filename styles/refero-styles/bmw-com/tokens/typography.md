# Typography

## Families

| Token | Family | Fallback | Role |
| --- | --- | --- | --- |
| `--font-bmwtypenextlatin` | BMWTypeNextLatin | Inter | Workhorse UI, nav, links, body, footer |
| `--font-bmwtypenextlatin-light` | BMWTypeNextLatin Light | Inter Light | Large display heading only |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- | --- |
| Body small | 16px | 400 | 1.6 | normal | `--text-body-sm` |
| Body | 18px | 400 or 900 | 1.63 | normal | `--text-body` |
| Display | 60px | 300 | 1.3 | normal | `--text-display` |

## Rules

- Use the light display face only at large sizes.
- Keep the signature heading at weight 300.
- Use 16px regular text for nav links, footer links, and inline actions.
- Use 700 or 900 sparingly for emphasis or brand lockups.
- Avoid condensed, decorative, handwritten, or editorial serif typefaces.

## Implementation Notes

If `BMWTypeNextLatin` is not licensed or available, use Inter with a light weight for the display moment. The point is not an exact font clone; the point is restrained geometric sans typography with premium spacing.
