# Information Architecture and Page Composition

## Purpose

Professional UI begins with deciding what belongs where. A page packed with words is often an information-architecture failure before it is a typography problem.

## One Page, One Job

Every page or major state must have:

- One purpose.
- One primary audience.
- One primary action.
- A defined completion or next state.

Secondary actions may exist, but they must not visually compete with the primary action unless the user genuinely faces an equal choice.

## Page Inventory Template

For each page, record:

| Field | Question |
|---|---|
| Purpose | What user outcome does this page enable? |
| Audience | Who uses it? |
| Entry | How do users arrive? |
| Primary action | What is the main next step? |
| Required information | What must be known before action? |
| Deferred information | What can be hidden or moved elsewhere? |
| Success state | What confirms completion? |
| Failure state | What can fail and how is recovery offered? |
| Empty state | What does no data mean? |
| Permission state | What happens when access is missing? |

## Public Website Architecture

A typical product or service website may include:

- Home.
- Product or services.
- Individual product/service detail.
- Use cases or industries.
- Pricing or engagement model.
- Evidence: case studies, results, testimonials, credentials.
- About.
- Resources or insights.
- Contact or consultation.
- Legal and privacy.

Do not place the complete contents of every page on the homepage.

### Homepage responsibility

The homepage should:

- Establish the offer.
- Identify the audience.
- Demonstrate the main outcome.
- Provide evidence.
- Route users to the correct next page or action.

It should not become a full product manual, complete service catalogue, company history, and FAQ in one continuous scroll.

## Web Application Architecture

A task-oriented application commonly needs:

- Authentication and onboarding.
- App shell and navigation.
- Home/status overview.
- Core workflow list.
- Create/upload/import flow.
- Detail/review workspace.
- Exceptions and resolution.
- Reports or export.
- Notifications/activity.
- Settings and access management.
- Help and recovery.

Group navigation by user goals, not database tables or development modules.

## First Viewport Standard

For a public website, the first viewport should normally reveal:

- What the product/service is.
- Who it is for.
- The main outcome.
- A clear next action.
- A product visual or credibility signal when useful.
- Enough of the next section to suggest continuation when appropriate.

For an application, the first viewport should reveal:

- Current context and page title.
- Important status or exception.
- Primary task/action.
- Core working area.

Do not use the entire first viewport for a decorative headline while hiding the product.

## Section Purpose Test

A section may be added only when it answers a distinct question:

- What is it?
- How does it work?
- What can I do?
- Is it relevant to me?
- Why should I trust it?
- What will it cost?
- What happens next?
- What evidence exists?

If two sections answer the same question, combine them.

## Recommended Homepage Shape

A balanced premium product homepage often needs only:

1. Hero and product proof.
2. Credibility signal.
3. Product demonstration or workflow.
4. Three to five major capabilities.
5. Use cases or outcomes.
6. Evidence or case result.
7. Final action.
8. Footer.

This is a starting shape, not a template requirement. Remove sections that do not support the product.

## Composition Patterns

### Product-first hero

Use when the interface itself is the strongest proof. Place concise copy beside or above a real DOM product demonstration.

### Evidence-first hero

Use for high-trust services and products. Lead with a specific result, credential, or known pain point, then the action.

### Split task hero

Use when two legitimate audiences or workflows exist. Keep choices clear and limited.

### Scroll product story

Use for complex products that benefit from staged explanation. Keep native scroll, one sticky scene at a time, and a static reduced-motion layout.

### Dashboard command centre

Use when users need status, exceptions, and actions. Prioritize current risk and work over decorative summaries.

### Review workspace

Use for tax, audit, approvals, or QA. Combine list/table context with a focused detail panel, evidence, comments, and resolution actions.

## Avoid Card Soup

Use cards for independent objects, comparisons, or interactive modules. Avoid creating a card for every sentence.

Signals of card soup:

- More than three consecutive sections use the same card grid.
- Cards contain long paragraphs with no distinct action or state.
- Everything has the same radius, border, shadow, and padding.
- Page hierarchy depends only on card background changes.
- Nested cards create visual noise.

Alternatives:

- Open layout with typography and spacing.
- Split sections.
- Lists with dividers.
- Table or timeline.
- Full-width product demonstration.
- Tabs or segmented views.
- Editorial image/text composition.

## Dashboard Hierarchy

Prioritize in this order when relevant:

1. Critical exceptions and blocked work.
2. Primary next action.
3. Current status and progress.
4. Trend and comparative metrics.
5. Recent activity.
6. Supporting context.

Do not begin with six equal metric cards if only one number requires attention.

## Forms and Workflows

- Break long forms by meaningful decision stages, not arbitrary page count.
- Keep labels visible.
- Explain consequences near the action.
- Preserve entered data on recoverable errors.
- Confirm destructive actions in proportion to risk.
- Show progress for long-running uploads or analysis.
- Provide a review step when errors are expensive.

## Responsive Composition

Responsive design is not shrinking desktop.

Define for each page:

- What moves first.
- What stacks.
- What becomes a drawer or sheet.
- What table columns remain visible.
- What becomes a detail view.
- What sticky actions remain accessible.
- What media is removed or simplified.
- What copy is shortened or disclosed progressively.

## Navigation Standards

- Use familiar labels.
- Keep top-level choices limited.
- Do not mirror every internal database category.
- Highlight location and current task.
- Ensure mobile navigation opens, closes, restores focus, and does not trap scroll.
- Use mega menus only when taxonomy genuinely requires them.

## Page Blueprint Use

Read `system/page-blueprints.json` and choose the closest page type. Adapt it to the actual product rather than copying all listed blocks.

The blueprint provides:

- Page purpose.
- Required blocks.
- Optional blocks.
- Default content budget.
- State requirements.
- Common anti-patterns.
