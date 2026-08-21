# Business Source Ingestion

Use this prompt when the user gives a Google Maps link, business website URL, social profile, directory listing, or another public source and asks the Vault to understand the business or build from it.

## Goal

Turn a minimal source reference into a strict, evidence-backed build input before any visual direction is chosen.

## Source-specific routing

Raw URL ingestion now selects one source playbook from `research/source-playbooks/index.json`:

- Google Maps / Google Business Profile → `research/source-playbooks/google-maps.md`
- Instagram → `research/source-playbooks/instagram.md`
- Facebook or public directory/review listing → `research/source-playbooks/facebook-directory.md`
- normal business website / unknown web host → `research/source-playbooks/business-website.md`

Read the shared ingestion prompt plus only the selected playbook. Do not preload all four playbooks into the agent context.

## Workflow

1. Run raw URL ingestion or identify the source type.
2. Read the selected source-specific playbook named in `business-source-request.json`.
3. Inspect the source using available browser/web/connectors. Do not claim a blocked source was inspected.
4. Extract exact factual strings for business identity, contact/location, website, ratings, hours, offers and other operational facts that are actually present.
5. Extract only assets that are permitted to be used and record provenance/ownership/use status.
6. When reviews are used, preserve author, rating, relative time and text verbatim. Do not clean grammar, normalize punctuation, remove emoji or collapse intentional blank lines.
7. Separate verified/source facts from inference. Business category, likely audience, brand tone and visual signals belong under `inference`, not under verified facts unless explicitly stated by the source.
8. Record research gaps, source conflicts and prohibited assumptions.
9. Create a JSON report conforming to `research/business-source-report.schema.json`.
10. Run:

```bash
python scripts/vault-agent.py ingest BUSINESS_SOURCE_REPORT.json --output-dir business-ingestion
```

11. Read `business-ingestion/ingestion-summary.json`. If ready, continue with the generated `business-profile.json` and Master Build Orchestrator. If owner confirmation is required, stop visual design until the blocking gap is resolved.

## Raw URL mode

The local CLI does not pretend to scrape the live web. Running:

```bash
python scripts/vault-agent.py ingest "https://example.com/business"
```

creates `business-source-request.json` with:

- detected `source.typeHint`;
- selected playbook id/path;
- required reads;
- shared hard rules;
- required evidence categories;
- blocked-source behavior.

The AI research layer should then inspect the source with its available tools, write the Business Source Report, and rerun ingestion.

## Multi-source research

A source playbook governs one inspected source. When the business needs multiple sources, keep each source/reference distinct in evidence. Do not merge conflicts silently. Prefer current owner-controlled evidence for current operational facts when appropriate, but record conflicts and confidence impact explicitly.

## Source-of-truth rules

- Do not replace an exact source value with a friendlier or derived version.
- Do not replace a business website with a Maps URL or vice versa.
- Do not round ratings or recompute review counts unless the source itself supplies the resulting value.
- Do not create placeholder people, reviews, timestamps, phone numbers, social profiles, addresses, products, hours or claims.
- Unsupported fields are omitted or empty.
- If the asset policy is `allowlist-only` or `verified-only`, no unlisted image may appear in the build.
- If an allowlisted image fails, do not silently substitute stock/generated media.
- Generated concept media is allowed only when the report explicitly chooses `verified-plus-generated-concept`, and it must not be presented as verified business photography.
- Do not force every business into a one-page site. Page/route architecture is decided later by the selected domain pack and build plan.

## Expected outputs

- `BUSINESS_SOURCE_REPORT.json`
- `CONTENT_SOURCE_OF_TRUTH.json`
- `ASSET_MANIFEST.json`
- `BUSINESS_RESEARCH.md`
- `business-profile.json`
- `BUILD_PROMPT.md`
- `ingestion-summary.json`

These artifacts exist to reduce agent improvisation. The source report is evidence; the business profile is planning input; the build prompt is a constraint layer; none of them substitutes for rendered QA.
