# Senior Product Team Protocol

Use this protocol whenever an AI agent designs or builds a website, web application, dashboard, internal tool, or app screen from this vault.

## Purpose

The protocol prevents an AI from jumping directly from a vague brief to styled JSX. It requires the agent to reason and deliver as a coordinated senior product designer, content designer, and front-end engineer.

## The Three-Lens Review

Every decision must survive three questions:

### Product-design lens

- What user problem does this solve?
- What is the primary task?
- What must be understood before action?
- What can be deferred?
- What states and edge cases exist?
- Does the hierarchy match risk and frequency?

### Content-design lens

- What is the minimum wording needed for confident action?
- Is the message specific to this product?
- Is information repeated?
- Can a visual, data point, component state, or progressive disclosure replace prose?
- Are labels clear without surrounding explanation?
- Does the copy fit realistic mobile layouts?

### Front-end engineering lens

- Is the pattern reusable and semantic?
- Are all states implemented?
- Is keyboard and screen-reader behavior correct?
- Does it survive long content and narrow screens?
- Is motion performant and reduced-motion safe?
- Can the implementation be maintained in the target stack?

A decision is not approved when one lens fails.

## Stage-Gate Workflow

### Gate 0 — Repository inspection

Inspect the target repository before proposing a visual system.

Record:

- Framework and package manager.
- Routing.
- Styling approach.
- Existing tokens and components.
- Existing accessibility and testing tools.
- Build, lint, typecheck, and test commands.
- Product terminology already present.
- Existing user roles and workflows.

Do not replace a working stack merely because another stack is fashionable.

### Gate 1 — Product frame

Complete these statements:

- The primary user is …
- They are trying to …
- The highest-risk failure is …
- The primary page or workflow outcome is …
- The single most important action is …
- Success is observable when …

If these cannot be stated plainly, do not begin page design.

### Gate 2 — Page inventory

For every page or major application state, define:

- Purpose.
- Primary audience.
- Entry point.
- Primary action.
- Secondary actions.
- Information needed before action.
- Information that can be deferred.
- Empty, loading, error, success, and permission behavior.

Avoid pages whose purpose is “show more information.” Be specific.

### Gate 3 — Content plan

Select a content-density mode and set budgets before writing final copy.

Default recommendation:

- Public product website: `balanced`.
- Luxury or highly visual launch page: `sparse`.
- Professional service information: `informational`, split across dedicated pages.
- Dashboard or internal tool: `data-dense`, with minimal explanatory prose.

Create a message hierarchy:

1. Outcome.
2. Evidence.
3. Action.
4. Supporting detail.
5. Optional depth.

Remove repeated messages before styling.

### Gate 4 — Reference selection

Select:

- One primary style bundle.
- One production-theme archetype.
- Page-specific screen references.
- One primary motion model when justified.
- Two to five motion primitives.

Reject a combination that mixes unrelated brand attitudes.

### Gate 5 — Design recipe

Complete `design-recipe.json`. It is the source of truth for:

- Product and audience.
- Content density.
- Visual tone.
- Layout density.
- Navigation model.
- Component inventory.
- State requirements.
- Motion model and intensity.
- Accessibility and performance constraints.
- Quality evidence.

### Gate 6 — Skeleton before decoration

Build and review a low-decoration structure first:

- Semantic landmarks.
- Navigation.
- Page headings.
- Content order.
- Forms and tables.
- Empty and error states.
- Mobile flow.

Do not use gradients, large illustrations, or complex animation to hide weak structure.

### Gate 7 — Token and component implementation

Implement:

1. Semantic colors.
2. Type scale.
3. Spacing scale.
4. Radius, border, and shadow rules.
5. Motion tokens.
6. Core components.
7. Application shell.
8. Page blocks.

Avoid local one-off values unless documented.

### Gate 8 — State completion

Before polishing, verify all relevant states:

- Loading.
- Empty.
- Error.
- Validation.
- Success.
- Disabled.
- Permission denied.
- Destructive confirmation.
- Retry/recovery.
- Long-running progress.

A page with only the ideal populated state is a mock-up, not a finished product.

### Gate 9 — Motion pass

Motion is added only after static hierarchy and states work.

For each animation, document:

- Communication purpose.
- Trigger.
- Duration and easing.
- Interruption behavior.
- Reduced-motion behavior.
- Mobile performance risk.

Delete motion that does not clarify anything.

### Gate 10 — Content compression pass

Review the rendered interface and ask:

- Can the hero support be shortened?
- Are two sections saying the same thing?
- Can a list become a diagram or interactive flow?
- Are cards carrying paragraphs that belong on detail pages?
- Are buttons clear without helper paragraphs?
- Does mobile show action before explanation?

The content plan is not finished until reviewed in the actual layout.

### Gate 11 — Quality evidence

Run automated checks and record:

- Lint.
- Typecheck.
- Tests.
- Build.
- Content/design validator.
- Asset scan.
- Desktop, laptop, and mobile review.
- Keyboard and focus review.
- Reduced-motion review.
- Long-content stress test.

## Decision Rules

### Add a section only when

- It answers a distinct user question.
- It supports a distinct decision.
- It provides evidence not available elsewhere.
- It introduces a new workflow or capability.
- It is required for trust, compliance, or conversion.

### Add a card only when

- The information is an independent object or action.
- The boundary improves scanning or comparison.
- The card has a meaningful state or interaction.

Do not use a card merely to place a border around text.

### Add motion only when

- It shows cause and effect.
- It connects states.
- It directs attention to a meaningful change.
- It demonstrates the product.
- It communicates progress or feedback.

### Add copy only when

- It reduces uncertainty.
- It enables a decision.
- It explains a non-obvious consequence.
- It establishes evidence or trust.
- It supports recovery from an error.

## Handoff Summary Format

Every final handoff should state:

- Product and primary user.
- Selected style and motion direction.
- Content-density mode and major reductions made.
- Pages and workflows completed.
- Components and states completed.
- Accessibility and responsive checks.
- Validation commands and results.
- Remaining risks or manual checks.
