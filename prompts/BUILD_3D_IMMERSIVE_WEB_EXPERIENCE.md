# Build a Premium 3D & Immersive Web Experience

Use when the user requests a 3D website, WebGL/WebGPU, Three.js/R3F/Babylon/Spline, product configurator, spatial portfolio, showroom, digital twin, interactive globe, AR or WebXR.

Act as a senior product designer, content designer, 3D art director, technical 3D director, accessibility specialist and performance/asset-pipeline engineer.

## 0. Mandatory business understanding before 3D selection

When the target is a real business, brand, creator, organisation, venue, product or service, read and satisfy `guides/BUSINESS_RESEARCH_GATE.md` first.

Do **not** select a 3D recipe, style, scene archetype, art direction, model, shader, video treatment or motion language until `BUSINESS_RESEARCH.md` and `business-profile.json` establish what the business actually does and design selection is allowed.

The business research must establish from evidence:

- what the business actually does;
- its core offer/content/products/services;
- its primary audience/customer;
- the primary website action or user task;
- the major content/proof types;
- meaningful visual/brand/cultural signals;
- verified facts versus owner-confirmation items.

If supplied Instagram, TikTok or other sources are inaccessible, search alternative public sources. If the core business remains unclear, stop before design selection and request screenshots, a screen recording, bio, service/product information, brand materials or other evidence. Never substitute a generic creator, luxury, futuristic or category-themed concept for missing business understanding.

3D selection is a consequence of business research, not the starting point.

## 1. Mandatory 3D subject + interaction-intent gate

Before selecting a 3D design recipe, read:

- `3d/subject-domain-map.json`
- `3d/interaction-intent-system.json`
- `packs/3d-immersive-web/interaction-patterns.json`

Classify the intended primary 3D subject as one of the supported subject classes, then state the user goal. Run:

```bash
python scripts/select-3d-interaction-plan.py business-profile.json \
  --subject-class <subject-class> \
  --goal <goal>
```

This gate exists because different 3D subjects require different scene structures and interaction languages. They are not interchangeable visual effects.

Examples:

- **Vehicle / assembled product:** orbit inspection, authored detail cameras, real component explosion/assembly, verified material/configuration switching. A car forming from parts requires separate component meshes and a real assembly story; it is not a generic transition.
- **Architecture / property:** exterior orbit, authored room nodes, dolly/fly-through, section cuts, floor/unit focus and verified dimensions. A house should not fly apart or assemble unless construction sequence is actually being explained.
- **Garment / textile:** fit/material inspection, bounded viewpoints and verified fabric variants. Do not apply automotive explosion choreography to clothing.
- **Food:** ingredient/process storytelling and product focus. Do not apply industrial mechanical interaction language.
- **Spatial data:** verified routes, maps, nodes and data-driven particles. Never fabricate routes or use a decorative globe with fake information.
- **Abstract concepts:** only use 3D when the geometry has a documented mapping to a real process, system or brand idea.

### Camera semantics are mandatory

Treat camera operations as meaning, not decoration:

- **Dolly in/out:** camera physically approaches or leaves the subject; useful for revealing detail and spatial relationship.
- **Zoom:** changes field of view; it is not the same as dolly movement and can distort perceived perspective.
- **Orbit:** inspection around a stable target; appropriate for bounded products, not every hero.
- **Pan/tilt:** redirects attention from a fixed camera position.
- **Truck/pedestal:** lateral/vertical translation; useful for silhouette and architectural reveals.
- **Fly-through:** movement through navigable space; appropriate for verified property/spatial scenes with bounds and fallback.
- **Target focus:** authored transition to a component, room, amenity or hotspot.
- **Section transition:** coordinated camera + clipping/section plane to reveal meaningful internal structure.

The selector must block a subject class that is unrelated to the verified business. A tax firm cannot receive a vehicle merely because vehicle animation is impressive. A fashion brand cannot inherit a house fly-through. A real-estate development cannot receive mechanical car assembly choreography.

If the requested interaction is `review-required` or `blocked`, do not implement it until the missing structural/semantic requirement is resolved.

## 2. Materialize and select an AI Agent Recipe

Only after the business gate and the subject/interaction-intent gate are satisfied, read `3d/AI_AGENT_RECIPE_STANDARD.md`, then run:

```bash
python scripts/build-ai-agent-recipes.py
```

The registry currently resolves **478 executable recipes**:

- 300 concrete 3D design directions;
- 138 MotionSites public reference abstractions;
- 40 MotionSites-derived motion patterns.

