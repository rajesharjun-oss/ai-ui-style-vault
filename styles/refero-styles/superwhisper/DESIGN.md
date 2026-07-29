# Superwhisper Style Reference

## North Star

Superwhisper feels like a midnight dictation cockpit with aurora glass. It should feel fast, private, technical, and voice-first. The interface is dark and focused, with enough color to make recording, transcription, and AI actions feel alive.

The signature is a near-black canvas, frosted charcoal surfaces, pill-shaped controls, a violet-to-teal gradient action language, waveform visualizations, and compact metadata.

## Color

The palette is dark neutral with aurora accents:

- `Obsidian` `#030712`: deepest canvas and page background.
- `Deep Space` `#0a0f1c`: radial gradient base and large section backgrounds.
- `Charcoal Glass` `#111827`: cards, panels, command surfaces, and input backgrounds.
- `Slate Border` `#1f2937`: borders, dividers, dark outlines.
- `Iron` `#374151`: muted fills, inactive controls, subtle separators.
- `Cool Gray` `#9ca3af`: secondary text and metadata.
- `Mist` `#e5e7eb`: primary body text on dark.
- `White` `#ffffff`: highest contrast text, CTA labels, selected icons.
- `Electric Violet` `#8b5cf6`: primary brand energy and gradient start.
- `Neon Teal` `#22d3ee`: gradient end, active voice status, waveform peaks.
- `Aurora Cyan` `#06b6d4`: supporting voice accent and active highlights.
- `Indigo Glow` `#6366f1`: secondary gradient stop and focus detail.
- `Pink Pulse` `#ec4899`: tiny recording or expressive accent.
- `Success Mint` `#34d399`: success state, completed transcription, online state.
- `Amber Signal` `#fbbf24`: warning or attention state.

Use violet and teal as the core accent pair. Pink, mint, and amber are status-level accents only.

## Typography

Use Inter for all normal UI and content. Use JetBrains Mono for technical metadata, model names, latency, token counts, timestamps, shortcut labels, and command-line-like details.

Recommended roles:

- Mono label: 11px to 12px, JetBrains Mono, 500, line-height 1.33.
- UI: 14px, Inter, 500, line-height 1.43.
- Body: 16px, Inter, 400, line-height 1.6.
- Transcript: 17px, Inter, 400, line-height 1.65.
- Card title: 20px, Inter, 600, line-height 1.3.
- Section heading: 36px, Inter, 700, line-height 1.1, letter-spacing -0.03em.
- Hero: 64px, Inter, 700, line-height 0.98, letter-spacing -0.05em.

Keep text compact and legible. The product should feel like a tool, not a cinematic poster.

## Layout

The layout should be dark, centered, and product-led:

- Full-page dark gradient canvas.
- Sticky or simple top navigation with pill CTA.
- Centered hero with large headline, short copy, and a voice recorder/prompt panel.
- Product demo area with waveform, transcript, and command chips.
- Feature cards in a dark glass grid.
- Pricing or workflow sections using segmented controls and compact cards.

Use max width around 1200px. Use section gaps around 80px to 112px. App panels can be denser with 12px to 20px gaps.

## Shape And Elevation

Superwhisper is pill-first for active controls:

- Main CTA: 9999px.
- Voice recorder pill: 9999px.
- Command chips: 9999px.
- Cards: 20px.
- App panels: 24px.
- Inputs: 14px.
- Transcript cards: 16px.

Elevation comes from glass, borders, and glow:

```css
0 24px 80px rgba(0, 0, 0, 0.35),
0 0 0 1px rgba(255, 255, 255, 0.06)
```

Aurora glow:

```css
0 0 40px rgba(139, 92, 246, 0.28),
0 0 64px rgba(34, 211, 238, 0.18)
```

Use glow sparingly around the active voice or primary CTA area.

## Components

### Primary Gradient CTA

Use a gradient from Electric Violet through Indigo Glow to Neon Teal, white text, 9999px radius, Inter 14px to 16px 600, and soft aurora glow. Use for start, download, record, or try actions.

### Secondary Dark Pill

Charcoal Glass fill, Slate Border outline, Mist text, 9999px radius. Use for secondary actions and navigation CTAs.

### Voice Recorder Pill

Large pill panel with dark glass surface, record button, waveform or pulse dots, command label, status text, and a gradient active state.

### Transcript Panel

Charcoal Glass card with 16px radius, transcript copy at 17px, highlighted recognized words, mono timestamps, and action chips.

### Command Chip

9999px radius, Charcoal fill, Slate Border outline, Cool Gray text, optional icon. Active command uses violet/teal border or fill.

### Model Badge

JetBrains Mono, 11px to 12px, dark fill, subtle border, cool metadata style. Use for model names, latency, device mode, and privacy status.

### Feature Card

Charcoal Glass background, 20px radius, subtle border, small gradient icon, title, body, and optional code/command preview.

### Waveform Visualization

Use vertical bars, dots, or smooth lines in Neon Teal, Aurora Cyan, and Electric Violet. Keep it decorative but tied to voice state.

### Pricing Toggle

Pill segmented control with Charcoal background, active segment in white or gradient, compact labels.

### Nav Header

Dark transparent or Obsidian surface, subtle border, small text links, and one primary gradient pill CTA.

## Imagery

Use product-real voice UI: recorder controls, waveforms, transcript panels, command chips, model badges, automation flows, and keyboard-shortcut surfaces. Avoid stock microphones, generic AI heads, neon blobs, or unrelated cosmic art.

## Do

- Use Obsidian and Deep Space as the dominant backgrounds.
- Use one violet-to-teal gradient action path.
- Use glassy charcoal cards with subtle borders.
- Use Inter for normal UI and JetBrains Mono for metadata.
- Use waveform and transcript visuals as product proof.
- Keep controls pill-shaped where the interaction is voice or command driven.
- Use status colors sparingly.

## Do Not

- Do not use bright white full-page backgrounds.
- Do not use many unrelated neon accents.
- Do not make every card glow.
- Do not use decorative AI stock imagery.
- Do not use heavy colored gradients as full section backgrounds.
- Do not make the interface feel like a music app unless the voice product requires it.
