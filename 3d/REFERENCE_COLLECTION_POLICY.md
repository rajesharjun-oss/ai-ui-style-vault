# 3D Reference Collection Policy

## Purpose

The 3D reference library stores structured links and concise, vault-authored metadata so agents can compare visual styles, interaction patterns, implementation approaches, performance risks and fallback strategies. It is not a mirror of another website, gallery, template marketplace or asset library.

## What may be stored

- Public source and project URLs.
- Project title and a short original summary.
- Public creator/studio name, tags and date text when clearly published.
- Vault-authored style-family, interaction, performance, mobile and fallback classifications.
- Licence posture such as `reference-only`, `verify-per-example`, `verify-per-item`, `official-project-terms`, `owner-provided` or `original`.
- Retrieval date, review status and source type.

## What must not be stored without explicit rights

- Copied screenshots or preview videos.
- Website HTML, CSS, JavaScript, shaders or proprietary source code.
- Proprietary 3D models, textures, HDRIs, audio, fonts or archives.
- Full copyrighted descriptions or marketing copy.
- Credentials, private API responses or personal information.
- Base64 media, data URLs or binary payloads.

## Source classes

1. `reference-gallery` — inspiration links only.
2. `awards-gallery` — inspiration links only.
3. `official-documentation` — implementation guidance under current project terms.
4. `official-example` — technique example; verify repository/file licence.
5. `implementation-demo` — verify licence and attribution before adaptation.
6. `community-demo` — verify individual creator and project terms.
7. `template-marketplace` — purchase or platform terms may be required.
8. `asset-library` — verify each asset even when a platform commonly offers permissive licences.
9. `owner-provided` or `original` — record authorship or written permission.

## Collection workflow

1. Add the source to `3d/source-catalog.json` and `3d/references/collection-seeds.json`.
2. Collect only public links and minimal metadata, respecting source access controls, robots/rate limits and authentication boundaries.
3. Never bypass a security checkpoint or access restriction merely to populate the catalogue.
4. Put raw metadata JSON—not media—into a temporary import file.
5. Run `scripts/normalize-3d-reference-catalog.py`.
6. Review deduplication, semantic classification, live availability and current source terms.
7. Commit only normalized metadata and review notes.
8. Revalidate periodically because websites, project availability and licences can change.

## Semantic relevance requirement

Reference selection is subordinate to the 3D Semantic Relevance Contract. A reference is useful only when its underlying subject, scene logic or interaction pattern fits the target business and page purpose. Do not choose a reference merely because it looks expensive, cinematic or technically impressive.

## Originality rule

References may influence principles such as camera pacing, information hierarchy, lighting attitude, scene composition or fallback strategy. They may not be used to reproduce another project's branding, copy, models, media, proprietary code, exact composition or animation choreography.

## Removal and correction

Remove or amend a record when its source disappears, licence posture is wrong, a link redirects to unsafe material, a rights holder requests removal, or the record contains more than minimal descriptive metadata.
