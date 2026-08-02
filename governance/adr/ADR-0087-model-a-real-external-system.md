---
id: ADR-0087
title: The next milestone is modeling one large external software system
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0080, ADR-0082, ADR-0084, ADR-0085]
---

# ADR-0087 — Model a real external system

## Context

> **Self-modeling now provides diminishing architectural returns.** The next
> objective is not improving the Engineering OS repository. It is proving that
> Engineering OS generalizes.

The largest model that exists is 28 nodes, hand-authored, in a domain invented to
exercise the metamodel.

## Decision

**The next major milestone is to model one large external software system.**

**Not a toy example. Not another Engineering OS repository. A real system.**

### Selection criteria

The system must already have **architecture, source code, documentation,
evolution history, bugs and design decisions.** All six: a system without
recorded decisions cannot exercise `establishes`, and one without evolution
history cannot exercise supersession.

### The success criterion

> **Does Engineering OS reveal relationships that existing documentation
> cannot?**

**Not** *can it represent the system* — representation is not the claim.
Reproducing a system's own documentation as a graph would be a faithful failure.

The evidence sought is a specific kind of finding: an invariant nobody had
written down, a capability with no owner, a decision superseded but still
enforced, a dependency the architecture diagram omits.

### Candidates

| Candidate | Assessment |
|---|---|
| **PostgreSQL** | Decades of evolution, exceptional internals documentation, a public decision record in mailing-list threads. **Design decisions are the weakest axis** — they exist but are not indexed |
| **Kubernetes** | KEPs are an explicit, indexed design-decision corpus — the only candidate whose decisions are already first-class. Architecture, docs, history and bugs are all abundant |
| **GeneXus / GEAI** | Domain access and real stakes. **Least reproducible for an external reader**, which weakens the evidence for anyone who did not build it |
| **Engineering OS self-model** | Cheapest, and explicitly excluded by this decision |

**Recommended: Kubernetes**, because KEPs make *which decision established this?*
answerable from existing material rather than from reconstruction — and that is
the question the metamodel most needs to be tested against.

**The choice is the Project Owner's.** This decision fixes the criteria, not the
system.

### Scope

**One subsystem, modelled deeply, beats the whole system modelled shallowly.**
The claim being tested is about relationships, and relationships need depth.

## Alternatives considered

**A full self-model of Engineering OS first.** Rejected as the milestone, though
it may happen incidentally. The metamodel was designed against this repository,
so success proves almost nothing — it is the definition of a biased test.

**Several systems at once.** Rejected. One system modelled deeply produces
falsifiable findings; three modelled shallowly produce a survey.

**Wait until the metamodel is complete.** Rejected under `ADR-0084` and
`ADR-0085`. Four entities remain and none is blocking; the external system is
what should reveal whether they are needed at all.

## Consequences

### Positive

- **It is the first externally checkable claim the project can make.** Every
  result so far is verifiable only by reading this repository.
- It will expose metamodel gaps that no amount of self-modeling would, and
  `ADR-0085` turns each into a question rather than an entity.
- **It tests the compiler at a scale it has never seen.** Every query scans;
  there is no index; 28 nodes have hidden that completely.

### Negative

- **Modeling a large system by hand is expensive**, and nothing extracts a model
  from source. The first attempt will be mostly manual, which bounds the depth
  achievable and may bias toward what is easy to transcribe.
- **The success criterion is a judgement.** *Reveals what documentation cannot*
  has no threshold, and a motivated author can find something interesting in any
  graph.

### Neutral

- No existing artifact changes.

## Compliance

The milestone is recorded in `governance/roadmap.md` with the chosen system and
subsystem. Findings are recorded as they arise, including the absence of them.
