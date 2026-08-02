---
id: ADR-0026
title: The lifecycle belongs to a Revision; state machines are named after the entity they govern
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0044]
related: [ADR-0020, ADR-0025, ADR-0027, ISSUE-0046, ISSUE-0048]
---

# ADR-0026 — The lifecycle belongs to a Revision

**This is a core modeling guideline.** It applies to every versioned object in
Engineering OS, not only to the artifacts in this repository.

## Context

`ADR-0020` was explicit that the lifecycle applies to a **revision**, not to an
artifact. `ADR-0025` then named the state machine `ArtifactLifecycle` in its
examples. `ISSUE-0044` recorded the tension and noted that the name would
propagate into every schema, contract and validator downstream.

## Decision

**`ADR-0020` is correct. The lifecycle belongs to a Revision, not to an
Artifact.**

- An **Artifact** is an *identity* that may own many Revisions.
- A **Revision** has exactly one lifecycle state.

**The state machine is named after the entity that owns it:**

```text
ArtifactRevisionLifecycle.Draft
ArtifactRevisionLifecycle.UnderReview
ArtifactRevisionLifecycle.Accepted
ArtifactRevisionLifecycle.Active
ArtifactRevisionLifecycle.Superseded
ArtifactRevisionLifecycle.Archived
```

### The Artifact itself has no lifecycle

It has **metadata**: identifier, ownership, revision history. **Only its
revisions transition through states.**

There is no such thing as "the state of an artifact". The question is
malformed — one asks for the state of a revision, or for which revision is
`Active`.

### Correction to ADR-0025

`ADR-0025`'s decision stands unchanged: every state belongs to exactly one state
machine, and namespaced labels imply no cross-machine equivalence.

Its **examples** are corrected. `ArtifactLifecycle.Active` should read
`ArtifactRevisionLifecycle.Active`, and "Artifact Lifecycle" in the example
inventory should read "Artifact Revision Lifecycle".

## Alternatives considered

**`ArtifactLifecycle`, with states understood to apply to the current revision.**
Rejected: it requires the reader to remember an implicit indirection, and a
reader who forgets it concludes that an artifact is `Active` — which is false
whenever an artifact has a superseded revision, meaning almost always.

**Both machines — an artifact-level one and a revision-level one.** Rejected:
the artifact has no states to transition through. The machine would be empty,
and inventing states for it to justify the symmetry would be modeling backwards.

**`RevisionLifecycle`, without the entity prefix.** Rejected because it breaks
the naming rule this ADR establishes. The governed entity is an *artifact
revision*, and other kinds of revision will exist — a workflow execution
revision, a knowledge package revision. Naming the machine after its entity
keeps them distinguishable by construction.

## Consequences

### Positive

- **The naming rule generalizes.** A state machine's name states what
  transitions, so `WorkflowExecutionLifecycle` and `CompilerExecutionLifecycle`
  are unambiguous without further explanation.
- **A whole class of confusion becomes unaskable.** "What state is this artifact
  in?" is now a malformed question rather than one with a misleading answer.
- The identity/revision split is the right frame for every versioned object,
  which is a larger benefit than settling one name: it will govern Knowledge
  Packages, ontology modules, skills and contracts alike.
- It gives `ISSUE-0007` (what identifies a revision) a clean subject: revisions
  are identified within an artifact identity, not globally.

### Negative

- Verbose names. `ArtifactRevisionLifecycle.UnderReview` is a mouthful, and the
  temptation to abbreviate in prose will be constant.
- **It corrects an example inside an `Active` ADR, and the documentation system
  has no mechanism for that.** Supersession would be wrong — `ADR-0025`'s rule
  is untouched — but "corrected in part" is not an available state.
  `ISSUE-0048`.
- **Core modeling guidelines are now declared across scattered ADRs with no home
  document.** This is the second such declaration after `ADR-0025`.
  `ISSUE-0046`.

### Neutral

- No state value changes. Only the machine's name and the entity it is attached
  to.

## Compliance

No document attributes a lifecycle state to an artifact. Every state machine is
named after the entity it governs. Every reference to the revision lifecycle
uses `ArtifactRevisionLifecycle`.
