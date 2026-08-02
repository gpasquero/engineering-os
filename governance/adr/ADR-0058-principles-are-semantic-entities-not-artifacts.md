---
id: ADR-0058
title: Principles are semantic entities extracted by the compiler, not authored artifacts
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0070]
related: [ADR-0029, ADR-0034, ADR-0054, ADR-0056, ADR-0059, ISSUE-0071]
---

# ADR-0058 — Principles are semantic entities, not artifacts

## Context

`ADR-0056` established Principles as the first level of engineering knowledge,
with three examples that are currently `Active` ADRs. `ISSUE-0070` asked whether
Principle is a first-class artifact type, and recorded the tension: `ADR-0029`'s
argument applies with more force to principles than to policies, but a fourth
normative artifact type runs against `ADR-0049`'s scarcity discipline.

Both horns assumed a Principle is a document.

## Decision

**Do not introduce Principle as another normative artifact type.**

> **Principles are not artifacts. They are semantic relationships that emerge
> from accepted architectural knowledge.**

```text
ADR        establishes   Principle
Principle  motivates     Policy
Policy     governs       Process
Process    produces      Artifacts
```

**Principles belong to the semantic model, not to the document taxonomy.** They
are represented in the Engineering OS Metamodel as **first-class semantic
entities** rather than as authored documents.

**The Knowledge Compiler extracts Principles from authoritative artifacts** and
makes them explicit inside the Canonical Knowledge Model. The Knowledge Explorer
then allows **navigation by Principle independently of the documents that
established them**.

This preserves a small document taxonomy while making Principles explicit and
queryable.

## Alternatives considered

All three options recorded in `ISSUE-0070` treat a Principle as something
authored:

**A first-class artifact type.** Rejected: it adds a fourth normative type
against `ADR-0049`'s scarcity discipline, and it would require someone to decide
when a principle has been established rather than letting it emerge.

**A role an ADR plays, marked by a dimension assignment.** Rejected: it leaves
principles inside a corpus `ADR-0029` says is history, and one principle
frequently emerges across several ADRs rather than being owned by one.

**Content within a Policy.** Rejected: a principle can exist before any policy
implements it — the Registry Pattern did for five sessions — and this reading
would make it unnameable until then.

## Consequences

### Positive

- **The document taxonomy stays small while principles become queryable.** Both
  goals in `ISSUE-0070` are satisfied instead of traded off.
- A principle established across several ADRs is one entity, not a
  cross-reference. The Registry Pattern emerges from `ADR-0027`, `ADR-0028`,
  `ADR-0031` and `ADR-0032`; as a semantic entity it is one node.
- **Navigation by Principle independently of the documents** is exactly the kind
  of view no authored document could provide, which makes it a real
  justification for the compiler rather than a restatement.
- It resolves `ADR-0056`'s heterogeneity: its three levels mixed one semantic
  entity with two artifact kinds, and now the difference is stated.

### Negative

- **"Extracts" carries the weight, and nothing says how.** If an ADR must declare
  the principles it establishes, extraction is parsing. If the compiler infers
  them, extraction is inference — which collides with `ADR-0020`'s determinism
  requirement and with the rule that a generator may never invoke an agent.
  `ISSUE-0071`.
- A Principle is `derived`, so it is never accepted. Its trust comes entirely
  from the accepted ADRs it is extracted from — sound, but it means a
  mis-extracted principle carries the authority of artifacts that never asserted
  it.
- Principles cannot be corrected directly. Fixing one means changing what the
  ADRs say or how extraction works, which is a longer loop than editing a
  document.

### Neutral

- `ADR-0056`'s chain is preserved and given relationship names: *establishes*,
  *motivates*, *governs*, *produces*.

## Compliance

No Principle is an authored document. Every Principle in the Canonical Knowledge
Model traces to the authoritative artifacts that establish it. The document
taxonomy gains no new normative type.
