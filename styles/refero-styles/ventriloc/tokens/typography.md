# Typography

## PolySans

- **Role:** Headings, display text, nav items, and button labels.
- **Fallback:** Inter Tight or Space Grotesk at weight 400
- **Weight:** 400 only
- **Sizes:** 12px, 13px, 16px, 32px, 40px, 66px
- **Line height:** 0.91-1.38
- **Letter spacing:** -0.0200em
- **Rule:** Never bold PolySans-style headings.

## Inter

- **Role:** Body copy, captions, metadata, helper text, and UI labels.
- **Fallback:** system-ui or Roboto
- **Weights:** 400, 500, 600
- **Sizes:** 12px, 13px, 14px, 15px, 16px, 18px
- **Line height:** 1.15-1.50

## Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| micro | 13px | 1.2 | 500 | 0 | `--text-micro` |
| caption | 14px | 1.43 | 500 | 0 | `--text-caption` |
| ui | 15px | 1.33 | 500 | 0 | `--text-ui` |
| body | 16px | 1.5 | 400 | 0 | `--text-body` |
| subheading | 18px | 1.25 | 400 | 0 | `--text-subheading` |
| heading | 32px | 1.19 | 400 | -0.64px | `--text-heading` |
| heading-lg | 40px | 1.2 | 400 | -0.8px | `--text-heading-lg` |
| display | 66px | 0.91 | 400 | -1.32px | `--text-display` |

## Rules

- PolySans-style text is the voice; Inter is the grammar.
- Use PolySans-style type at weight 400 for headings, nav, and buttons.
- Use Inter for paragraphs, captions, and metadata.
- Keep display line-height tight, especially 66px at 0.91.
- Use -0.02em tracking on PolySans-style elements.

