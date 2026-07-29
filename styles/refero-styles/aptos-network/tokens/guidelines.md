# Guidelines

### Do
- Use Season Serif for all text - there is no secondary typeface. Weight 335-340 for display 55px+, weight 400-420 for body and UI, weight 420-444 for emphasis.
- Apply -0.030em letter-spacing to any type 90px or larger. Positive tracking (+0.01em) only at 9px caption size. Body text uses normal tracking.
- Use full-bleed color section backgrounds (Sage, Warm Stone, Soft Sand, Powder Blue) at 90-150px vertical padding. Never constrain sections to a max-width background.
- Draw all dividers as `inset 0 0 0 1px {color}` box-shadows, not as border properties. Rotate colors: Ink, Soft Sand, Powder Blue.
- Use 9999px radius for all buttons, nav container, and tags. Use 0px radius for all other surfaces (cards, code panels, inputs).
- Enable `font-feature-settings: "calt"` on all Season Serif text - contextual alternates are part of the brand voice.
- Split every section into left text / right decoration at roughly 55/45. Text left-aligns; decorative striped panel occupies the right.

### Don't
- Do not use any sans-serif typeface. Season Serif carries everything, including buttons, nav, and code labels.
- Do not use drop shadows. The system is flat by design - all line work is 1px inset.
- Do not use border-radius on cards, panels, code blocks, or images. Only buttons and the nav pill are rounded (9999px).
- Do not use bright or saturated colors. Every chromatic value is muted: sage, khaki, sand, powder blue. Saturation above 40% breaks the system.
- Do not use smooth gradients. The decorative right-side panels are hard-edge striped patterns implemented with sharp linear-gradient color stops.
- Do not use standard font weights (300, 400, 700). Season Serif uses fractional weights (335, 340, 420, 444) - pick from the available scale.
- Do not place text on both halves of a split section. The right side is always decorative (striped pattern or code panel), never text.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
