---
id: ADR-0063
title: Engineering OS is licensed under Apache-2.0
status: accepted
date: 2026-08-02
supersedes: null
superseded-by: null
resolves: [ISSUE-0011]
related: [ADR-0001]
---

# ADR-0063 — Apache-2.0

## Context

`ISSUE-0011` recorded that the repository is published at
`github.com/gpasquero/engineering-os` with visibility `PUBLIC` and no licence
file. Under default copyright nobody may legally copy, modify or reuse it — the
opposite of the apparent intent, and worse than either a deliberate licence or a
private repository.

## Decision

**This project is intended to be publicly reusable.**

The repository is licensed under the **Apache License 2.0**.

SPDX identifier: **`Apache-2.0`**

### Because

- it permits commercial and non-commercial use;
- it permits modification and redistribution;
- it includes an **explicit patent grant**;
- it is appropriate for a framework expected to contain specifications, tooling
  and executable code.

### What is added

- `LICENSE` — the canonical Apache-2.0 text.
- SPDX headers **where appropriate, once executable source code exists**.
- A short licensing section in `README.md`.

**Headers are not retroactively added to Markdown governance documents.**

## Alternatives considered

**MIT.** Permissive and shorter, but no patent grant. For a framework expected
to ship tooling and executable code, the explicit grant is the reason to prefer
Apache-2.0.

**A copyleft licence.** Rejected: it would constrain adopting repositories,
which are expected to contain proprietary domain knowledge. Engineering OS is
applied *to* systems it does not own.

**Remain unlicensed.** Rejected — it is the state `ISSUE-0011` identified as
worse than either alternative.

## Consequences

### Positive

- The repository becomes legally reusable, which is what publishing it publicly
  was for.
- The patent grant covers the compiler and tooling that M9 will produce.
- Adopting repositories are unconstrained in what they build on top.

### Negative

- Apache-2.0 requires attribution and a NOTICE of modifications, which is a real
  obligation on adopters — modest, and the price of the patent grant.
- SPDX headers become an ongoing convention once code exists, and nothing yet
  enforces them.

## Compliance

`LICENSE` contains the canonical Apache-2.0 text. Executable source files carry
an SPDX header. Markdown governance documents do not.
