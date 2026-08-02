---
id: ACCEPT-0043
artifact: SESSION-0047 — the longitudinal experiment and the Understanding System
artifact-revision: cebb2b9
reviewer: Project Owner (gpasquero)
acceptance-date: 2026-08-02
decision: accepted
related-adrs: [ADR-0123, ADR-0124, ADR-0125, ADR-0126]
related-issues: []
supersedes: null
superseded-by: null
signatures: []
---

# ACCEPT-0043 — The project became falsifiable

## Artifact

The work of `SESSION-0047`, at revision **`cebb2b9`**.

Scope: `ADR-0123` (superseding `ADR-0122`), `ADR-0124`, `ADR-0125`, `ADR-0126`,
`tools/longitudinal.py`, and `external/ai-desk-longitudinal/LONGITUDINAL.md`.

**Sequence continuous.**

## Decision

**`accepted`.** These revisions are now `Active`.

## Rationale

As given by the reviewer:

- **One of the strongest validation sessions so far — not because Engineering OS
  improved, but because it became falsifiable.** For the first time the project
  measured one of its own central promises over time and obtained a mixed
  result.
- **Keep that experiment exactly as it is. Do not optimize it away.**
- `ADR-0123` is the correct product definition, and the experiment demonstrates
  something further: **Engineering Understanding is not equivalent to
  Engineering Knowledge.** The model accumulated knowledge; understanding did
  not improve.
- **The most important observation is not the percentage.** It is the sentence
  *"the model became larger without becoming more useful"* — **the first product
  KPI that actually matters.**

## Condition 1 — reviewer approval

Approval given explicitly by the Project Owner. Author and reviewer are
different parties, as `ADR-0023` requires.

## Condition 2 — traceability

Four decisions, each implemented in the session that recorded it. `ADR-0122` is
superseded with symmetry recorded on both records.

## Condition 3 — validation summary

287 records, 17 fixtures, 20 registries, both query engines in agreement, and a
reproducible ten-commit experiment whose result is recorded rather than
improved.

## Exceptions

None. The `C3` semantic asymmetry was found and deliberately not fixed in the
session that discovered it.

## Notes

The reviewer reframed the next step and set the phase that follows:

> The objective is no longer *"What can Continuous Acquisition infer?"* It is
> **"What understanding should Continuous Acquisition preserve without requiring
> another onboarding?"** Inference is an implementation mechanism. **Preserved
> understanding is the product capability.**
>
> **Preserve semantics first. Infer second.**

And the North Star, recorded as `ADR-0131`:

> **Can Engineering OS preserve engineering understanding as software evolves?**
> That is the promise customers will actually evaluate.

Also recorded: `ADR-0127` (knowledge is not understanding), `ADR-0128`
(Understanding Retention), `ADR-0129` (the longitudinal suite is permanent) and
`ADR-0130` (preserve semantics first).
