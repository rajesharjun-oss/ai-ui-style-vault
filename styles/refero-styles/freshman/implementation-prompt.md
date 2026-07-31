# AI Implementation Prompt

Build a Freshman-inspired interface using this source-derived style bundle.

Reference site: https://freshman.tv
Theme: dark
Category: Media
North star: cinema title card on black velvet

Use these palette anchors:

- Pure White `#ffffff` for Primary text, logotype fill, border strokes, and the dominant foreground on the dark canvas - carries 92% of all color instances
- Carbon Black `#000000` for Base canvas and primary background - the default surface for every page
- Charcoal Shale `#101010` for Secondary surface for icon wells, sub-panels, and slight tonal lift above the pure-black canvas
- Signal Red `#ff2936` for Sparingly-applied accent for active states, marquee highlights, and high-emphasis punctuation - used as a single saturated note against the monochrome system

Use these typography anchors:

- Editorial New `--font-editorial-new` for Hero and headline display - the ultralight weight 200 is anti-convention; combined with the 20px breakpoint it reads as editorial print rather than web UI
- TT Firs Neue `--font-tt-firs-neue` for Workhorse UI and body sans - the only geometric grotesque in the system, anchors the project ticker labels, menu trigger, and utility text
- Altform `--font-altform` for Compact meta and condensed labels - tight 0.86-0.88 line-height and -0.03em tracking make it read like a festival credit roll
- Wasted Year `--font-wasted-year` for Signature editorial flourishes - bracket-wrapped taglines and small accent phrases; its hand-set quality is used for personality, not information density

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: .
- Section gap: 48-80px.
- Card padding: 12-20px.
- Element gap: 12px.

Build these component patterns where relevant:

- Hero Wordmark: Brand identity anchor - the primary visual element on the dark canvas
- Project Reel Ticker: Persistent bottom band showcasing latest work like a film festival credit roll
- Menu Trigger: Primary navigation entry point
- Brand Glyph: Persistent mark in the upper-left corner
- Year Counter: Cinematic page-position indicator
- Editorial Tagline Block: Voice/mission statement with typographic personality
- Cookie Consent Strip: Bottom-right regulatory notice
- Project Item Cell: Individual entry inside the project reel
- Thin Hairline Divider: Section separator - the only structural chrome in the system

Do:

- Set the wordmark at 200 weight italic in Editorial New - never bold, never regular; the ultralight is the signature
- Use only #ffffff text on #000000 canvas; treat the 1px white hairline as the only structural divider allowed
- Anchor the project reel to the viewport bottom on every page - it functions as the site's navigation spine
- Pair the body description (TT Firs Neue 16px) with a bracket-wrapped Wasted Year tagline directly beneath it; the handwriting-font punctuation is non-optional
- Use #ff2936 for at most one element per viewport - it is punctuation, not paint
- Set compact UI labels (reel items, counters) in Altform with 0.86-0.88 line-height and -0.03em tracking for the festival-credit-roll rhythm
- Keep the MENU trigger as a bare typographic label - no border, no background, no icon button chrome

Avoid:

- Do not introduce shadows, gradients, or elevation of any kind - flatness is the system
- Do not add card backgrounds or rounded corners; all surfaces are 0px radius on the black canvas
- Do not use bold or semibold weights for headlines - the weight 200 Editorial New is the anti-convention that defines the brand
- Do not use #ff2936 as a button fill or large background block - it loses all impact if used at scale
- Do not add a secondary navigation, breadcrumbs, or page tabs - the MENU trigger and the reel are the entire IA
- Do not set body copy above 16px or below 14px - the type scale is deliberately tight
- Do not alternate between light and dark sections; the page is uniformly dark, depth comes from type scale not surface color

Source prompt cues:

**Quick Color Reference**
- canvas/background: #000000
- primary text: #ffffff
- secondary surface: #101010
- hairline border: #ffffff (1px)
- accent / active state: #ff2936
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. *Hero wordmark screen*: full-viewport Carbon Black (#000000) background. Center a single italic 'freshman' logotype in Editorial New weight 200, white (#ffffff), sized to fill ~60% of the viewport width, letter-spacing -0.01em. Below it, a two-line description in TT Firs Neue 16px weight 400 white, centered, max-width 600px. Beneath that, a bracket-wrapped tagline in Wasted Year 14px white.

2. *Project reel ticker*: pinned bar at the viewport bottom, Carbon Black (#000000) background, 1px white (#ffffff) top border. Single row of project items, 12px column gaps, 20px vertical padding. Each item = uppercase project name (TT Firs Neue 16px weight 400 white) stacked over a sub-label (TT Firs Neue 12px, line-height 0.88, white at 70% perceived opacity). Zero radius on all elements.

3. *Year counter*: centered horizontally, positioned in the lower third of the viewport. Set '2025' in Altform 14px weight 400 white, line-height 0.88, letter-spacing -0.03em. No background, no border.

4. *Top navigation bar*: full-width, Carbon Black background, 20px vertical padding. Left: a small 16px white hash/cross glyph. Right: '+ MENU' in TT Firs Neue 16px weight 400 white. No borders, no background fills, no separators between left and right.

5. *Cookie consent strip*: bottom-right corner, Charcoal Shale (#101010) background, 1px white (#ffffff) border, 12px text in TT Firs Neue weight 400, uppercase, white. ~12px padding. Zero radius. Flush to the viewport edge, never centered.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
