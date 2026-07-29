# Guidelines

## Do

- Use 1440px border-radius for all buttons, badges, nav items, and pill-shaped interactive elements
- Use 10px border-radius exclusively for card and content containers pill = interactive, rounded-rect = content
- Set all text in uppercase using Pragmatica Cond at weight 400 never use bold, never use mixed case
- Apply -0.02em letter-spacing to all type sizes above 14px; -0.01em is acceptable for 15px body passages
- Define surfaces through background tonal shifts (#0b0b0b #272a2a #edebe7) and 1px hairline borders, never through box-shadow
- Reserve #cc6437 Ember Rust for hairline accent strokes and small text highlights only never use it as a fill
- Use Roboto Mono 11px exclusively for system data (news ticker, metadata, technical labels) to create a clear typographic register

## Do Not

- Do not introduce bold or semi-bold weights the entire system operates at weight 400 only
- Do not add drop shadows, glow effects, or any box-shadow values the system is intentionally flat
- Do not use color fills on buttons all interactive controls are ghost/outlined with 1px borders
- Do not use mixed-case text or sentence case in any UI label, heading, or body string
- Do not introduce additional accent colors Ember Rust is the only chromatic note permitted
- Do not use non-pill radii (e.g. 4px, 8px) on buttons, badges, or nav items the 1440px pill is the system's signature shape
- Do not use gradients the system is built on flat color fields and blurred photography, not color transitions

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
