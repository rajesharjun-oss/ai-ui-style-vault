# Event Build Contract

Complete this contract before UI implementation. Replace every bracketed instruction and delete sections that do not apply.

## 1. Event identity

- Public title:
- Couple or host names and preferred order:
- Event type:
- Primary audience:
- Primary guest action:
- Locale and language:
- IANA timezone:
- Public launch date:
- Event start instant:
- Final event end instant:
- Post-event mode:
- Archive or retirement date:

## 2. Source and verification matrix

| Information | Value | Source | Status | Public/private | Owner |
|---|---|---|---|---|---|
| Names | | | verified / confirm | | |
| Event dates | | | | | |
| Times and timezone | | | | | |
| Venues and addresses | | | | | |
| Guest rules | | | | | |
| Dress code | | | | | |
| Couple biographies | | | | | |
| Relationship story | | | | | |
| Travel and accommodation | | | | | |
| Gift options | | | | | |
| Contacts | | | | | |

No value marked `confirm` may be presented as final public information.

## 3. Privacy model

Select one:

- [ ] Public
- [ ] Public summary, private details
- [ ] Guest code
- [ ] Authenticated guest
- [ ] Fully private

Define:

- Search indexing:
- Social preview content:
- Protected pages:
- Guest lookup method:
- Invitation-code policy:
- Rate limiting:
- Session provider:
- Public/private media split:
- Children or vulnerable-person media policy:
- Guest-data retention:
- Media retention:
- Financial-detail retention:
- Site archival plan:

## 4. Page set

| Page | Purpose | Primary action | Privacy | Lifecycle availability |
|---|---|---|---|---|
| Homepage | | | | |
| Meet the couple/hosts | | | | |
| Story | | | | |
| Event details | | | | |
| Dress code | | | | |
| Gallery | | | | |
| RSVP | | | | |
| Gifting | | | | |
| Travel | | | | |
| FAQ | | | | |
| Post-event | | | | |

Remove unused pages. Do not add pages merely to make the site larger.

## 5. Event lifecycle

Define the verified transition rules:

| State | Starts | Ends | Homepage message | Primary action |
|---|---|---|---|---|
| Save the date | | | | |
| Invitation announced | | | | |
| RSVP not open | | | | |
| RSVP open | | | | |
| RSVP deadline passed | | | | |
| Event upcoming | | | | |
| Event today | | | | |
| Event in progress | | | | |
| Event completed | | | | |
| Post-event gallery | | | | |
| Archived | | | | |

The implementation must use verified instants and the event timezone. It must not rely only on the visitor's local calendar date.

## 6. RSVP capability

Classify RSVP:

- [ ] verified-and-integrated
- [ ] design-only-prototype
- [ ] requires-integration
- [ ] out-of-scope

- Source of truth:
- Guest identifier:
- Approved guest limit source:
- Events selectable per invitation:
- Fields collected:
- Confirmation channels:
- Edit policy:
- Closed-state contact:
- Error and conflict recovery:
- Data export/backup:
- Data deletion date:

A prototype must never display a false server confirmation.

## 7. Integrations

| Capability | Provider/source | Classification | Server/client boundary | Failure state |
|---|---|---|---|---|
| Guest lookup | | | | |
| RSVP storage | | | | |
| Email | | | | |
| SMS/WhatsApp | | | | |
| Maps/directions | | | | |
| Calendar/ICS | | | | |
| Media hosting | | | | |
| Video | | | | |
| Guest uploads | | | | |
| Gift registry | | | | |
| Protected transfer | | | | |
| Analytics | | | | |

Allowed classifications:

```text
verified-and-integrated
design-only-prototype
requires-integration
requires-host-confirmation
out-of-scope
```

## 8. Content strategy

- Homepage content-density mode:
- Hero headline budget:
- Hero support budget:
- Biography summary budget:
- Timeline summary budget:
- FAQ approach:
- Languages:
- Faith/cultural terminology reviewer:
- Long-content disclosure plan:
- Content that must not be indexed:

## 9. Visual direction

- Selected production theme:
- Primary vault style bundle:
- Supporting screen references:
- Event palette source:
- Typography plan:
- Pattern/material source:
- Motion attitude:
- Allowed motion primitives:
- Reduced-motion fallback:
- What will be adapted:
- What will not be copied:

## 10. Asset and consent summary

- Hero media:
- Couple portraits:
- Story media:
- Gallery media:
- Video:
- Venue/travel media:
- Decorative generated media:
- Photographer/videographer permission:
- Guest media consent:
- Download policy:
- Crop/focal-point plan:
- Performance formats:

Detailed entries belong in `ASSET_PLAN.md`.

## 11. Accessibility and responsive contract

- Desktop target:
- Laptop target:
- Tablet target when relevant:
- Mobile target:
- Small-mobile/zoom strategy:
- Mobile navigation:
- Timeline transformation:
- Biography disclosure:
- Gallery viewer semantics:
- Video caption/transcript path:
- Form error handling:
- Focus management:
- No-animation fallback:
- Reduced-motion behaviour:

## 12. Required state demonstrations

Before handoff, render and inspect:

- [ ] Homepage upcoming
- [ ] RSVP open
- [ ] Event today
- [ ] Event in progress
- [ ] Event completed
- [ ] Post-event mode
- [ ] Mobile menu
- [ ] Couple profile mobile
- [ ] Timeline mobile
- [ ] Gallery and lightbox
- [ ] Video dialog
- [ ] RSVP validation error
- [ ] RSVP submitting
- [ ] RSVP confirmed
- [ ] RSVP closed
- [ ] Guest code invalid
- [ ] Gift details hidden/revealed
- [ ] Reduced motion
- [ ] No-animation fallback
- [ ] High zoom and long content

## 13. Launch and handoff

- Build command:
- Test commands:
- Validation commands:
- Deployment target:
- Environment variables:
- Host admin process:
- Guest-data access process:
- Content update process:
- Emergency removal contact:
- Known limitations:
- Owner-confirmation items:
