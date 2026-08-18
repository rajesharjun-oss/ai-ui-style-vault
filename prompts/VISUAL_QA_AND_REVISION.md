# Visual QA and Revision

This prompt is mandatory after the first browser render of a website, web application, dashboard, or app-like interface.

Source-code inspection is not a visual review. A handoff is not complete until the rendered implementation has been inspected, corrected, passed through the structured anti-generic QA gate, and passed through the Design Critic when a Vault build plan exists.

## Goal

Find and correct visible, interactive, responsive, content, asset, originality, component-contract, design-drift, and generic-AI-pattern problems before handoff.

## 1. Prepare the review

- Start the application in the environment where it will be tested.
- Verify the actual URL and HTTP response.
- Open a clean browser session.
- Record the build commit or file version.
- Disable browser extensions that materially affect layout when possible.
- Use realistic content and data.
- Have `vault-build-plan.json`, the selected component contracts, and any benchmark expectations available for comparison.

## 2. Capture the required viewports

At minimum capture:

- 1440×1000 desktop.
- 1280×800 laptop.
- Approximately 390×844 mobile.

Also capture:

- First viewport.
- Every major section or route.
- Mobile navigation open.
- Important hover, focus, open, loading, empty, error, and success states.
- Modals, drawers, menus, tables, forms, and media controls.
- Reduced-motion mode for motion-heavy experiences.

## 3. Inspect product and content quality

Check:

- Can the user understand the offer or task immediately?
- Is the primary action obvious?
- Is the first viewport concise?
- Are headings specific rather than interchangeable?
- Are benefits or calls to action repeated?
- Are paragraphs or cards doing work that a visual, UI demonstration, metric, table, or disclosure could do better?
- Is practical business information complete and easy to find?
- Does each section have a distinct purpose?
- Could any section be removed without loss? If yes, remove or merge it.
- Do selected section recipes match their actual purpose and evidence?
- Did the implementation drift from the researched business, primary task, selected theme, or conversion model?

## 4. Inspect component correctness

For each important interactive component, compare the rendered behavior to the canonical component contract.

Check:

- Was the correct semantic component chosen for the task?
- Are required loading, empty, error, selected, disabled, open/closed, validation, and recovery states present where relevant?
- Does keyboard behavior match the component model?
- Are labels, accessible names, descriptions, errors, current/selected state, sort state, or expanded state exposed appropriately?
- Does the component have an intentional mobile strategy?
- Has a generic visual substitute replaced the intended component? Examples: cards replacing a comparison table, a dropdown menu replacing a select, a tooltip containing interactive form content, or a toast replacing persistent validation.

Use `python scripts/resolve-component-contract.py "<component or alias>"` when the correct contract is unclear.

## 5. Inspect visual hierarchy and originality

Check:

- Display type does not crowd out useful content.
- Heading scales step down logically.
- Line lengths are readable.
- Spacing communicates grouping.
- Cards are used only when the content is an independent object or action.
- Colour and emphasis match decision priority.
- The page does not repeat the same section rhythm.
- Decorative elements have a product or brand reason.
- The result looks specific to this product or business.
- The page is not relying on default purple/blue gradients, glass cards, excessive pills, sparkles/blobs, generic feature cards, or giant type merely to appear premium.
- The implementation could not be relabelled for an unrelated business without substantial change.

## 6. Inspect assets and art direction

Check:

- Every image is relevant to its section.
- The same image is not repeated across unrelated sections.
- Product imagery has consistent lighting, angle, crop, background, and quality.
- Images are sharp at rendered size.
- Generated or stock assets are not presented as official business photography.
- Process claims use process imagery.
- Media crops work on mobile.
- Text remains legible over media.
- Alt text and fallbacks are appropriate.
- No protected target-site assets are hotlinked or copied without permission.
- Any 3D, video, or immersive visual remains semantically relevant to the business and page purpose.

## 7. Inspect layout and responsiveness

Check:

- No horizontal overflow.
- No clipped text or controls.
- Sticky or fixed headers do not cover content.
- Anchor links use correct offsets.
- Browser zoom does not break navigation or headings.
- Mobile composition is intentionally rearranged rather than merely shrunk or stacked.
- Touch targets are usable.
- Tables have a mobile strategy.
- Footer and final actions remain reachable.
- Safe-area and viewport-height behaviour are sensible.

## 8. Inspect interaction and accessibility

Check:

