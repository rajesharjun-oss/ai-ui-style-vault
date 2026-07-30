# Column

Source: [Refero Style](https://styles.refero.design/style/a76ec6ba-20b3-495c-9d89-1e58281e79e7)
Reference site: [https://column.com](https://column.com)
Captured: 2026-07-30
Refero published: 2026-03-22T20:28:02.000Z
Refero modified: 2026-07-03T10:10:39.337Z
Theme: light
Category: Fintech

## Style Summary

Explore Column's light Fintech design system: Indigo Navy #111a4a, Midnight Ink #011821 colors, SuisseIntl, SuisseIntlMono typography, and DESIGN.md for AI...

North star: deep navy ledger under cool dawn

## What To Borrow

- Indigo Navy `#111a4a` for Primary brand color - filled CTAs, navigation active states, heading text, logo wordmark. The deep violet-tinted navy carries institutional weight without going pure black; pairs with white text for the site's most confident button
- Midnight Ink `#011821` for Dark surface and emphasis text - product card backgrounds, high-contrast body copy. Near-gray with a cool blue-green undertone; works as the dark-mode substrate when a section needs to invert
- Slate Ink `#3b3e47` for Secondary heading and body text - slightly warmer than Midnight Ink, used where pure black feels too harsh against the light canvas
- Steel `#7c7f88` for Body and link text - the dominant muted text color (245 occurrences in body). Neutral gray-blue that reads as quiet, never washed out
- Fog `#a9acb6` for Icon strokes, tertiary borders, placeholder text. Mid-gray that separates without competing with text
- Mist `#cbcccf` for Lightest body text - captions, disclaimers, fine print. Stays legible on white but recedes visually
- Silver Lining `#e3e4e8` for Card borders, input borders, divider lines. The structural hairline color - appears wherever two surfaces need to separate without shadow
- Cloud Canvas `#f6f6f8` for Page background - the dominant canvas color. Near-white with a barely-perceptible cool tint that keeps the page from feeling sterile
- Pure White `#ffffff` for Card surfaces, nav background, button fills, secondary text. The top layer of the surface stack
- Charcoal `#232730` for Nav icons, dark icon strokes - slightly bluer than pure black, used in icon contexts where Slate Ink would be too warm
- Obsidian `#12161e` for Deep icon strokes and nav elements. Near-black with a blue undertone that matches the indigo navy family
- Pure Black `#000000` for Maximum contrast text, dark fills in illustrations. Used sparingly - Indigo Navy or Slate Ink carry most text work
- Signal Orange `#ec652b` for Accent CTA fill and featured card background - one of the few saturated warm colors in the system. Appears on the Brex highlight card and select buttons to draw the eye without feeling decorative
- Peach Glow `#f2936b` for Soft accent surface - lighter companion to Signal Orange, used as card backgrounds where warmth is needed at lower intensity
- Seafoam 600 `#44b48b` for Code and data text - the signature color for JSON keys, identifiers, and financial values in code snippets. Also used for chart data points and growth visualizations
- Seafoam 700 `#167e6c` for Darker seafoam for strokes, chart lines, and icon accents in data contexts. Anchors the seafoam scale on darker backgrounds
- Seafoam 400 `#94efb7` for Highlighted code text - string values, URLs, API endpoints in code blocks. The lightest seafoam, reads as green-tinted monospace
- Deep Sea `#023247` for Decorative stroke and chart accent - deep teal used in SVG illustrations and data visualizations alongside the seafoam scale
- Sky Cyan `#88deeb` for Soft accent surface and stroke - appears as background washes behind data widgets and as decorative chart strokes
- Cobalt Edge `#1e4199` for Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Ocean Depth `#0c6997` for Decorative fill - medium blue used in illustration and SVG contexts

- SuisseIntl `--font-suisseintl` for Primary typeface - used for all headings, body, buttons, nav, links, and card text. The custom geometric grotesque gives Column a distinctive editorial register that distinguishes it from Inter-only fintechs. Weight 600 at 52-60px for display, weight 500 for sub-headings, weight 400 for body, weight 300 for low-emphasis links.
- SuisseIntlMono `--font-suisseintlmono` for Monospace companion to SuisseIntl - used for technical labels, API identifiers, and inline data in UI chrome. Maintains the same proportions as SuisseIntl so mono and proportional text align cleanly in mixed contexts.
- SFMono `--font-sfmono` for Code snippet rendering - appears in JSON examples and API documentation blocks. Tinted in seafoam green scale to visually distinguish code from UI prose.
- Inter `--font-inter` for UI fallback font - used in dashboard and product surface contexts where Inter's wider character set and system familiarity take priority over brand identity.

## Avoid

- Don't use the 9999px pill radius on buttons - buttons stay at 8px to maintain the sharp, confident banking feel.
- Don't place seafoam green (#44b48b) on body copy outside code or data contexts - the color signals technical content, not prose.
- Don't stack more than two card shadow styles on the same page - the product card shadow and the transaction widget shadow are both dramatic; using both simultaneously creates visual noise.
- Don't use the linear rainbow gradient on UI elements - it's a one-time decorative asset for the halftone map illustration only.
- Don't set body text below 14px in SuisseIntl - drop to SuisseIntlMono or SFMono at 10-12px for micro-copy and technical labels.
- Don't apply the Cobalt Edge (#1e4199) or Ocean Depth (#0c6997) colors to text or buttons - they are decorative SVG colors only.
- Don't use pure black (#000000) for body text - use Slate Ink (#3b3e47) or Obsidian (#12161e) for a softer, more refined dark.

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
