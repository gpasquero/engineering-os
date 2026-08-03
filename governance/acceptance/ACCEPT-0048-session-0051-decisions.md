---
id: ACCEPT-0048
artifact: SESSION-0051 — Human Curation as a product
artifact-revision: 33dea67
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0142, ADR-0143, ADR-0144, ADR-0145, ADR-0146]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0048 — MVP closure directive

## Artifact

The work of `SESSION-0051`, at revision **`33dea67`**.

Scope: `ADR-0142`–`ADR-0146`, `tools/curate.py`, and the
`DS-brownfield-onboarding` skill contract.

**Sequence gap: `ACCEPT-0047` was not allocated.** The reviewer is the
register's authority and requested this identifier directly. The gap is
documented here and in `governance/acceptance/README.md`; a reference to it is
not dangling.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer, together with a change of objective:

> Engineering OS has reached sufficient architectural maturity for an MVP. From
> this point forward, **enter Research Freeze.**
>
> **The goal is no longer to improve the architecture. The goal is to make
> Engineering OS installable, understandable and usable by someone who did not
> build it.**

`README.md` becomes the primary deliverable, written for a third-party engineer
who has never seen the project and will not ask its authors for missing steps.

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

Five decisions, each implemented in the session that recorded it. The closure
directive is recorded as `ADR-0147`, which the reviewer authorised as the final
ADR of the research phase.

## Condition 3 — validation summary

`python tools/check.py` — 12 checks. `python tools/smoke.py` — the documented
MVP path, end to end, in a clean temporary workspace.

## Exceptions

**The MVP is not complete.** Thirteen of fourteen checklist items are done; the
fourteenth — *one third-party engineer completes the flow without private
guidance* — cannot be satisfied from inside this repository and governs the
rest.

## Notes

The sixteen-step MVP journey and the twenty-three README sections were specified
by the reviewer and are recorded in `ADR-0147` and `docs/mvp-checklist.md`.

**No further ADR is written** unless a documented workflow cannot be completed,
a third-party user hits a blocker, or correctness or trust would be
compromised.
