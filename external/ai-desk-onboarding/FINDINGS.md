---
id: EXTERNAL-AIDESK-ONBOARDING-FINDINGS
title: Findings — the first Brownfield onboarding
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0090, ADR-0105, ADR-0106, ADR-0107]
---

# Findings — the first Brownfield onboarding

**A complete vertical slice**, from a repository and one bootstrap node to a
compiled model, generated products and an Engineering Plan.

```sh
python3 discovery/run.py /Users/willy/Localsources/ai-desk external/ai-desk-onboarding
python3 tools/review.py external/ai-desk-onboarding summary
python3 tools/review.py external/ai-desk-onboarding apply --ids=… --reviewer=…
python3 tools/compile.py external/ai-desk-onboarding
python3 tools/direct.py external/ai-desk-onboarding I-modify-behavior Capability.Auth
```

## What discovery produced

**315 entities · 365 relationships · 5 ambiguities · 8 gaps**, from a 469-file
repository, reproducibly — the candidate model carries a content digest.

| Extracted | |
|---|---|
| packages · frameworks | 4 · 18 |
| NestJS modules | 28 |
| API endpoints | 161 |
| database tables | 34 (30 tenant-scoped) |
| test suites | 70 |
| environment variables | 27 |
| external integrations | 5 |
| existing ADRs | 5 |
| **invariants inferred** | **94** |

| Support | Count | Review |
|---|---|---|
| `S-tested` | 234 | batch |
| `S-inferred` | 218 | **individual** |
| `S-implemented` | 124 | batch |
| `S-confirmed-deterministic` | 99 | batch |
| `S-specified` | 5 | **individual** |

## The honest comparison

> *Show exactly how the resulting plan is better than the earlier ad hoc
> grep-based model.*

**In some ways it is not**, and the ways it is not are the finding.

| | grep-based | discovered |
|---|---|---|
| invariants surfaced for the OAuth plan | 5 | **7** |
| test suites named | 5 | 5 |
| distinct targets | 13 | 13 |
| tasks | 6 | **5** |
| decisions before the first LLM token | **54** | 51 |

**The KPI went down.** The discovered plan makes fewer decisions upstream, not
more.

### Where discovery wins

**Coverage and reproducibility.** The hand model covered one module; discovery
covered 28, found 161 endpoints and 34 tables, and would find them again
identically. **A human reading source does not scale and does not repeat.**

It also produced findings no one asked for: **all five ADRs are `Proposed` while
the codebase implements them**, `refresh_tokens` carries no tenant column in a
system whose foundational decision is tenant isolation, and two modules have no
test suite.

### Where discovery loses, and why

The grep model's invariants are **concepts**: `TenantIsolation`,
`NoUserEnumeration`, `RefreshRotation`, `TokenIntegrity`.

The discovered model's are **transcriptions**:
`RejectsA7CharPasswordBelowMinimum`, `RejectsANonStringPasswordTypeConfusio`.

**A human read eight lockout test cases and wrote one invariant. Rule `R1` reads
eight test names and proposes eight invariants.** More assertions, worse
abstractions.

**And the most important one was missed.** `TenantIsolation` is stated in ADR
prose. `R1` reads test names. **A bounded rule cannot find what is not where it
looks**, and no rule was written for prose because writing one deterministically
means pattern-matching English.

### What that measures

This is the **deterministic ceiling**, measured rather than assumed
(`ADR-0107`):

> **Deterministic extraction is better than a human at coverage and worse at
> abstraction.**

That is the argument for a probabilistic interpreter — and it is now an argument
from evidence rather than from expectation. `ADR-0103` permits one; this is the
measurement that would justify building it.

## The applier

**25 entities and 23 relationships authorized** from 315, by an explicit
reviewer. 290 left unaccepted. **342 relationships were refused** because an
endpoint was not accepted — an edge to an unaccepted node would compile to a
dangling reference.

An accepted proposal becomes an **authoring source**, not a model write
(`ADR-0106`). Each carries its provenance, support classification, originating
worker and task, and — where inferred — the rule.

**The compiler is unchanged.** It reads a generated source exactly as it reads a
hand-written one.

## Two defects the pipeline found

**The applier's YAML emission was wrong.** Hand-rolled quoting broke on a label
containing `:` and on a value beginning with `@`. **A generated source is compiler
input**, so the fix was to emit with a YAML writer — which `ADR-0106` predicted
when it recorded that the parser schema becomes load-bearing.

**`implements` was used directly and was not registered.** The fourth instance of
a core relationship type used directly rather than specialized — the same gap
`SESSION-0028` found three times.

## Generated products

All deterministic, all from the CKM:

| Product | State |
|---|---|
| Canonical Knowledge Model | 27 nodes, 24 edges |
| OWL ontology | `model.ttl`, imports the metamodel |
| **SHACL shapes** | `shapes.ttl`, 73 triples — **generated from the same registries the compiler reads**, so shapes and compiler cannot disagree |
| **Search, impact, traceability indexes** | `indexes.json` — **derived by the declared query engine**, so an index and an answer cannot disagree |
| Navigable Knowledge Explorer | `explorer.html`, self-contained, question-driven |
| Mermaid graph | `graph.md` |

## Limitations

**The authorized slice is 25 of 315.** The compiled model is small because
review is individual for inferred assertions and only auth was authorized.

**No workflows were discovered.** No worker extracts them; recorded as a gap.

**Nothing was observed at runtime.** Discovery read files only; recorded as a gap.

**Bounded interpreters are stack-specific.** `R1` reads TypeScript `it()` names.
