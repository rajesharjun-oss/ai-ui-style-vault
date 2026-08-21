# Business Entity & CMS Modeling

Use this guide after `BUSINESS_SOURCE_REPORT.json` has been created and ingested.

## Why this stage exists

A business source contains evidence, but a website and an admin panel need structured entities. The generator converts evidence into entities without inventing the operational system behind them.

The core rule is:

> **Evidence creates records. Missing evidence creates no placeholder records.**

A visually complete admin dashboard is not more important than factual integrity.

## Command

```bash
python scripts/vault-agent.py model business-ingestion
```

or directly:

```bash
python scripts/generate-business-content-model.py business-ingestion --json
```

## Outputs

- `BUSINESS_ENTITY_MODEL.json` — canonical entity registry and provenance/editability classification.
- `PUBLIC_CONTENT_MODEL.json` — which evidence-backed content families and sections are eligible for public display.
- `ADMIN_CMS_MODEL.json` — which CMS modules are justified, which are disabled, and which synthetic operational modules are forbidden.
- `CMS_BUILD_CONTRACT.md` — implementation rules for the admin/CMS.
- `content-model-summary.json` — compact routing summary.

## Default entity semantics

### Business identity / contact facts

Public when relevant. Admin may edit with provenance. A real implementation should retain the original source value and change history rather than silently replacing evidence.

### Hours

Only exist when evidenced or explicitly supplied by the owner. Admin may update with provenance. Do not compute or invent an `open now` state unless runtime business logic and timezone requirements are explicitly part of the product.

### Offers / highlights

Only exist when supported. They are not permission to invent a complete catalog, menu or service list.

### Media

Approved source/user assets may become gallery records. Reorder and visibility controls are reasonable. Replacement must respect `ASSET_MANIFEST.json`; generated concept media cannot silently replace verified business photography.

### Reviews

Verbatim content is immutable source evidence. Admin capability is moderation-only by default: view, feature or hide from the public site. Do not rewrite review text, author, rating or relative time.

### Inference

Audience, category, tone and visual signals may guide planning/design but are not editable verified business facts.

## Forbidden synthetic admin modules

Do not create these merely because they make an admin interface look sophisticated:

- orders;
- revenue/sales analytics;
- stock/inventory/availability;
- bookings/reservations;
- customers/CRM records;
- user activity;
- security-event logs;
- system health/uptime percentages;
- made-up timestamps or recent activity;
- sample staff/admin users.

Any of these can become legitimate modules later, but only after the owner defines the workflow, fields, permissions, integrations and actual data source.

## Public website rule

`PUBLIC_CONTENT_MODEL.json` determines content eligibility, not final page architecture. The selected product-domain pack still decides how supported content should be composed.

For example, a restaurant with ten photographs and five reviews may justify gallery and review sections. That does not automatically justify a menu, checkout or order-tracking flow.

## Admin design rule

The admin should mirror entity semantics rather than copy the marketing site. Use appropriate dense product UI, tables/lists/forms where justified, and implement loading/empty/error/success/permission states. Disabled modules stay absent rather than appearing as fake populated dashboard cards.

## Handoff checks

Before calling an admin/CMS build complete, verify:

- every visible record traces to evidence or owner-supplied data;
- every editable field has a defined provenance/update policy;
- verbatim records are not editable as normal copy;
- no unsupported module was populated with sample data;
- public and admin views resolve to the same canonical source-of-truth entities;
- role/permission behavior is defined for any actual write-capable admin implementation.
