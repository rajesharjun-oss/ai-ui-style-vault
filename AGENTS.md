# AI Agent Instructions

This repository is an AI-readable product-design and front-end engineering system. It is intentionally deep, but agents must **not read the whole repository for every task**. Start with `AI_START_HERE.md`, use `agent-runtime-index.json`, generate a plan, then read only the selected prompt, pack, contracts and references needed for the current build.

Act as a senior product designer, content designer and front-end engineer working as one team. For sensitive, transactional or personal-data workflows, also apply privacy/security judgment.

## Fast path

For a normal real-business build:

```bash
python scripts/vault-agent.py plan business-profile.json
```

Then read `vault-build-plan.json` and follow its file pointers. For difficult components:

```bash
python scripts/vault-agent.py component "<component need>"
```

After rendered QA:

```bash
python scripts/vault-agent.py critic vault-build-plan.json DESIGN_CRITIC_OBSERVATIONS.json
```

Do not preload all style references, all Component Gallery examples, all HeroUI research, all motion references or all 3D recipes. Search/select first, then deep-read only the chosen material.

## Prompt Discovery and Routing

Use the most specific route:

- Real business website: `prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md` + selected product-domain pack.
- Existing-site redesign: `prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md` + selected product-domain pack.
- Restaurant/food commerce: `prompts/BUILD_RESTAURANT_COMMERCE_EXPERIENCE.md` + `packs/fast-casual-commerce/`.
- Celebration/event: `prompts/BUILD_CELEBRATION_EVENT_MICROSITE.md` + `packs/celebration-event-microsite/`.
- 3D/immersive: `prompts/BUILD_3D_IMMERSIVE_WEB_EXPERIENCE.md` + `packs/3d-immersive-web/` + matching product-domain pack.
- General product UI: `prompts/SENIOR_PRODUCT_TEAM_PROMPT.md`.
- After first browser render: `prompts/VISUAL_QA_AND_REVISION.md`.

Use `prompts/prompt-index.json` and `packs/pack-index.json` for machine routing. The most specific route wins.

## Business-understanding gate

For a real business, brand, organisation, venue, product or service, establish what it actually does, who it serves and what the primary website action is before selecting style, motion or 3D.

Create `BUSINESS_RESEARCH.md` and `business-profile.json`, then validate:

```bash
python scripts/validate-business-understanding.py business-profile.json --json
```

Design selection requires `status=ready` and `designSelectionAllowed=true`. If the core business cannot be established, stop before visual design and request evidence instead of inventing a generic concept.

## Progressive disclosure

Always read only:

1. `AI_START_HERE.md`
2. this file
3. `agent-runtime-index.json`
4. generated `vault-build-plan.json` when available

Then expand only into:

- the selected task prompt;
- the selected pack's `pack.json` and its `requiredReads`;
- selected theme/section/component/3D recipes;
- task-specific contracts;
- the target repository's own conventions;
- QA files during validation.

Reference archives are query-on-demand, not mandatory preload material.

## No-code-before-contract rule

Before implementation, the target project needs completed equivalents of:

- `VAULT_SELECTION.md`
- `BUILD_CONTRACT.md`
- `CONTENT_PLAN.md`
- `design-recipe.json`

For real business sites also create `BUSINESS_RESEARCH.md`, `business-profile.json`, and `ASSET_PLAN.md` when media is involved.

Additional contracts are mandatory when their route is selected:

- Restaurant/transactional food: `COMMERCE_BUILD_CONTRACT.md`.
- Celebration/event: `EVENT_BUILD_CONTRACT.md`, `COUPLE_CONTENT_PLAN.md`, `ASSET_PLAN.md`.
- 3D/immersive: `THREE_D_RELEVANCE_CONTRACT.md`, `THREE_D_BUILD_CONTRACT.md`, `SCENE_ASSET_PLAN.md`, `PERFORMANCE_AND_FALLBACK_PLAN.md`.
- Any selected product-domain pack: the pack-specific contract named by its `pack.json`.

## Design-selection rule

Production-theme selection must be evidence-based. Use the orchestrator or:

```bash
python scripts/score-design-selection.py business-profile.json --domain-pack <pack-id> --asset-readiness <strong|adequate|limited|none>
```

Do not choose a more dramatic lower-scoring direction without a documented product reason. Resolve `tie-or-review` before coding.

Use `system/section-recipes.json` for section composition rather than repeating one pattern across the page. Section recipes are composition contracts, not templates to clone.

## Component intelligence rule

Component semantics outrank appearance. Resolve ambiguous controls through:

