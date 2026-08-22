# Canonical Component Intelligence Standard

Component Gallery is used as a cross-design-system taxonomy and comparison layer, not as a screenshot/template source. HeroUI is one implementation source among many and is preferred for React projects only when its behavior and dependency profile fit the target repository.

## Selection sequence

1. Resolve the user's term or alias to one of the 60 canonical component families in `component-catalog.json`.
2. Read `contract-rules.json` and resolve the component's interaction archetype.
3. Apply the universal semantic, state, keyboard, accessibility and responsive requirements.
4. Check the critical distinctions before choosing a visually similar alternative.
5. If HeroUI has a compatible primitive, read `references/heroui-v3/behavior-contracts.json` and the relevant upstream package/test evidence.
6. If HeroUI does not fit, implement the canonical behavior contract using the target stack or another appropriately licensed design system.
7. Restyle the component through the selected Vault production theme/domain pack; do not import another system's brand expression by default.
8. Render and test realistic content, keyboard interaction, focus, error/loading/empty states, 200% zoom and narrow mobile widths.

## Cross-system comparison priorities

When comparing examples from Component Gallery, weight evidence in this order:

- semantics and task fit;
- accessibility and keyboard behavior;
- state completeness and recovery;
- content and labeling guidance;
- responsive behavior;
- API/composition clarity;
- implementation-stack fit;
- visual styling.

A design system with strong accessibility and usage guidance is more valuable to the Vault than a visually attractive example with no documented behavior.

## Non-interchangeable patterns

The following pairs must be treated as different interaction contracts even when they look similar:

- Button / Link
- Select / Dropdown menu
- Tooltip / Popover
- Alert / Toast
- Tabs / Segmented control
- Spinner / Progress bar
- Accordion / Tree view
- Modal / Popover
- Checkbox / Radio button
- Combobox / Select

The full distinction text is machine-readable in `contract-rules.json`.

## HeroUI integration

HeroUI contributes implementation-level evidence for React projects: React Aria semantics, compound composition, data-state styling, controlled overlays, keyboard interaction, selection/sorting behavior, validation states and SSR-sensitive tests. Use `resolve-component-contract.py` to combine Component Gallery taxonomy with HeroUI behavior contracts.

Example:

```bash
python scripts/resolve-component-contract.py autosuggest
python scripts/resolve-component-contract.py "dropdown menu"
python scripts/resolve-component-contract.py table --compact
```

## Rights and provenance

Component Gallery examples may point to many independent design systems with different licenses. Do not infer reuse permission from being listed in Component Gallery. Use the Gallery for taxonomy, aliases, counts and comparative UX research; check the originating system before copying source. Do not vendor screenshots, logos, proprietary content or exact brand compositions.
