# 3D & Immersive Web Validation Report

**Branch:** `feat/3d-immersive-web-pack`  
**Validated:** 16 August 2026  
**Pull request:** #5  
**Vault quality run:** `31973073055` — passed

## Validated inventory

- 21 canonical structured 3D style families.
- 8 production-theme directions.
- **30 scene archetypes × 10 art-direction treatments = 300 concrete combinable 3D design directions.**
- 11 page and experience blueprints.
- 29 component contracts.
- 39 spatial interaction patterns.
- 41 capability, quality, error, fallback and XR states.
- 30 structured 3D source records.
- 34 technique records.
- 31 reference-discovery seeds.
- Six additional publicly reviewed expansion sources, including A1 Gallery, mesh3d, ThreeJS Resources and Refs.Gallery.
- Four capability tiers: static, basic-mobile, balanced and high.

The 300-direction library is defined in `packs/3d-immersive-web/design-combination-system.json` and selected with `python scripts/select-3d-design-ideas.py "<business or product brief>"`. The selector filters scene archetypes by detected business domain before ranking art-direction treatments.

## Semantic relevance hard gate

The pack requires `THREE_D_RELEVANCE_CONTRACT.md` before major 3D, video or animated-background asset selection.

Validated rules:

- Primary 3D subjects, hero videos and hero animated backgrounds require relevance score **4–5**.
- Secondary decorative media requires relevance score **3+**.
- Explicitly unrelated subjects are denied before broad positive matching.
- The complete scene is checked: central object, environment, props, materials, lighting, camera/motion and fallback media.
- An attractive but unrelated asset is not accepted merely because it looks premium, cinematic or futuristic.
- The 300-direction selector only shortlists compatible scene/treatment directions; the actual asset still has to pass the semantic relevance contract.

Regression checks passed:

- Pizza restaurant + pepperoni pizza/oven → candidate.
- Pizza restaurant + Ferrari/sports car → reject.
- Tax/accounting consultancy + sports car → reject.
- Pizza + food product inside a sports-car showroom → reject the scene because the environment is unrelated.
- Pizza + restaurant interior + pizza oven → candidate scene.
- Pizza design-idea selection returns only `restaurant-food` compatible scene archetypes.
- Professional-services design-idea selection excludes product-turntable and AR-placement patterns.

## Validation suite

The Vault quality workflow passed all of the following:

- Python tool compilation.
- Full unit-test discovery, including semantic relevance, 300-direction selection and reference-collection tests.
- JSON document parsing for Fast-Casual Commerce, Celebration & Event Microsite and 3D & Immersive Web packs.
- Fast-Casual Commerce validator.
- Celebration & Event Microsite validator.
- 3D & Immersive Web validator.
- Cross-agent/index validation.

The 3D validator now explicitly requires:

- 30 unique scene archetypes.
- 10 unique art directions.
- Exactly 300 concrete base combinations.
- A domain mapping, purpose and fallback for every scene archetype.
- The domain-aware design selector.
- The expansion-source snapshot.

## Inspiration-source expansion

Current public discovery snapshots are recorded in `3d/references/expansion-sources-2026-08-16.json`.

The expansion review includes:

- A1 Gallery 3D.
- mesh3d all websites, WebGL-filtered websites and featured websites.
- ThreeJS Resources showcase.
- Refs.Gallery 3D tag.

Counts in that file are retrieval-time discovery snapshots, not permanent inventory promises.

## Refs.Gallery research

The original `https://refs.gallery/category/3d` automated metadata collection returned **0 usable project records** because the category could not be enumerated reliably through the available public/dynamic access path without bypassing source controls. The vault deliberately does not bypass security checkpoints.

A publicly indexed 3D tag page was later identified and is recorded as an inspiration source. This does not change the original collection count: no screenshots, videos, source code, models, textures, branding or exact layouts were copied.

## Reference collection safeguards

The library includes:

- `3d/REFERENCE_COLLECTION_POLICY.md`
- `3d/reference-record.schema.json`
- `3d/references/collection-seeds.json`
- `3d/references/manual-import.example.json`
- `3d/references/refresh-plan.json`
- `3d/references/expansion-sources-2026-08-16.json`
- `scripts/normalize-3d-reference-catalog.py`

The normalizer removes common tracking parameters, canonicalises URLs, deduplicates records, constrains copied text and rejects fields containing copied source code, screenshots, embedded media, model files, texture files or archives.

## Status

The expanded 3D pack is materialized on the feature branch and the latest Vault quality workflow passes. It remains unmerged until explicitly approved for merge.
