# AI Implementation Prompt

Build a Daniellelevitt-inspired interface using this source-derived style bundle.

Reference site: https://www.daniellelevitt.com
Theme: mixed
Category: Agency
North star: Punk broadsheet at billboard scale - a flat acid-mint field cracked open by a slab of vermillion condensed type the size of a car door.

Use these palette anchors:

- Vermillion `#d15022` for Display type, navigation, outlined action borders, section headings - burnt orange against white and mint creates the system's only chromatic voice; it carries every heading, every link, and the massive name lockup
- Acid Mint `#75dfb5` for Green action color for filled buttons, selected navigation states, and focused conversion moments
- Pure Black `#000000` for Image borders, hairline dividers, secondary borders, and body-text outlines where Vermillion isn't used - the structural ink that frames every photograph
- Paper White `#ffffff` for Primary canvas behind image collages and the opening viewport - flat, untextured, the gallery wall on which the photographs are pinned

Use these typography anchors:

- Helvetica Now Display `--font-helvetica-now-display` for Body emphasis, navigation labels, sub-headings, image captions, link text - the non-display workhorse at 29px bold for the bio statement and 18px for running text. The 800 weight everywhere (no medium, no regular) is a signature choice: the system never steps down from maximum volume.
- Helvetica Now Display Condensed `--font-helvetica-now-display-condensed` for Display name lockup and section-spanning hero type - the ultra-condensed bold at 72px+ fills viewports and overlaps photography. The condensation is the brand's signature: standard Helvetica at 800 wouldn't create the same monolithic, poster-scale letters that define the site's identity.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 50px.
- Card padding: 0px.
- Element gap: 20px.

Build these component patterns where relevant:

- Display Name Lockup: Site-defining typographic element
- Image Collage Block: Editorial photo arrangement on white canvas
- Bio Statement Block: Primary descriptive text
- Minimal Navigation: Site wayfinding
- Outlined Action Link: Outlined/ghost link treatment
- Full-Bleed Section Background: Page-level color band
- Image Frame Border: Photograph containment

Do:

- Use Vermillion (#d15022) for all display type, headings, and navigation - it is the only chromatic voice in the system
- Set all type at weight 800 - the system never steps down to medium or regular; 29px bold IS the body weight
- Use Helvetica Now Display Condensed 800 at 72px+ with lineHeight 0.95 for any display or section-spanning text
- Use 0px border-radius on every element - images, buttons, tags, cards all have hard rectangular edges
- Frame every photograph with a 1-2px Pure Black (#000000) border
- Let display type bleed to viewport edges - never constrain with max-width or padding around the name lockup
- Use Acid Mint (#75dfb5) as a full-bleed section background, never as a card surface or accent fill

Avoid:

- Don't introduce a second body weight below 800 - medium and regular have no place in this system
- Don't add drop shadows, gradients, or any elevation - the system is completely flat
- Don't use rounded corners on images, buttons, or containers - 0px radius is non-negotiable
- Don't constrain the layout to a max-width container - the editorial poster aesthetic requires full-bleed
- Don't add a third color - the palette is strictly Vermillion, Acid Mint, Black, and White
- Don't separate type and photography into stacked rows - they should overlap and share the same plane
- Don't use a standard sans-serif at body sizes - even 18px and 29px text must be 800 weight to match the system's volume

Source prompt cues:

**Quick Color Reference:**
- Text/Heading: #d15022 (Vermillion)
- Background (light section): #ffffff (Paper White)
- Background (accent section): #75dfb5 (Acid Mint)
- Borders/Image frames: #000000 (Pure Black)
- Outlined action border: #d15022 (Vermillion)
- primary action: #d15022 (outlined action border)

**Example Component Prompts:**

1. **Display Name Lockup**: Full-bleed section. Background: #75dfb5 (Acid Mint). Text: 'Danielle Levitt' in Helvetica Now Display Condensed 800, 72px, #d15022 (Vermillion), lineHeight 0.95, letter-spacing -0.72px. Text bleeds to viewport edges. No padding, no max-width.

2. **Image Collage Block**: White (#ffffff) canvas. Three editorial photographs at varied sizes (roughly 200x300, 350x250, 250x350px), each with 0px radius and 1.5px #000000 border. Images overlap each other asymmetrically, with a 72px Helvetica Now Display Condensed 800 #d15022 text element positioned behind one of the images, partially visible.

3. **Bio Statement**: Acid Mint (#75dfb5) full-bleed background. Text: 'Danielle Levitt is a film director and photographer whose work covers two decades of documenting music, art, fashion, and celebrity.' Set in Helvetica Now Display 800, 29px, #d15022 (Vermillion), lineHeight 1.0, letter-spacing -0.29px. Centered, with 20px margin-top from the display lockup above.

4. **Outlined Link**: Transparent background. 1.5px #d15022 (Vermillion) border, 12px 24px padding. Text: 'Studio:' in Helvetica Now Display 800, 18px, #d15022, letter-spacing -0.18px. No fill, no shadow.

5. **Navigation Bar**: Paper White (#ffffff) background, 20px padding from viewport edges. Top-left: 'D - L' in Helvetica Now Display 800, 18px, #d15022. Top-right: 'Menu' in the same style. 1px #000000 bottom border.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
