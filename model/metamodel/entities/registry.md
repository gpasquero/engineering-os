---
id: METAMODEL-Registry
title: Registry
status: draft
created: 2026-08-02
updated: 2026-08-02
semantic-layer: A
entity-family: operational
artifact-kind: authoritative
established-by: [ADR-0031, ADR-0032, ADR-0070, ADR-0083]
---

# Registry

**A declared, extensible set whose membership rule is stated rather than
implied.**

> **Not `RegistrySpecification`.** A registry has no instances that exist
> independently of the repository, so there is nothing for a Specification to be
> a specification *of* (`ADR-0070`).

## What new semantics does this introduce?

**Governed extensibility.** A registry is the only construct that can say *this
set is open, and here is exactly how it opens.*

`Vocabulary` is a closed enumeration. `Dimension` is an axis. Neither can state a
membership rule that a third party may satisfy without modifying the framework —
which is the whole of what makes Engineering OS extensible without being forkable
(`ADR-0041`).

## What the compiler does differently

It stops knowing file shapes. Before this entity the compiler had three ad-hoc
readers; it now implements three **extraction kinds** and learns which registries
exist from a declaration (`ADR-0083`).

**This is the entity `ADR-0075` predicted would be needed**, and it was needed for
the reason predicted: the compiler was reading registries by regex.

## identity

A stable identifier, unique within the repository.

## purpose

To make *what may be added, and by whom* a declared property rather than a
property of whatever code happens to read the file.

Every registry declares six things:

| Field | States |
|---|---|
| `id` | the registry's identifier |
| `registers` | what kind of thing it holds |
| `source` | the authoritative artifact |
| `extraction` | how entries are read |
| **`membership`** | what makes an entry a member |
| **`extension`** | how an adopting repository may add to it |

**`membership` and `extension` are the fields that matter**, and they were
required by `ADR-0032` for seventeen sessions without a single registry declaring
either.

## Specification and projection

> **A Registry Specification is authoritative; a Registry Projection is derived**
> (`ADR-0032`).

The declaration is the specification. Any rendered index of members is a
projection, and **hand-maintaining one is the failure `ISSUE-0037` records.**

## ownership

Framework registries are owned by Engineering OS. An adopting repository declares
its own, and extends framework registries **only as their `extension` field
permits**.

## lifecycle owner

`ArtifactRevisionLifecycle`.

## authoritative representation

A declaration in `model/metamodel/registries.md`.

## derived representations

- A Registry Projection per registry — an index of current members.
- Coverage reports: registries whose members no artifact references.

## relationships

| Relationship | Target | Cardinality |
|---|---|---|
| contains | any registered entry | zero or more |
| defined-in | Artifact | exactly one, its source |
| governed-by | GovernancePolicy | zero or more |
| validated-by | ValidationRule | zero or more |

## extension points

**Registries are the extension mechanism**, so this entity is where extensibility
is defined rather than something that has extension points of its own.

## Debt

**No Registry Projection is generated.** The specification/projection
distinction is declared and only one half exists.

**`extraction` is a closed vocabulary of three kinds** covering four registries.
That the shapes are not arbitrary is weak evidence from a small sample.

**Nothing validates a registry against its own membership rule.** `membership` is
prose; the extractor decides membership in practice. **The rule and the mechanism
can disagree and nothing would notice** — which is the same gap
`Invariant.enforced-at` records, reproduced one level up.
