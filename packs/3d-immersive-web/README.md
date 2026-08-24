# 3D & Immersive Web Pack

This capability pack helps AI agents create original 3D, WebGL, WebGPU, spatial, product-configurator, digital-twin, map, AR and WebXR experiences without sacrificing content, accessibility, performance or the primary product task.

It can be combined with a product-domain pack. The domain pack defines what the product must accomplish; this pack defines when and how spatial technology is selected, implemented, measured and degraded safely.

## Design-library depth

The pack now has two complementary layers:

1. **Canonical architecture:** 21 style families, 8 production themes, 11 experience blueprints, 29 component contracts and 39 interaction patterns.
2. **Concrete design-direction matrix:** 30 scene archetypes × 10 art-direction treatments = **300 combinable 3D design directions**.

Inspect `design-combination-system.json` or run:

```text
python scripts/select-3d-design-ideas.py "<business, product and page brief>"
```

The selector filters scene archetypes by detected business domain before ranking treatments. A shortlisted direction is not automatic approval: the actual model, environment, props, materials, lighting, motion, video and fallback media must still pass `THREE_D_RELEVANCE_CONTRACT.md`.

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

## Mandatory 3D mode classification

After 3D is justified, classify **what kind of 3D interaction the user actually needs** before searching for assets or choosing a runtime:

```text
0 — none
1 — visual-only
2 — authored-animation
3 — inspectable-object
4 — configurable-object
5 — spatial-exploration
6 — interactive-world
```

Run:

```text
python scripts/vault-agent.py 3d-mode "<explicit 3D user goal>" --subject-class <class> --asset-format <glb|gltf|other|none> --asset-readiness <strong|adequate|limited|none>
```

This classification is driven by the user goal, not by the file type. A `.glb`/`.gltf` file does **not** automatically imply free rotation. A GLB can remain visual-only or authored-animation. Conversely, a request such as “let customers swipe/drag a mannequin 360 to inspect the dress” remains `inspectable-object` even when the model does not exist yet; production must create/source the required geometry without changing the mode.

Mode routing:

- `visual-only` → choose the lowest-cost 3D-looking visual medium; no free rotation is implied.
- `authored-animation` → video/image sequence/model-viewer animation/custom runtime according to fidelity; user observes or scroll-scrubs authored motion.
- `inspectable-object` → real geometry plus bounded drag/swipe/orbit/zoom; `<model-viewer>` is preferred when one bounded object is sufficient.
- `configurable-object` → real geometry plus verified variants/materials/components; `<model-viewer>` may handle simple material variants, otherwise use a custom runtime.
- `spatial-exploration` → guided or bounded navigation through meaningful space; use custom Three.js/R3F/Babylon/WebXR when justified.
- `interactive-world` → multi-object/game-like/custom physics/data/world interaction; use a custom runtime.

Do not continue to production/runtime selection when the mode is unclear. The mode is a stable product requirement and must not be silently changed merely because a particular asset or library is convenient.

## 3D production-resource layer

Once the subject, interaction, **3D mode** and scene direction are approved, use `3d-production-resources/` only for the concrete production needs that remain: terrain, vegetation, buildings, photogrammetry, LiDAR, materials, lighting, simulation, characters, mocap, GIS, glTF/web export, rendering, audio, data visualization or Blender automation.

```text
python scripts/vault-agent.py 3d-resource "<concrete production need>" --domain <domain-pack>
python scripts/vault-agent.py 3d-resource-skill <category-id> --output SKILL.md
```

This layer does not justify 3D and does not change the selected mode. It turns a pinned Awesome Blender research source into a compact production taxonomy. The list itself is CC0, but each linked tool/add-on/asset/service/dataset retains its own independent licence/terms and must be verified before production use.

Raw Blender production scenes are never treated as web deliverables. Retopology/decimation, texture baking/compression, animation reduction, export validation and browser-performance QA remain part of the delivery path.

## 3D delivery-runtime layer

