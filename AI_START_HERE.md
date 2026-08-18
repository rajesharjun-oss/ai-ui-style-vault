# AI UI Style Vault — Start Here

This is the shortest supported entry point for an AI coding/design agent.

The vault is large by design, but an agent should **not read the entire repository** before every build. Use progressive disclosure: understand the task, run the router/orchestrator, then read only the files selected for that task.

## 60-second workflow

1. Inspect the target project and user brief.
2. For a real business, create/validate `business-profile.json` before visual design.
3. Run the master planner:

```bash
python scripts/vault-build-orchestrator.py business-profile.json --output vault-build-plan.json
```

4. Read `vault-build-plan.json` and only the domain/capability/contract files it requires.
5. Resolve difficult UI components through the component intelligence layer:

```bash
python scripts/resolve-component-contract.py "<component need>"
```

6. Build the semantic/static experience first. Add motion/3D only when the plan justifies it.
7. Render desktop/mobile and complete `VISUAL_QA_OBSERVATIONS.json` plus `DESIGN_CRITIC_OBSERVATIONS.json`.
8. Run both gates:

```bash
python scripts/validate-anti-generic-visual.py <site-root> VISUAL_QA_OBSERVATIONS.json --json-out visual-qa-score.json
python scripts/run-design-critic.py vault-build-plan.json DESIGN_CRITIC_OBSERVATIONS.json --json-out design-critic-result.json
```

9. Revise until both pass.

## One-command helper

Use `scripts/vault-agent.py` as the compact front door:

```bash
python scripts/vault-agent.py plan business-profile.json
python scripts/vault-agent.py component "autosuggest"
python scripts/vault-agent.py component "dropdown menu"
python scripts/vault-agent.py critic vault-build-plan.json DESIGN_CRITIC_OBSERVATIONS.json
```

The helper delegates to canonical vault tools; it does not duplicate their logic.

## What to read first

Always read:

- `AI_START_HERE.md`
- `AGENTS.md`
- the generated `vault-build-plan.json` when one exists

Then read only the files named by the selected prompt, domain pack, capability pack, component contract or QA stage.

Do **not** preload every style catalog, motion source, Component Gallery reference, HeroUI record, 3D recipe or benchmark into context. Search/select first, then read the chosen records deeply.

## Hard rules that never disappear

- Research a real business before choosing style, motion or 3D.
- Component semantics outrank appearance.
- Do not clone protected layouts, brands, media, copy or exact choreography.
- Do not invent business facts, products, prices, credentials, availability, integrations or proof.
- A real product/property/facility represented by generated or conceptual media must be clearly identified as such.
- 3D must be semantically relevant to the subject and user goal; spectacle alone is insufficient.
- Essential content/actions must survive reduced motion, failed animation and non-WebGL fallbacks.
- Mobile is an intentional composition, not a shrunken desktop.
- Rendered QA is mandatory before handoff.
- Never claim localhost/deployment status that was not actually verified.

## Progressive disclosure levels

**Level 0 — Routing:** `AI_START_HERE.md`, `AGENTS.md`, `agent-runtime-index.json`.

**Level 1 — Planning:** business profile, orchestrator output, selected prompt and selected pack `pack.json`.

**Level 2 — Implementation:** only selected pack required reads, selected section/component/3D recipes, relevant contracts and target-repo conventions.

**Level 3 — Validation:** rendered QA, anti-generic gate, Design Critic, selected benchmark when appropriate.

**Reference archive:** style catalogs, Component Gallery comparisons, HeroUI source research, motion/3D reference catalogs. Query them only when needed.

## Stop conditions

Stop and request evidence instead of improvising when a real business's core offer, audience or primary conversion is unclear. Stop 3D selection when the subject or interaction goal is unclear. Stop handoff when rendered evidence is missing or either QA gate fails.
