# Typography

## Font Families

| Role | Family | Fallback |
|------|--------|----------|
| Display | `new-kansas` | `DM Serif Display`, `Georgia`, serif |
| Body and UI | `Nunito Sans` | `ui-sans-serif`, system-ui |

Google Fonts export for the body family:

```text
https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;500;600;700&display=swap
```

## Scale

| Token | Size | Weight | Line height | Tracking | Use |
|-------|------|--------|-------------|----------|-----|
| Caption | 12px | 400-700 | 1.33-1.5 | 0 to -0.01px | Metadata, badges, helper text |
| Body Small | 14px | 400-700 | 1.43 | 0 to -0.011px | Secondary copy, nav, card details |
| UI Medium | 15px | 600 | 1.33 | -0.012px | Button and nav text |
| Body | 16px | 400-700 | 1.5 | 0 to -0.011px | Main copy, forms, card content |
| Body Large | 18px | 400-700 | 1.56 | 0 | Lead copy |
| Subheading | 20px | 400-700 | 1.4 | -0.012px | Section intros and compact headings |
| Heading Small | 28px | 500 | 1.2-1.35 | -0.01px | Small serif headings |
| Heading | 48px | 400-500 | 1.2 | -0.013px | Hero and major section headings |
| Display | 64px | 400-500 | 1.2 | -0.023px | Large landing page display |

## Rules

- Keep serif display type light and calm.
- Use `Nunito Sans` for every body, form, nav, and button surface.
- Do not use the serif below 28px.
- Do not make display headlines weight 700.
- Keep headline copy short enough to breathe in centered compositions.
