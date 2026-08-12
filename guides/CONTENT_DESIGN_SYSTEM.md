# Content Design System

## Goal

The interface should communicate with clarity and restraint. It must not feel like an AI essay distributed across a hero and twelve rounded cards.

Content design is part of the product architecture. It decides what users need, when they need it, how much they can process, and whether words are the best format.

## Content Density Modes

### Sparse

Best for luxury services, cinematic launches, portfolios, and highly visual products.

Characteristics:

- One dominant message per viewport.
- Short headings and minimal support copy.
- Strong visual or product demonstration.
- Detail lives on dedicated pages or progressive-disclosure surfaces.

Typical homepage target: 250–550 visible words excluding legal/footer text.

### Balanced

Default for SaaS, AI tools, professional products, and conversion-focused websites.

Characteristics:

- Concise hero.
- Clear evidence and product demonstration.
- Three to five major capabilities.
- Limited explanatory text.
- Detail separated into dedicated pages.

Typical homepage target: 450–900 visible words excluding legal/footer text.

### Informational

Best for professional services, regulated offerings, education, and products requiring trust or explanation.

Characteristics:

- Strong navigation and page segmentation.
- Detailed content distributed across dedicated pages.
- Summaries on landing pages.
- Scannable headings, lists, diagrams, and accordions.

Typical homepage target: 650–1,100 visible words. Detailed service pages may exceed this when information is genuinely required.

### Data-Dense

Best for dashboards, internal tools, operational systems, and analysis products.

Characteristics:

- Data, exceptions, status, and actions lead.
- Minimal promotional language.
- Short helper copy near complex controls.
- Contextual definitions and tooltips.
- Tables, charts, filters, and states carry meaning.

There is no single page word target; explanatory prose should remain low while labels and data may be dense.

## Default Copy Budgets

| Element | Recommended | Review at | Notes |
|---|---:|---:|---|
| Eyebrow | 2–5 words | 8 | Use only when it adds category or context. |
| Hero headline | 5–12 | 16 | State product outcome, not a slogan. |
| Hero support | 15–35 | 55 | One compact paragraph. |
| Primary CTA | 1–4 | 6 | Use a concrete verb and destination. |
| Secondary CTA | 1–5 | 7 | Distinguish it from the primary action. |
| Section heading | 3–10 | 14 | Make the point, not the topic label. |
| Section introduction | 25–60 | 90 | Often optional when cards or visuals are self-explanatory. |
| Feature title | 2–7 | 10 | Specific capability or outcome. |
| Feature description | 15–45 | 70 | Do not restate the title. |
| Card title | 2–8 | 12 | Avoid sentence-length labels. |
| Card body | 15–45 | 80 | Move depth elsewhere. |
| Testimonial | 20–70 | 110 | Keep only the evidential part. |
| Navigation item | 1–3 | 5 | Use familiar terms. |
| Tooltip | 5–25 | 40 | Explain the non-obvious. |
| Validation message | 4–18 | 30 | State problem and recovery. |
| Empty-state body | 10–35 | 55 | Explain cause and next action. |

Budgets are review triggers, not blind truncation rules.

## Message Hierarchy

Every page should answer these questions in order:

1. **What is this?**
2. **Why does it matter to me?**
3. **What should I do next?**
4. **Why should I trust it?**
5. **Where can I learn more?**

An application page may substitute:

1. What is the current state?
2. What requires attention?
3. What action is available?
4. What happens after the action?
5. How can I recover if something fails?

## Hero Standard

A strong hero usually contains:

- Optional eyebrow.
- One headline.
- One support paragraph.
- One primary action and, only when useful, one secondary action.
- One meaningful visual, product UI, or proof object.

Avoid:

- Multiple paragraphs.
- More than two calls to action.
- A feature list competing with the headline.
- A generic promise without a concrete outcome.
- Animated text that delays comprehension.

Example:

**Weak:**

> Revolutionize your business with our cutting-edge, seamless and powerful AI platform designed to unlock your full potential and take your workflow to the next level.

**Specific:**

> Review VAT and WHT exceptions before filing.
>
> Upload transaction schedules, resolve flagged entries, and export a documented review report.

## Progressive Disclosure Rules

Keep information visible when it is required for immediate understanding or safe action. Defer it when it is optional, advanced, repetitive, or rarely needed.

Use:

- Tabs for peer categories that users compare or switch between.
- Accordions for optional explanation, FAQs, and policy detail.
- Drawers for contextual detail that should not replace the main page.
- Modals for bounded decisions, not long reading.
- Tooltips for short definitions and non-obvious icons.
- Expandable rows for table-level detail.
- Dedicated pages for deep service, policy, documentation, or product information.
- Step flows for sequential tasks.

Do not hide information required to understand price, risk, consent, destructive action, or legal effect.

## Visual-First Translation

Before adding a paragraph, test whether the content is better expressed as:

| Information | Prefer |
|---|---|
| Multi-step process | Numbered workflow or animated product tour |
| Trend or change | Chart, sparkline, delta, or metric card |
| Comparison | Table or side-by-side states |
| Timeline | Timeline or milestone rail |
| Product capability | Live DOM product UI or concise demo |
| Status | Badge, progress, state banner, or timeline |
| Taxonomy | Tabs, segmented controls, filters, or navigation |
| Cause and resolution | Error state with recovery action |
| Evidence | Metric, named customer proof, audit trail, or case result |

A visual must carry information. Decorative artwork does not replace necessary explanation.

## Repetition Control

Create a message inventory before final copy. Each major benefit should have one primary home.

Acceptable repetition:

- A concise reminder in the final CTA.
- The same task label in navigation and page title.
- A safety warning repeated at the point of irreversible action.

Unacceptable repetition:

- Hero, features, “why us,” and CTA saying the same outcome.
- Every feature description repeating “save time and improve efficiency.”
- Multiple sections explaining that the product uses AI.
- Repeated company introductions.

## Generic AI Language

Avoid phrases that could describe almost any product:

- Revolutionize your workflow.
- Unlock your potential.
- Transform your business.
- Take it to the next level.
- Seamless and powerful.
- Robust and scalable.
- Cutting-edge solution.
- All-in-one platform.
- Built for the future.
- Empower your team.
- Supercharge productivity.
- Effortlessly streamline.
- Reimagine the way you work.

Replace generic claims with:

- A specific action.
- A measurable outcome.
- A named workflow.
- A concrete differentiator.
- Verifiable evidence.

## Interface Writing Standards

### Buttons

Use verb + object or verb + destination when needed:

- Upload schedule.
- Review exceptions.
- Export report.
- Invite reviewer.
- Save changes.
- Try again.

Avoid:

- Click here.
- Continue, when the destination is unclear.
- Submit, when a more specific action exists.
- Learn more repeated across the page.

### Headings

Headings should communicate the point:

- “Resolve exceptions before filing” is stronger than “Our features.”
- “Payments awaiting classification” is stronger than “Overview.”

### Form help

Use help text only when it prevents error or explains consequence. Do not restate the field label.

### Validation

A useful error message contains:

- What happened.
- Why, when known.
- How to recover.

Example:

> The schedule could not be read. Upload an `.xlsx` file with the transaction headers in the first row.

### Empty states

Differentiate:

- First-use empty.
- Filtered empty.
- Permission-restricted empty.
- Error empty.
- Completed state.

Each should offer the appropriate next action.

## Content by Product Type

### Marketing website

- Lead with outcome and proof.
- Keep the homepage as a summary, not the entire company brochure.
- Give detailed services, documentation, and policies dedicated pages.

### Professional-services website

- Establish expertise and trust.
- Use short service summaries on the homepage.
- Put scope, process, deliverables, and technical depth on service pages.
- Avoid corporate-history paragraphs before explaining the service.

### Business web application

- Use task and status language.
- Place help at the point of complexity.
- Avoid promotional copy inside operational workflows.

### Dashboard

- Prioritize exceptions, trend, status, and action.
- Do not explain obvious metrics in paragraphs.
- Use concise interpretation only where data could be misunderstood.

### AI workspace

- Explain capability, input expectations, limitations, and state.
- Keep surrounding chrome quiet so the primary interaction dominates.

### Mobile application

- Reduce copy further.
- Use progressive disclosure.
- Keep the primary action reachable and visible.
- Test long names and localized text.

## Content Stress Tests

Review each important screen with:

- Real production copy.
- Maximum realistic copy.
- Long person and company names.
- Large currency and percentage values.
- Detailed validation messages.
- Empty and failure states.
- Mobile width.
- 200% browser zoom.

A component that only works with short placeholder text is not complete.

## Content Handoff Evidence

Record:

- Chosen density mode.
- Hero and page copy budgets.
- Major messages removed or merged.
- Content converted to visual or progressive-disclosure patterns.
- Generic claims replaced.
- Long-content and mobile stress-test results.