After the mandatory 3D mode is selected and a web-ready asset exists, use `3d-delivery-runtimes/` to choose the smallest sufficient browser runtime instead of defaulting immediately to custom Three.js.

The first deep adapter is Google `<model-viewer>` and covers five bounded delivery profiles: basic inspection, semantic hotspots/dimensions, lightweight material variants, glTF animation playback and AR placement.

```text
python scripts/vault-agent.py 3d-runtime "rotate and inspect the verified product" --mode inspectable-object --format glb
python scripts/vault-agent.py 3d-runtime-skill model-viewer-basic-inspector --output SKILL.md
```

The runtime selector **must consume the classified mode**. `visual-only` will not become rotatable because a GLB exists. `inspectable-object` and `configurable-object` may route to `<model-viewer>` when bounded. `spatial-exploration` and `interactive-world` escalate to custom Three.js / React Three Fiber / Babylon.js instead of being forced into a single-object viewer.

The runtime adapter pins the reviewed `@google/model-viewer` package and its tested Three.js peer relationship. Demo/shared models and environment assets remain separate provenance items and are not automatically cleared by the Apache-2.0 software licence.

## Required contracts

- `THREE_D_RELEVANCE_CONTRACT.md`
- `THREE_D_BUILD_CONTRACT.md`
- `SCENE_ASSET_PLAN.md`
- `PERFORMANCE_AND_FALLBACK_PLAN.md`
- `3d/mode-classification.json`
- Core project contracts and any selected product-domain contract

## Semantic relevance is a hard gate

Every major 3D object, video, animated background, environment or spatial effect must directly support the actual business, product, service, process, place, verified data, audience or page purpose.

Examples:

- Pizza site → pizza, dough, ingredients, ovens, packaging and food-service environments.
- Fashion → actual garments, fabrics, accessories and product inspection.
- Property → verified buildings, floor plans, interiors, materials or neighbourhood context.
- Professional services → verified process, system or data visualisation, or restrained domain-specific abstraction.
- Celebration → verified rings, flowers, fabric, monograms and venue or ceremonial motifs.
- Automotive → verified vehicles, components, showrooms or engineering context.

A Ferrari on a pizza website is rejected. A relevant pizza model inside an unrelated sports-car showroom is also rejected because the whole scene must make sense.

Relevance thresholds:

- Primary visual: score 4–5.
- Secondary decoration: at least 3.
- Score below 3: reject.
- Explicit forbidden-domain subject: reject before positive matching.

## Non-negotiable rules

- Essential content and controls remain semantic DOM.
- A complete static/2D fallback is designed first.
- Heavy assets load only after capability and intent checks.
- Every model, texture, HDRI, animation, shader and code example has provenance and licence records.
- Classify the 3D mode before production or runtime selection; asset format never determines interaction mode.
- External production-resource candidates require their own current licence/terms, compatibility and security checks; a curated-list licence never flows through to linked resources.
- 3D delivery runtimes require a selected mode plus real GLB/glTF, browser and device validation; a successful local render is not enough.
- Reference sites are inspiration only.
- Mobile receives an intentional lower tier.
- Reduced motion, unsupported devices, low power, errors and context loss are complete states.
- Real-time scenes are measured against `performance-budgets.json`.
- Generated or licensed media must match the verified business context; visual impressiveness alone never justifies an asset.

## Inspiration library

The source library covers reference galleries, official examples, community demos and asset libraries. `3d/references/expansion-sources-2026-08-16.json` records the latest expansion review, including A1 Gallery, mesh3d, ThreeJS Resources and the publicly indexed Refs.Gallery 3D tag.

The original automated Refs.Gallery category collection still records 0 safely enumerated project records. The vault does not bypass source access controls and does not copy project screenshots, videos, source code, models, textures, branding, marketing copy or exact layouts.

Use `3d/REFERENCE_COLLECTION_POLICY.md` and verify current per-item rights before production reuse.
