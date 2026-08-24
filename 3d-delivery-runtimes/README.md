# 3D Delivery Runtime Intelligence

This layer answers a different question from the Blender/production-resource layer:

> **Given an approved web-ready 3D asset and a verified interaction goal, what is the smallest sufficient browser runtime?**

The first deep runtime adapter is Google `<model-viewer>`. It is deliberately placed before custom Three.js / React Three Fiber / Babylon.js in the escalation path for bounded single-model and small-model interactions.

## Pipeline position

```text
business/domain research
→ immersive architecture when justified
→ 3D interaction intent when justified
→ 3D design direction
→ 3D production resources / asset preparation
→ 3D delivery runtime selection  ← here
→ performance/fallback QA
→ visual QA / Design Critic
```

Resource discovery and runtime selection do not justify 3D. If a still image, video or normal DOM composition solves the problem, use that instead.

## Google `<model-viewer>` adapter

The adapter is pinned in `source-policy.json` and exposes five Vault-authored delivery profiles:

- `model-viewer-basic-inspector`
- `model-viewer-annotated-inspector`
- `model-viewer-variant-configurator-lite`
- `model-viewer-animated-product`
- `model-viewer-ar-placement`

These profiles capture transferable capability contracts, not Google demo branding or shared demo assets.

## Commands

Select a delivery profile:

```bash
python scripts/vault-agent.py 3d-runtime "rotate and inspect the verified product" --format glb
```

Generate an implementation skill:

```bash
python scripts/vault-agent.py 3d-runtime-skill model-viewer-basic-inspector --output SKILL.md
```

Direct engine commands:

```bash
python scripts/3d-delivery-runtimes.py validate
python scripts/3d-delivery-runtimes.py list
python scripts/3d-delivery-runtimes.py select "AR placement of a verified chair" --format glb
python scripts/3d-delivery-runtimes.py skill model-viewer-ar-placement
```

## Escalation rule

Use `<model-viewer>` when the product task is bounded: inspect a model, show verified hotspots/dimensions, play glTF clips, switch real material variants, or place the model in AR.

Escalate to custom Three.js / React Three Fiber / Babylon.js only when the experience genuinely needs a navigable multi-object world, bespoke camera choreography, custom physics, complex object-object interaction, large spatial datasets, or a deeply custom render pipeline.

## Hard requirements

- Essential content/actions stay semantic DOM.
- GLB/glTF source, dimensions, variants, annotations and claims must be verified.
- Use a poster/static fallback and intentional mobile behavior.
- AR is enhancement-only and needs explicit unsupported/tracking-failure states.
- Keep `@google/model-viewer` and its tested Three.js peer version pinned together unless compatibility is deliberately revalidated.
- Verify every copied model, environment map or demo asset separately; the Apache-2.0 software licence does not automatically clear unrelated third-party assets.
- Measure the actual page in target browsers/devices before handoff.
