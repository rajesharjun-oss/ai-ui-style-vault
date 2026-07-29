# Typography

## Families

- Primary: `WF Visual Sans Variable`
- Mono: `WF Visual Sans Mono`
- Fallback: `Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`

If the Webflow font is unavailable, use Inter as the nearest practical substitute.

## Type Scale

| Role | Size | Line Height | Tracking | Weight | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| Badge | 10px | 1.2 | 0.1em | 600 | Uppercase new tags |
| Eyebrow | 13px | 1.3 | 0.1em | 500 | Section labels |
| Small body | 14px | 1.45 | 0 | 400 | Nav, metadata, compact copy |
| Body | 16px | 1.5 | 0 | 400 | Standard paragraphs |
| Body large | 20px | 1.45 | 0 | 400 | Hero and section support copy |
| Card heading | 24px | 1.2 | -0.01em | 600 | Feature cards |
| Section heading | 40-56px | 1.08 | -0.01em | 600 | Section leads |
| Display | 56-80px | 1.04 | -0.01em | 600 | Hero headline |
| Mono label | 13px | 1.4 | 0 | 400 | Product UI labels and code-like details |

## Rules

- Keep display type large and weight 600.
- Do not use weight 400 for hero display copy.
- Do not set display headlines below 40px on desktop.
- Keep tracking tight at display sizes.
- Use only one type size inside a single heading block.
- Do not mix in serif or decorative fonts.

## Responsive Notes

On mobile, reduce hero display toward 40-48px while preserving weight 600 and tight tracking. Keep supporting copy around 16-18px and collapse layout before compressing text too hard.

