---
id: EXTERNAL-K8S-SSA-FINDINGS
title: Findings — Kubernetes Server-Side Apply validation
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0084, ADR-0087]
---

# Findings — Kubernetes Server-Side Apply

**41 nodes, 75 edges**, four source classes, seven questions executed through the
shared declarative query engine.

```sh
python3 tools/compile.py external/kubernetes-ssa
python3 tools/ask.py external/kubernetes-ssa Q-evidence Invariant.TimestampNotUpdatedOnTakeover
open external/kubernetes-ssa/build/explorer.html
```

## The proof-of-value result

> **A `managedFields` entry's `time` is not the time that entry last changed.**

The API type comment says a timestamp does **not** update when a field is removed
because another manager took it over. The documentation says `force` **removes
the field from all other managers' entries**. Neither mentions the other.

Combined: a forced apply silently reduces another manager's field set while
leaving its timestamp untouched — and `conflict.go`'s `printManager` renders that
timestamp in the conflict message a user reads while reasoning about ownership.

**No fetched document contains the conclusion.** Full derivation and
classification in `ground-truth.md` Q7.

**Honest strength:** a documentation-and-observability finding, not a correctness
bug. The weakest form of the claim that still counts. A contradiction between
sources would have been stronger; this validation did not find one, and the model
is too small to conclude none exists.

## What the milestone proved about Engineering OS

**It answered questions without knowing anything about Kubernetes.** No
Kubernetes-specific entity, predicate, operator or compiler behaviour was added.
The domain arrived entirely as Layer B data: KEPs became `ADR`, docs and source
and tests became `Artifact`, guarantees became `Invariant`.

**The metamodel generalized.** It was designed against a governance repository
and mapped an API-machinery subsystem with **one** correction, which was
domain-neutral.

**It declined to answer.** `KEP.5958` carries `support: incomplete` because only
the directory listing was fetched. Q5 is classified **ambiguous** rather than
asserting supersession. `Q-unsupported` returns empty — every invariant is cited.

## The one compiler gap, and its correction

**Failed requirement:** *every modeled assertion must preserve provenance to its
exact source.* No authoring field could carry a source URI or locator.

| Step | Result |
|---|---|
| Where the gap belongs | **authoring representation** and **CKM** |
| Smallest general correction | an optional `attributes` mapping of scalar key/values, carried verbatim into the model and given **no meaning** by the compiler |
| Regression fixture | `tests/projects/node-attributes` and `tests/projects/bad-attributes` — **neither mentions Kubernetes** |
| Fixtures rerun | 16 projects, all green |

**Nothing Kubernetes-specific entered the compiler or the query language.**

Three queries were added — `Q-constraints`, `Q-evidence`, `Q-unsupported` — all
domain-neutral, all declarative, all executed by both engines.

## Limitations

| Limitation | Consequence |
|---|---|
| **Test granularity is the file** | `Q-tests` names a file containing 30 test functions, not the test that protects a behaviour. The sharpest limitation found |
| **KEP granularity is the document** | KEP-555 establishes six things, so `Q-rationale` is less discriminating than a finer decision record would allow |
| **Only KEP-555 was read in full** | Q5's refinement edges mean *concerns the same subsystem*, not *verified refinement* |
| **`structured-merge-diff` excluded** | Q2's answer is right and smaller than the system |
| **Hop distance is not severity** | Q6 returns 9 nodes at 1–4 hops and nothing ranks them |
| **41 nodes** | Large enough to join four sources; far too small to test traversal limits, which never fired |

## Path selection — the predicted question did not arise

`ADR-0088` retains the best deterministic path to each result and notes this is
not the same as preserving all valid explanations.

**In this model it did not matter.** Every multi-hop result reached its target by
one materially distinct evidence path. `Invariant.TimestampNotUpdatedOnTakeover`
has two *evidence* edges but they are two 1-hop results, not two paths to one
node.

**Recorded rather than acted on**, as directed. The concrete question that would
force the decision has not yet occurred.

## What a second iteration should change

1. **Model individual test functions.** The single highest-value change; it makes
   Q3 precise and costs 30 nodes.
2. **Read KEP-2885 and KEP-5958 in full**, so refinement edges mean refinement.
3. **Look for a contradiction, not a join.** Two sources that disagree would be a
   materially stronger result than two that combine.
