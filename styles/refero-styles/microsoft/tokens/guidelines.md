# Guidelines

### Do
- Use #0067b8 as the sole chromatic color for all filled action buttons, link text, and active navigation indicators
- Set button border-radius to 2px - subtle rounding, not pill-shaped
- Apply the card shadow stack (rgba(0,0,0,0.13) 0 3px 7px + rgba(0,0,0,0.11) 0 1px 2px) only to product cards in grids
- Use Segoe UI weight 600 for headings, card titles, and button labels; weight 400 for all body, nav, and link text
- Maintain 8px as the base spacing unit - use 8/16/24/48px steps for padding, margins, and gaps
- Layer white overlay cards (32-48px padding, no border) over full-bleed hero photography for text legibility
- Keep card grids at 4 equal columns with 16-24px gaps inside a max-width 1200px container

### Don't
- Do not introduce additional brand colors - the system is monochrome plus #0067b8
- Do not use border-radius greater than 2px on buttons, inputs, or cards - keep edges nearly sharp
- Do not apply shadows to navigation bars, buttons, or text blocks - only to product cards
- Do not use Segoe UI weights other than 400 and 600 - no 300 whisper-weights or 700 bold declarations
- Do not create outlined or ghost button variants - all actions are filled blue or simple text links
- Do not add decorative gradients - the system relies on photography and flat surfaces
- Do not use fully saturated icons - category icons should be 1.5-2px stroke outline style in #616161 or #000000

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
