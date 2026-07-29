# Spacing And Shape

## Spacing

| Purpose | Value | Notes |
|---|---:|---|
| Density | spacious | Command-focused, not dense |
| Base unit | 4px | Token foundation |
| Max width | 1440px | Generous centered container |
| Section gap | 96px | Minimum major-section spacing |
| Button padding | 8px 12px | Compact black CTA |
| Chip padding | 4px 8px | Suggestion chips |
| Prompt input padding | 16px | Large prompt surface |
| Template grid | 3 columns | Desktop gallery pattern |

## Shape

| Element | Radius | Notes |
|---|---:|---|
| Suggestion chip | 6px | Small bordered prompts |
| Button | 8px | Primary and secondary actions |
| Card | 12px | Template cards |
| Prompt input | 12px | Main input surface |
| Filter pill | 9999px | Category filters only |

## Elevation

Template card:

```css
0 0 0 1px rgba(0, 0, 0, 0.08),
0 2px 1px rgba(0, 0, 0, 0.04)
```

Modal or popover:

```css
0 25px 50px -12px rgba(0, 0, 0, 0.25)
```

Do not use shadows on buttons or inputs.
