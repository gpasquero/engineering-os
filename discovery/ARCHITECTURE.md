---
id: DISCOVERY-ARCHITECTURE
title: Engineering Discovery — architecture
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0060, ADR-0061, ADR-0072, ADR-0101, ADR-0105, ADR-0106]
---

# Engineering Discovery — architecture

> **Engineering Discovery is the first engineering workflow executed by
> Engineering OS itself** (`ADR-0105`). It is not a preprocessing step.

```text
Repository → Discovery Intent → Discovery Plan → Discovery Task Graph
   → Discovery Workers → Candidate Engineering Model → Engineering Review
   → Authoritative Engineering Model → Compiler → CKM → Director
```

## The claim, and its test

> **The only difference between Brownfield and Continuous Engineering is the
> objective. Everything else is identical.**

**Tested, and it holds.** `I-onboard` on a repository produces a plan, a task
graph, worker assignments, a governance gate and a knowledge-update task —
through **`tools/direct.py` unchanged**:

```sh
python3 tools/compile.py external/ai-desk-onboarding
python3 tools/direct.py external/ai-desk-onboarding I-onboard Artifact.AiDeskRepository
```

**No execution mechanism was built.** Discovery is declarations in the existing
registries.

## The bootstrap: a repository is an Artifact

A repository under discovery has no model, and every plan requires a subject that
is a node. **Exactly one node is authored — the repository itself.**

Discovery is then a plan applied to it. **No special case, no second entry
point**, and the seed is two files.

## Contracts

### In: the Execution Context

Unchanged (`ADR-0101`). A discovery worker receives the same nine-field package
as any other worker: objective, rationale, assumptions, evidence, affected nodes,
expected outputs, completion conditions, required updates, **allowed scope**.

For discovery, `allowedScope` is what makes *which files may this worker read* a
declared fact rather than a worker's discretion.

### Out: proposed assertions

A Candidate Engineering Model is **a set of proposed assertions**, in the same
shape an Execution Observation produces after intake (`ADR-0106`):

| Field | Required |
|---|---|
| the assertion — node or edge | yes |
| provenance — file, locator | **yes; a proposal without it is a guess** |
| origin — worker, task, run | yes |
| intake outcome | assigned by intake, not by the worker |
| what it would displace | yes when it contradicts something |
| confidence | optional; **may only add scrutiny** (`ADR-0104`) |

> **Nothing is authoritative until reviewed.** The gate every task graph already
> terminates in is the one that makes a candidate model authoritative — the same
> gate, not a discovery-specific one.

## Artifacts

| Artifact | Is | Authoritative |
|---|---|---|
| Seed model | one node: the repository | yes, authored |
| Candidate Engineering Model | proposed assertions with provenance | **no** |
| Gap report | what discovery did **not** find | **no**, and proposes no knowledge |
| Authoritative Engineering Model | accepted proposals, written as authoring sources | yes |
| CKM | compiled from the above | derived (`ADR-0072`) |

## Worker types

Declared in `model/workers.md`. **Discovery workers read source; nothing else in
the architecture ever does** (`ADR-0105`).

| Worker | Provides | Class |
|---|---|---|
| `W-structure-extractor` | parse, query | **mechanical** |
| `W-domain-interpreter` | parse, interpret, propose | reasoning |
| `W-constraint-interpreter` | read, interpret, propose | reasoning |
| `W-decision-archaeologist` | read, interpret, propose | reasoning |
| `W-gap-identifier` | query, propose | **mechanical** |

**Two of five are mechanical**, and the split is `ADR-0060`'s: structure is
derived, meaning is interpreted.

`W-decision-archaeologist` **proposes nothing where a rationale is absent** — a
missing decision is a knowledge gap, not a gap to fill.

## Extension points

Every one is a registry entry. **No code changes to add a discovery capability.**

| To add | Declare in |
|---|---|
| an activity — API, database, runtime discovery | a task kind + a plan phase |
| a worker type | `model/workers.md` |
| a capability | `model/worker-capabilities.md` |
| a proposal category requiring authorization | `model/governance-gates.md` |
| a new discovery objective | `model/engineering-intents.md` |

**The action vocabulary is derived from task kinds**, so an activity's action
exists because its task kind declares it. That was found by friction: declaring
discovery needed three new actions, and the vocabulary was hardcoded in Python.

## Interaction with the compiler

**The compiler is unchanged and gains no input class.**

```text
proposed assertions → review → AUTHORING SOURCES → compiler → CKM
```

An accepted proposal is **written as an authoring source and recompiled like
everything else** (`ADR-0106`). The compiler remains the only writer of the
model, and it still writes from authoring sources — one of which may now
originate from a worker, after review.

This is why `ADR-0072` and `ADR-0081` survive without exception, and why
**discovery intake and the loop's knowledge-update are one mechanism**, not two.

## Not built

**Everything downstream of the task graph.** No discovery worker exists, no
proposal format is serialised, and **no applier writes an accepted proposal as an
authoring source** — which is the same missing mechanism the loop has lacked
since `SESSION-0036`.

## The problem this architecture does not solve

**Review does not scale.** A candidate model for a 469-file repository may
propose thousands of assertions, each requiring acceptance.

Batch acceptance — *accept every evidence proposal from this run* — is the
obvious mitigation and **trades scrutiny for throughput**, which is the trade
`ADR-0023` exists to prevent. It is recorded unresolved rather than settled
speculatively.

**The architecture is correct and the bottleneck is real.**
