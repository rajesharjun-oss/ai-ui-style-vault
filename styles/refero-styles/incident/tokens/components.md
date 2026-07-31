# Components

### Navigation Bar
**Role:** Top-level site navigation

White (#ffffff) background, sits on the concrete canvas. Uses Times for nav labels at 16px weight 400. The brand mark in Signal Orange (#f25533) anchors the left. Hairline black (#000000) bottom border separates it from page content. Carbon (#161618) used for stroked logo elements.

### Neutral Button
**Role:** Primary interactive action

Concrete (#efefef) background - the same as the page canvas, making the button feel like a raised card rather than a filled action. Black (#000000) 1px border, 4px radius, padding 1px top/bottom and 6px left/right (deliberately compact). Label in Arial 13px weight 400, Ink (#000000). No color fill, no shadow - the button is a labeled rectangle with a hairline frame.

### Critical Alert Banner
**Role:** Outage or incident status display

Soft red/pink wash background (tinted toward Alert Red #ff492c at low opacity), left-aligned warning triangle icon in Alert Red. Headline in Times 16px weight 700, body text in Times 16px weight 400. Full-width card with 8px radius and a saturated red border on the container card below.

### Warning Alert Banner
**Role:** Degraded service or maintenance notice

Amber/yellow icon (Ember #f1641e) with warning triangle. Headline in Times 16px weight 700, descriptive body in Times 16px weight 400. Sits inside a white card with a light amber-tinted border.

### Status Tag / Pill
**Role:** Component-level status indicator (e.g. Website, App)

Small rounded-corner tag, 4px radius. Tinted background matching the status color: soft red wash for outages, soft amber wash for degraded. Label in Arial or Times at 13px, color matching the status hue. Inline, sits adjacent to other tags.

### Status Card
**Role:** Container for a single incident report

White (#ffffff) background on the concrete canvas. 12px radius. Border is chromatic and status-dependent: red-pink for active incidents, amber for warnings, subtle gray for resolved. Internal padding 24px. Contains icon, headline, body, and metadata line in muted gray.

### Section Heading (Serif)
**Role:** Page and section titles

Times weight 400 or 700, 24-32px scale. Color is Ink (#000000) for primary, Carbon (#161618) for secondary. No underline, no decoration - the serif face does the hierarchy work. Often paired with a 16px body paragraph below in the same family at 16px.

### Text Link
**Role:** Inline navigation to subpages or external resources

Underlined text in a saturated blue (appears as ~#0000ff in rendered links), Arial or Times depending on context. No arrow, no icon - the underline is the affordance. Sits within serif body text blocks.

### File-Type Illustration
**Role:** Decorative graphic for file format references

Document-shape icon with a folded corner, filled in Signal Orange (#f25533), with white label text (e.g. 'PNG') in Arial bold. No shadow, no border - flat brand-colored fill on the concrete canvas.

### Product Feature Card
**Role:** Text-first card describing a product capability

No visible card container - text sits directly on the concrete canvas. Serif headline (Times 24-32px), sans-serif body description (Arial 13px or Times 16px), underlined text link. Accompanied optionally by a line-art illustration in blue or orange. Maximum text density without card chrome.
