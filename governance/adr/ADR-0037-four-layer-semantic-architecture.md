---
id: ADR-0037
title: The four-layer semantic architecture; the Metamodel is Layer A
status: accepted
date: 2026-08-02
supersedes: ADR-0014
superseded-by: null
resolves: [ISSUE-0031, ISSUE-0055]
related: [ADR-0010, ADR-0012, ADR-0035, ADR-0036, ADR-0038, ISSUE-0056]
---

# ADR-0037 — The four-layer semantic architecture

**This completes the architecture.** Every artifact in Engineering OS belongs to
exactly one of four semantic layers. It supersedes `ADR-0014`, whose three tiers
become layers B, C and D.

## Context

`ISSUE-0055` asked where the Metamodel lives and whether it is Layer A or Layer
B. `ISSUE-0031` asked what Engineering OS's own `model/` contains. Both were
recorded as the same question from opposite sides.

Two overlapping schemes were also in use: `ADR-0010`'s Layer A / Layer B
(methodology versus knowledge model) and `ADR-0014`'s three tiers (authoritative
/ canonical / derived).

## Decision

**The Engineering OS Metamodel is Layer A.** It belongs to Engineering OS
itself, and **defines the semantic language used to describe every Engineering
OS repository**.

Every adopting repository owns its own knowledge model (Layer B), but **that
knowledge model is expressed using the Engineering OS Metamodel**.

### The four layers

| Layer | Name | Defines |
|---|---|---|
| **A** | Engineering OS Metamodel | **the language** |
| **B** | Repository Knowledge Model | **a specific domain**, using that language |
| **C** | Canonical Knowledge Model | compiler-generated semantic representation of Layer B |
| **D** | Derived Projections | Knowledge Explorer, documentation, Registry Projections, search, Knowledge Packages, validation reports, future AI interfaces |

```text
Engineering OS
    model/
        metamodel/
            ArtifactType · RegistrySpecification · RegistryProjection ·
            Policy · Workflow · Skill · Capability · StateMachine ·
            Vocabulary · Ontology · Concept · AcceptanceRecord ·
            KnowledgePackage · …
                 ↓
        Knowledge Compiler
                 ↓
        Repository Canonical Knowledge Model
                 ↓
        Knowledge Explorer · Knowledge Packages · Indexes ·
        Documentation · Validation · Search
```

**Every artifact in Engineering OS belongs to exactly one layer.**

### Metamodel ownership

- **Authored inside the Engineering OS repository**, at `model/metamodel/`.
- An **authoritative artifact**.
- **Versioned with Engineering OS.**
- Evolves through the **same governance process** as every other authoritative
  artifact.
- **Adopting repositories never modify the metamodel. They instantiate it.**

### ISSUE-0031 is resolved by the same decision

Engineering OS's own `model/` contains `metamodel/`. The metamodel is the core
of the self-model, because **Engineering OS's domain is how systems are
described**. M11's self-model is therefore largely the metamodel rather than a
separate body of work.

## What survives from ADR-0014

The knowledge-compiler principle in full: the compiler stages (parsing,
normalization, validation, semantic linking), the rule that no consumer parses
authoritative assets directly, the absence of any privileged consumer, the
canonical model never being hand-edited and never living inside `model/`, and
the artifact taxonomy from `ADR-0012`.

`ADR-0014`'s three tiers are preserved exactly, renamed as layers **B**, **C**
and **D**. What is added is Layer A above them.

## Correction to ADR-0010

`ADR-0010` used "Layer A" for the methodology and "Layer B" for the knowledge
model. **Layer A is redefined here as the Metamodel.** `ADR-0010`'s substantive
decision — knowledge is repository-local, environments federate — is untouched
and remains `Active`; only its layer terminology is superseded by this scheme.

## Alternatives considered

**The metamodel as Layer B of the Engineering OS repository only.** Rejected:
every adopting repository's Layer B must conform to it, so it cannot be one
repository's local knowledge. That is precisely what makes it the language rather
than an instance.

**The metamodel in `shared/`, shipped as methodology.** Rejected: it is
genuinely the ontology of Engineering OS's own domain, and placing it outside
`model/` would deny that while gaining nothing — adopters receive it as part of
Engineering OS either way.

**Distribute the metamodel as a Knowledge Package.** The more elegant long-term
answer, and it would make the metamodel the first real use of federation.
Rejected for now: federation is M13 and M2 cannot wait eleven milestones.
Nothing here precludes adding it later.

## Consequences

### Positive

- **Two issues resolved by one decision**, and M2 is unblocked.
- Four clean layers, with every artifact classifiable into exactly one. This is
  the criterion `ADR-0038` makes mandatory.
- **`model/` for Engineering OS gets concrete content.** M11's self-model was an
  open-ended question; it is now largely the metamodel.
- Adopters get a shared semantic language without owning it — which is what
  makes Knowledge Packages (`ADR-0019`) interpretable across repositories at all.

### Negative

- **The old "Layer A = methodology" content has no layer.** `shared/`, `skills/`,
  `workflows/`, `templates/`, `schemas/` and `governance/` were Layer A under
  `ADR-0010`. Layer A is now the Metamodel alone, and nothing says where they
  belong. `ISSUE-0056`.
- **"Layer" is redefined**, which is the sixth terminology change in this
  project — and the first that redefines existing terms rather than splitting an
  overloaded one. A reader of `ADR-0010` will find the old meaning.
- Layer A lives inside `model/`, which `ADR-0010` framed as the repository-local
  knowledge model. For Engineering OS this is coherent, since its domain *is* the
  metamodel — but the shorthand "`model/` is Layer B" no longer holds for this
  repository, and that exception must be stated wherever it matters.
- Metamodel versioning is now load-bearing for every adopter, and no versioning
  policy exists (`ISSUE-0007`).

## Compliance

Every artifact belongs to exactly one layer. No adopting repository modifies the
metamodel. The metamodel is authored in `model/metamodel/`, versioned with
Engineering OS, and accepted through the normal workflow.
