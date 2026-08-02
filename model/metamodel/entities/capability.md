---
id: METAMODEL-Capability
title: Capability
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0035]
---

# Capability

**Something a system can do, described in domain terms and externally
visible.** What the system offers, not how it is built.

## identity

A **qualified name within a bounded context**, like a Concept. A capability
named in two contexts is two Capabilities.

## purpose

To name what a system does at the level a stakeholder recognises, independently
of the commands, queries, workflows or code that realise it.

The distinction that matters: **a Capability survives its implementation.**
Rewriting the mechanism that realises a capability does not change the
capability. That is what makes it the stable anchor for impact analysis — a
change is significant when it changes what the system can do, not when it
changes how.

## ownership

Owned by the bounded context that provides it, in the repository that owns that
domain (`ADR-0010`).

## lifecycle owner

`ArtifactRevisionLifecycle`, through the artifact that specifies it.

## authoritative representation

A capability specification stating:

- the actors who invoke it
- preconditions and postconditions
- the invariants it must preserve
- failure modes
- the commands, queries and events through which it is realised

## derived representations

- A node in the Canonical Knowledge Model, linked to the Concepts it is
  expressed in and the artifacts realising it.
- Impact-graph edges: which capabilities a change touches.
- Entries in the Knowledge Explorer.

## relationships

| Relationship | Target | Notes |
|---|---|---|
| provided-by | BoundedContext | exactly one |
| expressed-in | Concept | one or more |
| realised-by | Workflow, Skill, or domain implementation | zero or more |
| preserves | Invariant | zero or more |
| invoked-by | Actor | zero or more |

**`realised-by` is zero-or-more, not one-or-more.** A specified capability with
no realisation is a legitimate state — it is a capability the system is
supposed to have and does not, which is exactly what a reconstruction should be
able to say.

## extension points

Every adopting repository defines its own Capabilities. Engineering OS defines
none for itself yet.

## Debt

**Three referenced entities do not exist**: `BoundedContext`, `Invariant`,
`Actor`. All three are central in the inherited prototypes and absent from the
metamodel inventory. Recorded rather than added, per `ADR-0062`.

This is the second entity in this batch to reference `BoundedContext`. Two
references from two independent specifications is the signal that it belongs in
the next batch.
