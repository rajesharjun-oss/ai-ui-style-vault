# 3D Reference and Technique Library

This directory supports `packs/3d-immersive-web/` with structured styles, sources, reference metadata, techniques, semantic domain rules and design-direction selection.

## Design depth

The capability pack includes:

- 21 canonical style families.
- 8 production themes.
- 30 domain-aware scene archetypes.
- 10 art-direction treatments.
- **300 concrete scene × treatment design directions.**
- 39 interaction patterns.
- 34 implementation techniques.

Use:

```text
python scripts/select-3d-design-ideas.py "<business, product and page brief>"
```

to shortlist domain-compatible design directions. Then complete `THREE_D_RELEVANCE_CONTRACT.md` for the actual 3D object, environment, props, lighting, motion, video/background and fallback assets. The selector cannot override the semantic relevance gate.

Use:

```text
python scripts/select-3d-references.py "<brief>"
```

to shortlist reference metadata.

## Reference sources

`references/expansion-sources-2026-08-16.json` records the current expansion review, including A1 Gallery, mesh3d, ThreeJS Resources and the publicly indexed Refs.Gallery 3D tag.

The original Refs.Gallery automated category collection contains 0 safely enumerated project records. The library does not bypass access controls and stores no copied screenshots, source code, models, textures or proprietary media.

A reference is not a reuse licence. Follow `REFERENCE_COLLECTION_POLICY.md` and verify current per-item rights before production use.
