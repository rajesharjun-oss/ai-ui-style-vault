# Code Candy Floating Indicator Nav

A dark navigation bar with a green floating active indicator. It starts inactive and only moves after user selection.

## Use When

Use for mobile nav, bottom nav bars, compact app shells, dashboard section switches, and interaction-heavy product demos.

## Agent Rules

- Do not autoplay or cycle active states.
- Every segment must be clickable and keyboard operable with Enter or Space.
- Keep the active label readable and avoid hidden overlays intercepting clicks.
- Use `aria-label`, `aria-pressed`, or `aria-current` depending on the target app.
- Preserve reduced-motion behavior by moving instantly.

## Files

- `index.html`: standalone design-only preview.
- `pattern.json`: machine-readable library entry.
- `verification-notes.md`: source verification summary.