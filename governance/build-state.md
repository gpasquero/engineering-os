---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: brownfield
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**Brownfield onboarding** — both halves: **discovery production** and **proposal
intake and application** (`ADR-0107`).

## The complete slice runs

```sh
python3 discovery/run.py /Users/willy/Localsources/ai-desk external/ai-desk-onboarding
python3 tools/review.py external/ai-desk-onboarding summary
python3 tools/review.py external/ai-desk-onboarding apply --ids=… --reviewer=…
python3 tools/compile.py external/ai-desk-onboarding
python3 tools/direct.py external/ai-desk-onboarding I-modify-behavior Capability.Auth
```

**ai-desk + one bootstrap node → 315 proposals → 25 authorized → CKM → OWL,
SHACL, indexes, explorer → Engineering Plan.**

## The honest result

| | grep-based | discovered |
|---|---|---|
| invariants for the OAuth plan | 5 | **7** |
| tasks | 6 | 5 |
| decisions before the first LLM token | **54** | 51 |

**The KPI went down.** Discovery wins on **coverage and reproducibility** — 28
modules, 161 endpoints, 34 tables, 70 test suites, repeatable with a stable
digest — and **loses on abstraction**.

A human read eight lockout tests and wrote **one** invariant. Rule `R1` reads
eight test names and proposes **eight**. And **tenant isolation was missed
entirely**: it is stated in ADR prose, and `R1` reads test names.

> **Deterministic extraction is better than a human at coverage and worse at
> abstraction.**

That is the **deterministic ceiling, measured rather than assumed** — and the
argument for a probabilistic interpreter is now evidential (`ADR-0103` permits
one; none is built).

## What exists

| Area | State |
|---|---|
| **`discovery/workers/extractors.py`** | 8 deterministic extractors — structure, stack, modules, APIs, persistence, tests, config, integrations, decisions |
| **`discovery/workers/interpreters.py`** | 2 bounded rules + gap identification. **Every inference names its rule** |
| **`discovery/candidate.py`** | Candidate Engineering Model with a content digest |
| **`compiler/apply/`** | Authorization + application. **An accepted proposal becomes an authoring source, never a model write** |
| **`tools/review.py`** | Summary, ambiguities, gaps, conflicts, authorize-and-apply |
| **`model/support-classification.md`** | 8 kinds — 3 batch-reviewable, 3 individual, 1 gap-only |
| **`compiler/emitters/shacl/`** | Shapes **generated from the same registries the compiler reads** |
| **`compiler/emitters/indexes/`** | Search, impact, traceability — **derived by the declared query engine** |
| `external/ai-desk-onboarding/` | Candidate model · 25 authorized sources · CKM · 6 generated products |
| `tests/` | 17 fixtures, 9 negative, golden outputs for **6 emitters** |
| Registries | 15 |
| `model/metamodel/` | 23 of 27 entities — **unchanged for eight milestones** |

## Findings about ai-desk that no one asked for

- **All five ADRs are `Proposed`** while the codebase implements them — recorded
  as five ambiguities, not silently resolved.
- **`refresh_tokens` carries no tenant column**, in a system whose foundational
  decision is tenant isolation via RLS. Recorded as a gap: *whether that is
  correct is unrecorded.*
- **Two modules have no test suite** in the modelled scope.
- 30 of 34 tables are tenant-scoped; the 4 that are not are each recorded.

## Two defects the pipeline found

**The applier's YAML emission was wrong** — hand-rolled quoting broke on a label
containing `:` and a value beginning with `@`. **A generated source is compiler
input**, which `ADR-0106` predicted would make the parser schema load-bearing.

**`implements` was used directly and unregistered** — the fourth instance of a
core relationship type used directly rather than specialized.

## What does not exist

**No probabilistic interpreter.** The ceiling is measured and nothing crosses it.

**No prose rule.** Tenant isolation is missed because no bounded rule reads ADR
prose.

**Nothing applies an execution observation** — though the applier that would do
it now exists, which is `ADR-0106`'s point.

**No workflow discovery. No runtime observation.** Both recorded as gaps.

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. Fifteen registries, zero generated |

## Debt discovered while building

| Question | Where |
|---|---|
| **94 invariants inferred, each a transcription rather than a concept** | `ai-desk-onboarding/FINDINGS.md` |
| A bounded rule cannot find what is not where it looks | `ADR-0107` |
| Extractors are stack-specific and need writing again for the next stack | `ADR-0107` |
| Review is individual for `S-inferred`, so 218 of 315 proposals need one-by-one judgement | `support-classification.md` |
| `S-implemented` and `S-tested` overlap; the extractor decides by file path | `support-classification.md` |

## Next action

**A rule that reads prose, or the first probabilistic interpreter.** The
measurement above is its justification, and `ADR-0103` requires the justification
to be genuine rather than convenient.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
