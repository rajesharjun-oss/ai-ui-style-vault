# AI Implementation Prompt

Build a Grafbase-inspired interface using this source-derived style bundle.

Reference site: https://grafbase.com
Theme: light
Category: Dev Tools
North star: engineering blueprint on cool marble

Use these palette anchors:

- Graphite Ink `#1b1b1b` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Marble `#ffffff` for Card surfaces, elevated panels, nav background, button text on dark fills. The brightest layer in the system
- Drafting Gray `#eaeaea` for Page canvas and section backgrounds. The second surface tier beneath white cards - the tone of the drafting table itself
- Steel `#60646c` for Secondary body text, subtext, helper copy. Carries information density without competing with primary headings
- Ash `#7c7c7c` for Muted tertiary text and less-emphasized metadata. Used where information recedes
- Hairline `#e0e1e6` for 1px borders, card outlines, divider rules. The system's structural lines - cool-tinted to read as architectural, not decorative
- Mint Signal `#00f2e6` for Saturated cyan-mint used inside product UI mockups and integration icon tiles. Not an interface accent - it is product-content color bleeding into marketing surfaces
- Moss `#8dc63f` for Secondary chromatic accent appearing in product screenshot data and integration tiles. Sits next to Mint Signal in the same icon/system cluster
- Sky `#00b9f1` for Tertiary accent in product UI and integration iconography. Completes the cool triad (mint, moss, sky) that defines the brand's chromatic fingerprint within screenshots

Use these typography anchors:

- Inter `--font-inter` for Sole typeface. Display uses weight 600 at 90px with -0.05em tracking (about -4.5px) - headline authority through geometric compression rather than heaviness. Headings at 40px use weight 500 with -0.025em tracking for a slightly looser, more editorial register. Body at 16px stays at weight 400 with normal tracking. The 13/14px sizes handle UI chrome and captions. No system fonts, no second family - Inter is the brand.
- sans (custom utility) `--font-sans-custom-utility` for Rare fallback utility class. Treat as Inter - likely a Tailwind 'sans' alias that resolved to a custom stack. Do not introduce as a distinct type family in output.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 28px.
- Element gap: 24px.

Build these component patterns where relevant:

- Announcement Bar: Site-wide notification strip
- Navigation Bar: Primary site navigation
- Primary Action Button: Highest-emphasis CTA
- Ghost Button: Secondary CTA
- Pill Button (Auth): Tertiary / sign-in variant
- Hero Headline: Primary page headline
- Product Preview Panel: Hero-right visual / dashboard mockup
- Feature Card: Section content container
- Integration Icon Tile: Logo / partner showcase
- Comparison Card: Alternative-to card in the "compare" carousel
- Footer Link Group: Site footer navigation
- Carousel Navigation: Section paginator

Do:

- Use Graphite Ink (#1b1b1b) for all primary text and all primary action buttons - never introduce a chromatic brand color for CTAs.
- Set display headlines at 90px Inter 600 with letter-spacing -4.5px; headings at 40px Inter 500 with -1px tracking. The negative tracking is the signature - do not normalize it.
- Apply 6px radius to all rectangular buttons, 40px to any pill-shaped button, and 20px to all cards and large content panels.
- Keep the interface fully monochromatic on white #ffffff and #eaeaea surfaces. Reserve the forest-to-teal gradient exclusively for the announcement bar.
- Use Steel (#60646c) for subtext and helper copy, Ash (#7c7c7c) for tertiary metadata - do not invent new grays.
- Build product mockups and integration tiles in the cool triad (Mint Signal, Moss, Sky) so the chromatic identity lives inside the product, not on the marketing chrome.
- Use the single shadow rgba(0,0,0,0.15) 0px 4px 20px 0px on primary buttons and elevated preview panels only - do not stack multiple shadow levels.

Avoid:

- Do not add saturated accent colors to the interface - the system is intentionally 99% achromatic.
- Do not use pure black (#000000); use Graphite Ink (#1b1b1b) which is softer against the cool gray canvas.
- Do not introduce a second typeface - Inter is the system, used at every size from 13px caption to 90px display.
- Do not set letter-spacing to 0 on display and heading text - the -4.5px / -1px tracking is what makes the large type feel engineered rather than webby.
- Do not add drop shadows to ghost buttons, cards, or nav - the shadow belongs only on the primary action button and the hero preview panel.
- Do not create button variants with new colors for hover/active states - swap to a slight opacity reduction or a subtle bg-gray-100 treatment instead.
- Do not place the green-to-teal gradient anywhere other than the top announcement bar - it is a one-shot signal, not a reusable surface.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
