# AI Implementation Prompt

Build a Authkit-inspired interface using this source-derived style bundle.

Reference site: https://authkit.com
Theme: dark
Category: Dev Tools
North star: Frosted glass cathedral at midnight

Use these palette anchors:

- Midnight Canvas `#05060f` for Page background, deepest card surface, badge fills - the near-black base everything else floats on
- Steel Plate `#2f343e` for Elevated surface, button fills for ghost/secondary actions, subtle panel backing
- Fog Veil `#9da7ba` for Muted body copy, card text - readable but stepped back from headlines
- Moon Mist `#c7d3ea` for Body text, secondary labels, muted helper copy
- Frost Glow `#d1e4fa` for Primary text fill for body and links, badge text, icon fills - the default luminous foreground
- Ice Highlight `#d8ecf8` for Light text on dark surfaces, inverse labels, and high-contrast captions. Do not promote it to the primary CTA color; Headline gradient - top-to-bottom fade from Ice Highlight to soft blue, used on the AuthKit wordmark and key headings
- Pure White `#ffffff` for Button text, input text, maximum-emphasis foreground
- Void Violet `#663af3` for Primary CTA fill - the only chromatic accent, used exclusively for the Continue/Submit button inside auth forms; vivid violet against near-black creates focused urgency without breaking the monochromatic mood
- Blueprint Blue `#b6d9fc` for Decorative icon accent, soft highlight wash on feature illustrations
- Ember Glow `#e46d4c` for Secondary accent - appears in demo/showcase contexts (logo recoloring swatches) for brand-color customization display
- Signal Blue `#027dea` for Secondary accent - appears in customization swatch grids to demonstrate brand-color options
- Deep Teal `#269684` for Secondary accent - appears in customization swatch grids
- Gridline Blue `#3f4959` for Shadow color for outer card drop-shadows - cool dark blue-grey gives elevation a tinted, on-brand feel rather than neutral black
- Glass Edge `#bad7f7` for Hairline borders on buttons, inputs, and links - inset 1px stroke of frosted blue-white that defines edges without hard lines
- Luminous Fill `#c7d3ea` for Badge fill and soft surface tint - translucent cool white for tag backgrounds and subtle UI washes

Use these typography anchors:

- Untitled Sans `--font-untitled-sans` for Body, UI, buttons, inputs, badges, small headings - the working typeface for everything functional
- aeonikPro `--font-aeonikpro` for Display headings only - the wordmark 'AuthKit', section headings, hero copy; weight 500 at 44-48px gives the wordmark a wide, calm presence rather than a bold shout
- dotDigital `--font-dotdigital` for All-caps eyebrow labels ('Introducing', 'Extensible by design', 'Shine bright') - 0.10em tracked monospace-flavored caps act as quiet section markers between the display type and body copy

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 120px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Pill Button (Primary Ghost): Default button - used for 'Get started', 'Continue with Google/Microsoft', 'Learn more' links
- Pill Button (Outlined): Secondary navigation button - header GitHub icon, secondary CTAs
- Violet CTA Button: Sole chromatic CTA - appears only inside auth-form mockups as the 'Continue' submit button
- Glass Card (Feature): Feature cards, icon containers, section panels
- Auth-Form Modal Card: The headline product - floating login/signup cards in the hero
- Text Input: Email, password, and text fields inside auth forms
- Provider Button (Social Login): Continue with Google / Microsoft / SSO buttons
- Section Eyebrow Label: All-caps section markers ('Introducing', 'Extensible by design', 'Shine bright', 'Light and dark modes supported')
- Feature Icon Tile: Icon containers in the feature row (Single Sign-On, Password, MFA, Social Login, RBAC, Magic Auth)
- Badge / Tag: Category tags on integration cards (Email & Password, Social Login, MFA, SSO)
- Logo Mark (WorkOS / AuthKit): Wordmark in header and hero
- Background Grid Layer: Ambient page atmosphere - blueprint grid behind all sections

Do:

