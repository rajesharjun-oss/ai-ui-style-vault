# Code Candy Auth Slanted Overlay

A dark premium login/signup interaction with a slanted gradient overlay. The state changes only when the visitor clicks `Create account` or `Sign in`.

## Use When

Use for SaaS, membership, portfolio, or premium product account screens that need a memorable auth transition without autoplay.

## Agent Rules

- Keep the transition click-triggered and reversible.
- Use real form controls, labels, validation, secure backend auth, CSRF/session protections, and rate limits in production.
- Do not ship fake auth or rely on frontend-only checks.
- Do not include source-video headline text or code snippets inside the visual UI.
- Preserve reduced-motion behavior by switching states instantly.

## Files

- `index.html`: standalone design-only preview.
- `pattern.json`: machine-readable library entry.
- `verification-notes.md`: source verification summary.