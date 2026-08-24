# AI UI Style Vault — Start Here

This is the shortest supported entry point for an AI coding/design agent.

The vault is large by design, but an agent should **not read the entire repository** before every build. Use progressive disclosure: understand the task, ingest/research the business when needed, model evidence-backed content/admin entities, run the router/orchestrator, resolve components, select an immersive architecture when the brief calls for one, select any justified interactive effects/3D, **classify the exact 3D interaction mode**, identify concrete 3D production needs, choose the smallest sufficient browser delivery runtime, then read only the files selected for that task.

## 60-second workflow

1. Inspect the target project and user brief.
2. When the user supplies a business URL, Maps link, directory listing, social profile or other source, start with source ingestion:

```bash
python scripts/vault-agent.py ingest "<business-source-url>"
```

Raw URL mode creates `business-source-request.json`. The AI research layer should inspect the source with available web/browser/connectors, use the single source-specific playbook selected by the request, create a report conforming to `research/business-source-report.schema.json`, then run:

```bash
python scripts/vault-agent.py ingest BUSINESS_SOURCE_REPORT.json --output-dir business-ingestion
```

This produces a strict source-of-truth bundle: `CONTENT_SOURCE_OF_TRUTH.json`, `ASSET_MANIFEST.json`, `BUSINESS_RESEARCH.md`, `business-profile.json`, `BUILD_PROMPT.md` and `ingestion-summary.json`.

3. Convert that evidence into public-content and optional admin/CMS models:

```bash
python scripts/vault-agent.py model business-ingestion
```

This produces `BUSINESS_ENTITY_MODEL.json`, `PUBLIC_CONTENT_MODEL.json`, `ADMIN_CMS_MODEL.json`, `CMS_BUILD_CONTRACT.md` and `content-model-summary.json`. Only evidenced entities become records/modules. Missing evidence must not create placeholder orders, revenue, inventory, bookings, customers, system-health or security-log data.

4. If there is no source URL, create/validate `business-profile.json` from available verified evidence before visual design. If an admin/CMS is requested, still create an evidence-backed content model before designing the admin.
5. Run the master planner:

```bash
python scripts/vault-build-orchestrator.py business-profile.json --output vault-build-plan.json
```

6. Read `vault-build-plan.json`, `PUBLIC_CONTENT_MODEL.json` when present, `ADMIN_CMS_MODEL.json` when admin is requested, and only the domain/capability/contract files required by the plan.
7. Resolve difficult UI components through the component intelligence layer:

```bash
python scripts/resolve-component-contract.py "<component need>"
```

8. If the user explicitly wants an immersive/experiential website, select the **experience architecture before the visual effect**:

```bash
python scripts/vault-agent.py immersive business-profile.json --goal "<actual user goal>"
```

The selector may return `none`; that is a successful result when immersion would add spectacle without enough user/business value.

9. When an immersive template is selected, generate the implementation skill:

```bash
python scripts/vault-agent.py immersive-skill <template-id> --output SKILL.md
```

The skill defines the experience state model, runtime level, mobile transformation, non-immersive fallback, source/reuse boundary, recommended effects and relevant 3D blueprint. It does **not** automatically authorize 3D or copying the research source.

10. Build the semantic/static experience first. If an interactive enhancement may materially improve a section, run:

```bash
python scripts/vault-agent.py effect business-profile.json --section hero
```

`decision: none` is a successful result. Do not add an effect merely because one exists.

11. When an effect is selected, generate its implementation skill:

```bash
python scripts/vault-agent.py effect-skill <effect-id> --output SKILL.md
```

Use the lowest-complexity compatible runtime, preserve mobile/reduced-motion behavior and route to the 3D capability system only when the subject becomes explorable, configurable or spatially informative.

12. When 3D is justified, select the interaction plan before searching for assets/tools:

```bash
python scripts/select-3d-interaction-plan.py business-profile.json --subject-class <class> --goal "<goal>"
```

The selected 3D plan defines what the user must be able to inspect, configure, navigate or understand. Resource availability must never be used as the reason to add 3D.

