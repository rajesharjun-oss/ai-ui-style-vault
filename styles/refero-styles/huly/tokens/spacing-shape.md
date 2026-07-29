# Spacing And Shape

## Spacing

| Purpose | Value |
|---|---:|
| Density | comfortable |
| Base unit | `4px` |
| Max width | `1200px` |
| Section gap | `96px` |
| Card padding | `24px` |
| Element gap | `12px` |

## Spacing Scale

| Name | Value | Token |
|---|---:|---|
| 4 | `4px` | `--spacing-4` |
| 8 | `8px` | `--spacing-8` |
| 12 | `12px` | `--spacing-12` |
| 16 | `16px` | `--spacing-16` |
| 20 | `20px` | `--spacing-20` |
| 24 | `24px` | `--spacing-24` |
| 28 | `28px` | `--spacing-28` |
| 32 | `32px` | `--spacing-32` |
| 36 | `36px` | `--spacing-36` |
| 40 | `40px` | `--spacing-40` |
| 64 | `64px` | `--spacing-64` |
| 160 | `160px` | `--spacing-160` |
| 180 | `180px` | `--spacing-180` |
| 240 | `240px` | `--spacing-240` |

## Border Radius

| Element | Value | Token |
|---|---:|---|
| inputs | `4px` | `--radius-inputs` |
| cards | `12px` | `--radius-cards` |
| panels | `30px` | `--radius-panels` |
| tags | `9999px` | `--radius-tags` |
| buttons | `9999px` | `--radius-buttons` |

## Shadows

| Name | Value | Token |
|---|---|---|
| Product screenshot card | `rgba(0, 0, 0, 0.5) 0px 6px 25px 0px` | `--shadow-xl` |
| Floating panel | `rgba(0, 0, 0, 0.35) 0px 4px 16px 0px` | `--shadow-md` |
| Subtle elevation | `rgba(0, 0, 0, 0.15) 0px 4px 6px 0px` | `--shadow-sm` |
| Focus ring | `rgba(255, 255, 255, 0.4) 0px 0px 0px 6px` | `--shadow-subtle` |

## Shape Rules

- Buttons, tags, chips, and segmented controls should use full pill geometry.
- Cards should use `12px` radius.
- Larger panels can use `30px` radius.
- Inputs stay tighter at `4px`.
- Avoid sharp-corner controls; the style language is round and pill-forward.

