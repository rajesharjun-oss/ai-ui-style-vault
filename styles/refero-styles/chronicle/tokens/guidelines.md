# Guidelines

### Do
- Use #000000 or #050505 as the filled button background - never use a chromatic color for any interactive element
- Apply Diatype with letter-spacing -0.030em at 54px display and -0.023em at 32px headings; body text at 16px uses 0 tracking
- Alternate page sections between #ffffff and #f3f3f3 backgrounds to create rhythm without decorative elements
- Use 4px border-radius for all buttons, inputs, and tags; 8px for cards and image frames only
- Maintain 1px solid #e2e2e2 hairline borders on image frames and card edges - never use thicker strokes
- Reserve electric blue and any chromatic color strictly for rendered product UI content inside frames, never in navigation, buttons, or backgrounds
- Use the single shadow token (rgba(5,5,5,0.08) 0px 2px 24px 0px) only for white cards sitting on gray surfaces - no shadow on white-on-white

### Don't
- Never introduce a brand color (blue, purple, green) into navigation, buttons, section backgrounds, or typography - the UI is intentionally achromatic
- Never round buttons or inputs beyond 4px - pill-shaped buttons would break the editorial typographic register
- Never use font weights above 500 - Diatype at 400/500 is the full weight range; heavier weights crush the mechanical letterform quality
- Never stack more than two type sizes within a single content block without re-establishing hierarchy through #6b6b6b muted color rather than additional size steps
- Never apply more than one shadow elevation level - the system uses a single subtle card shadow; adding layered shadows introduces unwanted depth
- Never center-align body paragraphs or subheadings - all text below headline level is left-aligned
- Never use #b3b3b3 or #929292 as text colors for meaningful content - these tones exist only for disabled states and decorative separators

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