13. **Classify the 3D mode before production or runtime selection.** This is mandatory:

```bash
python scripts/vault-agent.py 3d-mode \
  "<explicit 3D interaction goal>" \
  --subject-class <class> \
  --asset-format <glb|gltf|other|none> \
  --asset-readiness <strong|adequate|limited|none>
```

The seven modes are:

```text
0 none
1 visual-only
2 authored-animation
3 inspectable-object
4 configurable-object
5 spatial-exploration
6 interactive-world
```

The **interaction goal determines the mode**. The asset format only tells us whether the required asset already exists. A GLB/GLTF file never automatically means users should be able to rotate it. Conversely, “let customers swipe/drag a mannequin 360 to inspect the dress” is `inspectable-object` even if no GLB has been produced yet.

14. If the selected mode requires geometry/assets that do not yet exist — terrain, vegetation, architecture, photogrammetry, LiDAR, materials, lighting, simulation, characters, mocap, GIS, web export, rendering, audio, data visualization or Blender automation — select the production category:

```bash
python scripts/vault-agent.py 3d-resource "<concrete production need>" --domain <selected-domain-pack>
python scripts/vault-agent.py 3d-resource-skill <category-id> --output SKILL.md
```

Production must satisfy the selected mode; it must not silently change the mode because a particular tool or asset is easier. Candidates are **not approved dependencies/assets**: verify each resource's own current licence/terms, compatibility, security and asset provenance before use.

15. When the selected mode needs browser 3D and a web-ready GLB/glTF exists, choose the **smallest sufficient delivery runtime**. Pass the classified mode explicitly:

```bash
python scripts/vault-agent.py 3d-runtime \
  "rotate and inspect the verified product" \
  --mode inspectable-object \
  --format glb
python scripts/vault-agent.py 3d-runtime-skill model-viewer-basic-inspector --output SKILL.md
```

The first deep runtime adapter is Google `<model-viewer>`. `inspectable-object` and simple `configurable-object` tasks may route there. `visual-only` does not become rotatable merely because a GLB exists. `spatial-exploration` and `interactive-world` escalate to a custom Three.js/R3F/Babylon/WebGPU/WebXR plan rather than being forced into a bounded single-object viewer.

16. Render desktop/mobile. If an effect ships, complete `EFFECT_QA_OBSERVATIONS.json` and run:

```bash
python scripts/vault-agent.py effect-qa <effect-id> EFFECT_QA_OBSERVATIONS.json
```

17. Complete `VISUAL_QA_OBSERVATIONS.json` plus `DESIGN_CRITIC_OBSERVATIONS.json` and run:

```bash
python scripts/validate-anti-generic-visual.py <site-root> VISUAL_QA_OBSERVATIONS.json --json-out visual-qa-score.json
python scripts/run-design-critic.py vault-build-plan.json DESIGN_CRITIC_OBSERVATIONS.json --json-out design-critic-result.json
```

18. Revise until every applicable gate passes.

## One-command helper

```bash
python scripts/vault-agent.py ingest "https://maps.example/business"
python scripts/vault-agent.py ingest BUSINESS_SOURCE_REPORT.json --output-dir business-ingestion
python scripts/vault-agent.py model business-ingestion
python scripts/vault-agent.py plan business-ingestion/business-profile.json
python scripts/vault-agent.py component "autosuggest"
python scripts/vault-agent.py immersive business-ingestion/business-profile.json --goal "continuous product storytelling"
python scripts/vault-agent.py immersive-skill continuous-scroll-narrative --output SKILL.md
python scripts/vault-agent.py effect business-ingestion/business-profile.json --section hero
python scripts/vault-agent.py effect-skill ambient-particle-network --output SKILL.md
python scripts/vault-agent.py 3d-mode "users swipe or drag the mannequin 360 to inspect the dress" --subject-class garment-textile --asset-format none --asset-readiness none
python scripts/vault-agent.py 3d-resource "create a web-ready mannequin and garment model" --domain fashion-couture
python scripts/vault-agent.py 3d-resource-skill character-human --output SKILL.md
python scripts/vault-agent.py 3d-runtime "rotate and inspect the verified dress mannequin" --mode inspectable-object --format glb
python scripts/vault-agent.py 3d-runtime-skill model-viewer-basic-inspector --output SKILL.md
python scripts/vault-agent.py effect-qa ambient-particle-network EFFECT_QA_OBSERVATIONS.json
python scripts/vault-agent.py studio-index
python scripts/vault-agent.py critic vault-build-plan.json DESIGN_CRITIC_OBSERVATIONS.json
```

