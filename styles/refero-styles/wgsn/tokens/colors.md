# Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Paper White | `#ffffff` | `--color-paper-white` | Primary canvas, card surfaces, button text, and the base against which every other neutral is measured. Carries ~21:1 contrast with deep charcoal for all body and display text |
| Bone Warm | `#f6f2eb` | `--color-bone-warm` | Secondary surface wash - the system's only warm neutral. Used as a soft section background to break white-on-white monotony and evoke paper-stock texture. Contrasts 14.4:1 with charcoal text |
| Ash Mist | `#f5f5f5` | `--color-ash-mist` | Input field backgrounds, inset card wells, and disabled surface states. The cool-gray complement to Bone Warm - use the warm tone for sections, the cool tone for form wells |
| Graphite Border | `#666666` | `--color-graphite-border` | Default hairline border color (444 border usages - by far the most-used neutral in the system). Also used for muted helper text and icon outlines. The structural divider color of the entire UI |
| Smoke Border | `#999999` | `--color-smoke-border` | Secondary hairline borders and placeholder text - used when #666666 would feel too heavy against a light surface |
| Pearl Border | `#cccccc` | `--color-pearl-border` | Subtle dividers and very light borders in nav-adjacent contexts where separation should be nearly invisible |
| Silver Border | `#bdbdbd` | `--color-silver-border` | Light link borders, particularly for outlined navigation links that need separation without emphasis |
| Slate Text | `#333333` | `--color-slate-text` | Secondary body copy, link borders, and UI text that should recede from primary content. Pairs with Paper White for ~12.6:1 contrast |
| Carbon Input | `#495057` | `--color-carbon-input` | Input field text color - a cool desaturated charcoal that feels typographic rather than aggressive, distinct from the warmer #333333 used elsewhere |
| Obsidian | `#212121` | `--color-obsidian` | Primary action fill, primary nav background, and the deepest neutral in the system. Used for the filled CTA button, sticky header band, and dark surface blocks. Contrasts 16.1:1 with white - strong enough for any text role |
| Pure Black | `#000000` | `--color-pure-black` | Maximum-emphasis text, heading borders, and accent strokes. Reserved for the most important typographic moments and thin rule lines - never used as a large fill surface (use Obsidian instead) |
