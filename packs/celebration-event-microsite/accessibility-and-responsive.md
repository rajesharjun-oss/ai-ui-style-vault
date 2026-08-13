# Accessibility and Responsive Standard

## Accessibility baseline

Celebration websites are emotional and media-rich, but core information and actions must remain accessible.

Required:

- Semantic landmarks and one clear page heading.
- Skip link.
- Keyboard-accessible navigation, gallery, video, RSVP and disclosure controls.
- Visible focus that works over light, dark and photographic surfaces.
- Persistent form labels.
- Fieldsets and legends for attendance, event and meal choices.
- Error summary and field-level errors.
- Meaningful image alternatives.
- Captions or transcripts for important video and audio.
- Accessible names for icon-only buttons.
- Sufficient contrast.
- Content visible without animation or Intersection Observer.
- `prefers-reduced-motion` support.
- High-zoom and text-resize resilience.

## Heading and reading order

The visual order must match the DOM order. Avoid compositions where desktop positioning makes a story appear chronological while screen readers receive a different sequence.

Use an ordered list for schedules and timelines. Dates should use machine-readable `datetime` values where practical.

## Typography

- Script faces are decorative and should be limited to short names, monograms or accents.
- Do not use script for biographies, event details, form labels or instructions.
- Body copy should remain at least comfortably readable at mobile sizes.
- Avoid very light serif text over busy photography.
- Control line length, especially on biography and story pages.
- Preserve names and diacritics without forced uppercase transformations that reduce readability.

## Colour and dress-code palettes

Colour swatches must include names. Do not communicate invitation status, event type or RSVP errors through colour alone.

Metallic, blush and pastel palettes must still meet contrast requirements for text and controls.

## Responsive design

Define intentional layouts for:

- Wide desktop.
- Laptop.
- Tablet when the navigation or timeline changes materially.
- Approximately 390×844 mobile.
- Small mobile around 320 px when supported.
- 200% and 400% zoom.

### Hero

- Protect faces, attire and culturally meaningful details.
- Set image focal points per breakpoint.
- Keep names, date, place summary and primary action within a usable first view.
- Do not place essential text permanently inside the image file.
- Provide a high-contrast fallback when the image fails.

### Navigation

Desktop may use a compact fixed or sticky navigation. Mobile should use a semantic menu button and an intentionally composed menu—not a desktop bar squeezed into one line.

The mobile menu must:

- Announce expanded state.
- Trap focus only when implemented as a modal navigation surface.
- Close with Escape.
- Restore focus.
- Avoid obscuring the viewport or trapping scroll.
- Reflect RSVP and post-event status accurately.

### Profiles and long stories

Desktop may use side-by-side media and copy. Mobile should stack profiles, show a concise summary and progressively disclose long biographies.

Timelines should become one chronological column on mobile. Do not alternate left and right in a way that creates excessive empty space or ambiguous reading order.

### Galleries

- Use responsive grids on large screens.
- Use a carefully tested swipe or snap model on mobile only when navigation and position remain understandable.
- Do not hide captions only on hover.
- Keep dialog controls inside the safe viewport.
- Prevent body scroll behind an open modal.

### Forms

- Use single-column fields on mobile.
- Keep the submit action visible after the final field.
- Avoid keyboard-obscured controls.
- Preserve responses after validation or network failure.
- Use native input types where appropriate without relying only on browser validation.

### Event details

Stack itinerary items and repeat critical directions actions when long content separates them. Written addresses and contact information should remain copyable.

## Motion and no-JavaScript fallback

All content that is revealed on scroll must start visible by default or become visible under a documented no-JavaScript class strategy. A failure to initialise animation must not leave headings, cards, forms or galleries invisible.

Reduced-motion mode must:

- Stop petals, confetti and looping particles.
- Disable parallax.
- Show timeline entries immediately.
- Avoid animated counting that is necessary to understand the date.
- Replace complex page transitions with instant or subtle opacity changes.
- Prevent background video autoplay.

## Dialogs

Gallery and video dialogs require:

- `dialog` or equivalent accessible dialog semantics.
- Label and optional description.
- Initial focus.
- Focus containment.
- Escape close.
- Focus restoration.
- Close button accessible at all zoom levels.
- No essential action hidden outside the viewport.

## Performance and low-connectivity behaviour

- Prioritise one hero image, not an entire gallery.
- Use transformed derivatives rather than full-resolution originals.
- Lazy-load non-critical media.
- Show text and event details before optional video.
- Provide offline read-only behaviour only when designed and truthful.
- Do not queue RSVP or financial actions invisibly while offline.

## Visual QA matrix

At minimum, capture and inspect:

1. Homepage before RSVP opens.
2. Homepage while RSVP is open.
3. Homepage on event day.
4. Homepage after event completion.
5. Meet-the-couple desktop and mobile.
6. Story timeline desktop and mobile.
7. Gallery and open viewer.
8. Video dialog.
9. RSVP default, validation error, submitting, confirmed and closed.
10. Guest-code required and invalid states.
11. Gift details hidden and revealed.
12. Mobile menu open.
13. Reduced-motion mode.
14. Long names, long venue names and translated copy.
15. 200% zoom and narrow mobile.

## Reject conditions

Reject the build when:

- Clickable media uses non-semantic `div` elements.
- Script fonts are used for body copy or forms.
- Scroll-reveal failure leaves content blank.
- Mobile biographies become an uninterrupted wall of text.
- Timeline order is unclear without its visual layout.
- Focus disappears over photography.
- A modal cannot be closed with keyboard.
- The countdown updates a live region every second.
- Colour is the only dress-code guidance.
- Sticky navigation covers headings or RSVP fields.
- Horizontal overflow appears at target widths.
