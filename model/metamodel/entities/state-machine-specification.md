---
id: METAMODEL-StateMachineSpecification
title: StateMachineSpecification
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0025, ADR-0027, ADR-0065]
---

# StateMachineSpecification

**Defines one state machine: its states, its transitions, and what it governs.**

## What new semantics does this introduce?

**Legal transition.** Nothing else in the metamodel can say *this thing may
become that thing, and nothing else.*

`Invariant` states conditions that must hold; `RelationshipType` states which
associations may exist. Neither can express change over time, and every other
relationship in the metamodel is timeless.

It also introduces **state ownership**: a state is not a free-floating label but
a member of exactly one machine's vocabulary.

## identity

An identifier, unique within the repository.

## purpose

To make "state" a **scoped** concept.

> **Every state belongs to exactly one state machine. There is no global concept
> of "state"** (`ADR-0025`).

`Active` in `ArtifactRevisionLifecycle` and `Active` in some future
`SubscriptionLifecycle` are different states that happen to share a word. Names
may coincide **only when explicitly namespaced**:

```text
ArtifactRevisionLifecycle.Active
```

**"State" was the third term this project had to split.** This entity is what
makes the split structural rather than a naming convention.

## Registration, not enumeration

**Engineering OS does not maintain a fixed catalog of state machines**
(`ADR-0027`). It defines a registration model, and **validates registrations
rather than enumerating every possible lifecycle.**

Every registration declares nine things:

| Field | States |
|---|---|
| identifier | the machine's name |
| owner | who owns it |
| governed entity | what it governs |
| purpose | why it exists |
| vocabulary | the states, as a closed enumeration |
| transition rules | which state may follow which |
| authoritative specification | where it is defined |
| related ontology concepts | what it connects to semantically |
| related workflows | which Workflows drive it |

## ownership

Framework machines are owned by Engineering OS. **An adopting repository
registers its own** without modifying the metamodel.

## lifecycle owner

`ArtifactRevisionLifecycle` — which is itself specified by an instance of this
entity. **The metamodel's lifecycle is described by a member of the metamodel**,
and that self-reference is sound: `ADR-0023` permits governance to be
self-hosting provided it is never self-certifying.

## authoritative representation

A registration declaring the nine fields, with the vocabulary expressed as a
`Vocabulary` — a closed enumeration with exactly one definition (`ADR-0008`).

## derived representations

- A state diagram in the Knowledge Explorer.
- The State Machine Registry Projection.
- Transition-validation rules for the compiler.
- Nodes and edges in the Canonical Knowledge Model.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| governs | entity type | one or more |
| declares-states | Vocabulary | exactly one |
| declares-transitions | transition rule | one or more |
| driven-by | Workflow | zero or more |
| scoped-to | BoundedContext | exactly one |

**`governs` is one-or-more, not exactly one.** `ArtifactRevisionLifecycle`
governs revisions of every artifact type in the repository — one machine, many
governed types. This is what makes the machine a specification rather than a
per-entity attachment.

## extension points

An adopting repository registers additional machines and may not weaken the
transition rules of a framework machine.

## Debt

**Transition rules are not an entity and have no notation.** `declares-transitions`
points at "transition rule", which exists nowhere in the inventory — the fourth
instance of a relationship pointing at something undefined
(`FINDINGS.md` #8).

A transition is a from-state, a to-state, and optionally a guard. Under
`ADR-0068`'s test it is **extrinsic** — the same state is reachable from
different states in different machines — which means it should be a reified
association, not a property. **Recorded, not built**: B1 does not require it.

**No machine has been registered.** `ArtifactRevisionLifecycle` is used
throughout the repository, is referenced by fourteen entity specifications, and
has never been registered under `ADR-0027`'s model. The registry it would be
registered in is `KNOWLEDGE-MANIFEST.yaml`, which does not exist.

**`Vocabulary` is unspecified**, and `declares-states` depends on it.
