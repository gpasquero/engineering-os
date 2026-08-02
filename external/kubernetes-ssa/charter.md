---
id: EXTERNAL-K8S-SSA-CHARTER
title: Validation charter — Kubernetes Server-Side Apply
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: None
artifact-kind: authoritative
established-by: [ADR-0084, ADR-0085, ADR-0087]
---

# Validation charter — Kubernetes Server-Side Apply

**Written before any modeling.** `ADR-0087` requires the boundary to be fixed in
advance so that the result is a test rather than a demonstration.

## Selected subsystem

**Server-Side Apply and managed fields**, in `kubernetes/kubernetes` and
`kubernetes/enhancements`.

Chosen because it satisfies every criterion `ADR-0087` sets:

| Criterion | Evidence |
|---|---|
| explicit design-decision history | KEP-555, plus KEP-2155, KEP-2885, KEP-5958 |
| nontrivial ownership and conflict semantics | field managers, conflicts, `force`, shared ownership |
| spans API behaviour, implementation, tests, compatibility | all four exist and are separately maintained |
| later decisions refined earlier behaviour | three later KEPs touch it |
| impact questions are meaningful | changing ownership semantics affects every controller |
| unfamiliar enough to test generalization | the metamodel was designed against a governance repository, not an API server |

## Authoritative sources

All four required source classes (`ADR-0087`), each verified reachable before
authoring:

| Class | Source | Verified |
|---|---|---|
| **Design decisions** | `kubernetes/enhancements` `keps/sig-api-machinery/555-server-side-apply/README.md` | fetched |
| | `2155-clientgo-apply`, `2885-server-side-unknown-field-validation`, `5958-client-opt-out-managedfields` | directory listing fetched |
| **Documentation** | `kubernetes.io/docs/reference/using-api/server-side-apply/` | fetched |
| **Implementation** | `staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/fieldmanager.go` | HTTP 200, symbols extracted |
| | `.../internal/conflict.go` | fetched |
| | `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/types.go` — `ManagedFieldsEntry` | HTTP 200, definition extracted |
| **Tests** | `test/integration/apiserver/apply/apply_test.go` | HTTP 200, 30 test function names extracted |

Release notes and issue history are **excluded** unless they materially explain
evolution or supersession.

## Scope

- Field management: what a field manager is, what `managedFields` records.
- Conflict semantics: detection, `force`, shared ownership, ownership transfer.
- Field removal semantics.
- Compatibility guarantees stated by KEP-555.
- The subresource and status-field protection path.
- Which tests protect which behaviour.

## Excluded

- The `structured-merge-diff` merge algorithm internals.
- CRD-specific apply paths and `apiextensions-apiserver`.
- `kubectl` client-side behaviour beyond the `--force-conflicts` flag.
- Performance, scalability and storage concerns.
- Every Kubernetes subsystem other than SSA.

**Depth over breadth** (`ADR-0087`). A shallow model of all of Kubernetes proves
nothing.

## Target engineering questions

The seven `ADR-0087` requires, executed through the shared declarative query
engine — no bespoke code:

1. Which design decision introduced this behaviour?
2. Which implementation components realize it?
3. Which tests protect it?
4. Which invariants or compatibility guarantees constrain it?
5. Which later decisions refined or superseded it?
6. What is affected if the behaviour changes?
7. **What information becomes discoverable only after combining multiple
   sources?**

## Success criteria

**Question 7 is the primary proof of value.** The validation succeeds only if its
answer **genuinely requires evidence from more than one source class**.

Reproducing what one document already says — however well modelled — is a
faithful failure.

Also required:

- all four source classes connected;
- every assertion carries provenance to its exact source;
- expected answers reviewed against the sources, classified as **confirmed**,
  **incomplete**, **ambiguous** or **unsupported**;
- **"insufficient evidence" is an available answer.** A confident fabricated
  connection is worse than an incomplete result;
- limitations documented;
- all existing fixtures green, build deterministic;
- **no Kubernetes-specific behaviour in the compiler or query language.**

## Stopping condition

Stop when the seven questions execute and their answers are reviewed — **whether
or not the answers are good.**

A negative result is a result. If question 7 produces nothing that required
combining sources, that is the finding, and the milestone ends with it recorded
rather than with the model extended until something interesting appears.

**Do not extend the model to make an answer better.** Extend it only when a
required question cannot be answered *correctly*.

## Authoring method

**Manual, from fetched sources** (`ADR-0087` direction). No automatic extraction:
it would add a second uncontrolled variable and obscure whether a failure belongs
to ingestion or to semantics.

Every assertion in the model cites the source it came from. Assertions that could
not be verified against a fetched source are marked as such and are **not** given
supporting evidence.
