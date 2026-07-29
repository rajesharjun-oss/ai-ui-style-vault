# cord.com Design Reference

## North Star

Build a calm, polished recruiting marketplace that feels like a deep-ocean signal station on a white sea-fog canvas. The interface should be airy, centered, and human: navy typography, one bright blue action color, rounded search controls, photo-led company cards, and a single dark CTA banner as the tonal break.

The design is approachable despite its serious navy palette because the shapes are generous and the imagery is authentic.

## Theme

- Mode: light.
- Canvas: white.
- Primary text: navy, not black.
- Accent: signal blue.
- Status color: teal only for presence and response signals.
- Geometry: soft 20-24px rounding.
- Elevation: blue-tinted shadows.

## Color System

Core colors:

- Midnight Harbor: `#0b3658` for primary text, headings, logo grounding, and the dark CTA banner.
- Signal Blue: `#4e9ad9` for the logo, primary buttons, active nav, selected toggles, and active-state labels.
- Slate Channel: `#486984` for secondary text, muted icons, and outline-link treatment.
- Pale Steel: `#688dac` for tertiary text, labels, and light meta.
- Sea Fog: `#dde7ee` for borders, image borders, underlines, and hairlines.
- Ice Tint: `#e6f1fa` for hover surfaces, active toggle fills, tinted input background, and status badge fill.
- Light Mist: `#c8d8e4` for disabled or secondary fills.
- Canvas White: `#ffffff` for the page, cards, and button text.
- Active Teal: `#42b3b1` for presence, live, and response-status signals only.

Do not use pure black for primary text. The navy is the brand voice.

## Typography

Primary family: Figtree.  
Substitutes: Inter, DM Sans, Plus Jakarta Sans.

Rules:

- Use one type family across the interface.
- Use 400 for body.
- Use 600 for buttons, chips, and emphasis.
- Use 700 for card names and smaller headings.
- Use 800 for display headlines.
- Apply subtle negative tracking as type gets larger.
- Keep the hero headline heavy enough to feel stamped.

Type scale:

- Caption: 10px, line-height 1.5, tracking 0.1px.
- Body small: 14px, line-height 1.4, tracking -0.07px.
- Body: 16px, line-height 1.5, tracking -0.08px.
- Subheading: 18px, line-height 1.4, tracking -0.09px.
- Heading small: 20px, line-height 1.3, tracking -0.1px.
- Heading: 24px, line-height 1.3, tracking -0.12px.
- Heading large: 32px, line-height 1.25, tracking -0.16px.
- Display: 48px, line-height 1.2, tracking -0.24px.
- Hero: 100px, line-height 1, tracking -0.5px.

## Layout

- Page max width: 1200px.
- Base unit: 4px.
- Section gap: 64px.
- Card padding: 20px.
- Element gap: 12px.
- Hero is vertically stacked and centered.
- Company grid uses 3 columns on desktop.
- Dark CTA banner is full-bleed and appears near the page end.
- Footer is a 4-column link grid.

Hero order:

1. Minimal nav.
2. Toggle pill.
3. 100px two-line hero headline.
4. Subtitle.
5. Search input.
6. Filter chip row.

## Shape

- Cards: 20px radius.
- Images: 20px radius.
- Buttons: 24px radius.
- Inputs: 24px radius.
- Pills: 35px radius.
- Badges: 5px radius.
- Filter chips: 8px radius.

The rounding is a core brand pillar. Avoid sharp corners.

## Elevation

Use blue-tinted shadows only:

- Card: `0px 12px 48px 0px rgba(11, 54, 88, 0.08)`.
- Subtle card: `0px 4px 32px 0px rgba(11, 54, 88, 0.08)`.
- Button hover: `0px 4px 12px 0px rgba(11, 54, 88, 0.04)`.

Avoid generic gray shadows.

## Imagery

Imagery is authentic company photography:

- Team photos.
- Office and workplace scenes.
- Outdoor group images.
- Real profile avatars.
- Company logos under the image.

Images should be natural color, full-bleed inside cards, and rounded to match the card radius. Do not use abstract graphics or 3D renders.

## AI Build Notes

Start with a white canvas, navy hero, signal-blue CTA, and a wide pill search field. Add rounded company cards with full-bleed photos and blue-tinted elevation. Finish with one full-bleed navy CTA banner and a quiet footer.

