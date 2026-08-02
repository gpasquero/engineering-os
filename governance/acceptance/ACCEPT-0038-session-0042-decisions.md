---
id: ACCEPT-0038
artifact: SESSION-0042 — Discovery Skills and the blind benchmark
artifact-revision: 5c0781fdfc14d40f200a07e5fc07d521b5e6163d
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0113]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0038 — Discovery Skills and the blind benchmark

## Artifact

The work of `SESSION-0042`, at revision
**`5c0781fdfc14d40f200a07e5fc07d521b5e6163d`**.

Scope: Discovery Skills as engine-independent contracts, the blind benchmark
run, the six contract defects it surfaced, the extractor fix, and the comparison
harness.

**Sequence continuous.** `ACCEPT-0038` follows `ACCEPT-0037`.

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **The Discovery Worker benchmark is concluded.** It answered the architectural
  question it was created to answer: **deterministic and probabilistic workers
  contribute different classes of engineering knowledge, and Engineering OS
  should support both.**
- **Further benchmark work stops** unless a real onboarding failure reopens the
  question.
- **The product bottleneck has moved.** Discovery is no longer the research
  target; **Brownfield Knowledge Acquisition is.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

`ADR-0113` establishes the Skill contract; the blind run tested it and produced
six contract defects, four fixed in the same session.

## Condition 3 — validation summary

264 records, 17 fixtures, 19 registries, golden outputs for six emitters, both
query engines in agreement, generation deterministic.

## Exceptions

None.

## Notes

The reviewer elevates the Mechanical Model — *"do not think of it as an
intermediate file; it is the reproducible engineering observation layer upon
which all interpretation operates"* — and names Brownfield Acquisition as a
product rather than an implementation detail.

**The complete lifecycle was built and run in the accepting session**, against a
real commit from `ai-desk`'s history. Recorded in
`external/ai-desk-lifecycle/LIFECYCLE.md`.
