# Colors

## Palette

| Name | Value | Token | Role |
|---|---:|---|---|
| Carbon Vellum | `#fcfcfc` | `--color-carbon-vellum` | Primary text, inverse button text, icon strokes, and paper-like contrast against the void |
| Obsidian | `#0a0a13` | `--color-obsidian` | Primary page canvas and dominant background with blue undertone |
| Pitch | `#000000` | `--color-pitch` | Dark supporting neutral for text, icons, and strong contrast. Do not use as the full-page background alone |
| Void | `#040407` | `--color-void` | Secondary canvas layer and top nav background |
| Graphite | `#08080c` | `--color-graphite` | Card surface for elevated product mockups |
| Smoke | `#757580` | `--color-smoke` | Secondary body text and metadata |
| Ash | `#a3a3b3` | `--color-ash` | Tertiary text, card descriptions, inactive nav, muted foreground |
| Charcoal | `#2a2a32` | `--color-charcoal` | Hairline divider and subtle card border |
| Iris Glow | `#6199f6` | `--color-iris-glow` | Sole chromatic accent for icons, eyebrow labels, links, active states, and feature marks |
| Twilight | `#4f4f80` | `--color-twilight` | Muted violet for product-frame borders, glow halos, and atmospheric tints |
| Specter Lilac | `#dedfee` | `--color-specter-lilac` | Soft highlight on violet accents and light-mode card edges |

## Gradients

```css
--gradient-hero: linear-gradient(195deg, #0a0010 0%, #02000a 48%, #0c1d32 100%);
--gradient-radial-glow: radial-gradient(circle at 50% 100%, rgba(0, 11, 53, 0.7), rgba(10, 10, 19, 0) 60%);
--gradient-section: radial-gradient(circle at 0% 0%, #0e0f20 0%, #0c0c19 48%, #000000 100%);
```

## Rules

- Iris Glow is the only chromatic accent.
- Twilight is for borders and halo atmospherics only.
- Do not use flat black as the full page canvas.
- Keep all secondary information in Smoke or Ash.

