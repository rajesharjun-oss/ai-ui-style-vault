# Typography

## Feather

- **Role:** Rounded display face for section titles and high-emotion marketing headings.
- **Fallback:** Feather Bold, Nunito Black, rounded extra-bold sans
- **Weight:** 700
- **Sizes:** 48px, 64px
- **Line height:** 1.20
- **Letter spacing:** -0.0200em
- **Rule:** Do not use below 48px.

## Duolingo Sans

- **Role:** Body, nav, labels, subheadings, links, and smaller emphasis.
- **Fallback:** DIN Next, Inter, Nunito Sans, ui-sans-serif, system-ui
- **Weights:** 500, 700
- **Sizes:** 13px, 14px, 15px, 17px, 19px, 32px
- **Line heights:** 1.15, 1.18, 1.20, 1.21, 1.23, 1.33, 1.40, 1.41, 1.47
- **Letter spacing:** normal for body, 0.0530em for uppercase nav labels

## Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| caption | 13px | 1.23 | 700 | 0 | `--text-caption` |
| nav-label | 15px | 1.33 | 700 | 0.795px | `--text-nav-label` |
| body | 17px | 1.18 | 500 | 0 | `--text-body` |
| subheading | 19px | 1.4 | 700 | 0 | `--text-subheading` |
| heading-sm | 32px | 1.2 | 700 | 0 | `--text-heading-sm` |
| heading | 48px | 1.2 | 700 | -0.96px | `--text-heading` |
| display | 64px | 1.2 | 700 | -1.28px | `--text-display` |

## Rules

- Use Feather-style display only for 48-64px section headings.
- Use duolingo-sans style type for everything else.
- Reserve uppercase 15px with 0.0530em tracking for nav and language labels.
- Keep body copy at 17px/500 and Pencil Gray.

