# Privacy and Guest Access Standard

## Principle

A celebration website may contain identity, guest, contact, attendance, travel, financial and private-media information. The privacy model must be chosen before implementation and enforced on the server—not simulated only in the interface.

## Supported privacy models

### Public

Use only when all published content is intentionally public. Do not include guest lookup, private photographs, personal contact numbers, exact accommodation details or sensitive gifting information without explicit approval.

### Public summary, private details

The public site may show names, an approved hero, date summary and general story. Venue specifics, RSVP, private galleries, travel details and gifting require a guest code or authenticated access.

### Guest code

A guest enters a unique or household-level invitation code. Codes must be sufficiently random, rate limited, revocable and authorised server-side.

### Authenticated guest

Use when guests need persistent RSVP editing, travel information, uploads or private media. Authentication and session handling must have a documented provider and recovery path.

### Fully private

All event content requires authorised access. Search indexing, social previews, caches and public media URLs must be disabled or restricted appropriately.

## Guest lookup

Guest lookup must:

- Resist name and email enumeration.
- Return minimal information before verification.
- Use rate limiting and abuse monitoring.
- Normalise input carefully without creating broad matches.
- Enforce approved guest and plus-one limits server-side.
- Avoid logging sensitive lookup values in analytics.
- Provide a neutral not-found message.

Do not download the whole guest list to the browser to implement search.

## RSVP data

Collect only what the hosts actually need. Common fields may include:

- Attendance.
- Approved guest count.
- Event selection.
- Meal or dietary information.
- Travel or accommodation status.
- A message to the couple.

Document:

- Source of truth.
- Lawful or consent basis where relevant.
- Who can access responses.
- Confirmation method.
- Edit and deletion policy.
- Retention period.
- Export and backup policy.
- Breach or support contact.

Do not claim that a prototype form stores or confirms responses.

## Invitation codes and links

- Prefer random, non-guessable identifiers.
- Never encode names, phone numbers or event roles directly into public URLs.
- Expire or revoke compromised codes.
- Do not expose the access code in analytics, referrer data or error reporting.
- Use HTTPS.
- Apply server-side authorisation to every protected resource.

## Search engines and social previews

For private sites:

- Use access control; `robots.txt` and `noindex` are not security boundaries.
- Avoid private names, venue details and financial data in titles, descriptions, Open Graph tags and JSON-LD.
- Review cached previews before launch.
- Avoid public image URLs for private hero media when privacy is required.

## Gifting and financial details

Bank, mobile-money or delivery details must be:

- Confirmed by the authorised hosts.
- Optional in the guest journey.
- Hidden until deliberate disclosure or verified guest access when appropriate.
- Excluded from public metadata, structured data and analytics.
- Paired with an official verification contact.
- Removable quickly if compromised.

Do not process card payments directly unless a compliant payment provider and server integration are explicitly in scope. Do not present a design prototype as a working payment route.

## Contact actions

Email, telephone and WhatsApp information requires host approval. Identify the contact role—such as RSVP coordinator or travel contact—rather than exposing unrelated personal details.

Opening an external messaging app should be explicit. Do not prefill sensitive guest information into a third-party URL without consent.

## Media privacy

- Separate public and guest-only media collections.
- Do not rely on obscurity of image URLs.
- Restrict original uploads.
- Remove embedded metadata when appropriate.
- Moderate guest uploads before publication.
- Provide a removal contact.
- Define post-event retention and archival.

## Children and vulnerable people

Photographs or data concerning children require heightened consent and access controls. Avoid publishing full names, schools, routines, travel details or other identifying information.

## Analytics

Use privacy-conscious analytics. Do not send:

- Guest names.
- Invitation codes.
- Attendance choices.
- Dietary information.
- Bank or gifting details.
- Private media identifiers.
- Personal messages.

Analytics must not block RSVP or core content.

## Security states

The interface must support:

- Guest code required.
- Invalid or expired code.
- Rate limited.
- Session expired.
- Permission denied.
- RSVP conflict.
- Confirmation delivery failed.
- Protected media unavailable.
- Gifting details withdrawn.

Each state should explain what the guest can do without revealing protected information.

## Post-event retention

Before launch, hosts must decide:

- When RSVP editing closes.
- When guest data is deleted or archived.
- When financial details are removed.
- Whether private media remains available.
- Whether guest uploads close.
- Whether the site becomes a gallery, read-only archive or is retired.

## Reject conditions

Reject the implementation when:

- Privacy exists only as a hidden CSS section.
- Guest records are searchable client-side.
- Access codes are guessable or exposed in logs.
- Financial details are indexed publicly without deliberate approval.
- A third-party service receives sensitive data without disclosure.
- The final handoff does not distinguish real integrations from prototypes.
