# AI Implementation Prompt

Build a Signal Messenger-inspired interface using this source-derived style bundle.

Reference site: https://signal.org
Theme: light
Category: Other
North star: Frosted privacy glass. A nearly white room washed in pale blue light, with one vivid blue line marking every door you can open.

Use these palette anchors:

- Signal Blue `#2c6bed` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Deep Signal `#2942ff` for Navigation links and brand mark anchors - slightly cooler and more electric than Signal Blue, reserved for chrome-level interaction
- Signal Sky `#9dbbf8` for Hero section wash, large decorative panels - soft periwinkle that bathes the page in brand color without overwhelming
- Signal Mist `#a5cad5` for Secondary feature panel backgrounds - desaturated teal that recedes behind content, used to break the page rhythm without adding chroma
- Ink `#1b1b1b` for Primary body and heading text - soft black at AAA contrast on every surface, the dominant typographic color
- Slate `#404654` for Secondary body text, subdued paragraphs - cool gray with a faint violet cast that echoes the brand blue
- Twilight `#3c3744` for Footer background - muted purple-black that grounds the page in a warm dark wash without pure black harshness
- Fog `#e9e9e9` for Hairline borders, dividers, footer text - the structural neutral that separates content bands
- Paper `#f6f6f6` for Page canvas - off-white that warms the stark white without going cream
- White `#ffffff` for Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color

Use these typography anchors:

- Inter `--font-inter` for Sole typeface across the entire site. Weight 800 headlines are anti-soft - paired with tight 1.07-1.14 line-heights they create near-solid blocks of type that anchor the page. Weight 600 handles buttons and subheadings with a confident mid-weight. Weight 400 body at 1.50 line-height provides generous reading rhythm. The extreme contrast between 800 display and 400 body is the typographic signature.
- system-ui `--font-system-ui` for system-ui - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64-80px.
- Card padding: 30-48px.
- Element gap: 12-24px.

Build these component patterns where relevant:

- Outlined Primary Action Button: Primary CTA across the site - used for 'Get Signal', 'Donate to Signal', and most conversion points
- Filled Teal Action Button: Secondary or contextual action - used sparingly for in-feature prompts like the encrypted message reveal
- Navigation Link: Top bar navigation items
- Display Headline: Hero and section-opening headlines
- Body Paragraph: Supporting copy under headlines and in feature descriptions
- Hero Phone Mockup Container: Product visualization in hero and feature sections
- Feature Content Panel: Right-side visual container in 2-column feature sections
- Encrypted Message Chip: Decorative element demonstrating the encryption feature
- Halftone Globe Illustration: Decorative illustration in the nonprofit/donation section
- Footer Link Column: Organized link groups in the dark footer
- Signal Mark Lockup: Brand identifier in the header
- Donate Outlined Button: Conversion button in the footer illustration section

Do:

- Use Inter weight 800 for all headlines - the extreme weight contrast against 400 body text is the typographic signature
- Set line-height to 1.07 for 60px display text and 1.14 for 40px section headings - the tight leading makes headlines feel architectural
- Use outlined buttons (1.5px Signal Blue border, white fill) as the default CTA style - filled buttons only when sitting on a colored panel
- Apply 8px border-radius to all buttons and 16px to all image/panel containers - the radius gap between interactive and visual elements is intentional
- Use Signal Sky (#9dbbf8) for hero washes and Signal Mist (#a5cad5) for secondary panels - alternate the two blue tones to create page rhythm
- Set body text line-height to 1.50 - the generous leading is required for the 16px body to feel readable at the page's comfortable density
- Limit the brand blue to interactive elements, links, and the halftone illustration - never use it for large decorative fills or backgrounds other than the defined panel washes

Avoid:

- Don't use filled blue buttons on white backgrounds - outlined buttons are the primary CTA pattern and should not be overridden
- Don't add gradients, drop shadows beyond the defined elevation token, or decorative borders - the design relies on flat color bands for structure
- Don't use colors outside the defined palette - no additional chroma, no warm accents, no status colors beyond the blue family
- Don't set headline line-height above 1.20 - loose leading destroys the dense, confident type character
- Don't use pill-shaped buttons (9999px radius) - the 8px radius is a deliberate choice that distinguishes Signal from typical consumer apps
- Don't add photography, abstract graphics, or illustration styles other than the halftone dot technique - the visual personality is singular
- Don't use Inter at weights other than 400, 600, or 800 - 500 and 700 are absent from the type system for a reason; the three-weight gap is the scale

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
