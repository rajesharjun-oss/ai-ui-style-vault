# Code Candy Auth Overlay Slide

A clean light login/signup interaction where an overlay slides between sign-in and create-account panels on explicit click.

## Use When

Use for creator tools, workspace onboarding, account portals, and light product experiences that need a clear auth switcher.

## Agent Rules

- Keep create-account and sign-in forms visible, reachable, and unclipped in both states.
- Do not autoplay between states.
- Avoid vertical seam artifacts by sizing and translating the overlay deliberately.
- Use real form controls, validation, secure backend auth, CSRF/session protections, and rate limits in production.
- Preserve reduced-motion behavior by switching sides instantly.

## Files

- `index.html`: standalone design-only preview.
- `pattern.json`: machine-readable library entry.
- `verification-notes.md`: source verification summary.