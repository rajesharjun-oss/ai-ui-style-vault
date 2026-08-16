# 3D & Immersive Web Pack

This capability pack helps AI agents create original 3D, WebGL, WebGPU, spatial, product-configurator, digital-twin, map, AR and WebXR experiences without sacrificing content, accessibility, performance or the primary product task.

It can be combined with a product-domain pack. The domain pack defines what the product must accomplish; this pack defines when and how spatial technology is selected, implemented, measured and degraded safely.

## Required medium decision

```text
semantic DOM + CSS
→ CSS perspective
→ image sequence or video
→ Rive
→ Spline/embed
→ <model-viewer>
→ custom Three.js / React Three Fiber / Babylon.js
→ WebXR
```

Escalate only when the preceding option cannot deliver the required interaction, accuracy or storytelling.

## Required contracts

- `THREE_D_BUILD_CONTRACT.md`
- `SCENE_ASSET_PLAN.md`
- `PERFORMANCE_AND_FALLBACK_PLAN.md`
- Core project contracts and any selected product-domain contract

## Non-negotiable rules

- Essential content and controls remain semantic DOM.
- A complete static/2D fallback is designed first.
- Heavy assets load only after capability and intent checks.
- Every model, texture, HDRI, animation, shader and code example has provenance and licence records.
- Reference sites are inspiration only.
- Mobile receives an intentional lower tier.
- Reduced motion, unsupported devices, low power, errors and context loss are complete states.
- Real-time scenes are measured against `performance-budgets.json`.

The Refs.Gallery metadata catalogue currently records 0 unique public project links discovered during the recorded collection. It stores no copied project media or code.