The helper delegates to canonical vault tools; it does not duplicate their logic.

## Immersive Template Library

`immersive-templates/template-catalog.json` is the experience-architecture layer. It answers:

> If this website genuinely benefits from being immersive, **what kind of immersive experience should it be?**

The initial library contains six architectures across four immersion levels:

- Level 1 — motion-rich DOM: `motion-rich-portfolio`
- Level 2 — canvas/shader: `fluid-canvas-brand-hero`, `cinematic-gaming-commerce`
- Level 3 — mixed DOM + WebGL scrollytelling: `continuous-scroll-narrative`
- Level 4 — primary 3D world: `tactile-3d-object-library`, `procedural-living-world`

Selection uses the validated business profile, selected domain pack, the user's actual experience goal, asset readiness and performance priority. Every template records a state model, relevant 3D blueprint, runtime requirements, mobile transformation, reduced-motion behavior, normal-site fallback, suggested effects and source/reuse boundary.

`immersive-templates/source-policy.json` pins the six research repositories. Public source is not automatically reusable source. MIT references may be selectively adapted with notices; reference-only sources contribute principles but not implementation code, branding, copy, artwork, assets or exact choreography.

## 3D Mode Classification

`3d/mode-classification.json` is the mandatory interaction contract after 3D relevance/intent and before production/runtime selection. It answers:

> **What must the visitor actually be able to do with the 3D?**

The mode is stable unless the user/product requirement changes. Do not downgrade `inspectable-object` to an authored animation because only a video is available; instead produce/source the required geometry. Do not upgrade `visual-only` to a rotatable viewer merely because a GLB exists.

Detailed guidance: `3d/MODE_CLASSIFICATION.md`.

## 3D Production Resource Intelligence

`3d-production-resources/resource-catalog.json` is the **production capability layer after 3D mode selection**. It answers:

> We know the required 3D mode and asset. **What production category and external resource candidates can help us create it?**

The first catalog covers 18 production categories: procedural terrain, vegetation/nature, architectural generation, photogrammetry, point clouds/LiDAR, PBR materials/texturing, lighting/HDRI, simulation/physics, characters/humans, animation/mocap, GIS/maps, web export/glTF, asset libraries, rendering/optimization, data visualization, sound/audio, format conversion and Blender scripting.

The source adapter pins `agmmnn/awesome-blender` at a known revision. Its list is CC0, but linked resources keep their own independent licences/terms. The Vault therefore stores candidate names/links and original production guidance; it does not mirror third-party Blender add-ons, models, textures, HDRIs, datasets or commercial downloads.

A resource candidate is only a due-diligence lead. Verify its own current licence/terms, supported Blender/runtime versions, maintenance status, security implications, export compatibility, and the separate rights for any model/texture/HDRI/audio/scan/dataset used with it.

## 3D Delivery Runtime Intelligence

`3d-delivery-runtimes/runtime-catalog.json` is the layer between a prepared web asset and custom 3D engineering. It answers:

> We already classified the interaction mode and have the required asset. **Can a bounded standard runtime deliver that mode, or do we need custom Three.js/R3F/Babylon?**

The first deep adapter pins `google/model-viewer` and exposes five Vault-authored profiles:

- `model-viewer-basic-inspector`
- `model-viewer-annotated-inspector`
- `model-viewer-variant-configurator-lite`
- `model-viewer-animated-product`
- `model-viewer-ar-placement`

The runtime selector is now **mode-gated**. It requires `--mode`, filters to compatible delivery profiles and will block when an approved GLB/glTF is missing rather than inventing a fake viewer. It escalates spatial/world modes to a custom runtime and de-escalates visual-only mode to a simpler medium.

