# Front-End Implementation Standard

## Goal

Translate the selected design and content system into maintainable, accessible, responsive, performant production UI.

## Implementation Order

1. Inspect and preserve target-repo conventions.
2. Create or map semantic design tokens.
3. Build app shell and layout primitives.
4. Build reusable controls and data components.
5. Compose pages from components.
6. Implement states and validation.
7. Add responsive transformations.
8. Add purposeful motion.
9. Run content and visual compression passes.
10. Run quality checks.

## Semantic Tokens First

Do not style pages directly from copied brand hex values. Translate selected references into semantic roles:

- `background`
- `surface`
- `surface-muted`
- `surface-elevated`
- `text-primary`
- `text-secondary`
- `text-muted`
- `border`
- `border-strong`
- `accent`
- `accent-contrast`
- `success`
- `warning`
- `danger`
- `info`
- `focus-ring`

Also define:

- Type roles.
- Spacing scale.
- Radius scale.
- Border treatment.
- Shadow levels.
- Container widths.
- Motion durations and easing.
- Layer/z-index map.

## Component Architecture

- Separate behavior from visual variants when practical.
- Prefer composition over large prop-driven “do everything” components.
- Keep page-specific data and business logic outside low-level visual primitives.
- Use shared field wrappers for label, help, error, required, and disabled semantics.
- Use variants linked to semantic intent, not arbitrary color names.
- Document escape hatches.

## Accessibility Baseline

- Use semantic HTML landmarks and headings.
- Maintain one logical `h1` per page view.
- Give controls accessible names.
- Associate labels and descriptions with inputs.
- Preserve keyboard navigation and expected shortcuts.
- Show visible focus using `:focus-visible`.
- Manage focus for dialogs, drawers, menus, and route changes.
- Do not rely on color alone for status.
- Provide sufficient contrast.
- Announce asynchronous status and form errors where needed.
- Ensure touch targets are usable.
- Respect zoom and text resizing.

## Responsive Standard

Review at minimum:

- 1440×1000 or wider.
- 1280×800.
- Approximately 390×844.

Also stress test:

- 320px width where product support requires it.
- 200% zoom.
- Long headings and labels.
- Large data values.

Define mobile behavior explicitly for:

- Navigation.
- Tables.
- Side panels.
- Dialogs and drawers.
- Sticky actions.
- Charts.
- Multi-column forms.
- Product demonstrations.

## Data Tables

A professional table should define:

- Sort.
- Filter.
- Search.
- Pagination or virtualization.
- Loading skeleton.
- Empty and filtered-empty states.
- Error and retry.
- Row selection.
- Bulk actions.
- Column priority on mobile.
- Horizontal overflow strategy.
- Sticky header behavior.
- Accessible row and column labels.
- Large-number alignment and formatting.

Do not make every table row a heavily rounded card on desktop unless the data model justifies it.

## Forms

- Keep labels persistent.
- Use placeholders as examples, not labels.
- Validate at an appropriate time.
- Keep messages near the field and summarize when necessary.
- Preserve user input after recoverable failures.
- Disable submission only when the reason is clear.
- Show progress for long-running operations.
- Prevent duplicate submission.
- Make destructive consequences explicit.

## Loading and Async Work

Choose the state based on duration and context:

- Immediate control feedback for short operations.
- Skeletons for stable content layout.
- Progress for known or meaningful duration.
- Background status for work users can leave.
- Clear retry and retained context on failure.

Do not use an indefinite spinner without context for long-running analysis or uploads.

## Motion Engineering

Use the smallest suitable tool:

- CSS transitions/keyframes for hover, focus, reveal, menu, and simple loading.
- Motion for React for component state and shared-layout transitions.
- GSAP for justified timeline or scroll choreography.
- Lottie/dotLottie for licensed vector animation.
- Rive for accessible state-machine-driven animation.
- Three.js for a genuinely primary 3D experience with static fallback.

Rules:

- Prefer transform and opacity.
- Avoid layout thrashing.
- Lazy-load offscreen media and animation.
- Use poster/fallback assets.
- Stop or simplify decorative loops for reduced motion.
- Keep core content readable before, during, and after animation.
- Do not mix libraries without a documented reason.

## Performance Baseline

- Avoid blocking first paint with large media or animation bundles.
- Compress and size images correctly.
- Use responsive images where relevant.
- Lazy-load below-the-fold media.
- Avoid shipping a heavy animation library for one fade.
- Prevent cumulative layout shift.
- Test mobile CPU/GPU behavior.
- Split rarely used routes or editor modules.
- Keep third-party scripts deliberate.

## Content in Components

- Components must survive realistic copy.
- Do not clip or hide essential text to preserve a mock-up.
- Use line clamp only where the full content is accessible elsewhere.
- Avoid fixed heights for variable content unless overflow behavior is designed.
- Use `min-width: 0` and appropriate wrapping in flex/grid layouts.
- Test long localization-like strings.

## Styling Discipline

Avoid defaulting to:

- Gradient-filled identity.
- Backdrop blur on every surface.
- Large shadows everywhere.
- 24–32px radii on every component.
- Pill shape for all buttons and tags.
- Excessive floating elements.
- Same card grid in every section.

These techniques are allowed when selected by the design recipe and applied with restraint.

## Engineering Handoff

Document:

- Stack and architecture decisions.
- Token mapping.
- Component inventory.
- State coverage.
- Responsive transformations.
- Motion library and fallbacks.
- Accessibility checks.
- Performance risks.
- Commands run and results.
