---
id: ADR-0045
title: Front matter is interchange syntax; a Human Representation serializes semantic assignments
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0060]
related: [ADR-0001, ADR-0017, ADR-0042, ADR-0047, ISSUE-0063]
---

# ADR-0045 — Front matter is interchange syntax

## Context

`ADR-0042` established that artifacts are classified by Dimension Assignments —
semantic relationships represented in the Canonical Knowledge Model as graph
edges rather than embedded metadata.

`ISSUE-0060` recorded the collision that followed. `ADR-0017` guarantees that
authoritative artifacts stay usable without executing the compiler, and
`ADR-0001` requires the repository to be legible as memory. If classification
exists only in a compiled graph, a human reading an artifact cannot tell what
layer it belongs to, whether it is authoritative, or who owns it.

The issue posed the crux as: **is front matter a property, or a serialization of
a relationship?**

## Decision

**The authoritative repository must remain understandable without executing the
compiler.**

Therefore every authoritative artifact **may expose a Human Representation of
selected classifications**.

> **This representation is not the semantic source of truth. It is a canonical
> serialization of semantic assignments.**

```text
Dimension Assignment
        ↓
Canonical Serialization
        ↓
Artifact Front Matter
```

**The compiler reconstructs semantic relationships from that serialization. The
semantic relationship exists independently of the serialization.**

This preserves both principles:

- the repository remains human-readable;
- the Canonical Knowledge Model remains graph-based.

> **Front matter is an interchange syntax, not the semantic model.**

This distinction is part of the compiler architecture.

## Alternatives considered

**Front matter as the semantic model** — the reading `ADR-0042` rejected.
Rejected again for the same reason: classification would become a property of
the artifact, so reclassifying would mean editing it.

**Assignments as separate authored artifacts.** Rejected: it satisfies
`ADR-0042` cleanly but produces one artifact per artifact per dimension, and
leaves the reader of an artifact no better off than the graph-only option.

**Accept that classification is unreadable without the compiler**, amending
`ADR-0017`. Rejected: that guarantee is what keeps adoption cheap and the
repository legible as memory. Trading it for a representation convenience would
be the wrong side of the exchange.

## Consequences

### Positive

- **The crux is answered: serialization, not property.** Front matter can carry
  classification without classification being a property of the artifact —
  which is why both `ADR-0017` and `ADR-0042` survive intact.
- The compiler gains a defined input format for assignments, rather than having
  to discover them.
- It generalizes: the same reasoning applies to any human-facing encoding of a
  semantic relationship, which `ADR-0047` makes explicit.

### Negative

- **"May expose" and "selected classifications" leave the minimum unstated.**
  `ADR-0038` makes four classifications mandatory to know — layer, artifact
  kind, metamodel entity, compiler phase — and if serialization is optional or
  partial, an artifact can satisfy this ADR while remaining opaque on exactly
  those four. `ISSUE-0063`.
- Two encodings of one fact now exist. They cannot disagree in principle, since
  one is derived from the other — but nothing yet checks that the serialization
  in a file matches the assignment the compiler holds.
- "Canonical serialization" implies a specification that does not exist: what
  the syntax is, and how round-tripping is guaranteed.

### Neutral

- No existing front matter changes. What changes is what front matter *is*.

## Compliance

No document treats front matter as the semantic source of truth. Every
serialized classification corresponds to a Dimension Assignment. The compiler
reconstructs assignments from the serialization rather than defining them there.
