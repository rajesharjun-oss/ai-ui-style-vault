# Grafbase

Source: [Refero Style](https://styles.refero.design/style/1c1d3939-8d82-4907-aa3c-c9b2fcfbab4f) 
Reference site: [https://grafbase.com](https://grafbase.com) 
Captured: 2026-07-29 
Refero published: 2026-01-25T11:19:26.000Z 
Refero modified: 2026-06-03T16:06:30.187Z 
Theme: light 
Category: Dev Tools

## Style Summary

Explore Grafbase's light Dev Tools design system: Graphite Ink #1b1b1b, Marble #ffffff colors, Inter, sans (custom utility) typography, and DESIGN.md for AI...

North star: engineering blueprint on cool marble

## What To Borrow

- Graphite Ink `#1b1b1b` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Marble `#ffffff` for Card surfaces, elevated panels, nav background, button text on dark fills. The brightest layer in the system
- Drafting Gray `#eaeaea` for Page canvas and section backgrounds. The second surface tier beneath white cards - the tone of the drafting table itself
- Steel `#60646c` for Secondary body text, subtext, helper copy. Carries information density without competing with primary headings
- Ash `#7c7c7c` for Muted tertiary text and less-emphasized metadata. Used where information recedes
- Hairline `#e0e1e6` for 1px borders, card outlines, divider rules. The system's structural lines - cool-tinted to read as architectural, not decorative
- Mint Signal `#00f2e6` for Saturated cyan-mint used inside product UI mockups and integration icon tiles. Not an interface accent - it is product-content color bleeding into marketing surfaces
- Moss `#8dc63f` for Secondary chromatic accent appearing in product screenshot data and integration tiles. Sits next to Mint Signal in the same icon/system cluster
- Sky `#00b9f1` for Tertiary accent in product UI and integration iconography. Completes the cool triad (mint, moss, sky) that defines the brand's chromatic fingerprint within screenshots

- Inter `--font-inter` for Sole typeface. Display uses weight 600 at 90px with -0.05em tracking (about -4.5px) - headline authority through geometric compression rather than heaviness. Headings at 40px use weight 500 with -0.025em tracking for a slightly looser, more editorial register. Body at 16px stays at weight 400 with normal tracking. The 13/14px sizes handle UI chrome and captions. No system fonts, no second family - Inter is the brand.
- sans (custom utility) `--font-sans-custom-utility` for Rare fallback utility class. Treat as Inter - likely a Tailwind 'sans' alias that resolved to a custom stack. Do not introduce as a distinct type family in output.

## Avoid

- Do not add saturated accent colors to the interface - the system is intentionally 99% achromatic.
- Do not use pure black (#000000); use Graphite Ink (#1b1b1b) which is softer against the cool gray canvas.
- Do not introduce a second typeface - Inter is the system, used at every size from 13px caption to 90px display.
- Do not set letter-spacing to 0 on display and heading text - the -4.5px / -1px tracking is what makes the large type feel engineered rather than webby.
- Do not add drop shadows to ghost buttons, cards, or nav - the shadow belongs only on the primary action button and the hero preview panel.
- Do not create button variants with new colors for hover/active states - swap to a slight opacity reduction or a subtle bg-gray-100 treatment instead.
- Do not place the green-to-teal gradient anywhere other than the top announcement bar - it is a one-shot signal, not a reusable surface.

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
