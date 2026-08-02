---
id: GOVERNANCE-README
title: Governance
status: accepted
created: 2026-08-02
updated: 2026-08-02
---

# Governance

This directory is the persistent memory of the project.

Everything a future session needs to continue lives here. A session that reads
this directory in full can work without asking a question that was already
answered.

## Read in this order

Defined normatively in `session-protocol.md`. In summary:

1. `vision.md` — why this exists
2. `principles.md` — the non-negotiable rules
3. `glossary.md` — read before interpreting anything else
4. `repository-architecture.md` — what belongs where
5. `documentation-system.md` — how to record what you learn
6. `roadmap.md` — the milestone sequence
7. `build-state.md` — what exists today
8. `issues/index.md` — what is unresolved
9. `adr/README.md` — what was decided and why
10. `sessions/` — recent trajectory

## Contents

| Path | Purpose | Mutability |
|---|---|---|
| `vision.md` | Why the project exists | Mutable |
| `principles.md` | Non-negotiable rules | Mutable via ADR |
| `glossary.md` | Ubiquitous language | Mutable |
| `repository-architecture.md` | Target structure and directory contracts | Mutable |
| `documentation-system.md` | Document types, IDs, lifecycle | Mutable via ADR |
| `session-protocol.md` | How a session starts and ends | Mutable via ADR |
| `roadmap.md` | Milestone sequence | Mutable |
| `build-state.md` | Current status only | Overwritten each session |
| `inherited-decisions.md` | Pre-M1 decisions awaiting ADR context | Mutable |
| `adr/` | Decision records | Immutable once accepted |
| `issues/` | Open questions, inconsistencies, gaps, risks | Mutable until closed |
| `sessions/` | Append-only session journal | Immutable |
| `governance/design/` | Working proposals, not yet decisions | Mutable |

## The rule that makes this work

If information is missing, **create an issue — do not assume**.
