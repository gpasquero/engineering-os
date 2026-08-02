---
id: ISSUE-0034
title: Whether model/ is authoritative input or the compiled canonical model is undefined
type: question
status: resolved
severity: blocking
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0011-engineering-os-is-a-knowledge-compiler.md
  - governance/adr/ADR-0010-repository-local-knowledge-ownership.md
  - governance/adr/ADR-0012-executable-framework-and-artifact-taxonomy.md
resolved-by: ADR-0014
---

# ISSUE-0034 — Is `model/` authoritative input or compiled output?

## Statement

`ADR-0010` establishes `model/` as the repository's knowledge model.

`ADR-0011` establishes that authoritative assets are **compiled into** a
canonical knowledge model, which is the primary product of compilation.

These two statements can be reconciled in two incompatible ways, and nothing
chooses between them:

**Reading A — `model/` is authoritative input.** Humans and agents author
ontology, glossary and specifications in `model/`. The compiler consumes them
and emits the canonical knowledge model as a *derived* artifact somewhere else.
`model/` is the source; the canonical model is a build output.

**Reading B — `model/` is the canonical model.** `model/` *is* the compiled
output, and the authoritative assets are something upstream of it.

## Why it matters

`model-spec/` is an M2 deliverable and specifies the structure of `model/`. Its
design depends entirely on which reading is correct — a source tree and a
compiler output tree have different structures, different version-control
policies, and opposite editing rules.

Under `ADR-0012` this determines whether `model/` is `authoritative` or
`derived`, which in turn determines whether editing it by hand is normal
practice or forbidden.

It is marked `blocking` because building `model-spec/` under the wrong reading
would have to be redone entirely.

## What we know

- The inherited `reconstruct-system-knowledge` prototype treats `model/` as the
  place agents *write* reconstructed knowledge, which points to Reading A.
- `ADR-0011` says the canonical model is "the internal representation of the
  system", and internal representations are normally build artifacts, not
  hand-edited trees — which also points to Reading A, with the canonical model
  living outside `model/`.
- But `ADR-0010` describes `model/` as what a repository *owns*, and ownership
  language fits a source tree better than a build output.

Reading A is the more likely intent. It is not confirmed, and the two ADRs can
be read either way as written.

## Open sub-questions

- If Reading A: where does the compiled canonical model live, and is it
  committed to version control?
- Is a Knowledge Package (`ISSUE-0029`) an export of `model/` or of the compiled
  canonical model? The answer changes what federation actually exchanges.

## Resolution

`ADR-0014`. **Reading A.** Repository assets are the authoritative source of
knowledge; the canonical knowledge model is a derived artifact produced by the
Knowledge Compiler.

Three tiers are now explicitly named:

1. **Authoritative Knowledge Model** — the repository assets. `model/` belongs
   here: ontology source, glossary, invariants, workflows, capabilities,
   specifications, ADR references, traceability metadata. Artifact kind
   `authoritative`.
2. **Canonical Knowledge Model** — the compiler's internal representation. Never
   edited by humans, always reproducible, living under generated artifacts and
   **never inside `model/`**. Artifact kind `derived`. Serialization is an
   implementation decision.
3. **Derived Artifacts** — website, indexes, graph projections, reports, caches.

`ADR-0014` supersedes `ADR-0011`, which stated the compiler principle without
distinguishing the tiers — the omission that produced this issue.

`model-spec/` is now designable: it specifies an authoritative source tree.
