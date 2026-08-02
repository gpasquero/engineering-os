---
id: EXAMPLE-VERTICAL-SLICE
title: The first vertical slice
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: B
artifact-kind: authoritative
established-by: [ADR-0080, ADR-0081, ADR-0082]
---

# The first vertical slice

```text
Authoritative Repository → Compiler → Canonical Knowledge Model
                                            ↓
                          Knowledge Explorer · tools/ask.py
                                            ↓
                                  Developer Question
                                            ↓
                                    Semantic Answer
```

**28 nodes, 52 edges.** A small ordering domain with enough governance around it
that questions are worth asking.

```sh
python3 tools/compile.py examples/vertical-slice
python3 tools/ask.py examples/vertical-slice questions
python3 tools/ask.py examples/vertical-slice impact Concept.Order
python3 tools/ask.py examples/vertical-slice impact Concept.Order --json
open examples/vertical-slice/build/explorer.html
```

## The seven questions

`ADR-0082` names seven questions a developer must be able to ask. **Six are
answered from the model. One is not, and the reason matters.**

### 1. What breaks if I change this Concept? ✅

```text
$ python3 tools/ask.py examples/vertical-slice impact Concept.Order
  affected:
    Artifact.CheckoutTests   hops=1  via=references
    Artifact.OrderingSpec    hops=1  via=represents
    Capability.PlaceOrder    hops=1  via=references
    Invariant.PaymentBeforeShipping  hops=1  via=constrains
    Skill.ValidateOrder      hops=1  via=requires
    ADR.011                  hops=2  via=constrains
    ...
```

Transitive closure over incoming edges. **Ten nodes affected, seven directly.**

### 2. Why does this relationship exist? ✅

Every edge carries its core type, category and the vocabulary definition — from
the model, without consulting the metamodel.

### 3. Which ADR established this Invariant? ✅

```text
$ python3 tools/ask.py examples/vertical-slice rationale Invariant.PaymentBeforeShipping
  established_by:
    ADR.011  Payment is settled synchronously at checkout  via=establishes
```

And it reports **whether the establishing decision still stands** —
`Invariant.SingleCurrency` traces to `ADR.004`, which is superseded.

### 4. Which Capabilities depend on this Workflow? ✅

`Capability.PlaceOrder` and `Capability.Refund`, the second reached only through
a shared Skill.

### 5. Which Tests must change? ✅ — with a caveat

`Artifact.CheckoutTests`. **There is no `Test` entity.** A test is modelled as an
Artifact that `validates` another and `references` the Concepts it exercises.

That the question is answerable without a `Test` entity is evidence for
`ADR-0067`: a `Test` would introduce no relationship `validates` does not
already express.

### 6. Which Specifications become inconsistent? ✅ — same caveat

`Artifact.OrderingSpec`, found through `represents`. No `Specification` entity
either.

### 7. Which AI workflow should execute? ❌ **Not answerable**

Nothing in the metamodel connects **a kind of change** to **a workflow that
should handle it**. `Policy.governs` points at a Workflow but is not conditional
on a change; `EngineeringGate` reviews but does not select.

**The missing concept is a trigger** — *when this kind of thing changes, run
that*. `ADR-0068` classified `triggers` as a core relationship type and **no
entity uses it.**

This is the finding the slice exists to produce. `ADR-0082` predicted two
questions might not be answerable; one was, and this is the other.

## What the model demonstrates, not asserts

| | Where |
|---|---|
| **An unenforced Invariant is a finding** | `Invariant.SingleCurrency` has no `enforced-at`. `ask.py unenforced` lists it |
| **An unaccepted revision is not Active** | `ArtifactRevision.Payment.r3` has no AcceptanceRecord. `status` reports `active=False` |
| **A superseded ADR stays readable** | `ADR.004` is superseded by `ADR.011` and both remain in the model |
| **Ordering is extrinsic** | Two `WorkflowStep`s carry positions; the Skills do not |
| **Evidence is ranked by directness** | `Evidence.PaymentTrace` is a runtime observation; `Evidence.OrderSchema` a source reference |

## Agents are a first-class consumer

`--json` on every question. `tools/ask.py` **parses no authoring source** — it
consumes the Canonical Knowledge Model, which is what `ADR-0081` requires of
every component.

## What is still missing

- **Provenance is a path, not a revision.** `ADR-0064` wants
  `(artifact-id, revision-id)`.
- **No trigger concept**, so question 7 is unanswerable.
- **Closures are computed by scanning.** There is no index, and the Explorer
  computes them in the browser. Nobody knows where that stops.
- **The model is 28 nodes.** A metamodel that only models small examples is still
  unproven; `ADR-0082` makes modeling a real external system the next milestone.
