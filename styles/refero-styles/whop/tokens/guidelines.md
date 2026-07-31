# Guidelines

### Do
- Use Ember Orange (#fa4616) exclusively for the single primary action on any screen - never for decorative elements, tags, or secondary buttons
- Apply the hard burnt-orange offset shadow (rgb(182,38,0) 0px 3px 0px 0px) only to primary CTA buttons
- Set display headlines in acidGrotesk at 56px or 128px with line-height 1.00 and letter-spacing -0.03em - never use Inter for display sizes
- Use 24px border-radius for all card-like containers and 8px for all buttons - this size ratio is non-negotiable
- Keep the page canvas #f9f9f9 and card surfaces #ffffff - never invert this hierarchy
- Use 64-80px vertical gaps between major sections to maintain the spacious rhythm
- Use Geist Mono exclusively for code, terminal prompts, and technical metadata - never for UI labels or body text

### Don't
- Don't use Ember Orange for any element that isn't the primary action button on that screen
- Don't apply soft drop shadows, blur, or opacity-based shadows to any element - the system is flat
- Don't use display sizes (56px+) in Inter - Inter is for 13-20px functional UI only
- Don't add gradients - the system is entirely flat color
- Don't use neutral grays for decorative accents or illustrations - the palette is near-black to near-white with one orange
- Don't set border-radius values outside the four tokens: 4px, 8px, 12px, 16px, 24px
- Don't place multiple orange buttons on the same screen - one primary action per view

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
