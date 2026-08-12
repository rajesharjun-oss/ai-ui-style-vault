# Code Candy Interaction Gallery

Library-ready reconstructions of four public Code Candy motion snippets shared by the user.

This folder is a combined preview gallery. The reusable library entries live in separate folders:

- `../code-candy-auth-slanted-overlay/`
- `../code-candy-hover-pill-menu/`
- `../code-candy-floating-indicator-nav/`
- `../code-candy-auth-overlay-slide/`

## Included Patterns

- `code-candy-auth-slanted-overlay`: dark login/signup card with a slanted gradient overlay. State changes only when the visitor clicks `Create account` or `Sign in`.
- `code-candy-hover-pill-menu`: pill navigation where labels expand on hover or keyboard focus. No autoplay.
- `code-candy-floating-indicator-nav`: dark navigation bar with green circular indicator. Starts inactive; indicator appears and moves only after click.
- `code-candy-auth-overlay-slide`: light auth card with a clean two-panel overlay slide. State changes only on click; signup form stays readable.

## Agent Usage

Use these as interaction building blocks, not as page-level templates. Pull the behavior, timing, CSS values, and state model into the target product's own visual system.

Rules:

- Do not add autoplay to auth, nav, or menu state transitions.
- Keep login/signup transitions user-triggered and reversible.
- Remove TikTok/video headline text in production components.
- Keep visual previews design-only: do not show code blocks, snippets, or tutorial labels inside preview screenshots.
- Preserve reduced-motion handling in generated apps.
- Replace placeholder fields/icons with real accessible form controls when implementing inside an app.
- Do not store or copy TikTok videos; use the local code as the reusable artifact.

## Files

- `index.html`: combined component gallery with corrected non-autoplay behavior.
- `pattern.json`: gallery metadata pointing agents to the four standalone entries.
- `verification-notes.md`: what was source-video verified.