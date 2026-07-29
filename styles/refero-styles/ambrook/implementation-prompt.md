# AI Implementation Prompt

Build a Ambrook-inspired interface using this source-derived style bundle.

Reference site: https://ambrook.com
Theme: light
Category: Fintech
North star: harvest ledger on butcher paper

Use these palette anchors:

- Parchment `#fcfaf1` for Page canvas and card surfaces - warm off-white replaces pure #ffffff to keep the system grounded in an agricultural, paper-like register
- Bone `#efe9e0` for Secondary surface for footer, soft sections, and hairline borders that need separation from the parchment canvas without harsh contrast
- Pure White `#ffffff` for Elevated card and product-mockup surface - used sparingly to lift specific panels (like the Ledger screenshot) above the parchment base
- Loam `#c7bcaf` for Subtle dividers, card edges, and low-emphasis borders between the canvas and content blocks
- Bark `#96897b` for Muted helper text, metadata, and supporting labels where a softer voice is needed than primary body copy
- Saddle `#50463c` for Secondary body text and subdued icon fills - a warm brown-gray that recedes without disappearing
- Ink `#211b15` for Primary text, heading strokes, and the dominant border color across the system. Warm near-black with a hint of umber keeps the interface from feeling clinical
- Charcoal Olive `#252a23` for Dark mode-style panels, product UI containers, and high-emphasis icon fills - used when a section needs to invert the warm page into something product-focused
- Deep Olive `#434f40` for Navigation borders, icon strokes, and the most-used neutral divider in the system - a moss-toned dark that reads as organic rather than industrial
- Sage `#7a9779` for Green accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color
- Honey Amber `#e8b672` for Primary action button fill - the system's singular chromatic accent for CTAs, earning attention through warmth rather than saturation
- Wheat `#f0c891` for Lighter amber used for heading borders, icon accents, and subtle decorative strokes where honey would be too heavy

Use these typography anchors:

- Lateral `--font-lateral` for Workhorse sans for body, nav, buttons, inputs, and secondary headings. Weight 400 for running text, 500 for buttons and emphasis. Custom letterforms give it subtle warmth a generic sans would miss - slightly humanist proportions rather than mechanical geometric.
- Lateral Narrow `--font-lateral-narrow` for Condensed variant for tighter column headings and subhead text where horizontal space is constrained but body voice is still wanted.
- Lateral Display `--font-lateral-display` for Hero and section display face. Used at weight 500 (not the default 700) for major headlines - this restraint is signature: the type whispers authority instead of shouting. Slight serif character in the terminals gives it an editorial, almost newspaper-headline feel that matches the agricultural brand voice.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 60-90px.
- Card padding: 30-45px.
- Element gap: 8-15px.

Build these component patterns where relevant:

- Primary Action Button: Filled amber CTA for email signup, trial start, and get-started flows.
- Ghost Outline Button: Secondary action (Sign Up, Log In) where the primary amber is too loud.
- Email Capture Input: Hero-level signup field with embedded submit button.
- Section Eyebrow Label: Small uppercase tag above every section heading (e.g. "ACCOUNTING SOFTWARE", "WHO WE SERVE").
- Section Heading: Two-line editorial headline for each content section.
- Trust Signal Row: Horizontal bar of icon + label assurances below the hero CTA.
- Brand Logo Strip: Horizontal scroller of customer brand marks to build social proof.
- Industry Illustration Card: 3-column grid of industry categories (Farming, Ranching, Construction, Trucking, Property Management, Services).
- Product Showcase Panel: Dark inverted panel previewing the actual product UI (Ledger view).
- Documentary Photo Collage: Hero bottom strip - overlapping, slightly rotated documentary photographs of real workers.
- Footer Link: Underlined link in the footer area.

Do:

- Use #fcfaf1 parchment as the page canvas for every section - never switch to pure #ffffff for a full page.
- Set primary action buttons to #e8b672 honey amber with #211b15 text and 3.75px radius.
- Open every section with an uppercase eyebrow label at 13px Lateral with 0.058em letter-spacing before the heading.
- Use Lateral Display at weight 500 (not 700) for headlines at 38px, 53px, and 68px.
- Render industry illustrations as monochrome line art in #211b15 stroke - no fills, no color.
- Apply 3.75px border-radius to buttons, inputs, and small surfaces; 7.5px to larger cards and panels.

Avoid:

- Don't use pure #ffffff as a page background - parchment #fcfaf1 is the canvas signature.
- Don't set headlines at weight 700 - the system's authority comes from 500 and restraint.
- Don't introduce blue, red, or other saturated primaries - the only chromatic accent is honey amber #e8b672.
- Don't use pill-shaped (9999px) buttons - the system is defined by subtle 3.75px rounding.
- Don't fill illustrations with color - they must remain monochrome line art in #211b15.
- Don't use stock-polished or studio photography - documentary, full-sun, candid subjects only.
- Don't add drop shadows to cards or panels - the system relies on border color and surface warmth for separation.

Source prompt cues:

**Quick Color Reference**
- text: #211b15
- background: #fcfaf1
- border: #efe9e0 (light) / #211b15 (strong)
- accent: #e8b672 (honey amber)
- brand green: #434f40
- primary action: #e8b672 (filled action)

**Example Component Prompts**

1. **Hero section**: Parchment #fcfaf1 background. Eyebrow label "ACCOUNTING SOFTWARE" in Lateral 13px weight 400, uppercase, letter-spacing 0.058em, color #211b15. Headline "Financial tools worthy of your work." in Lateral Display 68px weight 500, line-height 1.0, letter-spacing -0.75px, color #211b15, centered. Subtext in Lateral 17px weight 400, color #50463c. Email input with 1px #211b15 border, 3.75px radius, Lateral 15px placeholder #96897b. Embedded amber submit button #e8b672 with #211b15 text, 3.75px radius, arrow after label.

2. **Industry category card**: 1px #efe9e0 divider on all sides, padding 45px 30px, no card background. Monochrome line-art illustration of a tractor in #211b15 stroke at 1.5px, centered, ~120px tall. Below: industry name "Farming" in Lateral 15px weight 500 #211b15, followed by arrow character.

3. **Dark product showcase panel**: Background #252a23, border-radius 7.5px, padding 45px. Left column: heading "Bookkeeping that makes sense." in Lateral Display 38px weight 500, color #fcfaf1, letter-spacing -0.42px. Right column: product screenshot (Ledger table) on white #ffffff surface, slightly overlapping the dark panel's right edge.

4. Create a Primary Action Button: #e8b672 background, #211b15 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

5. **Documentary photo collage**: Five overlapping photographs at the page break below the hero. Each photo has a 3px #fcfaf1 border, slight rotation (-3 to +3 ), no border-radius. Subjects: welder, farmer, rancher, trucker, mechanic - candid, full-sun, documentary style.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
