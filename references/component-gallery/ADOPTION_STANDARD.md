# Component Gallery Adoption Standard

## Purpose

Use Component Gallery as a cross-design-system research layer for component semantics, terminology, variants and implementation discovery. It is not a source to clone screenshots or a substitute for checking the license and guidance of the originating design system.

## Required reasoning order

1. Identify the user task and interaction need.
2. Resolve the canonical component family and aliases from `component-catalog.json`.
3. Distinguish visually similar but behaviorally different controls, especially button vs link, select vs dropdown menu, tooltip vs popover, tabs vs segmented control, accordion vs tree view, spinner vs progress bar, and alert vs toast.
4. Determine required states, keyboard behavior, labels, focus, validation and recovery.
5. Review multiple design-system examples when the interaction is consequential or ambiguous.
6. Prefer an existing compatible accessible primitive when one exists.
7. If using HeroUI, run `scripts/select-heroui-components.py` and preserve the React Aria behavior contract while restyling through vault tokens.
8. If no compatible primitive exists, implement the behavior contract using semantic platform primitives or another verified accessible library.

## Cross-system synthesis rule

Do not average visual styles across many systems. Cross-system research is for discovering stable behavior, naming, state and accessibility conventions. The target business/domain pack and selected vault theme still control visual direction.

## Required component contract

For every consequential component record:

- canonical component family;
- aliases encountered in the brief or source systems;
- user task;
- trigger and dismissal behavior where relevant;
- selection model where relevant;
- keyboard behavior;
- focus behavior;
- accessible name/description requirements;
- required states;
- validation/recovery behavior;
- responsive transformation;
- content constraints;
- chosen implementation primitive;
- fallback or no-JavaScript behavior where relevant;
- source and license notes.

## Important distinctions

### Button vs link

Use a button for an action in the current application context. Use a link for navigation to a resource or location. Do not style one as the other without preserving semantics.

### Select vs dropdown menu

A select changes a form value from predefined options. A dropdown menu exposes commands or navigation. Similar visual treatment does not make their behavior interchangeable.

### Tooltip vs popover

A tooltip is concise supplementary information and must not contain essential interactive workflow. A popover can contain interactive contextual content and needs explicit focus/dismissal behavior.

### Tabs vs segmented control

Tabs navigate among related content panels. Segmented controls switch a small set of modes or values. Choose based on information architecture, not appearance.

### Alert vs toast

An alert communicates important state or feedback in the content flow. A toast is transient layered feedback. Critical information must not depend solely on a disappearing toast.

### Spinner vs progress bar

Use a spinner when progress is indeterminate. Use a progress bar when completion can be measured. Never show fake percentage progress.

### Accordion vs tree view

Accordion items disclose sibling content regions. A tree represents nested hierarchical structure and has a different navigation/selection model.

## Visual anti-patterns

- Do not use cards for every component family.
- Do not replace semantic controls with clickable `div` elements.
- Do not use tooltips as a substitute for labels.
- Do not use disabled controls without explaining recovery when the reason is not obvious.
- Do not use placeholder text as the only field label.
- Do not hide validation until submission when earlier feedback is useful.
- Do not force desktop table behavior onto narrow screens without a deliberate strategy.
- Do not create decorative progress indicators that imply work is occurring when it is not.

## Licensing

Component Gallery links to many independent design systems. Always follow the license of the originating system before reusing code or assets. Component Gallery metadata and screenshots are reference material; never assume an example's code or visual assets are freely reusable just because it is listed in the gallery.
