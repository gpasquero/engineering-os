---
id: METAMODEL-Evidence
title: Evidence
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: descriptive
artifact-kind: authoritative
established-by: [ADR-0060, ADR-0061, ADR-0065]
related-issues: [ISSUE-0018, ISSUE-0073]
---

# Evidence

**A reference to an observable fact, cited in support of an assertion.**

## identity

The pair of **what is referenced** and **the assertion citing it**.

The same source supports many assertions; each citation is distinct Evidence.
Evidence is a *citation*, not a *source* — a distinction worth holding, because
conflating them is how a reference count becomes mistaken for corroboration.

## purpose

To make assertions **checkable rather than merely stated**.

Every Interpretive assertion in this framework — a Concept's meaning, an
Invariant's existence, a Capability's realisation — is a judgement. `ADR-0061`
is explicit that the compiler cannot make such judgements. What it *can* do is
carry the citation alongside the claim, so a reader can go and look.

> **Evidence does not make an assertion true. It makes it falsifiable.**

## kinds

The inherited prototypes ranked evidence by directness, and the ranking is worth
preserving: **observed runtime behaviour outranks source code, which outranks
documentation, which outranks inference.**

| Kind | Example |
|---|---|
| Runtime observation | a trace, a log, a measured response |
| Source reference | file, symbol, line range |
| Artifact reference | a document, at a specific revision |
| External reference | a standard, ticket, or third-party document |
| Inference | derived from other evidence, explicitly marked |

**Inference is the weakest kind and must be marked as such.** Evidence that does
not distinguish observation from inference is how a chain of guesses acquires the
appearance of a chain of facts.

## ownership

Owned by the assertion that cites it. Evidence has no standing on its own; a
citation supporting nothing is not Evidence.

## lifecycle owner

`ArtifactRevisionLifecycle`, through the assertion citing it.

## authoritative representation

A citation in the semantic model: the kind, the reference, and — where the
referenced thing is versioned — **the revision at which it was observed**.

The revision matters. A source reference without one is a claim about a file that
may no longer say what was claimed, and `ADR-0064` gives the identity model that
makes pinning possible.

## derived representations

- Edges in the Canonical Knowledge Model, from assertion to evidence.
- A staleness report: citations whose referenced revision is no longer current.
- Provenance display in the Knowledge Explorer.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| supports | any assertion | one or more |
| references | Artifact, source location or external identifier | exactly one |
| observed-at | ArtifactRevision | zero or one |
| of-kind | evidence kind | exactly one |

## extension points

The kinds above are a **registered vocabulary**, not a closed list (`ADR-0031`).

## Debt

**The inherited evidence model was never adopted** (`ISSUE-0018`). This
specification reconstructs its ranking from the prototypes without adopting its
confidence scoring, its status model, or its aggregation rules. Whether those
belong here is unresolved.

**Runtime observation is the highest-ranked kind and the least modelled**
(`ISSUE-0073`). Operational Knowledge sits outside the model entirely
(`ADR-0061`), yet the ranking places it at the top. That contradiction was
predicted to surface during B1 and this is where it surfaces — **it does not
block the specification**, because a citation can reference a runtime
observation without the model owning the observation.

**Nothing prevents circular support.** Assertion A citing B citing A is
constructible. Detecting it is mechanical and belongs to B5.
