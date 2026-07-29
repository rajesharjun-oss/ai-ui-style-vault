# PLATFORM - Style Reference

## North Star

Build the interface like a white cube gallery catalog pinned to the wall: pure white canvas, pure black lines, compact typography, sharp geometry, and art as the only color. The UI should feel editorial, sparse, and precise, never decorative.

## Theme

Light. Bone White is the page and card surface. Lamp Black is the only structural UI color. Gray values are used only for captions, helper text, borders, and dividers.

## Color Tokens

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Lamp Black | `#000000` | `--color-lamp-black` | Primary text, card and nav borders, links, icons, structural UI |
| Graphite | `#808080` | `--color-graphite` | Secondary captions, timestamps, de-emphasized metadata |
| Iron Gray | `#aaaaaa` | `--color-iron-gray` | Tertiary captions, breadcrumb separators, fine print |
| Smoke Gray | `#b3b3b3` | `--color-smoke-gray` | Muted helper text, metadata captions, placeholder labels |
| Concrete Gray | `#cccccc` | `--color-concrete-gray` | Secondary borders, input outlines, disabled states |
| Ash Gray | `#dddddd` | `--color-ash-gray` | Hairline dividers and subtle surface separation |
| Bone White | `#ffffff` | `--color-bone-white` | Page background, card surfaces, negative space |

## Typography

Use MediumLLWeb if available. Fallback to Sohne, Inter, Neue Haas Grotesk, or another restrained neo-grotesque.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 12px | 500 | 1.2 | 0.01em |
| Body Small | 15px | 400 | 1.2 | 0.01em |
| Subheading | 20px | 500 | 1.15 | 0.01em |
| Heading | 48px | 400 | 1.15 | 0.02em |
| Display | 72px | 400 | 1 | 0.02em |

Rules:

- Use one typeface across the entire site.
- Use 400 as the default weight for body, navigation, headings, and long text.
- Reserve 500 for labels, artist names, prices, and compact metadata emphasis.
- Use only five sizes: 12px, 15px, 20px, 48px, and 72px.
- Use tabular numerals for prices and numeric metadata.
- Do not add intermediate body sizes.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | Compact |
| Max width | 1280px |
| Section gap | 72px |
| Card padding | 30px |
| Element gap | 10px |

Spacing scale: 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 18, 20, 30, 36, 72, 122.

Radius scale:

- Tags: 0px.
- Cards: 0px.
- Badges: 0px.
- Inputs: 0px.
- Buttons: 0px.
- Images inside catalog cards: 0px.

Elevation:

- No shadows.
- No glows.
- No blur effects.
- Use only 1px borders and gray band color shifts.

## Components

### Top Navigation Bar

Use a flat horizontal bar with Bone White background, 0px radius, and 1px Lamp Black bottom border. Left side contains `PLATFORM:` at 12px MediumLLWeb 500 uppercase, followed by 15px 400-weight links such as Shop, Objects, and Artists. Right side contains region selector, account icon, saved items, and search. Use 6px vertical padding and 20px to 40px horizontal padding.

### Hero Spotlight Banner

Use a full-bleed dark artwork or editorial photograph filling the viewport. Center overlay type: `SPOTLIGHT:` at 48px 400 weight and artist name at 72px 400 weight, both Bone White. Add 15px centered subtext and a plain Explore now text link. No button chrome and no card wrapper.

### Section Header Band

Use an edge-to-edge Ash Gray band or hairline-separated band. Left column uses a 12px 500 uppercase section label. Center column uses 15px 400 descriptive text. Right column uses a 15px underlined text link. Use a 1px Lamp Black bottom border.

### Artwork Card

Use 0px radius, 1px Lamp Black border, no shadow, and Bone White background. Artwork image fills the card width edge-to-edge with 1:1 or 3:4 aspect ratio. Metadata below is centered: artist name at 12px 500 uppercase, title and year at 15px 400, medium at 15px 400, and price at 12px 500 with tabular numerals. Use about 20px padding below the image.

### Artwork Grid

Use 4 columns on desktop, 2 on tablet, 1 on mobile. Use equal column widths, 20px to 30px gutters, and consistent image-to-text ratios. The grid sits directly below the section header band without extra decorative spacing.

### Text Link

Use plain underlined Lamp Black text at 15px 400 weight. Directional links may include a simple leading chevron character in implementation if supported. No button background, no color change on hover; hover may thicken underline or shift to 500 weight.

### Ghost Icon Button

Use icon-only controls with 0px radius, no background, no border, and Lamp Black stroke or fill. Use 4px to 6px padding around account, saved items, search, or save icons.

### Body Text Block

Use 15px MediumLLWeb, 400 weight, 1.20 line-height, Lamp Black text, and a max-width near 640px. Use for descriptions, artist bios, and zone introductions. Long-form text is left-aligned.

### Metadata Caption

Use a centered stack under each artwork. Artist name is 12px 500 uppercase, title/year and medium are 15px 400, price is 12px 500, all Lamp Black. Enable tabular numerals for price alignment.

### Footer

Use Bone White background with a 1px Lamp Black top border. Use multi-column link lists at 15px 400. Bottom row uses 12px text for copyright and legal links. Keep it flat and undecorated.

### Search Input

Use transparent background and only a 1px Lamp Black bottom border. Placeholder is 15px Smoke Gray. No full input box and no radius. Search icon sits inline at the right.

## Layout And Imagery

- Use a full-bleed hero, then vertical catalog flow.
- Card grid and text blocks sit inside a 1280px max-width container.
- Hero and section header bands stretch edge-to-edge.
- Each content zone opens with a section band, then an artwork grid.
- The main flow is nav, hero, zone band, grid, zone band, grid, footer.
- Avoid sidebars and breadcrumb-heavy layouts in the main flow.
- Imagery is fine-art photography and artwork product crops.
- Artwork should be isolated for inspection on white.
- No lifestyle photography, human models, decorative illustrations, or colored badges.

## Do

- Use only Lamp Black for text, borders, links, and interactive elements.
- Set every UI radius to 0px.
- Use MediumLLWeb 400 as the default type weight.
- Reserve 500 for labels, artist names, and prices.
- Use 1px Lamp Black borders for card outlines, nav separation, and section dividers.
- Keep the type scale to 12px, 15px, 20px, 48px, and 72px.
- Use tabular numerals for prices and metadata.
- Maintain a 1280px max-width with generous side margins.

## Do Not

- Do not add rounded corners.
- Do not introduce shadows, glows, or blur effects.
- Do not use color for UI hierarchy.
- Do not use gradient backgrounds.
- Do not use 13px to 17px body sizes; the compact 15px rhythm is intentional.
- Do not center long-form body copy.
- Do not add colored badges, tags, or status pills.
