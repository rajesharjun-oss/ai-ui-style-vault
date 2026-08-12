# Verification Notes

Verified on 2026-08-04 from the user-provided screenshot `WhatsApp Image 2026-08-04 at 3.06.07 PM.jpeg`.

Visible source signals:

- Title frame: hover expanding login.
- Login card with cyan/magenta neon frame, dark panel, username/password inputs, sign-in button, forgot password, and sign-up link.
- Visible CSS comment: `4-segment conic gradient on a rotating square`.
- Visible CSS values: `.box::before`, `position: absolute`, `inset: 50%`, `width: 170cqmax`, `height: 170cqmax`, `translate: -50% -50%`, `conic-gradient(from 0deg, ...)`, cyan `#35eaff`, magenta `#ff0a6c`, `filter: blur(1px) drop-shadow(0 0 12px #35eaff)`, and `animation: neon-rotate 5s linear infinite`.

Library upgrade:

- The screenshot only exposed the login face, but the visible `Sign up` control is implemented as a real explicit signup mode for library usefulness.
- The preview keeps expansion hover/focus triggered and prevents automatic auth-state movement.

Limit: only a screenshot and partial code frame were available, so this is a faithful reusable reconstruction of visible behavior and values, not a claim of full-source exactness.