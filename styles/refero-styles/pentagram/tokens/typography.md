# Typography

### Plain - All roles - display, headings, body, caption, nav, button. The single typeface carries the entire site. Weight contrast is limited (400 vs 500) so hierarchy comes from size and tracking, not boldness. The 52px display at -0.02em tracking is anti-display: it whispers instead of shouts. Line-heights under 1.1 on 32-52px create stacked, compressed blocks where headings read as solid slabs. Open features 'kern' and 'case' hint at a typeface with carefully spaced uppercase alternates - the 'case' feature likely gives access to stylistic capital forms. - `--font-plain`
- **Substitute:** Sohne, Inter, Neue Haas Grotesk, ABC Diatype
- **Weights:** 400, 500
- **Sizes:** 13, 16, 19, 27, 32, 52
- **Line height:** 1.00 (display), 1.05-1.20 (headings), 1.25-1.32 (body), 1.88 (loose body)
- **Letter spacing:** -0.02em on 27px, -0.01em on <27px
- **OpenType features:** `"kern", "case"`
- **Role:** All roles - display, headings, body, caption, nav, button. The single typeface carries the entire site. Weight contrast is limited (400 vs 500) so hierarchy comes from size and tracking, not boldness. The 52px display at -0.02em tracking is anti-display: it whispers instead of shouts. Line-heights under 1.1 on 32-52px create stacked, compressed blocks where headings read as solid slabs. Open features 'kern' and 'case' hint at a typeface with carefully spaced uppercase alternates - the 'case' feature likely gives access to stylistic capital forms.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 13px | 1.25 | -0.13px | `--text-caption` |
| body-sm | 16px | 1.32 | -0.16px | `--text-body-sm` |
| subheading | 19px | 1.2 | -0.19px | `--text-subheading` |
| heading-sm | 27px | 1.19 | -0.54px | `--text-heading-sm` |
| heading | 32px | 1.05 | -0.64px | `--text-heading` |
| display | 52px | 1 | -1.04px | `--text-display` |
