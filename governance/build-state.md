---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: acquisition
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**Brownfield acquisition** in three stages (`ADR-0110`), across three modes
(`ADR-0112`).

## The trust boundary

> **Review and acceptance, not determinism** (`ADR-0110`).

| | Valuable because |
|---|---|
| Deterministic discovery | reproducible, cheap, auditable |
| Probabilistic discovery | synthesizes meaning across weakly structured evidence |

**Both are used. Neither is authoritative.** `ADR-0103` still protects the
Director — a language model may enter acquisition and never planning — and the
boundary between them is curation.

## The first comparative benchmark

One frozen Mechanical Model, digest `dd47744e6bc66150`. Four interpreters.

| | R1 | R3 | **R4** | Claude |
|---|---|---|---|---|
| assertions | 271 | 203 | **302** | 4 |
| concepts · guarantees | 0 · 99 | 31 · 0 | **31 · 99** | 3 · 0 |
| `specializes` edges | 0 | 0 | **99** | 0 |
| **cross-source syntheses** | 0 | 0 | 0 | **4** |
| reproducible | exactly | exactly | exactly | no |

**Volume and abstraction are different axes.** `R4` proposes 302 assertions and
zero syntheses; the probabilistic worker proposes 4 and 4.

**Three of four probabilistic findings are `F-rule-insufficient`** — the only
failure class that is evidence for probabilistic interpretation. `SESSION-0040`'s
was `F-fact-ignored`, which is not.

**The comparison is contaminated and says so**: the worker had seen `R1`/`R3`/`R4`
output. No proposal is drawn from test text; all rest on route, table, dependency
or document facts. A blind comparison needs a worker that has not seen this
repository.

## The strongest probabilistic finding

**Exactly one route of 161 carries the tenant in its URL path** —
`POST /channels/:tenantSlug/:channelType/webhook`. Every other route derives it
from the token.

**The tenant isolation invariant therefore has two enforcement paths**, and
nothing in the repository records that one is different. Reaching it requires
comparing a route against the distribution of all other routes; **no declared
rule compares a fact to its own population.**

## Granularity is preserved

`ADR-0111`. Both levels, related by `specializes`, using existing constructs:

```text
Invariant.AccountLockoutBruteForceProtection      ← concept
    ▲ specializes
Invariant.LocksTheAccountOnThe5ThWrongPassword    ← guarantee
```

**No `Guarantee` entity.** A specific guarantee is a narrower `Invariant`, and
`specializes` is a registered core type. **The metamodel is unchanged for a tenth
milestone.**

## What exists

| Area | State |
|---|---|
| `discovery/mechanical.py` | Facts only, reproducible, versioned vocabulary |
| **`discovery/interpretive.py`** | 6 named rules, **three comparable strategies** including `R4` |
| **`external/…/experiment/`** | The benchmark and the probabilistic worker's proposals with full `ADR-0109` provenance |
| **`model/interpretive-failures.md`** | 5 classes. *Do not call it an interpretation failure until the required fact is known available* |
| **`model/drift-categories.md`** | 11 categories, all proposals, one recordable |
| `model/assertion-origins.md` | **5 origins**, plus 6 provenance fields required of probabilistic proposals |
| `compiler/apply/` · `tools/review.py` | Authorization and application |
| `external/ai-desk-onboarding/` | Mechanical model · 302 proposals · **30 authored sources** · CKM 32 nodes · 6 products |
| Registries | **18** |
| `model/metamodel/` | 23 of 27 entities — **unchanged for ten milestones** |

## What does not exist

**Continuous Acquisition and Periodic Reacquisition.** Two of three modes are
declared and unbuilt, and **the drift report cannot be meaningful until at least
one incremental update has happened.**

**A blind comparison.** The one run is contaminated by construction.

**Curation measurement** — assertions accepted and rejected under review is the
metric that matters most and was not measured.

**The navigable knowledge product** from a broad authorized model. 30 of 302
proposals are applied.

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. Eighteen registries, zero generated |

## Governance note

**`ACCEPT-0033` and `ACCEPT-0035` are not allocated.** Each was skipped when the
next identifier was requested. Both gaps are documented in the index and in the
records that follow them; validation reports an undocumented gap and accepts a
documented one.

## Debt discovered while building

| Question | Where |
|---|---|
| **Invariant counts stopped being comparable** — `R4` proposes both levels, so *number of invariants* conflates concepts and guarantees | `ADR-0111` |
| A specific invariant with no general one is anomalous and nothing detects it | `ADR-0111` |
| Failure classification is manual; nothing checks whether a fact is in the Mechanical Model | `interpretive-failures.md` |
| `F-fact-ignored` is only detectable in hindsight, when a better rule uses the fact | `interpretive-failures.md` |
| Curation load rises with probabilistic proposals, and review already does not scale | `ADR-0110` |
| The `ADR-0103` boundary now depends on a distinction a reader must hold: models in acquisition, never in direction | `ADR-0110` |

## Next action

**A genuinely blind comparison**, then **Continuous Acquisition** — the mode
whose absence makes the drift report meaningless.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
