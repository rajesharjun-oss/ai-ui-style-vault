# Guidelines

### Do
- Use #266df0 (Cobalt Core) as the single accent for all interactive highlights, active states, and link text - never introduce additional saturated colors
- Set display headlines in InterDisplay weight 600 at 40-64px with tracking -0.015em to -0.02em and line-height 1.0-1.1
- Use 10px border-radius for all buttons and inputs, 7px for tags and badges, 11-14px for cards
- Apply blue-tinted shadows at very low opacity (rgba(28, 40, 64, 0.04) to rgba(28, 40, 64, 0.1)) - never use warm-gray or pure-black shadows
- Use Inter weight 500 as the default UI weight, not 400 - the slightly heavier weight is the system's default voice
- Activate 'ss03' on all Inter and InterDisplay text for the alternate geometric character
- Keep the max-width at 1440px and maintain 80-120px vertical gaps between major sections

### Don't
- Don't use rounded buttons with radius above 12px - the 10px radius is part of the system identity
- Don't introduce secondary accent colors, gradients on buttons, or decorative color - one blue accent is the rule
- Don't use TiemposText for anything other than testimonial pull-quote headings - the serif/sans contrast is earned by rarity
- Don't use Inter weight 400 as a default - weight 500 carries the UI voice
- Don't apply shadows warmer than rgba(28, 40, 64, ...) - the blue-tinted shadow is deliberate, not neutral
- Don't use letter-spacing wider than 0 for body or heading text - the system is consistently tight-tracked
- Don't place the cobalt accent on filled backgrounds in body copy - it belongs to links, icons, and small interactive moments

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
