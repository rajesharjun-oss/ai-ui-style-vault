# Guidelines

### Do
- Use #000000 as the page background everywhere; let #131313 appear only when a true surface lift is needed without breaking the monochrome language.
- Set all interface text in Neue Haas Grotesk 55 Roman at weight 400 only, with font-feature-settings: 'case' on to keep all-caps forms typographically correct.
- Use only the four documented sizes - 11, 14, 18, 54 - to build hierarchy. No weights beyond 400.
- Use #ffffff for primary text, hairline rules, and the 1px borders that separate regions; use #afafaf only when a label must visibly step back.
- Keep all border-radius at 4px across buttons, cards, chips, and inputs - the system has one radius and it should not be overridden.
- Let product or editorial photography carry the visual weight; the chrome should be invisible. Frame hero imagery with a 1px white border on black.
- Separate major regions (announcement, nav, footer) with a 1px solid #ffffff hairline rule rather than background-color changes or padding alone.

### Don't
- Do not introduce any chromatic color - no brand accent, no semantic red/green/blue, no hover tint. The system is monochromatic by conviction.
- Do not use font-weight above 400, and do not add italic. Weight contrast is not available as a hierarchy tool.
- Do not use box-shadow, gradients, or glow effects. Surfaces are flat black; depth comes from hairline borders and photography only.
- Do not use border-radius larger than 4px. Pills, fully rounded shapes, and large curves are outside this system.
- Do not use backgrounds or fills on nav links, buttons in the main flow, or cart. The bordered chip is the only filled/bordered interactive shape, and it belongs only in the announcement bar.
- Do not underline links or change their color on hover. Text links are distinguished by position, context, and cursor only.
- Do not set type below 11px or use centered body copy. Small text is always uppercase, tight-leading, left-aligned in rows.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
