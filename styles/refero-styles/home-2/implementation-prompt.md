# AI Implementation Prompt

Build a Home-inspired interface using this source-derived style bundle.

Reference site: https://www.fluidtouch.biz
Theme: dark
Category: Productivity
North star: Stargazer's dark observatory

Use these palette anchors:

- Hot Magenta `#ed1672` for Active nav links, primary CTA fills, decorative accent dots - the only chromatic voice in the system, reserved so each occurrence reads as signal
- Midnight Ink `#121318` for Page canvas, hero background, footer - the deep-space base layer everything floats on
- Deep Space `#191c26` for Elevated card surfaces, section backgrounds one step above canvas
- Slate Edge `#212529` for Hairline borders, image frame rules, subtle structural dividers
- Pure White `#ffffff` for Primary text, headline color, nav links, button text - the only color competing with the magenta accent
- Void Black `#000000` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color

Use these typography anchors:

- Poppins `--font-poppins` for Display headlines at 700 weight dominate at 110px - the geometric bold reads as monumental and confident, the kind of type that fills a dark page like a billboard. At 400 it's used for nav and small UI labels where it stays unobtrusive.
- Muli `--font-muli` for Body and nav body text. Weight 300 is the signature choice - a humanist sans at near-thin weight against the Poppins 700 display creates a call-and-response rhythm: the headline shouts, the body whispers. Muli's softer curves (vs Poppins' geometric strictness) warm the dark page.

Use these layout rules:

- Base spacing: 8px.
- Density: spacious.
- Page max-width: 1280px.
- Section gap: 113px.
- Card padding: 20-32px.
- Element gap: 15px.

Build these component patterns where relevant:

- Pill CTA Button: Primary action trigger - the only filled button in the system
- Ghost Nav Link: Navigation item in resting state
- Active Nav Link: Currently selected page indicator
- Brand Mark: Logo lockup in header
- Hero Display Headline: Page-level headline on hero sections
- Hero Subtext: Supporting line beneath the display headline
- Body Text Block: Standard paragraph content
- Constellation Background Pattern: Decorative atmosphere layer on hero
- Full-bleed Image Section: Lifestyle or product photography inserted between dark sections
- Hairline Section Divider: Subtle structural rule between content blocks
- Magenta Accent Dot: Decorative punctuation - typically the period after a headline

Do:

- Use #ed1672 only for the active nav link, the filled CTA, and the decorative accent dot - limit to 2-3 instances per screen
- Set hero headlines at exactly 110px in Poppins 700 with line-height 1.00 to maintain the billboard impact
- Pair Muli 300 body text with the Poppins 700 display - never substitute another humanist sans for Muli, the weight contrast is the system
- Use 100px border-radius on every button and tag - the full pill shape is non-negotiable for brand recognition
- Maintain 113px horizontal margins on centered text blocks to preserve the floating-in-space feel
- Let the constellation pattern stay at 3% colorfulness - never boost opacity, it must read as background atmosphere
- Use full-bleed photography only between dark sections, never on the same plane as text

Avoid:

- Don't introduce a second accent color - the entire brand voice is one magenta against monochrome
- Don't apply drop shadows to any element; depth comes from surface lightness steps only
- Don't use Poppins 400 for headlines or Muli 400 for display - weight roles are fixed
- Don't reduce the 110px hero size for 'mobile friendliness' without a deliberate type-scale override
- Don't add border-radius to cards, images, or inputs - only buttons and tags get the 100px pill
- Don't use #ed1672 for body text or small labels - it fails contrast (4.4:1) and the pink must remain large or decorative
- Don't stack multiple saturated elements on one screen - the dark canvas is the brand, keep it 97% achromatic

Source prompt cues:

**Quick Color Reference**
- text: #ffffff
- background: #121318
- border: #212529
- surface: #191c26
- accent: #ed1672
- primary action: #ed1672 (filled action)

**3-5 Example Component Prompts**

1. **Hero section**: Background #121318 with a low-opacity white dot-and-line constellation pattern. Centered headline at 110px Poppins 700 in #ffffff, line-height 1.00. Append a solid #ed1672 period after the headline as decorative punctuation. Below at 113px gap, subtext at 18px Muli 300 in #ffffff, centered.

2. **Navigation bar**: Transparent background overlaid on dark canvas. Brand mark on left (Hot Magenta #ed1672 square icon + white 'fluidtouch' Poppins 700 wordmark). Nav links on right: 6 items, Muli 400 18px in #ffffff, 56px gap between items. Active item (first one) colored #ed1672 instead of white.

3. **Pill CTA button**: 100px border-radius, #ed1672 fill, white Poppins 400 16px text, 15px horizontal padding x 10px vertical padding. No border, no shadow. On hover, no color change - only subtle brightness lift via opacity.

4. **Full-bleed image section**: Edge-to-edge photograph, no border-radius, no border, no padding. Must sit directly between two dark sections with no gap. Image should be warm-toned, human-scaled, naturally lit.

5. **Body text block**: Muli 300 at 22px, line-height 1.50, color #ffffff. Content container centered with 113px left and right margins. No first-line indent, no drop cap, single column only.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
