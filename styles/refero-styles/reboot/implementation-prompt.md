# AI Implementation Prompt

Build a reboot-inspired interface using this source-derived style bundle.

Reference site: https://reboot.studio
Theme: light
Category: Agency
North star: quiet atelier on cream paper - a design studio's homepage that reads like a printed monograph, where the only color is the one blue mark in the margin

Use these palette anchors:

- Paper Gray `#e5e7eb` for Page canvas and hairline borders - the warm off-white ground that all type sits on
- Editorial Black `#000000` for Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color
- Charcoal Ink `#232323` for Headings and emphasized prose - a near-black that softens headlines against the pure black of running text
- Soft Graphite `#a7a7a7` for Muted body text and secondary metadata - the gray that carries secondary sentences without competing with the lead
- Faded Pencil `#c8c8c8` for Tertiary annotations and the most restrained helper text - the lightest voice in the grayscale scale
- Pure White `#ffffff` for Surface highlights and inverse text on the black pill button
- Sapphire Beam `#00c8fb` for Decorative inline gradient - cyan-to-indigo mark used as a full-stop between sentences, never as a fill or background
- Ember Sunset `#ef3313` for Secondary decorative gradient - warm triple-stop used sparingly for moments that need a chromatic counterpoint to the blue

Use these typography anchors:

- Inter `--font-inter` for The sole typographic voice - used for everything from nav metadata to display headlines. Weight 400 carries running prose, weight 500 lifts section lead-ins and the primary action, weight 600 is reserved for the wordmark. The narrow three-size scale (14/16/40) is deliberate: hierarchy comes from luminance and weight, not from a cascading type ramp.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 720px.
- Section gap: 80px.
- Card padding: 32px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary Pill Button: The single action surface - used for 'See work' and any definitive call to action
- Status Badge: Inline metadata pill - used for 'Hiring' indicators in the header
- Wordmark Lockup: Brand identity in the header
- Inline Gradient Marker: Chromatic punctuation between sentences - the only color in the body content
- Text Link: Inline navigation - 'Book a call' and similar
- Prose Section Block: The fundamental content unit - a paragraph with mixed-emphasis sentences
- Muted Manifesto Block: Secondary statements that should recede - lists of disciplines, timeframes, closing lines
- Device Mockup Illustration: Sole illustrative element - a phone frame used as inline punctuation
- Minimal Header Bar: Top-of-page navigation and brand placement

Do:

- Use Inter at weights 400 and 500 for all body and heading text; reserve 600 for the wordmark only
- Use the three-step grayscale scale (#000000 #232323 #a7a7a7) to create text hierarchy within a single block instead of jumping to a larger size
- Use the black pill button (fill #000000, radius 9999px, text #ffffff, Inter 14px/500) for the single primary action per page
- Use the Sapphire Beam gradient (#00c8fb #1a2ff7) only on 20-24px inline marker icons, never as a background or button fill
- Left-align all content in a single narrow column (max ~480px) inside an 720px page container
- Set section gap to 80px and use 32px internal padding for any surface that needs containment
- Set cards and non-button containers to 16px border-radius; set all buttons and badges to 9999px

Avoid:

- Don't introduce chromatic colors beyond the two existing gradients - the palette is achromatic plus two accent gradients
- Don't use more than three type sizes; the scale is intentionally 14 / 16 / 40
- Don't use color to signal emphasis - use weight shifts (400 500) and grayscale steps instead
- Don't add backgrounds, borders, or cards to text blocks - text should sit directly on the page canvas
- Don't apply drop shadows to text, buttons, or content blocks; the design is flat by principle
- Don't center text or use multi-column layouts; everything is a single left-aligned column
- Don't scale the blue gradient to fill large areas or use it on the primary button - it is decorative punctuation, not a brand fill

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
