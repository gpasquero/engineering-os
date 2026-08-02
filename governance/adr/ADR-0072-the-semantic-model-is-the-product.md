---
id: ADR-0072
title: The Canonical Knowledge Model is the primary product; everything else is a projection
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0014, ADR-0016, ADR-0047, ADR-0052, ADR-0061]
---

# ADR-0072 — The semantic model is the product

## Context

`SESSION-0026` produced the first session in which the compiler **produced
architectural knowledge rather than validating repository consistency.**

The distinction is not a nuance:

> **A validator answers: "Is this repository correct?"**
>
> **A compiler answers: "What knowledge exists in this repository?"**

Every check this project has built until now answered the first question.
`tools/compile.py` answers the second, and the difference changes what the
repository is *for*.

## Decision

**The compiler is not validating documents. It is constructing an executable
semantic model.**

**That semantic model — the Canonical Knowledge Model — is the primary product of
the repository.**

Everything else is a projection of it:

```text
                Canonical Knowledge Model
                          │
   ┌──────────┬───────────┼───────────┬──────────────┐
  OWL      Explorer     graphs    Registry        future
                                 Projections   documentation
```

**OWL, the HTML Explorer, Markdown projections, registries, search indexes and
all future documentation are projections.** None is the product. None is
authoritative over the model.

### What this reorders

`ADR-0052` already established the compilation hierarchy — *Authoritative
Semantic Model → Canonical Knowledge Model → Projection*. This decision states
what that hierarchy is **for**, and the consequence it had been carrying without
stating:

- The authoring sources are **input**, not the deliverable.
- The Canonical Knowledge Model is the deliverable.
- **A projection is never a source of truth**, however convenient it is to read.

`ISSUE-0037` — hand-maintained projections — stops being an operational
inconvenience under this decision and becomes an architectural violation: a
hand-maintained projection is a projection with no model behind it.

### What it does not change

**Authoring stays human and Markdown stays readable** (`ADR-0017`). The model is
the product; the sources are still written by people, and must still be usable
without executing the compiler.

## Alternatives considered

**Leave the distinction implicit.** Rejected: it was implicit for twelve
sessions and produced five hand-maintained registers, each of which is a
projection nobody recognised as one.

**Declare the Markdown authoritative and the model derived.** Rejected. It is the
current *authoring* arrangement and it is not an ordering of authority: the
Markdown is a serialization of assertions, and the model is what those assertions
mean (`ADR-0045`, which said the same thing about front matter).

**Declare the OWL the product.** Rejected — it binds the deliverable to one
formalism. OWL is a projection, and `ADR-0068` and `ADR-0066` both turned on
Engineering OS not being defined by what OWL can express.

## Consequences

### Positive

- **It settles the question `FINDINGS.md` left open** — whether Markdown or OWL
  is authoritative once the compiler exists. Neither. Both are projections of the
  model; the Markdown is additionally the authoring form.
- Every future output has an obvious place: it is a projection, and it is
  generated.
- **It gives `ISSUE-0037` a principled resolution** rather than a tooling one.
- It makes the value of the repository independent of its file formats.

### Negative

- **Most of the repository is now formally a projection that is not generated.**
  Four governance indexes, the ADR corrections table, and the metamodel ontology
  itself are hand-maintained. This decision does not fix them; it reclassifies
  them as debt of a more serious kind.
- The Canonical Knowledge Model currently covers thirteen example nodes and none
  of the governance corpus. **The declared product barely exists.**

### Neutral

- No entity changes.

## Compliance

Every generated artifact declares itself derived (`ADR-0012`). No projection is
edited by hand. New outputs are added as projections of the Canonical Knowledge
Model, never as parallel sources.
