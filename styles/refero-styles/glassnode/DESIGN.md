# Glassnode Design Reference

## North Star

Build an institutional data product that feels like a financial research console behind glass walls. The interface should be cool, precise, analytical, and restrained: gray canvas, white cards, black text, hairline borders, 2px geometry, and chart-native imagery.

The design should communicate authority through data density, typographic weight, and disciplined spacing rather than decorative color.

## Theme

- Mode: mixed.
- Default canvas: cool light gray.
- Card surface: white.
- Dark sections: near-black.
- Accent: pale lavender wash only.
- Action style: black/white neutral, no chromatic CTA.
- Geometry: near-rectangular 2px radius.

## Color System

Core colors:

- Pure Black: `#000000` for text, icons, strong contrast, and filled light-surface actions.
- Obsidian: `#1a1a1a` for dark bands, footer, announcement bar, and dark surfaces.
- Graphite: `#333333` for secondary headings and nav text.
- Iron: `#5a5a5a` for muted body copy and helper text.
- Slate: `#666666` for de-emphasized paragraphs.
- Steel: `#808080` for placeholders, disabled states, and input borders.
- Fog: `#a0a0a0` for muted text, icon strokes, and subtle dark-band copy.
- Ash: `#bfbfbf` for light dividers and icon strokes on light surfaces.
- Mist: `#dedfe1` for card outlines, hairline borders, and dividers.
- Cloud: `#edeff2` for page canvas and spaces between bands.
- Paper: `#f7f8fa` for light section backgrounds and subtle inset panels.
- White: `#ffffff` for cards, inputs, elevated surfaces, and text on dark.
- Glacier Tint: `#e2e7fc` for soft accent wash, selected states, and chart fill.
- Badge Slate: `#6f6f6f` for small uppercase labels.

## Typography

Primary family: Inter.  
Hero display family: Fraktion.

Inter:

- Use for body copy, navigation, buttons, badges, cards, UI labels, and all subheadings.
- Use 400 for normal copy.
- Use 500 for controls and navigation.
- Use 700 for headings and report titles.
- Keep default letter spacing.

Fraktion:

- Use only for the primary 56px hero H1.
- Use weight 700.
- Fall back to a geometric bold sans when unavailable.
- Do not use it for small labels, cards, nav, or body copy.

Type scale:

- Caption: 12px, line-height 1.4.
- Body small: 14px, line-height 1.5.
- Body: 16px, line-height 1.5.
- Subheading: 20px, line-height 1.4.
- Heading small: 24px, line-height 1.3.
- Heading: 32px, line-height 1.2.
- Display: 56px, line-height 1.2.

## Layout

- Page max width: 1200px.
- Base unit: 8px.
- Section gap: 80px.
- Card padding: 16px.
- Element gap: 16px.
- Use full-width light and dark bands.
- Use a 2-column hero: copy and CTA on the left, chart widget on the right.
- Follow with alternating dark feature blocks, light report grids, and a dark subscribe section.

The rhythm should feel like dashboard plus editorial report.

## Shape

- Nav: 2px radius.
- Tags: 2px radius.
- Cards: 2px radius.
- Inputs: 2px radius.
- Buttons: 2px radius.

Do not round beyond 2px unless a browser focus ring visually requires it.

## Elevation

Use almost no shadow.

Allowed shadows:

- Primary filled button: `rgba(0, 0, 0, 0.04) 0px 2px 4px 0px`.
- Hero chart widget: `rgba(0, 0, 0, 0.04) 0px 2px 4px 0px, rgba(0, 0, 0, 0.08) 0px 8px 32px 0px`.

Everything else should be separated by 1px borders and surface contrast.

## Imagery

Use data visualizations rather than lifestyle photography:

- Line charts with blue strokes over pale lavender fills.
- Abstract chart illustrations on dark bands.
- Rectangular report covers.
- Monochrome partner logos.
- Product widgets that look like credible live data, not decoration.

## AI Build Notes

Start with a cloud-gray page, a strong 56px hero H1, neutral CTA pair, and a white chart widget. Then add a dark feature band and a white report-card grid. Keep the accent restrained to lavender washes and chart fills; never create a colorful brand palette.

