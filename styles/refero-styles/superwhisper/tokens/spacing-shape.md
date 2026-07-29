# Spacing And Shape

## Spacing

| Purpose | Value | Notes |
|---|---:|---|
| Density | comfortable | Focused tool rhythm |
| Base unit | 4px | Token foundation |
| Max width | 1200px | Centered layout |
| App panel gap | 12px to 20px | Voice UI and command surfaces |
| Card padding | 24px | Feature cards and panels |
| Section gap | 80px to 112px | Marketing/product sections |
| Hero padding | 96px to 128px | Top hero area |
| Chip padding | 6px 12px | Command chips |
| CTA padding | 12px 22px | Pill buttons |

## Shape

| Element | Radius | Notes |
|---|---:|---|
| Main CTA | 9999px | Full pill |
| Voice recorder | 9999px | Large pill control |
| Command chip | 9999px | Compact command labels |
| Cards | 20px | Feature cards |
| App panels | 24px | Large product demo panels |
| Inputs | 14px | Prompt and settings inputs |
| Transcript card | 16px | Transcript blocks |

## Elevation

Glass card:

```css
0 24px 80px rgba(0, 0, 0, 0.35),
0 0 0 1px rgba(255, 255, 255, 0.06)
```

Aurora glow:

```css
0 0 40px rgba(139, 92, 246, 0.28),
0 0 64px rgba(34, 211, 238, 0.18)
```

Use glow only around key active voice and CTA moments.
