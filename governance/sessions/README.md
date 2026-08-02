---
id: SESSION-INDEX
title: Session Journal
status: current
created: 2026-08-02
updated: 2026-08-02
---

# Session Journal

Append-only. One file per session, named `SESSION-NNNN-YYYY-MM-DD.md`.

A session log is **immutable once written**. It records what was true at that
point in time. Corrections belong in a later session log, not in an edit.

Session logs are the trajectory record: they answer "how did we get here",
which no other document does. `build-state.md` answers "where are we", and the
ADRs answer "why".

**Highest allocated ID: `SESSION-0015`.**

## Index

| ID | Date | Milestone | Summary |
|---|---|---|---|
| [SESSION-0001](SESSION-0001-2026-08-02.md) | 2026-08-02 | M1 | Repository bootstrap: architecture, documentation system, session protocol, 8 ADRs, 28 issues |
| [SESSION-0002](SESSION-0002-2026-08-02.md) | 2026-08-02 | M1 | Owner answers on `MANIFEST.yaml` and knowledge ownership; `ADR-0009`, `ADR-0010`; `ADR-0006` superseded; M2 unblocked |
| [SESSION-0003](SESSION-0003-2026-08-02.md) | 2026-08-02 | M2 | Knowledge compiler, executable framework, three manifests; `ADR-0011`–`ADR-0013`; `ADR-0009` superseded; M2 blocked again by `ISSUE-0032`, `ISSUE-0034` |
| [SESSION-0004](SESSION-0004-2026-08-02.md) | 2026-08-02 | M2 | Three-tier knowledge model, determinism boundary, governance-as-source, reference architecture; `ADR-0014`–`ADR-0017`; `ADR-0011` superseded; M2 unblocked |
| [SESSION-0005](SESSION-0005-2026-08-02.md) | 2026-08-02 | M2 | Acceptance confers authoritative status; Knowledge Packages as published interface; `ADR-0018`, `ADR-0019`; `ADR-0015` superseded; M2 blocked by `ISSUE-0038`, `ISSUE-0040`, `ISSUE-0041` |
| [SESSION-0006](SESSION-0006-2026-08-02.md) | 2026-08-02 | M2 | Taxonomy/lifecycle split, Acceptance Record spec, trust root `ACCEPT-0001`, governance self-hosting; `ADR-0020`–`ADR-0023`; `ADR-0018` superseded; M2 unblocked |
| [SESSION-0007](SESSION-0007-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0002` — first acceptance under the normal workflow; acceptance chain terminates at the record; every state belongs to one state machine; `ADR-0024`, `ADR-0025` |
| [SESSION-0008](SESSION-0008-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0003`; lifecycle belongs to a Revision; state machines are registered not enumerated; `ADR-0026`, `ADR-0027` |
| [SESSION-0009](SESSION-0009-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0004`; registry lives in `KNOWLEDGE-MANIFEST.yaml`; Modeling Policy as a first-class artifact type; `ADR-0028`, `ADR-0029` |
| [SESSION-0010](SESSION-0010-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0005`; normative artifact taxonomy; **Registry Pattern** named after four independent rediscoveries; `ADR-0030`, `ADR-0031` |
| [SESSION-0011](SESSION-0011-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0006`; Registry Specification vs Projection; `ProcessPolicy` governs Workflow; Knowledge Explorer defined; `ADR-0032`–`ADR-0034`. **M2 and M3 unblocked.** |
| [SESSION-0012](SESSION-0012-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0007`; **the Engineering OS Metamodel**; the Canonical Knowledge Model conforms to it; `ADR-0035`, `ADR-0036`. **M2 reordered — metamodel before compiler interface.** |
| [SESSION-0013](SESSION-0013-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0008`; **four-layer semantic architecture**; four questions per artifact type; `ADR-0037`, `ADR-0038`; `ADR-0014` superseded. `ISSUE-0031` and `ISSUE-0055` resolved together. |
| [SESSION-0014](SESSION-0014-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0009`; layers classify **artifacts, not directories**; **Architectural Dimensions**; `ADR-0039`, `ADR-0040`. `ADR-0037` corrected. |
| [SESSION-0015](SESSION-0015-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0010`; dimensions registered; **Dimension Assignments**; **three semantic levels**; `ADR-0041`–`ADR-0043` |

## Reading

At session start, read the most recent one to three logs. Reading the whole
journal is unnecessary; `build-state.md` and `issues/index.md` carry the
current picture.
