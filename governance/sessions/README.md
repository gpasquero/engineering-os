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

**Highest allocated ID: `SESSION-0022`.**

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
| [SESSION-0016](SESSION-0016-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0011`; independence ≠ isolation; **front matter as interchange syntax**; qualified names; **three representations**; `ADR-0044`–`ADR-0047` |
| [SESSION-0017](SESSION-0017-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0012`; `DimensionSpecification`; **dimensions are scarce**; **Definition → Instance → Assignment → Projection**; `ADR-0048`–`ADR-0050` |
| [SESSION-0018](SESSION-0018-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0013`; Dimension Review; **two orthogonal hierarchies**; **semantic vs compiler architecture**; `ADR-0051`–`ADR-0053`; `ADR-0050` superseded |
| [SESSION-0019](SESSION-0019-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0014`; **Engineering Gate**; questions belong to Gates; **Principle → Policy → Process**; `ADR-0054`–`ADR-0056`; `ADR-0038` superseded |
| [SESSION-0020](SESSION-0020-2026-08-02.md) | 2026-08-02 | M2 | `ACCEPT-0015`; **Naming Qualification**; Principles are semantic entities; **authored versus discovered knowledge**; `ADR-0057`–`ADR-0059` |
| [SESSION-0021](SESSION-0021-2026-08-02.md) | 2026-08-02 | B1 | `ACCEPT-0016`; Mechanical vs Interpretive Discovery; four knowledge categories; **`ADR-0062` — architecture through implementation**; 22 issues re-triaged as debt; **`model/metamodel/` created** |
| [SESSION-0022](SESSION-0022-2026-08-02.md) | 2026-08-02 | B1 | `ACCEPT-0017`; **Apache-2.0**; artifact identity model; inventory reclassified into five categories; **7 metamodel entities specified**; `ADR-0063`, `ADR-0064` |
| [SESSION-0023](SESSION-0023-2026-08-02.md) | 2026-08-02 | B1 | `ACCEPT-0018`; **descriptive vs operational entities** (`ADR-0065`); semantic backbone completed — 12 of 27 specified; **first OWL skeleton**, and six findings from writing it |
| [SESSION-0024](SESSION-0024-2026-08-02.md) | 2026-08-02 | B1 | `ACCEPT-0019`; **`RelationshipType` replaces `Relationship`** (`ADR-0066`); **the relationship is the design unit** (`ADR-0067`); operational family complete — 19 of 27; second OWL checkpoint; `ISSUE-0074` |
| [SESSION-0025](SESSION-0025-2026-08-02.md) | 2026-08-02 | B1 | `ACCEPT-0020`; **ordering is intrinsic or extrinsic** (`ADR-0068`); state machines specified; **the Specification/Instance pattern failed its second domain**; three generated graph views; 22 of 28 |
| [SESSION-0026](SESSION-0026-2026-08-02.md) | 2026-08-02 | B1 | `ACCEPT-0021`; **normalization not entity reduction** (`ADR-0069`); **the Specification criterion** (`ADR-0070`) resolving `ISSUE-0074`; **relationship vocabulary** (`ADR-0071`); **first end-to-end compilation** — CKM, OWL, graph, explorer |

## Reading

At session start, read the most recent one to three logs. Reading the whole
journal is unnecessary; `build-state.md` and `issues/index.md` carry the
current picture.