- Use 999px radius for all interactive elements (buttons, social-login buttons, tag toggles); reserve 16px radius exclusively for cards and modals, 6px for badges and inputs, and 9999px for circular icon containers.
- Build elevation from inset frost highlights + soft outer halos rather than conventional drop-shadows: pair inset rgba(216,236,248,0.2) 1px top edge with a 24-48px inset glow and a dark cool drop.
- Use Void Violet (#663af3) exclusively for the auth-form Continue/submit CTA - never as a decorative accent or non-auth button background.
- Set headline text in aeonikPro weight 500 at 44-48px with the Skywash vertical gradient (#d8ecf8 #98c0ef); body and UI in Untitled Sans 400-500.
- Place all-caps eyebrow labels (dotDigital, 15px, 0.10em tracking, #c7d3ea) centered and flanked by fading horizontal lines at rgba(186,215,247,0.12) to mark every section opening.
- Use rgba(186,215,247,0.12) as the universal hairline border - never solid strokes; the frosted-inset edge is the system's border language.
- Set section gaps at 120px and card padding at 24px; rhythm should feel cathedral-like rather than dense SaaS.
- Render text in the Ice Highlight Frost Glow Moon Mist Fog Veil progression (#d8ecf8 #d1e4fa #c7d3ea #9da7ba) for heading body muted body helper copy.
- Use the conic-gradient spotlight halo (rgba(124,145,182,0.5) at center, fading outward) at the top of every full-bleed hero to anchor the composition.

Avoid:

- Do not introduce additional chromatic accents - the palette is monochromatic with one violet CTA; any extra hue breaks the system.
- Do not use solid colored borders; replace them with 1px inset rgba(186,215,247,0.12) strokes to preserve the glass aesthetic.
- Do not use bold weights (600+) on aeonikPro display headings - the wordmark's authority comes from weight 500 at large size, not volume.
- Do not apply conventional drop-shadows; the system reads elevation through inset glow + dark halo.
- Do not mix radius families on the same component type - every button is pill, every card is 16px, every badge is 6px.
- Do not place white (#ffffff) on background tints brighter than rgba(186,214,247,0.12) - the contrast floor collapses.
- Do not use the Skywash gradient on body text or buttons; reserve it for the display wordmark and the largest headings only.
- Do not introduce light-theme colors into core tokens even though the product supports light mode; the marketing site is dark-first, and light-mode demos are a product feature, not a design-system palette.

Source prompt cues:

Quick Color Reference:
- canvas: #05060f
- surface (frosted glass card): rgba(186,214,247,0.03)
- surface (elevated modal): rgba(5,6,15,0.97)
- text (headline): #d8ecf8
- text (body): #d1e4fa
- text (muted): #c7d3ea
- text (helper): #9da7ba
- border (hairline): rgba(186,215,247,0.12)
- accent / primary action: #663af3 (filled action)

Example Component Prompts:

1. Create a Primary Action Button: #663af3 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Section eyebrow + heading stack: eyebrow is 15px dotDigital weight 400 letter-spacing 0.10em #c7d3ea, centered, flanked by fading horizontal lines (gradient from transparent to rgba(186,215,247,0.12) to transparent). Below, heading is 44px aeonikPro weight 500 in #d8ecf8, centered. Body below is 16px Untitled Sans 400 in #c7d3ea, max-width 640px centered.

3. Feature icon tile row: six circular tiles (9999px radius, 56px), background rgba(186,214,247,0.06), outlined line-art icon centered in #d1e4fa, label below in 14px Untitled Sans #c7d3ea. Tiles connected by 1px horizontal line at rgba(186,215,247,0.12).

4. Ghost pill button: 999px radius, padding 8px 16px, background rgba(186,214,247,0.06), 1px inset border rgba(186,215,247,0.12), text #ffffff, 14px Untitled Sans weight 500.

5. Background canvas with grid: #05060f base, 1px grid lines at rgba(186,215,247,0.06) at 80px intervals, full-bleed, masked to fade at edges. Conic-gradient spotlight at top center: conic-gradient(at 50% -5%, transparent 45%, rgba(124,145,182,0.3) 49%, rgba(124,145,182,0.5) 50%, rgba(124,145,182,0.3) 51%, transparent 55%).

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
