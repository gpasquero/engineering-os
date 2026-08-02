"""Engineering Discovery — production of a Candidate Engineering Model.

Discovery **performs reverse engineering**. The orchestration declarations say
how it is directed; these workers do the work (ADR-0107).

> **No worker writes authoritative knowledge.** Every output is a proposal
> carrying provenance, a support classification, and the worker and task that
> produced it (ADR-0105, ADR-0106).

Workers are of three kinds:

  * **deterministic extractors** — read a file, report what it says. Re-running
    reproduces the result exactly.
  * **bounded interpreters** — apply a NAMED rule to already-extracted
    assertions. Deterministic, and classified `S-inferred` because the rule may
    be sound and the instance wrong.
  * **gap identifiers** — report what is absent. Propose no knowledge.

**No language model participates in discovery production.** `ADR-0103` permits
becoming smarter and not less deterministic; a probabilistic interpreter is
admissible under `ADR-0105` and is not built here, so that the first candidate
model is reproducible.
"""
