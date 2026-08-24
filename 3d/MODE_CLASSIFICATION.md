# 3D Mode Classification

This is the mandatory bridge between **“3D is justified”** and **“how do we produce/render it?”**.

It prevents a common AI-agent mistake: treating every 3D request or every available `.glb`/`.gltf` file as a freely rotatable product viewer.

## The seven modes

| Level | Mode | Meaning | Typical user control | Typical delivery |
|---:|---|---|---|---|
| 0 | `none` | Real-time 3D adds no material value | none | DOM / image / video |
| 1 | `visual-only` | 3D-looking composition with no direct object manipulation | none/passive | CSS perspective / video / Spline / authored Three.js |
| 2 | `authored-animation` | Controlled animation or camera story | play/pause/scroll/chapter | video / image sequence / model-viewer animation / Three.js |
| 3 | `inspectable-object` | User directly inspects one bounded object | drag/swipe/orbit/zoom | GLB/GLTF + model-viewer first |
| 4 | `configurable-object` | User inspects and changes verified options | bounded inspection + variants | GLB/GLTF + model-viewer for simple variants, custom runtime for complex configuration |
| 5 | `spatial-exploration` | User navigates meaningful space | guided nodes / first-person / room navigation | Three.js / R3F / Babylon / WebXR |
| 6 | `interactive-world` | Multi-object/game-like/custom simulation world | custom world interaction | Three.js / R3F / Babylon / WebGPU / WebXR |

## Core rule

> **The interaction goal determines the mode. The file format only determines whether the required asset is ready.**

Examples:

- A shoe `.glb` used only in a cinematic hero can still be `visual-only` or `authored-animation`.
- “Let users swipe/drag the mannequin 360 to see the dress from every angle” is `inspectable-object` even if the GLB has not been created yet.
- “Let users rotate the dress and switch between actual available fabrics” is `configurable-object`.
- A building `.glb` does not turn a room-to-room walkthrough into a model-viewer task; it remains `spatial-exploration`.

## Agent command

```bash
python scripts/vault-agent.py 3d-mode \
  "3D mannequin wearing the dress; users swipe or drag to rotate 360 and inspect front, sides and back" \
  --subject-class garment-textile \
  --asset-format none \
  --asset-readiness none
```

Expected mode:

```text
inspectable-object
userControl: bounded-orbit-drag-swipe-zoom
assetRequirement: approved-glb-gltf-or-equivalent-real-geometry
assetPlan.action: produce-or-source-approved-3d-asset
```

After the model is produced and a web-ready GLB exists:

```bash
python scripts/vault-agent.py 3d-runtime \
  "rotate and inspect the dress mannequin" \
  --mode inspectable-object \
  --format glb
```

The runtime selector is mode-gated: it cannot silently turn `visual-only` into a rotatable viewer, and it will escalate `spatial-exploration` / `interactive-world` instead of forcing them into `<model-viewer>`.

## Stop conditions

- If the request only says “make it 3D” and gives no interaction purpose, do not infer rotation/configuration/navigation.
- If mode 3–6 is selected but approved geometry is missing, preserve the mode and route to 3D production-resource intelligence.
- If a runtime cannot satisfy the selected mode, change the runtime — **not the mode** — unless the user/product requirement itself changes.
