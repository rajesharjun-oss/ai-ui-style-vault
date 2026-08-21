# Business Source Ingestion

Use this prompt when the user gives a Google Maps link, business website URL, social profile, directory listing, or another public source and asks the Vault to understand the business or build from it.

## Goal

Turn a minimal source reference into a strict, evidence-backed build input before any visual direction is chosen.

## Workflow

1. Identify the source type.
2. Inspect the source using available browser/web/connectors. Do not claim a blocked source was inspected.
3. Extract exact factual strings for business identity, contact/location, website, ratings, hours, offers and other operational facts that are actually present.
4. Extract only assets that are permitted to be used and record provenance.
5. When reviews are used, preserve author, rating, relative time and text verbatim. Do not clean grammar, normalize punctuation, remove emoji or collapse intentional blank lines.
6. Separate verified/source facts from inference. Business category, likely audience, brand tone and visual signals belong under `inference`, not under verified facts unless explicitly stated by the source.
7. Record research gaps and prohibited assumptions.
8. Create a JSON report conforming to `research/business-source-report.schema.json`.
9. Run:

```bash
python scripts/vault-agent.py ingest BUSINESS_SOURCE_REPORT.json --output-dir business-ingestion
```

10. Read `business-ingestion/ingestion-summary.json`. If ready, continue with the generated `business-profile.json` and Master Build Orchestrator. If owner confirmation is required, stop visual design until the blocking gap is resolved.

## Raw URL mode

The local CLI does not pretend to scrape the live web. Running:

```bash
python scripts/vault-agent.py ingest "https://example.com/business"
```

creates `business-source-request.json` describing the evidence the AI research layer must gather. The agent should then inspect the source with its available tools, write the Business Source Report, and rerun ingestion.

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
