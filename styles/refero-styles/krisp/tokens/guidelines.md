# Guidelines

### Do
- Use #f2ece2 (Warm Paper) as the default page canvas - never substitute pure white at the root level
- Apply the Iris Spark to Cyan Glow gradient only on display-size headlines (42px+); never on body or heading text
- Use 8px border-radius for all buttons and small interactive elements; 16px for cards; 9999px for pills and tabs
- Double-duty #131032 (Midnight Iris) as both text color on light surfaces and background color on dark sections - the hue reads as the same brand identity in both contexts
- Separate action button styles by fill: Iris Spark (#614efa) for one type, Slate (#1a1a22) for the other - never use two violet buttons side by side
- Use Hairline (#e7e7ea) at 1px for card borders and dividers; achieve elevation through surface color shifts rather than shadows
- Keep #918f9f (Fog) as the only muted body text color; never use Ash (#a1a1aa) for primary copy

### Don't
- Don't introduce new saturated colors - Iris Spark is the only vivid hue, and it should appear at most 1-2 times per viewport
- Don't apply drop shadows to cards or panels - surface shifts on the Warm Paper canvas are the elevation system
- Don't use pure #000000 for text - Midnight Iris (#131032) carries the brand undertone
- Don't place white cards on white backgrounds; always layer Snow (#ffffff) on Warm Paper (#f2ece2) or Cloud (#f7f7f8) for separation
- Don't use gradients on body, heading, or subheading text - the gradient treatment is reserved for display headlines only
- Don't use border-radius larger than 8px on buttons - the 8px radius is the button signature, not pills
- Don't show customer logos in full color - they must be muted to grayscale/gray to maintain the quiet editorial feel

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
