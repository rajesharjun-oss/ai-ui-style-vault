# Motion And Atmosphere

## Motion Timing

| Purpose | Duration | Easing |
| --- | --- | --- |
| UI hover feedback | `0.2s` to `0.4s` | ease-out |
| Overlay fade | `0.3s` to `0.5s` | ease |
| Scene transition | `0.8s` to `9s` | ease or linear |
| Sequential reveal | ticker-like cadence | ease |

## Motion Rules

- Favor opacity fades over sliding, bouncing, or scaling.
- Let scene-level movement feel gravitational and unhurried.
- Keep UI feedback quiet and quick.
- Avoid snappy app-like motion.
- Avoid large parallax that distracts from the central rendered scene.

## Atmosphere

- The UI should feel like black velvet around a rendered object.
- Depth comes from translucency, blur, and the scene behind the panel.
- Motion should feel cinematic rather than utilitarian.
- Any glow, gradient, particle, or aurora effect belongs to the 3D scene, not the UI chrome.
