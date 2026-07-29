# Slack Design Reference

## North Star

Aubergine stage with white spotlights. Deep plum dominates dark sections while a near-white canvas lets oversized Avant-Garde headlines breathe.

## Theme

light style for SaaS interfaces.

## Color System

- Aubergine `#611f69` for Filled CTA buttons, primary navigation fills, dark hero backgrounds the brand's signature mid-plum, dense enough to ground without veering black
- Deep Plum `#481a54` for Largest canvas inversion full-bleed dark section backgrounds, decorative dark blocks, surface for headline text on white sections
- Purple Haze `#f9f0ff` for Softest lilac wash for body backgrounds, pill fills, and card surfaces the quiet brand tint that never competes with text
- Lavender Mist `#eac8fe` for Mid-saturation lavender for card borders, decorative outlines, and pill borders bridges white and purple without harsh contrast
- Vivid Violet `linear-gradient(104deg, rgb(0, 0, 0) 9.56%, rgb(186, 1, 255) 102.66%)` for Headline accent text and gradient text fills on dark sections the bright punch of color that makes key phrases feel switched on; Diagonal black-to-violet gradient for accent text and decorative text fills on dark section...
- Plum Shadow `#3d0157` for Darker plum for button text and shadow tones on aubergine surfaces reads as near-black against purple fills
- Iris `#730394` for Secondary purple for background fills and link accents sits between Aubergine and Vivid Violet on the purple ramp
- Iris Light `#d17dfe` for Decorative card text and bright accents inside feature cards a lighter iris that adds lift without losing brand identity

Use the listed source colors as the authoritative palette. Keep the most saturated or highest-contrast color for primary action moments unless the component notes say otherwise.

## Typography

- Salesforce-Avant-Garde Display and heading face geometric, wide, compressed. Carries every headline from 21px subheads up to 96px hero display. The 400-weight at 76px is anti-convention: Slack trusts its letterforms enough to let headlines whisper rather than shout. Tracking tightens progressively from -0.004em at body sizes to -0.012em at 64px+ `--font-salesforce-avant-garde`
- Salesforce-Sans Workhorse body and UI face handles nav, body copy, buttons, captions, and labels. The 12px/700 with 0.057em tracking (uppercase) is the eyebrow-label pattern used for section tags. Body sits at 16px/1.5 generous enough for reading, compact enough for dense product cards `--font-salesforce-sans`

Use the source font pairing to preserve the visual voice. When custom fonts are not available, choose close substitutes with similar weight, width, and editorial character.

## Layout And Spacing

- Base unit: source-defined
- Density: comfortable
- Page max-width: 1200px
- Section gap: 80-100px
- Card padding: 24px
- Element gap: 8-12px

## Components

- Primary CTA Button (Aubergine Fill): Main conversion action
- Ghost CTA Button: Secondary action beside primary CTA
- Nav Pill Button: Sticky navigation action
- Header Request Demo Link: Low-emphasis nav link
- Sign In Link: Account access
- Feature Card (Lavender Border): Content card with subtle brand frame
- Product Screenshot Card: Large product UI embed
- Floating Sticky Nav: Persistent top navigation

## Implementation Guidance

- Use #611f69 for filled CTAs only never as background fills for hero sections or large surfaces; reserve #481a54 for those.
- Set display headlines at 64-96px using Salesforce-Avant-Garde with -0.012em tracking; the compressed wide forms are what make Slack's hero feel architectural.
- Apply the gradient text fill (black #ba01ff) to single keywords inside white-section headlines not to entire headlines or body copy.
- Use 16px radius on all cards and content surfaces; pair with 1px lavender (#eac8fe) borders instead of heavy shadows for the default card state.
- Reserve the 32px ambient shadow (rgba(0,0,0,0.1) 0px 0px 32px 0px) for product screenshot cards and floating overlays only not for static content cards.
- Alternate white canvas sections with #481a54 dark hero bands to create rhythm; use #f9f0ff as a quieter mid-tone when transitioning without full inversion.
- Set eyebrow labels at 12px/700 with 0.057em uppercase tracking this is the tag pattern for 'New Feature' and section categories.

## Guardrails

- Do not use pill-radius (999px) on primary CTA buttons Slack's filled actions are always rectangular with 4px corners.
- Do not apply the #eac8fe lavender border to product screenshot cards those need white or transparent backgrounds to let the embedded UI breathe.
- Do not use Vivid Violet (#9602c7) or Iris Light (#d17dfe) for body text on white backgrounds contrast ratios are too low; reserve for dark-section accents and card-only contexts.
- Do not mix Channel Blue (#1264a3) into marketing-page CTAs that blue belongs inside Slack product UI screenshots, not the marketing chrome.
- Do not add drop shadows to text inside the dark hero band; the band itself provides enough contrast.
- Do not use gradient fills on UI surfaces (buttons, cards, inputs) the gradient treatment is text-only and decorative.
- Do not set body copy below 14px or above 18px; the 16px/1.5 lineHeight is the working standard for readability across marketing and feature copy.
