# Photography and Video Standard

## Principle

Personal media is often the primary design material in a couple or celebration website. Treat it as private, identity-bearing content rather than interchangeable decoration.

## Accepted sources

Use only:

- Media supplied by the couple or authorised hosts.
- Media supplied by an authorised photographer or videographer with permission for web use.
- Clearly licensed venue, travel or decorative media.
- Original decorative illustrations, patterns, florals or textures.
- Generated decorative media that does not impersonate a real person, venue or event.

Do not:

- Copy photographs from another couple's website or social profile.
- Present generated people as the couple, relatives, guests or vendors.
- Infer personal facts from photographs.
- Publish private images without consent.
- Reuse one portrait across unrelated sections simply to fill space.

## Asset plan

For every major media item, document:

- Owner or creator.
- Consent and usage status.
- Source file.
- Subject and purpose.
- Public, guest-only or host-only access.
- Focal point.
- Desktop and mobile crop.
- Aspect ratio.
- Caption and alternative text.
- Colour treatment.
- Delivery format.
- Download permission.
- Retention or archival plan.

## Art direction

Choose one coherent photographic language based on the actual event:

- Formal portraits.
- Traditional attire.
- Candid relationship memories.
- Venue and ceremonial details.
- Family or community photographs.
- Editorial pre-wedding imagery.

A gallery may contain different periods and cameras, but the page treatment should still be coherent through crop, spacing, captioning and background choices.

## Hero media

The hero image must:

- Show the intended people or event context clearly.
- Preserve faces and culturally meaningful attire at all breakpoints.
- Support readable text without destructive overlays.
- Have a defined mobile focal point.
- Use responsive sources and explicit dimensions.
- Be compressed and prioritised as the likely Largest Contentful Paint asset.

Do not preload every gallery image. Preload only the true critical hero asset when evidence supports it.

## Portraits

- Do not crop heads, hands, jewellery or attire details unintentionally.
- Avoid aggressive face retouching or identity alteration.
- Preserve skin tone and garment colour accurately.
- Use distinct alt text when the portrait communicates identity or attire.
- Use an empty alt attribute only when the image is genuinely redundant beside equivalent visible text.

## Gallery media

- Lazy-load non-critical images.
- Provide width and height to prevent layout shift.
- Use AVIF or WebP with an appropriate fallback when supported.
- Keep original uploads private and serve transformed derivatives.
- Avoid exposing predictable private-media URLs.
- Provide captions where context matters.
- Respect photographer watermark and download restrictions.

## Video

Every video experience must define:

- Poster image.
- Duration or expectation when useful.
- Controls.
- Captions, subtitles or transcript path.
- Audio behaviour.
- Mobile delivery.
- Fallback when unavailable.
- Privacy and hosting status.

Autoplay with sound is prohibited. Background video must be muted, optional, nonessential and disabled for reduced-motion or constrained-data contexts.

## Accessible viewer

Photo lightboxes and video modals must use:

- Semantic button triggers.
- Labelled dialog semantics.
- Focus trapping.
- Escape-to-close.
- Focus restoration.
- Reachable close controls.
- Keyboard previous/next actions.
- Captions outside low-contrast image overlays.
- A non-dialog fallback link when appropriate.

Clickable `div` elements are not acceptable.

## Generated decorative assets

Generated assets may include:

- Floral line work.
- Textile-inspired abstract patterns.
- Confetti or petal shapes.
- Paper or material textures.
- Nonliteral venue atmosphere.

They must be recorded as `decorative-generated-asset`. They must not falsely claim to show the real couple, ceremony, venue, attire, gifts or guests.

## Privacy

Before publication, confirm:

- Who appears in each image.
- Whether children are present.
- Whether guests consented to public display.
- Whether the site is indexed.
- Whether media requires guest-code access.
- Whether downloads are permitted.
- When media will be removed or archived.

Guest-upload galleries require moderation, malware checks, file limits, consent, deletion handling and publication approval.

## Quality reject conditions

Reject or replace media when:

- It is low resolution at the intended rendered size.
- Faces or attire are distorted by crop.
- The colour treatment changes identity or ceremony colours inaccurately.
- It is copied or licensing is unclear.
- It reveals private information unintentionally.
- It is generated but presented as documentary evidence.
- The video lacks controls or a text alternative.
- Gallery content becomes invisible when scroll-reveal JavaScript fails.
