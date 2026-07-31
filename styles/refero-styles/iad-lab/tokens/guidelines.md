# Guidelines

### Do
- Use #f8f8f8 for all text and borders; #222222 is the only background. This binary is the system.
- Apply 20px border-radius to any rounded element - buttons, tags, chips, containers. Never use sharp corners on interactive surfaces.
- Set the display heading to overflow the viewport. The wordmark must bleed past both left and right edges - if all letters are fully visible, it is too small.
- Use Neue Haas Unica weight 400 as default; reserve weight 700 for active or emphasized labels only. Do not mix intermediate weights.
- Separate list items with 1px solid #f8f8f8 bottom borders. This hairline divider is the primary structural separator in the system.
- Use 24px as the default element gap and 16px as the tight gap. Maintain the 4px base unit for all spacing decisions.
- Let photography fill 100vw with zero padding or border-radius. Full-bleed is non-negotiable for visual panels.

### Don't
- Do not introduce any color beyond the four neutrals (#222222, #f8f8f8, #2a2b2d, #757577). Chromatic accents are forbidden.
- Do not add drop shadows, gradients, or glow effects. Elevation is communicated through photography scale, not CSS shadows.
- Do not add a traditional navigation bar, header, or footer chrome. The meta label and dot navigation are the entire structural frame.
- Do not center text in narrow columns. Text should be short, left-aligned, and surrounded by generous negative space.
- Do not use border-radius values other than 15px or 20px. Avoid 4px, 8px, or fully rounded (9999px) - neither matches the system's geometric language.
- Do not set the display heading at a size where all letters fit within the viewport. The cropping is intentional and defines the visual identity.
- Do not use line-height above 1.35 for body text or below 1.10 for headings. The tight heading leading creates the architectural feel.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
