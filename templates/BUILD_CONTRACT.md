# Build Contract

> Complete this document before implementation. Replace instructional text with project-specific decisions. Do not leave placeholders at handoff.

## 1. Product Frame

- Product name:
- Build type:
- Domain:
- Primary users:
- Secondary users:
- Top user tasks:
- Primary outcome:
- Trust level: low / medium / high / critical
- Risk level: low / medium / high / regulated
- Highest-cost user error:
- Success signals:

## 2. Target Repository

- Repository/path:
- Framework:
- Package manager:
- Routing:
- Styling approach:
- Existing component system:
- Existing design tokens:
- Existing test/accessibility tools:
- Commands:
  - Install:
  - Dev:
  - Lint:
  - Typecheck:
  - Test:
  - Build:

## 3. Primary Journey

Write the main journey as a short sequence.

`Entry → Context → Primary task → Review/confirmation → Success/recovery`

Primary journey:

## 4. Page and State Inventory

| Page/state | Purpose | Audience | Primary action | Required information | Deferred information | Required states |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Every page must have one purpose and one primary action.

## 5. Information Architecture

- Navigation model:
- Top-level navigation items:
- Contextual navigation:
- What belongs on the homepage/dashboard:
- What moves to dedicated pages:
- What uses progressive disclosure:
- Mobile navigation behavior:

## 6. Component Inventory

Use IDs from `system/component-manifest.json` where possible.

| Component/pattern | Pages | Variants | Required states | Responsive behavior | Accessibility notes |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 7. System State Matrix

Mark relevant states and define behavior.

| State | Required? | Where | User message | Recovery/action |
|---|---:|---|---|---|
| Loading |  |  |  |  |
| Empty — first use |  |  |  |  |
| Empty — filtered |  |  |  |  |
| Error |  |  |  |  |
| Validation error |  |  |  |  |
| Success |  |  |  |  |
| Disabled/read-only |  |  |  |  |
| Permission denied |  |  |  |  |
| Offline/retrying |  |  |  |  |
| Conflict/stale data |  |  |  |  |
| Destructive confirmation |  |  |  |  |
| Long-running progress |  |  |  |  |

## 8. Responsive Contract

### Desktop — 1440×1000+

- Navigation:
- Content columns:
- Tables/data:
- Sticky elements:

### Laptop — 1280×800

- What compacts:
- What wraps:
- What remains visible:

### Mobile — approximately 390×844

- Navigation transformation:
- Content order:
- Table/list transformation:
- Panel/dialog transformation:
- Sticky action behavior:
- Media/motion simplification:

### Stress tests

- Long headings:
- Long company/person names:
- Large values:
- Detailed errors:
- 200% zoom:

## 9. Accessibility Contract

- Target standard:
- Keyboard workflow:
- Focus management:
- Labels/descriptions/errors:
- Contrast and non-color status:
- Screen-reader announcements:
- Zoom/text resize:
- Reduced motion:
- Touch targets:

## 10. Engineering Decisions

- Semantic token mapping:
- Reusable primitives/components:
- Data-fetching/state approach:
- Form/validation approach:
- Table strategy:
- Motion tool and reason:
- Performance risks and mitigation:
- Security/authorization notes:

## 11. Scope Control

### Must ship

- 

### May ship

- 

### Explicitly out of scope

- 

### Content or features removed to preserve clarity

- 

## 12. Quality Evidence

- [ ] `VAULT_SELECTION.md` completed.
- [ ] `CONTENT_PLAN.md` completed.
- [ ] `design-recipe.json` completed and valid.
- [ ] Lint passes.
- [ ] Typecheck passes.
- [ ] Tests pass.
- [ ] Build passes.
- [ ] Content/design validator passes or approved exceptions are recorded.
- [ ] Desktop, laptop, and mobile views reviewed.
- [ ] Keyboard and focus reviewed.
- [ ] Loading, empty, error, success, disabled, and permission states reviewed where relevant.
- [ ] Long-content stress test completed.
- [ ] Reduced-motion behavior reviewed.
- [ ] Asset and license audit completed.

## 13. Handoff Notes

- Completed scope:
- Important design decisions:
- Important content reductions:
- Known risks:
- Manual checks remaining:
