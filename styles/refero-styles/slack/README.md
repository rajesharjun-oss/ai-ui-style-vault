# Slack

Source: [Refero Style](https://styles.refero.design/style/e26cb9b0-f876-41ff-9f24-fd67a6b9776c)  
Reference site: [https://slack.com](https://slack.com)  
Captured: 2026-07-29  
Refero published: 2026-02-24T12:54:51.000Z  
Refero modified: 2026-07-03T10:57:19.944Z  
Theme: light  
Category: SaaS

## Style Summary

Explore Slack's light SaaS design system: Aubergine #611f69, Deep Plum #481a54 colors, Salesforce-Avant-Garde, Salesforce-Sans typography, and DESIGN.md for...

North star: Aubergine stage with white spotlights. Deep plum dominates dark sections while a near-white canvas lets oversized Avant-Garde headlines breathe.

## What To Borrow

- Aubergine `#611f69` as Filled CTA buttons, primary navigation fills, dark hero backgrounds the brand's signature mid-plum, dense enough to ground without veering black
- Deep Plum `#481a54` as Largest canvas inversion full-bleed dark section backgrounds, decorative dark blocks, surface for headline text on white sections
- Purple Haze `#f9f0ff` as Softest lilac wash for body backgrounds, pill fills, and card surfaces the quiet brand tint that never competes with text
- Lavender Mist `#eac8fe` as Mid-saturation lavender for card borders, decorative outlines, and pill borders bridges white and purple without harsh contrast
- Vivid Violet `linear-gradient(104deg, rgb(0, 0, 0) 9.56%, rgb(186, 1, 255) 102.66%)` as Headline accent text and gradient text fills on dark sections the bright punch of color that makes key phrases feel switched on; Diagonal black-to-violet gradient for accent text and decorative text fills on dark section...
- Plum Shadow `#3d0157` as Darker plum for button text and shadow tones on aubergine surfaces reads as near-black against purple fills
- Salesforce-Avant-Garde Display and heading face geometric, wide, compressed. Carries every headline from 21px subheads up to 96px hero display. The 400-weight at 76px is anti-convention: Slack trusts its letterforms enough to let headlines whisper rather than shout. Tracking tightens progressively from -0.004em at body sizes to -0.012em at 64px+ `--font-salesforce-avant-garde` for the source typography voice
- Salesforce-Sans Workhorse body and UI face handles nav, body copy, buttons, captions, and labels. The 12px/700 with 0.057em tracking (uppercase) is the eyebrow-label pattern used for section tags. Body sits at 16px/1.5 generous enough for reading, compact enough for dense product cards `--font-salesforce-sans` for the source typography voice
- source-defined base spacing with comfortable density
- Source radius system: tags 4px, cards 16px, pills 999px, badges 90px

## Avoid

- Do not use pill-radius (999px) on primary CTA buttons Slack's filled actions are always rectangular with 4px corners.
- Do not apply the #eac8fe lavender border to product screenshot cards those need white or transparent backgrounds to let the embedded UI breathe.
- Do not use Vivid Violet (#9602c7) or Iris Light (#d17dfe) for body text on white backgrounds contrast ratios are too low; reserve for dark-section accents and card-only contexts.
- Do not mix Channel Blue (#1264a3) into marketing-page CTAs that blue belongs inside Slack product UI screenshots, not the marketing chrome.
- Do not add drop shadows to text inside the dark hero band; the band itself provides enough contrast.
- Do not use gradient fills on UI surfaces (buttons, cards, inputs) the gradient treatment is text-only and decorative.
- Do not set body copy below 14px or above 18px; the 16px/1.5 lineHeight is the working standard for readability across marketing and feature copy.

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
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
