---
id: METAMODEL-Skill
title: Skill
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: operational
artifact-kind: authoritative
established-by: [ADR-0033, ADR-0065]
---

# Skill

**A composable unit of methodology with an explicit contract.**

## What new semantics does this introduce?

**The contract** — a declared relationship between what a unit of work requires
and what it produces.

Nothing else in the metamodel expresses that. `Capability` says a system can do
something; a Skill says *how it is done, what it needs, and what results.*
`Workflow` sequences Skills but holds no methodology of its own (`ADR-0033`),
which is precisely why the methodology needs somewhere to live.

## identity

A qualified name within the repository.

## purpose

To make methodology **composable and substitutable**.

A Skill with an explicit contract can be replaced by another satisfying the same
contract. Without one, methodology is prose: readable, unenforceable, and
impossible to sequence reliably.

> **"Skill" was the first term this project had to split.** The unqualified word
> conflated an Engineering OS methodology unit with a Claude Code skill package.
> This entity is the former. The latter is a packaging format, and a distribution
> concern (`ADR-0017`).

## ownership

Framework skills are owned by Engineering OS. Adopting repositories declare their
own and may substitute their own for a framework skill satisfying the same
contract.

## lifecycle owner

`ArtifactRevisionLifecycle`.

## authoritative representation

A declaration naming the contract — required inputs, produced outputs,
preconditions, and the methodology itself.

**The methodology is prose and authoritative as prose.** A Skill describes how a
judgement is made, and most engineering judgement is not formalisable without
losing what matters. The *contract* is formal; the *method* is not.

## derived representations

- Nodes in the Canonical Knowledge Model.
- A contract-compatibility view: which Skills could substitute for which.
- An orphaned-skill report: Skills no WorkflowStep executes.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| requires | Artifact or Concept | zero or more |
| produces | Artifact | one or more |
| governed-by | ProcessPolicy | zero or more |
| executed-by | WorkflowStep | zero or more |

**`produces` is one-or-more.** A Skill that produces nothing is not a unit of
methodology — it is a description of an attitude. This is the one cardinality in
the metamodel deliberately set to exclude the empty case.

## extension points

An adopting repository declares any skills its methodology needs, and may
substitute for framework skills by contract.

## Debt

**Contract compatibility is undefined.** Substitution is the entire argument for
contracts, and nothing states when two contracts are compatible — whether
identical, or whether a wider input and narrower output suffices. Not needed to
finish B1; needed before substitution is claimed to work.

**The contract has no formal notation.** Same gap as `RelationshipType`
cardinality, and probably the same solution.

**No relationship to `Capability`.** A Skill produces artifacts; a Capability is
something a system can do. Whether skills realise capabilities, or the two are
unrelated, is unaddressed — and the answer decides whether the descriptive and
operational families connect here or not at all.
