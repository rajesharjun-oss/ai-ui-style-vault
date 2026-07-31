# Guidelines

### Do
- Use Greycliff weight 300 for any text 30px and above - the light weight is the brand's voice, not a fallback
- Maintain letter-spacing of -0.025em on display and heading sizes; let it relax to normal at body sizes
- Keep the palette monochromatic on the page surface - introduce the violet spark (#6d4aff) only in the wordmark icon, never as a button fill, border, or background
- Use 16px border-radius for all cards and image wells; use 9999px (full pill) for all buttons, tags, and avatars
- Apply the single shadow (rgba(30, 41, 59, 0.15) 0px 25px 50px -12px) only to the hero media well - do not propagate it to cards or modals
- Set body text to #334155 and nav/UI text to #475569 - reserve #0f172a for headings and the wordmark
- Use 8px and 16px for inline element gaps; jump to 48px or 64px between sections; never use 24px as a section gap

### Don't
- Do not introduce a second typeface - the system is single-family by design
- Do not use weight 700 on headings; weight 300 is the display treatment and weight 500-600 is the UI treatment
- Do not use a chromatic color as a button background, link color, or badge fill - the interface is intentionally colorless
- Do not add borders to cards that sit on #f2f3f5; let the white-on-plaster contrast do the work
- Do not center display headings - they are always left-aligned with the content column
- Do not use sharp corners (0-4px radius) on any surface - the system reads rounded or pill, never squared
- Do not stack multiple shadow layers or add glow effects - one shadow, used once, is the rule

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
