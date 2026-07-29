# Spacing And Shape

## Spacing

| Purpose | Value |
|---|---:|
| Density | comfortable |
| Base unit | `4px` |
| Max width | `1200px` |
| Section gap | `80px` |
| Card padding | `20px` |
| Element gap | `8px` |

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
| 40 | `40px` | `--spacing-40` |
| 64 | `64px` | `--spacing-64` |
| 80 | `80px` | `--spacing-80` |
| 96 | `96px` | `--spacing-96` |
| 124 | `124px` | `--spacing-124` |
| 128 | `128px` | `--spacing-128` |
| 160 | `160px` | `--spacing-160` |

## Border Radius

| Element | Value | Token |
|---|---:|---|
| images | `12px` | `--radius-images` |
| inputs | `16px` | `--radius-inputs` |
| small cards | `16px` | `--radius-smallcards` |
| elevated cards | `20px` | `--radius-elevatedcards` |
| cards | `24px` | `--radius-cards` |
| buttons | `9999px` | `--radius-buttons` |

## Elevation

| Name | Value | Token |
|---|---|---|
| Dropdown / popover | `oklab(0 0 0 / 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.08) 0px 4px 24px 0px` | `--shadow-subtle` |
| Modal / overlay card | `oklab(0 0 0 / 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 8px 40px 0px` | `--shadow-subtle-2` |
| Floating product artifact | `rgba(4, 23, 43, 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px` | `--shadow-subtle-3` |

## Shape Rules

- Buttons use full pill geometry.
- Content cards use `24px` radius.
- Inputs use `16px` radius.
- Floating product artifacts use `20px` radius.
- Keep most cards flat; only floating product artifacts should show elevation.

