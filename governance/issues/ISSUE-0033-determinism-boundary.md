---
id: ISSUE-0033
title: The boundary between deterministic compilation and non-deterministic agent work is undefined
type: question
status: open
severity: high
created: 2026-08-02
updated: 2026-08-02
blocks: [M2]
evidence:
  - governance/adr/ADR-0012-executable-framework-and-artifact-taxonomy.md
  - governance/adr/ADR-0011-engineering-os-is-a-knowledge-compiler.md
resolved-by: null
---

# ISSUE-0033 — The determinism boundary is undefined

## Statement

`ADR-0012` requires that every executable pipeline be deterministic: the same
authoritative inputs must always produce the same outputs.

Engineering OS is a framework for **AI** software engineering. Its skills are
executed by agents, and agent output is not deterministic. An impact analysis,
a reconstructed glossary, a proposed ontology module — none of these will be
byte-identical across two runs on the same inputs.

Where the deterministic pipeline ends and non-deterministic work begins is not
defined.

## Why it matters

If the boundary is drawn too wide, the determinism requirement is unenforceable
and will be quietly ignored — which is worse than not stating it. If drawn too
narrowly, agent-produced artifacts fall outside the artifact taxonomy entirely
and the build pipeline cannot reason about them.

This affects the artifact taxonomy vocabulary, which is an M2 deliverable. An
agent-authored impact analysis is not `authoritative` in the human-authored
sense, not `derived` in the deterministic sense, and neither `runtime` nor
`cached`.

## What we know

- `ADR-0011`'s pipeline — parsing, normalization, validation, semantic linking —
  is mechanical and can be fully deterministic.
- Agent work *produces authoritative assets*; the compiler *consumes* them. That
  suggests the boundary is the compiler's input edge: agents write authoritative
  artifacts, the pipeline deterministically compiles them.
- Under that reading, an agent-authored artifact becomes authoritative **once
  reviewed and committed**, and its non-determinism is irrelevant because it is
  now a fixed input.

That reading is coherent and is the most likely answer, but it has not been
confirmed, and it leaves a real question open: does an agent-authored artifact
need a distinct status before review?

## Open sub-questions

- Is there a fifth artifact kind for agent-produced, not-yet-reviewed output?
- Does the taxonomy need to record *who* authored an artifact, not only how?
- Can a generator invoke an agent? If so, that generator is not deterministic
  and `ADR-0012` forbids it — is that intended?

## Resolution criteria

An ADR stating exactly which stages must be deterministic, and how
agent-produced artifacts are classified in the taxonomy.
