# Components

### Top Bar
**Role:** Primary site navigation

Full-width black bar (#000000), fixed/sticky, 8px vertical padding, 20px horizontal padding. Left-aligned: brand name 'Klim Type Foundry' in white Sohne 16px regular, then 'Fonts' as a 16px Sohne link in Flare Orange (#d33c03). Right-aligned: hamburger menu icon in white. No drop shadow, no border - the bar sits as a pure black strip.

### Label Tag
**Role:** Collection or edition annotation

Inline rectangular tag with Flare Orange (#d33c03) background, white Sohne 16px text, 2px border-radius, 8px horizontal and 4-5px vertical padding. Used to label specimen collections (e.g. 'Die Grotesk', 'American Grotesk Collection'). Positioned bottom-left of the image it annotates.

### Typeface Specimen Band
**Role:** Full-width type showcase row in the font catalogue

Full-bleed horizontal band, one per typeface family. Alternates between Gallery Black (#000000), Charcoal Surface (#1c1c1c), Slate Mist (#3c585f), and Marble (#f9f9f9). Contains three zones: (1) family name set in the typeface itself at 36px+ in Bone (#ffffff on dark bands) or Graphite (#555555 on light bands), left-aligned with ~20px left padding; (2) variant list in Sohne 16px regular, center-aligned, listing sub-styles (e.g. 'Founders Grotesk', 'Founders Grotesk Condensed'); (3) 'Buy' links in Sohne 16px, right-aligned, in Fog (#7f7f7f) on dark or Graphite on light. No card chrome, no borders between zones - the three columns float in the band.

### Specimen Variant Row
**Role:** Individual sub-style entry within a typeface band

Single line of Sohne 16px text listing one variant name (e.g. 'Founders Grotesk Condensed'). Text color matches the band's text tier: Bone on dark, Graphite on light. 7px row-gap between variant entries. No bullet, no chevron - pure text.

### Buy Link
**Role:** Purchase action for a typeface variant

Sohne 16px, right-aligned in the specimen band. Text color: Fog (#7f7f7f) on dark bands, Graphite (#555555) on light. No background fill, no border, no padding - the word 'Buy' alone, set as text. Hover state brightens to Bone or Electric Blue.

### Image Specimen
**Role:** Full-bleed type-in-context or object photography

Edge-to-edge image with no border-radius (0px), no frame, no caption. Fills the full viewport width. May be paired with a Label Tag in the bottom-left corner. Images sit on the page canvas (Marble for light sections, Gallery Black for dark sections) with no gutter.

### Hamburger Menu Trigger
**Role:** Mobile and desktop menu toggle

Three short horizontal lines in Bone (#ffffff), 2px thick, right-aligned in the Top Bar. No background, no border. Touch target approximately 24x24px.

### Input Field
**Role:** Form input for search or filter

Charcoal Surface (#1c1c1c) background, Graphite (#555555) 1px border, 2px border-radius, 8px horizontal padding, Sohne 16px text in Bone. No visible focus ring color specified - likely defaults to Electric Blue or a 1px border darken.

### Text Link
**Role:** Inline hyperlink within body or navigation content

Sohne 16px, no underline by default. Color varies by context: Flare Orange (#d33c03) for primary nav links, Electric Blue (#24a7f2), Signal Red (#e90702), Mint Pulse (#93ffe6), or Canary (#ffff79) for inline links on dark backgrounds. Ash (#939393) 1px border may appear on interactive containers.

### Section Divider
**Role:** Horizontal rule between specimen bands

Implicit - specimen bands stack directly with no visible divider. The color change of the background itself creates separation. No border, no line, no whitespace gap greater than the band padding.

### Collection Annotation
**Role:** Editorial label overlaid on specimen imagery

Identical visual treatment to the Label Tag - Flare Orange (#d33c03) background, white Sohne text, 2px radius, small padding. Anchored to bottom-left of the image it describes. Functions as a caption that can be clicked to enter a collection.
