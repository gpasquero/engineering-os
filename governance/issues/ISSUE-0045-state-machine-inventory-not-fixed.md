---
id: ISSUE-0045
title: The inventory of state machines is not fixed
type: gap
status: resolved
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0025-every-state-belongs-to-exactly-one-state-machine.md
resolved-by: ADR-0027
---

# ISSUE-0045 — The state machine inventory is not fixed

## Statement

`ADR-0025` establishes that every state belongs to exactly one state machine,
and lists seven as **examples**:

Artifact Lifecycle · ADR Lifecycle · Issue Lifecycle · Milestone Lifecycle ·
Acceptance Lifecycle · Workflow Execution Lifecycle · Compiler Execution
Lifecycle

The list is illustrative, not closed. `shared/vocabularies/` must define
vocabularies grouped by state machine, and cannot do so without knowing which
machines exist.

## Why it matters

Three distinct problems, in increasing order of difficulty.

**Some listed machines do not exist yet.** Workflow Execution arrives with M8;
Compiler Execution depends on the compiler interface. Defining their vocabularies
now would be speculation.

**Some existing vocabularies are unlisted.** `documentation-system.md` defines a
governance-document status (`accepted`, `current`, `proposal`, `superseded`)
that maps to no machine in the list. Either it is an eighth machine, or it
should collapse into one of the seven.

**The rule is stronger than the list.** `ADR-0025` is a modeling rule for the
entire Engineering OS, including target domains. A skill reconstructing a
banking system will discover state machines that no inventory here could
anticipate. So the inventory cannot be closed in the way a vocabulary usually
is — what must be fixed is which machines *this repository* owns, and how a new
one is legitimately introduced.

That third point is the substance: the answer is probably not a list at all, but
a registration rule.

## Open sub-questions

- Which machines are normative for M2, and which are deferred until their
  subject exists?
- Where is a state machine declared — `shared/vocabularies/`, or
  `KNOWLEDGE-MANIFEST.yaml`, which already lists "state machines" among its
  concerns?
- How does a target repository declare its own machines without colliding with
  the framework's?

## Resolution

`ADR-0027`. **Do not maintain a fixed catalog. State machines are registered,
not enumerated.**

The suspicion recorded above was right: the answer is a registration rule, not a
list.

Every state machine registers nine fields — identifier, owner, governed entity,
purpose, vocabulary, transition rules, authoritative specification, related
ontology concepts, related workflows.

The repository contains only the machines that exist today. **The framework
validates registrations rather than enumerating every possible lifecycle**, which
makes the architecture extensible by design. The registry becomes the source of
truth, and documentation, visualizations, ontology navigation and validation are
generated from it rather than from hand-maintained lists.

**The same mechanism serves Engineering OS and every adopting repository** —
mirroring `ADR-0013`, where three manifests serve both.

Opened by this answer: `ISSUE-0047` — where the registry lives, given that
`ADR-0013` already assigns state machines to `KNOWLEDGE-MANIFEST.yaml`.
