# Code Candy Hover Expanding Login

A dark hover/focus expanding auth card with a rotating cyan/magenta conic-gradient border and explicit login/signup switching.

## Use When

Use for cyber, developer-tool, gaming, AI, or experimental account screens that can support a theatrical auth entry without hurting usability.

## Agent Rules

- Expansion must be hover/focus triggered, not autoplayed.
- Click-away and `Esc` must collapse any sticky expanded state after a mode switch.
- The `Sign up` and `Already registered? Sign in` controls must actually switch states or navigate intentionally. Never leave them as dead links.
- Use real labeled inputs, secure backend auth, validation, rate limiting, CSRF/session protections, and safe error messages in production.
- Stop the neon rotation for reduced-motion users.
- Keep source-video headings and code-frame text out of preview UI.
- Do not use fake-only auth outside a clearly marked prototype.

## Files

- `index.html`: standalone design-only preview with login and signup modes.
- `pattern.json`: machine-readable library entry.
- `verification-notes.md`: screenshot/code-frame verification summary.