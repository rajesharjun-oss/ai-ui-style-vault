# 3D Delivery Runtime Intelligence

This layer answers a different question from the Blender/production-resource layer:

> **Given an approved web-ready 3D asset and an already-classified 3D interaction mode, what is the smallest sufficient browser runtime?**

The first deep runtime adapter is Google `<model-viewer>`. It is deliberately placed before custom Three.js / React Three Fiber / Babylon.js in the escalation path for bounded single-model interactions.

## Mandatory input: 3D mode

Do **not** call this layer before `3d/mode-classification.json` has classified the user requirement.

The runtime does not decide whether a model should be rotatable. That has already been decided by the interaction mode:

- `visual-only` → no free rotation; choose a simpler visual path.
- `authored-animation` → controlled animation only; model-viewer animation is one possible implementation.
- `inspectable-object` → bounded drag/swipe/orbit/zoom; model-viewer is preferred when sufficient.
- `configurable-object` → bounded inspection plus verified variants; model-viewer can handle simple material variants.
- `spatial-exploration` / `interactive-world` → escalate to custom spatial/world runtime.

A `.glb` or `.gltf` file never upgrades the mode by itself.

## Pipeline position

```text
business/domain research
→ immersive architecture when justified
→ 3D relevance + interaction intent
→ 3D mode classification (mandatory)
→ 3D design direction
→ 3D production resources / asset preparation when needed
→ 3D delivery runtime selection  ← here
→ performance/fallback QA
→ visual QA / Design Critic
```

## Google `<model-viewer>` adapter

The adapter is pinned in `source-policy.json` and exposes five Vault-authored delivery profiles:

- `model-viewer-basic-inspector`
- `model-viewer-annotated-inspector`
- `model-viewer-variant-configurator-lite`
- `model-viewer-animated-product`
- `model-viewer-ar-placement`

These profiles capture transferable capability contracts, not Google demo branding or shared demo assets.

## Commands

First classify:

```bash
python scripts/vault-agent.py 3d-mode \
  "users swipe or drag the mannequin 360 to inspect the dress" \
  --subject-class garment-textile \
  --asset-format glb \
  --asset-readiness strong
```

Then pass the selected mode to delivery selection:

```bash
python scripts/vault-agent.py 3d-runtime \
  "rotate and inspect the verified dress mannequin" \
  --mode inspectable-object \
  --format glb
```

Generate an implementation skill:

```bash
python scripts/vault-agent.py 3d-runtime-skill model-viewer-basic-inspector --output SKILL.md
```

Direct engine commands:

```bash
python scripts/3d-delivery-runtimes.py validate
python scripts/3d-delivery-runtimes.py list
python scripts/3d-delivery-runtimes.py select "AR placement of a verified chair" --mode inspectable-object --format glb --ar
python scripts/3d-delivery-runtimes.py skill model-viewer-ar-placement
```

## Enforcement

The delivery selector now enforces the mode gate:

- `none` / `visual-only` returns `decision: none` rather than inventing a rotatable viewer.
- `inspectable-object` only considers inspector/annotation/AR-compatible profiles.
- `configurable-object` only considers compatible configuration/AR profiles.
- `authored-animation` only considers the animated-product profile.
- `spatial-exploration` / `interactive-world` returns `decision: escalate` to a custom runtime.
- modes that need a browser 3D asset are blocked until an approved GLB/glTF is declared.

If the selected runtime cannot satisfy the mode, change the runtime — not the interaction mode — unless the user/product requirement changes.

## Hard requirements

- Essential content/actions stay semantic DOM.
- 3D mode is classified before this layer.
- GLB/glTF availability never determines the interaction mode.
- GLB/glTF source, dimensions, variants, annotations and claims must be verified.
- Use a poster/static fallback and intentional mobile behavior.
- AR is enhancement-only and needs explicit unsupported/tracking-failure states.
- Keep `@google/model-viewer` and its tested Three.js peer version pinned together unless compatibility is deliberately revalidated.
- Verify every copied model, environment map or demo asset separately; the Apache-2.0 software licence does not automatically clear unrelated third-party assets.
- Measure the actual page in target browsers/devices before handoff.
