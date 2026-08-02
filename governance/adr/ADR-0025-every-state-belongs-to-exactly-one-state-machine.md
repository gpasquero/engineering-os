---
id: ADR-0025
title: Every state belongs to exactly one state machine; state names are namespaced
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0043]
related: [ADR-0002, ADR-0012, ADR-0020, ISSUE-0044, ISSUE-0045]
---

# ADR-0025 — Every state belongs to exactly one state machine

**This is a fundamental modeling rule for the entire Engineering OS.** It
governs `shared/vocabularies/`, and it governs how skills model state in target
domains.

## Context

The project has caught the same class of defect three times:

| Collision | Caught in |
|---|---|
| "skill" — methodology unit versus vendor packaging format | `ISSUE-0012`, M1 |
| "authoritative" — artifact kind versus lifecycle state | `ISSUE-0038` |
| Four document status vocabularies overlapping the revision lifecycle | `ISSUE-0043` |

Each was patched individually. `ISSUE-0043` identified the shared root cause:
the project was mixing several independent state vocabularies as though they
described one thing.

The live symptom was stark — nineteen ADRs marked `status: accepted`, while
`ADR-0020` states that exactly one revision of an artifact is `Active` at a time.

## Decision

**Every state belongs to exactly one state machine.**

**There is no global concept of "state."** There are multiple independent state
machines, each owning its own vocabulary.

Examples of distinct state machines:

- Artifact Lifecycle
- ADR Lifecycle
- Issue Lifecycle
- Milestone Lifecycle
- Acceptance Lifecycle
- Workflow Execution Lifecycle
- Compiler Execution Lifecycle

**State names may coincide only if they are explicitly namespaced:**

```text
ArtifactLifecycle.Active
IssueLifecycle.Open
ADRLifecycle.Accepted
AcceptanceLifecycle.Recorded
CompilerExecution.Completed
```

> **The same textual label must never imply semantic equivalence across state
> machines.**

`ADRLifecycle.Accepted` and `ArtifactLifecycle.Accepted` are different states.
That they share a label is a coincidence of English, not a relationship.

### Consequence for `shared/vocabularies/`

Vocabularies are defined **grouped by state machine**, not as a single global
list of states.

### Where the namespace may be implied

In document front matter the state machine is determined by document type: an
ADR's `status` is an `ADRLifecycle` state, an issue's is `IssueLifecycle`.
Explicit qualification is required wherever the machine is not fixed by
context — in prose, in vocabularies, in contracts and in any cross-machine
comparison.

> This last clause is a derivation, not something stated in the answer to
> `ISSUE-0043`. It exists so that front matter does not become
> `status: ADRLifecycle.Accepted`. If fully explicit namespacing was intended
> everywhere, this clause needs correcting.

## Alternatives considered

**Adopt one lifecycle universally**, replacing the per-type vocabularies.
Rejected: it forces genuinely different processes into one vocabulary. An
issue's `Open`/`Resolved` describes whether a *question* is answered; a
revision's `Draft`/`Active` describes whether a *revision governs*. Collapsing
them would lose that, and would have to invent a shared meaning that does not
exist.

**Map between vocabularies** rather than separating them. Rejected: a mapping
asserts equivalences that are not real, and it leaves two names for what the
mapping claims is one concept — the failure `ISSUE-0038` was opened to prevent.

**Keep patching collisions individually.** Rejected explicitly: three
occurrences is a pattern, and the fourth would arrive in `shared/vocabularies/`
where it would be inherited by every schema and validator downstream.

## Consequences

### Positive

- **The root cause is addressed, not the third symptom.** Future collisions
  become impossible by construction rather than by vigilance.
- The nineteen-ADRs contradiction dissolves without renaming anything:
  `ADRLifecycle.Accepted` and `ArtifactLifecycle.Active` were never the same
  state.
- The four "overlapping" vocabularies in `documentation-system.md` are
  retroactively legitimate — they were always separate state machines, just
  never named as such.
- `shared/vocabularies/` gains a clear structure before it is written.
- **The rule propagates into the methodology itself.** The inherited prototypes
  require modeling lifecycles and state machines in target domains; this rule
  now governs how those are named, which is a larger benefit than fixing this
  repository's own vocabulary.

### Negative

- **Verbosity.** Fully qualified state names are heavier to read and write, and
  the implied-namespace clause above is a compromise that will itself need
  policing.
- **The inventory of state machines is not fixed.** The list above is examples,
  not a closed set, and two named machines — Workflow Execution and Compiler
  Execution — do not exist yet. `ISSUE-0045`.
- **"Artifact Lifecycle" conflicts with `ADR-0020`**, which was explicit that the
  lifecycle applies to a *revision*, not an artifact. `ISSUE-0044`.
- Every existing bare state reference in the corpus must be checked for
  ambiguity, and prose that reads naturally today may need qualifying.

### Neutral

- No existing state value changes. Only the framing, the grouping and the naming
  discipline change.

## Compliance

No document defines a state without naming its state machine. No vocabulary file
contains states from more than one machine. No comparison or inference treats
two identically-labelled states from different machines as equivalent.
