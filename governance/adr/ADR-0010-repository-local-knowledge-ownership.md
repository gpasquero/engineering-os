---
id: ADR-0010
title: Knowledge is repository-local; multi-repository environments federate
status: accepted
date: 2026-08-02
supersedes: ADR-0006
superseded-by: null
resolves: [ISSUE-0004]
related: [ISSUE-0014, ISSUE-0015, ISSUE-0029, ISSUE-0031, ADR-0009]
---

# ADR-0010 — Knowledge is repository-local; multi-repository environments federate

## Context

`ISSUE-0004` recorded that all three prototypes assume the knowledge model lives
at `model/` inside the target repository, and that none considered
multi-repository systems. It blocked M2, because `model-spec/` must state where
its scaffold is installed.

`ADR-0006` had separated the product layer from the model artifact layer, and in
doing so asserted that this repository "contains `model-spec/` and **never a
live `model/` directory**". That assertion is now known to be wrong.

## Decision

**`model/` is always repository-local. Every repository adopting Engineering OS
owns its own knowledge model.**

Knowledge is owned by the repository that owns the domain.

```text
engineering-os/     model/  -> describes Engineering OS itself
banking-system/     model/  -> describes the banking domain
crm/                model/  -> describes the CRM domain
```

There is **no shared central `model/` directory.** Multi-repository environments
are handled through **federation**, not by sharing one model.

In future, a repository may export a versioned **Knowledge Package** containing
its ontology, graph, glossary, specifications and metadata, so that repositories
can reference one another without sharing their internal source of truth. The
package format and exchange protocol are undefined — `ISSUE-0029`. The design of
`model-spec/` and `MANIFEST.yaml` must not preclude it.

### What this changes in `ADR-0006`

`ADR-0006` is superseded. Two of its three claims survive; one is corrected.

**Survives — the two-layer distinction.** Layer A is the methodology; Layer B is
the knowledge model the methodology produces. They remain different things.

**Survives — `model-spec/`.** This repository specifies and scaffolds the Layer B
tree. `model-spec/` is the specification; `model/` is an instance of it. Both
exist here, and they are not the same artifact.

**Corrected — this repository does have a live `model/`.** Layer A and Layer B
**coexist in every repository that adopts Engineering OS, including this one.**
What distinguishes this repository is not the absence of Layer B; it is that it
*also authors* Layer A.

Engineering OS therefore applies its own methodology to itself. That is not a
side effect of this decision — it is a consequence worth having, and it becomes
a milestone (`ISSUE-0031`).

## Alternatives considered

**Sibling knowledge repository.** Rejected: it separates knowledge from the code
it describes, so the two version independently and drift. Co-versioning the model
with its domain is the property that makes traceability meaningful.

**Central knowledge store for an organization.** Rejected: it makes one team the
owner of every domain's meaning, which contradicts the bounded-context
discipline the methodology exists to enforce. Federation achieves cross-system
questions without central ownership.

**Configurable location with an in-repo default.** Rejected: configurability
would require every skill to resolve a configured root, adding indirection to
every path in the system to serve a case that federation handles better.

## Consequences

### Positive

- Path resolution simplifies: `model/` is always relative to the repository
  root. This narrows `ISSUE-0015` to the skill-relative case.
- Knowledge ownership follows domain ownership, matching bounded-context
  boundaries rather than cutting across them.
- Dogfooding becomes possible, and the strongest available test of the
  methodology is applying it to itself.

### Negative

- A federation subsystem is now implied and does not exist. Knowledge Packages
  are a substantial future body of work (`ISSUE-0029`), and designing for them
  before they are specified risks either over-engineering or building something
  federation cannot use.
- Cross-repository questions are harder than they would be with a central store,
  until federation exists.
- **`model-spec/` and `model/` will be confused**, because they are adjacent,
  similarly named, and one is an instance of the other. This needs explicit
  treatment in the glossary and in `model-spec/`'s own README.

### Neutral

- `ISSUE-0014` (where change records live in the tree) is unaffected and remains
  open.

## Compliance

No skill writes to a knowledge model outside the repository it is operating on.
`model/` is never referenced by an absolute or cross-repository path. Any
cross-repository reference goes through a Knowledge Package once one exists, and
until then is recorded as an unmet need rather than worked around.
