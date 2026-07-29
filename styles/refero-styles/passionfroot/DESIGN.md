# Passionfroot - Style Reference

> Twilight cloud library on warm parchment: a restrained serif headline floats over cream cards, pastel accents, and a dark violet-to-coral atmosphere.

**Theme:** mixed

Passionfroot is a warm creative SaaS system. It starts with a cinematic dusk hero, then settles into parchment surfaces, compact rounded UI, and lightly elevated cream cards. The system is colorful, but the color is distributed in small hits: pastel feature cards, decorative strokes, icon borders, chips, and illustration details. The interface should never become a single-color brand wash.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Ink Black | `#1d1d1c` | `--color-ink-black` | Primary text, structural borders, dark neutral fills |
| Parchment Cream | `#f8f7f2` | `--color-parchment-cream` | Default page canvas and warm nav surface |
| Sand Gray | `#d8d6ce` | `--color-sand-gray` | Warm hairlines, dividers, shadow base |
| Linen Beige | `#edeae4` | `--color-linen-beige` | Secondary card and elevated surface |
| Paper White | `#ffffff` | `--color-paper-white` | Highest elevation panels, inputs, neutral buttons |
| Charcoal Stone | `#43423e` | `--color-charcoal-stone` | Body copy, neutral button labels, muted borders |
| Ash Gray | `#99978f` | `--color-ash-gray` | Placeholder text, disabled text, low emphasis icons |
| Slate Warm | `#7a7974` | `--color-slate-warm` | Secondary muted labels with more contrast |
| Electric Violet | `#b26bf5` | `--color-electric-violet` | Main brand accent and vivid lavender highlight |
| Twilight Indigo | `#190922` | `--color-twilight-indigo` | Dark hero, atmospheric background, deep contrast |
| Bubblegum Pink | `#f788d2` | `--color-bubblegum-pink` | Pastel card color and playful accent |
| Tangerine | `#ff9147` | `--color-tangerine` | Sunset warmth, decorative accents |
| Aqua Teal | `#4ad5e8` | `--color-aqua-teal` | Bright cool accent and illustration fill |
| Sky Blue | `#51b1fb` | `--color-sky-blue` | Light blue accent for rotation |
| Sunshine Yellow | `#ffe747` | `--color-sunshine-yellow` | Warm highlight and cheerful card wash |
| Lavender Glow | `#b977f8` | `--color-lavender-glow` | Soft border and icon accent |
| Pale Violet | `#dab2ff` | `--color-pale-violet` | Outlined button border and light accent stroke |
| Lilac Mist | `#f3e8ff` | `--color-lilac-mist` | Pale violet wash for subtle UI states |
| Deep Violet | `#8200db` | `--color-deep-violet` | Saturated icon stroke and accent outline |
| Coral Red | `#ee5968` | `--color-coral-red` | Mascot and illustration warmth |
| Mint Green | `#58df8c` | `--color-mint-green` | Soft green emphasis and decorative fill |
| Forest Green | `#00a63e` | `--color-forest-green` | Small green graphic marks |
| Burnt Orange | `#eb6928` | `--color-burnt-orange` | Warm outline, icon stroke, illustration detail |
| Deep Teal | `#2c91af` | `--color-deep-teal` | Cool stroke and informational accent |
| Magenta Bloom | `#b036a4` | `--color-magenta-bloom` | Magenta icon border and decorative stroke |
| Mint Wash | `#dcfce7` | `--color-mint-wash` | Pale green wash for soft highlight areas |

## Tokens - Typography

- Display family: `new-kansas`, with `DM Serif Display` or a high-quality editorial serif as fallback.
- Body/UI family: `Nunito Sans`, then `ui-sans-serif`.
- Display usage: 48px to 64px, weight 400 or 500, loose and calm.
- Body usage: 14px to 18px, mostly 400 to 600.
- UI labels: 12px to 15px, usually medium or semibold.

| Step | Size | Weight | Line height | Suggested role |
|------|------|--------|-------------|----------------|
| Caption | 12px | 400-700 | 1.33-1.5 | Tiny labels, metadata, helper text |
| Body Small | 14px | 400-700 | 1.43 | Secondary text, nav, compact cards |
| UI Medium | 15px | 600 | 1.33 | Buttons and nav pills |
| Body | 16px | 400-700 | 1.5 | Main body copy and forms |
| Body Large | 18px | 400-700 | 1.56 | Lead copy and card text |
| Subheading | 20px | 400-700 | 1.4 | Small section headings |
| Heading Small | 28px | 500 | 1.2-1.35 | Compact serif headings |
| Heading | 48px | 400-500 | 1.2 | Hero and section headlines |
| Display | 64px | 400-500 | 1.2 | Large hero moments |

## Tokens - Spacing And Shape

| Purpose | Value |
|---------|-------|
| Density | compact |
| Max width | 1200px |
| Section gap | 64px |
| Card padding | 16px |
| Element gap | 8px |
| Spacing scale | 4, 5, 6, 8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 73, 80, 96px |
| Cards | 12px radius |
| Inputs | 12px radius |
| Buttons | 12px radius |
| Large cards | 16px radius |
| Special panels | 24px radius |
| Pills and chips | 9999px radius |

## Components

- Hero: full viewport or near-full viewport, centered text, dark twilight gradient, floating product cards, and a bottom-corner mascot or object.
- Navigation: floating top bar, transparent over hero and cream over content, with compact labels.
- Buttons: neutral filled white or ink buttons with 12px radius; colorful CTAs are handled by borders, accents, and surrounding details.
- Chips: full pill geometry with 9999px radius and compact type.
- Cards: 12px rounded, thin warm border, light cream or paper white fill, warm shadow.
- Feature cards: rotate pastel fills rather than using one dominant accent.
- Tabs: simple text tabs with underline or quiet active state.
- Prompt panels: white cards on top of illustrated or atmospheric backgrounds.
- Logo bars: one centered horizontal row with generous gaps.

## Layout And Imagery

The layout uses a centered 1200px content model. The first screen is atmospheric, but later sections become more product-readable. Alternate dark sky sections with parchment and paper sections. Keep grids simple and avoid dense admin-table behavior.

Imagery can include 3D mascots, floating UI cards, cloud or twilight gradients, and pastel shapes. The key is tactile layering: cream paper surfaces over dusk atmosphere, not decorative blobs everywhere.

## Do

- Use `new-kansas` or a close editorial serif for 48px to 64px display headlines.
- Use `Parchment Cream` as the default canvas instead of pure white.
- Keep cards, buttons, and inputs at 12px radius.
- Reserve 9999px radius for tags, suggestion chips, and true pills.
- Use warm tinted shadows and borders so surfaces feel like paper.
- Rotate violet, pink, orange, teal, blue, yellow, and green accents across cards.
- Use `Ink Black` for primary text and structural outlines.

## Do Not

- Do not bold display headlines into a heavy corporate voice.
- Do not use pure white as the page background except for elevated panels.
- Do not use pure black for normal text when `Ink Black` is available.
- Do not add heavy gray or black drop shadows.
- Do not turn the main CTA into a flat solid violet button.
- Do not introduce arbitrary radii outside 12px, 16px, 24px, and 9999px.
- Do not use the serif family for small body text.
