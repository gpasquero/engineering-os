---
id: ACCEPT-INDEX
title: Acceptance Records
status: current
created: 2026-08-02
updated: 2026-08-02
related: [ADR-0021, ADR-0022, ADR-0023, ISSUE-0042]
---

# Acceptance Records

An Acceptance Record is the artifact that confers authoritative status. Without
one, a revision is not `Active` — whoever authored it, and whether or not it is
committed.

**Acceptance is an engineering decision, not a Git operation** (`ADR-0020`).

**Highest allocated ID: `ACCEPT-0045`.** IDs are never reused.

> **`ACCEPT-0033` and `ACCEPT-0035` are not allocated.** Each was skipped when
> the reviewer requested the next identifier: `ACCEPT-0034` while the highest was
> `0032`, and `ACCEPT-0036` while the highest was `0034`. The gaps are deliberate
> and documented in the records that follow them. Neither will be created.

## Index

| ID | Covers | Reviewer | Decision | Date |
|---|---|---|---|---|
| [ACCEPT-0001](ACCEPT-0001-bootstrap.md) | Bootstrap corpus at `2b6484f` | Project owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0002](ACCEPT-0002-session-0006-decisions.md) | `SESSION-0006` decisions at `aed6d89` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0003](ACCEPT-0003-session-0007-decisions.md) | `SESSION-0007` decisions at `d439084` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0004](ACCEPT-0004-session-0008-decisions.md) | `SESSION-0008` decisions at `51bed77` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0005](ACCEPT-0005-session-0009-decisions.md) | `SESSION-0009` decisions at `7af8f44` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0006](ACCEPT-0006-session-0010-decisions.md) | `SESSION-0010` decisions at `a87ce51` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0007](ACCEPT-0007-session-0011-decisions.md) | `SESSION-0011` decisions at `ef8e067` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0008](ACCEPT-0008-session-0012-decisions.md) | `SESSION-0012` decisions at `2d35b74` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0009](ACCEPT-0009-session-0013-decisions.md) | `SESSION-0013` decisions at `dd3d26e` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0010](ACCEPT-0010-session-0014-decisions.md) | `SESSION-0014` decisions at `c8e50a2` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0011](ACCEPT-0011-session-0015-decisions.md) | `SESSION-0015` decisions at `12692f0` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0012](ACCEPT-0012-session-0016-decisions.md) | `SESSION-0016` decisions at `875b853` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0013](ACCEPT-0013-session-0017-decisions.md) | `SESSION-0017` decisions at `1345bfc` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0014](ACCEPT-0014-session-0018-decisions.md) | `SESSION-0018` decisions at `206a7cd` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0015](ACCEPT-0015-session-0019-decisions.md) | `SESSION-0019` decisions at `4d1c8d0` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0016](ACCEPT-0016-session-0020-decisions.md) | `SESSION-0020` decisions at `ba530b5` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0017](ACCEPT-0017-session-0021-decisions.md) | `SESSION-0021` decisions and first Layer A artifacts at `926b0ee` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0018](ACCEPT-0018-session-0022-decisions.md) | `SESSION-0022` decisions, licence and metamodel batch at `b23b173` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0019](ACCEPT-0019-session-0023-decisions.md) | `SESSION-0023` decisions, semantic backbone and first OWL ontology at `7ee3b44` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0020](ACCEPT-0020-session-0024-decisions.md) | `SESSION-0024` decisions, operational family and second OWL checkpoint at `1fdc337` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0021](ACCEPT-0021-session-0025-decisions.md) | `SESSION-0025` decisions, ordering resolution and generated graph views at `e7a07b8` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0022](ACCEPT-0022-session-0026-decisions.md) | `SESSION-0026` decisions, normalization and first executable pipeline at `f2ba10c` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0023](ACCEPT-0023-session-0027-decisions.md) | `SESSION-0027` decisions, compiler phases and regression suite at `47eebe5` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0024](ACCEPT-0024-session-0028-decisions.md) | `SESSION-0028` decisions, compiler modularization and declarative validation at `c0b0b59` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0025](ACCEPT-0025-session-0029-decisions.md) | `SESSION-0029` decisions and the first vertical slice at `17ab3fd` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0026](ACCEPT-0026-session-0030-decisions.md) | `SESSION-0030` decisions and the semantic query API at `a55f5f6` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0027](ACCEPT-0027-session-0031-decisions.md) | `SESSION-0031` decisions and query-result hardening at `c655fd7` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0028](ACCEPT-0028-session-0032-decisions.md) | `SESSION-0032` — the external Kubernetes validation at `6d5da52` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0029](ACCEPT-0029-session-0033-decisions.md) | `SESSION-0033` — the Engineering Recommendation Engine at `0499e77` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0030](ACCEPT-0030-session-0034-decisions.md) | `SESSION-0034` — the Engineering Planning Engine at `f49b1a1` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0031](ACCEPT-0031-session-0035-decisions.md) | `SESSION-0035` — the Task Graph at `d4954eb` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0032](ACCEPT-0032-session-0036-decisions.md) | `SESSION-0036` — the Engineering Director runtime at `fe7a263` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0034](ACCEPT-0034-session-0037-decisions.md) | `SESSION-0037` — autonomy and the first real-repository run at `1003d57` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0036](ACCEPT-0036-session-0040-decisions.md) | `SESSION-0040` — two-stage Discovery and a refuted conclusion at `2a13b4c` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0037](ACCEPT-0037-session-0041-decisions.md) | `SESSION-0041` — acquisition stages and the first benchmark at `288a351` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0038](ACCEPT-0038-session-0042-decisions.md) | `SESSION-0042` — Discovery Skills and the blind benchmark at `5c0781f` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0039](ACCEPT-0039-session-0043-decisions.md) | `SESSION-0043` — the complete acquisition lifecycle at `2924fd5` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0040](ACCEPT-0040-session-0044-decisions.md) | `SESSION-0044` — drift routing, the skill catalog and the product test at `20c7502` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0041](ACCEPT-0041-session-0045-decisions.md) | `SESSION-0045` — Stack Profiles and the first generalization benchmark at `92a0248` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0042](ACCEPT-0042-session-0046-decisions.md) | `SESSION-0046` — the product metric and the skill taxonomy at `d82ec43` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0043](ACCEPT-0043-session-0047-decisions.md) | `SESSION-0047` — the longitudinal experiment at `cebb2b9` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0044](ACCEPT-0044-session-0048-decisions.md) | `SESSION-0048` — Understanding Retention and the diagnosis at `185db71` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |
| [ACCEPT-0045](ACCEPT-0045-session-0049-decisions.md) | `SESSION-0049` — semantic preservation, 100 % retention at `d6d3bef` | Project Owner (`gpasquero`) | accepted | 2026-08-02 |

