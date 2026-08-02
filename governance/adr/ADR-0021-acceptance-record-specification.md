---
id: ADR-0021
title: Acceptance Records are first-class authoritative artifacts with a defined specification
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0041]
related: [ADR-0020, ADR-0022, ADR-0023, ISSUE-0042]
---

# ADR-0021 — Acceptance Record specification

## Context

`ADR-0020` (via `ADR-0018`) makes acceptance the act that confers authoritative
status, and requires that acceptance be traceable knowledge. `ISSUE-0041`
recorded that nothing defined what an acceptance record *is* — its fields,
location, or artifact kind — and that its third condition depends on validation
tooling that will not exist until M9.

## Decision

**Acceptance Records are first-class Authoritative Artifacts** with a dedicated
specification.

### Location

```text
governance/acceptance/
```

### Minimum fields

- `id`
- artifact identifier
- artifact revision
- reviewer
- acceptance date
- acceptance decision
- rationale
- related ADRs
- related Issues
- validation summary
- exceptions
- supersedes
- superseded by
- signatures *(future extension)*

### Deterministic validation — the applicability rule

Condition 3 of acceptance requires successful validation of **all applicable**
deterministic validations.

**If no deterministic validator exists yet, then none are applicable, and
condition 3 is satisfied.**

This is **not an exception**. It is the normal interpretation of applicability.
As validation tooling evolves, additional deterministic checks automatically
become applicable without any change to the acceptance model.

## Alternatives considered

**Embed acceptance in the accepted artifact's front matter.** Rejected: the
artifact would be modified by its own acceptance, changing the very revision
being accepted. It would also make acceptance history unreadable, since each new
acceptance would overwrite the last.

**Use signed commits or git trailers.** Rejected: `ADR-0018` established that
acceptance is an engineering decision, not a Git operation. Encoding it in VCS
metadata would reintroduce exactly the coupling that decision removed, and would
make acceptance invisible to the knowledge compiler.

**Treat condition 3 as blocking until validators exist.** Rejected, and this is
the important rejection: it would make *every* artifact unacceptable before M9,
including the decision needed to bootstrap the trust root. The applicability
reading avoids inventing a temporary exception that would later need unwinding.

**Treat condition 3 as a waived exception until M9.** Rejected for the same
reason stated positively: an exception must be tracked, expire, and be removed.
Applicability needs none of that, and produces identical behaviour.

## Consequences

### Positive

- `ADR-0018` becomes implementable, and `ISSUE-0040` becomes resolvable — there
  is now somewhere to write that something was accepted.
- The `exceptions` field makes deviations explicit and reviewable rather than
  silent.
- `supersedes` / `superseded by` give acceptance its own history, so an artifact
  re-accepted after revision keeps a readable chain.
- The applicability rule means the acceptance model never changes as tooling
  arrives — checks simply become applicable.

### Negative

- **Acceptance Records are Authoritative Artifacts, so by the letter of
  `ADR-0020` they require acceptance themselves — an infinite regress.**
  Recorded as `ISSUE-0042`; the base case is not settled here.
- Real friction per change. Every authoritative revision now needs a record,
  authored and reviewed.
- The `validation summary` field will be near-empty until M9, which risks
  becoming a formality that is later ignored rather than filled.

### Neutral

- `signatures` is named as a future extension and deliberately unspecified.

## Compliance

Every Authoritative Artifact revision that is `Active` has a corresponding
Acceptance Record under `governance/acceptance/`. No acceptance is recorded
anywhere else. A record with an empty `validation summary` is valid only where
no deterministic validator was applicable.
