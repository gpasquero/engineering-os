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

**Highest allocated ID: `ACCEPT-0001`.** IDs are sequential and never reused.

## Index

| ID | Covers | Reviewer | Decision | Date |
|---|---|---|---|---|
| [ACCEPT-0001](ACCEPT-0001-bootstrap.md) | Bootstrap corpus at `2b6484f` | Project owner (`gpasquero`) | accepted | 2026-08-02 |

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

## Known gap

Whether an Acceptance Record itself requires acceptance is unresolved —
`ISSUE-0042`. `ACCEPT-0001` is asserted as the base case by `ADR-0022`, but the
general regress is not settled.
