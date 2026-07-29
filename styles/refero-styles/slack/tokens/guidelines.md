# Guidelines

## Do

- Use #611f69 for filled CTAs only never as background fills for hero sections or large surfaces; reserve #481a54 for those.
- Set display headlines at 64-96px using Salesforce-Avant-Garde with -0.012em tracking; the compressed wide forms are what make Slack's hero feel architectural.
- Apply the gradient text fill (black #ba01ff) to single keywords inside white-section headlines not to entire headlines or body copy.
- Use 16px radius on all cards and content surfaces; pair with 1px lavender (#eac8fe) borders instead of heavy shadows for the default card state.
- Reserve the 32px ambient shadow (rgba(0,0,0,0.1) 0px 0px 32px 0px) for product screenshot cards and floating overlays only not for static content cards.
- Alternate white canvas sections with #481a54 dark hero bands to create rhythm; use #f9f0ff as a quieter mid-tone when transitioning without full inversion.
- Set eyebrow labels at 12px/700 with 0.057em uppercase tracking this is the tag pattern for 'New Feature' and section categories.

## Do Not

- Do not use pill-radius (999px) on primary CTA buttons Slack's filled actions are always rectangular with 4px corners.
- Do not apply the #eac8fe lavender border to product screenshot cards those need white or transparent backgrounds to let the embedded UI breathe.
- Do not use Vivid Violet (#9602c7) or Iris Light (#d17dfe) for body text on white backgrounds contrast ratios are too low; reserve for dark-section accents and card-only contexts.
- Do not mix Channel Blue (#1264a3) into marketing-page CTAs that blue belongs inside Slack product UI screenshots, not the marketing chrome.
- Do not add drop shadows to text inside the dark hero band; the band itself provides enough contrast.
- Do not use gradient fills on UI surfaces (buttons, cards, inputs) the gradient treatment is text-only and decorative.
- Do not set body copy below 14px or above 18px; the 16px/1.5 lineHeight is the working standard for readability across marketing and feature copy.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
