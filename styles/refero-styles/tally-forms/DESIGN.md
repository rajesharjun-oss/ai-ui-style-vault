# Tally Forms Style Reference

## North Star

Tally Forms feels like a clean digital notebook with cheerful margin doodles. The interface is practical and form-builder focused, but small hand-drawn shapes and bright accent bursts make it feel approachable.

The system should feel simple enough for a non-designer to trust, while still giving enough structure for forms, templates, submissions, analytics, and editor flows.

## Color

The palette is mostly neutral paper and graphite, with blue reserved for actual interaction and brighter colors reserved for playful illustration.

- `Graphite Ink` `#37352f`: primary text, headings, strong labels, editor text.
- `Paper` `#ffffff`: main cards, form fields, editor surfaces, page content.
- `Warm Paper` `#f7f6f3`: alternate page canvas, muted sections, form-builder background.
- `Line Gray` `#e9e9e7`: borders, dividers, input outlines.
- `Mist Gray` `#ebebec`: hover fills and inactive subtle surfaces.
- `Soft Gray` `#787774`: secondary text, metadata, placeholders.
- `Action Blue` `#0b6bcb`: primary buttons, links, selected states, focus accents.
- `Blue Tint` `#eaf3ff`: selected row or soft action background.
- `Sun Yellow` `#ffeaa7`: doodle fills, cheerful highlights, background shapes.
- `Warm Orange` `#f5a623`: decorative highlight and expressive accent.
- `Electric Magenta` `#f81ce5`: hero expression, radial accents, doodles, not UI controls.
- `Lime Pop` `#c3ff43`: expressive doodle accent.
- `Soft Purple` `#8b5cf6`: gradient/doodle accent only.

Keep Action Blue as the only serious interface color. Do not use magenta, lime, or orange for normal buttons, destructive states, or form validation.

## Typography

Use Inter for the entire interface. The type should feel Notion-like: plain, readable, and compact.

Recommended roles:

- Micro: 12px, weight 500, line-height 1.33.
- UI: 14px, weight 500, line-height 1.43.
- Body: 16px, weight 400, line-height 1.6.
- Body large: 18px, weight 400, line-height 1.47.
- Card title: 20px to 24px, weight 600, line-height 1.25 to 1.33.
- Section heading: 32px to 42px, weight 700, tight negative tracking.
- Hero: 60px to 64px, weight 700, line-height about 1.05, letter-spacing around -0.04em.

Avoid decorative typefaces. The personality comes from doodles, not fonts.

## Layout

The layout should be spacious but not luxurious:

- Centered max width around 1200px.
- Hero with large headline, short copy, blue CTA, and playful doodle cluster.
- Product/editor preview card showing form-building blocks.
- Template grids and feature cards using soft shadows.
- Section gaps around 64px to 96px.
- Form/editor surfaces with clear hierarchy and minimal chrome.

The style can support both a marketing homepage and an app editor. For app views, keep sidebars and panels compact, using the same paper surfaces and blue selected states.

## Shape And Elevation

The source uses modest radii:

- Buttons: 7px.
- Inputs: 7px.
- Tags: 7px.
- Cards: 10px.
- Doodle blobs: 9999px or organic custom shapes.

Elevation should be soft and low-stakes. Use light borders and a small shadow on cards:

```css
0 1px 1px rgba(0, 0, 0, 0.12),
0 3px 9px rgba(61, 59, 53, 0.10)
```

Do not create heavy floating SaaS panels.

## Components

### Primary Blue Button

Action Blue background, white text, 7px radius, Inter 16px/500, compact padding. Use for start, create form, publish, sign up, and continue actions.

### Secondary Button

Paper or transparent background, Line Gray border, Graphite Ink text, 7px radius. Hover uses Mist Gray.

### Form Builder Card

Paper surface, 10px radius, Line Gray border, soft shadow, block rows, small icons, and editor-like text.

### Form Input

Paper background, 1px Line Gray border, 7px radius, 16px text, Soft Gray placeholder, blue focus ring.

### Template Card

Paper surface, 10px radius, subtle shadow, form preview, category tag, and short description. Keep cards clean and scannable.

### Tag Or Status Badge

7px radius, small text, Paper or Warm Paper fill, Line Gray border. Use Action Blue only for selected state.

### Doodle Cluster

Use Sun Yellow, Electric Magenta, Lime Pop, Soft Purple, and hand-drawn black linework. Keep it near hero, empty states, or celebratory moments.

### Response Graph Card

Paper card with small chart, soft grid lines, blue selected bar or line, and compact labels.

### Editor Sidebar

Warm Paper or Paper background, thin divider, compact block list, selected state in Blue Tint or Action Blue marker.

### Mobile Menu

Paper surface, 10px to 12px radius, simple text links, blue CTA, no heavy overlay effects.

## Imagery

Use product screenshots, form builder UI, response charts, templates, simple doodles, and lightweight hand-drawn marks. Avoid glossy 3D, stock office photos, dark hero scenes, and complex illustrations that fight the editor UI.

## Do

- Use Inter everywhere.
- Use 7px radius for controls.
- Use 10px radius for cards.
- Use Action Blue for real actions and links.
- Keep magenta/yellow/lime decorative.
- Use light borders and subtle shadows.
- Make product/editor UI the main proof.

## Do Not

- Do not use decorative typefaces.
- Do not turn doodle colors into core UI colors.
- Do not use heavy shadows or glassmorphism.
- Do not make controls fully pill-shaped.
- Do not add extra saturated accent systems.
- Do not build a dense enterprise dashboard from this style.
