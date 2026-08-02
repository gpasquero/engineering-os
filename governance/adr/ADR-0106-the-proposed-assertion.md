---
id: ADR-0106
title: A Candidate Engineering Model and an Execution Observation are the same artifact at different scales
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: []
related: [ADR-0072, ADR-0081, ADR-0100, ADR-0101, ADR-0104, ADR-0105]
---

# ADR-0106 — The proposed assertion

## Context

`ADR-0105` establishes that Discovery produces a **Candidate Engineering Model**
that is reviewed before becoming authoritative.

`ADR-0101` established that Execution produces **Observations** that are
classified before entering the model — and **nothing applies the resulting
proposal.** That is the loop's unclosed step, named in every build state since
`SESSION-0036`.

**These look like two problems. They are one.**

## The observation

Strip both to their structure:

| | Produced by | Contains | Before entering |
|---|---|---|---|
| Candidate Engineering Model | discovery workers | claims about what a repository contains, with provenance | engineering review |
| Execution Observation (accepted) | execution workers | claims about what execution found, with provenance | governance gate |

**Both are sets of proposed assertions with provenance, produced by probabilistic
workers, requiring authorization before becoming knowledge.**

They differ in **scale** — thousands versus a handful — and in **occasion** —
onboarding versus change. **They do not differ in kind.**

## Decision

**The proposed assertion is the common unit**, and one mechanism handles both.

```text
discovery workers ─┐
                   ├→ proposed assertions → review → authoring sources → compiler → CKM
execution workers ─┘
```

### An accepted proposal becomes an authoring source

Not a direct model write. **An approved assertion is authored into the
repository and recompiled like everything else.**

This is what `SESSION-0036`'s log predicted before discovery was on the table:

> *An approved observation becomes an authored assertion, which recompiles like
> everything else. That keeps `ADR-0072` intact — the model is the product and
> the sources are the input.*

`ADR-0072` survives untouched: **the compiler remains the only thing that writes
the model, and it still writes from authoring sources.** What changes is that a
source may now originate from a worker rather than a person — after review.

### One mechanism, built once

The next build is **not** a discovery intake and a knowledge-update applier. It
is **one applier**: take approved proposed assertions, write them as authoring
sources, recompile.

Discovery gets its onboarding path and the loop closes, from the same code.

### What a proposed assertion must carry

| Field | Why |
|---|---|
| the assertion | the node or edge proposed |
| provenance | the exact source it came from (`ADR-0101`) |
| origin | which worker, which task, which run |
| intake outcome | `record` · `govern` · `reject` (`ADR-0101`, `ADR-0104`) |
| **what it would displace** | an assertion that contradicts an existing one is never additive |

**The last field is the one that makes review possible at scale**, because it
separates *new knowledge* from *changed knowledge*, and only the second requires
judgement about what was there before.

## Alternatives considered

**Two mechanisms, one per source.** Rejected — the reason for the decision. They
would diverge, and the divergence would be in what counts as authorized.

**Let discovery write authoritative sources directly, since a human reviews the
repository anyway.** Rejected: review of a diff is not review of an assertion.
A reviewer reading 3,000 generated lines is performing acceptance theatre, and
`ADR-0023`'s requirement that acceptance be real would be satisfied only
formally.

**Have the compiler consume candidate models as a second input class.** Rejected.
It would give the compiler two inputs with different authority, and every
downstream consumer would need to know which produced what — the exact confusion
`ADR-0072` exists to prevent.

## Consequences

### Positive

- **The next build is one mechanism instead of two**, and it closes the loop as a
  side effect of building onboarding.
- `ADR-0072` and `ADR-0081` are preserved without exception: one writer, one
  input class, one product.
- **It makes the review bottleneck concrete rather than vague**: the question is
  how to review proposed assertions at scale, and it is the same question in both
  cases.

### Negative

- **The review bottleneck is real and this decision does not solve it.** A
  candidate model for a 469-file repository may propose thousands of assertions.
  Batch acceptance — *accept every `evidence-discovered` proposal from this run* —
  is the obvious mitigation and **trades scrutiny for throughput**, which is
  exactly the trade `ADR-0023` was written to prevent. It is left unresolved
  deliberately rather than settled speculatively.
- **Writing authoring sources from proposals means workers shape the repository's
  text**, not only its model. A malformed generated source is a compiler input,
  and the parser's schema is now load-bearing in a way it was not.

### Neutral

- No existing artifact changes. Two planned mechanisms become one.

## Compliance

Discovery and execution both emit proposed assertions in the same shape. **One
applier writes approved assertions as authoring sources**, and the compiler is
unchanged. No component writes the Canonical Knowledge Model directly.
