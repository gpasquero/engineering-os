---
id: MODEL-PLANS
title: Engineering Plans
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
artifact-kind: authoritative
established-by: [ADR-0091, ADR-0092, ADR-0093, ADR-0094]
---

# Engineering Plans

**A recommendation says what to look at. A plan says what to do, in what order,
and how to know it worked.**

> **Every action is explainable through semantic queries. A plan states nothing a
> query did not return, and no language model participates in producing one**
> (`ADR-0092`, `ADR-0094`).

## Structure

| Part | Declared as |
|---|---|
| objective | a template naming the subject |
| assumptions | queries whose results are stated as preconditions |
| reasoning chain | produced — every query run, with subject, result and `because` |
| ordered actions | phases, each drawing actions from a recommendation |
| dependencies | `requires` between phases |
| required reviews | a query plus the checkpoint it gates |
| expected evidence | what should exist afterwards that does not now |
| completion conditions | statements, each backed by a query that must be empty or non-empty |
| **deferred decisions** | **stated explicitly** (`ADR-0093`) |

## The plans

```yaml
plans:
  - id: P-change-implementation
    objective: Change {subject} without breaking what depends on it
    applies-to: [Artifact]
    rationale: >
      An implementation is constrained by things stated elsewhere by someone
      else. The plan front-loads the reading an engineer would otherwise skip,
      and orders the work so that the step that can stop you comes first.
    assumptions:
      - query: Q-assumptions
        statement: These invariants must still hold after the change.
      - query: Q-evidence
        statement: These sources are what this artifact's claims rest on.
    phases:
      - id: understand
        goal: Know what constrains this before touching it
        recommendation: R-change-implementation
        actions: [review, investigate]
      - id: change
        goal: Make the change and carry its consequences
        recommendation: R-change-implementation
        actions: [inspect]
        requires: [understand]
      - id: verify
        goal: Establish that nothing it protected has regressed
        recommendation: R-change-implementation
        actions: [verify]
        requires: [change]
    reviews:
      - at: understand
        query: Q-assumptions
        because: an unlisted invariant is one nobody will check
      - at: verify
        query: Q-tests
        because: a change with no test touching it is unverified, not safe
    expected-evidence:
      - query: Q-tests
        statement: A test exercising the changed behaviour should exist afterwards.
    completion:
      - query: Q-assumptions
        expect: non-empty
        statement: The constraints on this artifact are known and were reviewed.
      - query: Q-tests
        expect: non-empty
        statement: At least one test validates this artifact.
    defers:
      - Whether the change is source-compatible for existing callers.
      - Whether a new invariant should be recorded as a result of the change.
      - The implementation itself.

  - id: P-change-capability
    objective: Change what {subject} does, and carry it through every realisation
    applies-to: [Capability]
    rationale: >
      Added because a real run could not express the workflow it was given
      (ADR-0102). "I need to add OAuth" is a change to a capability, and neither
      existing plan applied to one. A capability is realised by artifacts and
      bounded by invariants, so changing it means every realisation plus
      everything that constrains it — and the constraints come first, because
      they are what a new authentication path is most likely to violate.
    assumptions:
      - query: Q-constraints
        statement: These invariants bound what this capability may do.
      - query: Q-rationale
        statement: This decision established the capability; check it still stands.
    phases:
      - id: understand
        goal: Establish what bounds this capability before extending it
        recommendation: R-change-concept
        actions: [review, validate]
      - id: change
        goal: Carry the change through every realisation
        recommendation: R-change-concept
        actions: [update, inspect]
        requires: [understand]
      - id: verify
        goal: Confirm every bound still holds
        recommendation: R-change-concept
        actions: [verify]
        requires: [change]
    reviews:
      - at: understand
        query: Q-constraints
        because: >
          A new path through a capability is most likely to violate a constraint
          nobody re-read.
      - at: verify
        query: Q-tests
        because: an unchanged test suite after a capability change is a warning
    expected-evidence:
      - query: Q-tests
        statement: A test exercising the new behaviour should exist afterwards.
    completion:
      - query: Q-constraints
        expect: non-empty
        statement: The invariants bounding this capability are known and were reviewed.
      - query: Q-specifications
        expect: non-empty
        statement: The artifacts realising this capability are identified.
    defers:
      - Whether the new behaviour belongs in this capability or a new one.
      - Whether an existing invariant must be weakened, and whether that is acceptable.
      - Which realisation changes first.
      - The implementation itself.

  - id: P-change-concept
    objective: Change the meaning of {subject} and carry the consequences
    applies-to: [Concept]
    rationale: >
      Changing a concept changes the meaning everything downstream was built
      against. The decision that established it comes first, because it is the
      only step whose answer can be "do not do this".
    assumptions:
      - query: Q-rationale
        statement: This decision established the current meaning; check it still stands.
      - query: Q-constraints
        statement: These guarantees must survive the change.
    phases:
      - id: understand
        goal: Establish why the current meaning exists
        recommendation: R-change-concept
        actions: [review, validate]
      - id: change
        goal: Change the meaning and everything stated in terms of it
        recommendation: R-change-concept
        actions: [update, inspect]
        requires: [understand]
      - id: verify
        goal: Confirm the guarantees survived
        recommendation: R-change-concept
        actions: [verify]
        requires: [change]
    reviews:
      - at: understand
        query: Q-rationale
        because: a superseded rationale means the change may already be decided
    expected-evidence:
      - query: Q-specifications
        statement: Every specification representing this concept should be updated.
    completion:
      - query: Q-constraints
        expect: non-empty
        statement: The guarantees constraining this concept are known.
      - query: Q-specifications
        expect: non-empty
        statement: The specifications to update are identified.
    defers:
      - Whether the new meaning is compatible with the old one.
      - Whether a new ADR is required, and what it should decide.
      - Whether downstream consumers outside this model are affected.
```

## Debt

**Phase order and `requires` are judgements encoded as data with nothing to
check them.** Declaring *understand before change* asserts an engineering
practice no evidence in this repository supports.

**Completion conditions are checkable in principle and unchecked in practice.**
Nothing re-runs a plan afterwards to see whether it completed.

**`defers` is authored, not derived.** It is a list someone wrote of what the
plan cannot decide — which is honest and is exactly as complete as the author was
careful. Nothing detects a decision that was neither derived nor deferred.

**A plan inherits every weakness of its queries**, and presents them with more
authority than the query deserves.
