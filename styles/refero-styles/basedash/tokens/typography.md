# Typography

## Families

| Role | Font | Fallback | Use |
| --- | --- | --- | --- |
| UI | Inter | system-ui, sans-serif | Nav, buttons, labels, forms, body, tables, cards |
| Display | Alpha Lyrae | Cormorant Garamond, EB Garamond, PT Serif | Hero h1 and major section titles only |
| Quote | Iowan Old Style | Source Serif Pro Light, Lora, Palatino | Testimonial pull quotes |

## Type Scale

| Token | Size | Weight | Line height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 12px | 400 | 1.5 | -0.36px |
| Body Small | 14px | 400 | 1.43 | -0.42px |
| Body | 16px | 400 | 1.5 | -0.48px |
| Body Large | 18px | 400 | 1.56 | -0.54px |
| Subheading | 24px | 300 | 1.25 | -0.6px |
| Heading Small | 30px | 400 | 1.2 | -0.9px |
| Heading | 34px | 400 | 1.2 | -1.02px |
| Display | 48px | 400 | 1 | 0 |

## Implementation Notes

- Inter is the workhorse. It should handle nearly every UI surface.
- Keep body and UI letter spacing tight to preserve the engineered feel.
- Do not use the display serif for buttons, nav, badges, forms, or tables.
- Use the quote serif only when you need a deliberate human trust moment.
