# Celebration Asset Plan — Example Structure

Copy this file to the target project as `ASSET_PLAN.md`. Replace every example entry.

## Asset policy

- Couple/host media source:
- Photographer/videographer permission:
- Public versus guest-only collections:
- Generated decorative-media policy:
- Guest-media consent policy:
- Download policy:
- Original-file storage:
- Responsive-derivative provider:
- Retention and deletion plan:

## Asset register

| ID | Page/use | Subject | Source/creator | Provenance | Consent | Access | Crop/focal point | Formats | Alt/caption | Retention |
|---|---|---|---|---|---|---|---|---|---|---|
| hero-couple | Homepage hero | Couple portrait | Couple-provided | couple-provided | confirmed | public | Keep both faces and attire visible; mobile focal point centred | AVIF/WebP/JPEG | Approved description | Review after archive date |
| portrait-one | Profile | Person one | Photographer | photographer-licensed | confirmed | public | 4:5 portrait | AVIF/WebP/JPEG | Approved description | Site lifetime |
| proposal-video | Story/video dialog | Proposal video | Couple-provided | couple-provided | confirmed | guest-only | 16:9 poster | MP4/WebM + captions | Caption and transcript | Remove on request |
| floral-line | Decorative divider | Abstract flowers | Original/generated | decorative-generated-asset | not applicable | public | Scalable | SVG | Decorative, empty alt | Site lifetime |

## Hero checklist

- [ ] Correct people and event.
- [ ] Identity and skin tone preserved.
- [ ] Attire colours accurate.
- [ ] Desktop crop approved.
- [ ] Mobile crop approved.
- [ ] Text contrast tested.
- [ ] Explicit dimensions supplied.
- [ ] Responsive sources generated.
- [ ] Critical hero only is preloaded.
- [ ] Failure fallback exists.

## Gallery checklist

- [ ] Media order approved.
- [ ] Public/private access assigned.
- [ ] Captions or alternatives supplied.
- [ ] Children and guests reviewed for consent.
- [ ] Lazy loading configured.
- [ ] Viewer keyboard and focus behaviour tested.
- [ ] Download policy enforced.
- [ ] Original upload URLs are not exposed unintentionally.

## Video checklist

- [ ] Poster image.
- [ ] Controls.
- [ ] Captions/subtitles.
- [ ] Transcript or summary.
- [ ] No autoplay with sound.
- [ ] Reduced-motion/data fallback.
- [ ] Focus-managed dialog.
- [ ] Hosting and access confirmed.
- [ ] Unavailable state.

## Decorative generated assets

| ID | Prompt/purpose | Generator | Status | What it must not imply |
|---|---|---|---|---|
| | | | decorative-generated-asset | Must not impersonate the couple, venue or event |

## Launch review

- [ ] Every asset has provenance.
- [ ] Every person-bearing asset has consent status.
- [ ] No copied target-site media.
- [ ] No generated people presented as real.
- [ ] No private asset is available through a public predictable URL.
- [ ] No sensitive metadata is included unnecessarily.
- [ ] Performance derivatives are complete.
- [ ] Post-event and deletion behaviour is documented.
