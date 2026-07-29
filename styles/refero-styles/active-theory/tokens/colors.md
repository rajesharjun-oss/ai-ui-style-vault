# Color Tokens

## Brand

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Dusk Violet | `#343755` | `--color-dusk-violet` | Primary action fill and the only chromatic UI accent. |

## Neutrals

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Void Black | `#000000` | `--color-void-black` | Page canvas, immersive background, dark stacked surfaces. |
| Ghost White | `#ffffff` | `--color-ghost-white` | Primary text, icon strokes, high-contrast labels. |
| Ash Border | `#4d4d4d` | `--color-ash-border` | Card borders, divider hairlines, low-weight separators. |
| Smoke | `#808080` | `--color-smoke` | Muted borders on ghost buttons and secondary chrome. |
| Fog | `#999999` | `--color-fog` | Medium-contrast outlines and structural separators. |
| Pale Mist | `#c6c6c6` | `--color-pale-mist` | Tertiary text, default links, low-priority metadata. |

## Alpha Surfaces

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Translucent Overlay | `rgba(0,0,0,0.5)` | `--surface-translucent-overlay` | Cookie banners, modal scrims, tooltip panels. |
| Frosted Glass | `rgba(255,255,255,0.1)` | `--surface-frosted-glass` | Ghost button fill, hover wash, subtle glass surface. |
| Ghost Border | `rgba(255,255,255,0.6)` | `--border-ghost` | Ghost nav button outlines. |

## Rules

- Use `#000000` as the only canvas color.
- Use Dusk Violet only for singular dominant CTAs.
- Do not introduce additional chromatic accents.
- Do not use solid white or solid gray card surfaces.
- Let the WebGL scene carry gradient richness and color drama.
