---
id: EXTERNAL-AIDESK-AUTH-FINDINGS
title: Findings — running the Engineering Director on a real repository
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0090, ADR-0098, ADR-0102, ADR-0103]
---

# Findings — ai-desk authentication

**31 nodes, 63 edges**, modelled from the working tree of a real 469-file
TypeScript repository. Every symbol, test name and quotation extracted by `grep`
on 2026-08-02.

```sh
python3 tools/compile.py external/ai-desk-auth
python3 tools/direct.py external/ai-desk-auth I-modify-behavior Capability.Login
python3 tools/advise.py external/ai-desk-auth R-audit-model
```

## The measurement

> **Where does deterministic reasoning stop and workers begin?**

| Workflow | Before the first LLM token | Left to workers |
|---|---|---|
| *"I need to add OAuth"* → `Capability.Login` | **54** | 7 |
| Change `Artifact.AuthService` | **54** | 6 |

The 7: four decisions the plan enumerates as deferred, and three tasks classed
`reasoning`.

**Of six tasks, three are mechanical or gated and three require a worker.** The
boundary is not a ratio to be optimised — it is a list, and each item can be
examined.

## Friction, which is the point

`ADR-0102` says architectural change should originate from friction observed
during real execution. **This run produced exactly one piece, immediately.**

### The natural subject had no plan

`I-modify-behavior` on `Capability.Login` — the obvious reading of *"I need to
add OAuth"* — returned:

```text
NOT-APPLICABLE — no plan selected by 'I-modify-behavior' applies to 'Capability.Login'
```

`P-change-implementation` applies to `Artifact`. `P-change-concept` applies to
`Concept`. **Nothing applied to a capability**, which is what a feature request
actually changes.

`P-change-capability` was added **because a real run could not express the
workflow it was given** — not because an inventory was incomplete. That is the
first architectural change in this project motivated by friction rather than by
inspection.

**The friction was recorded before it was fixed**, and the failing invocation is
reproducible: the plan is new, the model is not.

## Findings about ai-desk

Classified by `ADR-0090`. **Kind describes what was found; support describes how
well it is evidenced.**

| # | Finding | Kind | Rank | Support |
|---|---|---|---|---|
| 1 | **`Invariant.TenantIdOnEveryConnection` has no enforcement point.** ADR-0001 calls it "discipline: `tenant_id` must be set on every connection" | **traceability-gap** | 4 | confirmed |
| 2 | ADR-0001's status is **`Proposed`**, and the codebase implements it | **traceability-gap** | 4 | confirmed |
| 3 | Two test suites — `auth.service.spec.ts` (12 cases) and `password-security.spec.ts` (11) — **have no invariant traced to them** | **documentation-gap** | 5 | confirmed |
| 4 | `jwt-security.spec.ts` asserts "rejects a token with a tampered payload (modified `tid`)" — **tenant isolation enforced at the token layer**, in a suite that never names the multi-tenancy decision | **traceability-gap** | 4 | confirmed |
| 5 | Account lockout's exact 15-minute window and the no-enumeration guarantee are **stated only as test names** | **documentation-gap** | 5 | confirmed |
| 6 | `JwtAuthGuard` is a one-line subclass; **all verification behaviour is inherited** and nothing local expresses what it enforces | **observability-gap** | 6 | confirmed |

**Finding 1 is the one worth acting on.** The most foundational decision in the
system — RLS multi-tenancy — rests on a step the ADR itself describes as
requiring discipline, and **no artifact in the modelled scope is recorded as
enforcing it.** The system's strongest isolation claim depends on its weakest
enforcement mechanism.

**Finding 4 is the one that required the model.** The connection between a JWT
test case and the multi-tenancy ADR exists in neither document; it exists in the
graph, because both are modelled and the test's own words name `tid`.

**Ranks 1–3 remain empty**, as they did for Kubernetes. No confirmed
contradiction, no behavioral or architectural inconsistency.

## What this run says about the architecture

**The metamodel needed no change.** Twenty-three entities modelled a Go-based
API-machinery subsystem and a TypeScript SaaS backend without amendment — the
sixth milestone in which it has not moved.

**The one change was a plan, not a construct.** `P-change-capability` is data. No
entity, operator, registry or engine was added, which is what `ADR-0102` requires
of infrastructure.

**Test granularity improved and it mattered.** One node per suite with case
counts — the change the Kubernetes findings ranked first — is what made findings
3 and 5 visible. `Q-tests` still names suites rather than cases; **it is now
useful anyway**, which the file-level model was not.

## Honesty about scope

**No code was changed and no test was run.** The workflow was planned, not
executed; the Director produced tasks and stopped where a worker would begin.

**The model covers authentication only** — 31 nodes of a 469-file repository.
Every finding is bounded by that, and finding 3 in particular may be a modelling
gap rather than a repository one: the two suites without invariants may assert
things the model simply did not capture.