Google `<model-viewer>` is designed to make interactive 3D and optional AR easier across browsers/devices. The Vault uses it as the preferred bounded delivery step before custom Three.js when its feature set is sufficient. The source policy records the Apache-2.0 software licence, reviewed package version and tested Three.js peer relationship; shared/demo assets require separate provenance review.

## Interactive Effect Intelligence

`interactive-effects/effects.json` is the layer between ordinary components/motion and full 3D. It answers:

> What interactive enhancement is appropriate for this business, section and device/performance context — if any?

Selection uses business/domain fit, section compatibility, explicit business signals, asset readiness and performance priority. Every record includes runtime, performance tier, mobile strategy, reduced-motion fallback, adjustable controls and reject conditions. `none` is first-class.

When the effect becomes a primary explorable/configurable/spatial product experience, stop using the lightweight effect layer and route to `3d/interaction-intent-system.json`.

## ThreeUI Community reference adapter

`references/threeui-community.json` records transferable ideas from the public ThreeUI Community repository: richer interaction taxonomy, live controls and variants, per-item skills, runtime isolation, source provenance, measured FPS and agent-facing catalog access.

It is deliberately **not** a source mirror. It does not contain Pro/Beta implementation source, remote catalog media or entitlement-bypass logic. The default path is an original Vault implementation; the public Community package is used only when deliberately selected and its licence/asset/runtime requirements are preserved.

## Vault Studio and MCP foundations

Generate the human/agent browse index with:

```bash
python scripts/vault-agent.py studio-index
```

The Studio index now includes domain packs, section recipes, interactive effects, immersive templates, **3D modes**, 3D production resources, 3D delivery-runtime profiles, capability packs and reference patterns.

`scripts/vault-mcp.py` provides a local, read-only stdio MCP surface for effect, immersive-template, **3D-mode classification**, 3D-production-resource and 3D-delivery-runtime search/selection/skill retrieval. Delivery-runtime selection through MCP also requires the classified mode.

## What to read first

Always read:

- `AI_START_HERE.md`
- `AGENTS.md`
- the generated `vault-build-plan.json` when one exists

When a business source URL is supplied, also read `prompts/BUSINESS_SOURCE_INGESTION.md`, the selected source playbook and the generated source-of-truth bundle before planning. When public/admin structure matters, read the generated business entity/content/CMS models instead of inventing modules.

When an immersive experience is requested, read `immersive-templates/README.md` plus the template catalog and source policy, then generate the selected template's skill. Do not preload or copy the six source repositories.

When 3D is justified, read `3d/mode-classification.json` / `3d/MODE_CLASSIFICATION.md` and classify the interaction mode before opening production resources or delivery-runtime implementations.

When a concrete 3D production need exists after mode selection, read `3d-production-resources/README.md`, select one production category, generate its skill, and only then inspect the small number of external candidates needed for due diligence. Do not preload the full Awesome Blender list or treat its source-list licence as a licence for linked tools/assets.

When a prepared 3D asset needs browser delivery, pass the selected mode to `3d-delivery-runtimes/` and generate the selected runtime skill before opening model-viewer examples. Do not clone the entire upstream repository into the target project.

When an interactive effect is justified, read `interactive-effects/effects.json` and the generated skill for the selected effect. Read `references/threeui-community.json` only when that reference research is needed; do not preload external implementations.

Do **not** preload every style catalog, motion source, Component Gallery reference, HeroUI record, 3D recipe, benchmark, effect reference, immersive source implementation, Blender production resource, model-viewer example or source playbook. Search/select first, then read chosen records deeply.

## Hard rules that never disappear

