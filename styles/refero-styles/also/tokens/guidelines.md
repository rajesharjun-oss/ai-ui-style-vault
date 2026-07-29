# Guidelines

### Do
- Set all buttons and tags to 9999px radius - the pill is non-negotiable across every variant (primary, dark, green, ghost).
- Use the single Shadow Plum (#48316a) 2px solid hard shadow on every elevated element - never use blur, never stack shadows, never change the offset.
- Use Electric Violet (#ac74fc) for links, active states, icon highlights, and section borders - it is the signal color and should appear in functional roles, not decoration.
- Set SerialC-Heavy labels in uppercase with positive tracking (0.036-0.063em) - never use it in mixed case or tight tracking.
- Push ABCCameraPlainVariable line-heights tighter as size grows: 1.5 at body, 1.0 at heading-lg, 0.93 at display - the system is defined by compression at scale.
- Maintain 8px base unit spacing: 16px element gap, 24px card padding, 80px section gap - never break to a 4px or 12px base.
- When a section flips to Electric Violet (#ac74fc) background, keep the same component structure, shadows, and type system - only the canvas color changes.

### Don't
- Never use soft drop shadows with blur - the 2px solid hard shadow is the only shadow in the system.
- Never use Pure White (#ffffff) as page canvas - always start from Cream Paper (#fcf7fa); white is reserved for cards and elevated surfaces.
- Never set ABCCameraPlainVariable with positive letter-spacing on body or heading text - the system compresses at scale, it does not expand.
- Never use rounded corners on product images, story cards, or hero photography - these are sharp-edged; only buttons, inputs, and feature cards get radius.
- Never add a second chromatic accent - Electric Violet is the system; Acid Lime and Signal Blue are rare utility colors for specific states only.
- Never use a different shadow color - Shadow Plum (#48316a) stays constant even on dark or green buttons, keeping the brand cohesive across all CTA variants.
- Never set SerialC-Heavy in lowercase or sentence case - it is an uppercase-only typeface in this system; using it otherwise breaks the typographic rhythm.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
