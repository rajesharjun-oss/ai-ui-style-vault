# Fast-Casual Commerce Accessibility and Responsive Standard

Restaurant ordering is a time-sensitive task. Accessibility, mobile behaviour, and recovery are core commerce requirements, not optional polish.

## Baseline

Target WCAG 2.2 AA unless the project documents a stronger requirement.

The full journey must work with:

- Keyboard only.
- Screen reader.
- 200% browser zoom and text enlargement.
- Touch input.
- Reduced motion.
- High contrast or forced colours where practical.
- Slow network and interrupted requests.

## Branch and fulfilment context

- Announce the current branch and fulfilment mode.
- Make changes available without forcing geolocation.
- Explain the effect of changing branch, address, or fulfilment before recalculating the cart.
- When cart items become invalid, preserve valid items and move focus to a clear conflict summary.
- Do not rely on map interaction as the only way to choose a branch or address.

## Category navigation

- Use navigation, tab, or link semantics appropriate to actual behaviour.
- Preserve visible focus and selected state.
- Ensure sticky category rails account for the primary header and anchor offset.
- On mobile, support touch scrolling without preventing page scroll.
- Provide a way to reach offscreen categories with keyboard.
- Do not use colour alone to show the selected category.

## Product cards

- Associate image, name, description, price, availability, and action.
- Action labels should identify the product when context is ambiguous.
- Do not rely on hover for price, modifiers, or availability.
- Keep logical reading order when visual layout changes.
- Provide stable skeletons that do not announce every decorative placeholder.

## Product customiser

- Use a route, dialog, or sheet with correct semantics and focus management.
- Label required option groups programmatically.
- Use fieldset and legend or equivalent grouping for related choices.
- Announce price changes politely; do not interrupt every selection.
- On validation, focus the first unresolved required group and summarise all errors.
- Preserve valid choices when one modifier becomes unavailable.
- Ensure the mobile action bar never covers the final option, error, or browser safe area.
- Support Escape or Back behaviour without losing selections unexpectedly.

## Cart

- Announce material item-count and total changes politely.
- Provide specific edit and remove labels.
- Removal should have confirmation or undo appropriate to the risk.
- Keep recalculation and conflict messages close to affected items and in a summary.
- Do not move focus unpredictably when quantities change.
- When an asynchronous update fails, restore the previous verified quantity and explain recovery.

## Checkout

- Use persistent labels; placeholders are examples, not labels.
- Group contact, fulfilment, address, payment, and consent logically.
- Associate errors with fields and provide an error summary.
- Preserve valid data after payment or network failure.
- Prevent duplicate place-order submission.
- Announce payment-pending state and provide a safe status-check path.
- Do not mark the order complete until a verified order identifier is available.
- Make terms, fees, minimums, and total available before submission.

## Order status

- Use text and ordered structure, not animation alone.
- Mark the current status programmatically.
- Show timestamps and estimates only when verified.
- Provide support for delayed, cancelled, tracking-unavailable, and failed states.
- A map is supplementary; current status must remain understandable without it.

## Responsive transformations

Design these layouts intentionally:

### Wide desktop

- Product grid may use 3–5 columns depending on card content and image quality.
- Cart may be a stable side panel when it does not reduce menu usability.
- Customiser may use two regions.

### Laptop

- Reduce grid columns before compressing content.
- Verify sticky header, category rail, and cart summary do not stack into an oversized fixed area.
- Test 1280×800 specifically.

### Tablet

- Prefer 2–3 product columns.
- Use full-height cart or customiser overlays when side panels become narrow.
- Keep touch targets and text size stable.

### Mobile

- Use one or two product columns based on content; do not force two columns when names, prices, or actions wrap poorly.
- Use full-screen customiser, cart, branch selector, and address flows when needed.
- Keep one primary sticky action at a time.
- Respect `env(safe-area-inset-bottom)`.
- Prevent horizontal overflow at 320 CSS pixels and above.
- Do not merely shrink desktop navigation or checkout.

## Sticky and fixed elements

- Define header and category offsets as tokens.
- Apply `scroll-margin-top` to anchored sections.
- Test browser zoom, mobile software keyboard, orientation changes, and dynamic browser chrome.
- Fixed cart or checkout actions must not cover content, cookie controls, errors, or system navigation.
- Provide non-sticky fallback when viewport height is too small.

## Reduced motion

- Preserve selection, cart, validation, and order-status meaning without movement.
- Replace animated cart flights with immediate count and status feedback.
- Remove parallax and large spatial transitions.
- Do not animate order progress independently of verified status.
- Use brief opacity changes only when helpful.

## Live-region guidance

Use polite announcements for:

- Item added.
- Cart quantity or total updated.
- Coupon result.
- Address eligibility.
- Modifier or product availability change.
- Order status change.

Use assertive announcements only for blocking errors or safety-critical state. Avoid announcing every price recalculation keystroke.

## Responsive and accessibility QA

Test at minimum:

- 1440×1000.
- 1280×800.
- 768×1024.
- 390×844.
- 320×568 where practical.
- 200% zoom.
- Keyboard-only menu, customiser, cart, checkout, and branch selection.
- Screen-reader labels, groups, errors, status, and totals.
- Reduced motion.
- Offline or failed-request recovery.
