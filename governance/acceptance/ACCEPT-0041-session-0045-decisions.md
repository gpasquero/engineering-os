---
id: ACCEPT-0041
artifact: SESSION-0045 — Stack Profiles and the first generalization benchmark
artifact-revision: 92a0248
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0117, ADR-0118, ADR-0119]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0041 — Generalization, validated by failing honestly

## Artifact

The work of `SESSION-0045`, at revision **`92a0248`**.

Scope: `ADR-0117`, `ADR-0118`, `ADR-0119`, the declarative extractor and its two
Stack Profiles, the `R4` fabrication fix, and
`external/wa-b2b-onboarding/BENCHMARK.md`.

**Sequence continuous.**

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **The first meaningful validation that Engineering OS generalizes beyond
  repositories it was implicitly shaped around.**
- **The most important outcome is not that Spring Boot worked. It is that
  Engineering OS failed honestly.** The repository exercised the existing
  architecture without requiring metamodel changes, and the shortcomings
  appeared as **missing engineering understanding rather than missing
  engineering structure**.
- **`ADR-0117` is the correct abstraction.** Mechanical Acquisition stays
  stack-aware and repository-independent; Interpretive Discovery continues to
  consume only the Mechanical Engineering Model; framework-specific semantics
  must not leak into Discovery Skills.
- **The benchmark succeeded because it produced actionable ignorance. Nine
  unanswered engineering questions are a better result than nine fabricated
  answers.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

Three decisions, each implemented in the session that recorded it, and each
tested against a repository chosen for engineering characteristics rather than
language.

## Condition 3 — validation summary

276 records, 17 fixtures, 20 registries, both query engines in agreement, the
governance corpus checked by a committed tool, and the `ai-desk` lifecycle
reproducing its recorded result with only the mechanical digest changed.

## Exceptions

None. `DS-authorization-discovery` remains unbuilt by explicit direction, and
the reviewer set its evidence bar: the same missing understanding in a
fundamentally different repository — Spring Security, ASP.NET Identity, NestJS
Guards, Django Permissions.

## Notes

The reviewer set three further directions, recorded as decisions:

- **`ADR-0120`** — *the percentage of useful engineering questions answered* is
  the product metric; entities, predicates, graph size and proposal count are
  implementation metrics.
- **`ADR-0121`** — Technology and Domain Discovery Skills are distinct kinds
  that **produce exactly the same metamodel entities** and differ only in how
  understanding is acquired.
- **`ADR-0122`** — *Discovery exists so that six months later an engineer can ask
  a difficult question and receive an answer nobody had to rediscover.*

And the next benchmark: an event-driven system, chosen for **another engineering
shape**, not another technology.
