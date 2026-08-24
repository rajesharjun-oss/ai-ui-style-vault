# Immersive Template Library

This layer turns immersive references into reusable **architectures**, not cloned websites.

## Where it sits

`business research → content/CMS model → domain pack → page/section composition → components → immersive template (optional) → effects/3D recipes → QA`

An immersive template is selected only when the verified business story or user task benefits from continuous motion, canvas/WebGL, spatial inspection or a strong interactive world. `none` is a valid decision.

## Commands

```bash
python scripts/vault-agent.py immersive business-profile.json --goal "product launch"
python scripts/vault-agent.py immersive business-profile.json --goal "browse and inspect products" --level 4
python scripts/vault-agent.py immersive-skill tactile-3d-object-library --output SKILL.md
python scripts/immersive-templates.py validate
```

## Six initial architectures

- `motion-rich-portfolio` — motion-rich semantic DOM.
- `fluid-canvas-brand-hero` — interactive WebGL fluid field behind real content.
- `continuous-scroll-narrative` — chapter-based scrollytelling with a persistent visual stage.
- `tactile-3d-object-library` — browse → inspect → manipulate → return.
- `procedural-living-world` — seeded environmental world with restrained pointer response.
- `cinematic-gaming-commerce` — entertainment storefront with cinematic merchandising and overlays.

## Source policy

`source-policy.json` pins the six inspected repositories and records whether their implementation may be copied.

WebGL Fluid Background and GameOver are marked as MIT copy/adapt eligible, but the Vault does not mirror their full repositories in this first wave. An agent may selectively vendor the necessary MIT files at build time while preserving notices and separately auditing assets/plugins. Complete Shelf, Sylva, the Gentlerain clone and React Portfolio are **reference-only** for this Vault layer.

## Build rules

1. Start from a validated `business-profile.json`.
2. Select the domain pack before choosing immersion.
3. Run `immersive` with the user's actual goal.
4. If the decision is `none`, keep the normal premium site.
5. If a template is selected, generate its Skill.md and combine it with the named 3D blueprint/effects.
6. Replace source-specific identity, copy and media with verified business content or clearly labelled concept media.
7. Preserve normal semantic navigation/content and a non-immersive fallback.
8. Treat mobile as a different composition with lower simulation/geometry cost.
9. Run effect/3D performance QA plus the normal anti-generic visual QA and Design Critic.

## What 'template' means here

A template is a machine-readable experience contract: page architecture, state model, runtime tier, eligible domains/goals, mobile transformation, fallback, recommended effects and source/reuse boundary. It is deliberately more reusable than a copied screenshot or a hard-coded clone.
