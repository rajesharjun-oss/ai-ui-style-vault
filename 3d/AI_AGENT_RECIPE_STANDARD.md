# AI Agent Recipe Standard

This standard turns every concrete 3D design direction, MotionSites reference record and MotionSites-derived motion pattern into an executable design-and-build recipe for Codex, Claude Code, Gemini and other coding agents.

The recipe layer is intentionally **instruction-driven, not reference-driven**. External references are evidence and inspiration only. Agents must create original design systems, composition, copy, code, motion and assets.

## Coverage target

The materializer in `scripts/build-ai-agent-recipes.py` must resolve the current library into exactly:

- 300 concrete 3D design directions from `packs/3d-immersive-web/design-combination-system.json`;
- 138 MotionSites public reference records from the two public-catalog files in `3d/references/`;
- 40 MotionSites-derived motion patterns from the two pattern files in `3d/techniques/`.

Current executable-recipe target: **478 recipes**.

A source entry is not considered agent-ready until it resolves to all required recipe fields below.

## Required recipe fields

Every recipe must contain:

1. `whenToUse` — suitable page/business situations and the user outcome it supports.
2. `whenNotToUse` — explicit rejection conditions, including semantic mismatch.
3. `designObjective` — the intended experience/result, not a visual-effects description.
4. `compositionInstructions` — hierarchy, focal object, typography, spacing and section guidance.
5. `motionInstructions` — triggers, progress model, choreography, pacing and interaction limits.
6. `implementationApproach` — preferred technical medium and engineering strategy.
7. `assetInstructions` — required media/model inputs, provenance and semantic-relevance rules.
8. `responsiveBehavior` — desktop, tablet and mobile adaptation.
9. `performanceLimits` — progressive enhancement, loading, budget and capability-tier rules.
10. `accessibilityAndFallback` — reduced motion, keyboard/focus, semantic DOM and static fallback.
11. `originalityRules` — mandatory anti-cloning and rights-conscious constraints.
12. `acceptanceCriteria` — observable QA conditions before the agent may call the build complete.
13. `agentPrompt` — a self-contained execution prompt assembled from the recipe.

## Global operating rules

### 1. Semantic relevance is a hard gate

Complete `packs/3d-immersive-web/templates/THREE_D_RELEVANCE_CONTRACT.md` before asset search. Read `packs/3d-immersive-web/semantic-relevance-standard.md` and `3d/subject-domain-map.json`.

Primary hero media/3D subjects require relevance score **4–5**. Secondary decorative media requires at least **3**. Validate the complete scene: subject, environment, props, materials, lighting, camera/motion and fallback. Reject a beautiful but unrelated concept.

### 2. Choose the smallest sufficient medium

Prefer the least complex medium that can deliver the intended outcome:

`DOM/CSS → CSS perspective → image sequence/video → Rive → Spline → model-viewer → custom WebGL/WebGPU → WebXR`

Do not select Three.js, WebGPU or XR merely to make a page feel premium.

### 3. Content and product tasks stay usable without 3D

Navigation, forms, prices, legal text, product choices, CTAs, status and essential copy remain semantic DOM. The 3D/cinematic layer enhances comprehension or emotion; it cannot become the only usable interface.

### 4. Motion has a budget

Use one primary motion idea per major viewport moment and no more than five meaningful interaction systems on a page unless the brief explicitly justifies more. Avoid continuous movement in every section. The page needs visual rest.

### 5. Mobile is intentionally redesigned

Do not simply shrink the desktop experience. Reduce simultaneous layers, particle counts, camera movement and pinned distance. Preserve the same story/task with a lighter composition and a static or low-motion path where necessary.

### 6. Originality is mandatory

For external references, retain only abstract learnings: hierarchy, interaction type, pacing principle, information architecture pattern or technical approach. Never reproduce exact layout, source code, proprietary prompts, copy, branded media, models, textures or choreography.

## Agent selection workflow

When the user asks for a website or app and does not name a recipe:

1. verify business facts, audience, primary task and page purpose;
2. infer the target domain;
3. shortlist recipe candidates whose `whenToUse`, tags/domains and page purpose match;
4. reject candidates failing semantic relevance or capability/performance constraints;
5. choose one primary design direction and at most three supporting motion patterns;
6. generate a concise build brief from their recipe fields;
7. implement the original experience;
8. run visual, responsive, accessibility, performance and failure-state QA;
9. state which recipe IDs were used in the handoff notes.

If no candidate materially improves the experience, build the page without immersive 3D.

## Agent prompt contract

Each generated `agentPrompt` must tell the coding agent to:

- act as senior product designer, content designer, art director and front-end engineer;
- preserve verified business facts and avoid fabricated claims;
- create an original composition rather than cloning the source/reference;
- follow the semantic relevance gate before asset selection;
- keep essential UI in semantic DOM;
- implement responsive and reduced-motion variants;
- use progressive enhancement and the smallest sufficient medium;
- test the acceptance criteria before claiming completion;
- document the chosen recipe ID(s), deviations and fallback.

## Generated output

Run:

```bash
python scripts/build-ai-agent-recipes.py
```

Default output:

`3d/generated/ai-agent-recipes.json`

The generated file is deterministic and may be regenerated whenever the design system, public reference catalogs or motion-pattern catalogs change.
