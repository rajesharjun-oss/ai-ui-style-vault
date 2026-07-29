# Harness.io

Source: Refero Styles  
URL: https://styles.refero.design/style/6f3652cf-583f-411d-a117-3a03f6342917  
Reference site: https://gitness.com  
Captured: 2026-07-28

Harness.io is a midnight mission-control style: near-black surfaces, stacked dark cards, light hairline borders, wide-tracked Calsans headlines, Geist product UI, pill controls, and a phosphor mint highlight used like a monitor glow. It should feel like a high-contrast DevOps command deck.

Use this folder as an AI implementation brief. The most useful files are:

- `DESIGN.md` for the full style interpretation.
- `implementation-prompt.md` for a copy-ready prompt to hand to an AI builder.
- `style.json` for structured metadata.
- `code/css-variables.css` for CSS custom properties and component recipes.
- `code/tailwind-v4.css` for Tailwind v4 theme tokens.
- `code/design-tokens.json` for machine-readable tokens.

Core cues:

- Canvas: `#070707` Void Canvas.
- Main card surface: `#0d0e12` Carbon Plate.
- Nested surface: `#141418` Obsidian.
- Hover/divider surface: `#2e3038` Iron Edge.
- Primary text/action fill: `#ffffff` Pure White.
- Secondary text: `#c8cad0` Ash and `#aeaeb7` Graphite.
- Card borders: `#d9dae5` Fog, intentionally light on dark.
- Mint accent: `#70dcd3` Phosphor Mint, one featured panel per viewport.
- Blue action stroke: `#0092e4` Signal Blue for active links and focus accents.
- Display font: Calsans, positive tracking `0.056em`.
- UI font: Geist for body, nav, buttons, badges, forms, and activity feeds.
- Shape: 20px cards, 16px nested cards, 5px inputs, 800px pill controls.
- Depth: no card shadows; use surface steps and light borders.

This is best for DevOps platforms, Git hosting, CI/CD dashboards, developer infrastructure, security tooling, observability tools, and dark admin consoles.
