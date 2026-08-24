# 3D Production Resource Intelligence

This layer answers a different question from the Vault's 3D design system:

> **Once a 3D/immersive experience is justified, what production capability or external resource category can help us create the required geometry, materials, animation, scans, terrain, audio or export pipeline?**

It does **not** decide whether a website should use 3D. That decision remains with business research, immersive-template selection and the 3D interaction/relevance gates.

## Why it exists

The Vault already knows how to select immersive architecture, 3D scene direction, interactions, effects, performance tiers and fallbacks. Production still needs practical ways to create or source the underlying assets. This layer turns the public Awesome Blender directory into a rights-conscious production taxonomy and a compact selector.

Initial categories include terrain, procedural nature, architecture, photogrammetry, LiDAR/point clouds, materials, lighting/HDRI, simulation, characters, mocap/animation, GIS/maps, web export, asset libraries, rendering, data visualization, audio, format conversion and Blender scripting.

## Source boundary

`source-policy.json` pins `agmmnn/awesome-blender` at commit `beb0028ba436de00da336e1fd08098c1da1376df`.

The Awesome Blender list itself is CC0. **Its linked add-ons, tools, models, textures, HDRIs, services, datasets and downloads do not inherit CC0.** Every selected candidate therefore remains `verify-upstream` until its own current licence/terms, compatibility and asset rights are checked.

The Vault does not mirror third-party tools or asset libraries by default.

## Agent workflow

After a 3D subject/interaction plan identifies a production need, run:

```bash
python scripts/vault-agent.py 3d-resource "photogrammetry for an approved resort exterior"
```

Optional domain context can improve ranking:

```bash
python scripts/vault-agent.py 3d-resource "terrain and vegetation for a verified property site" --domain real-estate
```

Then generate the production skill for the selected category:

```bash
python scripts/vault-agent.py 3d-resource-skill photogrammetry-reconstruction --output SKILL.md
```

The generated skill gives the agent:

- when the category is appropriate;
- expected production outputs;
- a recommended production sequence;
- representative external candidates;
- web-delivery/fallback considerations;
- explicit rights and provenance checks;
- reject/avoid conditions.

After the GLB/glTF or other web-ready derivative exists, hand off to `3d-delivery-runtimes/` rather than assuming a custom renderer is required:

```bash
python scripts/vault-agent.py 3d-runtime "rotate and inspect the verified product" --format glb
```

The delivery layer may choose a bounded Google `<model-viewer>` profile, return `none` for a simpler media path, or escalate when a custom 3D runtime is genuinely required.

## Example pipeline

```text
verified business / project need
        ↓
immersive architecture (optional)
        ↓
3D subject + interaction plan
        ↓
scene/design recipe
        ↓
asset-production needs identified
        ↓
3D Production Resource selector
        ↓
category skill + candidate due diligence
        ↓
Blender/source production
        ↓
retopo / bake / optimize / export
        ↓
3D Delivery Runtime selector
        ↓
<model-viewer> / simpler media / custom runtime escalation
        ↓
performance + visual QA
```

## Hard rules

- A resource candidate is a **discovery lead**, not an approved dependency or asset.
- Verify the selected resource's own current licence/terms before use.
- Verify commercial use, modification, redistribution and embedding rights separately.
- Models, textures, HDRIs, audio, scans and datasets require their own provenance records.
- Use authoritative CAD/BIM/GIS/scan/source data when representing a real product, property, place or facility accurately.
- Generated/procedural content must not masquerade as a verified digital twin.
- Prefer offline production and baking when browser-side simulation is unnecessary.
- Optimize every 3D deliverable for the target runtime; raw Blender production scenes are not web assets.
- Maintain mobile, reduced-motion and non-WebGL fallbacks from the existing 3D/immersive contracts.
