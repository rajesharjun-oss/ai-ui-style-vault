# Active Theory Design Notes

Active Theory is a black-void immersive system. The rendered WebGL environment is the hero, and the UI chrome exists only as a minimal control layer. Every visual decision is designed to disappear behind the experience: translucent panels, hairline borders, low-density text, and one carefully rationed violet CTA.

## Visual Principles

- The canvas must stay absolute black.
- The 3D scene owns color, depth, and spectacle.
- UI surfaces are translucent or outlined, never solid white or gray.
- Elevation comes from stacking, opacity, and backdrop blur, not shadows.
- The violet accent is rare and reserved for one dominant action.
- Type contrast matters: geometric sans for chrome, Times serif for prose.

## Color System

The palette is black, white, grays, and one violet. Dusk Violet `#343755` is the only chromatic UI color. Ghost White `#ffffff` handles primary text and icons. Ash Border `#4d4d4d`, Smoke `#808080`, Fog `#999999`, and Pale Mist `#c6c6c6` create low-key hierarchy over the void.

## Typography

Use nbarchitekt or a close geometric sans for nav, buttons, metadata, and micro-labels. Keep it tiny: 10px to 14px. Use Times or a system serif for body copy so prose feels editorial rather than like UI.

## Layout

Use a full-viewport immersive canvas without a visible max-width container. Pin ghost navigation to the top-right. Let the central WebGL scene hold the page. Conventional content sections should appear as translucent overlays rather than replacing the canvas.

## Elevation

Do not use box shadows. Use rgba surfaces with `backdrop-filter: blur(4px)`. Depth should feel like glass hovering in space, not like paper casting a shadow.