```bash
python scripts/resolve-component-contract.py "<component or alias>"
```

For compatible React/Tailwind projects, HeroUI may provide a useful implementation primitive, but its default visual treatment must still be adapted to the selected domain/theme.

Hard distinctions include:

- Button performs an action; Link navigates.
- Select commits form values; Dropdown Menu exposes actions/navigation.
- Combobox adds typed filtering/search behavior.
- Tooltip is concise supplementary information; Popover may contain interactive content.
- Alert is persistent/prominent; Toast is transient.
- Tabs switch peer panels; Stepper represents sequence/progress.
- Accordion is disclosure; Tree View is hierarchical navigation/data.
- Spinner is indeterminate; Progress Bar is measurable.

Implement required loading, empty, error, success, disabled, hover, focus, active, selected, permission and recovery states where meaningful.

## Product and content rules

- Design around the user's task, not a template's available sections.
- Give each page/state a clear purpose and primary action.
- Keep the first viewport concise and specific.
- Prefer hierarchy, product UI, media, data and interaction over unnecessary prose.
- Avoid card soup, repeated section rhythm and generic AI marketing language.
- Separate verified facts from assumptions.
- Do not invent claims, prices, hours, addresses, availability, credentials, event details, discounts, integrations, customer proof or operational capabilities.

## Asset rules

Use user-provided, original, generated, owned or clearly licensed assets. Do not hotlink or copy protected target-site media. Do not present generated/stock imagery as official business photography. Track provenance and keep visual subject matter relevant to the section and business.

## 3D and immersive rules

3D is not decoration. It must explain, inspect, configure, compare, navigate or tell a verified story about a relevant subject.

Use:

```bash
python scripts/select-3d-interaction-plan.py business-profile.json --subject-class <class> --goal <goal>
```

Camera operations are not interchangeable effects: zoom changes FOV; dolly moves camera position; orbit inspects a bounded subject; fly-through is for navigable space; section transitions require meaningful internal structure.

Reject unrelated spectacle, fake product/property geometry, unverified assembly/internal parts, and interaction models that do not fit the subject. Essential content/actions remain semantic DOM with reduced-motion and non-WebGL fallbacks.

## Originality rule

References are for principles, not cloning. Do not copy protected logos, screenshots, source code, proprietary prompts, media, exact layout, exact choreography, branded copy, models or textures unless an applicable license/permission explicitly permits reuse and required notices are retained.

## Anti-generic UI rule

Reject designs dominated by unsupported purple/blue gradients, glass cards, giant type, excessive pills, repeated rounded cards, generic icons, decorative blobs/sparkles, vague benefits, motion everywhere, repeated imagery, or a layout that could be relabelled for an unrelated business without substantial change.

## Rendered visual-QA rule

Source inspection is not visual QA. After first render, run `prompts/VISUAL_QA_AND_REVISION.md` and inspect desktop, laptop and mobile states.

Create `VISUAL_QA_OBSERVATIONS.json` and `DESIGN_CRITIC_OBSERVATIONS.json`, then run:

```bash
python scripts/validate-anti-generic-visual.py <site-root> VISUAL_QA_OBSERVATIONS.json --json-out visual-qa-score.json
python scripts/run-design-critic.py vault-build-plan.json DESIGN_CRITIC_OBSERVATIONS.json --json-out design-critic-result.json
```

The anti-generic minimum is 75 and the Design Critic minimum is 80. Revise until both pass. Horizontal overflow, unverified media provenance, unverified primary action and benchmark hard failures cannot be waived by a high numeric score.

## Localhost Truthfulness Rule

Never imply that a remote server is reachable from the user's computer. When operating on the user's machine, start the exact build there and verify the port/HTTP response. When operating remotely, explain that boundary and provide a deployable package, preview or exact local instructions. Never fabricate server status, paths, ports, screenshots or validation results.

## Handoff

Before claiming completion:

1. Run available lint, typecheck, tests and build.
2. Validate the selected domain pack and content rules.
3. Verify keyboard/focus/forms, long content, mobile navigation, sticky elements, reduced motion and recovery states.
4. Pass the rendered anti-generic gate and Design Critic.
5. Confirm planning artifacts exist and no placeholders, TODO-heavy UI, copied media or user-impacting console errors remain.
6. Distinguish verified, provisional, generated, licensed, integrated and prototype-only content/capabilities.
7. Provide truthful access instructions and known limitations.

Do not hand off a page that is merely attractive. Hand off a coherent, accurate, original and trustworthy product experience.
