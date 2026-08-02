---
id: METAMODEL-Actor
title: Actor
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0035, ADR-0065]
---

# Actor

**A role that interacts with a system's Capabilities.**

## identity

A qualified name within a BoundedContext.

## purpose

To answer **for whom** a Capability exists.

A Capability is externally visible by definition — visible *to someone*. Without
Actors, that someone is implicit, and a capability inventory becomes a list of
functions with no account of who needs them.

Actors also make a specific omission visible: **a Capability with no Actor is
either unused or has an undocumented consumer.** Both are findings.

## Actor is a role, not a party

An Actor is *Reviewer*, not *gpasquero*. It is a role, and:

- one person or system may fill several roles;
- one role may be filled by several parties;
- **a role may be filled by a human, another system, or an agent.**

The third case is not a special case in this framework. Engineering OS is
designed for AI-assisted engineering, and an agent invoking a capability is an
Actor by exactly the same definition as a person doing so.

**Actors are not an authorization model.** They describe who interacts, not who
is permitted to. A permission is an `Invariant` about an Actor and a Capability.

## ownership

Owned by the BoundedContext in which the role is meaningful.

## lifecycle owner

`ArtifactRevisionLifecycle`.

## authoritative representation

A declaration in the semantic model: the role name, its context, and what
distinguishes it from adjacent roles.

## derived representations

- Nodes in the Canonical Knowledge Model.
- A capability-by-actor view in the Knowledge Explorer.
- An orphaned-capability report: capabilities no Actor uses.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| uses | Capability | zero or more |
| scoped-to | BoundedContext | exactly one |
| specialises | Actor | zero or one |

**`specialises` is a single parent.** Multiple inheritance of roles is
expressible in OWL and almost always a modelling error at this level — a role
that is genuinely two roles is two Actors.

## extension points

An adopting repository declares the roles its domain has. The framework declares
none, though its own governance clearly has several — Project Owner, Reviewer,
Author.

## Debt

**The framework's governance roles are undeclared.** `ADR-0023` distinguishes
author from reviewer and `ACCEPT-0001` names a Project Owner, all in prose. None
is declared as an Actor. This is the same gap `BoundedContext` records, and both
close when the framework models itself in B3.

**The `specialises` single-parent restriction is asserted, not derived.** It is a
judgement about modelling discipline, and the OWL skeleton may show it to be
unnecessary. Recorded so that the decision is visible when it is revisited.
