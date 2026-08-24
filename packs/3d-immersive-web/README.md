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

## 3D production-resource layer

Once the subject, interaction and scene direction are approved, use `3d-production-resources/` only for the **concrete production needs** that remain: terrain, vegetation, buildings, photogrammetry, LiDAR, materials, lighting, simulation, characters, mocap, GIS, glTF/web export, rendering, audio, data visualization or Blender automation.

```text
python scripts/vault-agent.py 3d-resource "<concrete production need>" --domain <domain-pack>
python scripts/vault-agent.py 3d-resource-skill <category-id> --output SKILL.md
```

This layer does not justify 3D and does not auto-install tools. It turns a pinned Awesome Blender research source into a compact production taxonomy. The list itself is CC0, but each linked tool/add-on/asset/service/dataset retains its own independent licence/terms and must be verified before production use.

Raw Blender production scenes are never treated as web deliverables. Retopology/decimation, texture baking/compression, animation reduction, export validation and browser-performance QA remain part of the delivery path.

## Required contracts

- `THREE_D_RELEVANCE_CONTRACT.md`
- `THREE_D_BUILD_CONTRACT.md`
- `SCENE_ASSET_PLAN.md`
- `PERFORMANCE_AND_FALLBACK_PLAN.md`
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
- External production-resource candidates require their own current licence/terms, compatibility and security checks; a curated-list licence never flows through to linked resources.
- Reference sites are inspiration only.
- Mobile receives an intentional lower tier.
- Reduced motion, unsupported devices, low power, errors and context loss are complete states.
- Real-time scenes are measured against `performance-budgets.json`.
- Generated or licensed media must match the verified business context; visual impressiveness alone never justifies an asset.

## Inspiration library

The source library covers reference galleries, official examples, community demos and asset libraries. `3d/references/expansion-sources-2026-08-16.json` records the latest expansion review, including A1 Gallery, mesh3d, ThreeJS Resources and the publicly indexed Refs.Gallery 3D tag.

The original automated Refs.Gallery category collection still records 0 safely enumerated project records. The vault does not bypass source access controls and does not copy project screenshots, videos, source code, models, textures, branding, marketing copy or exact layouts.

Use `3d/REFERENCE_COLLECTION_POLICY.md` and verify current per-item rights before production reuse.
