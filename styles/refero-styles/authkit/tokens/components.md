# Components

### Pill Button (Primary Ghost)
**Role:** Default button - used for 'Get started', 'Continue with Google/Microsoft', 'Learn more' links

999px radius, padding 8px 16px, background rgba(186,214,247,0.06) (faint frost wash), text #ffffff, 1px inset border rgba(186,215,247,0.12) of frosted blue-white. Weight 500, 14px Untitled Sans. Hover lightens the frost wash to rgba(186,214,247,0.12).

### Pill Button (Outlined)
**Role:** Secondary navigation button - header GitHub icon, secondary CTAs

999px radius, padding 8px 16px, transparent background, text #d1e4fa, 1px inset border rgba(186,215,247,0.12). Same geometry as primary ghost; only the fill differs.

### Violet CTA Button
**Role:** Sole chromatic CTA - appears only inside auth-form mockups as the 'Continue' submit button

Solid fill #663af3, white text, 6px radius, padding 12px 24px, weight 500. The only place a non-monochrome button appears; its vivid violet punches against the midnight palette.

### Glass Card (Feature)
**Role:** Feature cards, icon containers, section panels

16px radius, background rgba(186,214,247,0.03) (nearly invisible frost tint), padding 24px, no hard border. Elevation built from inset frost highlight + soft outer halo - reads as a glass plate lit from behind.

### Auth-Form Modal Card
**Role:** The headline product - floating login/signup cards in the hero

16px radius, background rgba(5,6,15,0.97), padding 24-32px. Three-layer shadow stack: top inset frost (#d8ecf8 20%), mid inset glow (#a8d8f5 6%), bottom drop (#000 30%). Floats above the hero with the central card scaled larger than its siblings.

### Text Input
**Role:** Email, password, and text fields inside auth forms

6px radius, background rgba(199,211,234,0.06), text #ffffff, placeholder #c7d3ea at ~60% opacity, 1px inset border rgba(186,215,247,0.12). Padding 10px horizontal. Focus state increases the border opacity to 0.24.

### Provider Button (Social Login)
**Role:** Continue with Google / Microsoft / SSO buttons

Full-width pill (999px or 6px radius variant), padding 12px 16px, background rgba(199,211,234,0.06), white text, provider icon left-aligned. Divider 'OR' sits between email submit and social options in 12px muted caps.

### Section Eyebrow Label
**Role:** All-caps section markers ('Introducing', 'Extensible by design', 'Shine bright', 'Light and dark modes supported')

15px dotDigital, weight 400, letter-spacing 0.10em, color #c7d3ea, centered. Flanked by thin horizontal lines that fade from transparent to rgba(186,215,247,0.12) and back.

### Feature Icon Tile
**Role:** Icon containers in the feature row (Single Sign-On, Password, MFA, Social Login, RBAC, Magic Auth)

9999px radius (perfect circle), ~56-64px square, background frosted tint, outlined glyph icon in #d1e4fa. Icons are line-art (1.5px stroke), mono - no fill, no color variation between tiles.

### Badge / Tag
**Role:** Category tags on integration cards (Email & Password, Social Login, MFA, SSO)

6px radius, background rgba(199,211,234,0.12), text #d1e4fa, padding 4px 8px, 12px Untitled Sans weight 500. Multi-layer inset shadow gives a faint inner glow.

### Logo Mark (WorkOS / AuthKit)
**Role:** Wordmark in header and hero

WorkOS wordmark is Untitled Sans weight 500 at 16px in #d1e4fa. The AuthKit hero wordmark is aeonikPro weight 500 at ~140-180px (display size extrapolated), filled with the Skywash vertical gradient (#d8ecf8 #98c0ef).

### Background Grid Layer
**Role:** Ambient page atmosphere - blueprint grid behind all sections

Full-bleed SVG/div layer with 1px lines at rgba(186,215,247,0.06), ~80-100px cell spacing, masked to fade at edges. A conic gradient halo sits at the top center creating a spotlight effect.

### Theme Toggle (Light/Dark)
**Role:** Demonstrates the product's light/dark mode support

Pill-shaped segmented control, 999px radius, two segments (moon icon / sun icon), 32px tall. Active segment has a slightly brighter frost background; inactive is transparent.

### Customization Swatch
**Role:** Color picker tiles in the 'Your brand. Your style.' section

Small 20-24px squares, 4-6px radius, filled with the brand color (violet, blue, teal, orange). Arranged in a row with 4px gaps. Labeled 'Colour' in 12px muted text.
