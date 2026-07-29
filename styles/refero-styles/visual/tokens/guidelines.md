# Guidelines

## Do

- Use the serif at 6496px weight 300 for all hero and section headlines the thin strokes at poster scale are the signature
- Set page background to #f6f6f4 and card surfaces to #ffffff the warm cream is non-negotiable, never use pure #ffffff as the page canvas
- Pair the neutral filled button (#2c2c26 fill, #ffffff text) with the ghost outline button (1px #000000 border) they always appear as a 2-button cluster with 8px gap
- Use mono at 1216px with tracking -0.067em for all UI text, nav, buttons, and body copy this creates the terminal/code-margin feel
- Separate sections with 80px vertical gaps, not with borders or background color shifts the whitespace is the structure
- Place the #fff347 accent as 24px strokes or small fill blocks (max ~120px wide), never as large fills or backgrounds
- Use 8px radius on cards and 3px radius on buttons, tags, and nav elements the radius contrast is deliberate

## Do Not

- Don't use pure #ffffff as the page background always #f6f6f4 for the warm cream canvas
- Don't add drop shadows to cards or buttons the system is intentionally flat, separation comes from 1px borders and color contrast
- Don't use the serif at body sizes (16px or below) it is a display-only face; body copy must be mono
- Don't apply #fff347 to text, large backgrounds, or filled buttons it is a decorative accent only, not an action color
- Don't use cool grays (blues or true neutrals) the entire palette runs warm: olive-sage tones, warm blacks (#2c2c26 not #000000 for surfaces), and cream whites
- Don't use gradients the system is flat color only, with the one exception of the 3D hero render which contains its own internal gradients
- Don't exceed 4 instances of #fff347 per screen the accent loses impact if it appears more than 34 times on a single page

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
