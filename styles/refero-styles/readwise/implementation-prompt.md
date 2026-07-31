# AI Implementation Prompt

Build a Readwise-inspired interface using this source-derived style bundle.

Reference site: https://readwise.io
Theme: light
Category: Productivity
North star: A reader's annotated journal - quiet paper-white, serif headlines, and one blue pen.

Use these palette anchors:

- Pen Blue `#478cd0` for Blue supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Highlighter Yellow `#fff7ca` for Yellow supporting accent for decorative details and low-frequency emphasis.
- Reader Orange `#fb9100` for Orange supporting accent for decorative details and low-frequency emphasis
- Paper White `#ffffff` for Card surfaces, product screenshot backgrounds, button text on filled buttons, and the nav background. The topmost surface tier
- Ink `#1f1f1f` for Primary heading and body text. Near-black rather than pure black - softer on the eye, reads as printed ink rather than digital display
- Page Mist `#f1f5f8` for Page canvas background. A cool, very-light blue-gray that reads as off-white paper rather than a flat gray, giving the entire page a subtle blue cast
- Deep Slate `#2d2f33` for Secondary text and dark surface details. Used in nav and component borders where a slightly different tone from Ink is needed
- True Black `#000000` for Dark supporting neutral for text, icons, and strong contrast.

Use these typography anchors:

- Charter `--font-charter` for Editorial serif used exclusively for headlines and large display text. The choice of a transitional serif in a productivity SaaS is the site's signature move - it signals 'reading' and 'books' before any copy is read. Weight 400 at 50px with lineHeight 1.00 creates tight, book-title-style display; weight 600 at 29px handles section headlines. Substitute: Source Serif Pro or Lora if Charter is unavailable.
- Mulish `--font-mulish` for Humanist sans for everything non-display: nav, body, buttons, labels, icons. The weight range is wide - 400 for body, 600 for buttons, 700/800 for bold tags and emphasis. Tighter lineHeight (1.09) at 11px keeps captions compact; 1.50 at 16-18px gives body copy room to breathe. Consistent -0.02em tracking across all sizes tightens the sans into a clean utility voice.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 24px.
- Element gap: 12px.

Build these component patterns where relevant:

- Primary CTA Button: The main conversion action on hero and feature sections
- Ghost Sign In Button: Top-right navigation action
- Feature Badge Tag: Flags new or beta features in the nav
- Step Icon Circle: Visual anchor for 'How it works' steps
- Testimonial Card: User social proof in horizontal scroll
- In-line Highlighted Text: Emphasizes key phrases in body copy
- Product Hero Mockup: Shows the actual app on laptop and phone
- Navigation Bar: Top-level site navigation
- Text Link: In-body navigation and references
- Section Heading: Top-of-section titles like 'Here's how Readwise works:' and 'Here's what our users say:'

Do:

- Use Charter 50px weight 400 for hero display headlines, lineHeight 1.00, no letter-spacing adjustment - the tight leading makes the headline feel like a book title.
- Apply #fff7ca as a background wash behind 2-4 word phrases in body copy to signal emphasis; never as a full-surface background or button fill.
- Set the primary CTA as a solid #478cd0 button with white text, 10px radius, and 10/24px padding - no gradients, no shadows on the button itself.
- Use Mulish -0.02em tracking at all sizes; the tightened letter-spacing is what makes the sans feel like a deliberate choice rather than a default.
- Layer cards on the #f1f5f8 canvas with white #ffffff fills and hairline borders rather than relying on shadows for separation.
- Limit chromatic color to the single Pen Blue accent for actions and links; use Reader Orange only for the single 'Reader' feature badge.
- Pair every serif headline with Mulish body text at 16-18px - the contrast between transitional serif and humanist sans is the site's typographic identity.

Avoid:

- Don't use Charter for body copy, nav, or buttons - it's reserved for headlines 22px and above.
- Don't apply #fff7ca to full card surfaces, section backgrounds, or large areas - it loses its meaning as a highlighter if it covers more than a line of text.
- Don't introduce additional accent colors beyond Pen Blue, Highlighter Yellow, and Reader Orange - the system is deliberately near-monochromatic.
- Don't use heavy drop shadows on cards or buttons; if elevation is needed, keep it soft (spread 20px) and tinted with Ink rather than pure black.
- Don't set display headlines in all-caps or with positive letter-spacing - Charter at 50px works because of its tight 1.00 leading and natural tracking.
- Don't use a filled colored button for secondary actions; use the Ghost Sign In style (white fill, 1px border) or a plain text link in Pen Blue.
- Don't set the page background to pure white #ffffff - Page Mist #f1f5f8 is what makes the white cards and product mockups read as elevated surfaces.

Source prompt cues:

**Quick Color Reference**
- text: #1f1f1f
- background: #f1f5f8
- card surface: #ffffff
- border / hairline: #e2e8f0 (derive from #f1f5f8 family)
- highlight wash: #fff7ca
- primary action: no distinct CTA color
- feature badge: #fb9100 (Reader Orange, single-use)

**3-5 Example Component Prompts**

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. **Section heading block**: Charter 29px weight 400, #1f1f1f, lineHeight 1.13, centered. Followed by 64px vertical gap to a 3-column grid of step cards on the #f1f5f8 canvas.

3. **Step card**: centered column. 40px filled circle in #478cd0 with a white line-icon. Below: Charter 22px weight 600 step title in #1f1f1f. Below: Mulish 16px weight 400 description in #1f1f1f, max-width 280px.

4. **Testimonial card**: #ffffff background, 10px radius, 24px padding, 1px hairline border (#e2e8f0), soft shadow 0 2px 8px rgba(31,31,31,0.08). Avatar 32px circle top-left, name in Mulish 14px weight 700 #1f1f1f, handle in Mulish 14px weight 400 #478cd0, date in Mulish 14px weight 400 #1f1f1f. Body text in Mulish 14px weight 400 #1f1f1f with #478cd0 underlined link text inline.

5. **Ghost nav button**: #ffffff background, 1px solid #000000 border, 10px radius, Mulish 14px weight 600 #1f1f1f, 10px vertical / 18px horizontal padding. Sits at the right edge of the nav bar.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
