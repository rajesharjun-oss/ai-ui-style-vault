# Build a Premium 3D & Immersive Web Experience

Use when the user requests a 3D website, WebGL/WebGPU, Three.js/R3F/Babylon/Spline, product configurator, spatial portfolio, showroom, digital twin, interactive globe, AR or WebXR.

Act as a senior product designer, content designer, 3D art director, accessibility specialist and performance/asset-pipeline engineer.

## 0. Mandatory business understanding before 3D selection

When the target is a real business, brand, creator, organisation, venue, product or service, read and satisfy `guides/BUSINESS_RESEARCH_GATE.md` first.

Do **not** select a 3D recipe, style, scene archetype, art direction, model, shader, video treatment or motion language until `BUSINESS_RESEARCH.md` is sufficiently complete and its `researchStatus` is `ready`.

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

## 1. Materialize and select an AI Agent Recipe

Read `3d/AI_AGENT_RECIPE_STANDARD.md`, then run:

```bash
python scripts/build-ai-agent-recipes.py
```

The registry must currently resolve **478 executable recipes**:

- 300 concrete 3D design directions;
- 138 MotionSites public reference abstractions;
- 40 MotionSites-derived motion patterns.

Every recipe includes when-to-use, when-not-to-use, design objective, composition instructions, motion instructions, implementation approach, asset instructions, responsive behaviour, performance limits, accessibility/fallback, originality rules, acceptance criteria and a self-contained `agentPrompt`.

After the business research gate is ready, first determine verified business facts, audience, primary task, target domain and page purpose. Then:

1. shortlist semantically compatible design-direction recipes;
2. choose **one** primary design-direction recipe;
3. add no more than **three** supporting motion-pattern recipes where they materially improve the experience;
4. use external-reference recipes only for abstract inspiration, never as a source to clone;
5. record chosen recipe IDs in the build/handoff notes;
6. explain how specific research findings caused each selection.

If no immersive recipe materially improves the task, do not force 3D.

## 2. Mandatory semantic relevance gate

Only after business understanding is established, complete `THREE_D_RELEVANCE_CONTRACT.md` before searching for or selecting any model, video, animated background, environment or shader. Read `semantic-relevance-standard.md` plus `3d/subject-domain-map.json`. Every primary visual requires a documented relevance score of 4–5; secondary decoration requires at least 3. Reject any asset chosen mainly because it looks premium, futuristic or impressive. A pizza website must not receive an unrelated Ferrari, and equivalent cross-domain mismatches are prohibited. Validate the central object, environment, props, materials, lighting, camera motion and fallback media as one coherent scene.

The semantic relevance gate does not replace business research; it validates visual choices against business understanding already established.

## 3. Choose the smallest sufficient medium

Before coding, prove the need and compare DOM/CSS, CSS perspective, image sequence/video, Rive, Spline, model-viewer, custom WebGL/WebGPU and WebXR. Complete the 3D contracts; choose one family/theme/blueprint; design the complete static fallback; define licences, capability tiers and budgets.

## 4. Implement DOM-first

Essential copy, controls, routes, prices, forms, CTAs, status and legal information remain semantic DOM. Lazy-load runtime/assets after capability and intent checks. Use one renderer where possible. Synchronise hotspots with DOM controls. Handle reduced motion, save data, low power/memory, unsupported devices, loading phases, model/texture/shader errors and context loss.

Execute the selected recipes rather than improvising around their names. Follow every selected recipe's composition, motion, responsive, asset, performance, fallback and originality instructions.

## 5. Validate before handoff

Measure bundles, asset transfer, triangles, draw calls, texture/GPU memory, sustained FPS, input latency and first useful frame. Render static, basic-mobile, balanced and high tiers; WebGL disabled; slow network; errors; context loss; keyboard/focus; mobile touch; high zoom; fullscreen and XR states. Prove the primary task works without 3D.

Validate every selected recipe's acceptance criteria before saying the build is complete.

For a real business, the handoff must also show the causal chain:

`verified business evidence → audience/task → content strategy → selected design recipe → selected motion patterns → implementation decisions`

If that chain cannot be demonstrated, the build is not vault-compliant.

## 6. Reference and originality policy

Treat MotionSites, Refs.Gallery, awards sites, portfolios and marketplaces as reference-only unless separate terms grant reuse. Do not copy code, premium/proprietary prompts, media, branding, copy, models, textures, exact layout or choreography. Extract only transferable design/interaction principles and produce a materially original result for the target business.
