# 3D & Immersive Web Validation Report

**Branch:** `feat/3d-immersive-web-pack`  
**Validated:** 16 August 2026  
**Pull request:** #5  
**Vault quality run:** `31960943554` — passed

## Validated inventory

- 21 structured 3D style families.
- 8 production-theme directions.
- 11 page and experience blueprints.
- 29 component contracts.
- 39 spatial interaction patterns.
- 41 capability, quality, error, fallback and XR states.
- 30 structured 3D source records.
- 34 technique records.
- 31 reference-discovery seeds.
- Four capability tiers: static, basic-mobile, balanced and high.

## Semantic relevance hard gate

The pack requires `THREE_D_RELEVANCE_CONTRACT.md` before major 3D, video or animated-background asset selection.

Validated rules:

- Primary 3D subjects, hero videos and hero animated backgrounds require relevance score **4–5**.
- Secondary decorative media requires relevance score **3+**.
- Explicitly unrelated subjects are denied before broad positive matching.
- The complete scene is checked: central object, environment, props, materials, lighting, camera/motion and fallback media.
- An attractive but unrelated asset is not accepted merely because it looks premium, cinematic or futuristic.

Regression checks passed:

- Pizza restaurant + pepperoni pizza/oven → candidate.
- Pizza restaurant + Ferrari/sports car → reject.
- Tax/accounting consultancy + sports car → reject.
- Pizza + food product inside a sports-car showroom → reject the scene because the environment is unrelated.
- Pizza + restaurant interior + pizza oven → candidate scene.

## Validation suite

The Vault quality workflow passed all of the following:

- Python tool compilation.
- Full unit-test discovery, including semantic relevance and reference-collection tests.
- JSON document parsing for Fast-Casual Commerce, Celebration & Event Microsite and 3D & Immersive Web packs.
- Fast-Casual Commerce validator.
- Celebration & Event Microsite validator.
- 3D & Immersive Web validator.
- Cross-agent/index validation.

A preceding deterministic materialization run also completed 32 unit tests successfully before the reference-pipeline tests were added.

## Refs.Gallery 3D research

Source reviewed: `https://refs.gallery/category/3d`.

The attempted public metadata collection returned **0 usable project records** because the category could not be enumerated reliably through the available public/dynamic access path without bypassing source access controls. The vault deliberately does not bypass security checkpoints.

Refs.Gallery remains registered as a collection seed for future manual or publicly accessible metadata review. No screenshots, videos, source code, models, textures, branding or exact layouts were copied.

## Reference collection safeguards

The library now includes:

- `3d/REFERENCE_COLLECTION_POLICY.md`
- `3d/reference-record.schema.json`
- `3d/references/collection-seeds.json`
- `3d/references/manual-import.example.json`
- `3d/references/refresh-plan.json`
- `scripts/normalize-3d-reference-catalog.py`

The normalizer removes common tracking parameters, canonicalises URLs, deduplicates records, constrains copied text and rejects fields containing copied source code, screenshots, embedded media, model files, texture files or archives.

## Status

The 3D pack is materialized on the feature branch, the temporary generation scaffolding has been removed from the PR diff, and the current Vault quality workflow passes. It remains unmerged until explicitly approved for merge.
