# Reducto

Source: [Refero Style](https://styles.refero.design/style/af55f85e-1c82-44c1-a8d0-32634bfa6296)
Reference site: [https://reducto.ai](https://reducto.ai)
Captured: 2026-07-31
Refero published: 2026-04-30T00:25:22.041Z
Refero modified: 2026-06-05T08:44:40.882Z
Theme: light
Category: AI

## Style Summary

Explore Reducto's light AI design system: Aubergine #310632, Magenta Pulse #9d17a0 colors, reductoSerif, Inter typography, and DESIGN.md for AI agents.

North star: Magazine on warm paper

## What To Borrow

- Aubergine `#310632` for Primary text, headline color, nav active state, link accent, footer text - the deep plum that replaces black across the entire interface, giving body copy a warm violet cast instead of cold gray
- Magenta Pulse `#9d17a0` for Filled primary action background, selected nav indicator, brand icon color - the single vivid hue permitted on a CTA, used sparingly so the click target glows against the paper canvas
- Damson `#690f6b` for Outlined action border, secondary button outline - a darker shade of the action magenta, used when a ghost/outlined button needs chromatic weight without the filled fill
- Lilac Wash `#dcbffb` for Violet text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Ochre `#a2541b` for Decorative icon accent, illustrative highlight - used inside product visualizations and tag chips to add warm contrast against the dominant magenta/plum palette
- Moss `#718613` for Decorative icon and illustration accent - secondary chromatic note for data visualization callouts, kept low-frequency
- Reed `#87a017` for Green text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Paper `#fafaf9` for Page canvas, hero background, nav background - the warm off-white that defines the entire site's surface; never pure #ffffff at the top level
- Vellum `#f5f5f4` for Secondary surface, elevated card background, subtle section differentiation
- Snow `#ffffff` for Pure card surface, button text on dark/magenta fills, icon fill - only used as a surface lift or as foreground text, never as the page canvas
- Sand `#d7ccc1` for Primary border color, hairline dividers, card outlines - the warm beige border that replaces cold gray; the single most-used border token across the system
- Driftwood `#e7e5e4` for Subtle border, decorative separator, low-contrast outline - lighter than Sand for secondary dividers
- Stone `#d6d3d1` for Nav border, button border, body border - mid-tone warm gray for structural outlines where more contrast is needed than Sand provides
- Graphite `#292524` for Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color
- Slate `#57534d` for Secondary heading text, icon stroke, strong body text - mid-dark warm gray for emphasis without going full black
- Pewter `#79716b` for Body text, nav text, button text on light backgrounds, helper text - the default readable text color, warm and low-contrast
- Bark `#44403b` for Neutral button treatment for secondary actions and selected controls.
- Ash `#a6a09b` for Muted helper text, disabled state, low-priority captions - the lightest readable neutral

- reductoSerif `--font-reductoserif` for Display and headline serif - the brand's signature voice. Set at 64-136px for hero/display, drops to 24-32px for section headings. Weight 470 is the workhorse (editorial body weight for a display face), weight 650 is reserved for stat numbers. The tight -0.01em tracking at every size is critical: it tightens the serif's natural rhythm into a modern, condensed look. Substituted with Playfair Display, Lora, or Source Serif Pro when unavailable.
- Inter `--font-inter` for Body and UI sans - the workhorse for nav links, buttons, descriptions, paragraphs, and form fields. Weight 400 for body, 500 for button labels and emphasized nav. Activates stylistic alternates 'salt' (single-storey 'a') and 'ss02' (open 'g') - these are essential to matching the brand; without them, Inter reads as generic.
- reductosans `--font-reductosans` for Compact UI sans for small labels, tag chips, micro-copy, and dense interface text where Inter feels too tall. Functionally overlaps with Inter but provides a tighter, more 'captured' rhythm for chrome.
- Reddit Mono `--font-reddit-mono` for Single-purpose display monospace for oversized stat numbers - the '2,000,000,000' counter. The -0.03em tracking pulls the mono's natural width inward so the number doesn't look like code, but a label. Substituted with JetBrains Mono or IBM Plex Mono.

## Avoid

- Don't use black (#000000) for body or heading text; use Graphite (#292524) or Aubergine (#310632) to keep the warm palette consistent.
- Don't apply drop shadows to cards or sections; depth must come from border color contrast or white-on-warm layering, not from blur shadows.
- Don't use cool gray (#6b7280, #94a3b8, etc.) for borders or text - every neutral in this system is warm (brown- or beige-tinted).
- Don't activate the magenta action color on more than one element per viewport section; if the CTA is magenta, the nav must stay neutral.
- Don't use the reductoSerif face for body copy or UI labels under 24px; it loses legibility below that and breaks the display/utility split.
- Don't introduce additional chromatic accent colors beyond Ochre, Moss, and Lilac; the palette intentionally restricts to plum-family + warm neutrals + 2-3 illustration accents.
- Don't use #0000ee or default browser link blue; all links must use Aubergine or Lilac Wash.

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
