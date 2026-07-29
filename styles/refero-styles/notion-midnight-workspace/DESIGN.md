# Notion Midnight Workspace Design Reference

## North Star

A midnight workspace that opens into a warm editorial room. The first viewport is dramatic, dark, focused, and product-led. Below the fold, the page becomes readable and paper-like, with white cards, testimonials, and calm product explanations.

## Theme

Mixed, productivity-focused, polished SaaS, product-led, editorial below the fold.

## Palette

Use Midnight Ink `#02093a` as the defining dark hero canvas. It is navy, not black. Signal Blue `#0075de` is the only filled CTA color. Sky Tint, Royal Violet, and Periwinkle can appear as large decorative auras, mockup glow, or dark-stage accent surfaces.

Use Paper White `#f6f5f4` for light sections. It is warmer than pure white and gives below-the-fold content an editorial feel. Pure White `#ffffff` is reserved for elevated cards, inputs, and reversed text. Onyx `#000000` is text and border ink, not a background.

## Typography

NotionInter is the workhorse. Use it for body, navigation, UI labels, buttons, most headings, cards, testimonials, and product content. Use weight 500 for UI labels and buttons, 600 for below-the-fold section headings, and 700 for the hero display.

Lyon Text is a rare editorial accent. Use it at about 32px for one thoughtful section title or pull-quote-like heading. Do not use it for labels, navigation, or anything below 24px.

Hero type can reach 64px with line-height 1 and tight tracking. Below the fold, headings sit around 40px to 54px with generous section spacing.

## Layout

Use full-bleed bands. The page starts with a full-height or near-full-height Midnight Ink hero. Center the headline, subtext, and dual CTA row. Place a large product screenshot near the lower part of the hero, often overlapping the transition.

After the hero, use a logo band on the dark stage, then make a sharp transition into Paper White sections. Do not blend the two stages with a gradient. The light sections use a centered 1200px max-width layout, large headings, product cards, and testimonial grids.

## Surfaces And Elevation

Hero product mockups can float with soft multi-layer shadows because they are objects staged on the dark canvas. Below the fold, product cards are much quieter: white surfaces, 12px radius, clean layout, and little or no shadow.

Keep each card either midnight-stage or paper-stage. Do not combine dark header blocks and light body blocks inside the same card unless the reference component explicitly needs it.

## Components

Primary CTAs use Signal Blue fill, Pure White text, 8px radius, and NotionInter weight 500. Ghost actions are text-only or transparent buttons, matching the current surface.

Product screenshot cards are the hero visual. Use 12px radius and present real app UI. The screenshot is content, not decoration.

Pill badges use 9999px radius and soft blue background with Cerulean text. Use them sparingly for "New" or feature markers.

Testimonials use Pure White cards, 12px radius, 24px padding, and confident quote text.

## Imagery

Use product screenshots, UI mockups, dashboard crops, and small illustrated mascot or badge elements around the hero. Do not use lifestyle photography. The product is the main visual.

Gradients are allowed only as large decorative auras around product mockups or hero background accents. Do not apply gradients to text, borders, buttons, or small UI.

## Implementation Feel

The experience should feel like a serious product workspace turning into a thoughtful editorial explanation. The contrast between midnight stage and paper page is the key. Keep the transition sharp and intentional.