Every recipe includes when-to-use, when-not-to-use, design objective, composition instructions, motion instructions, implementation approach, asset instructions, responsive behaviour, performance limits, accessibility/fallback, originality rules, acceptance criteria and a self-contained `agentPrompt`.

After the preceding gates are ready:

1. shortlist semantically compatible design-direction recipes;
2. choose **one** primary design-direction recipe;
3. add no more than **three** supporting motion-pattern recipes where they materially improve the experience;
4. reject motion recipes that conflict with the selected subject interaction plan;
5. use external-reference recipes only for abstract inspiration, never as a source to clone;
6. record chosen recipe IDs and selected interaction IDs in the build/handoff notes;
7. explain how specific research findings caused each selection.

If no immersive recipe materially improves the task, do not force 3D.

## 3. Mandatory semantic relevance gate

Complete `THREE_D_RELEVANCE_CONTRACT.md` before searching for or selecting any model, video, animated background, environment or shader. Read `semantic-relevance-standard.md` plus `3d/subject-domain-map.json`. Every primary visual requires a documented relevance score of 4–5; secondary decoration requires at least 3.

Validate the full scene, not only the hero object:

- central object/subject;
- environment;
- supporting props;
- materials;
- lighting;
- camera behaviour;
- interaction model;
- fallback media.

Reject any asset or interaction chosen mainly because it looks premium, futuristic or impressive.

## 4. Choose the smallest sufficient medium

Before coding, prove the need and compare:

`DOM/CSS → CSS perspective → authored video → image sequence → Rive → Spline → model-viewer → Three.js/R3F/Babylon → custom WebGL/WebGPU → WebXR`

Choose according to the interaction requirement, not fashion:

- authored video/image sequence for fixed cinematic or scroll-scrub choreography;
- model-viewer for straightforward bounded product inspection/AR;
- Spline for moderate art-directed interactivity;
- Three.js/R3F/Babylon for custom camera systems, true assembly/explosion, configurators, spatial navigation and data-driven scenes;
- WebGPU/custom pipelines only when the rendering/compute requirement justifies the engineering and compatibility cost.

Complete the 3D contracts; design the complete static fallback; define licences, capability tiers and budgets.

## 5. Model and animation structure must support the interaction

Do not promise an interaction the assets cannot support.

For assembly/exploded product scenes, require:

- separately addressable meshes/components;
- meaningful pivots/origins;
- deterministic assembled and exploded transforms;
- named component hierarchy;
- verified internal components when shown;
- camera states that preserve orientation.

For property walkthroughs, require:

- navigable spatial geometry;
- correct scale or clearly labelled concept scale;
- room/floor structure;
- camera/navigation bounds and collision strategy;
- authored viewpoints and reset/recovery;
- real-versus-render provenance.

For deforming garments/soft bodies, require an appropriate rig, cloth simulation or authored animation and do not imply unknown fabric behaviour.

For scroll choreography, use explicit scene states/chapter progress; do not make every object respond independently to scroll.

## 6. Implement DOM-first

Essential copy, controls, routes, prices, forms, CTAs, status and legal information remain semantic DOM. Lazy-load runtime/assets after capability and intent checks. Use one renderer where possible. Synchronise hotspots with DOM controls. Handle reduced motion, save data, low power/memory, unsupported devices, loading phases, model/texture/shader errors and context loss.

Execute the selected recipes and interaction plan rather than improvising around their names.

## 7. Validate before handoff

Measure bundles, asset transfer, triangles, draw calls, texture/GPU memory, sustained FPS, input latency and first useful frame. Render static, basic-mobile, balanced and high tiers; WebGL disabled; slow network; errors; context loss; keyboard/focus; mobile touch; high zoom; fullscreen and XR states when applicable.

Also validate the actual interaction semantics:

- assembly ends in the correct component transforms;
- explosion preserves component identity and orientation;
- camera reset returns to a stable authored pose;
- property navigation does not unintentionally pass through geometry;
- hotspots remain aligned and accessible;
- material switching represents real variants;
- reduced-motion mode removes forced camera travel while preserving direct access to the same information;
- primary task works without 3D.

For a real business, the handoff must show the causal chain:

`verified business evidence → valid 3D subject → valid user goal → interaction/camera plan → asset/model requirements → selected design recipe → implementation decisions`

If that chain cannot be demonstrated, the build is not vault-compliant.

## 8. Reference and originality policy

Treat MotionSites, Refs.Gallery, awards sites, portfolios and marketplaces as reference-only unless separate terms grant reuse. Do not copy code, premium/proprietary prompts, media, branding, copy, models, textures, exact layout or choreography. Extract only transferable design/interaction principles and produce a materially original result for the target business.
