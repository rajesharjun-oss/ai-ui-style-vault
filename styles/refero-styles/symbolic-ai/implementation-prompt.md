# AI Implementation Prompt

Build a Symbolic.ai-inspired interface using this source-derived style bundle.

Reference site: https://symbolic.ai
Theme: light
Category: AI
North star: editorial newsroom on cream paper. A broadsheet masthead in serif type, floating on warm off-white stock, with soft tan shadows that make every card feel like it was set in letterpress - not rendered.

Use these palette anchors:

- Canvas Cream `#fdfcf5` for Primary page canvas and white card surfaces.
- Ink Black `#000000` for Primary text, hairline borders, icon strokes, and the single CTA fill - black-on-cream is the system's only action color, no chromatic buttons
- Paper White `#ffffff` for Card surfaces, elevated content layers, input fills - the brighter sheet the cream canvas holds
- Charcoal `#4c4c4a` for Secondary borders, muted body text, link underline tones
- Slate Black `#333231` for Strong secondary borders and slightly softer heading text - separates structural dividers from Ink Black
- Warm Gray `#7f7e7b` for Captions, helper text, disabled states, tertiary borders
- Mid Stone `#656562` for Muted body copy and secondary dividers
- Soft Sand `#f5f3e9` for Subtle section bands, recessed surfaces, and the lighter shadow base
- Khaki Shadow `#edeadd` for The warm shadow tint used across all card elevations - replaces standard cool gray
- Sandstone `#e5e2d0` for Faint horizontal rules and gentle background tints
- Lavender Mist `#e2e0e4` for Cool-leaning hairline borders, subtle separation lines
- Editorial Teal `#10756a` for Teal wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- AI Violet `#6938ef` for Violet outline accent for tags, dividers, and focused UI edges.
- Deep Violet `#6a27d9` for Dark-mode variant of AI Violet for borders and stronger emphasis on processing states
- Stamp Red `#f42c2b` for Red wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Suisse Works `--font-suisse-works` for Editorial serif for all headlines and display type - Book (450) carries the masthead voice at 28-58px, Medium (500) for sub-headings at 20px. Suisse Works' high contrast and sharp serifs give the interface a printed-broadsheet authority that no sans could replicate.
- Open Runde `--font-open-runde` for Humanist sans for body, navigation, links, and most UI labels. Open Runde's slightly rounded geometric forms soften the editorial serif above - Regular (400) for body, Semibold (600) for nav emphasis, Bold (700) for inline labels. The wide x-height at 16px with 1.63 line-height creates comfortable reading density.
- Geist Mono `--font-geist-mono` for Monospaced labels for product state indicators ('Rewriting...', 'Transcribing...') and technical metadata. Geist Mono at 14px is intentionally small - it's a whisper of machinery inside the editorial voice, not a visual block.
- Grenze Gotisch `--font-grenze-gotisch` for Decorative blackletter for stamp-style elements like 'For Immediate Release'. Used once or twice per screen as accent texture, never for body. The gothic contrast against Suisse Works' modern serif is the system's signature historical flourish.
- Inter `--font-inter` for Minor fallback for non-primary UI labels where Open Runde is unavailable

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary CTA Button: The single action on a page
- Secondary Nav Button: Persistent site actions in the header
- Text Navigation Link: Top-bar nav items
- Feature Demo Card: Showcase product capabilities in scroll sections
- Newspaper Clipping Card: Atmospheric product illustration - embeds the publishing context
- AI Processing Pill: Indicate the system is actively working on a task
- Verification Checkmark: Show that content has been validated
- Stamp Badge: Editorial decoration - urgency or release-state indicators
- Editorial Headline: Hero and section titles
- Hero Subtext: Supporting paragraph under the hero headline
- Top Navigation Bar: Persistent site navigation
- Input Field: Form inputs

Do:

- Use #fdfcf5 as the page background and #ffffff only for card and elevated surfaces - the warm/cool contrast between canvas and paper is the system's foundation
- Use Suisse Works (or GT Sectra) for all headlines 20px and above; never substitute a sans for editorial display type
- Apply the warm khaki shadow rgba(213, 208, 184, 0.4) 0px 2px 6px to every card - never use cool gray shadows
- Use 8px radius for standard cards and inputs, 24px for large feature demo cards, and 10000px (pill) for all buttons and AI processing indicators
- Use Ink Black (#000000) as the single primary action color - fill the CTA button solid black, no gradients, no chromatic alternatives
- Reserve Editorial Teal (#10756a) for verification and 'correct' states; reserve AI Violet (#6938ef) for active processing labels
- Use present-participle AI labels with trailing ellipsis ('Rewriting...', 'Fact checking...') in Geist Mono - the verb-in-progress is the system's primary way to say 'the machine is working'

Avoid:

- Don't introduce chromatic CTA buttons - black-on-cream is the system's only action language
- Don't use pure white (#ffffff) as a page background - the cream canvas (#fdfcf5) is the entire atmosphere
- Don't apply cool gray shadows (rgba(0,0,0,...)) - all elevation must use the warm khaki base
- Don't mix sans-serif into headlines above 20px - the serif/sans split is structural, not decorative
- Don't use Stamp Red (#f42c2b) for buttons, errors, or destructive actions - red is reserved for editorial stamp accents only
- Don't flatten the type scale - Suisse Works Book (450) is the headline weight; don't promote to Bold (700) for emphasis, use size and line-height instead
- Don't add drop shadows stronger than 0.4 opacity - the system never goes beyond a soft printed-paper lift, never a hovering UI panel

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #fdfcf5
- border: #4c4c4a
- accent: #10756a (teal - verification)
- AI state: #6938ef (violet - processing)
- primary action: #000000 (filled action)

**Example Component Prompts**

1. **Hero section**: Canvas background #fdfcf5. Headline at 58px Suisse Works Book 450, #000000, centered, line-height 1.50. Subtext at 16px Open Runde Regular, #4c4c4a, centered, max-width 560px. CTA: black pill button (#000000 fill, #ffffff text, 10000px radius, 8px/20px padding, Open Runde Semibold 16px, label 'Request a demo '). 80px section gap below.

2. **Feature demo card**: #ffffff surface, 24px corner radius, 20px padding, shadow rgba(213, 208, 184, 0.4) 0px 2px 6px 0px. Contains a newspaper-textured image inside with a 1px #4c4c4a border and 8px radius. Overlaid top-left: AI Processing Pill (#ffffff background, 1px #6938ef border, Geist Mono 14px #6938ef text, 10000px radius, 4px/12px padding, label 'Rewriting...'). Card is rotated -1.5 degrees.

3. **Top nav bar**: #fdfcf5 background, 1px #e5e2d0 bottom border, 64px height, 24px horizontal padding. Logo (4-dot cluster) left, 5 text links right (Open Runde Regular 16px #000000), Sign up button (#000000 fill, #ffffff text, Open Runde Medium 16px, 16px radius, 8px/16px padding) at far right.

4. **AI processing pill (standalone)**: #ffffff background, 1px #6938ef border, 10000px radius, 4px vertical / 12px horizontal padding. Inside: spinning violet arc icon (16px) + Geist Mono 14px #6938ef text reading 'Fact checking...'. The trailing ellipsis is required.

5. **Stamp badge decoration**: Grenze Gotisch 48px / line-height 1.0, #f42c2b, uppercase 'FOR IMMEDIATE RELEASE', rotated -3 degrees, no background, optional 1px #f42c2b border at 0.3 opacity forming a faded rectangle.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