- Research a real business before choosing style, immersive architecture, motion, effects or 3D.
- Exact/source facts remain source facts; do not replace them with derived or friendlier substitutes.
- Reviews marked verbatim remain verbatim.
- Respect the source asset policy; `allowlist-only` means no unlisted image may appear.
- Unsupported business fields are omitted or left empty rather than populated with placeholders.
- Admin/CMS structure is evidence-backed; do not invent operational modules, records or dashboard statistics.
- Review text is immutable source content unless the owner supplies replacement source text.
- Component semantics outrank appearance.
- Immersive templates and interactive effects are optional; `none` is a valid selection at either layer.
- Source-reference licences and reuse boundaries are hard gates. Do not copy reference-only implementations.
- **Classify every justified 3D request into mode 0–6 before production/runtime selection.**
- **A GLB/GLTF file never determines interaction mode and never automatically grants free rotation.**
- If the selected mode requires user-manipulable geometry and the asset is missing, preserve the mode and produce/source the asset rather than faking the interaction.
- A 3D production resource candidate is not approved until its own current licence/terms, maintenance, compatibility, security and asset provenance are verified.
- The CC0 licence of the Awesome Blender list does not transfer to linked tools, assets, services or datasets.
- A 3D delivery runtime does not justify or change 3D mode; it implements the already-approved interaction contract.
- Pin `@google/model-viewer` and its tested Three.js peer together unless compatibility is deliberately revalidated; do not use forced peer overrides as the default production strategy.
- Apache-2.0 coverage of model-viewer software does not automatically clear shared/demo models, HDRIs or other third-party assets.
- Effects must support a verified business/page purpose and may not imply fake telemetry, fake places or unsupported operational state.
- Do not clone protected layouts, brands, media, copy, exact choreography or restricted third-party implementation source.
- Do not invent business facts, products, prices, credentials, availability, integrations or proof.
- Generated/conceptual media representing a real product/property/facility must be clearly identified as such.
- 3D must be semantically relevant to the subject and user goal; spectacle or available tooling alone is insufficient.
- Raw Blender production scenes are not web deliverables: optimize geometry, textures, animation and export formats for the actual runtime.
- Essential content/actions must survive reduced motion, failed animation and non-WebGL fallbacks.
- Mobile is an intentional composition, not a shrunken desktop.
- Measured effect/3D performance and rendered visual QA are mandatory before handoff when those layers are used.
- Never claim localhost/deployment status that was not actually verified.

## Progressive disclosure levels

**Level 0 — Routing:** `AI_START_HERE.md`, `AGENTS.md`, `agent-runtime-index.json`.

**Level 1 — Source/research:** source URL, selected source playbook, Business Source Report, source-of-truth bundle and business profile.

**Level 2 — Content/admin modeling:** `BUSINESS_ENTITY_MODEL.json`, `PUBLIC_CONTENT_MODEL.json`, `ADMIN_CMS_MODEL.json`, `CMS_BUILD_CONTRACT.md`.

**Level 3 — Planning:** business profile, orchestrator output, selected prompt and selected pack.

**Level 4 — Implementation:** only selected pack required reads, selected immersive template skill, section/component/effect/3D recipes, **selected 3D mode**, selected 3D production-resource skill, selected 3D delivery-runtime skill, relevant contracts and target-repo conventions.

**Level 5 — Validation:** effect/3D/runtime performance QA when applicable, rendered QA, anti-generic gate, Design Critic and selected benchmark.

**Reference archive:** style catalogs, Component Gallery comparisons, HeroUI source research, motion/3D catalogs, immersive source pins, Awesome Blender source pin, model-viewer source pin and ThreeUI Community metadata. Query only when needed.

## Stop conditions

Stop and request evidence instead of improvising when a real business's core offer, audience or primary conversion is unclear. A blocked URL is not inspected evidence. Stop admin/CMS generation when the requested module has no underlying evidenced or owner-defined data model. Stop immersive selection when no architecture clears the threshold. Stop effect selection when no semantic candidate clears the threshold. Stop 3D selection when the subject or interaction goal is unclear. **Stop before production/runtime selection when the 3D mode is not explicit.** Stop 3D production-resource selection when the required asset/output is still vague. Do not install/adopt an external production candidate until its own rights, compatibility and provenance checks are complete. Stop 3D delivery selection until the classified mode and actual web asset format are known; escalate rather than forcing model-viewer when the selected mode exceeds its bounded interaction model. Stop handoff when measured/rendered evidence is missing or any applicable QA gate fails.
