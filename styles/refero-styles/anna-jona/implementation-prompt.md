# AI Implementation Prompt

Build a Anna Jona-inspired interface using this source-derived style bundle.

Reference site: https://annajona.is
Theme: light
Category: Other
North star: a love letter on blush paper

Use these palette anchors:

- Blush Paper `#fce1e3` for Page canvas, section backgrounds, the warm field all content lives on
- Coral Crimson `#db404f` for All headings, body text, icons, and the sole action color - the entire voice of the brand
- Midnight Ink `#0e1736` for Deep accent for select surfaces and inverse contexts, a cool counterpoint to the warm field
- Pure White `#ffffff` for Image backgrounds, inline accents, negative space within photographs and cards
- Soft Black `#000000` for Decorative strokes, icon fills, hairline borders - the only place pure black appears

Use these typography anchors:

- Sansita `--font-sansita` for Display and heading face - bold, slightly condensed, with -0.02em tracking that tightens at every size. Carries all editorial weight: the page announces itself through this one confident voice.
- Nunito Sans `--font-nunito-sans` for Body and UI face - the 18px body sets a generous reading rhythm at 1.5 line-height; 700 weight for emphasized inline phrases and small caps headers. The 72px outlier is likely a single oversized numeral or pull-quote.
- Clarkson `--font-clarkson` for Secondary prose - the slightly taller 1.7 line-height is for long-form letter passages where breathing room matters more than density

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 144px.
- Card padding: 48px.
- Element gap: 11px.

Build these component patterns where relevant:

- Hero Statement: Opening page declaration - the largest text block on the site
- Angled Image Bleed: Full-bleed photograph that breaks the pink field with a diagonal cut
- Letter Section: Long-form prose block - the emotional heart of the page
- Pill Button: Sole interactive element style
- Rounded Decorative Shape: 90px-radius geometric element used as visual punctuation
- Side-by-Side Image Pair: Two-photo composition for showing complementary views
- Inline Link: Text-level navigation within body prose
- Section Anchor Header: Small-caps or oversized subhead marking a new prose section

Do:

- Use only Coral Crimson (#db404f) for all text, icons, and interactive elements - never introduce a second chromatic text color
- Set all body text at 18px with 1.5 line-height in Nunito Sans - smaller or denser prose breaks the editorial reading rhythm
- Apply -0.02em letter-spacing to every Sansita heading size, scaling proportionally (e.g. -1.4px at 70px, -0.56px at 28px)
- Break sections with full-bleed photographs using angled diagonal edges (8-12 clip-path), never with horizontal dividers or color bands
- Use 90px border-radius for decorative shapes and 300px for the pill button - these two radii are the only geometry in the system
- Maintain 144px top padding on major sections and 48px between paragraphs to preserve the slow, letter-like vertical cadence
- Place all content directly on Blush Paper (#fce1e3) - no white cards, no elevated panels, no background containers

Avoid:

- Do not add box-shadows, drop-shadows, or any z-depth indication - the design is intentionally paper-flat
- Do not introduce additional accent colors - Coral Crimson is the only chromatic voice
- Do not use rectangular image containers, standard card components, or 8-16px UI corner radii - the system operates at two radius extremes only
- Do not set body text below 18px - the type scale starts at body and grows upward
- Do not use horizontal rules, section dividers, or background color bands to separate content - use diagonal image bleeds and whitespace instead
- Do not apply different colors to link states - all text including links stays Coral Crimson, distinguished only by underline
- Do not use sans-serif for headlines - Sansita 700 is the only display voice and defines the editorial character

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
