# Celebration Pack Code References

These files are framework-neutral references:

- `event-types.ts` defines event, host, guest, RSVP, media, privacy and integration contracts.
- `event-lifecycle.ts` validates verified event instants and resolves pre-event, same-day, in-progress, completed, gallery and archived states.

## Important boundaries

- Use ISO date-times with explicit offsets.
- Record an IANA timezone such as `Africa/Lagos` for display and same-day logic.
- Use a trusted server clock for protected content, RSVP opening/closing, guest access, gifting disclosure and post-event publication.
- Do not download the complete guest list to the browser.
- Do not display `rsvp-confirmed` until the source of truth accepts the response.
- Do not rely on hidden CSS or client-only checks for privacy.
- Replace sample copy and data with verified event information.

The code is not a complete RSVP backend, authentication system, payment flow or media service. Adapt it to the target stack and document the real provider and recovery behaviour in `EVENT_BUILD_CONTRACT.md`.