- Keyboard order is logical.
- Focus is visible.
- Menus, dialogs, drawers, tabs, and accordions are operable.
- Forms have persistent labels and useful errors.
- Loading and progress states are understandable.
- Empty and error states provide recovery.
- Destructive actions require appropriate confirmation.
- Colour contrast is adequate.
- Reduced-motion mode preserves all content and actions.
- Autoplay media has controls when required.
- Browser console contains no user-impacting errors.

## 9. Inspect performance signals

Check:

- Hero media does not block first paint unnecessarily.
- Offscreen media is lazy-loaded.
- Images have appropriate dimensions and formats.
- Motion uses transform and opacity where possible.
- Layout shift is controlled.
- Heavy libraries are justified.
- Mobile CPU and scrolling remain responsive.

## 10. Structured anti-generic QA gate

After the screenshots have been inspected, copy `quality/VISUAL_QA_OBSERVATIONS.template.json` into the target project as `VISUAL_QA_OBSERVATIONS.json` and complete it from observed evidence. Do not mark an item true without inspecting it.

Then run:

```bash
python scripts/validate-anti-generic-visual.py <site-root> <VISUAL_QA_OBSERVATIONS.json> --json-out <visual-qa-score.json>
```

The validator combines source-level heuristics with rendered-review evidence. The minimum passing score is **75**. Horizontal overflow, unverified media provenance, or an unverified primary action are hard failures regardless of numeric score.

A failing score means revise and rerun. Do not waive the gate merely because the design looks attractive.

## 11. Design Critic gate

When the project has a `vault-build-plan.json`, copy `quality/DESIGN_CRITIC_OBSERVATIONS.template.json` to the target project as `DESIGN_CRITIC_OBSERVATIONS.json` and complete it from the rendered implementation.

For normal builds run:

```bash
python scripts/run-design-critic.py vault-build-plan.json DESIGN_CRITIC_OBSERVATIONS.json --json-out design-critic-result.json
```

For a benchmark build run:

```bash
python scripts/run-design-critic.py vault-build-plan.json DESIGN_CRITIC_OBSERVATIONS.json --benchmark-id <benchmark-id> --json-out design-critic-result.json
```

The Design Critic checks business specificity, task visibility, conversion truth, theme/section drift, component semantic correctness, keyboard/responsive verification, critical states, forbidden component substitutions, asset truthfulness, and subject-aware 3D execution. The minimum passing score is **80**, with hard failures overriding the score.

A build must fail the critic when it uses the wrong component semantics, contains unsupported business claims, presents generated media as real evidence, uses unplanned/unrelated 3D, lacks required mobile reachability, or violates benchmark-specific forbidden substitutions.

## 12. Revision loop

Create `VISUAL_QA_REPORT.md` with each finding, severity, viewport, evidence, fix, and verification status.

Use this loop:

1. Capture.
2. Inspect.
3. Record.
4. Complete structured observations.
5. Run the anti-generic QA gate.
6. Run the Design Critic when a build plan exists.
7. Fix blockers, component misuse, design drift, important issues, and generic-design signals.
8. Rebuild.
9. Recapture affected views.
10. Verify the fix did not create a regression.
11. Rerun both gates until they pass.

Do not stop after listing problems. Apply the corrections.

## 13. Handoff evidence

Provide:

- Final desktop and mobile screenshots.
- Key interaction screenshots.
- The exact URL tested.
- The exact commands run.
- Browser and viewport information.
- `VISUAL_QA_REPORT.md`.
- `VISUAL_QA_OBSERVATIONS.json`.
- Anti-generic visual QA score/result.
- `DESIGN_CRITIC_OBSERVATIONS.json` and `design-critic-result.json` when applicable.
- Known limitations.
- Any manual checks still required.

## Automatic rejection conditions

Reject the handoff when:

- No rendered screenshots exist.
- The anti-generic visual QA score is below 75.
- The Design Critic score is below 80 when the critic applies.
- A sticky header covers content.
- Mobile has overlap or horizontal overflow.
- Primary actions are obscured or broken.
- Required component semantics or states are wrong/missing.
- Product imagery is visibly inconsistent or inappropriate.
- Media provenance is not verified.
- The page relies on repeated stock or generated imagery.
- Important business information is missing.
- Generic AI copy or card soup remains.
- Motion has no reduced-motion path.
- Essential content depends on animation or JavaScript initialisation.
- 3D is used without a valid subject, user goal, interaction plan, and fallback.
- The agent claims a localhost URL that was not verified in the correct environment.
