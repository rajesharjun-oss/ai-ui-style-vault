# Guidelines

### Do
- Use Bone (#f0f0f0) for all text on the dark void - never use pure white, which clashes with the warm off-white palette
- Apply 100px border-radius to every interactive button, badge, nav item, and avatar - the pill shape is the system's signature geometry
- Keep all type at Inter Display weight 400 - never introduce bold or semibold weights; build hierarchy through size and spacing only
- Use 0.04em letter-spacing on all text - this consistent positive tracking is what makes the whisper-weight type legible and gives the system its measured, deliberate feel
- Reserve Live Wire (#08ff00) exclusively for the availability status dot - it is the only chromatic color and must appear nowhere else
- Set page backgrounds to Void (#0f0f0f), not pure black - the near-black prevents OLED smearing and creates a subtle canvas depth
- Use 4px border-radius for image containers and 100px for all interactive elements - maintain the sharp/round duality

### Don't
- Don't introduce any new accent colors beyond Live Wire green - the system is deliberately monochromatic and any additional hue will break the gallery void
- Don't use drop shadows for card or surface elevation - depth must come from the artwork itself or surface tone shifts, not from shadow stacks
- Don't bold headlines or use weight 500+ - the entire type system breathes at weight 400; adding weight disrupts the flat, even texture
- Don't use sharp corners (<12px) on buttons, nav items, or badges - the pill geometry is the system's visual identity
- Don't use pure black (#000000) as a fill background for cards or surfaces - reserve it for hairline borders and edges; use Void (#0f0f0f) for surfaces
- Don't place body text below 14px or above 40px - the type scale is deliberately compressed; deviation breaks the editorial restraint
- Don't add gradients, glows, or color washes to UI elements - the system's visual energy comes from the 3D/photographic content, not from UI decoration

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
