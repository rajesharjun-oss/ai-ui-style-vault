# Spacing And Shape

## Spacing

| Purpose | Value |
|---|---:|
| Density | comfortable |
| Base unit | `8px` |
| Max width | `1432px` |
| Section gap | `64px` |
| Card padding | `40px` |
| Element gap | `16px` |

## Spacing Scale

| Name | Value | Token |
|---|---:|---|
| 8 | `8px` | `--spacing-8` |
| 16 | `16px` | `--spacing-16` |
| 24 | `24px` | `--spacing-24` |
| 32 | `32px` | `--spacing-32` |
| 40 | `40px` | `--spacing-40` |
| 64 | `64px` | `--spacing-64` |
| 72 | `72px` | `--spacing-72` |
| 80 | `80px` | `--spacing-80` |
| 200 | `200px` | `--spacing-200` |
| 216 | `216px` | `--spacing-216` |

## Border Radius

| Element | Value | Token |
|---|---:|---|
| cards | `40px` | `--radius-cards` |
| buttons | `100px` | `--radius-buttons` |
| pills | `9999px` | `--radius-pills` |
| tags | `9999px` | `--radius-tags` |

## Shadows

| Name | Value | Token |
|---|---|---|
| Subtle ambient elevation | `rgba(0, 0, 0, 0.1) 0px 0px 10px 0px` | `--shadow-md` |

## Shape Rules

- Buttons use `100px` radius or full pill radius.
- Tags and pipeline nodes use full pill geometry.
- Feature cards use soft `40px` corners.
- Avoid sharp corners and moderate card radii below `16px`.
- Prefer borders and surface contrast over shadows.

