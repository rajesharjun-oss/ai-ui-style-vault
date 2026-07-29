# Spacing And Shape

## Spacing

| Name | Value | Token | Notes |
| --- | ---: | --- | --- |
| 8 | 8px | `--spacing-8` | Base unit |
| 16 | 16px | `--spacing-16` | Element gap and card padding |
| 24 | 24px | `--spacing-24` | Compact section inner space |
| 32 | 32px | `--spacing-32` | Medium stack gap |
| 48 | 48px | `--spacing-48` | Section gap |
| 64 | 64px | `--spacing-64` | Hero spacing |
| 80 | 80px | `--spacing-80` | Large block spacing |
| 96 | 96px | `--spacing-96` | Major section spacing |
| 128 | 128px | `--spacing-128` | Hero or CTA band |
| 192 | 192px | `--spacing-192` | Big decorative spacing |

## Layout Values

- Page max width: 1200px.
- Section gap: 48px.
- Card padding: 16px.
- Element gap: 16px.
- Hero copy max width: 560px.

## Radius

| Element | Value | Notes |
| --- | ---: | --- |
| Nav | 6px | Compact controls |
| Buttons | 6px | Primary and secondary actions |
| Links | 6px | Active link ring treatment |
| Tags | 6px | Status and nav tags |
| Cards | 12px | Feature cards |
| Large cards | 16px | App mockups |
| Images | 24px | Rounded media |
| Feature panels | 32px | Soft cloud-paper panels |

## Shadows

Use soft, blue-tinted card shadows. Avoid generic heavy black shadows.

Suggested card shadow:

```css
rgba(15, 34, 52, 0.01) 0 27px 11px 0,
rgba(15, 34, 52, 0.03) 0 15px 9px 0,
rgba(15, 34, 52, 0.05) 0 7px 7px 0,
rgba(15, 34, 52, 0.06) 0 2px 4px 0
```

## Shape Rules

- Controls use 6px radius.
- Cards use 12px or 16px radius.
- Feature panels can be softer at 32px.
- Pixel sprites stay blocky; do not anti-alias them.

