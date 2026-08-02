---
id: EXTERNAL-K8S-SSA-FINDINGS
title: Findings — Kubernetes Server-Side Apply validation
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0084, ADR-0087, ADR-0089, ADR-0090]
---

# Findings — Kubernetes Server-Side Apply

**41 nodes, 75 edges**, four source classes, seven questions executed through the
shared declarative query engine.

```sh
python3 tools/compile.py external/kubernetes-ssa
python3 tools/ask.py external/kubernetes-ssa Q-evidence Invariant.TimestampNotUpdatedOnTakeover
open external/kubernetes-ssa/build/explorer.html
```

## Findings, classified

`ADR-0090`. **Kind describes what was found; support describes how well it is
evidenced.** A finding may not claim a kind stronger than its support permits.

| # | Finding | Kind | Rank | Support |
|---|---|---|---|---|
| 1 | A `managedFields` timestamp is not the time that entry last changed | **documentation-gap** | 5 | confirmed |
| 2 | …and that timestamp is rendered in the conflict message a user reads while reasoning about ownership | **observability-gap** | 6 | confirmed |
| 3 | `Invariant.ApplyRequiresFieldManager` is asserted by a test name and stated by no fetched document | **documentation-gap** | 5 | confirmed |
| 4 | Nothing in the model constrains `Concept.Conflict`; `Q-assumptions` on `conflict.go` returns empty | **traceability-gap** | 4 | confirmed |
| 5 | Whether KEP-2885 and KEP-5958 refine or supersede parts of KEP-555 | **ambiguous-evidence** | 7 | ambiguous |
| 6 | Who owns fields set by defaulting or by controllers | **missing-evidence** | 8 | unsupported |

**No confirmed contradiction, no behavioral or architectural inconsistency** —
ranks 1 to 3 are empty. The strongest thing this validation found is a
documentation gap.

**That is the honest headline.** A system that reported finding 1 without saying
it ranks fifth of eight would be overstating itself in exactly the way `ADR-0090`
exists to prevent.

### Finding 4 was produced by a question, not by reading

`Q-assumptions` on `Artifact.ConflictGo` returns **empty**: no invariant in the
model constrains `Concept.Conflict`. The same query on `Artifact.MetaV1Types`
returns two.

The asymmetry is the finding. Conflict detection is the behaviour most likely to
surprise a user, and it is the one part of the modelled subsystem with no
recorded constraint. **Nobody noticed while authoring; the query found it.**

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

## Engineering questions a maintainer would actually ask

`ADR-0089`. Three of the six the reviewer named were already answerable; three
required work, and one required a change to the query language.

| Question | Query | Result on this model |
|---|---|---|
| Why was this behaviour introduced? | `Q-rationale` | KEP-555 |
| What assumptions does this implementation depend on? | `Q-assumptions` | **new** — and it found finding 4 |
| What would break if we changed this ownership rule? | `Q-impact` | 9 nodes |
| Which compatibility guarantees constrain this change? | `Q-constraints` | 3 invariants |
| Which decisions became obsolete but are still reflected in code? | `Q-obsolete-decisions` | **new** — **empty, and true**: no KEP in this model is superseded |
| Which implementation artifacts no longer match their design rationale? | `Q-stale-implementation` | **new** — empty, same reason |

**Two of the new queries return nothing on Kubernetes, and that is a correct
answer, not a failure.** They are exercised by `tests/projects/has-path`, which
mentions no domain.

### `has-path` — the second compiler gap

*Which implementation artifacts no longer match their original design
rationale?* **could not be expressed.** It filters a row on a property three hops
away — the supersession of the decision that established the concept the artifact
represents — while still returning the row. `has-edge` is single-hop and the
pipeline cannot return to an earlier stage.

The correction is one operator, `has-path`, taking an ordered sequence of edge
specs. Domain-neutral, mirrored in both engines, covered by a fixture that
mentions no domain.

**Two external-validation gaps, two domain-neutral corrections.** Neither was
about Kubernetes: the first was the authoring format, the second the query
language.

## Recommendations

`ADR-0091`. **Questions produce knowledge; recommendations produce guidance.**

```sh
python3 tools/advise.py external/kubernetes-ssa R-change-implementation Artifact.ConflictGo
python3 tools/advise.py external/kubernetes-ssa R-audit-model
```

`R-audit-model` runs the model's own honesty checks against Kubernetes and
returns **two items in five steps**: `BackwardCompatible` and
`TimestampNotUpdatedOnTakeover` have no recorded enforcement point.

The second is worth pausing on. **The finding this validation is proudest of is
also an invariant nothing enforces** — which is exactly what a maintainer should
know about it.

Every line of every recommendation names the query that produced it. Nothing is
asserted that a query did not return.

## What a second iteration should change

1. **Model individual test functions.** The single highest-value change; it makes
   Q3 precise and costs 30 nodes.
2. **Read KEP-2885 and KEP-5958 in full**, so refinement edges mean refinement.
3. **Look for a contradiction, not a join.** Ranks 1–3 of the taxonomy are empty.
   Two sources that disagree would be materially stronger than two that combine,
   and aiming at rank 1 is now a statable target rather than a vague ambition.
