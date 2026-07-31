# AI Implementation Prompt

Build a Promly-inspired interface using this source-derived style bundle.

Reference site: https://promlyapp.com
Theme: dark
Category: Other
North star: Midnight pulse through violet glass - a youth sanctuary lit by neon accents on near-black surfaces, where rounded photo collages float like screensavers behind sharp confident type.

Use these palette anchors:

- Void Indigo `#040723` for Page background, primary surface - near-black with a violet undertone that makes the whole canvas feel tinted rather than neutral
- Abyss Plum `#140f33` for Elevated card surface, shadow tone - a step lighter than Void Indigo, used to lift cards off the canvas with violet ambient
- Onyx `#000000` for Deep contrast surface for cards, input fills, and the darkest band behind photo content
- Glacier `#e4ebf3` for Off-white section backgrounds, light card surfaces - cool-tinted to harmonize with the violet system
- Paper `#ffffff` for Primary text on dark surfaces, button labels, image overlays - the dominant non-background color in the system
- Smoke `#999999` for Secondary/muted body text, disabled labels
- Ash `#808080` for Tertiary text and subtle borders on light sections
- Graphite `#333333` for Image borders, input strokes, secondary link text on light surfaces
- Charcoal `#222222` for Button borders on light surfaces, heavy text emphasis
- Cinder `#cccccc` for Input field borders, form dividers
- Pulse Blue `#3898ec` for Primary filled action background (CTA buttons, active nav) - the only chromatic fill in the system, acts as the single notification LED against the dark canvas
- Iris `#755eff` for Outlined action border, secondary accent - the violet identity color applied to ghost buttons and decorative strokes
- Lavender Lightning `#aa57ff` for Outlined action border, gradient start - lighter violet for tertiary buttons and gradient origins
- Neon Sprout `#0be014` for Link borders, icon borders, active state highlights - vivid green used sparingly as functional punctuation on links and tags
- Dusk Fade `#47246a` for Gradient mid-stop - deep violet that bridges bright lavender to black in hero gradient washes

Use these typography anchors:

- Avenir `--font-avenir` for Primary typeface across all contexts - headings, body, navigation, buttons, cards. Light 300 for large display headings creates a soft documentary feel; bold 700 for buttons and tag labels; regular 400 for body and supporting text.
- Poppins `--font-poppins` for Rare single-use bold label - appears on one decorative badge/button context, providing a geometric contrast to Avenir's humanist curves

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 20px.

Build these component patterns where relevant:

- Primary Filled Button: Main conversion action - donations, sign-ups, primary CTAs
- Outlined Action Button: Secondary conversion - ghost CTAs on dark and light sections
- Navigation Pill Button: Header CTA - the persistent 'Donate' action in the top nav
- Navigation Bar: Sticky site header with brand, dropdown nav, and CTA
- Hero Section: Above-the-fold headline + photo collage
- Photo Collage Grid: Decorative youth imagery on hero and section right sides
- Gradient Feature Card: Highlighted content section with light-violet background
- App Mockup Display: Product visual showing the Promly app interface
- Credential/Award Row: Social proof - awards, recognitions, media features
- Achievement List: Founder/organization accolades in text form
- Event Feature Section: Immersive content section - concerts, festivals, events
- Footer: Site footer (implied, not fully visible in screenshots)

Do:

- Use the Hero Dusk gradient (linear-gradient(216deg, #a755fb 20%, #47246a 37%, #000000 90%)) as the only hero background - never substitute a flat color or a different gradient angle.
- Apply 20px border-radius to all documentary photos and 30px to larger featured crops; 12px to all buttons and inputs; 25px to section cards.
- Set headlines at 60px Avenir weight 300 with -4px letter-spacing - the light weight is the signature, not bold.
- Use Pulse Blue (#3898ec) filled buttons for the single primary action per screen; Iris (#755eff) outlined buttons for secondary actions.
- Anchor each hero with a right-side photo collage of 8-10 rounded images with 1px white borders, arranged in offset rows.
- Let the violet-tinted shadow (rgba(102, 77, 255, 0.2) 0px 4px 100px) be the only elevation effect on cards - no gray drop shadows.
- Set section gap to 80px and card padding to 20px as the structural rhythm baseline.

Avoid:

- Do not use bold (700) or extra-bold weights for display headings - weight 300 is the system's identity choice; bold headlines break the whisper-tone.
- Do not introduce new colors for action buttons - the system has exactly one filled chromatic action (Pulse Blue) and outlined actions must use Iris, Lavender Lightning, or Neon Sprout.
- Do not apply flat black (#000000) as the page background - Void Indigo (#040723) is the system canvas; pure black is reserved for deepest card surfaces only.
- Do not use sharp corners (0px radius) on any image or card - every visual element must carry at least 8px radius, most 12-20px.
- Do not place green on filled buttons or backgrounds - Neon Sprout (#0be014) is link-border and icon-border only.
- Do not stack shadows or use gray-toned drop shadows - the single violet glow shadow is the only allowed elevation effect.
- Do not alternate text alignment arbitrarily - heroes are consistently left-aligned text with right-side photo collage; do not center-align long-form content.

Source prompt cues:

Quick Color Reference:
- Text (primary on dark): #ffffff
- Background (page canvas): #040723
- Border (subtle): #808080 / #333333
- Accent (links, tags): #0be014
- Brand violet (outlined actions): #755eff
- primary action: #3898ec (filled action)

Example Component Prompts:

1. Create a Primary Action Button: #3898ec background, #222222 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Create a feature highlight card: full-width card on Void Indigo (#040723) canvas, internal background Lavender Wash gradient (linear-gradient(135deg, #9e58fe 39%, #ffffff)), 25px corner radius, 24px padding. Heading at 35px Avenir weight 300, #000000. Body text at 18px Avenir weight 400, #333333. Row of three outlined buttons: transparent background, 1px #755eff border, 12px radius, #755eff text at 18px Avenir weight 700. Right side: photo collage of 6-8 rounded images, 20px radius.


4. Create an event feature section: full-bleed dark Onyx (#000000) background. Left half: atmospheric concert crowd photo (warm-lit, full saturation) bleeding to the left edge, 20px radius on the right edge only. Right half: headline 'Join us at the Changemakers Music Festival' at 60px Avenir weight 300, #ffffff, vertically centered. Below headline: two action buttons (one filled Pulse Blue, one outlined Iris #755eff).

5. Create a credential row: full-width dark band on Void Indigo (#040723), centered horizontal row of 5-6 circular award/badge logos, each ~80px diameter, gold and white badges, 40px gap between badges. No text labels - the badges carry the credibility.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
