# Component and State Standard

## Purpose

A premium UI library is defined by consistent behavior and complete states, not only attractive default screenshots.

Use `system/component-manifest.json` as the machine-readable contract.

## Foundation Components

The initial production set must cover:

- Button.
- Icon button.
- Button group.
- Input.
- Textarea.
- Select.
- Combobox.
- Checkbox.
- Radio group.
- Switch.
- Date picker.
- File upload.
- Search input.
- Form field.
- Card.
- Metric card.
- Chart card.
- Table/data-grid shell.
- Tabs.
- Accordion.
- Tooltip.
- Popover.
- Dropdown menu.
- Command palette.
- Dialog.
- Drawer.
- Toast.
- Banner.
- Badge.
- Avatar.
- Pagination.
- Breadcrumb.
- Navbar.
- Sidebar.
- Page header.
- Empty state.
- Error state.
- Skeleton.
- Progress.
- Stepper.

## Universal Interaction States

Interactive components should define, when relevant:

- Default.
- Hover.
- Focus-visible.
- Pressed/active.
- Selected.
- Disabled.
- Read-only.
- Loading.
- Success.
- Warning.
- Error.

The visual difference between states must be perceivable without depending on color alone.

## Page and Data States

Every data-driven page should consider:

- First use/no data.
- Filtered no results.
- Loading.
- Partial loading.
- Failed load.
- Stale data.
- Offline/reconnecting.
- Permission denied.
- Empty due to scope or date.
- Success/completed.
- Archived/deleted.

## Button Contract

A button must define:

- Primary, secondary, quiet/ghost, and destructive intent where needed.
- Text and icon-only forms.
- Loading behavior that preserves width.
- Disabled and permission-denied behavior.
- Keyboard activation.
- Focus-visible state.
- Press feedback.
- Clear accessible name for icon-only controls.

Avoid more than one primary button in a local decision area.

## Form Field Contract

A field must support:

- Label.
- Required/optional indication.
- Help text.
- Error message.
- Success or verified state where useful.
- Disabled.
- Read-only.
- Loading or async validation where relevant.
- Character count where relevant.
- Accessible association among label, description, and error.

## File Upload Contract

The upload pattern must include:

- Accepted file types and size.
- Browse and drag/drop where useful.
- Keyboard-accessible input.
- Selected-file review.
- Upload progress.
- Processing state.
- Validation error.
- Processing failure and retry.
- Remove/replace action.
- Privacy or retention explanation when important.

## Table/Data Grid Contract

The table must define:

- Column labels and alignment.
- Sorting.
- Filtering.
- Search.
- Selection.
- Bulk action.
- Pagination or virtualization.
- Loading.
- Empty.
- Filtered empty.
- Error/retry.
- Responsive strategy.
- Row detail.
- Keyboard and screen-reader behavior.

## Modal and Drawer Contract

- Move focus into the surface.
- Trap focus only while open.
- Restore focus on close.
- Close using escape unless unsafe.
- Provide a clear title.
- Do not hide critical consequences.
- Prevent accidental dismissal during irreversible or long-running action when necessary.
- Use a drawer for contextual detail and a dialog for bounded decisions.

## Toast and Banner Contract

- Toasts are transient feedback, not the only place for critical errors.
- Banners communicate persistent page or system status.
- Include recovery action when possible.
- Announce status accessibly.
- Avoid stacking many simultaneous toasts.

## Empty-State Contract

Differentiate:

- First-use empty: explain value and primary setup action.
- Filtered empty: explain filters and offer reset.
- Permission empty: explain access and next step.
- Error empty: explain failure and retry.
- Completed empty: confirm there is no remaining work.

## Error-State Contract

An error state should contain:

- Specific failure.
- Impact.
- Recovery action.
- Preservation of user work when possible.
- Support or diagnostic path when recovery fails.

Avoid “Something went wrong” as the complete experience.

## Component Visual QA

Preview each component with:

- Short and long content.
- Light and dark theme when supported.
- Keyboard focus.
- Disabled and loading state.
- Validation/error state.
- Mobile width.
- Reduced motion.
- High zoom.

## Component Acceptance Criteria

A component is not production-ready when:

- Only the default state exists.
- Focus is invisible.
- Long content clips unexpectedly.
- Loading causes major layout shift.
- Disabled state is indistinguishable or unexplained.
- Error behavior is missing.
- Mobile behavior is undefined.
- Animation is required to understand content.
- Accessible name, role, or relationship is missing.
