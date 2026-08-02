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

  - id: P-review-unsupported
    objective: Decide whether {subject} should be retracted or re-evidenced
    applies-to: [Invariant, Concept, Capability, Artifact]
    rationale: >
      A maintained assertion that a fresh reacquisition no longer supports has
      three possible causes and only one of them justifies retraction: the
      evidence moved, the extractor changed, or the system genuinely changed.
      **Retraction is the only plan that can destroy curated knowledge**, so it
      begins by looking for the evidence rather than by removing the claim.
    assumptions:
      - query: Q-evidence
        statement: This is the evidence the assertion currently cites.
      - query: Q-rationale
        statement: This is the decision that established it, if any.
    phases:
      - id: locate
        goal: Find the evidence, or establish that it is gone
        recommendation: R-change-implementation
        actions: [investigate]
      - id: assess
        goal: Determine which of the three causes applies
        recommendation: R-change-implementation
        actions: [review]
        requires: [locate]
      - id: decide
        goal: Retract, re-evidence, or leave standing
        recommendation: R-audit-model
        actions: [investigate]
        requires: [assess]
    reviews:
      - at: decide
        query: Q-evidence
        because: >
          Retracting an assertion whose evidence merely moved destroys curated
          knowledge, and nothing restores it.
    expected-evidence:
      - query: Q-evidence
        statement: Either new provenance, or a recorded reason for retraction.
    completion:
      - query: Q-evidence
        expect: non-empty
        statement: The assertion's evidence situation is known.
    defers:
      - Whether the system changed or the extractor did.
      - Whether retraction or re-evidencing is correct.
      - "**The retraction itself, which is a governed proposal and never automatic.**"

  - id: P-verify-capability
    objective: Establish whether {subject} is actually implemented
    applies-to: [Capability]
    rationale: >
      A modelled capability with no implementation evidence is either a
      description of something that was never built, or a gap in extraction. The
      difference matters and neither is visible from the model alone.
    assumptions:
      - query: Q-constraints
        statement: These invariants bound the capability, if it exists.
    phases:
      - id: search
        goal: Look for an implementation the model does not record
        recommendation: R-change-concept
        actions: [review]
      - id: conclude
        goal: Record the implementation, or record its absence
        recommendation: R-audit-model
        actions: [investigate]
        requires: [search]
    reviews:
      - at: conclude
        query: Q-constraints
        because: a capability that constrains nothing may not be a capability
    expected-evidence:
      - query: Q-tests
        statement: An implementing or validating artifact should be linked afterwards.
    completion:
      - query: Q-constraints
        expect: non-empty
        statement: What bounds this capability is known.
    defers:
      - Whether the capability was never built or merely never modelled.
      - Whether an unimplemented capability should be retracted or kept as intent.

  - id: P-establish-enforcement
    objective: Find where {subject} is enforced, or record that nothing enforces it
    applies-to: [Invariant]
    rationale: >
      An invariant with no enforcement point is a finding, not an error
      (`invariant.md`). This plan does not assume enforcement exists — it
      establishes which of the two states holds, because an unenforced invariant
      that everyone believes is enforced is the more dangerous case.
    assumptions:
      - query: Q-evidence
        statement: This is what the invariant rests on.
    phases:
      - id: search
        goal: Look for a test, guard or check that enforces it
        recommendation: R-change-implementation
        actions: [investigate]
      - id: record
        goal: Link the enforcement point, or record its absence explicitly
        recommendation: R-audit-model
        actions: [investigate]
        requires: [search]
    reviews:
      - at: record
        query: Q-evidence
        because: >
          Recording an enforcement point that does not enforce is worse than
          recording none.
    expected-evidence:
      - query: Q-evidence
        statement: Either an enforcement link, or a recorded absence.
    completion:
      - query: Q-evidence
        expect: non-empty
        statement: The invariant's evidence is known.
    defers:
      - Whether the absence of enforcement is acceptable.
      - Whether enforcement should be added, and where.

  - id: P-resolve-conflict
    objective: Resolve two readings of the same evidence about {subject}
    applies-to: [Invariant, Concept, Capability, Artifact, ADR]
    rationale: >
      A conflict is the strongest finding kind (`ADR-0090`) and the only one a
      rule may never settle. This plan gathers both readings and their evidence
      and stops — the decision is a human's.
    assumptions:
      - query: Q-evidence
        statement: This is the evidence both readings rest on.
      - query: Q-rationale
        statement: This decision established the maintained reading, if any.
    phases:
      - id: gather
        goal: Assemble both readings with their evidence
        recommendation: R-change-concept
        actions: [review, validate]
    reviews:
      - at: gather
        query: Q-rationale
        because: >
          A conflict with a superseded decision on one side is not a conflict.
    expected-evidence:
      - query: Q-evidence
        statement: Both readings should be traceable to their sources.
    completion:
      - query: Q-evidence
        expect: non-empty
        statement: Both readings are evidenced.
    defers:
      - "**Which reading is correct — this plan cannot and must not decide.**"
      - Whether both are wrong.
      - Whether the conflict indicates a real inconsistency in the system.

  - id: P-discover
    objective: Build a Candidate Engineering Model of {subject}
    applies-to: [Artifact]
    rationale: >
      The first engineering workflow Engineering OS executes on an unknown
      repository (ADR-0105). It produces PROPOSALS, never authoritative
      knowledge: the review gate every plan already terminates in is what makes
      a candidate model authoritative, and it is the same gate.
    assumptions:
      - query: Q-provenance
        statement: This is the repository being onboarded, and what is known of it.
    phases:
      - id: extract
        goal: Derive structure mechanically, interpreting nothing
        recommendation: R-discover
        actions: [extract]
      - id: interpret
        goal: Propose engineering knowledge, each proposal citing its source
        recommendation: R-discover
        actions: [interpret]
        requires: [extract]
      - id: assess
        goal: Report what the candidate model does not contain
        recommendation: R-discover
        actions: [identify-gaps]
        requires: [interpret]
    reviews:
      - at: interpret
        query: Q-evidence
        because: >
          A proposal without provenance is a guess, and a candidate model is
          mostly proposals.
    expected-evidence:
      - query: Q-unsupported
        statement: Every proposed assertion should carry provenance afterwards.
    completion:
      - query: Q-provenance
        expect: non-empty
        statement: The repository under discovery is identified.
    defers:
      - Which proposals are accepted — that is the review gate, not the plan.
      - Whether a proposed concept is the right abstraction for this domain.
      - Everything the repository contains that discovery did not reach.

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
