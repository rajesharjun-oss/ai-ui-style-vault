# Celebration Motion Guidance

## Motion model

Use motion to support anticipation, ceremony, memory and continuity. It should not delay guest tasks or turn every page into an animation demo.

Choose one primary motion attitude:

- `quiet-celebration` — soft reveals, image fades, subtle monogram drawing.
- `ceremonial-reveal` — measured entrances inspired by processional rhythm or stationery.
- `microinteraction-led-celebration` — playful but controlled feedback for informal events.
- `quiet-premium` — almost static, with precise state transitions and gallery movement.

Use no more than five recurring motion primitives unless a justified cinematic sequence is part of the brief.

## Appropriate patterns

### Hero entrance

- Names and event details enter once.
- Keep timing short enough that the primary action is available immediately.
- Do not animate every word separately by default.

### Monogram drawing

- Treat as decorative.
- Provide a static monogram immediately in reduced-motion mode.
- Do not block navigation while it completes.

### Petals, florals and confetti

- Use low density.
- Disable pointer events.
- Keep particles away from important text and controls.
- Pause when the page is hidden.
- Stop for reduced motion, low power or constrained data when detectable.
- Avoid particles in form-heavy RSVP screens.

### Scroll reveals

- Reveal grouped sections, not every sentence.
- Content must be visible if JavaScript fails.
- Avoid long stagger chains on mobile.
- Do not use scroll position as the only way to understand a timeline.

### Timeline progression

- Animate the progress line or milestone emphasis only after the content is already readable.
- Respect chronological DOM order.
- Avoid parallax that separates a date from its story.

### Gallery transitions

- Use short crossfades, shared-position transitions or direct changes.
- Do not autoplay through personal photographs without a user-selected slideshow mode.
- Preserve captions and focus.

### Video dialog

- Use a small opacity/scale transition.
- Video does not autoplay with sound.
- Closing stops playback and restores focus.

### Countdown

- Update visual units without announcing every second.
- Use days and hours when the event is distant; avoid urgency theatre.
- The event-state transition is more important than number animation.

### Page transitions

- Keep transitions short and reversible.
- Do not hide page content while waiting for decorative animation.
- Preserve browser history, scroll restoration and deep links.

## Timing guidance

| Interaction | Typical duration |
|---|---:|
| Button feedback | 100–180 ms |
| Menu or disclosure | 160–260 ms |
| Dialog open/close | 180–300 ms |
| Image crossfade | 250–450 ms |
| Section reveal | 300–600 ms |
| Ceremonial hero sequence | 600–1200 ms total |

Durations are guidelines. Test on mobile and slower devices.

## Performance

Prefer transform and opacity. Avoid continuously animating layout properties. Limit simultaneous blurred layers, large shadows, canvases and DOM particles.

Use CSS for simple states, Motion for React or an equivalent component animation tool for coordinated UI, and GSAP only for justified storytelling choreography. Do not combine several motion libraries casually.

## Reduced motion

Under `prefers-reduced-motion: reduce`:

- Stop petals, confetti, floating flourishes and parallax.
- Display all scroll-reveal content immediately.
- Disable background video autoplay.
- Replace animated counters with static text.
- Keep dialogs and menus functional with instant or minimal transitions.
- Retain status, focus and confirmation feedback.

Example:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }

  [data-decorative-motion] {
    display: none !important;
  }

  [data-reveal] {
    opacity: 1 !important;
    transform: none !important;
  }
}
```

## QA

Test:

- First load with and without JavaScript.
- Reduced motion.
- Keyboard navigation while elements are transitioning.
- Background-tab pause behaviour.
- Mobile menu and dialog focus.
- Low-end mobile performance.
- Content visibility during screenshot, print and browser zoom.
- Event lifecycle changes without replaying disruptive hero animation.

## Reject conditions

Reject motion when:

- Guests wait to reach RSVP or directions.
- Text is unreadable until animation completes.
- Decorative particles reduce contrast or intercept clicks.
- Scroll reveal leaves blank sections in unusual rendering contexts.
- Motion continues indefinitely on forms or practical details pages.
- Reduced-motion mode removes feedback or hides content.
- Several unrelated animation styles make the site feel assembled from demos.
