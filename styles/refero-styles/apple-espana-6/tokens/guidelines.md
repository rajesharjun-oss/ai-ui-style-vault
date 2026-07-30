# Guidelines

### Do
- Use #0071e3 fill with #ffffff text and 9999px radius exclusively for the primary Buy action - never introduce a second chromatic button color
- Set display type at 56-80px in SF Pro Display weight 600 with -0.015em to -0.005em letter-spacing for all hero and section openers
- Apply 28px border-radius to every card, product viewer, and light surface container - this single radius defines the system's softness
- Compose body copy at 17px SF Pro Text weight 400 with 1.47 line-height and -0.022em tracking as the universal paragraph spec
- Maintain pure black (#000000) as the page canvas with no gradient or texture - let product photography provide all visual warmth
- Use rgba(66,66,69,0.72) with backdrop-filter blur(20px) saturate(1) for any floating UI element that must layer over photography
- Keep nav text at 80% white opacity (#cccccc equivalent) at 12px weight 400 - full-white nav feels aggressive against the black bar

### Don't
- Never use a second accent color beyond #0071e3 for actions - the blue is rationed, do not dilute it with green, orange, or purple CTAs
- Never add box-shadows to cards or buttons - the system defines elevation through color and radius alone, shadows would feel cheap
- Never use font-weight 700 anywhere - the system maxes at 600 because 700 reads as desperate on the negative tracking
- Never set headings below 28px - the scale starts at subheading 28px and goes up; small bold text is not in the vocabulary
- Never introduce a new radius below 10px for interactive elements - pills (9999px), cards (28px), and links (10px) are the only curves
- Never use color #0066cc as a button fill - it is link-text only; filling a button with it would confuse the action hierarchy
- Never add background gradients to text blocks or content sections - gradients are reserved for chip badges and decorative product imagery

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
