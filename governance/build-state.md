---
id: BUILD-STATE
title: Build State
status: current
created: 2026-08-02
updated: 2026-08-02
milestone: kubernetes-ssa
---

# Build State

**This document describes only what exists. Planned work belongs in
`governance/roadmap.md`. Overwrite this file; do not append.**

> An **Authoritative Artifact**, not a projection (`ADR-0016`).
> Semantic Layer: `None` — this is a governance artifact (`ADR-0039`).

## Current work

**The Kubernetes Server-Side Apply validation** (`ADR-0087`) — **executed**.

## The result

```sh
python3 tools/compile.py external/kubernetes-ssa
python3 tools/ask.py external/kubernetes-ssa Q-evidence Invariant.TimestampNotUpdatedOnTakeover
```

> **A `managedFields` entry's `time` is not the time that entry last changed.**

The API type comment states that a timestamp does not update when another manager
takes a field over. The documentation states that `force` removes the field from
all other managers' entries. **Neither mentions the other.** `conflict.go` renders
that timestamp in the message a user reads while reasoning about ownership.

**No fetched document contains the conclusion.** It exists only in the join —
which is what `ADR-0087` set out to test.

**Honest strength:** a documentation-and-observability finding, not a correctness
bug. The weakest form of the claim that still counts.

## What exists

| Area | State |
|---|---|
| **`external/kubernetes-ssa/`** | Charter · **41 nodes, 75 edges** · reviewed ground truth · findings |
| | Four source classes: **KEP-555, kubernetes.io docs, three source files, the integration test file** — every one fetched and verified |
| | **18 Evidence nodes**, each with source URI, locator and kind |
| `model/queries.md` | **14 declared queries** — `Q-constraints`, `Q-evidence`, `Q-unsupported` added, all domain-neutral |
| `compiler/parser/` | Nodes carry an **uninterpreted `attributes` mapping** — the one gap the milestone found |
| `tests/` | **16 fixtures**, 9 negative, golden outputs, determinism, query rows/status/paths |
| Parity | **832 query/subject pairs** across three projects, full fidelity |
| `model/metamodel/` | 23 of 27 entities — **unchanged this milestone** |
| ADRs | 88 — 80 accepted, 8 superseded. **No new ADR** |
| Issues | 74 — 1 open, 51 resolved, 22 deferred |
| Acceptance Records | 27 |
| Session journal | 32 entries |

**No Kubernetes-specific entity, predicate, operator or compiler behaviour was
added.** The domain arrived entirely as Layer B data.

## Completion criteria (`ADR-0087`)

| Criterion | State |
|---|---|
| one subsystem modelled deeply | ✅ SSA and managed fields |
| all four source classes connected | ✅ KEPs, docs, source, tests |
| the seven required questions execute | ✅ through the shared query engine |
| expected answers reviewed | ✅ `ground-truth.md`, classified confirmed/incomplete/ambiguous |
| at least one cross-source insight | ✅ the timestamp finding |
| limitations documented | ✅ six, including the sharpest one |
| all fixtures green | ✅ 16 projects |
| build deterministic | ✅ |
| no Kubernetes leakage into compiler core | ✅ |

## Limitations found

| Limitation | Consequence |
|---|---|
| **Test granularity is the file** | `Q-tests` names a file of 30 test functions, not the test protecting a behaviour. **The sharpest limitation** |
| KEP granularity is the document | KEP-555 establishes six things; `Q-rationale` is correspondingly blunt |
| Only KEP-555 read in full | Q5's refinement edges mean *same subsystem*, not *verified refinement*; classified **ambiguous** |
| Hop distance is not severity | Q6 returns 9 nodes at 1–4 hops with no ranking |
| 41 nodes | Traversal limits never fired; scale is untested |

## Path selection — the predicted question did not arise

`ADR-0088` notes that retaining the best deterministic path is not the same as
preserving all valid explanations. **In this model it did not matter**: every
multi-hop result reached its target by one materially distinct evidence path.
**Recorded, not acted on**, as directed.

## Blocking

**Nothing.**

| Issue | Why it is open |
|---|---|
| `ISSUE-0037` | Hand-maintained projections. Five registries, five hand-maintained sources, zero generated |

## Next action

**The Project Owner's decision.** The milestone's completion criteria are met and
`ADR-0084` says framework expansion waits until the proof is complete.

If a second iteration is wanted, `FINDINGS.md` ranks three changes, and the first
is worth more than the other two together: **model individual test functions** —
it makes Q3 precise and costs 30 nodes.

## Repository state

- Branch: `main`, published to `github.com/gpasquero/engineering-os`
- Licence: **Apache-2.0**
