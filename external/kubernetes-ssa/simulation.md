---
id: EXTERNAL-K8S-SSA-SIMULATION
title: End-to-end orchestration simulation
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0098, ADR-0099, ADR-0100, ADR-0101]
---

# End-to-end orchestration simulation

> **The implementation is mocked. The orchestration is not.**

```sh
python3 tools/direct.py external/kubernetes-ssa I-modify-behavior Artifact.ConflictGo \
    --observations=external/kubernetes-ssa/simulated-observations.yaml
```

One command runs the complete deterministic loop:

```text
Developer Intent → Plan → Task Graph → Worker Assignment
   → Execution Context → [mocked Execution] → Observations → Knowledge Update proposal
```

**No language model participates.**

## What the run produces

| Stage | Result |
|---|---|
| Intent | `I-modify-behavior` — *what am I changing, and what depends on it?* |
| Plan | `P-change-implementation`, 4 phases, 3 deferred decisions |
| Task Graph | 5 tasks, 5 levels, 3 mechanical · 2 reasoning · 1 gate |
| Assignment | 4 assignable, **1 awaiting authorization** |
| Contexts | 5 execution packages, 9 fields each |
| Observations | 6 emitted → **2 record · 2 govern · 2 reject** |
| **KPI** | **36 decisions before the first LLM token · 5 left to workers** |

## The observations, and what happened to each

| Kind | Outcome | Why |
|---|---|---|
| `O-evidence-discovered` | **record** | additive; adds provenance to an existing claim |
| `O-invariant-confirmed` | **record** | corroboration; changes no assertion |
| `O-unexpected-dependency` | **govern** → `G-knowledge-update` | a new edge changes every downstream impact answer |
| `O-assumption-disproved` | **govern** → `G-decision-record` | a failed assumption usually means a decision was made on wrong grounds |
| `O-architectural-concern` | **reject** | an opinion, not an observation |
| `O-performance-regression` | **reject** | **no such kind** — rejected with a diagnostic rather than ignored |

**Only two of six may enter the model mechanically, and both are additive.**
That distribution is the design, not an accident: workers never write to the
model, and everything that could change or contradict an assertion is governed.

## Two defects, found only by running the loop

Both were in **declarations**, not in the engine, and both were invisible to
every existing check.

### Gate identifiers were written without their prefix

`G-decision-record` declared `required-for-observation-kinds:
[assumption-disproved, ...]` while the kinds are `O-assumption-disproved`. **The
gate matched nothing**, and every governed observation silently fell through to
the general `G-knowledge-update` gate.

**A registry that names things wrongly is not detectably different from one that
names nothing.** Nothing checked cross-registry references.

### A gate was declared for an observation kind that is rejected

`architectural-concern` is classified `reject` — it never enters the model. A
gate authorizing its entry is **unreachable by construction**, and the
declaration asserted a control that could never fire.

## What the simulation exposed about the architecture

**The loop runs, and it does not close.** `T05-update-knowledge` is assignable to
`W-knowledge-recorder` and produces a **proposal**. Nothing applies it: no
authorization artifact exists, and no path writes an approved proposal back into
the model.

**Every run ends at a human.** `T04-review-gate` requires `C-approve`, which no
worker provides (`ADR-0100`). That is by design, and it means no end-to-end run
ever completes unattended.

**Assignment is under-determined and correctly so.** `T02-change-inspect` matches
four worker types — including `W-documentation-writer`, which is plainly wrong
for it. Capability matching cannot express *the right worker for this kind of
artifact*, and preferring one would be a heuristic (`ADR-0099`).

**One assumption was carried into execution as UNVERIFIED** and the mocked
execution disproved it — the `Concept.Conflict` traceability gap, arriving for
the third time: found by a query, used by a plan, and now confirmed by a run.

## Honesty about what this is not

**No Kubernetes code was read, changed or tested.** The observations are
plausible and invented, and every statement in
`simulated-observations.yaml` is marked unverified. **Nothing here is a claim
about Server-Side Apply.**

What is real is the orchestration: the plan, graph, assignment, contexts, intake
classification and gate routing are all derived from declarations and the model.
