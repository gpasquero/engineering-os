---
id: ACCEPT-0046
artifact: SESSION-0050 — the benchmark begins measuring Guidance
artifact-revision: a0f3316
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0137, ADR-0138, ADR-0139, ADR-0140, ADR-0141]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0046 — Guidance measured, Discovery declared mature

## Artifact

The work of `SESSION-0050`, at revision **`a0f3316`**.

Scope: `ADR-0137`–`ADR-0141`, `tools/guidance.py`, Guidance Preservation in the
frozen suite, the model-wide-step check, and `LIFECYCLE.md`.

**Sequence continuous.**

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **`ADR-0140` is an important strategic decision.** Deterministic Discovery is
  no longer the bottleneck. **Do not continue investing in deterministic
  onboarding unless a benchmark demonstrates a clear deficiency.** The
  architecture should now assume Mechanical Discovery is a mature capability.
- **`ADR-0141` also feels correct.** The Repository Lifecycle is becoming the
  primary product workflow. **Customers will experience the lifecycle. Very few
  will ever care about compiler phases. That is a healthy architectural
  inversion.**
- **Brownfield Onboarding should now become the primary research area.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

Five decisions, each implemented in the session that recorded it, and a Guidance
measurement that found a defect on its first run.

## Condition 3 — validation summary

308 records, 17 fixtures, 20 registries, both query engines in agreement, the
frozen suite rerun with its baseline preserved.

## Exceptions

None.

## Notes

The reviewer named a further transition and four directions, recorded as
decisions:

> Until now Engineering OS has mostly answered *"what do we know about this
> system?"* The next phase is **"what should an engineer do next?"** That is a
> different product. **Engineering Guidance is becoming the center.**

- the Onboarding Skill produces **two** deliverables — a Candidate Engineering
  Model and an **Engineering Review** (`ADR-0142`);
- **five responsibilities stay sharply separated** — extract, hypothesize,
  authorize, preserve, consume (`ADR-0143`);
- onboarding is optimized for **reviewer efficiency**, and the benchmark that
  ultimately matters **requires humans and may not be simulated** (`ADR-0144`);
- **Human Curation is a first-class product** and a user-experience problem
  (`ADR-0145`).
