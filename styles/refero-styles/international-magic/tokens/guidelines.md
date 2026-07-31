# Guidelines

### Do
- Keep every screen fully achromatic - palette is Void, Chalk, and three mid-grays; no chromatic accents.
- Center all content in a 640px column and let 120px of Void separate every section.
- Use the 24px radius on any container that holds a piece of work (device, video, image), and 9999px radius on any tag, badge, or button.
- Lift featured work with the single ambient shadow `0px 64px 72px 0px rgba(0,0,0,0.25)` - never stack a second tier.
- Set display headlines at 96px / weight 400 / letter-spacing -1.632px; the whisper weight is the brand.
- Use `ordn` and `ss01` font features wherever Wand UI Pro appears - they are part of the voice.
- Treat the top bar as a sentence, not a bar: three words, 11px / 550, no background, no border.

### Don't
- Don't introduce any hue - no blue, no red, no warm grays with chroma. The page is 0% colorful by design.
- Don't add a filled primary-color CTA. Actions stay ghost (outlined Ivory) or neutral-charcoal.
- Don't use sharp 0-4px corners on device or card surfaces - the 24px radius is what makes the dark canvas feel soft.
- Don't crowd sections. If vertical space between blocks drops below 80px, the void stops working.
- Don't use weights above 650 in Wand UI Pro; the type system caps there and going heavier breaks the quiet voice.
- Don't add secondary shadows, colored shadows, or border-glow effects to lift work - the 64/72/25% ambient shadow is the only elevation.
- Don't left-align hero content. Every headline, subtitle, badge, and CTA in the main column is centered.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
