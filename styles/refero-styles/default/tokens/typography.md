# Typography

## Font Families

| Role | Family | Notes |
|------|--------|-------|
| All text | `Inter` | Use the variable font when possible |

Recommended OpenType features:

```css
font-feature-settings: "ss01" 1, "ss03" 1;
```

## Scale

| Token | Size | Weight | Line height | Tracking | Use |
|-------|------|--------|-------------|----------|-----|
| Body Large | 14px | 400-500 | 1.43 | -0.32px | Compact copy and table text |
| Body XL | 16px | 400 | 1.5 | 0 | Main body copy |
| Subheading | 18px | 450 | 1 | -0.61px | Compact subheads |
| Heading | 32px | 400 | 1.25 | -0.64px | Section headings |
| Heading Large | 42px | 400 | 1.2 | -0.88px | Large headings |
| Display | 52px | 400 | 1 | -1.3px | Hero display |
| Display Large | 64px | 400 | 0.94 | -1.28px | Oversized display |

## Rules

- Keep all large headlines at weight 400.
- Use fractional weights in body/UI only when the font supports them.
- Tighten tracking at small sizes for a more engineered feel.
- Enable `ss01` and `ss03` to make Inter feel more geometric.
- Do not use bold display type.
