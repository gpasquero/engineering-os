---
id: EXTERNAL-AIDESK-AUTH-CHARTER
title: Validation charter — ai-desk authentication
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0087, ADR-0098, ADR-0102]
---

# Validation charter — ai-desk authentication

**A real repository, not a synthetic example.** `/Users/willy/Localsources/ai-desk`
— a multi-tenant SaaS helpdesk, 314 TypeScript and 155 TSX files, 5 ADRs, 134
test files.

## The objective is different from the Kubernetes validation

`ADR-0087` asked whether Engineering OS **generalizes**. This asks something
narrower and more useful:

> **Measure where deterministic reasoning stops and workers begin, on real
> engineering work.**

The workflow is the one named in the direction: **"I need to add OAuth."**

## Scope

The authentication subsystem, and only enough of it to run one workflow:

- login, token issuance, refresh rotation, logout;
- the account-lockout and JWT-security behaviours the tests protect;
- the multi-tenancy constraint that governs all of it.

**Excluded**: tickets, channels, SLA, real-time, custom fields, the widget, and
every other module.

## Sources, all read before authoring

| Class | Source |
|---|---|
| Design decisions | `docs/adr/ADR-0001-multi-tenancy-strategy.md` |
| Implementation | `packages/backend/src/modules/auth/auth.service.ts` |
| | `packages/backend/src/common/guards/jwt-auth.guard.ts` |
| | `packages/backend/src/common/database/schema/refresh-tokens.ts` |
| Tests | `__tests__/account-lockout.spec.ts` (8 cases) |
| | `__tests__/refresh-token-rotation.spec.ts` (7 cases) |
| | `__tests__/jwt-security.spec.ts` (12 cases) |
| | `__tests__/auth.service.spec.ts` (12) · `password-security.spec.ts` (11) |

**Every symbol, test name and quotation was extracted from the working tree**, by
`grep`, on 2026-08-02. Nothing is recalled.

## Test granularity

The Kubernetes model recorded *one node per test file* and `FINDINGS.md` named
that its sharpest limitation.

**This model records one node per test suite, with its case count**, and the
invariants each suite asserts are modelled individually from the test names. That
is the second-iteration change `FINDINGS.md` ranked first, applied.

## Success criteria

**Not** *can it model the subsystem*. That question is answered.

| Criterion | Measured by |
|---|---|
| The Director runs on a real repository | one command, end to end |
| **Where deterministic reasoning stops** | the KPI, both numbers |
| What the workflow could not decide | the plan's enumerated `defers` |
| Friction | anything the architecture could not express, recorded rather than worked around |

## Stopping condition

Stop when the workflow has run and the boundary is measured — **whether or not
the result is flattering.**

**Do not extend the model to improve the number.**
