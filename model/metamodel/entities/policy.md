---
id: METAMODEL-Policy
title: Policy
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: operational
artifact-kind: authoritative
established-by: [ADR-0029, ADR-0030, ADR-0056, ADR-0065]
---

# Policy

**A normative rule, motivated by a Principle, that governs something.**

## What new semantics does this introduce?

**Normativity, and its motivation.** Nothing else in the metamodel can say *this
must be so, because of that*.

`Invariant` states what must be true **of the modelled world**. Policy states
what must be true **of the engineering performed on it** — and, unlike an
Invariant, it must name the Principle it derives from.

That link is the new relationship: `motivated-by`. It is what makes
`Principle → Policy → Engineering Process → Artifact` (`ADR-0056`) a chain
rather than four unrelated things.

## identity

A qualified name within the repository, plus its **kind**.

## Three kinds

`ADR-0030` splits Policy by what it governs. The split is not cosmetic: the three
kinds have different targets and different enforcement.

| Kind | Governs | Example |
|---|---|---|
| **GovernancePolicy** | how decisions are made and recorded | acceptance requires a reviewer who is not the author |
| **ModelingPolicy** | how the knowledge model may be shaped | an entity must introduce a new semantic relationship (`ADR-0067`) |
| **ProcessPolicy** | how engineering work is performed | a Workflow sequences Skills and holds no methodology |

**`Policy` unqualified was the fourth term this project had to split.** The
three kinds are the canonical names; the bare word is informal (`ADR-0057`).

## purpose

To make rules **traceable to reasons**.

A rule with no stated motivation cannot be evaluated when circumstances change —
it can only be obeyed or violated. A Policy that names its Principle can be asked
the one useful question: *does the reason still hold?*

## ownership

Framework policies are owned by Engineering OS. An adopting repository declares
its own, and may not weaken a framework policy — only add to it.

## lifecycle owner

`ArtifactRevisionLifecycle`.

## authoritative representation

A statement in the semantic model: the rule, its kind, the Principle motivating
it, and what it governs.

**A Policy is authored, never derived.** Principles are extracted by the compiler
(`ADR-0058`); Policies are written by people who decide that a Principle should
constrain something.

## derived representations

- Nodes in the Canonical Knowledge Model, linked to Principle and to targets.
- An unmotivated-policy report: policies naming no Principle.
- Policy display in the Knowledge Explorer, grouped by Principle.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| motivated-by | Principle | one or more |
| governs | Workflow, EngineeringGate, Artifact or the model | one or more |
| of-kind | GovernancePolicy, ModelingPolicy or ProcessPolicy | exactly one |
| enforced-by | ValidationRule | zero or more |

**`enforced-by` is zero-or-more**, and the zero case is the interesting one. A
Policy no ValidationRule enforces is a rule kept by discipline — the same shape
as `Invariant.enforced-at`, and the same finding when it is empty.

## extension points

An adopting repository declares its own policies of any of the three kinds. The
kinds themselves are closed: adding a fourth is a metamodel change.

## Debt

**`ADR-0067` is currently a decision doing a ModelingPolicy's job.** It says so
itself, and says it will relocate once Policy is implemented. This specification
is what makes that relocation possible; performing it is B3 work.

**Nothing prevents a Policy contradicting another.** Two policies motivated by
different Principles can govern the same target incompatibly. Detecting that is
not mechanical, and no Gate currently reviews policy introduction.

**Precedence is unstated.** If a repository policy and a framework policy both
apply, which wins is undefined. "May not weaken, only add" is written above as
the intent, and nothing enforces or even formalises it.
