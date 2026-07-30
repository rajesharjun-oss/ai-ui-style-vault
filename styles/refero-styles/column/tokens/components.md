# Components

### Primary Filled Button
**Role:** Main call-to-action - highest-emphasis interactive element.

Background: #111a4a (Indigo Navy). Text: #ffffff, 14px SuisseIntl weight 500, letter-spacing normal. Border: none. Radius: 8px. Padding: 12px top/bottom, 20px left/right. Arrow icon after label. Box-shadow: rgba(17,26,74,0.1) 0px 1px 3px, rgba(17,26,74,0.05) 0px 1px 0px, with inset white highlight for slight inner luminosity. Used for 'Sign up' and top-of-page conversion actions.

### Secondary Outlined Button
**Role:** Secondary action - less weight than primary but still a distinct CTA.

Background: transparent. Text: #111a4a, 14px SuisseIntl weight 500. Border: 1px solid #111a4a. Radius: 8px. Padding: 12px top/bottom, 32px left/right. No arrow by default. Used for 'Documentation' and 'Learn about our bank' - sits beside the primary without competing.

### Ghost Navigation Pill
**Role:** Top-bar navigation trigger - 'Products', 'Developers', 'Blog'.

Background: rgba(255,255,255,0.25) with backdrop blur. Text: #000000, 14px SuisseIntl weight 400. Border: 1px solid #ffffff. Radius: 8px. Padding: 6px top/bottom, 12px left/right. Chevron icon for dropdowns. Frosted-glass effect sits over the hero background.

### Pill Button
**Role:** Compact action - tag-like buttons used for filtering and quick navigation.

Background: rgba(255,255,255,0.5). Text: #232730, 12-14px SuisseIntl weight 400. Border: 1px solid #e3e4e8. Radius: 8px (not fully rounded). Padding: 0px vertical, 16px horizontal for compact alignment.

### Accent Orange Button
**Role:** High-attention CTA - used when a section needs a warm, urgent accent.

Background: #ec652b (Signal Orange). Text: #ffffff, 14px SuisseIntl weight 500. Border: none. Radius: 8px. Padding: 12px top/bottom, 20px left/right. Appears on the Brex highlight card and select promotional surfaces - never on the primary nav.

### Product Card (Elevated)
**Role:** Feature showcase card - used for product mockups and feature highlights.

Background: rgba(2,50,71,0.01) (near-transparent with the faintest blue-green tint). Radius: 8px. Box-shadow: five-layer progressive shadow stack - rgba(0,0,0,0.02) at 40px/32px, 0.03 at 22px/18px, 0.03 at 12px/10px, 0.04 at 7px/5px, 0.07 at 3px/2px. Padding: 0 (content is positioned absolutely inside). No border. The shadow stack creates a diffused, hovering presence rather than a hard card edge.

### Transaction Widget Card
**Role:** Compact data card - shows account balances, transfer details, payment status.

Background: #ffffff. Radius: 8px. Box-shadow: rgba(30,30,44,0.15) 24px 48px 64px - a dramatic, off-axis shadow that makes the widget feel like it's floating above the hero. Inset border: 1px solid #ffffff. Padding: 12px top/bottom, 0 left/right. Contains flag icons, amount text (SuisseIntl weight 500, 16-18px), and status badges.

### Bordered Content Card
**Role:** Standard card for grouped content - quotes, code examples, feature blocks.

Background: #ffffff. Radius: 8px. Box-shadow: rgba(18,22,30,0.024) 0px 1px 4px, rgba(18,22,30,0.05) 0px 1px 0px, rgba(18,22,30,0.024) 0px 0px 0px 1px - combines a hairline border with a whisper of shadow. Padding: 12px all sides.

### Code Block
**Role:** JSON/API example - shows developer-facing content with syntax-tinted text.

Background: #ffffff. Radius: 8px. Monospace: SFMono 12px, line-height 1.5. Keys tinted #167e6c (Seafoam 700), string values #94efb7 (Seafoam 400), structural brackets in #232730. The entire block reads as a data object rather than formatted prose.

### FDIC Badge
**Role:** Trust indicator - regulatory badge for bank membership.

Background: rgba(255,255,255,0.8) with backdrop blur(8px). Text: #000000, 10-12px SuisseIntl weight 400. Radius: 9999px (full pill). Padding: 4px 12px. Semi-transparent so it floats over the hero gradient without blocking it.

### Tag with Dot
**Role:** Status or category label - 'TRUSTED AT SCALE II', 'DEVELOPER FIRST'.

Background: rgba(0,0,0,0) (transparent, sits over light backgrounds). Text: #000000 or #111a4a, 12px SuisseIntl weight 500, uppercase, letter-spacing slightly expanded. Small green or blue dot prefix for category color. Radius: 0 (no rounding - reads as a label, not a chip).

### Logo Bar Card
**Role:** Partner/customer logo showcase - used in trust strip and case studies.

Background: #ffffff or transparent. Individual logos rendered as flat monochrome SVG at 16-20px height, #000000 or #7c7f88. Spacing: 48px between logos. No card chrome - logos sit directly on the canvas with whitespace as separator.

### Account Balance Card
**Role:** Featured account display - the Brex operating account mockup.

Background: #ec652b (Signal Orange) for the primary featured card, or #ffffff for secondary. Radius: 8px. Contains SwissIntl amount text at 24px weight 500, small chart line in white at 60% opacity, and account metadata in 12px weight 400. The orange variant is the system's most saturated surface - used at most once per page.

### Stats Row
**Role:** Trust metrics - '$4.5T+', '99.999%', 'No. 1', '$100B+'.

Four-column grid with no dividers. Each stat: number in #167e6c (Seafoam 700) at 28px SuisseIntl weight 500, label in #7c7f88 at 14px weight 400 below. 48px row gap. The seafoam number color ties the stats to the data/code visual language.
