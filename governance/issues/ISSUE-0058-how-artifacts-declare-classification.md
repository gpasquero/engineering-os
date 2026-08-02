---
id: ISSUE-0058
title: How an artifact declares its classification, now that paths no longer imply it
type: question
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0039-layers-classify-artifacts-not-directories.md
  - governance/adr/ADR-0040-architectural-dimensions.md
  - governance/documentation-system.md
resolved-by: ADR-0042
---

# ISSUE-0058 — How an artifact declares its classification

## Statement

`ADR-0039` establishes that **the compiler classifies artifacts, not folders**,
and that repository layout is an implementation concern. `ADR-0040` establishes
that every artifact is classified along multiple independent dimensions.

Nothing says how an artifact's classification reaches the compiler.

## Why it matters

Path-based inference was the implicit mechanism — everything under
`governance/adr/` was an ADR, everything under `model/` was authoritative. That
inference is now explicitly disallowed as an architectural basis.

Front matter exists for `governance/` documents and is scheduled to extend
outward in M2. Whether it carries dimensional classification, and how much,
determines the shape of every contract in M2.

## Options

- **Front matter on every artifact.** Consistent with the existing documentation
  system, human-readable, and satisfies `ADR-0017`'s requirement that
  authoritative artifacts stay usable without the compiler. Verbose: eight
  dimensions on every file, most of them constant within an artifact type.
- **Declared per artifact *type*, in the metamodel or a registry.** An ADR is
  Governance / Authoritative / Input once, not on every ADR. Far less repetition,
  and it matches `ADR-0031`'s split between registry and instance. But an
  individual artifact could not then deviate — and `Lifecycle` and `Visibility`
  plainly vary per artifact.
- **Both, split by variance.** Type-level defaults for dimensions constant
  across a type; front matter for those that vary per artifact. Most likely
  correct, and it needs a rule for which dimension goes where.
- **A separate classification manifest.** Rejected on sight: it would separate an
  artifact from its own classification, and drift is guaranteed.

## The sharper question

**Which dimensions vary per artifact, and which are properties of the type?**

`Lifecycle` clearly varies — that is what a revision lifecycle is for.
`Semantic Layer` and `Artifact Taxonomy` look constant per type. `Ownership` and
`Visibility` are unclear, partly because they are undefined (`ISSUE-0057`).

Answering that determines the option above rather than the other way round.

## Resolution

`ADR-0042`. **All four options above are rejected**, because each treats
classification as a *property of the artifact*. That framing is the defect.

> **Artifacts do not "contain" dimension values. Artifacts are classified by
> Dimension Assignments** — explicit semantic relationships.

```text
Artifact → Dimension Assignment → Dimension → Dimension Value
```

Assignments are versioned; they may change without changing artifact identity;
dimensions evolve independently; and **validation applies to assignments, not to
artifacts**. The Canonical Knowledge Model represents dimensions as **graph
relationships rather than embedded metadata**.

The sharper question posed above — which dimensions vary per artifact and which
are properties of the type — dissolves: no dimension is a property of anything.
Variance is expressed by which assignments exist.

This is the **third** time an issue's own candidate answers were all rejected in
favour of reframing, after `ISSUE-0053` and `ISSUE-0056`.

**What remains open:** where assignments are *authored*. `ADR-0042` fixes their
representation in Layer C, which is derived and cannot be a source.
`ISSUE-0060`, which also records the tension with `ADR-0017`'s guarantee that
authoritative artifacts stay readable without the compiler.
