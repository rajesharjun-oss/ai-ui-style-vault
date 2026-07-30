# Guidelines

### Do
- Use the Aurora Lilac Deep Iris gradient (135deg) as the full-bleed background for hero sections, section transitions, and atmospheric dividers - never as a small accent or button fill.
- Set all display text at 47px with IvarHeadline Medium (serif) or Matter Medium/SemiBold (sans) with tracking between -0.015em and -0.025em - never set display copy at body sizes with display weight.
- Apply tabular numerals ('tnum') via font-feature-settings on all Matter text - it signals precision and is a non-negotiable brand mark.
- Use 0px border-radius on all components - cards, buttons, tags, frames. The sharp-cornered geometry is core to the system; rounding would undermine the architectural feel.
- Pair white text (#ffffff) on gradient/violet backgrounds, and Midnight Ink (#000000) on white surfaces - never use gray text on white for primary content.
- Use hairline borders (1px) in white on dark surfaces and Midnight Ink or Smoke Line (#cccccc) on light surfaces for structural framing.
- Maintain a 6px base unit for all spacing - derive all padding, margins, and gaps as multiples (12px, 18px, 23px, 36px).

### Don't
- Don't introduce additional colors to the palette - the system is achromatic + violet gradient. No green, blue, red, or warm accents outside the gradient.
- Don't use border-radius greater than 0px on any component - no rounded buttons, no pill tags, no curved cards. The sharp geometry is intentional.
- Don't set headings at weights above 600 (SemiBold) - the system relies on the Medium-to-SemiBold tier, not heavy/black weights.
- Don't apply drop shadows or elevation effects - the design uses flat surfaces with hairline borders for separation, never shadows.
- Don't use the gradient on small UI elements (buttons, badges, icons) - it belongs only on large atmospheric surfaces.
- Don't set body text below 14px or above 18px - the 14-18px range is the only readable zone for this system.
- Don't mix serif and sans within the same heading - choose IvarHeadline OR Matter for any single headline, not both.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