## The three conditions

A revision may be accepted only when all three hold (`ADR-0020`):

1. **Explicit reviewer approval.**
2. **Traceability** to the motivating issue, ADR or requirement.
3. **Successful validation of all applicable deterministic checks.**

On condition 3: *applicable* is the operative word. Where no deterministic
validator exists, none are applicable and the condition is satisfied. This is
not an exception — it is the normal reading, and it means the acceptance model
never changes as tooling arrives (`ADR-0021`).

## Rules

- **Self-certification is prohibited.** An author does not accept their own
  work, and Engineering OS never assumes an AI agent may do so. Only an
  explicitly `Active` governance policy could ever permit it (`ADR-0023`).
- **Exactly one retrospective acceptance exists** — `ACCEPT-0001`, the trust
  root. No second one is ever created (`ADR-0022`).
- Governance policies follow this same lifecycle, and the currently `Active`
  policy always governs the acceptance of the next revision. Governance is
  self-hosting but never self-certifying (`ADR-0023`).
- Use `_template.md`.

## The chain terminates here

**An Acceptance Record is never itself subject to an additional Acceptance
Record** (`ADR-0024`). It derives its authority from the decision it records.
This is the base case of the acceptance model, not an exception.

One consequence is worth stating plainly: an Acceptance Record is the single
artifact that nothing else checks. The `reviewer` field must therefore always
name a real, askable party.
