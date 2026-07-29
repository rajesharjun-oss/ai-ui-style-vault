# Guidelines

### Do
- Set all display sizes (48px and above) in Onest weight 200-300 - the whisper-weight headline is the brand's editorial signature
- Use letter-spacing in negative em values across the entire type scale, tightening to -0.091em at 152px display
- Reserve Ember Orange (#f15730) for filled buttons and Tangerine Blaze (#f7651a) for entire promotional surfaces; never mix them in the same component
- Use Apricot Whisper (#ff8562) for 1-2px hairline borders on cards and link underlines - not for fills
- Apply 600px border-radius to every button and 30px to every input - the pill is non-negotiable for actions
- Default card corners to 10px and product image corners to 15px
- Use Mist Gray (#eeeeee) for borders only on white surfaces where Graphite would feel too heavy

### Don't
- Don't apply box-shadows to cards, buttons, or modals - the system communicates depth with borders and color alone
- Don't use Orange for body text - its contrast on white fails accessibility, keep it for fills, borders, and large display numbers only
- Don't use weights 600-800 for body text or UI labels - reserve them for the rare emphasis moment
- Don't introduce a second accent color or hue - the orange must remain the single chromatic note
- Don't use 0px or 4px border-radius on cards or images - the 10px/15px minimum is part of the soft editorial feel
- Don't center product card text - left-align all UI copy; centering is reserved for the hero overlay and modal content
- Don't apply gradients to surface fills - the only observed gradient is a single progress-bar indicator on a dark surface

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
