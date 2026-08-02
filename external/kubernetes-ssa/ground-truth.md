---
id: EXTERNAL-K8S-SSA-GROUND-TRUTH
title: Ground truth — Kubernetes Server-Side Apply
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0087, ADR-0088]
---

# Ground truth — Kubernetes Server-Side Apply

Expected answers for the seven required questions, **reviewed against the
sources**, each classified:

| Classification | Means |
|---|---|
| **confirmed** | every element traced to a fetched source |
| **incomplete** | correct as far as it goes; the model is missing evidence that exists |
| **ambiguous** | the sources permit more than one reading |
| **unsupported** | the model asserts something no fetched source establishes |

> **"Insufficient evidence" is an available answer.** A confident fabricated
> connection is worse than an incomplete result.

---

## Q1 — Which design decision introduced this behaviour?

```sh
python3 tools/ask.py external/kubernetes-ssa Q-rationale Invariant.StatusFieldsProtected --paths
```

**Answer:** `KEP.555`, via `establishes`.

**Classification: confirmed.** KEP-555 names `ResetFieldsProvider` and the
status-field protection problem it addresses.

**Limitation:** the model records KEP-555 as the establishing decision for six
things. That is faithful to a KEP that large, and it makes `Q-rationale` less
discriminating than it would be on a finer-grained decision record.

## Q2 — Which implementation components realize it?

```sh
python3 tools/ask.py external/kubernetes-ssa Q-specifications Concept.Conflict
```

**Answer:** `Artifact.ConflictGo`.

**Classification: incomplete.** Correct — `conflict.go` was fetched and its
symbols verified. But conflict *detection* also lives in `structured-merge-diff`,
which the charter excludes. **The answer is right and the model is smaller than
the system**, which is the expected consequence of a bounded scope and is stated
rather than hidden.

## Q3 — Which tests protect it?

```sh
python3 tools/ask.py external/kubernetes-ssa Q-tests Concept.ManagedFields
```

**Answer:** `Artifact.ApplyIntegrationTest`.

**Classification: incomplete, and the limitation is structural.** The model has
one node for a file containing **30 test functions**. `Q-tests` can therefore say
*which file* but not *which test*.

**This is a genuine modelling finding, not a defect of the question.** Modelling
each test function as its own Artifact would have made the answer precise. The
charter chose file granularity, and the cost is now measurable.

## Q4 — Which invariants or compatibility guarantees constrain it?

```sh
python3 tools/ask.py external/kubernetes-ssa Q-constraints Capability.ServerSideApply
```

**Answer:** `Invariant.BackwardCompatible`, `Invariant.StatusFieldsProtected`,
`Invariant.ApplyRequiresFieldManager`.

**Classification: confirmed.** The first two are quoted from KEP-555. The third
is derived from a test name — and is recorded in the model as asserted by a test
and stated by no fetched document.

## Q5 — Which later decisions refined or superseded it?

```sh
python3 tools/ask.py external/kubernetes-ssa Q-impact KEP.555
```

**Answer:** `KEP.2155`, `KEP.2885` reference KEP-555. `KEP.5958` references
`Concept.ManagedFields` and does not reach KEP-555.

**Classification: ambiguous.** The KEP *directory listing* was fetched and
confirms these numbers exist; **only KEP-555's README was read in full.** The
`references` edges express *these decisions concern the same subsystem*, not a
verified refinement relation.

`KEP.5958` carries `support: incomplete` in the model for exactly this reason.

> **Engineering OS reports a relationship it can support and does not claim
> supersession it cannot.** The distinction is visible in the model's attributes,
> not only in this document.

## Q6 — What is affected if the behaviour changes?

```sh
python3 tools/ask.py external/kubernetes-ssa Q-impact Concept.Force
```

**Answer:** 9 nodes — the integration tests and the docs directly; three
invariants at 2 hops; KEP-555 at 3; KEP-2155 and KEP-2885 at 4.

**Classification: confirmed, with a caveat about depth.** Every edge is one the
model asserts. **Hop distance is not impact severity**, and nothing in the result
says otherwise. A reader who treats 4 hops as "affected" the way 1 hop is
affected will be wrong.

## Q7 — What becomes discoverable only after combining multiple sources?

**This is the primary proof of value.**

```sh
python3 tools/ask.py external/kubernetes-ssa Q-evidence Invariant.TimestampNotUpdatedOnTakeover
```

**Answer:** `Evidence.TimeFieldComment` (source class: **implementation**) and
`Evidence.DocsForce` (source class: **documentation**).

### The finding

Two facts, in two documents, neither of which mentions the other:

**From `apimachinery/pkg/apis/meta/v1/types.go`**, the `ManagedFieldsEntry.Time`
doc comment:

> "The timestamp will also be updated if a field is added, the manager changes
> any of the owned fields value or removes a field. **The timestamp does not
> update when a field is removed from the entry because another manager took it
> over.**"

**From the Server-Side Apply reference documentation**, on `force`:

> "This forces the operation to succeed, changes the value of the field, and
> **removes the field from all other managers' entries in `managedFields`**."

**Combined:** a forced apply modifies another manager's `managedFields` entry —
removing a field from it — **while leaving that entry's timestamp untouched.**

Therefore:

> **A `managedFields` entry's `time` is not the time that entry last changed.**
> It is the time that manager last acted. After a forced apply, an entry can
> show an old timestamp and a field set that was silently reduced moments ago.

### Why this required more than one source

- The **API type comment** states the timestamp rule and never mentions `force`,
  conflicts or other managers' entries.
- The **documentation** states the force rule and never mentions timestamps.
- The **implementation** (`conflict.go`, `printManager`) renders manager, apiVersion,
  operation **and time** in the conflict message a user sees — so the misleading
  timestamp is surfaced at precisely the moment a user is reasoning about
  ownership.
- The **tests** (`TestApplyUpdateApplyConflictForced`) exercise the forced path
  without asserting anything about timestamps.

**No single fetched document contains the conclusion.** It exists only in the
join.

### Classification: confirmed

Both quotations are verbatim from sources fetched during this session, recorded
as `Evidence` nodes with exact locators. The inference connecting them is
one step and stated explicitly rather than implied.

### Honesty about strength

**This is a documentation-and-observability finding, not a correctness bug.**
Nothing behaves incorrectly. What it shows is that a reader combining the two
rules learns something neither states — which is the claim `ADR-0087` set out to
test, and the weakest form of it that still counts.

**A stronger result would have been a contradiction between sources.** This
validation did not find one, and the model is too small to conclude that none
exists.

---

## Second candidate, recorded and weaker

`Invariant.ApplyRequiresFieldManager` is asserted by a **test name** and by no
fetched document. That is a real gap between test and documentation, and it is
**not** a cross-source insight — it is a single-source observation about an
absence. Recorded so that it is not mistaken for a second proof.

## Answers the model cannot give

| Question | Why |
|---|---|
| *Which test function protects this?* | test granularity is the file |
| *Did KEP-2885 refine or supersede part of KEP-555?* | only KEP-555's README was read |
| *Who owns fields set by defaulting?* | the documentation does not address it, and the model does not invent an answer |
| *What does structured-merge-diff contribute?* | excluded by the charter |

**Every one of these is recorded rather than guessed.**
