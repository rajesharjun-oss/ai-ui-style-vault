# AI Implementation Prompt

Build a Shade-inspired interface using this source-derived style bundle.

Reference site: https://shade.inc
Theme: light
Category: SaaS
North star: Editorial paper cutouts on white

Use these palette anchors:

- Charcoal Ink `#131315` for Primary text, dark pill button fill, heading borders - warm near-black, the only filled button color in the system
- Pure White `#ffffff` for Page canvas, card surfaces, button text, ghost button background
- Bone `#f7f5ff` for Secondary canvas, subtle violet-tinted off-white for alternating sections
- Cutout Gray `#f1f1f1` for Solid offset shadow color under primary buttons and secondary surfaces
- Slate Mid `#717173` for Muted body text, secondary metadata, helper copy
- Hairline `#d0d0d0` for Subtle borders, dividers, inactive tab indicators
- Deep Charcoal `#444444` for Input borders, slightly heavier dividers than Hairline
- Logo Violet `#855cf7` for Brand mark gradient terminus, logo cube fill - the only saturated color in the system
- Lavender Trace `#dacefd` for Selected tab underline, violet hairline accents, announcement pill border - violet at whisper volume

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Inter Display `--font-inter-display` for Primary typeface for all UI text, body and headings alike. Single weight 400 carries the entire hierarchy through size and tracking alone - no bold, no light. The custom stylistic sets (ss01, ss07, ss08) reshape the g, a, and l terminals into a more geometric, editorial silhouette that distinguishes it from stock Inter.
- Aux Mono `--font-aux-mono` for Monospaced label font for section eyebrows (e.g. 'DAY 1', 'LET'S CHAT', nav items, badge text). Sets at 14px with -0.04em tracking gives timestamps and labels a technical, archival feel against the editorial display type.
- Inter `--font-inter` for Secondary fallback / system-level utility text where the custom display features aren't required

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 100px.
- Card padding: 24px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary Pill Button: Highest-emphasis action
- Ghost Pill Button: Secondary action paired with primary
- Top Navigation Bar: Site-wide navigation
- Announcement Pill: Inline news/feature flag above hero
- Hero Headline: Page-level display
- Tab Navigation Strip: In-section content switcher
- Product Screenshot Card: Feature proof point
- Logo Strip: Social proof / partner bar
- Timeline Onboarding Row: Step-based explanation
- Cookie Consent Banner: Bottom-right compliance notice
- Brand Logo Mark: Identity

Do:

- Use the hard offset shadow (8px 8px 0px 0px #f1f1f1) exclusively on primary pill buttons - never apply blur or diffusion to elevation
- Set Inter Display at weight 400 only; let size and -0.03em tracking carry hierarchy, never switch to bold
- Reserve #855cf7 for the logo gradient and the active tab underline - every other accent must be the muted #dacefd lavender
- Pair every primary CTA with a ghost secondary button of identical 35px radius and padding
- Use 100px between major sections, 10-12px between inline elements, 24px inside cards
- Treat photography as full-bleed and unbordered - let the white canvas frame it like a gallery wall
- Apply Aux Mono 14px -0.04em to all eyebrow labels, timestamps, and tab headings

Avoid:

- Do not introduce additional brand colors or saturated fills - the system is 99% achromatic by design
- Do not use soft blurred shadows on buttons; the signature is hard, solid, paper-cutout offsets
- Do not bold headlines or use weight 500+ in Inter Display - the single-weight hierarchy is intentional
- Do not round the active tab into a pill background; the 2px violet underline is the only acceptable indicator
- Do not add gradient backgrounds to sections or cards - gradients are reserved for the brand mark
- Do not use border-radius values outside the defined scale (35/20/14/9/2px)
- Do not center-align body paragraphs longer than two lines - the system is left-aligned with a centered display headline only

Source prompt cues:

Quick Color Reference:
 text: #131315 (charcoal)
 background: #ffffff (canvas), #f7f5ff (bone secondary)
 border: #d0d0d0 (hairline), #444444 (input)
 accent: #855cf7 (logo/active tab), #dacefd (lavender whisper)
 primary action: #131315 (filled action)

3-5 Example Component Prompts:

1. Hero section: white #ffffff canvas. Display headline at 72px Inter Display weight 400, color #131315, letter-spacing -0.03em (-2.16px), line-height 1.1. Muted paragraph at 18px weight 400, #717173. Two buttons side by side: ghost pill (1.5px #131315 border, 35px radius, #131315 text, 15px 24px padding) + dark pill (#131315 fill, white text, 35px radius, hard 8px 8px 0px 0px #f1f1f1 shadow, 15px 24px padding). Centered stack, max-width 900px.

2. Announcement pill: 1px #dacefd border, fully rounded (999px), Aux Mono 14px text in #855cf7, transparent fill, 6px 14px padding, centered above hero with 16px bottom margin.

3. Tab nav strip: four labels in Inter Display 16px #717173, evenly spaced across full width, 1px #d0d0d0 hairline beneath entire row, 2px solid #855cf7 underline directly below the active tab label only.

4. Product screenshot card: 14px radius, 1px inset rgba(0,0,0,0.05) border, no outer shadow, 24px padding, sitting on #f7f5ff bone surface. Image fills the card edge-to-edge with no rounded inner clipping.

5. Timeline step row: three columns with Aux Mono 14px eyebrow in #717173, Inter Display 24px heading in #131315, 16px body text in #717173. Full-width 1px #d0d0d0 rule below, 2px solid #131315 circle markers (10px diameter) at each step column position; outlined circle for inactive steps.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
